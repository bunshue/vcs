// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <GL/glut.h>  //32位元用的

//  main.cpp
//  opengl_progress_struct

//#include <GLUT/GLUT.h>
//#include <OpenGL/OpenGL.h>

// 初始化參數
void init() {
    glClearColor(0.1, 0.1, 0.4, 0.0);
    glShadeModel(GL_SMOOTH);
}

// 繪圖回調函數
void display()
{
    printf("d ");
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT);

    // 繪制三角形
    glBegin(GL_TRIANGLES);
    glColor3f(1, 0, 0);
    glVertex3f(-1, -1, -5);
    glColor3f(0, 1, 0);
    glVertex3f(1, -1, -5);
    glColor3f(0, 0, 1);
    glVertex3f(0, 1, -5);
    glEnd();
    // 執行繪圖命令
    glFlush();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, const char* argv[])
{
    // 初始化顯示模式
    glutInit(&argc, const_cast<char**>(argv));
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    // 初始化窗口
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Color Map");

    init();

    glutReshapeFunc(reshape);
    glutDisplayFunc(display);

    // 開始主循環繪制
    glutMainLoop();
    return 0;
}

