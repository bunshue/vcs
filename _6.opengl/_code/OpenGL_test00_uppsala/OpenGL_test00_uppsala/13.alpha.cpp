/*
 *  alpha.c
 *  This program draws several overlapping filled polygons
 *  to demonstrate the effect order has on alpha blending results.
 */

#include "../../Common.h"

 /*  Initialize alpha blending function.  */

void myinit(void)
{
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0);   //���f�y�нd��2D, ��ܽd�� : X�b(-1.0 ~ 1.0) Y�b(-1.0 ~ 1.0), ���U�����I

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

    glFlush();  // ����ø�ϩR�O
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
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    myinit();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
