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

const uint width = 512;
const uint height = 512;

GLuint pbo;  // OpenGL pixel buffer object

StopWatchInterface *timer = NULL;

#define MAX(a, b) ((a > b) ? a : b)

extern "C" void cleanup();

// display results using OpenGL (called by GLUT)
void display()
{
    sdkStartTimer(&timer);

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
}

void idle()
{
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;

    default:
        break;
    }

    glutPostRedisplay();
}

void reshape(int x, int y)
{
    glViewport(0, 0, x, y);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, 1.0, 0.0, 1.0, 0.0, 1.0);
}

void cleanup()
{
    sdkDeleteTimer(&timer);
}

void initGLBuffers()
{
    printf("initGLBuffers\n");

    // create pixel buffer object
    glGenBuffers(1, &pbo);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, pbo);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, width * height * sizeof(GLubyte) * 4, 0, GL_STREAM_DRAW_ARB);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, 0);
}

void initGL(int* argc, char** argv)
{
    printf("initGL\n");

    // initialize GLUT callback functions
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    glutInitWindowSize(width, height);

    glutCreateWindow("開啟新視窗");

    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutReshapeFunc(reshape);
    glutIdleFunc(idle);

    if (!isGLVersionSupported(2, 0) || !areGLExtensionsSupported("GL_ARB_pixel_buffer_object"))
    {
        fprintf(stderr, "Required OpenGL extensions are missing.");
        exit(EXIT_FAILURE);
    }
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    char* ref_file = NULL;

    printf("main start\n");

    if (checkCmdLineFlag(argc, (const char**)argv, "file"))
    {
        printf("XXXXXXXXXXX\n");
        std::cout << "xxxxxx" << std::endl;
        getCmdLineArgumentString(argc, (const char**)argv, "file", &ref_file);
    }

    // use command-line specified CUDA device, otherwise use device with highest
    // Gflops/s
    int cuda_device = findCudaDevice(argc, (const char**)argv);
    // check the compute capability of the device
    int num_devices = 0;
    checkCudaErrors(cudaGetDeviceCount(&num_devices));

    if (num_devices == 0)
    {
        printf("your system does not have a CUDA capable device, waiving test...\n");
        return EXIT_WAIVED;
    }

    // check if the command-line chosen device ID is within range, exit if not
    if (cuda_device >= num_devices)
    {
        printf("cuda_device=%d is invalid, must choose device ID between 0 and %d\n", cuda_device, num_devices - 1);
        return EXIT_FAILURE;
    }
    checkCudaErrors(cudaSetDevice(cuda_device));

    // Checking for compute capabilities
    cudaDeviceProp deviceProp;
    checkCudaErrors(cudaGetDeviceProperties(&deviceProp, cuda_device));
    printf("Device: <%s> canMapHostMemory: %s\n", deviceProp.name,deviceProp.canMapHostMemory ? "Yes" : "No");

    if (deviceProp.canMapHostMemory == 0)
    {
        printf("Using cudaMallocHost, CUDA device does not support mapping of generic host memory\n");
        //bPinGenericMemory = false;
    }

    float scale_factor = 1.0f;

    scale_factor =
        MAX((32.0f / (_ConvertSMVer2Cores(deviceProp.major, deviceProp.minor) *
            (float)deviceProp.multiProcessorCount)),
            1.0f);
    int n = 16 * 1024 * 1024;      // number of ints in the data set
    n = (int)rint((float)n / scale_factor);

    printf("> CUDA Capable: SM %d.%d hardware\n", deviceProp.major,
        deviceProp.minor);
    printf("> %d Multiprocessor(s) x %d (Cores/Multiprocessor) = %d (Cores)\n",
        deviceProp.multiProcessorCount,
        _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor),
        _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor) *
        deviceProp.multiProcessorCount);

    printf("> scale_factor = %1.4f\n", 1.0f / scale_factor);
    printf("> array_size   = %d\n\n", n);

    printf("版本資訊\n");
    //printf("Header version:  %u.%u\n", NVMEDIA_2D_VERSION_MAJOR, NVMEDIA_2D_VERSION_MINOR);
    printf("CUDART_VERSION : %d\n", CUDART_VERSION);
    //printf("__CUDA_API_VERSION : %d\n", __CUDA_API_VERSION);
    //printf("NVTX_VERSION : %d\n", NVTX_VERSION);
    printf("GL_VERSION : %d\n", GL_VERSION);




    initGL(&argc, argv);  //開啟CUDA3D Texture

    // OpenGL buffers
    initGLBuffers();

    printf("call glutCloseFunc\n");
    glutCloseFunc(cleanup);

    glutMainLoop();

    exit(EXIT_SUCCESS);
}



