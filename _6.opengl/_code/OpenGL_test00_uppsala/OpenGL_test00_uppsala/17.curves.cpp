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

/* Display list constants. */
#define MARK_LIST           1
#define LAGRANGE_TITLE_LIST 5

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
    glColor3f(0.0, 0.0, 0.0);  /* Draw separator lines in black. */

    glBegin(GL_LINES);
    glVertex2i(0, WindowSizeY3);
    glVertex2i(WindowSizeX, WindowSizeY3);
    glVertex2i(0, 2 * WindowSizeY3);
    glVertex2i(WindowSizeX, 2 * WindowSizeY3);
    glEnd();

    /* Place titles. */
    glRasterPos2i(BORDER, 2 * WindowSizeY3 + BORDER);
    glCallList(LAGRANGE_TITLE_LIST);

    /* Do Lagrange interpolation in top third of window. */
    glLoadIdentity();
    gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    glViewport(BORDER, 2 * WindowSizeY3 + BORDER, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(MARK_LIST);      //1

    /* Do Bezier curve in middle third of window. */
    glViewport(BORDER, WindowSizeY3 + BORDER, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(MARK_LIST);      //1
    
    /* Do spline curve in bottom third of window. */
    glViewport(BORDER, BORDER, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(MARK_LIST);      //1

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
    //在 List MARK_LIST 製作第 MARK_LIST 張圖, MARK_LIST = 1
    glNewList(MARK_LIST, GL_COMPILE);
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

/* This procedure does Lagrange interpolation of the data. */
void Lagrange_interpolate()
{
    int i;
    char title[] = "Lagrange Interpolation";

    //顯示標題
    //在 List LAGRANGE_TITLE_LIST 製作第 LAGRANGE_TITLE_LIST 張圖, LAGRANGE_TITLE_LIST = 5
    glNewList(LAGRANGE_TITLE_LIST, GL_COMPILE); //5
    glColor3f(0.0, 0.0, 0.0);  /* Draw title in black. */
    for (i = 0; i < (int)strlen(title); i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, title[i]);
    }
    glEndList();
}

/* This is the routine that generates the image to be displayed. */
void gfxinit()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    /* Generate the three different curves for displaying. */

    mark_points();          /* Generate the data marks display list.            */
    Lagrange_interpolate(); /* Generate the lines for Lagrange interpolation.   */
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
