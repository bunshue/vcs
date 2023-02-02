//evaluator.cpp
//This program fits a set of data with a Bezier curve using OpenGL evaluators

#include "../../Common.h"

 /* Drawing constants. */
#define MAX_POINTS  100  /* maximum number of control points          */
#define STEPS        20  /* number of steps to draw each segment over */

double points[MAX_POINTS + 2][3];
double minx;
double maxx;
double miny;
double maxy;
double xrange;
double yrange;
int number_of_points = 0;

/* This is the routine that generates the image to be displayed. */
void gfxinit()
{
    int i, j;

    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */
    glEnable(GL_MAP1_VERTEX_3);

    /* Generate the display list for the points. */
    //�b List 1 �s�@��1�i��
    glNewList(1, GL_COMPILE);
    glColor3d(1.0, 0.0, 0.0);
    glPointSize(4.0);
    glBegin(GL_POINTS);
    for (i = 0; i < number_of_points; i++)
    {
        glVertex3dv(&points[i][0]);
    }
    glEnd();
    glEndList();

    /* Generate the display list for the curve. */
    //�b List 2 �s�@��1�i��
    glNewList(2, GL_COMPILE);
    glColor3d(0.0, 0.0, 0.0);
    for (j = 0; j < number_of_points; j += 3)
    {
        glMap1d(GL_MAP1_VERTEX_3, 0.0, STEPS, 3, 4, &points[j][0]);
        glBegin(GL_LINE_STRIP);
        for (i = 0; i <= STEPS; i++)
        {
            glEvalCoord1d(i);
        }
        glEnd();
    }
    glEndList();
}

/* This is the callback function that gets executed every time the display size has changed. */
void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(minx - 0.05 * xrange, maxx + 0.05 * xrange, miny - 0.05 * yrange, maxy + 0.05 * yrange);
}

/* This is the callback function that gets executed every time the display needs to be updated. */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glCallList(1);  //��ܲ�1�i��
    glCallList(2);  //��ܲ�2�i��

    glFlush();  // ����ø�ϩR�O
}

/* This function gets the input data for the program to process. */
void interact(void)
{
    printf("Ū����� ST\n");

    ifstream points_file;

    //�}���ɮ�
    points_file.open("data/17.points.dat", ios::in);
    if (points_file.is_open() == false)
    {
        cerr << "Data file 'points.dat' not found." << endl;
        exit(EXIT_FAILURE);
    }

    //Ū���ɮ׸��
    /* Read file into arrays, determining maximum and minimum values and ranges. */
    maxx = maxy = -1.0e38;
    minx = miny = 1.0e38;
    while (points_file >> points[number_of_points][0] >> points[number_of_points][1])
    {
        if (points[number_of_points][0] < minx)
        {
            minx = points[number_of_points][0];
        }
        if (points[number_of_points][0] > maxx)
        {
            maxx = points[number_of_points][0];
        }
        if (points[number_of_points][1] < miny)
        {
            miny = points[number_of_points][1];
        }
        if (points[number_of_points][1] > maxy)
        {
            maxy = points[number_of_points][1];
        }
        points[number_of_points][2] = 0.0;
        number_of_points++;
        if (number_of_points == MAX_POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    /* Load two additional copies of last point to make sure the right number of
       data points are available for a Bezier curve. */

    points[number_of_points + 1][0] = points[number_of_points][0] = points[number_of_points - 1][0];
    points[number_of_points + 1][1] = points[number_of_points][1] = points[number_of_points - 1][1];
    points[number_of_points + 1][2] = points[number_of_points][2] = 0.0;
    printf("Ū����� SP, �@���o %d �I���\n", number_of_points);
}

int main(int argc, char** argv)
{
    interact();		//Ū�����

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "�����, �L����, �� Esc ���}\n";

    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    gfxinit();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

