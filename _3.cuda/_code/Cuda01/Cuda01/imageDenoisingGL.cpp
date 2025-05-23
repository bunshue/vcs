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

////////////////////////////////////////////////////////////////////////////////
// Global data handlers and parameters
////////////////////////////////////////////////////////////////////////////////
// OpenGL PBO and texture "names"
GLuint gl_PBO, gl_Tex;
struct cudaGraphicsResource* cuda_pbo_resource;  // handles OpenGL-CUDA exchange

int mode = 4;   //0: 使用圖片640X480
                //1: 使用圖片1920X1080
                //2: 自製圖片資料1    circle
                //3: 自製圖片資料2    wave
                //4: 自製圖片資料2    sinewave

bool flag_use_cuda = true;

// Source image on the host side
uchar4* h_Src1;
uchar4* h_Src2;
int imageW;
int imageH;

////////////////////////////////////////////////////////////////////////////////
// Main program
////////////////////////////////////////////////////////////////////////////////
bool flag_print_fps_info = false;
StopWatchInterface* timer = NULL;

const int frameN = 24;
int frameCounter = 0;

#define BUFFER_DATA(i) ((char *)0 + i)

// Auto-Verification Code
int fpsCount = 0;  // FPS count for averaging
int fpsLimit = 1;  // FPS limit for sampling
unsigned int frameCount = 0;

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
        sprintf(fps, "%3.1f fps", ifps);

        glutSetWindowTitle(fps);
        fpsCount = 0;

        // fpsLimit = (int)MAX(ifps, 1.f);
        sdkResetTimer(&timer);
    }
}

void do_alpha_mixer(int alpha, TColor* d_dst)
{
    if (mode == 3)
    {
        cuda_Wave1(d_dst, alpha, imageW, imageH);
    }
    else if (mode == 4)
    {
        cuda_Wave2(d_dst, alpha, imageW, imageH);
    }
    else
    {
        cuda_Mix(d_dst, alpha, imageW, imageH, texImage1, texImage2);
    }
}

int flag_direction = 0;
int alpha = 0;
void runImageFilters(TColor* d_dst)
{
    do_alpha_mixer(alpha, d_dst);

    //glColor3f(0.46f, 0.73f, 0.0f);
    //glColor3f(1.0f, 0, 0);  //只留紅色系
    //glColor3f(0, 1.0f, 0);  //只留綠色系
    //glColor3f(0, 0, 1.0f);  //只留藍色系

    if (mode == 3)
    {
        alpha++;
    }
    else
    {
        if (flag_direction == 0)
        {
            alpha++;
            if (alpha > 100)
            {
                alpha = 100;
                flag_direction = 1;
            }
        }
        else
        {
            alpha--;
            if (alpha < 0)
            {
                alpha = 0;
                flag_direction = 0;
            }
        }
    }
    getLastCudaError("Filtering kernel execution failed.\n");
}

void display(void)
{
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

        if (flag_print_fps_info == true)
        {
            printf("FPS: %3.1f\n", frameN / (sdkGetTimerValue(&timer) * 0.001));
            flag_print_fps_info = false;
        }
    }

    glutSwapBuffers();
    glutReportErrors();

    sdkStopTimer(&timer);

    computeFPS();
}

void timerEvent(int value)
{
    //printf("t");
    if (glutGetWindow())
    {
        //printf("r");
        //printf("glutGetWindow ");
        glutPostRedisplay();
        glutTimerFunc(REFRESH_DELAY, timerEvent, 0);    //設定timer事件
    }
}

void reshape(int x, int y)
{
    printf("reshape\n");
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;

    case '1':
        printf("1\n");
        break;

    case '2':
        printf("2\n");
        break;

    case '3':
        break;

    case '4':
        break;

    case 'f':
    case 'F':
        flag_print_fps_info = true;
        break;

    case '?':
        break;
    }
}

int ox = 0, oy = 0;
int buttonState = 0;
float camera_trans[] = { 0, -2, -150 };
float camera_rot[] = { 0, 0, 0 };
float camera_trans_lag[] = { 0, -2, -150 };
float camera_rot_lag[] = { 0, 0, 0 };
const float inertia = 0.1f;

void mouse(int button, int state, int x, int y)
{
    int mods;

    if (state == GLUT_DOWN)
    {
        buttonState |= 1 << button;
    }
    else if (state == GLUT_UP)
    {
        buttonState = 0;
    }

    mods = glutGetModifiers();

    if (mods & GLUT_ACTIVE_SHIFT)
    {
        buttonState = 2;
    }
    else if (mods & GLUT_ACTIVE_CTRL)
    {
        buttonState = 3;
    }

    ox = x;
    oy = y;

    glutPostRedisplay();

    printf("(%d, %d, %d) ", buttonState, ox, oy);
}

void motion(int x, int y)
{
    float dx = (float)(x - ox);
    float dy = (float)(y - oy);

    if (buttonState == 3)
    {
        // left+middle = zoom
        camera_trans[2] += (dy / 100.0f) * 0.5f * fabs(camera_trans[2]);
    }
    else if (buttonState & 2)
    {
        // middle = translate
        camera_trans[0] += dx / 100.0f;
        camera_trans[1] -= dy / 100.0f;
    }
    else if (buttonState & 1)
    {
        // left = rotate
        camera_rot[0] += dy / 5.0f;
        camera_rot[1] += dx / 5.0f;
    }
    ox = x;
    oy = y;
    glutPostRedisplay();
}

