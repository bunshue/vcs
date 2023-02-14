#include "../../Common.h"

#define WINDOW_SIZE  600  /* initial size of window                             */
#define BORDER        10  /* border width in each viewport                      */

#define POINTS     51
Point points[POINTS];

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

    printf("���o %d �I���\n", POINTS);

    for (int i = 0; i < POINTS; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }

    points[POINTS / 8].y = 1.0f;     //�G�N�y�@�ӯS�j�I

    return;
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

    glColor3f(0.0, 0.0, 0.0);  //�¦�u

    //�b���e�u�e��
    /*
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
    */
    glBegin(GL_LINES);
    glVertex2i(0, WindowSizeY3);
    glVertex2i(WindowSizeX, WindowSizeY3);
    glVertex2i(0, 2 * WindowSizeY3);
    glVertex2i(WindowSizeX, 2 * WindowSizeY3);
    glEnd();

    /* Do Lagrange interpolation in top third of window. */
    glLoadIdentity();   //�]�m���x�}
    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);
    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);
    //gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    //printf("���f�y�нd��2D, ��ܽd�� : X�b(%f ~ %f) Y�b(%f ~ %f), ���U�����I\n", minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);

    glColor3f(0.0, 0.0, 1.0);  //�Ŧ�u
    float dd = 0.93f;
    float point1[3] = { 1.00f - dd, 1.00f - dd, 0 };	//���U
    float point2[3] = { dd, 1.00f - dd, 0 };	//�k�U
    float point3[3] = { dd, dd, 0 };	//�k�W
    float point4[3] = { 1.00f - dd, dd, 0 };	//���W
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//���U
    glVertex3fv(point2);	//�k�U
    glVertex3fv(point3);	//�k�W
    glVertex3fv(point4);	//���W
    glEnd();

    draw_rectangle(color_purple, 3, 1.00f - dd, 1.00f - dd, 0.4f, 0.4f);

    glColor3f(1.0, 0.0, 0.0);  //����u

    //���ܤW��
    glViewport(BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport �W x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    //draw_rectangle(color_purple, 3, -0.9f, -0.9f, 0.4f, 0.4f);

    //���ܤ���
    glViewport(BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport �� x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1

    //���ܤU��
    glViewport(BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport �U x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1

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

    const char* windowName = "Curve Fitting";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape, keyboard0);

    init_data_2();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
