//#include <helper_gl.h>
//#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../Common.h"

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

void draw_point_test(void)
{
    //畫點
    glPointSize(20.0f);	//設定點的大小, N X N
    glBegin(GL_POINTS);
    for (float i = 1; i < 8; i+=2)
    {
        float j = i * 1/10;

        glColor3f(1.0, 0.0, 0.0);	//紅

        glVertex2f(-j, -j);
        glVertex2f(-j, 0);
        glVertex2f(-j, j);
        glVertex2f(0, j);
        glVertex2f(j, j);
        glVertex2f(j, 0);
        glVertex2f(j, -j);
        glVertex2f(0, -j);
    }
    glEnd();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9); //畫視窗邊界

    float width = 3;
    float x1 = 0;
    float y1 = 0.3;
    float x2 = 0.3;
    float y2 = -0.3;
    float x3 = -0.3;
    float y3 = -0.3;
    //draw_triangle(color_y, width, x1, y1, x2, y2, x3, y3);

    draw_point_test();

    //畫多邊形
    glColor3f(0.2f, 0.6f, 0.5f);    //設定顏色
    glBegin(GL_POLYGON);
    {
        //多邊形的頂點數：數越大越趨近于圓
        const int n = 10;
        const GLfloat R = 0.3f;
        const GLfloat pi = 3.1415926f;
        for (int i = 0; i < n; i++)
        {
            glVertex2f(R * cos(2 * pi / n * i), R * sin(2 * pi / n * i));
        }
    }
    glEnd();

    //畫實心矩形
    float dd = 0.15;
    glBegin(GL_QUADS);              //矩形
    {
        glColor3f(0.0f, 0.0f, 1.0f); //設定顏色, B
        glVertex2f(-dd, -dd);    // x, y
        glVertex2f(dd, -dd);
        glVertex2f(dd, dd);
        glVertex2f(-dd, dd);
    }
    glEnd();


    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    //初始化GLUT庫，這個函數只是傳說命令參數并且初始化glut庫
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("OpenGL測試");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function
    glutMouseFunc(mouse0);       //設定callback function
    glutMotionFunc(motion0);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

