#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#define CI_OFFSET 16

GLenum mode1 = GL_FALSE;
GLenum mode2 = GL_FALSE;
GLint size = 1;

float pntA[3] = {
    -160.0, 0.0, 0.0
};

float pntB[3] = {
    -130.0, 0.0, 0.0
};

float pntC[3] = {
    -40.0, -50.0, 0.0
};

float pntD[3] = {
    30.0, 60.0, 0.0
};

void Init(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);

    glLineStipple(1, 0xF0E0);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE);
}

void display(void)
{
    GLint ci, i;

    glClear(GL_COLOR_BUFFER_BIT);

    glLineWidth((float)size);      //���G�u�e�̤j��10
    printf("%d ", size);

    if (mode1 == 1)
    {
        glEnable(GL_LINE_STIPPLE);
    }
    else
    {
        glDisable(GL_LINE_STIPPLE);
    }

    if (mode2 == 1)
    {
        ci = CI_OFFSET;
        glEnable(GL_LINE_SMOOTH);
        glEnable(GL_BLEND);
    }
    else
    {
        ci = 3;
        glDisable(GL_LINE_SMOOTH);
        glDisable(GL_BLEND);
    }

    glPushMatrix();

    for (i = 0; i < 360; i += 5)
    {
        glRotatef(5.0, 0, 0, 1);

        glColor3f(1.0, 0.0, 0.0);   //�]�w�C��  //R, ���u
        glBegin(GL_LINE_STRIP);
        glVertex3fv(pntA);
        glVertex3fv(pntB);
        glEnd();

        glPointSize(10.0f); 	//�]�w�I���j�p, N X N
        glColor3f(0.0, 1.0, 0.0);   //�]�w�C��  //G, ���I
        glBegin(GL_POINTS);
        glVertex3fv(pntA);
        glVertex3fv(pntB);
        glEnd();
    }

    glPopMatrix();

    glFlush();
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-175, 175, -175, 175);	//���f�y�нd��, 2D
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case '1':
        mode1 = 1 - mode1;
        glutPostRedisplay();
        break;
    case '2':
        mode2 = 1 - mode2;
        glutPostRedisplay();
        break;
    case 27:
    case 'q':
    case 'Q':
        //���}����
        glutDestroyWindow(glutGetWindow());
        return;
    }
}

void special(int key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case GLUT_KEY_UP:
        //printf("�A���F �W ");
        size++;
        if (size > 10)
            size = 10;
        glutPostRedisplay();
        break;
    case GLUT_KEY_DOWN:
        //printf("�A���F �U ");
        size--;
        if (size < 1)
        {
            size = 1;
        }
        glutPostRedisplay();
        break;
    }
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //�ŧi��ܼҦ��� Single Buffer �M RGBA

    glutInitWindowSize(600, 600);       // �]�w�����j�p
    glutInitWindowPosition(1100, 200);  // �]�w������m

    glutCreateWindow("Line Test");	//�}�ҵ��� ����ܥX���� Title

    Init();

    glutDisplayFunc(display);       //�]�wcallback function
    glutReshapeFunc(reshape);       //�]�wcallback function
    glutKeyboardFunc(keyboard);     //�]�wcallback function
    glutSpecialFunc(special);       //�]�wcallback function

    printf("�� �W �U ����, ���W�ܲʽu, ���U�ܲӽu\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
