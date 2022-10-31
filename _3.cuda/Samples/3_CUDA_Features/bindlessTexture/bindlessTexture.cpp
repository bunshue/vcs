/*
  Bindless Texture/Surface

  This sample generates a few 2D textures and uses cudaTextureObjects to
  perform pseudo virtual texturing for display. One 2D texture stores
  references to other textures.
  Furthermore use of mip mapping is shown using both cudaTextureObjects
  and cudaSurfaceObjects.

  Look into the bindlessTexture_kernel.cu file for most relevant code.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#include <vector>

#include <helper_gl.h>
#include <GL/freeglut.h>

#include "bindlessTexture.h"

#include <helper_functions.h>
#include <cuda_gl_interop.h>

#define MAX_EPSILON_ERROR 5.0f
#define THRESHOLD 0.15f

const char* imageFilenames[] = {
    "flower.ppm", "person.ppm", "sponge.ppm",
};

const cudaExtent atlasSize = make_cudaExtent(4, 4, 0);
const dim3 windowSize(512, 512);
const dim3 windowBlockSize(16, 16, 1);
const dim3 windowGridSize(windowSize.x / windowBlockSize.x, windowSize.y / windowBlockSize.y);

float lod = 0.5;  // texture mip map level

GLuint pbo;  // OpenGL pixel buffer object
struct cudaGraphicsResource* cuda_pbo_resource = NULL;  // CUDA Graphics Resource (to transfer PBO)

bool animate = true;

StopWatchInterface* timer = NULL;

uint* d_output = NULL;

// Auto-Verification Code
int fpsCount = 0;  // FPS count for averaging
int fpsLimit = 1;  // FPS limit for sampling
int g_Index = 0;
unsigned int frameCount = 0;
unsigned int g_TotalErrors = 0;

extern "C" void initAtlasAndImages(const Image * images, size_t numImages, cudaExtent atlasSize);
extern "C" void deinitAtlasAndImages();
extern "C" void randomizeAtlas();
extern "C" void renderAtlasImage(dim3 gridSize, dim3 blockSize, uint * d_output, uint imageW, uint imageH, float lod);

void computeFPS()
{
    frameCount++;
    fpsCount++;

    if (fpsCount == fpsLimit)
    {
        char fps[256];
        float ifps = 1.f / (sdkGetAverageTimerValue(&timer) / 1000.f);
        sprintf(fps, "%3.1f fps", ifps);

        glutSetWindowTitle(fps);
        fpsCount = 0;

        fpsLimit = (int)MAX(1.0f, ifps);
        sdkResetTimer(&timer);
    }
}

// render image using CUDA
void render()
{
    // map PBO to get CUDA device pointer
    checkCudaErrors(cudaGraphicsMapResources(1, &cuda_pbo_resource, 0));
    size_t num_bytes;
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&d_output, &num_bytes, cuda_pbo_resource));

    // call CUDA kernel, writing results to PBO
    renderAtlasImage(windowGridSize, windowBlockSize, d_output, windowSize.x, windowSize.y, lod);

    getLastCudaError("render_kernel failed");

    checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_resource, 0));
}

// display results using OpenGL (called by GLUT)
void display()
{
    sdkStartTimer(&timer);

    render();

    // display results
    glClear(GL_COLOR_BUFFER_BIT);

    // draw image from PBO
    glDisable(GL_DEPTH_TEST);
    glRasterPos2i(0, 0);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, pbo);
    glDrawPixels(windowSize.x, windowSize.y, GL_RGBA, GL_UNSIGNED_BYTE, 0);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, 0);

    glutSwapBuffers();
    glutReportErrors();

    sdkStopTimer(&timer);
    computeFPS();
}

void idle()
{
    if (animate)
    {
        lod += 0.02f;
        glutPostRedisplay();
    }
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;
        break;

    case '=':
    case '+':
        lod += 0.25f;
        break;

    case '-':
        lod -= 0.25f;
        break;

    case 'r':
        randomizeAtlas();
        break;

    case ' ':
        animate = !animate;
        lod = 0.0f;
        break;

    default:
        break;
    }

    glutPostRedisplay();
}

void reshape(int x, int y)
{
    glViewport(0, 0, x, y);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣

    glOrtho(0.0, 1.0, 0.0, 1.0, 0.0, 1.0);
}

// Global cleanup function
// Shared by both GL and non-GL code paths
void cleanup()
{
    sdkDeleteTimer(&timer);

    // unregister this buffer object from CUDA C
    if (cuda_pbo_resource)
    {
        cudaGraphicsUnregisterResource(cuda_pbo_resource);
        glDeleteBuffers(1, &pbo);
    }
}

void cleanup_all()
{
    cleanup();
    deinitAtlasAndImages();
}

void initGLBuffers()
{
    // create pixel buffer object
    glGenBuffers(1, &pbo);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, pbo);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, windowSize.x * windowSize.y * sizeof(GLubyte) * 4, 0, GL_STREAM_DRAW_ARB);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, 0);

    // register this buffer object with CUDA
    checkCudaErrors(cudaGraphicsGLRegisterBuffer(&cuda_pbo_resource, pbo, cudaGraphicsMapFlagsWriteDiscard));
}

// Load raw data from disk
uchar* loadRawFile(const char* filename, size_t size)
{
    FILE* fp = fopen(filename, "rb");

    if (!fp)
    {
        fprintf(stderr, "Error opening file '%s'\n", filename);
        return 0;
    }

    uchar* data = (uchar*)malloc(size);
    size_t read = fread(data, 1, size, fp);
    fclose(fp);

    printf("Read '%s', %zu bytes\n", filename, read);

    return data;
}

void initGL(int* argc, char** argv)
{
    // initialize GLUT callback functions
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    glutInitWindowSize(windowSize.x, windowSize.y);

    glutCreateWindow("New Window");

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function

    glutIdleFunc(idle);	//設定callback function, 利用idle事件進行重畫

    if (!isGLVersionSupported(2, 0) || !areGLExtensionsSupported("GL_ARB_pixel_buffer_object"))
    {
        fprintf(stderr, "Required OpenGL extensions are missing.");
        exit(EXIT_FAILURE);
    }
}

void runAutoTest(const char* ref_file, char* exec_path)
{
    printf("XXXXXXXXXXXXXXXXXXXXXXXXXXX\n");

    size_t windowBytes = windowSize.x * windowSize.y * sizeof(GLubyte) * 4;

    checkCudaErrors(cudaMalloc((void**)&d_output, windowBytes));

    // render the volumeData
    renderAtlasImage(windowGridSize, windowBlockSize, d_output, windowSize.x, windowSize.y, lod);

    checkCudaErrors(cudaDeviceSynchronize());
    getLastCudaError("render_kernel failed");

    void* h_output = malloc(windowBytes);
    checkCudaErrors(cudaMemcpy(h_output, d_output, windowBytes, cudaMemcpyDeviceToHost));

    //保留這個
    sdkDumpBin(h_output, (unsigned int)windowBytes, "bindlessTexture.bin");

    bool bTestResult = sdkCompareBin2BinFloat("bindlessTexture.bin", sdkFindFilePath(ref_file, exec_path), windowSize.x * windowSize.y, MAX_EPSILON_ERROR, THRESHOLD, exec_path);

    checkCudaErrors(cudaFree(d_output));
    free(h_output);
    deinitAtlasAndImages();

    sdkStopTimer(&timer);
    sdkDeleteTimer(&timer);

    exit(bTestResult ? EXIT_SUCCESS : EXIT_FAILURE);
}

void loadImageData(const char* exe_path)
{
    printf("\nloadImageData, filename : %s\n", exe_path);

    std::vector<Image> images;

    for (size_t i = 0; i < sizeof(imageFilenames) / sizeof(imageFilenames[0]); i++)
    {
        unsigned int imgWidth = 0;
        unsigned int imgHeight = 0;
        uchar* imgData = NULL;
        const char* imgFilename = imageFilenames[i];

        sdkLoadPPM4(imgFilename, (unsigned char**)&imgData, &imgWidth, &imgHeight);

        if (!imgData)
        {
            printf("Error opening file '%s'\n", imgFilename);
            exit(EXIT_FAILURE);
        }

        printf("Loaded '%s', %d X %d pixels\n", imgFilename, imgWidth, imgHeight);

        checkHost(imgWidth > 1);
        checkHost(imgHeight > 1);

        Image img;
        img.size = make_cudaExtent(imgWidth, imgHeight, 0);
        img.h_data = imgData;
        images.push_back(img);
    }
    initAtlasAndImages(&images[0], images.size(), atlasSize);
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    sdkCreateTimer(&timer);

    char* ref_file = NULL;

    printf("Starting...\n\n");

    srand(15234);

    // use command-line specified CUDA device, otherwise use device with highest Gflops/s
    findCudaDevice(argc, (const char**)argv);

    if (ref_file == NULL)
    {
        printf("here\n");

        initGL(&argc, argv);

        // OpenGL buffers
        initGLBuffers();
    }

    printf("11111\n");
    if (!checkCudaCapabilities(3, 0))
    {
        printf("XXXXXXX\n");
        cleanup();

        exit(EXIT_WAIVED);
    }
    printf("22222\n");

    loadImageData(argv[0]);

    if (ref_file != NULL)
    {
        printf("XXXXXXXXXXXXXXXXXXXXXXXXXXX\n");
        runAutoTest(ref_file, argv[0]);
    }

    printf("\nPress space to toggle animation\n"
        "Press '+' and '-' to change lod level\n"
        "Press 'r' to randomize virtual atlas\n");

    glutCloseFunc(cleanup_all);

    glutMainLoop();	//開始主循環繪製
}

