// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

// CUDA utilities and system includes
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// Includes
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "imageDenoising.h"

// includes, project
#include <helper_functions.h>  // includes for helper utility functions
#include <helper_cuda.h>  // includes for cuda error checking and initialization

const char* filterMode[] = { "Passthrough", "KNN method", "NLM method",
                            "Quick NLM(NLM2) method", NULL };

////////////////////////////////////////////////////////////////////////////////
// Global data handlers and parameters
////////////////////////////////////////////////////////////////////////////////
// OpenGL PBO and texture "names"
GLuint gl_PBO, gl_Tex;
struct cudaGraphicsResource *cuda_pbo_resource;  // handles OpenGL-CUDA exchange
// Source image on the host side

uchar4 *h_Src1;
uchar4* h_Src2;
int imageW, imageH;

////////////////////////////////////////////////////////////////////////////////
// Main program
////////////////////////////////////////////////////////////////////////////////
int g_Kernel = 0;
bool g_FPS = false;
bool g_Diag = false;
StopWatchInterface *timer = NULL;


const int frameN = 24;
int frameCounter = 0;
#define BUFFER_DATA(i) ((char *)0 + i)

// Auto-Verification Code
const int frameCheckNumber = 4;
int fpsCount = 0;  // FPS count for averaging
int fpsLimit = 1;  // FPS limit for sampling
unsigned int frameCount = 0;
unsigned int g_TotalErrors = 0;

int *pArgc = NULL;
char **pArgv = NULL;

#define MAX_EPSILON_ERROR 5
#define REFRESH_DELAY 10  // ms

void cleanup();

void computeFPS()
{
    //printf("computeFPS ");
    frameCount++;
    fpsCount++;

    if (fpsCount == fpsLimit)
    {
        char fps[256];
        float ifps = 1.f / (sdkGetAverageTimerValue(&timer) / 1000.f);
        sprintf(fps, "<%s>: %3.1f fps", filterMode[g_Kernel], ifps);

        glutSetWindowTitle(fps);
        fpsCount = 0;

        // fpsLimit = (int)MAX(ifps, 1.f);
        sdkResetTimer(&timer);
    }
}

void runImageFilters(TColor* d_dst)
{
    //printf("%d ", g_Kernel);
    switch (g_Kernel)
    {
    case 0:
        //cuda_Copy(d_dst, imageW, imageH, texImage);
        break;

    case 1:
        if (!g_Diag)
        {
        }
        else
        {
        }

        break;

    case 2:
        if (!g_Diag)
        {
        }
        else
        {
        }

        break;

    case 3:
        if (!g_Diag)
        {
        }
        else
        {
        }

        break;

    case 10:
        printf("Change some data\n");

        //cuda_Copy(d_dst, imageW, imageH, texImage);

        //print_some_data(texImage);    //TBD

        //cuda_Copy(d_dst, imageW, imageH, texImage);

        //cuda_NLM(d_dst, imageW/2, imageH, 1.0f / (nlmNoise * nlmNoise * 5), lerpC, texImage);

        g_Kernel = 0;
        break;

    case 11:
        printf("Copy ims 01\n");


        g_Kernel = 0;
        break;

    case 13:
        printf("Copy ims 03\n");


        g_Kernel = 0;
        break;
    }

    getLastCudaError("Filtering kernel execution failed.\n");
}

void displayFunc(void)
{
    //printf("dis ");

    sdkStartTimer(&timer);
    TColor* d_dst = NULL;
    size_t num_bytes;

    if (frameCounter++ == 0)
    {
        sdkResetTimer(&timer);
    }

    checkCudaErrors(cudaGraphicsMapResources(1, &cuda_pbo_resource, 0));
    getLastCudaError("cudaGraphicsMapResources failed");
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&d_dst, &num_bytes, cuda_pbo_resource));
    //printf("(%d) ", num_bytes);
    getLastCudaError("cudaGraphicsResourceGetMappedPointer failed");

    runImageFilters(d_dst);

    checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_resource, 0));

    // Common display code path
    {
        glClear(GL_COLOR_BUFFER_BIT);

        glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, imageW, imageH, GL_RGBA, GL_UNSIGNED_BYTE, BUFFER_DATA(0));
        glBegin(GL_TRIANGLES);
        glTexCoord2f(0, 0);
        glVertex2f(-1, -1);
        glTexCoord2f(2, 0);
        glVertex2f(+3, -1);
        glTexCoord2f(0, 2);
        glVertex2f(-1, +3);
        glEnd();
        glFinish();
    }

    if (frameCounter == frameN)
    {
        frameCounter = 0;

        if (g_FPS)
        {
            printf("FPS: %3.1f\n", frameN / (sdkGetTimerValue(&timer) * 0.001));
            g_FPS = false;
        }
    }

    glutSwapBuffers();
    glutReportErrors();

    sdkStopTimer(&timer);

    computeFPS();
}

void timerEvent(int value)
{
    //printf("timer ");
    if (glutGetWindow())
    {
        //printf("glutGetWindow ");
        glutPostRedisplay();
        glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
    }
}

