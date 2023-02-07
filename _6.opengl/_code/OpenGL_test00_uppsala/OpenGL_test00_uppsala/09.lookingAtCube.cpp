/* This program is modified from the rotating cube program to demonstrate
   the synthetic camera approach to viewing a scene. */

#include "../../Common.h"

// Vertices of the cube, centered at the origin.
GLfloat vertices[][3] =
{
    {-1.0, -1.0, -1.0},		//0
    {1.0, -1.0, -1.0},		//1
    {1.0, 1.0, -1.0},		//2
    {-1.0, 1.0, -1.0},		//3
    {-1.0, -1.0, 1.0},		//4
    {1.0, -1.0, 1.0},		//5
    {1.0, 1.0, 1.0},		//6
    {-1.0, 1.0, 1.0}		//7
};

/*
// Colors of the vertices.
GLfloat colors[][3] =
{
    {0.0,1.0,1.0}, {1.0,0.0,0.0}, {1.0,0.0,0.0}, {0.0,1.0,1.0},
    {0.0,1.0,0.0}, {0.0,1.0,0.0}, {0.0,1.0,0.0}, {0.0,1.0,0.0}
};
*/

// Colors of the vertices.
GLfloat colors[][3] =
{
    {1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
    {0.0, 0.0, 1.0},		//�� B
    {1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
    {0.0, 1.0, 1.0},		//�� Cyan�ѫC
    {1.0, 1.0, 0.0},		//�U Y
    {1.0, 0.0, 1.0},		//�k Magenta���
    {0.0, 1.0, 0.0},		//�W G
    {1.0, 0.0, 0.0}			//�e R
};

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] =
{
    0, 3, 2, 1,		//��
    2, 3, 7, 6,		//�W
    0, 4, 7, 3,		//��
    1, 2, 6, 5,		//�k
    4, 5, 6, 7,		//�e
    0, 1, 5, 4		//�U
};

// This function sets up the vertex arrays for the color cube.
void colorcube(void)
{
    glEnableClientState(GL_COLOR_ARRAY);
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(3, GL_FLOAT, 0, vertices);
    glColorPointer(3, GL_FLOAT, 0, colors);
}

// This function is the display callback. It draws the cube from the current viewing point.
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
    glFlush();  // ����ø�ϩR�O
}

// This is the reshape callback function. It resets the viewport to the entire window and
// the projection matrix to keep the cube centered in the window.
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
    {
        glOrtho(-2.0, 2.0, -2.0 * (GLfloat)h / (GLfloat)w, 2.0 * (GLfloat)h / (GLfloat)w, 1.0, 5.0);
    }
    else
    {
        glOrtho(-2.0 * (GLfloat)w / (GLfloat)h, 2.0 * (GLfloat)w / (GLfloat)h, -2.0, 2.0, 1.0, 5.0);
    }
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;
        break;
    case '1': /* positive x-axis */
        glLoadIdentity();
        gluLookAt(2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case '2': /* negative x-axis */
        glLoadIdentity();
        gluLookAt(-2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case '3': /* positive y-axis */
        glLoadIdentity();
        gluLookAt(0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0);
        break;
    case '4': /* negative y-axis */
        glLoadIdentity();
        gluLookAt(0.0, -2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
        break;
    case '5': /* positive z-axis */
        glLoadIdentity();
        gluLookAt(0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case '6': /* negative z-axis */
        glLoadIdentity();
        gluLookAt(0.0, 0.0, -2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    }
    glutPostRedisplay();    //�N��e�������W�аO�A�аO��ݭn�A����ܡC
}

int main(int argc, char** argv)
{
    const char* windowName = "Color Cube";
    const char* message = "�� 1 ~ 6 �ѦU�Ӥ�V�h�ݤ��, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    //���O�d
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glEnable(GL_DEPTH_TEST);
    colorcube();

    /* Set initial view to positive x-axis. */
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
