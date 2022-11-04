/*
    This example demonstrates how to use the Cuda OpenGL bindings to
    dynamically modify a vertex buffer using a Cuda kernel.

    The steps are:
    1. Create an empty vertex buffer object (VBO)
    2. Register the VBO with Cuda
    3. Map the VBO for writing from Cuda
    4. Run Cuda kernel to modify the vertex positions
    5. Unmap the VBO
    6. Render the results using OpenGL

    Host code
*/

// includes, system
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>

#include "../../../../_6.opengl/_code/Common.h"

#ifdef _WIN32
#  define WINDOWS_LEAN_AND_MEAN
#  define NOMINMAX
#  include <windows.h>
#endif

// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

// includes, cuda
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// Utilities and timing functions
#include <helper_functions.h>    // includes cuda.h and cuda_runtime_api.h

// CUDA helper functions
#include <helper_cuda.h>         // helper functions for CUDA error check

#include <vector_types.h>

#define MAX_EPSILON_ERROR 10.0f
#define THRESHOLD          0.30f
#define REFRESH_DELAY     10 //ms

#define abs(a, b)	(((a) > (b)) ? (a - b) : (b - a))

////////////////////////////////////////////////////////////////////////////////
// constants
const unsigned int window_width = 600;
const unsigned int window_height = 600;

const unsigned int mesh_width = 256;
const unsigned int mesh_height = 256;

// vbo variables
GLuint vbo;
struct cudaGraphicsResource* cuda_vbo_resource;
void* d_vbo_buffer = NULL;

float g_fAnim = 0.0;

// mouse controls
int mouse_old_x;
int mouse_old_y;
int mouse_buttons = 0;
float rotate_x = 0.0;
float rotate_y = 0.0;
float rotate_x_old = 1.0;
float rotate_y_old = 1.0;
float translate_z = -3.0;

StopWatchInterface* timer = NULL;

// Auto-Verification Code
int fpsCount = 0;        // FPS count for averaging
int fpsLimit = 1;        // FPS limit for sampling
float avgFPS = 0.0f;
unsigned int frameCount = 0;

#define MAX(a,b) ((a > b) ? a : b)

void cleanup();

// GL functionality
bool initGL(int* argc, char** argv);
void createVBO(GLuint* vbo, struct cudaGraphicsResource** vbo_res, unsigned int vbo_res_flags);
void deleteVBO(GLuint* vbo, struct cudaGraphicsResource* vbo_res);

// rendering callbacks
void display();
void mouse(int button, int state, int x, int y);
void motion(int x, int y);
void timerEvent(int value);

// Cuda functionality
void runCuda(struct cudaGraphicsResource** vbo_resource);

///////////////////////////////////////////////////////////////////////////////
//! Simple kernel to modify vertex positions in sine wave pattern
//! @param data  data in global memory
///////////////////////////////////////////////////////////////////////////////
__global__ void simple_vbo_kernel(float4* pos, unsigned int width, unsigned int height, float time)
{
    unsigned int x = blockIdx.x * blockDim.x + threadIdx.x;
    unsigned int y = blockIdx.y * blockDim.y + threadIdx.y;

    // calculate uv coordinates
    float u = x / (float)width;
    float v = y / (float)height;
    float w = 0;

    float cx = (float)width / 2;
    float cy = (float)height / 2;

    //printf("(%d, %d) ", width, height);
    //printf("(%d, %d) ", x, y);

    float dx = abs(x, cx);
    float dy = abs(y, cy);
    float freq = 20.0f;
    time = 0;

    if ((dx < 80) && (dy < 80))
    {
        //w = cosf(dx * dy / width / height * freq) / 2;
        //w = cosf((1 - u) * (1 - u) + (1 - v) * (1 - v));
    }
    else
    {
        w = 0;
    }
    //w = sqrtf((1 - u) * (1 - u) + (1 - v) * (1 - v));

    //w = 2 - u * u - v * v;
    //w /= 2;
    w = (u + v) / 2;

    //w = sqrtf(dx * dx * dy * dy / width / width / height / height);
    //w = sqrtf(u * u + v * v);

    float alpha = 1.0f;
    if (((x % 5) != 0) && ((y % 5) != 0))
    {
        alpha = 0.0f;
    }

    pos[y * width + x] = make_float4(u, v, w, alpha);

    if ((x == 0) || (y == 0) || (x == (width - 1)) || (y == (height - 1)))
    {
        pos[y * width + x] = make_float4(u, v, 0.0f, 1.0f);
    }

    if ((x == width / 3) || (y == height / 3) || (x == width * 2 / 3) || (y == height * 2 / 3))
    {
        pos[y * width + x] = make_float4(u, v, 0.5f, 1.0f);
    }

    if ((x >= width / 3) && (y >= height / 3) && (x <= width * 2 / 3) && (y <= height * 2 / 3))
    {
        pos[y * width + x] = make_float4(u, v, 1.0f, 1.0f);
    }
}

