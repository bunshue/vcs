// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

// CUDA utilities and system includes
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// Includes
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "SobelFilter_kernels.h"

// includes, project
#include <helper_functions.h>  // includes for SDK helper functions
#include <helper_cuda.h>  // includes for cuda initialization and error checking

const char* filterMode[] = { "No Filtering", "Sobel Texture", "Sobel SMEM+Texture", NULL };

//
// Cuda example code that implements the Sobel edge detection
// filter. This code works for 8-bit monochrome images.
//
// Use the '-' and '=' keys to change the scale factor.
//
// Other keys:
// I: display image
// T: display Sobel edge detection (computed solely with texture)
// S: display Sobel edge detection (computed with texture and shared memory)

void cleanup(void);
void initializeData(char* file);

#define MAX_EPSILON_ERROR 5.0f
#define REFRESH_DELAY 10  // ms

const char* sSDKsample = "CUDA Sobel Edge-Detection";

static int wWidth = 512;   // Window width
static int wHeight = 512;  // Window height
static int imWidth = 0;    // Image width
static int imHeight = 0;   // Image height

// Code to handle Auto verification
const int frameCheckNumber = 4;
int fpsCount = 0;  // FPS count for averaging
int fpsLimit = 8;  // FPS limit for sampling
unsigned int frameCount = 0;
unsigned int g_TotalErrors = 0;
StopWatchInterface* timer = NULL;
unsigned int g_Bpp;
unsigned int g_Index = 0;

bool g_bQAReadback = false;

// Display Data
static GLuint pbo_buffer = 0;  // Front and back CA buffers
struct cudaGraphicsResource* cuda_pbo_resource;  // CUDA Graphics Resource (to transfer PBO)

static GLuint texid = 0;       // Texture for display
unsigned char* pixels = NULL;  // Image pixel data on the host
float imageScale = 1.f;        // Image exposure
enum SobelDisplayMode g_SobelDisplayMode;

extern "C" void runAutoTest(int argc, char** argv);

#define OFFSET(i) ((char *)NULL + (i))
#define MAX(a, b) ((a > b) ? a : b)

void computeFPS()
{
    frameCount++;
    fpsCount++;

    if (fpsCount == fpsLimit)
    {
        char fps[256];
        float ifps = 1.f / (sdkGetAverageTimerValue(&timer) / 1000.f);
        sprintf(fps, "CUDA Edge Detection (%s): %3.1f fps", filterMode[g_SobelDisplayMode], ifps);

        glutSetWindowTitle(fps);    //顯示在圖框上的標題

        fpsCount = 0;

        sdkResetTimer(&timer);
    }
}

// This is the normal display path
void display(void)
{
    sdkStartTimer(&timer);

    // Sobel operation
    Pixel* data = NULL;

    // map PBO to get CUDA device pointer
    checkCudaErrors(cudaGraphicsMapResources(1, &cuda_pbo_resource, 0));
    size_t num_bytes;
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&data, &num_bytes, cuda_pbo_resource));
    // printf("CUDA mapped PBO: May access %ld bytes\n", num_bytes);

    sobelFilter(data, imWidth, imHeight, g_SobelDisplayMode, imageScale);
    checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_resource, 0));

    glClear(GL_COLOR_BUFFER_BIT);

    glBindTexture(GL_TEXTURE_2D, texid);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbo_buffer);
    glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, imWidth, imHeight, GL_LUMINANCE, GL_UNSIGNED_BYTE, OFFSET(0));
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER, 0);

    glDisable(GL_DEPTH_TEST);
    glEnable(GL_TEXTURE_2D);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    glBegin(GL_QUADS);
    glVertex2f(0, 0);
    glTexCoord2f(0, 0);
    glVertex2f(0, 1);
    glTexCoord2f(1, 0);
    glVertex2f(1, 1);
    glTexCoord2f(1, 1);
    glVertex2f(1, 0);
    glTexCoord2f(0, 1);
    glEnd();
    glBindTexture(GL_TEXTURE_2D, 0);
    glutSwapBuffers();

    sdkStopTimer(&timer);

    computeFPS();
}

