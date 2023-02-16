#include "../../Common.h"

const char* data_filename = "data/17.points.dat";

#define POINTS     151
#define MAX_POINTS     151
Point points[MAX_POINTS];
int number_of_points = 0;

float minx = 1.0e38f;
float maxx = -1.0e38f;
float miny = 1.0e38f;
float maxy = -1.0e38f;
float xrange = 0.0f;
float yrange = 0.0f;

int make_data_4_file(const char* filename)
{
    ifstream points_file;

    //�}���ɮ�
    points_file.open(filename, ios::in);
    if (points_file.is_open() == false)
    {
        cout << "�L�k�}���ɮ� : " << filename << endl;
        return 1;
    }

    //Ū���ɮ׸��
    while (points_file >> points[number_of_points].x >> points[number_of_points].y) //C++��Ū���ɮ׸��
    {
        number_of_points++;
        if (number_of_points == MAX_POINTS)
        {
            cout << "��F�I�ƤW��, �������}" << endl;
            break;
        }
    }
    points_file.close();
    return 0;
}

void find_data_boundary()
{
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

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //�]�m���x�}

    //���I�Ƭ���ǵe��
    gluOrtho2D(0.0f, 600.0f, 0.0f, 600.0f); //�]�w�y�нd�� 2D
    float offset = 25.0f;
    draw_rectangle(color_m, 1, offset, offset, 600.0f - offset * 2, 600.0f - offset * 2);    //���U�}�l w h

    glLoadIdentity();   //�]�m���x�}
    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //�]�w�y�нd�� 2D
    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);

    //�Τ�Ҭ���ǵe��
    glColor3f(0.0, 0.0, 1.0);  //�Ŧ�u
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);    //�Ť߯x��
    //glLineWidth(5.0f);	//�]�w�u�e
    float x_st = 0.0f;
    float y_st = 0.0f;
    float x_sp = 1.0f;
    float y_sp = 1.0f;
    glRectf(x_st, y_st, x_sp, y_sp);  //�q ���U �� �k�W

    glClearColor(1.0, 1.0, 1.0, 0.0);   //�զ�I��

    glColor3f(1.0, 0.0, 0.0);  //����u

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

    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    int ret = make_data_4_file(data_filename);    //�s�@���4. Ū�ɮ�
    printf("ret = %d\n", ret);

    find_data_boundary();
    //print_data();

    const char* windowName = "Curve Fitting";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
