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

// includes, project
#include <helper_functions.h>  // includes for helper utility functions
#include <helper_cuda.h>  // includes for cuda error checking and initialization

typedef unsigned int TColor;

////////////////////////////////////////////////////////////////////////////////
// Global data handlers and parameters
////////////////////////////////////////////////////////////////////////////////
// Texture object and channel descriptor for image texture
cudaTextureObject_t texImage;

cudaChannelFormatDesc uchar4tex = cudaCreateChannelDesc<uchar4>();

cudaArray* a_Src;   // CUDA array descriptor

cudaError_t CUDA_MallocArray(uchar4** src_image, int width, int height)
{
    cudaError_t error;

    error = cudaMallocArray(&a_Src, &uchar4tex, width, height);
    error = cudaMemcpy2DToArray(a_Src, 0, 0, *src_image, sizeof(uchar4) * width, sizeof(uchar4) * width, height, cudaMemcpyHostToDevice);

    cudaResourceDesc texRes;
    memset(&texRes, 0, sizeof(cudaResourceDesc));

    texRes.resType = cudaResourceTypeArray;
    texRes.res.array.array = a_Src;

    cudaTextureDesc texDescr;
    memset(&texDescr, 0, sizeof(cudaTextureDesc));

    texDescr.normalizedCoords = false;
    texDescr.filterMode = cudaFilterModeLinear;
    texDescr.addressMode[0] = cudaAddressModeWrap;
    texDescr.addressMode[1] = cudaAddressModeWrap;
    texDescr.readMode = cudaReadModeNormalizedFloat;

    checkCudaErrors(cudaCreateTextureObject(&texImage, &texRes, &texDescr, NULL));

    return error;
}

cudaError_t CUDA_FreeArray()
{
    return cudaFreeArray(a_Src);
}

////////////////////////////////////////////////////////////////////////////////
// Global data handlers and parameters
////////////////////////////////////////////////////////////////////////////////
// OpenGL PBO and texture "names"
GLuint gl_PBO;
GLuint gl_Tex;
struct cudaGraphicsResource* cuda_pbo_resource;  // handles OpenGL-CUDA exchange

// Source image on the host side
uchar4* source_image;
int W;
int H;

#define BUFFER_DATA(i) ((char *)0 + i)
#define REFRESH_DELAY 10  // ms

void display(void)
{
    printf("dis ");

    TColor* d_dst = NULL;
    size_t num_bytes;

    checkCudaErrors(cudaGraphicsMapResources(1, &cuda_pbo_resource, 0));
    getLastCudaError("cudaGraphicsMapResources failed");
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&d_dst, &num_bytes, cuda_pbo_resource));
    getLastCudaError("cudaGraphicsResourceGetMappedPointer failed");

    //printf("(%d) ", num_bytes);

    checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_resource, 0));

    glClear(GL_COLOR_BUFFER_BIT);

    glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, W, H, GL_RGBA, GL_UNSIGNED_BYTE, BUFFER_DATA(0));

    //以下這段為必要
    glBegin(GL_TRIANGLES);
    glTexCoord2f(0, 0);
    glVertex2f(-1, -1);
    glTexCoord2f(2, 0);
    glVertex2f(+3, -1);
    glTexCoord2f(0, 2);
    glVertex2f(-1, +3);
    glEnd();

    glFinish();

    glutSwapBuffers();
    glutReportErrors();
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
    }
}

void cleanup()
{
    printf("\ncleanup()\n");

    free(source_image);
    checkCudaErrors(CUDA_FreeArray());
    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_pbo_resource));
}

int initGL(int* argc, char** argv)
{
    printf("Initializing GLUT...\n");

    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);

    glutInitWindowSize(W, H); // 設定視窗大小
    glutInitWindowPosition(1100, 200); // 設定視窗位置

    glutCreateWindow("Image Denoising");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutKeyboardFunc(keyboard); //設定callback function
    glutCloseFunc(cleanup);     //設定callback function

    printf("OpenGL window created.\n");

    glewInit();
    printf("GLEW Version %s\n", glewGetString(GLEW_VERSION));

    return 0;
}

void initOpenGLBuffers()
{
    printf("Creating GL texture...\n");
    glEnable(GL_TEXTURE_2D);
    glGenTextures(1, &gl_Tex);	//生成紋理對象
    glBindTexture(GL_TEXTURE_2D, gl_Tex);	//綁定紋理

    //紋理濾波參數設置
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    /* 修改圖像資料
    for (int i = 0; i < W * H / 3; i++)
    {
        source_image[i].x = source_image[i].x / 2;
        source_image[i].y = source_image[i].y / 2;
        source_image[i].z = source_image[i].z / 2;
        source_image[i].w = source_image[i].w / 2;
    }
    */

    //在這裡把影像設定到pBox....
    //設置紋理數據
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, W, H, 0, GL_RGBA, GL_UNSIGNED_BYTE, source_image);

    printf("Texture created.\n");

    printf("Creating PBO...\n");
    glGenBuffers(1, &gl_PBO);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, gl_PBO);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, W * H * 4, source_image, GL_STREAM_COPY);

    checkCudaErrors(cudaGraphicsGLRegisterBuffer(&cuda_pbo_resource, gl_PBO, cudaGraphicsMapFlagsWriteDiscard));

    GLenum gl_error = glGetError();
    if (gl_error == GL_NO_ERROR)
    {
        printf("PBO created.\n");
    }
    else
    {
        printf("error");
        exit(EXIT_FAILURE);
    }
}

int main(int argc, char** argv)
{
    //自製圖片資料
    W = 640;
    H = 480;

    source_image = (uchar4*)malloc(W * H * 4);

    int i;
    int j;

    //在這裡製作圖片資料
    for (j = 0; j < H; j++)
    {
        for (i = 0; i < W; i++)
        {
            source_image[W * j + i].x = (i * j) % 256;   //R
            source_image[W * j + i].y = (i * j) % 256;   //G
            source_image[W * j + i].z = (i * j) % 256;   //B
        }
    }

    initGL(&argc, argv);
    findCudaDevice(argc, (const char**)argv);

    checkCudaErrors(CUDA_MallocArray(&source_image, W, H));

    initOpenGLBuffers();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