void timerEvent(int value)
{
    if (glutGetWindow())
    {
        glutPostRedisplay();
        glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
    }
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    char temp[256];

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        printf("Shutting down...\n");
        glutDestroyWindow(glutGetWindow());
        return;
        break;

    case '-':
        imageScale -= 0.1f;
        printf("brightness = %4.2f\n", imageScale);
        break;

    case '+':
        imageScale += 0.1f;
        printf("brightness = %4.2f\n", imageScale);
        break;

    case 'i':
    case 'I':
        g_SobelDisplayMode = SOBELDISPLAY_IMAGE;
        sprintf(temp, "CUDA Edge Detection (%s)", filterMode[g_SobelDisplayMode]);
        glutSetWindowTitle(temp);
        break;

    case 's':
    case 'S':
        g_SobelDisplayMode = SOBELDISPLAY_SOBELSHARED;
        sprintf(temp, "CUDA Edge Detection (%s)", filterMode[g_SobelDisplayMode]);
        glutSetWindowTitle(temp);
        break;

    case 't':
    case 'T':
        g_SobelDisplayMode = SOBELDISPLAY_SOBELTEX;
        sprintf(temp, "CUDA Edge Detection (%s)", filterMode[g_SobelDisplayMode]);
        glutSetWindowTitle(temp);
        break;

    default:
        break;
    }
}

void reshape(int x, int y)
{
    glViewport(0, 0, x, y);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    glOrtho(0, 1, 0, 1, 0, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
}

void cleanup(void)
{
    cudaGraphicsUnregisterResource(cuda_pbo_resource);

    glBindBuffer(GL_PIXEL_UNPACK_BUFFER, 0);
    glDeleteBuffers(1, &pbo_buffer);
    glDeleteTextures(1, &texid);
    deleteTexture();

    sdkDeleteTimer(&timer);
}

void initializeData(char* file)
{
    GLint bsize;
    unsigned int w, h;
    size_t file_length = strlen(file);

    if (!strcmp(&file[file_length - 3], "pgm"))
    {
        printf("here\n");
        if (sdkLoadPGM<unsigned char>(file, &pixels, &w, &h) != true)
        {
            printf("Failed to load PGM image file: %s\n", file);
            exit(EXIT_FAILURE);
        }

        g_Bpp = 1;
    }
    else if (!strcmp(&file[file_length - 3], "ppm"))
    {
        printf("XXXXXXXXXXXXXXXXXXXXXXX\n");
        if (sdkLoadPPM4(file, &pixels, &w, &h) != true)
        {
            printf("Failed to load PPM image file: %s\n", file);
            exit(EXIT_FAILURE);
        }

        g_Bpp = 4;
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXXXX\n");
        exit(EXIT_FAILURE);
    }

    imWidth = (int)w;
    imHeight = (int)h;
    setupTexture(imWidth, imHeight, pixels, g_Bpp);

    memset(pixels, 0x0, g_Bpp * sizeof(Pixel) * imWidth * imHeight);

    if (!g_bQAReadback)
    {
        printf("here\n");
        // use OpenGL Path
        glGenBuffers(1, &pbo_buffer);
        glBindBuffer(GL_PIXEL_UNPACK_BUFFER, pbo_buffer);
        glBufferData(GL_PIXEL_UNPACK_BUFFER, g_Bpp * sizeof(Pixel) * imWidth * imHeight, pixels, GL_STREAM_DRAW);

        glGetBufferParameteriv(GL_PIXEL_UNPACK_BUFFER, GL_BUFFER_SIZE, &bsize);

        if ((GLuint)bsize != (g_Bpp * sizeof(Pixel) * imWidth * imHeight))
        {
            printf("Buffer object (%d) has incorrect size (%d).\n", (unsigned)pbo_buffer, (unsigned)bsize);

            exit(EXIT_FAILURE);
        }

        glBindBuffer(GL_PIXEL_UNPACK_BUFFER, 0);

        // register this buffer object with CUDA
        checkCudaErrors(cudaGraphicsGLRegisterBuffer(&cuda_pbo_resource, pbo_buffer, cudaGraphicsMapFlagsWriteDiscard));

        glGenTextures(1, &texid);
        glBindTexture(GL_TEXTURE_2D, texid);
        glTexImage2D(GL_TEXTURE_2D, 0, ((g_Bpp == 1) ? GL_LUMINANCE : GL_BGRA), imWidth, imHeight, 0, GL_LUMINANCE, GL_UNSIGNED_BYTE, NULL);
        glBindTexture(GL_TEXTURE_2D, 0);

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
        glPixelStorei(GL_PACK_ALIGNMENT, 1);
    }
}

void loadDefaultImage(char* loc_exec)
{
    printf("Reading image: teapot.pgm\n");

    const char* image_filename = "teapot.pgm";
    char* image_path = sdkFindFilePath(image_filename, loc_exec);

    if (image_path == NULL)
    {
        printf("Failed to read image file: <%s>\n", image_filename);
        exit(EXIT_FAILURE);
    }

    initializeData(image_path);
    free(image_path);
}

void initGL(int* argc, char** argv)
{
    glutInit(argc, argv);

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);
    glutInitWindowSize(wWidth, wHeight);

    glutCreateWindow("CUDA Edge Detection + - I S T");

glewInit();
}

