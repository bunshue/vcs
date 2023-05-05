#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "imageDenoising.h"

// OpenGL PBO and texture "names"
GLuint gl_PBO;
GLuint gl_Tex;

// Source image
uchar4* h_Src1;
int imageW;
int imageH;

int picture_select = 0;

#define BUFFER_DATA(i) ((char *)0 + i)

void cleanup();

void runImageFilters(TColor* d_dst)
{
    //printf("%d ", picture_select);
    switch (picture_select)
    {
    case 0:
        break;

    case 1:

        break;

    case 2:

        break;

    case 3:

        break;

    case 10:
        picture_select = 0;
        break;

    case 11:
        printf("Copy ims 01\n");


        picture_select = 0;
        break;

    case 13:
        printf("Copy ims 03\n");


        picture_select = 0;
        break;
    }
}

void display(void)
{
    //printf("dis ");

    TColor* d_dst = NULL;

    //修改圖像專用
    //runImageFilters(d_dst);

    // Common display code path
    {
        glClear(GL_COLOR_BUFFER_BIT);

        glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, imageW, imageH, GL_RGBA, GL_UNSIGNED_BYTE, BUFFER_DATA(0));

        //畫三角形? 可能沒需要
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

    glutSwapBuffers();
    glutReportErrors();
}

void keyboard(unsigned char k, int /*x*/, int /*y*/)
{
    switch (k)
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
        printf("3\n");
        break;
    }
}

int initGL(int* argc, char** argv)
{
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);

    glutInitWindowSize(imageW, imageH);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Show bmp");

    glutDisplayFunc(display);   //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    glutCloseFunc(cleanup);

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

    /* 修改圖像資料
    for (int i = 0; i < imageW * imageH / 3; i++)
    {
        h_Src1[i].x = h_Src1[i].x / 2;
        h_Src1[i].y = h_Src1[i].y / 2;
        h_Src1[i].z = h_Src1[i].z / 2;
        h_Src1[i].w = h_Src1[i].w / 2;
    }
    */

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, imageW, imageH, 0, GL_RGBA, GL_UNSIGNED_BYTE, h_Src1);

    printf("Texture created.\n");

    printf("Creating PBO...\n");
    glGenBuffers(1, &gl_PBO);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, gl_PBO);
    glBufferData(GL_PIXEL_UNPACK_BUFFER_ARB, imageW * imageH * 4, h_Src1, GL_STREAM_COPY);

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
}

int main(int argc, char** argv)
{
    //const char* filename_read1 = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims01.bmp"; //32 bits
    const char* filename_read1 = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims01.24.bmp"; //24 bits
    //const char* filename_read2 = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims03.24.bmp"; //24 bits

    imageW = 0;
    imageH = 0;
    LoadBMPFile(&h_Src1, &imageW, &imageH, filename_read1);
    printf("filename : %s\tW = %d\tH = %d\n", filename_read1, imageW, imageH);

    initGL(&argc, argv);

    initOpenGLBuffers();

    glutSetWindowTitle("ims pic");

    glutMainLoop();	//開始主循環繪製
}

