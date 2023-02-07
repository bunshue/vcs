/*****************************************************************************
 *  curves.cpp                                                               *
 *     This program fits a set of data with three different curve fitting    *
 *  algorithms:  Lagrange interpolation, Bezier curves, and uniform cubic    *
 *  B-splines.                                                               *
 *****************************************************************************/

#include "../../Common.h"

 /* Drawing constants. */
#define WINDOW_SIZE  600  /* initial size of window                             */
#define BORDER        10  /* border width in each viewport                      */
#define MAX_POINTS   100  /* maximum number of control points                   */
#define MARK_FACTOR 0.35  /* scale factor for 'x' that marks each control point */
#define DELTA_T     0.05  /* time step factor for drawing each curve            */

double px[MAX_POINTS];
double py[MAX_POINTS];
double minx;
double maxx;
double miny;
double maxy;
double markd;

int number_of_points = 0;

int WindowSizeX = WINDOW_SIZE;
int WindowSizeY = WINDOW_SIZE;
int WindowSizeY3 = WINDOW_SIZE / 3;

/* This is the callback function that gets executed every time the display needs to be updated. */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glViewport(0, 0, WindowSizeX, WindowSizeY);

    /* Draw line separators between viewports. */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);

    glColor3f(0.0, 0.0, 0.0);  //黑色線

    glBegin(GL_LINES);
    glVertex2i(0, WindowSizeY3);
    glVertex2i(WindowSizeX, WindowSizeY3);
    glVertex2i(0, 2 * WindowSizeY3);
    glVertex2i(WindowSizeX, 2 * WindowSizeY3);
    glEnd();

    /* Do Lagrange interpolation in top third of window. */
    glLoadIdentity();
    gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);

    glColor3f(0.0, 0.0, 1.0);  //藍色線
    float dd = 0.93f;
    float point1[3] = { 1.00f-dd, 1.00f - dd, 0 };	//左下
    float point2[3] = { dd, 1.00f - dd, 0 };	//右下
    float point3[3] = { dd, dd, 0 };	//右上
    float point4[3] = { 1.00f - dd, dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();

    glColor3f(1.0, 0.0, 0.0);  //紅色線

    //移至上圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 上 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1

    //移至中圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 中 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1

    //移至下圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 下 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1

    glFlush();  // 執行繪圖命令
}

/* This is the callback function that gets executed every time the display size has changed. */
void reshape(int width, int height)
{
    WindowSizeX = width;
    WindowSizeY = height;
    WindowSizeY3 = height / 3;
}

/* This function gets the input data for the program to process. */
void interact(void)
{
    printf("讀取資料 ST\n");

    ifstream points_file;

    //開啟檔案
    points_file.open("data/17.points.dat", ios::in);
    if (points_file.is_open() == false)
    {
        cerr << "Data file 'points.dat' not found." << endl;
        exit(EXIT_FAILURE);
    }

    //讀取檔案資料
    /* Read file into arrays, determining maximum and minimum values. */
    maxx = maxy = -1.0e38;
    minx = miny = 1.0e38;
    while (points_file >> px[number_of_points] >> py[number_of_points]) //C++之讀取檔案資料
    {
        if (px[number_of_points] < minx)
        {
            minx = px[number_of_points];
        }
        if (px[number_of_points] > maxx)
        {
            maxx = px[number_of_points];
        }
        if (py[number_of_points] < miny)
        {
            miny = py[number_of_points];
        }
        if (py[number_of_points] > maxy)
        {
            maxy = py[number_of_points];
        }
        number_of_points++;
        if (number_of_points == MAX_POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }
    points_file.close();

    /* Determine length of line segments for making 'x' marks. */
    if (maxx - minx > maxy - miny)
    {
        markd = (maxx - minx) / number_of_points * MARK_FACTOR;
    }
    else
    {
        markd = (maxy - miny) / number_of_points * MARK_FACTOR;
    }
    printf("讀取資料 SP, 共取得 %d 點資料\n", number_of_points);
}

/* This routine makes a mark for each data point in the arrays. */
void mark_points()
{
    //在 List 1 製作第 1 張圖
    glNewList(1, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);  /* Draw the marks in red. */

    glBegin(GL_LINES);
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2d(px[i] - markd, py[i] - markd);
        glVertex2d(px[i] + markd, py[i] + markd);
        glVertex2d(px[i] - markd, py[i] + markd);
        glVertex2d(px[i] + markd, py[i] - markd);
    }
    glEnd();

    glEndList();
}

/* This is the routine that generates the image to be displayed. */
void gfxinit()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    mark_points();          /* Generate the data marks display list.            */
}

int main(int argc, char** argv)
{
    interact();		//讀取資料

    const char* windowName = "Curve Fitting";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape, keyboard0);

    gfxinit();

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
