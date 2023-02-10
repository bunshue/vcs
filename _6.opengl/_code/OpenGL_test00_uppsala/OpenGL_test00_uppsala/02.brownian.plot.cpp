#include "../../Common.h"

#define POINTS     100
Point points[POINTS];
int number_of_points = 0;

float minx;
float maxx;
float miny;
float maxy;
float xrange;
float yrange;

/* This function gets the input data for the program to process. */
void make_data_4_file(void)
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
    while (points_file >> points[number_of_points].x >> points[number_of_points].y)
    {
        if (points[number_of_points].x < minx)
        {
            minx = points[number_of_points].x;
        }
        if (points[number_of_points].x > maxx)
        {
            maxx = points[number_of_points].x;
        }
        if (points[number_of_points].y < miny)
        {
            miny = points[number_of_points].y;
        }
        if (points[number_of_points].y > maxy)
        {
            maxy = points[number_of_points].y;
        }
        number_of_points++;
        if (number_of_points == POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    printf("Ū����� SP, �@���o %d �I���\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void init_data_4()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    /* Generate the display list for the points. */
    //�b List 1 �s�@��1�i��
    glNewList(1, GL_COMPILE);
    glColor3d(1.0, 0.0, 0.0);
    glPointSize(4.0);
    glBegin(GL_POINTS);
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2f(points[i].x, points[i].y);
    }
    glEnd();
    glEndList();
}

/* This is the callback function that gets executed every time the display size has changed. */
void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    //gluOrtho2D(minx - 0.05 * xrange, maxx + 0.05 * xrange, miny - 0.05 * yrange, maxy + 0.05 * yrange);
    //printf("%f %f %f %f\n", minx - 0.05 * xrange, maxx + 0.05 * xrange, miny - 0.05 * yrange, maxy + 0.05 * yrange);

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);
}

/* This is the callback function that gets executed every time the display needs to be updated. */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glCallList(1);  //��ܲ�1�i��

    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    make_data_4_file();    //�s�@���4. Ū�ɮ�

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "�����, �L����, �� Esc ���}\n";

    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    init_data_4();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

