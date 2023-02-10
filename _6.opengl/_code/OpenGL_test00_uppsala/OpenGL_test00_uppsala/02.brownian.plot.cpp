//evaluator.cpp
//This program fits a set of data with a Bezier curve using OpenGL evaluators

#include "../../Common.h"

 /* Drawing constants. */
#define STEPS        20  /* number of steps to draw each segment over */

#define POINTS     100
Point points[POINTS];
int number_of_points = 0;

float minx;
float maxx;
float miny;
float maxy;
float xrange;
float yrange;

/* This is the routine that generates the image to be displayed. */
void gfxinit()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    /* Generate the display list for the points. */
    //在 List 1 製作第1張圖
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
    gluOrtho2D(minx - 0.05 * xrange, maxx + 0.05 * xrange, miny - 0.05 * yrange, maxy + 0.05 * yrange);
}

/* This is the callback function that gets executed every time the display needs to be updated. */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glCallList(1);  //顯示第1張圖

    glFlush();  // 執行繪圖命令
}

/* This function gets the input data for the program to process. */
void make_curve_data(void)
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

    printf("讀取資料 SP, 共取得 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

int main(int argc, char** argv)
{
    make_curve_data();		//讀取資料

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";

    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

