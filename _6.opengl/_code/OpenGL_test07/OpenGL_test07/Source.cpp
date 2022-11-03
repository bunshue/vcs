#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>
#include "../../Common.h"

// 初始化參數
void init()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_PROJECTION);
    glOrtho(-5, 5, -5, 5, 5, 15);
    glMatrixMode(GL_MODELVIEW);
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0);
}

// 繪圖回調函數
void display(void)
{
    //畫一個茶壺
    float color_red[4] = { 1.0f, 0.0f, 0.0f, 1.0f };
    draw_teapot(color_red, 1.0, 2.0);

    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    init();

    glutDisplayFunc(display);	    //設定callback function
    glutKeyboardFunc(keyboard0);	//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}


