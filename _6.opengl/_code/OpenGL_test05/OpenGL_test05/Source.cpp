#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// 初始化參數
void init()
{
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //GLAPI void GLAPIENTRY glOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar);
    //glOrtho(-2, 2, -2, 2, -2, 2);   //設置窗口坐標系大小

    //glOrtho(-2.0, 2.0, -2.0, 2.0, -1.0, 1.0);   //設置窗口坐標系大小
    //glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);   //設置窗口坐標系大小
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0); //窗口坐標範圍

    //畫一個矩形 R
    glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R

    float ww = 1.0f / 2;
    float hh = 1.0f / 2;

    float x_st = 0.0f;
    float y_st = 0.0f;
    float dx = 1.0f / 2;
    float dy = 1.0f / 2;
    for (x_st = -1.0; x_st < 1.0; x_st += dx)
    {
        y_st = x_st;
        glRectf(x_st, y_st, x_st + ww, y_st + hh);  //畫一個矩形
    }

    glFlush();//保證前面的OpenGL命令立即執行   glFlush​​負責刷新繪制緩沖器，保證繪圖命令立即執行。
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
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
    }
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    //glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
    glutInitWindowPosition(1100, 200);	//視窗起始位置

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    init();

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function

    // 開始主循環繪制
    glutMainLoop();

    return 0;
}


