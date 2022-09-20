#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

GLenum doubleBuffer;

static void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, 1.0, 0.1, 1000.0);
    glMatrixMode(GL_MODELVIEW);
}

static void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        exit(0);
    }
}

static void display(void)
{
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);

    if (doubleBuffer)
    {
        glutSwapBuffers();
    }
    else
    {
        glFlush();
    }
}

static void Args(int argc, char** argv)
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

    type = GLUT_RGB;
    type |= (doubleBuffer) ? GLUT_DOUBLE : GLUT_SINGLE;
    glutInitDisplayMode(type);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Shell");

    glutDisplayFunc(display);       //�]�wcallback function
    glutReshapeFunc(reshape);       //�]�wcallback function
    glutKeyboardFunc(keyboard);     //�]�wcallback function

    glutMainLoop();
}
