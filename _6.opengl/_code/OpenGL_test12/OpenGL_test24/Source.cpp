﻿#include "../../Common.h"

#define SIZE 600

int pointsChosen;
int x_st;
int y_st;
int numberOfLists = 0;
GLsizei ysize;

void gfxinit()
/* This is the routine that initializes some graphics parameters. */
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);
    glClearColor(1.0, 1.0, 1.0, 0.0);  /* make the background white */
    glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
    glColor3d(0.0, 0.0, 0.0);          /* initial drawing color is black */
    glLineWidth(1.0);                  /* initial thickness is 1 */
    glEndList();
    pointsChosen = 0;
    ysize = SIZE - 1;
}

// 繪圖回調函數
void display(void)
{
    int i;

    glClear(GL_COLOR_BUFFER_BIT);
    for (i = 1; i <= numberOfLists; i++)
    {
        glCallList(i);
    }
    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
/*
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}
*/

/* This function gets called whenever the window is resized. */
void reshape(GLsizei w, GLsizei h)
{
    /* Adjust the clipping rectangle. */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, w - 1, 0.0, h - 1);
    ysize = h - 1;

    /* Adjust the viewport. */

    glViewport(0, 0, w, h);
}

void mouse(int button, int state, int x, int y)
{
    if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN))
    {
        if (pointsChosen == 0)
        {
            x_st = x;
            y_st = ysize - y;
            pointsChosen = 1;
            printf("第1點(%d, %d) ", x_st, y_st);
        }
        else
        {
            glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
            glBegin(GL_LINES);
            glVertex2i(x_st, y_st);
            glVertex2i(x, ysize - y);
            glEnd();
            glEndList();
            glFlush();
            pointsChosen = 0;
            printf("第2點(%d, %d) ", x, ysize - y);
        }
    }
}

int main(int argc, char** argv)
{
    const char* windowName = "點選兩點連線";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    glutMouseFunc(mouse);       //設定callback function

    gfxinit();

    printf("\n點選兩點連線\n");

    printf("\n有誤差\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