void runAutoTest(int argc, char* argv[])
{
    printf("[%s] (automated testing w/ readback)\n", sSDKsample);
    int devID = findCudaDevice(argc, (const char**)argv);

    loadDefaultImage(argv[0]);

    Pixel* d_result;
    checkCudaErrors(cudaMalloc((void**)&d_result, imWidth * imHeight * sizeof(Pixel)));

    char* ref_file = NULL;
    char dump_file[256];

    int mode = 0;
    mode = getCmdLineArgumentInt(argc, (const char**)argv, "mode");
    getCmdLineArgumentString(argc, (const char**)argv, "file", &ref_file);

    switch (mode)
    {
    case 0:
        g_SobelDisplayMode = SOBELDISPLAY_IMAGE;
        sprintf(dump_file, "teapot_orig.pgm");
        break;

    case 1:
        g_SobelDisplayMode = SOBELDISPLAY_SOBELTEX;
        sprintf(dump_file, "teapot_tex.pgm");
        break;

    case 2:
        g_SobelDisplayMode = SOBELDISPLAY_SOBELSHARED;
        sprintf(dump_file, "teapot_shared.pgm");
        break;

    default:
        printf("Invalid Filter Mode File\n");
        exit(EXIT_FAILURE);
        break;
    }

    printf("AutoTest: %s <%s>\n", sSDKsample, filterMode[g_SobelDisplayMode]);
    sobelFilter(d_result, imWidth, imHeight, g_SobelDisplayMode, imageScale);
    checkCudaErrors(cudaDeviceSynchronize());

    unsigned char* h_result = (unsigned char*)malloc(imWidth * imHeight * sizeof(Pixel));
    checkCudaErrors(cudaMemcpy(h_result, d_result, imWidth * imHeight * sizeof(Pixel), cudaMemcpyDeviceToHost));
    sdkSavePGM(dump_file, h_result, imWidth, imHeight);

    if (!sdkComparePGM(dump_file, sdkFindFilePath(ref_file, argv[0]), MAX_EPSILON_ERROR, 0.15f, false))
    {
        g_TotalErrors++;
    }

    checkCudaErrors(cudaFree(d_result));
    free(h_result);

    if (g_TotalErrors != 0)
    {
        printf("Test failed!\n");
        exit(EXIT_FAILURE);
    }

    printf("Test passed!\n");
    exit(EXIT_SUCCESS);
}

int main(int argc, char** argv)
{
    printf("%s Starting...\n\n", sSDKsample);

    if (checkCmdLineFlag(argc, (const char**)argv, "help"))
    {
        printf("\nUsage: SobelFilter <options>\n");
        printf("\t\t-mode=n (0=original, 1=texture, 2=smem + texture)\n");
        printf("\t\t-file=ref_orig.pgm (ref_tex.pgm, ref_shared.pgm)\n\n");
        exit(EXIT_SUCCESS);
    }

    if (checkCmdLineFlag(argc, (const char**)argv, "file"))
    {
        g_bQAReadback = true;
        runAutoTest(argc, argv);
    }

    // use command-line specified CUDA device, otherwise use device with highest Gflops/s
    if (checkCmdLineFlag(argc, (const char**)argv, "device"))
    {
        printf("   This SDK does not explicitly support -device=n when running with OpenGL.\n");
        printf("   When specifying -device=n (n=0,1,2,....) the sample must not use OpenGL.\n");
        printf("   See details below to run without OpenGL:\n\n");
        printf(" > %s -device=n\n\n", argv[0]);
        printf("exiting...\n");
        exit(EXIT_SUCCESS);
    }

    initGL(&argc, argv);
    findCudaDevice(argc, (const char**)argv);

    sdkCreateTimer(&timer);
    sdkResetTimer(&timer);

    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutReshapeFunc(reshape);

    loadDefaultImage(argv[0]);

    // If code is not printing the usage, then we execute this path.
    printf("I: display Image (no filtering)\n");
    printf("T: display Sobel Edge Detection (Using Texture)\n");
    printf("S: display Sobel Edge Detection (Using SMEM+Texture)\n");
    printf("Use the '+' and '-' keys to change the brightness.\n");
    fflush(stdout);

    glutCloseFunc(cleanup);

    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
    glutMainLoop();	//開始主循環繪製
}
