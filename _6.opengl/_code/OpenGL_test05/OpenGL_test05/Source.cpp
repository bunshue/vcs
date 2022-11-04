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

typedef struct _cRec {
    float x, y;
} cRec;

int cCount = 0;
cRec cList[10];


void SetPoint(float x, float y)
{
    if (cCount < 10)
    {
        cList[cCount].x = x;
        cList[cCount].y = y;
        cCount++;
    }
}

void DrawPoint(void)
{
    int i;

    for (i = 0; i < 10; i++)
    {
        SetPoint(((float)i) / 10, ((float)i) / 10);
    }

    glColor3f(1.0, 1.0, 0.0);
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

    float width = 3;
    float x1 = 0;
    float y1 = 0.3;
    float x2 = 0.3;
    float y2 = -0.3;
    float x3 = -0.3;
    float y3 = -0.3;
    //draw_triangle(color_yellow, width, x1, y1, x2, y2, x3, y3);

    draw_point_test();

    DrawPoint();

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
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
        break;

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

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
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
    glutKeyboardFunc(keyboard); //設定callback function
    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