void idle(void)
{
    glutPostRedisplay();
}

int initGL(int* argc, char** argv)
{
    printf("Initializing GLUT...\n");
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);

    glutInitWindowSize(imageW, imageH); //設定視窗大小, 直接拉大內容
    if (imageW > 1200)
    {
        glutInitWindowPosition(0, 0);   //視窗起始位置
    }
    else
    {
        glutInitWindowPosition(1100, 200);   //視窗起始位置
    }

    glutCreateWindow("CUDA window system"); //開啟視窗 並顯示出視窗 Title
    //glutCreateWindow("CUDA window system"); //開啟視窗 並顯示出視窗 Title //顯示多個視窗
    //glutCreateWindow("CUDA window system"); //開啟視窗 並顯示出視窗 Title //顯示多個視窗

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    glutMouseFunc(mouse);           //設定callback function
    glutMotionFunc(motion);         //設定callback function
    glutIdleFunc(idle);		//設定callback function, 利用idle事件進行重畫
    glutCloseFunc(cleanup);         //設定callback function

    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);    //設定timer事件

    printf("OpenGL window created.\n");

    glewInit();	//OpenGL Extension Wrangler Library （GLEW） 跨平台C/C++擴展庫 初始化
    return 0;
}

void initOpenGLBuffers()
{
    printf("Creating GL texture...\n");
    glEnable(GL_TEXTURE_2D);
    glGenTextures(1, &gl_Tex);	//生成紋理對象
    glBindTexture(GL_TEXTURE_2D, gl_Tex);	//綁定紋理
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

    //在這裡把影像設定到pBox....
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
    if (mode == 2)
    {
        //自製圖片資料
        imageW = 512;
        imageH = 512;

        h_Src1 = (uchar4*)malloc(imageW * imageH * 4);
        h_Src2 = (uchar4*)malloc(imageW * imageH * 4);

        int i;
        int j;

        for (j = 0; j < imageH; j++)
        {
            for (i = 0; i < imageW; i++)
            {
                h_Src1[imageW * j + i].x = (i * j) % 256;   //R
                h_Src1[imageW * j + i].y = (i * j) % 256;   //G
                h_Src1[imageW * j + i].z = (i * j) % 256;   //B

                h_Src2[imageW * j + i].x = (i / 2) % 256;   //R
                h_Src2[imageW * j + i].y = (i / 2) % 256;   //G
                h_Src2[imageW * j + i].z = (i / 2) % 256;   //B
            }
        }
    }
    else if (mode == 3)
    {
        //自製圖片資料
        imageW = 1920;
        imageH = 1080;

        h_Src1 = (uchar4*)malloc(imageW * imageH * 4);
        h_Src2 = (uchar4*)malloc(imageW * imageH * 4);

        int i;
        int j;

        for (j = 0; j < imageH; j++)
        {
            for (i = 0; i < imageW; i++)
            {
                h_Src1[imageW * j + i].x = (i * j) % 256;   //R
                h_Src1[imageW * j + i].y = (i * j) % 256;   //G
                h_Src1[imageW * j + i].z = (i * j) % 256;   //B

                h_Src2[imageW * j + i].x = (i / 2) % 256;   //R
                h_Src2[imageW * j + i].y = (i / 2) % 256;   //G
                h_Src2[imageW * j + i].z = (i / 2) % 256;   //B
            }
        }


    }
    else
    {
        char* filename_read1 = ""; //24 bits
        char* filename_read2 = ""; //24 bits

        //讀取圖片資料
        if (mode == 0)  //小圖
        {
            //使用圖片640X480
            filename_read1 = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims01.24.bmp"; //24 bits
            filename_read2 = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims03.24.bmp"; //24 bits
        }
        else  //mode 1 大圖
        {
            //使用圖片1920X1080
            filename_read1 = "C:\\_git\\vcs\\_1.data\\______test_files1\\__pic\\_ggb\\ggb1.bmp"; //24 bits
            filename_read2 = "C:\\_git\\vcs\\_1.data\\______test_files1\\__pic\\_ggb\\ggb2.bmp"; //24 bits
        }

        imageW = 0;
        imageH = 0;
        LoadBMPFile(&h_Src1, &imageW, &imageH, filename_read1);
        printf("filename : %s\tW = %d\tH = %d\n", filename_read1, imageW, imageH);

        imageW = 0;
        imageH = 0;
        LoadBMPFile(&h_Src2, &imageW, &imageH, filename_read2);
        printf("filename : %s\tW = %d\tH = %d\n", filename_read2, imageW, imageH);
    }

    initGL(&argc, argv);
    findCudaDevice(argc, (const char**)argv);

    checkCudaErrors(CUDA_MallocArray(&texImage1, &h_Src1, imageW, imageH));
    checkCudaErrors(CUDA_MallocArray(&texImage2, &h_Src2, imageW, imageH));

    initOpenGLBuffers();
    //glutSetWindowTitle("ims pic");
    sdkCreateTimer(&timer);
    sdkStartTimer(&timer);

    //glutFullScreen();   //全螢幕顯示

    glutMainLoop();	//開始主循環繪製
}
