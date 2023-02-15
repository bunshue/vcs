#include "../../Common.h"

#define WINDOW_SIZE  600  /* initial size of window                             */
#define BORDER        10  /* border width in each viewport                      */

#define POINTS     51
Point points[POINTS];
int number_of_points = POINTS;

int WindowSizeX = WINDOW_SIZE;
int WindowSizeY = WINDOW_SIZE;
int WindowSizeY3 = WINDOW_SIZE / 3;

int t = 0;
void make_data_2_sine(void)
{
    for (int i = 0; i < POINTS; i++)
    {
        points[i].x = 0.02f * i;
        points[i].y = sin(PI * (float)(i * 4) / 180);
        //points[i].y = 25.0f * sin(PI * (float)(i + t) / 180);
    }
    //t++;
    points[POINTS / 8].y = 1.0f;     //�G�N�y�@�ӯS�j�I
    return;
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
    printf("�@�� %d �I���\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void init_data_2()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    //�b List 1 �s�@�� 1 �i��
    glNewList(1, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);  /* Draw the marks in red. */

    //�eX�аO
    glBegin(GL_LINES);
    float markd = 0.01f;
    for (int i = 0; i < POINTS; i++)
    {
        glVertex2d(points[i].x - markd, points[i].y - markd);   //���U
        glVertex2d(points[i].x + markd, points[i].y + markd);   //�k�W
        glVertex2d(points[i].x - markd, points[i].y + markd);   //���W
        glVertex2d(points[i].x + markd, points[i].y - markd);   //�k�U
    }
    glEnd();

    for (int i = 0; i < POINTS; i++)
    {
        //draw_point(color_r, 10, points[i].x, points[i].y);
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

    //���f�y�нd��, 2D	//��ܽd�� x(0 ~ WindowSizeX), y(0 ~ WindowSizeY)
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);

    //�ӵ۵��f�y�нd��e�@�Ӯ�
    float border = 10.0f;
    draw_rectangle(color_m, 1, border, border, (float)WindowSizeX - border * 2, (float)WindowSizeY - border * 2);    //���U�}�l w h

    glColor3f(0.0, 0.0, 0.0);  //�¦�u

    //���T����u
    glBegin(GL_LINES);
    glVertex2i(0, WindowSizeY3);
    glVertex2i(WindowSizeX, WindowSizeY3);
    glVertex2i(0, 2 * WindowSizeY3);
    glVertex2i(WindowSizeX, 2 * WindowSizeY3);
    glEnd();

    /* Do Lagrange interpolation in top third of window. */
    glLoadIdentity();   //�]�m���x�}
    float dd = 0.008f;
    //���f�y�нd��, 2D	//��ܽd�� x(0.0f ~ 1.0f), y(0.0f ~ 1.0f)
    gluOrtho2D(0.0f - dd, 1.0f + dd, 0.0f - dd, 1.0f + dd);
    //draw_rectangle(color_purple, 1, 0.0f+dd, 0.0f+dd, 1.0f-dd*2, 1.0f-dd*2);    //���U�}�l w h

    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);
    //gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    //printf("���f�y�нd��2D, ��ܽd�� : X�b(%f ~ %f) Y�b(%f ~ %f), ���U�����I\n", minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);

    glColor3f(1.0, 0.0, 0.0);  //����u

    //���ܤW��
    glViewport(BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport �W x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    draw_rectangle(color_r, 1, 0.0f, 0.0f, 1.0f, 1.0f);    //���U�}�l w h

    //���ܤ���
    glViewport(BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport �� x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    draw_rectangle(color_g, 1, 0.0f, 0.0f, 1.0f, 1.0f);    //���U�}�l w h

    //���ܤU��
    glViewport(BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport �U x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    draw_rectangle(color_b, 1, 0.0f, 0.0f, 1.0f, 1.0f);    //���U�}�l w h

    glFlush();  // ����ø�ϩR�O
}

/* This is the callback function that gets executed every time the display size has changed. */
void reshape(int width, int height)
{
    WindowSizeX = width;
    WindowSizeY = height;
    WindowSizeY3 = height / 3;
}

int main(int argc, char** argv)
{
    make_data_2_sine();
    find_data_boundary();
    print_data();

    const char* windowName = "Curve Fitting";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape, keyboard0);

    init_data_2();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
