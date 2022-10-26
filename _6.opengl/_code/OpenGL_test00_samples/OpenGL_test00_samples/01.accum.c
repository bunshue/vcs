//#include <helper_gl.h>
//#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

GLenum doubleBuffer;
GLint thing1, thing2, thing3, thing4;

void Init(void)
{
    //           R    G    B     A
    glClearColor(0.0, 0.0, 0.0, 0.0);   //設定背景色(0 0 0為黑色)

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

void display(void)
{
    glPushMatrix();

    glScalef(0.8, 0.8, 1.0);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing1);
    glAccum(GL_LOAD, 0.5);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing2);
    glAccum(GL_ACCUM, 0.5);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing3);
    glAccum(GL_ACCUM, 0.5);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing4);
    glAccum(GL_ACCUM, 0.5);

    glAccum(GL_RETURN, 1.0);

    glPopMatrix();

    if (doubleBuffer)
    {
        glutSwapBuffers();
    }
    else
    {
        glFlush();
    }
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case '1':
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        glutPostRedisplay();
        break;
    case '2':
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
    }
}

void Args(int argc, char** argv)
{
    GLint i;

    doubleBuffer = GL_FALSE;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-sb") == 0)
        {
            doubleBuffer = GL_FALSE;
        }
        else if (strcmp(argv[i], "-db") == 0)
        {
            doubleBuffer = GL_TRUE;
        }
    }
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);
    Args(argc, argv);

    type = GLUT_RGB | GLUT_ACCUM;
    type |= (doubleBuffer) ? GLUT_DOUBLE : GLUT_SINGLE;
    glutInitDisplayMode(type);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("顏色重疊測試");	//開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    printf("按 1 2 控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