void launch_kernel(float4* pos, unsigned int mesh_width, unsigned int mesh_height, float time)
{
    //printf("w = %d h = %d t = %f, ", mesh_width, mesh_height, time); 256, 256, dt = 0.01

    // execute the kernel
    dim3 block(8, 8, 1);
    dim3 grid(mesh_width / block.x, mesh_height / block.y, 1);
    //                32                    32             1

    //                   256             256
    //printf("mesh_width = %d mesh_height = %d t = %f, ", mesh_width, mesh_height, time);
    //                8            8            1
    //printf("block.x = %d block.y = %d block.z = %d, ", block.x, block.y, block.z);

    //mesh_width = 256
    //mesh_height = 256
    simple_vbo_kernel << < grid, block >> > (pos, mesh_width, mesh_height, time);
}

void computeFPS()
{
    frameCount++;
    fpsCount++;

    if (fpsCount == fpsLimit)
    {
        avgFPS = 1.f / (sdkGetAverageTimerValue(&timer) / 1000.f);
        fpsCount = 0;
        fpsLimit = (int)MAX(avgFPS, 1.f);

        sdkResetTimer(&timer);
    }

    char fps[256];
    sprintf(fps, "Cuda GL Interop (VBO): %3.1f fps (Max 100Hz)", avgFPS);
    glutSetWindowTitle(fps);
}

////////////////////////////////////////////////////////////////////////////////
//! Initialize GL
////////////////////////////////////////////////////////////////////////////////
bool initGL(int* argc, char** argv)
{
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);

    glutInitWindowSize(window_width, window_height);    // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Cuda GL Interop (VBO)");

    glutDisplayFunc(display);       //設定callback function
    glutKeyboardFunc(keyboard0);    //設定callback function
    glutMouseFunc(mouse);           //設定callback function
    glutMotionFunc(motion);         //設定callback function

    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    glewInit(); // initialize necessary OpenGL extensions

    // default initialization
    //glClearColor(0.0, 0.0, 0.0, 1.0);   //黑色背景
    glClearColor(1.0, 1.0, 0.0, 1.0);   //黃色背景

    glDisable(GL_DEPTH_TEST);

    // viewport
    glViewport(0, 0, window_width, window_height);

    // projection
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluPerspective(60.0, (GLfloat)window_width / (GLfloat)window_height, 0.1, 10.0);

    SDK_CHECK_ERROR_GL();

    return true;
}

////////////////////////////////////////////////////////////////////////////////
//! Run the Cuda part of the computation
////////////////////////////////////////////////////////////////////////////////
void runCuda(struct cudaGraphicsResource** vbo_resource)
{
    // map OpenGL buffer object for writing from CUDA
    float4* dptr;
    checkCudaErrors(cudaGraphicsMapResources(1, vbo_resource, 0));
    size_t num_bytes;
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&dptr, &num_bytes, *vbo_resource));

    //1048576 bytes
    //printf("CUDA mapped VBO: May access %ld bytes\n", num_bytes);

    // execute the kernel
    //    dim3 block(8, 8, 1);
    //    dim3 grid(mesh_width / block.x, mesh_height / block.y, 1);
    //    kernel<<< grid, block>>>(dptr, mesh_width, mesh_height, g_fAnim);

    //使用GPU
    launch_kernel(dptr, mesh_width, mesh_height, g_fAnim);

    //使用CPU
    //TBD
    /*
    //總是無法用CPU的方式改寫資料
    int i;
    for (i = 0; i < 10; i++)
    {
        dptr[i] = make_float4(0.3f, 0.5f, 0.7f, 1.0f);
    }
    */

    // unmap buffer object
    checkCudaErrors(cudaGraphicsUnmapResources(1, vbo_resource, 0));
}

