/*
  3D texture sample

  This sample loads a 3D volume from disk and displays slices through it using 3D texture lookups.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <helper_gl.h>

#include <GL/freeglut.h>

// includes, cuda
#include <vector_types.h>
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// CUDA utilities and system includes
#include <helper_cuda.h>
#include <helper_functions.h>
#include <vector_types.h>

typedef unsigned int uint;
typedef unsigned char uchar;

#define MAX_EPSILON_ERROR 5.0f
#define THRESHOLD 0.15f

char* image_filename = "Bucky.raw";

const cudaExtent volumeSize = make_cudaExtent(32, 32, 32);

const uint width = 512, height = 512;
const dim3 blockSize(16, 16, 1);
const dim3 gridSize(width / blockSize.x, height / blockSize.y);

float w = 0.5;  // texture coordinate in z

GLuint pbo;  // OpenGL pixel buffer object
struct cudaGraphicsResource* cuda_pbo_resource;  // CUDA Graphics Resource (to transfer PBO)

bool linearFiltering = true;
bool animate = true;

StopWatchInterface* timer = NULL;

uint* d_output = NULL;

// Auto-Verification Code
const int frameCheckNumber = 4;
int fpsCount = 0;  // FPS count for averaging
int fpsLimit = 1;  // FPS limit for sampling
int g_Index = 0;
unsigned int frameCount = 0;
unsigned int g_TotalErrors = 0;
volatile int g_GraphicsMapFlag = 0;

#ifndef MAX
#define MAX(a, b) ((a > b) ? a : b)
#endif

extern "C" void cleanup();
extern "C" void setTextureFilterMode(bool bLinearFilter);
extern "C" void initCuda(const uchar * h_volume, cudaExtent volumeSize);
extern "C" void render_kernel(dim3 gridSize, dim3 blockSize, uint * d_output, uint imageW, uint imageH, float w);
extern void cleanupCuda();

void loadVolumeData(char* filename);

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

        fpsLimit = ftoi(MAX(1.0f, ifps));
        sdkResetTimer(&timer);
    }
}

// render image using CUDA
void render()
{
    // map PBO to get CUDA device pointer
    g_GraphicsMapFlag++;
    checkCudaErrors(cudaGraphicsMapResources(1, &cuda_pbo_resource, 0));
    size_t num_bytes;
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&d_output, &num_bytes, cuda_pbo_resource));
    // printf("CUDA mapped PBO: May access %ld bytes\n", num_bytes);

    // call CUDA kernel, writing results to PBO
    render_kernel(gridSize, blockSize, d_output, width, height, w);

    getLastCudaError("render_kernel failed");

    if (g_GraphicsMapFlag)
    {
        checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_resource, 0));
        g_GraphicsMapFlag--;
    }
}

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
    glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, 0);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, 0);

    glutSwapBuffers();
    glutReportErrors();

    sdkStopTimer(&timer);
    computeFPS();
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

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;

    case '=':
    case '+':
        w += 0.01f;
        break;

    case '-':
        w -= 0.01f;
        break;

    case 'f':
        linearFiltering = !linearFiltering;
        setTextureFilterMode(linearFiltering);
        break;

    case ' ':
        animate = !animate;
        break;

    default:
        break;
    }

    glutPostRedisplay();
}

void idle()
{
    if (animate)
    {
        w += 0.01f;
        glutPostRedisplay();
    }
}

void cleanup()
{
    sdkDeleteTimer(&timer);

    // add extra check to unmap the resource before unregistering it
    if (g_GraphicsMapFlag)
    {
        checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_resource, 0));
        g_GraphicsMapFlag--;
    }

    // unregister this buffer object from CUDA C
    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_pbo_resource));
    glDeleteBuffers(1, &pbo);
    cleanupCuda();
}

void initGLBuffers()
{
    printf("initGLBuffers\n");

    // create pixel buffer object
    glGenBuffers(1, &pbo);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, pbo);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, width * height * sizeof(GLubyte) * 4, 0, GL_STREAM_DRAW_ARB);
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
    printf("initGL\n");

    // initialize GLUT callback functions
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    glutInitWindowSize(width, height);

    glutCreateWindow("CUDA 3D texture");

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function

    glutIdleFunc(idle); //設定callback function, 利用idle事件進行重畫

glewInit();
}

void loadVolumeData(char* filename)
{
    if (filename == NULL)
    {
        fprintf(stderr, "Error unable to find 3D Volume file: '%s'\n", filename);
        exit(EXIT_FAILURE);
    }

    size_t size = volumeSize.width * volumeSize.height * volumeSize.depth;

    uchar* h_volume = loadRawFile(filename, size);
    printf("loadVolumeData, path = %s, size = %lu\n", filename, size);

    initCuda(h_volume, volumeSize);
    sdkCreateTimer(&timer);

    free(h_volume);
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    printf("Starting...\n\n");

    initGL(&argc, argv);  //開啟CUDA3D Texture

    // OpenGL buffers
    initGLBuffers();

    loadVolumeData(image_filename);

    printf("Press space to toggle animation\nPress '+' and '-' to change displayed slice\n");

    glutCloseFunc(cleanup);

    glutMainLoop();	//開始主循環繪製

    exit(EXIT_SUCCESS);
}
