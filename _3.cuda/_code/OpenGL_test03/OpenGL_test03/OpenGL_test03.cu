// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <GL/glut.h>  //32位元用的

GLubyte rasters[24] = {
   0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00,
   0xff, 0x00, 0xff, 0x00, 0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00,
   0xff, 0xc0, 0xff, 0xc0 };

void init(void)
{
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

/*
void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z = 0, GLdouble w = 1);
void glRasterPos4dv(const GLdouble* v);
//確定當前光柵位置，x,y,z,w指定了當前光柵位置的坐標

glWindowPos(Type x, Type y, Type z);
//用窗口坐標指定當前光柵位置，不必進行矩陣變換、裁剪、或紋理坐標生成。z值被變換為由glDepthRange()設置的當前近側平面值和遠側平面值

void glBitmap(GLsizei, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat, GLfloat, const GLubyte* bitmap);
//繪制由bitmap指定的位圖，bitmap是一個指向位圖圖像的指針，位圖的原點是當前光柵位置，如果當前光柵位置無效，則這個函數不會繪制任何東西。
//width和height表示位圖的寬度和高度，xorig和yorig定義了位圖的原點，他是根據當期光柵位置確定的，右上為正。
//xmove和ymove表示位圖光柵化之后光柵坐標的x增加值和y增加值
*/

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f(1.0, 0.0, 0.0);
    glRasterPos2i(100, 300);//确定当前光栅位置，x,y,z,w指定了当前光栅位置的坐标
    glBitmap(10, 12, 0.0, 0.0, 11.0, 0.0, rasters);

    glColor3f(0.0, 1.0, 0.0);
    glRasterPos2i(100, 200);//确定当前光栅位置，x,y,z,w指定了当前光栅位置的坐标
    glBitmap(10, 12, 0.0, 0.0, 11.0, 0.0, rasters);

    glColor3f(0.0, 0.0, 1.0);
    glRasterPos2i(100, 100);//确定当前光栅位置，x,y,z,w指定了当前光栅位置的坐标
    glBitmap(10, 12, 0.0, 0.0, 11.0, 0.0, rasters);

    //绘制由bitmap指定的位图，bitmap是一个指向位图图像的指针，位图的原点是当前光栅位置，如果当前光栅位置无效，则这个函数不会绘制任何东西。
    //width和height表示位图的宽度和高度，xorig和yorig定义了位图的原点，他是根据当期光栅位置确定的，右上为正。
    //xmove和ymove表示位图光栅化之后光栅坐标的x增加值和y增加值
    glFlush();
}

void reshape(int w, int h)
{
    glViewport(0, 0, (GLsizei)w, (GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, w, 0, h, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        exit(0);
    }
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("測試Bipmap");

    init();

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);

    glutMainLoop();

    return 0;
}

