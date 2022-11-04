//#include <helper_gl.h>
//#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#define CI_OFFSET_1 16
#define CI_OFFSET_2 32

GLenum rgb;
GLenum antiAlias;
GLenum stipple;

GLubyte stippleBits[32 * 4] = {
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
    0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
};

void Init(void)
{
    GLint i;

    if (!rgb)
    {
        for (i = 0; i < 16; i++)
        {
            glutSetColor(i + CI_OFFSET_1, 0.0, 0.0, i / 15.0);
            glutSetColor(i + CI_OFFSET_2, 0.0, i / 15.0, 0.0);
        }
    }

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClearIndex(0.0);

    glPolygonStipple(stippleBits);

    antiAlias = GL_FALSE;
    stipple = GL_FALSE;
}

void display(void)
{
    GLint ci1, ci2;

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    if (antiAlias)
    {
        ci1 = CI_OFFSET_1;
        ci2 = CI_OFFSET_2;
        glBlendFunc(GL_SRC_ALPHA, GL_ONE);
        glEnable(GL_BLEND);
        glEnable(GL_POLYGON_SMOOTH);
        glDisable(GL_DEPTH_TEST);
    }
    else
    {
        ci1 = 4;
        ci2 = 2;
        glDisable(GL_BLEND);
        glDisable(GL_POLYGON_SMOOTH);
        glEnable(GL_DEPTH_TEST);
    }

    if (stipple)
    {
        glEnable(GL_POLYGON_STIPPLE);
    }
    else
    {
        glDisable(GL_POLYGON_STIPPLE);
    }

    glBegin(GL_TRIANGLES);
    (rgb) ? glColor3f(0.0, 0.0, 1.0) : glIndexi(ci1);
    glVertex3f(0.9, -0.9, -30.0);
    glVertex3f(0.9, 0.9, -30.0);
    glVertex3f(-0.9, 0.0, -30.0);
    (rgb) ? glColor3f(0.0, 1.0, 0.0) : glIndexi(ci2);
    glVertex3f(-0.9, -0.9, -40.0);
    glVertex3f(-0.9, 0.9, -40.0);
    glVertex3f(0.9, 0.0, -25.0);
    glEnd();

    glFlush();
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-1.0, 1.0, -1.0, 1.0, -0.5, 1000.0);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case '1':
        antiAlias = !antiAlias;
        glutPostRedisplay();
        break;
    case '2':
        stipple = !stipple;
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
    }
}

void Args(int argc, char** argv)
{
    GLint i;

    rgb = GL_TRUE;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-ci") == 0)
        {
            rgb = GL_FALSE;
        }
        else if (strcmp(argv[i], "-rgb") == 0)
        {
            rgb = GL_TRUE;
        }
    }
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);
    Args(argc, argv);

    type = GLUT_DEPTH;
    type |= (rgb) ? GLUT_RGB : GLUT_INDEX;
    type |= GLUT_SINGLE;
    glutInitDisplayMode(type);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Depth Test");	//開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    printf("按 1 2 控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
