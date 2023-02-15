#include "../../Common.h"

#define WINDOW_SIZE  600  /* initial size of window                             */
#define BORDER        10  /* border width in each viewport                      */

#define POINTS     151
Point points[POINTS];
int number_of_points = 0;

int WindowSizeX = WINDOW_SIZE;
int WindowSizeY = WINDOW_SIZE;

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
    while (points_file >> points[number_of_points].x >> points[number_of_points].y) //C++��Ū���ɮ׸��
    {
        number_of_points++;
        if (number_of_points == POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }
    points_file.close();
}

void find_data_boundary()
{
    float minx = 1.0e38f;
    float maxx = -1.0e38f;
    float miny = 1.0e38f;
    float maxy = -1.0e38f;
    float xrange = 0.0f;
    float yrange = 0.0f;

    for (int i = 0; i < number_of_points; i++)
    {
        //printf("%0.10f  %0.10f\n", points[i].x, points[i].y);

        if (points[i].x < minx)
        {
            minx = points[i].x;
        }
        if (points[i].x > maxx)
        {
            maxx = points[i].x;
        }
        if (points[i].y < miny)
        {
            miny = points[i].y;
        }
        if (points[i].y > maxy)
        {
            maxy = points[i].y;
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    printf("���o X �d��(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("���o Y �d��(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
}

void print_data(void)
{
    printf("Ū����� SP, �@���o %d �I���\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void init_data_4()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    //�b List 1 �s�@�� 1 �i��
    glNewList(1, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);  /* Draw the marks in red. */

    //�eX�аO
    glBegin(GL_LINES);
    float markd = 0.01f;
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2d(points[i].x - markd, points[i].y - markd);   //���U
        glVertex2d(points[i].x + markd, points[i].y + markd);   //�k�W
        glVertex2d(points[i].x - markd, points[i].y + markd);   //���W
        glVertex2d(points[i].x + markd, points[i].y - markd);   //�k�U
    }
    glEnd();

    //�s�u
    glBegin(GL_LINES);
    for (int i = 0; i < (number_of_points - 1); i++)
    {
        glVertex2d(points[i].x, points[i].y);
        glVertex2d(points[i + 1].x, points[i + 1].y);
    }
    glEnd();

    //�e�I
    for (int i = 0; i < number_of_points; i++)
    {
        draw_point(color_b, 5, points[i].x, points[i].y);
    }

    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glViewport(0, 0, WindowSizeX, WindowSizeY);

    /* Draw line separators between viewports. */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //�]�m���x�}
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);

    float offset = 25.0f;
    draw_rectangle(color_m, 1, offset, offset, (float)WindowSizeX - offset * 2, (float)WindowSizeY - offset * 2);    //���U�}�l w h

    glLoadIdentity();   //�]�m���x�}
    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);
    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);

    glColor3f(0.0, 0.0, 1.0);  //�Ŧ�u
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);    //�Ť߯x��
    //glLineWidth(5.0f);	//�]�w�u�e
    float x_st = 0.0f;
    float y_st = 0.0f;
    float x_sp = 1.0f;
    float y_sp = 1.0f;
    glRectf(x_st, y_st, x_sp, y_sp);  //�q ���U �� �k�W

    glColor3f(1.0, 0.0, 0.0);  //����u

    glViewport(BORDER, BORDER, WindowSizeX - 2 * BORDER, WindowSizeY - 2 * BORDER);
    printf("glViewport �U x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER, WindowSizeX - 2 * BORDER, WindowSizeY - 2 * BORDER);
    glCallList(1);      //1

    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    make_data_4_file();    //�s�@���4. Ū�ɮ�

    find_data_boundary();
    print_data();

    const char* windowName = "Curve Fitting";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape0, keyboard0);

    init_data_4();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
