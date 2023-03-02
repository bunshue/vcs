#include "../../Common.h"

int display_mode = 5;

const char* data_filename = "data/points.dat";

#define SEED srand
#define RANDNUM rand
#define RANDMAX RAND_MAX

#define POINTS     361
#define MAX_POINTS     361
Point points[MAX_POINTS];
int number_of_points = POINTS;

float minx = 1.0e38f;
float maxx = -1.0e38f;
float miny = 1.0e38f;
float maxy = -1.0e38f;
float xrange = 0.0f;
float yrange = 0.0f;

//display5
//�ϥ� OpenGL evaluators �e��, �e Bezier curve

 /* Drawing constants. */
#define STEPS        20  /* number of steps to draw each segment over */

#define POINTS2     100
#define MAX_POINTS2     100
float points2[POINTS2 + 2][3];    //�h���I�� Bezier curve ��

int t = 0;
void make_data_2_sine(void)
{
    number_of_points = 361;
    points[0].x = 0.0f;
    points[0].y = 0.0f;
    for (int i = 1; i < number_of_points; i++)
    {
        points[i].x = (float)i;
        points[i].y = 10.0f * sin(PI * (float)(i + t) / 180);
    }
    t++;
    //points[number_of_points / 2].y = 20.0f;     //�G�N�y�@�ӯS�j�I
    return;
}

int Arand;
int Nrand;
double GaussAdd;
double GaussFac;

/* Routine for initializing the Gaussian random number generator. This is an
 * implementation of algorithm InitGauss on page 77 of "The Science of Fractal Images".   */
void InitGauss(int seed)
{
    Nrand = 4;
    Arand = RANDMAX;
    GaussAdd = sqrt(3.0 * (double)Nrand);
    GaussFac = 2.0 * GaussAdd / ((double)Nrand * (double)Arand);
    SEED(seed);
}

/* Routine to generate a Gaussian random number. This is an implementation of
 * algorithm Gauss on page 77 of "The Science of Fractal Images."  */
double Gauss(void)
{
    double sum;
    int i;
    sum = 0.0;
    for (i = 1; i <= Nrand; i++)
    {
        sum += (double)RANDNUM();
    }
    return (GaussFac * sum - GaussAdd);
}

void make_data_3_gaussian(void)
{
    number_of_points = 100;

    float displacement;
    int i;

    // Begin by computing the vertices for the line as the sum of Gaussian random variables.
    InitGauss((int)time(NULL));
    displacement = 0.0f;

    points[0].x = 0.0f;
    points[0].y = 0.0f;
    for (i = 1; i < number_of_points; i++)
    {
        displacement += (float)Gauss();
        points[i].x = (float)i;
        points[i].y = displacement;
        //points[i].y = (float)i/10;     //debug
    }
    //points[number_of_points / 2].y = 20.0f;     //�G�N�y�@�ӯS�j�I
    return;
}

