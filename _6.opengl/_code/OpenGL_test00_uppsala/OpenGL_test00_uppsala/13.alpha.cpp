/*
 *  alpha.c
 *  This program draws several overlapping filled polygons
 *  to demonstrate the effect order has on alpha blending results.
 */

#include "../../Common.h"

 /*  Initialize alpha blending function.  */

void myinit(void)
{
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glShadeModel(GL_FLAT);
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glColor4f(1.0, 1.0, 0.0, 0.75);
    glRectf(0.0, 0.0, 0.5, 1.0);

    glColor4f(0.0, 1.0, 1.0, 0.75);
    glRectf(0.0, 0.0, 1.0, 0.5);
    /*	draw colored polygons in reverse order in upper right  */
    glColor4f(0.0, 1.0, 1.0, 0.75);
    glRectf(0.5, 0.5, 1.0, 1.0);

    glColor4f(1.0, 1.0, 0.0, 0.75);
    glRectf(0.5, 0.5, 1.0, 1.0);

    glutSwapBuffers();
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
    {
        gluOrtho2D(0.0, 1.0, 0.0, (GLfloat)h / (GLfloat)w);
    }
    else
    {
        gluOrtho2D(0.0, (GLfloat)w / (GLfloat)h, 0.0, 1.0);
    }
    glMatrixMode(GL_MODELVIEW);
}

/*  Main Loop
 *  Open window with initial window size, title bar,
 *  RGBA display mode, and handle input events.  */
int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Alpha Blending");

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    myinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
