//�ϥ� OpenGL evaluators �e��, �e Bezier curve

#include "../../Common.h"

 /* Drawing constants. */
#define STEPS        20  /* number of steps to draw each segment over */

#define POINTS     100
float points[POINTS + 2][3];    //�h���I�� Bezier curve ��
//Point points[POINTS]; reserved
int number_of_points = 0;

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
    while (points_file >> points[number_of_points][0] >> points[number_of_points][1])
    {
        points[number_of_points][2] = 0.0;
        number_of_points++;
        if (number_of_points == POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }

    /* Load two additional copies of last point to make sure the right number of
       data points are available for a Bezier curve. */

    points[number_of_points + 1][0] = points[number_of_points][0] = points[number_of_points - 1][0];
    points[number_of_points + 1][1] = points[number_of_points][1] = points[number_of_points - 1][1];
    points[number_of_points + 1][2] = points[number_of_points][2] = 0.0;

    printf("Ū����� SP, �@���o %d �I���\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i][0], points[i][1]);
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    int i, j;

    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */
    glEnable(GL_MAP1_VERTEX_3);

    for (i = 0; i < number_of_points; i++)
    {
        draw_point(color_b, 6, points[i][0], points[i][1]);
    }

    glColor3f(0.0f, 0.0f, 0.0f);   //�½u
    for (j = 0; j < number_of_points; j += 3)
    {
        glMap1f(GL_MAP1_VERTEX_3, 0.0, STEPS, 3, 4, &points[j][0]);
        glBegin(GL_LINE_STRIP);
        for (i = 0; i <= STEPS; i++)
        {
            glEvalCoord1f(i);
        }
        glEnd();
    }

    glFlush();  // ����ø�ϩR�O
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //�w���ƾڪ��d�� �~��o��g
}

int main(int argc, char** argv)
{
    make_data_4_file();    //�s�@���4. Ū�ɮ�

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

