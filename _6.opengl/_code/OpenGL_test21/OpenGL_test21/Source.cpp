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

typedef struct _cRec {
    float x, y;
} cRec;

cRec cList[50];
int cCount = 0;

void SetPoint(float x, float y)
{
    cList[cCount].x = x;
    cList[cCount].y = y;
    cCount++;
}

void DrawPoint(void)
{
    int i;

    printf("DrawPoint()\n");

    printf("Make some data\n");

    cCount = 0;

    float x;
    float y;
    for (i = 0; i < 50; i++)
    {
        x = -1.0 + 2.0 * i / 50;
        y = sin(x * 4) / 2;
        SetPoint(x, y);
    }

    glColor3f(1.0, 0.0, 1.0);
    glPointSize(10.0f); 	//設定點的大小, N X N
    glBegin(GL_POINTS);
    for (i = 0; i < cCount; i++)
    {
        glVertex2f(cList[i].x, cList[i].y);
    }
    glEnd();

    glFlush();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //畫視窗邊界
    float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
    draw_boundary(color_yellow, 0.9);

    DrawPoint();

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
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
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function
    glutMouseFunc(mouse0);       //設定callback function
    glutMotionFunc(motion0);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

