#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

void Init(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);

    glClearStencil(0);
    glStencilMask(1);
    glEnable(GL_STENCIL_TEST);
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);

    //紅色三角形
    glStencilFunc(GL_ALWAYS, 1, 1);
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);

    glColor3ub(255, 0, 0);
    glBegin(GL_POLYGON);
    glVertex3i(-4, -4, 0);
    glVertex3i(4, -4, 0);
    glVertex3i(0, 4, 0);
    glEnd();

    //綠色矩形 僅顯示與三角形重疊部分
    glStencilFunc(GL_EQUAL, 1, 1);
    glStencilOp(GL_INCR, GL_KEEP, GL_DECR);

    glColor3ub(0, 255, 0);
    glBegin(GL_POLYGON);
    glVertex3i(4, 3, 0);
    glVertex3i(-4, 3, 0);
    glVertex3i(-4, -3, 0);
    glVertex3i(4, -3, 0);
    glEnd();

    //藍色矩形 僅顯示在三角形後面
    glStencilFunc(GL_EQUAL, 1, 1);
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP);

    glColor3ub(0, 0, 255);
    glBegin(GL_POLYGON);
    glVertex3i(3, 2, 0);
    glVertex3i(-3, 2, 0);
    glVertex3i(-3, -2, 0);
    glVertex3i(3, -2, 0);
    glEnd();

    glFlush();
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-5.0, 5.0, -5.0, 5.0, -5.0, 5.0);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        exit(0);
    }
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);

    type = GLUT_RGB | GLUT_STENCIL;
    type |= GLUT_SINGLE;

    glutInitDisplayMode(type);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Stencil Test");	//開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
