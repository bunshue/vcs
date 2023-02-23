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

void make_teapot_data(void)
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

void init_teapot_data(void)
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
        glColor3d(1.0, 1.0, 0.0);   //����
        glMap2d(GL_MAP2_VERTEX_3, 0.0, 1.0, 12, 4, 0.0, 1.0, 3, 4, coords);
        glMapGrid2d(STEPS, 0.0, 1.0, STEPS, 0.0, 1.0);
        glEvalMesh2(GL_FILL, 0, STEPS, 0, STEPS);
        glEndList();
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //�M���I��

    glLoadIdentity();

    glOrtho(-4.0, 4.0, -4.0, 4.0, -4.0, 4.0);

    for (int i = 1; i <= PATCHES; i++)
    {
        glCallList(i);
    }

    //�w����ᤧ�y�жb
    draw_coordinates(2.5f);     //�e�y�жb

    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    make_teapot_data();		//Ū�����

    const char* windowName = "�S�ӯ���";
    const char* message = "�S�ӯ���, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    init_teapot_data();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
