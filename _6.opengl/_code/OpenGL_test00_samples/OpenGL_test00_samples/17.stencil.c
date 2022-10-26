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

    //����T����
    glStencilFunc(GL_ALWAYS, 1, 1);
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);

    glColor3ub(255, 0, 0);
    glBegin(GL_POLYGON);
    glVertex3i(-4, -4, 0);
    glVertex3i(4, -4, 0);
    glVertex3i(0, 4, 0);
    glEnd();

    //���x�� ����ܻP�T���έ��|����
    glStencilFunc(GL_EQUAL, 1, 1);
    glStencilOp(GL_INCR, GL_KEEP, GL_DECR);

    glColor3ub(0, 255, 0);
    glBegin(GL_POLYGON);
    glVertex3i(4, 3, 0);
    glVertex3i(-4, 3, 0);
    glVertex3i(-4, -3, 0);
    glVertex3i(4, -3, 0);
    glEnd();

    //�Ŧ�x�� ����ܦb�T���Ϋ᭱
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

    glutCreateWindow("Stencil Test");	//�}�ҵ��� ����ܥX���� Title

    Init();

    glutDisplayFunc(display);       //�]�wcallback function
    glutReshapeFunc(reshape);       //�]�wcallback function
    glutKeyboardFunc(keyboard);     //�]�wcallback function

    printf("�����, �L����, �� Esc ���}\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
