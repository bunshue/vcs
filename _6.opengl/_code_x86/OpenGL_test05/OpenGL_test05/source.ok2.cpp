// OpenGL Graphics includes
#include <helper_gl.h>

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//#include <GL/freeglut.h>	//64位元用的
#include <GL/glut.h>		//32位元用的

//  main.cpp
//  opengl_progress_struct

//#include <GLUT/GLUT.h>
//#include <OpenGL/OpenGL.h>

// 初始化參數
void init()
{
    glClearColor(0.1, 0.1, 0.4, 0.0);
    glShadeModel(GL_SMOOTH);
}

// 繪圖回調函數
void display()
{
    //printf("d ");
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT);

    // 繪制三角形
    glBegin(GL_TRIANGLES);
    glColor3f(1, 0, 0);     //紅
    glVertex3f(-2, -2, -5); //左下

    glColor3f(0, 1, 0);     //綠
    glVertex3f(2, -2, -5);  //右下

    glColor3f(0, 0, 1);     //藍
    glVertex3f(0, 2, -5);   //上
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
        break;

    case '4':
        break;

    case '?':
        break;
    }
}

int main(int argc, char** argv)
{
    // 初始化顯示模式
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    // 初始化窗口
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Color Map");

    init();

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function

    // 開始主循環繪制
    glutMainLoop();
    return 0;
}