int make_data_4_file(const char* filename)
{
    number_of_points = 0;

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
    minx = 1.0e38f;
    maxx = -1.0e38f;
    miny = 1.0e38f;
    maxy = -1.0e38f;
    xrange = 0.0f;
    yrange = 0.0f;

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
    printf("�@�� %d �I���\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void find_data_boundary2()
{
    minx = 1.0e38f;
    maxx = -1.0e38f;
    miny = 1.0e38f;
    maxy = -1.0e38f;
    xrange = 0.0f;
    yrange = 0.0f;

    for (int i = 0; i < number_of_points; i++)
    {
        //printf("%0.10f  %0.10f\n", points2[i][0], points2[i][1]);

        if (points2[i][0] < minx)
        {
            minx = points2[i][0];
        }
        if (points2[i][0] > maxx)
        {
            maxx = points2[i][0];
        }
        if (points2[i][1] < miny)
        {
            miny = points2[i][1];
        }
        if (points2[i][1] > maxy)
        {
            maxy = points2[i][1];
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    printf("���o X �d��(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("���o Y �d��(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
}

void print_data2(void)
{
    printf("�@�� %d �I���\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points2[i][0], points2[i][1]);
    }
}

int make_data_4_file2(const char* filename)
{
    number_of_points = 0;

    ifstream points_file;

    //�}���ɮ�
    points_file.open(filename, ios::in);
    if (points_file.is_open() == false)
    {
        cout << "�L�k�}���ɮ� : " << filename << endl;
        return 1;
    }

    //Ū���ɮ׸��
    while (points_file >> points2[number_of_points][0] >> points2[number_of_points][1])	////C++��Ū���ɮ׸��
    {
        points2[number_of_points][2] = 0.0;
        number_of_points++;
        if (number_of_points == MAX_POINTS2)
        {
            cout << "��F�I�ƤW��, �������}" << endl;
            break;
        }
    }
    points_file.close();

    /* Load two additional copies of last point to make sure the right number of
       data points are available for a Bezier curve. */

    points2[number_of_points + 1][0] = points2[number_of_points][0] = points2[number_of_points - 1][0];
    points2[number_of_points + 1][1] = points2[number_of_points][1] = points2[number_of_points - 1][1];
    points2[number_of_points + 1][2] = points2[number_of_points][2] = 0.0;

    return 0;
}

void make_data(int display_mode)
{
    if (display_mode == 0)
    {

    }
    else if (display_mode == 1)
    {
        //make_data_1_array();    //�s�@���1, �]�w�}�C, TBD
    }
    else if (display_mode == 2)
    {
        make_data_2_sine();	//�s�@���2, �p��
    }
    else if (display_mode == 3)
    {
        make_data_3_gaussian();//�s�@���3, �����p��
    }
    else if (display_mode == 4)
    {
        make_data_4_file(data_filename);    //�s�@���4a. Ū�ɮ�
    }
    else if (display_mode == 5)
    {
        make_data_4_file2(data_filename);    //�s�@���4b. Ū�ɮ�
    }

    if (display_mode < 5)
    {
        find_data_boundary();
        //print_data();
    }
    else if (display_mode == 5)
    {
        find_data_boundary2();
        //print_data2();
    }
}

void reset_default_setting()
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //�]�m�I���� �P �z����, Black
    glClear(GL_COLOR_BUFFER_BIT);   //�M���I��
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//�]�m���x�}
    gluOrtho2D(-1.0f, 1.0f, -1.0f, 1.0f); //���f�y�нd��, 2D

    glLineWidth(1.0f);	//�]�w�u�e

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //�L��, x64�����
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

void display1234(void)
{
    reset_default_setting();

    glClear(GL_COLOR_BUFFER_BIT);   //���϶¦�
    glClearColor(1.0, 1.0, 1.0, 0.0);   //�զ�I��

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //�]�m���x�}

    //gluOrtho2D(-0.5f, 1.1f, -0.5f, 1.1f);   //�]�w�y�нd�� 2D
    gluOrtho2D(minx, maxx, miny, maxy);
    printf("���f�y�нd��2D, ��ܽd�� : X�b(%f ~ %f) Y�b(%f ~ %f), ���U�����I\n", minx, maxx, miny, maxy);

    glClearColor(1.0, 1.0, 1.0, 0.0);   //�I���զ�
    glColor3f(1.0, 0.0, 0.0);           //�e������

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

    //�e�s�u
    glBegin(GL_LINE_STRIP);
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2f(points[i].x, points[i].y);
    }
    glEnd();

    /*
    //�ݤ��
    //�e�s�u
    glBegin(GL_LINES);
    for (int i = 0; i < (number_of_points - 1); i++)
    {
        glVertex2d(points[i].x, points[i].y);
        glVertex2d(points[i + 1].x, points[i + 1].y);
    }
    glEnd();
    */

    //�e�I
    for (int i = 0; i < number_of_points; i++)
    {
        draw_point(color_g, 10, points[i].x, points[i].y);
    }

    //�e�~��
    //draw_rectangle(color_m, 10, minx, miny, xrange - 10, yrange - 1);    //���U�}�l w h
    printf("���o X �d��(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("���o Y �d��(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
    printf("rectangle %0.10f  %0.10f  %0.10f  %0.10f\n", minx, miny, xrange - 10, yrange - 1);

    glFlush();  // ����ø�ϩR�O
}

void display5(void)
{
    //gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //�w���ƾڪ��d�� �~��o��g

    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);   //�]�m�I���� �P �z����, Black
    glClear(GL_COLOR_BUFFER_BIT);   //�M���I��
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//�]�m���x�}
    //gluOrtho2D(-1.0f, 1.0f, -1.0f, 1.0f); //���f�y�нd��, 2D

    //gluOrtho2D(-0.5f, 1.1f, -0.5f, 1.1f);   //�]�w�y�нd�� 2D

    gluOrtho2D(minx, maxx, miny, maxy);
    printf("���f�y�нd��2D, ��ܽd�� : X�b(%f ~ %f) Y�b(%f ~ %f), ���U�����I\n", minx, maxx, miny, maxy);

    glClear(GL_COLOR_BUFFER_BIT);

    int i, j;

    glClearColor(1.0, 1.0, 1.0, 0.0);   //�I���զ�
    glEnable(GL_MAP1_VERTEX_3);

    for (i = 0; i < number_of_points; i++)
    {
        draw_point(color_b, 6, points2[i][0], points2[i][1]);
    }

    glColor3f(0.0f, 0.0f, 0.0f);   //�½u

    //number_of_points = 51;
    for (j = 0; j < number_of_points; j += 3)   //�C���j2�I��@��
    {
        //printf("j=%d v = %f ", j, points2[j][0]);

                 //target,        u1,  u2,  stride, order, *points
        glMap1f(GL_MAP1_VERTEX_3, 0.0, STEPS, 3, 4, &points2[j][0]);
        glBegin(GL_LINE_STRIP);
        for (i = 0; i <= STEPS; i++)
        {
            //0~20, �@21��
            glEvalCoord1f((float)i);
        }
        glEnd();
    }

    glFlush();  // ����ø�ϩR�O
}

void display6(void)
{

}

void display7(void)
{

}

void display8(void)
{

}

void display9(void)
{

}

// ø�Ϧ^�ը��
void display(void)
{
    if (display_mode == 0)
    {
        reset_default_setting();
    }
    else if (display_mode < 5)
    {
        display1234();
    }
    else if (display_mode == 5)
    {
        display5();
    }
    else
    {
        reset_default_setting();
    }

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //�L��, x64�����
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //�w���ƾڪ��d�� �~��o��g
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("�A�ҫ����䪺�X�O%x\t���ɵ��������ƹ��y�ЬO(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //���}����
        glutDestroyWindow(glutGetWindow());
        return;
    case '0':
        display_mode = 0;
        break;
    case '1':
        display_mode = 1;
        break;
    case '2':
        display_mode = 2;
        break;
    case '3':
        display_mode = 3;
        break;
    case '4':
        display_mode = 4;
        break;
    case '5':
        display_mode = 5;
        break;
    case '6':
        display_mode = 6;
        break;
    case '7':
        display_mode = 7;
        break;
    case '8':
        display_mode = 8;
        break;
    case '9':
        display_mode = 9;
        break;
    case '?':
        break;
    }
    make_data(display_mode);
    glutPostRedisplay();    //�N��e�������W�аO�A�аO��ݭn�A����ܡC
}

void idle(void)
{
    glutPostRedisplay();    //�N��e�������W�аO�A�аO��ݭn�A����ܡC
}

int main(int argc, char** argv)
{
    const char* windowName = "²��2D OpenGL�e�� 0 ~ 9";
    const char* message = "²��2D OpenGL�e�� 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    //glutIdleFunc(idle);

    make_data(display_mode);

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
