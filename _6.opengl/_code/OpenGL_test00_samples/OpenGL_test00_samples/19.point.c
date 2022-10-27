#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#define CI_RED GLUT_RED
#define CI_ANTI_ALIAS_GREEN 16
#define CI_ANTI_ALIAS_YELLOW 32
#define CI_ANTI_ALIAS_RED 48

GLenum rgb;
GLint windW = 600;
GLint windH = 600;

GLenum mode;
GLint size;

float point[3] = {
    1.0, 1.0, 0.0
};

void Init(void)
{
    GLint i;

    if (!rgb)
    {
        for (i = 0; i < 16; i++)
        {
            glutSetColor(i + CI_ANTI_ALIAS_RED, i / 15.0, 0.0, 0.0);
            glutSetColor(i + CI_ANTI_ALIAS_YELLOW, i / 15.0, i / 15.0, 0.0);
            glutSetColor(i + CI_ANTI_ALIAS_GREEN, 0.0, i / 15.0, 0.0);
        }
    }

    glClearColor(0.0, 0.0, 0.0, 0.0);

    glBlendFunc(GL_SRC_ALPHA, GL_ZERO);

    mode = GL_FALSE;
    size = 1;
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    (rgb) ? glColor3f(1.0, 1.0, 0.0) : glIndexi(3);

    //畫橫線 x軸
    glBegin(GL_LINE_STRIP);
    glVertex2f(-windW / 2, 0);
    glVertex2f(windW / 2, 0);
    glEnd();

    //畫直線 y軸
    glBegin(GL_LINE_STRIP);
    glVertex2f(0, -windH / 2);
    glVertex2f(0, windH / 2);
    glEnd();

    if (mode)
    {
        glEnable(GL_BLEND);
        glEnable(GL_POINT_SMOOTH);
    }
    else
    {
        glDisable(GL_BLEND);
        glDisable(GL_POINT_SMOOTH);
    }

    glPointSize(size);
    if (mode)
    {
        (rgb) ? glColor3f(1.0, 0.0, 0.0) : glIndexi(CI_ANTI_ALIAS_RED);
    }
    else
    {
        (rgb) ? glColor3f(1.0, 0.0, 0.0) : glIndexi(CI_RED);
    }
    glBegin(GL_POINTS);
    glVertex3fv(point);
    glEnd();

    glDisable(GL_POINT_SMOOTH);

    glPointSize(20);
    (rgb) ? glColor3f(0.0, 1.0, 0.0) : glIndexi(2);
    glBegin(GL_POINTS);
    glVertex3fv(point);
    glEnd();

    glFlush();
}

void reshape(int width, int height)
{
    windW = width;
    windH = height;

    glViewport(0, 0, windW, windH);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-windW / 2, windW / 2, -windH / 2, windH / 2);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case '1':
        mode = !mode;
        glutPostRedisplay();
        break;
    case 'W':
        size++;
        glutPostRedisplay();
        break;
    case 'w':
        size--;
        if (size < 1)
        {
            size = 1;
        }
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
    }
}

void special(int key, int x, int y)
{
    switch (key)
    {
    case GLUT_KEY_LEFT:
        //printf("你按了 左 ");
        point[0] -= 2.25;
        glutPostRedisplay();
        break;
    case GLUT_KEY_RIGHT:
        //printf("你按了 右 ");
        point[0] += 2.25;
        glutPostRedisplay();
        break;
    case GLUT_KEY_UP:
        //printf("你按了 上 ");
        point[1] += 2.25;
        glutPostRedisplay();
        break;
    case GLUT_KEY_DOWN:
        //printf("你按了 下 ");
        point[1] -= 2.25;
        glutPostRedisplay();
        break;
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

    type = (rgb) ? GLUT_RGB : GLUT_INDEX;
    type |= GLUT_SINGLE;

    glutInitDisplayMode(type);
    glutInitWindowSize(windW, windH);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Point Test");

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    glutSpecialFunc(special);    //設定callback function

    printf("按 上 下 左 右 控制\n");

    glutMainLoop();	//開始主循環繪製
}
