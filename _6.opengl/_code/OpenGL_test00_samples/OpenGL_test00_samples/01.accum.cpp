#include "../../Common.h"

float alpha = 0.5;
GLint thing1;
GLint thing2;
GLint thing3;
GLint thing4;

void Init(void)
{
    //           R    G    B     A
    glClearColor(0.0, 0.0, 0.0, 0.0);   //�]�w�I����(0 0 0���¦�)

    glClearAccum(0.0, 0.0, 0.0, 0.0);

    thing1 = glGenLists(1);
    glNewList(thing1, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);   //R
    glRectf(-1.0, -0.8, 1.0, 0.8);
    glEndList();

    thing2 = glGenLists(1);
    glNewList(thing2, GL_COMPILE);
    glColor3f(0.0, 1.0, 0.0);   //G
    glRectf(-0.8, -1.0, 0.2, 1.0);
    glEndList();

    thing3 = glGenLists(1);
    glNewList(thing3, GL_COMPILE);
    glColor3f(0.0, 0.0, 1.0);   //B
    glRectf(-0.2, -1.0, 0.8, 1.0);

    /*
    thing4 = glGenLists(1);
    glNewList(thing4, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);   //xxxx
    glRectf(-1.2, -1.2, 1.2, 1.2);
    */

    glEndList();
}

// ø�Ϧ^�ը��
void display(void)
{
    glPushMatrix();	//�o�� Matrix Push/Pop �n���S�����??

    glScalef(0.8, 0.8, 0.8);	//X Y Z�Ҧ���ӵ�������� �̤j��1.0 �N�O100%

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing1);
    glAccum(GL_LOAD, alpha);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing2);
    glAccum(GL_ACCUM, alpha);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing3);
    glAccum(GL_ACCUM, alpha);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing4);
    glAccum(GL_ACCUM, alpha);
    
    /*
    char mesg[20];
    //sprintf(mesg, "Alpha = %3.3f", alpha);	//�L��, x64�����
    sprintf_s(mesg, sizeof(info), "Alpha = %3.3f", alpha);
    glutSetWindowTitle(mesg);
    */

    alpha += 0.1;
    if (alpha > 1.01)
    {
        alpha = 0;
    }

    glAccum(GL_RETURN, 1.0);

    glPopMatrix();

    glFlush();
}

// ���f�j�p�ܤƦ^�ը��
void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//�]�m���x�}
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//�]�m���x�}
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case '1':
        printf("�e��ߦ��\n");
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        glutPostRedisplay();	//����display()
        break;
    case '2':
        printf("�e�Ťߦ��(�~��)\n");
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        glutPostRedisplay();	//����display()
        break;
    case 'r':
        printf("���e alpha = %f ", alpha);
        glutPostRedisplay();	//����display()
        break;
    case 27:
        exit(0);
    }
}

int main(int argc, char** argv)
{
    const char* windowName = "�C�⭫�|����";
    const char* message = "�C�⭫�|����\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutInitDisplayMode(GLUT_RGB | GLUT_ACCUM | GLUT_SINGLE);

    Init();

    printf("�� 1 2 r ����\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
