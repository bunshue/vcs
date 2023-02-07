/*****************************************************************************
 * teapot.cpp                                                                *
 *     This program models the famous Utah teapot using Bezier patches.      *
 * OpenGL evaluators are used to draw the surfaces.                          *
 *****************************************************************************/

#include "../../Common.h"

 /* Drawing constants. */
#define STEPS        10  /* number of steps to draw each segment over */
#define PATCHES      32  /* number of surfaces in the teapot          */
#define VERTICES    306  /* number of control points                  */

double points[VERTICES + 1][3];
int patch_vertices[PATCHES][16];
static GLfloat theta[] = { 270.0, 0.0, 180.0 };

/* This is the routine that generates the image to be displayed. */
void gfxinit(void)
{
    int i;
    int j;
    int k;
    int vertex;
    double coords[48];
    double* p;

    glClearColor(1.0, 1.0, 1.0, 0.0);   //�I�����զ�
    glEnable(GL_MAP2_VERTEX_3);

    /* Generate the display lists for the surfaces. */
    for (k = 0; k < PATCHES; k++)
    {
        for (i = 0, p = coords; i < 16; i++)
        {
            vertex = patch_vertices[k][i];
            for (j = 0; j < 3; j++, p++)
            {
                *p = points[vertex][j];
            }
        }
        glNewList(k + 1, GL_COMPILE);
        glColor3d(1.0, 0.0, 0.0);   //����
        glMap2d(GL_MAP2_VERTEX_3, 0.0, 1.0, 12, 4, 0.0, 1.0, 3, 4, coords);
        glMapGrid2d(STEPS, 0.0, 1.0, STEPS, 0.0, 1.0);
        glEvalMesh2(GL_FILL, 0, STEPS, 0, STEPS);
        glEndList();
    }
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (width <= height)
    {
        glOrtho(-4.0, 4.0, -4.0 * (GLdouble)height / (GLdouble)width, 4.0 * (GLdouble)height / (GLdouble)width, -10.0, 10.0);
    }
    else
    {
        glOrtho(-4.0 * (GLdouble)width / (GLdouble)height, 4.0 * (GLdouble)width / (GLdouble)height, -4.0, 4.0, -10.0, 10.0);
    }
    glMatrixMode(GL_MODELVIEW);
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();
    glRotatef(theta[0], 1.0, 0.0, 0.0); //��x�b����S�w����
    glRotatef(theta[1], 0.0, 1.0, 0.0); //��y�b����S�w����
    glRotatef(theta[2], 0.0, 0.0, 1.0); //��z�b����S�w����
    for (int i = 1; i <= PATCHES; i++)
    {
        glCallList(i);
    }
    glFlush();  // ����ø�ϩR�O
}

//key �T�|�ȡAx�By�O��m, ���� ��V�� �P PageUp PageDown��
void special(int key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case GLUT_KEY_DOWN: /* rotate around the x-axis in a negative direction */
        printf("�U ");
        theta[0] -= 4.0;
        if (theta[0] < 0.0)
        {
            theta[0] += 360.0;
        }
        break;
    case GLUT_KEY_UP: /* rotate around the x-axis in a positive direction */
        printf("�W ");
        theta[0] += 4.0;
        if (theta[0] > 360.0)
        {
            theta[0] -= 360.0;
        }
        break;
    case GLUT_KEY_PAGE_UP: /* rotate around the y-axis in a negative direction */
        printf("PU ");
        theta[1] -= 4.0;
        if (theta[1] < 0.0)
        {
            theta[1] += 360.0;
        }
        break;
    case GLUT_KEY_PAGE_DOWN: /* rotate around the y-axis in a positive direction */
        printf("PD ");
        theta[1] += 4.0;
        if (theta[1] > 360.0)
        {
            theta[1] -= 360.0;
        }
        break;
    case GLUT_KEY_RIGHT: /* rotate around the z-axis in a negative direction */
        printf("�k ");
        theta[2] -= 4.0;
        if (theta[2] < 0.0)
        {
            theta[2] += 360.0;
        }
        break;
    case GLUT_KEY_LEFT: /* rotate around the z-axis in a positive direction */
        printf("�� ");
        theta[2] += 4.0;
        if (theta[2] > 360.0)
        {
            theta[2] -= 360.0;
        }
        break;
    }
    glutPostRedisplay();
}

/* This function gets the input data for the program to process. */
void interact(void)
{
    ifstream vertices_file;
    ifstream patches_file;
    int i;
    int j;

    //�}���ɮ�
    printf("�}���ɮ�: data/19.teapot.vertices\n");
    vertices_file.open("data/19.teapot.vertices", ios::in);
    if (vertices_file.fail())
    {
        printf("�䤣���ɮ�: data/19.teapot.vertices\n");
        patches_file.close();
        exit(EXIT_FAILURE);
    }

    printf("�}���ɮ�: data/19.teapot.patches\n");
    patches_file.open("data/19.teapot.patches", ios::in);
    if (patches_file.fail())
    {
        printf("�䤣���ɮ�: data/19.teapot.patches\n");
        exit(EXIT_FAILURE);
    }

    //Ū���ɮ׸��
    for (i = 1; i <= VERTICES; i++)
    {
        vertices_file >> points[i][0] >> points[i][1] >> points[i][2];  //C++��Ū���ɮ׸��
    }
    for (i = 0; i < PATCHES; i++)
    {
        for (j = 0; j < 16; j++)
        {
            patches_file >> patch_vertices[i][j];   //C++��Ū���ɮ׸��
        }
    }

    vertices_file.close();
    patches_file.close();
}

int main(int argc, char** argv)
{
    interact();		//Ū�����

    const char* windowName = "�S�ӯ���";
    const char* message = "�S�ӯ���, �� �W �U �� �k PageUp PageDown ����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    glutSpecialFunc(special);   //�]�wcallback function

    gfxinit();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
