/*
 *  alpha.c
 *  This program draws several overlapping filled polygons
 *  to demonstrate the effect order has on alpha blending results.
 */

#include "../../Common.h"

 /*  Initialize alpha blending function.  */

void myinit(void)
{
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0);

    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glShadeModel(GL_FLAT);
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glColor4f(1.0, 0.0, 0.0, 0.5); //R
    glRectf(-0.6f, -0.2f, 0.6f, 0.8f);

    glColor4f(0.0, 1.0, 0.0, 0.5); //G
    glRectf(-0.8f, -0.8f, 0.2f, 0.5f);

    glColor4f(0.0, 0.0, 1.0, 0.5); //B
    glRectf(-0.2f, -0.8f, 0.8f, 0.5f);

    glColor4f(1.0, 0.0, 0.0, 1.0);
    glRectf(0.33f, 0.33f, 0.66f, 0.66f);

    glFlush();  // 執行繪圖命令
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv)
{
    const char* windowName = "Alpha Blending";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";

    common_setup(argc, argv, windowName, message, display, reshape, keyboard0);

    //先保留
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA);

    myinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