void keyboard(unsigned char k, int /*x*/, int /*y*/)
{
    switch (k)
    {
    case 27:
    case 'q':
    case 'Q':
        //���}����
        glutDestroyWindow(glutGetWindow());
        return;

    case '1':
        printf("Passthrough.\n");
        g_Kernel = 0;
        break;

    case '2':
        printf("KNN method \n");
        g_Kernel = 1;
        break;

    case '3':
        printf("NLM method\n");
        g_Kernel = 2;
        break;

    case '4':
        printf("Quick NLM(NLM2) method\n");
        g_Kernel = 3;
        break;

    case 'c':
        printf("Change some data\n");
        g_Kernel = 10;
        break;

    case 'a':
        printf("Copy ims 01\n");
        g_Kernel = 11;
        break;

    case 'b':
        printf("Copy ims 03\n");
        g_Kernel = 13;
        break;

    case '*':
        printf(g_Diag ? "LERP highlighting mode.\n" : "Normal mode.\n");
        g_Diag = !g_Diag;
        break;

    case 'n':
        printf("Decrease noise level.\n");
        break;

    case 'N':
        printf("Increase noise level.\n");
        break;

    case 'l':
        printf("Decrease LERP quotient.\n");
        break;

    case 'L':
        printf("Increase LERP quotient.\n");
        break;

    case 'f':
    case 'F':
        g_FPS = true;
        break;

    case '?':
        break;
    }
}

int initGL(int* argc, char** argv)
{
    printf("Initializing GLUT...\n");
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);
    glutInitWindowSize(imageW, imageH);
    glutInitWindowPosition(512 - imageW / 2, 384 - imageH / 2);
    glutCreateWindow(argv[0]);

    glutDisplayFunc(displayFunc);   //�]�wcallback function
    glutKeyboardFunc(keyboard);     //�]�wcallback function

    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);    //�]�wtimer�ƥ�

    printf("OpenGL window created.\n");

    glutCloseFunc(cleanup);

    if (!isGLVersionSupported(1, 5) || !areGLExtensionsSupported("GL_ARB_vertex_buffer_object GL_ARB_pixel_buffer_object"))
    {
        fprintf(stderr, "Error: failed to get minimal extensions for demo\n");
        fprintf(stderr, "This sample requires:\n");
        fprintf(stderr, "  OpenGL version 1.5\n");
        fprintf(stderr, "  GL_ARB_vertex_buffer_object\n");
        fprintf(stderr, "  GL_ARB_pixel_buffer_object\n");
        fflush(stderr);
        return false;
    }

    return 0;
}

void initOpenGLBuffers()
{
    printf("Creating GL texture...\n");
    glEnable(GL_TEXTURE_2D);
    glGenTextures(1, &gl_Tex);
    glBindTexture(GL_TEXTURE_2D, gl_Tex);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    /*
    for (int i = 0; i < imageW * imageH; i++)
    {
        h_Src1[i].x = h_Src1[i].x / 2;
        h_Src1[i].y = h_Src1[i].y / 2;
        h_Src1[i].z = h_Src1[i].z / 2;
        h_Src1[i].w = h_Src1[i].w / 2;
    }
    */

    //�b�o�̧�v���]�w��pBox....
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, imageW, imageH, 0, GL_RGBA, GL_UNSIGNED_BYTE, h_Src1);

    printf("Texture created.\n");

    printf("Creating PBO...\n");
    glGenBuffers(1, &gl_PBO);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, gl_PBO);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, imageW * imageH * 4, h_Src1, GL_STREAM_COPY);

    checkCudaErrors(cudaGraphicsGLRegisterBuffer(&cuda_pbo_resource, gl_PBO, cudaGraphicsMapFlagsWriteDiscard));
    GLenum gl_error = glGetError();

    if (gl_error != GL_NO_ERROR)
    {
        char tmpStr[512];
        // NOTE: "%s(%i) : " allows Visual Studio to directly jump to the file at
        // the right line when the user double clicks on the error line in the
        // Output pane. Like any compile error.
        sprintf_s(tmpStr, 255, "\n%s(%i) : GL Error : %s\n\n", __FILE__, __LINE__, gluErrorString(gl_error));
        OutputDebugString(tmpStr);

        fprintf(stderr, "GL Error in file '%s' in line %d :\n", __FILE__, __LINE__);
        fprintf(stderr, "%s\n", gluErrorString(gl_error));
        exit(EXIT_FAILURE);
    }

    printf("PBO created.\n");
}

void cleanup()
{
    printf("cleanup()\n");

    free(h_Src1);
    free(h_Src2);
    checkCudaErrors(CUDA_FreeArray());
    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_pbo_resource));

sdkDeleteTimer(&timer);
}

int main(int argc, char** argv)
{
    //Ū���Ϥ����
    const char* filename_read1 = "C:\\______test_files\\ims01.24.bmp"; //24 bits
    const char* filename_read2 = "C:\\______test_files\\ims03.24.bmp"; //24 bits

    imageW = 0;
    imageH = 0;
    LoadBMPFile(&h_Src1, &imageW, &imageH, filename_read1);
    printf("filename : %s\tW = %d\tH = %d\n", filename_read1, imageW, imageH);

    imageW = 0;
    imageH = 0;
    LoadBMPFile(&h_Src2, &imageW, &imageH, filename_read2);
    printf("filename : %s\tW = %d\tH = %d\n", filename_read2, imageW, imageH);

    initGL(&argc, argv);
    findCudaDevice(argc, (const char**)argv);

    checkCudaErrors(CUDA_MallocArray(&h_Src1, imageW, imageH));
    checkCudaErrors(CUDA_MallocArray(&h_Src2, imageW, imageH));

    initOpenGLBuffers();
    glutSetWindowTitle("ims pic");

    glutMainLoop();
}
