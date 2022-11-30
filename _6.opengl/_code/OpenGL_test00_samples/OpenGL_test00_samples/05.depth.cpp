#include "../../Common.h"

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

    glClearColor(0.0, 0.0, 0.0, 0.0);

    glPolygonStipple(stippleBits);

    antiAlias = GL_FALSE;
    stipple = GL_FALSE;
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    if (antiAlias)
    {
        glBlendFunc(GL_SRC_ALPHA, GL_ONE);
        glEnable(GL_BLEND);
        glEnable(GL_POLYGON_SMOOTH);
        glDisable(GL_DEPTH_TEST);
    }
    else
    {
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
    glColor3f(0.0, 0.0, 1.0);
    glVertex3f(0.9, -0.9, -30.0);
    glVertex3f(0.9, 0.9, -30.0);
    glVertex3f(-0.9, 0.0, -30.0);
    glColor3f(0.0, 1.0, 0.0);
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

void keyboard(unsigned char key, int /*x*/, int /*y*/)
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

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);

    type = GLUT_DEPTH;
    type |= GLUT_RGB;
    type |= GLUT_SINGLE;
    glutInitDisplayMode(type);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Depth Test");	//開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    printf("按 1 2 控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