////////////////////////////////////////////////////////////////////////////////
//! Create VBO
////////////////////////////////////////////////////////////////////////////////
void createVBO(GLuint* vbo, struct cudaGraphicsResource** vbo_res, unsigned int vbo_res_flags)
{
    assert(vbo);

    // create buffer object
    glGenBuffers(1, vbo);
    glBindBuffer(GL_ARRAY_BUFFER, *vbo);

    // initialize buffer object
    unsigned int size = mesh_width * mesh_height * 4 * sizeof(float);
    glBufferData(GL_ARRAY_BUFFER, size, 0, GL_DYNAMIC_DRAW);

    glBindBuffer(GL_ARRAY_BUFFER, 0);

    // register this buffer object with CUDA
    checkCudaErrors(cudaGraphicsGLRegisterBuffer(vbo_res, *vbo, vbo_res_flags));

    SDK_CHECK_ERROR_GL();
}

////////////////////////////////////////////////////////////////////////////////
//! Delete VBO
////////////////////////////////////////////////////////////////////////////////
void deleteVBO(GLuint* vbo, struct cudaGraphicsResource* vbo_res)
{
    // unregister this buffer object with CUDA
    checkCudaErrors(cudaGraphicsUnregisterResource(vbo_res));

    glBindBuffer(1, *vbo);
    glDeleteBuffers(1, vbo);

    *vbo = 0;
}

void display()
{
    //printf("d ");
    sdkStartTimer(&timer);

    // run CUDA kernel to generate vertex positions
    runCuda(&cuda_vbo_resource);

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //畫視窗邊界
    float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
    draw_boundary(color_yellow, 1.5);

    // set view matrix
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
    glTranslatef(0.0, 0.0, translate_z);

    glRotatef(rotate_x, 1.0, 0.0, 0.0);
    glRotatef(rotate_y, 0.0, 1.0, 0.0);

    /*
    //debug print
    if ((rotate_x_old != rotate_x) && (rotate_y_old != rotate_y))
    {
        printf("rx = %f, ry = %f ", rotate_x, rotate_y);
        rotate_x_old = rotate_x;
        rotate_y_old = rotate_y;
    }
    */

    // render from the vbo
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glVertexPointer(4, GL_FLOAT, 0, 0);

    glEnableClientState(GL_VERTEX_ARRAY);
    glColor3f(1.0, 0.0, 0.0); //紅色
    //glColor3f(0.0, 1.0, 0.0); //綠色
    //glColor3f(0.0, 0.0, 1.0);   //藍色
    glDrawArrays(GL_POINTS, 0, mesh_width * mesh_height);
    glDisableClientState(GL_VERTEX_ARRAY);

    glutSwapBuffers();

    g_fAnim += 0.01f;

    sdkStopTimer(&timer);
    computeFPS();
}

void timerEvent(int value)
{
    if (glutGetWindow())
    {
        //在這裡呼叫重新畫圖
        //printf("d-");
        glutPostRedisplay();
        glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
    }
}

void cleanup()
{
    sdkDeleteTimer(&timer);

    if (vbo)
    {
        deleteVBO(&vbo, cuda_vbo_resource);
    }
}

void mouse(int button, int state, int x, int y)
{
    if (state == GLUT_DOWN)
    {
        mouse_buttons |= 1 << button;
    }
    else if (state == GLUT_UP)
    {
        mouse_buttons = 0;
    }

    mouse_old_x = x;
    mouse_old_y = y;
}

void motion(int x, int y)
{
    float dx, dy;
    dx = (float)(x - mouse_old_x);
    dy = (float)(y - mouse_old_y);

    if (mouse_buttons & 1)
    {
        //滑鼠左鍵
        rotate_x += dy * 0.2f;
        rotate_y += dx * 0.2f;
    }
    else if (mouse_buttons & 4)
    {
        //滑鼠右鍵
        translate_z += dy * 0.01f;
    }

    mouse_old_x = x;
    mouse_old_y = y;
}

int main(int argc, char** argv)
{
    printf("Starting...\n");

    // Create the CUTIL timer
    sdkCreateTimer(&timer);

    initGL(&argc, argv);
    findCudaDevice(argc, (const char**)argv);

    glutCloseFunc(cleanup);

    // create VBO
    createVBO(&vbo, &cuda_vbo_resource, cudaGraphicsMapFlagsWriteDiscard);

    // run the cuda part
    runCuda(&cuda_vbo_resource);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

