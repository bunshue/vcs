#include "../../Common.h"

#define WINDOW_SIZE  600  /* initial size of window                             */
#define BORDER        10  /* border width in each viewport                      */

#define POINTS     151
Point points[POINTS];
int number_of_points = 0;

int WindowSizeX = WINDOW_SIZE;
int WindowSizeY = WINDOW_SIZE;

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glViewport(0, 0, WindowSizeX, WindowSizeY);

    /* Draw line separators between viewports. */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //�]�m���x�}
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);

    glColor3f(0.0, 0.0, 0.0);  //�¦�u

    int offset = 20;
    glBegin(GL_LINES);
    glVertex2i(offset, offset);
    glVertex2i(WindowSizeX - offset, offset);
    glVertex2i(offset, WindowSizeY - offset);
    glVertex2i(WindowSizeX - offset, WindowSizeY - offset);
    glVertex2i(offset, offset);
    glVertex2i(offset, WindowSizeY - offset);
    glVertex2i(WindowSizeX - offset, offset);
    glVertex2i(WindowSizeX - offset, WindowSizeY - offset);
    glEnd();

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

/* This function gets the input data for the program to process. */
void make_curve_data(void)
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

    printf("Ū����� SP, �@���o %d �I���\n", number_of_points);

    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

/* This is the routine that generates the image to be displayed. */
void gfxinit()
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

    glEndList();
}

int main(int argc, char** argv)
{
    make_curve_data();		//Ū�����

    const char* windowName = "Curve Fitting";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape0, keyboard0);

    gfxinit();

    printf("�����, �L����, �� Esc ���}\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
