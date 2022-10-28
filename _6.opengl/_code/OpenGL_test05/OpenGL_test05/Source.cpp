#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);   //設置窗口坐標系大小, 3D
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0); //窗口坐標範圍, 2D

    //畫一個矩形 R
    //glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R, RGBA
    glColor3f(0.0, 1.0, 0.0);   //設置畫筆顏色為 G, RGB

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

    glFlush();//保證前面的OpenGL命令立即執行   glFlush​​負責刷新繪製緩沖器，保證繪圖命令立即執行。
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

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
    glutInitWindowPosition(1100, 200);	//視窗起始位置

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}


