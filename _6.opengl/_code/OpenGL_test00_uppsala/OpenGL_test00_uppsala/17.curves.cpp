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
#define LAGRANGE_LIST       2
#define BEZIER_LIST         3
#define SPLINE_LIST         4
#define LAGRANGE_TITLE_LIST 5
#define BEZIER_TITLE_LIST   6
#define SPLINE_TITLE_LIST   7

double px[MAX_POINTS], py[MAX_POINTS], minx, maxx, miny, maxy, markd;

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
    glRasterPos2i(BORDER, WindowSizeY3 + BORDER);
    glCallList(BEZIER_TITLE_LIST);
    glRasterPos2i(BORDER, BORDER);
    glCallList(SPLINE_TITLE_LIST);

    /* Do Lagrange interpolation in top third of window. */

    glLoadIdentity();
    gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    glViewport(BORDER, 2 * WindowSizeY3 + BORDER, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(MARK_LIST);
    glCallList(LAGRANGE_LIST);

    /* Do Bezier curve in middle third of window. */

    glViewport(BORDER, WindowSizeY3 + BORDER, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(MARK_LIST);
    glCallList(BEZIER_LIST);

    /* Do spline curve in bottom third of window. */

    glViewport(BORDER, BORDER, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(MARK_LIST);
    glCallList(SPLINE_LIST);

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
    ifstream points_file;

    /* Open data file. */

    points_file.open("data/17.points.dat", ios::in);
    if (!points_file.is_open())
    {
        cerr << "Data file 'points.dat' not found." << endl;
        exit(EXIT_FAILURE);
    }

    /* Read file into arrays, determining maximum and minimum values. */

    maxx = maxy = -1.0e38;
    minx = miny = 1.0e38;
    while (points_file >> px[number_of_points] >> py[number_of_points])
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
}

/* This routine makes a mark for each data point in the arrays. */
void mark_points()
{
    int i;

    glNewList(MARK_LIST, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);  /* Draw the marks in red. */
    glBegin(GL_LINES);
    for (i = 0; i < number_of_points; i++)
    {
        glVertex2d(px[i] - markd, py[i] - markd);
        glVertex2d(px[i] + markd, py[i] + markd);
        glVertex2d(px[i] - markd, py[i] + markd);
        glVertex2d(px[i] + markd, py[i] - markd);
    }
    glEnd();
    glEndList();
}

/* Evaluates the blending functions for Lagrange interpolation. */
double B(int n, double t)
{
    switch (n)
    {
    case 1: return -t * (t - 1.0) * (t - 2.0) / 6.0;
        break;
    case 2: return (t + 1.0) * (t - 1.0) * (t - 2.0) / 2.0;
        break;
    case 3: return -(t + 1.0) * t * (t - 2.0) / 2.0;
        break;
    case 4: return (t + 1.0) * t * (t - 1.0) / 6.0;
        break;
    }
    return 0.0;  // default case, should never happen
}

/* This procedure does Lagrange interpolation of the data. */
void Lagrange_interpolate()
{
    int i;
    double t, x, y, b1, b2, b3, b4;
    char title[] = "Lagrange Interpolation";

    glNewList(LAGRANGE_LIST, GL_COMPILE);
    glColor3f(0.0, 0.0, 0.0);  /* Draw curve in black. */
    glBegin(GL_LINE_STRIP);

    /* Handle first set of 4 points between t=-1 and t=0 separately. */
    for (t = -1.0; t < DELTA_T / 2.0; t += DELTA_T)
    {
        b1 = B(1, t);
        b2 = B(2, t);
        b3 = B(3, t);
        b4 = B(4, t);
        x = px[0] * b1 + px[1] * b2 + px[2] * b3 + px[3] * b4;
        y = py[0] * b1 + py[1] * b2 + py[2] * b3 + py[3] * b4;
        glVertex2d(x, y);
    }

    /* Handle middle segments. */
    for (i = 1; i <= number_of_points - 3; i++)
    {
        for (t = DELTA_T; t < 1.0 + DELTA_T / 2.0; t += DELTA_T)
        {
            b1 = B(1, t);
            b2 = B(2, t);
            b3 = B(3, t);
            b4 = B(4, t);
            x = px[i - 1] * b1 + px[i] * b2 + px[i + 1] * b3 + px[i + 2] * b4;
            y = py[i - 1] * b1 + py[i] * b2 + py[i + 1] * b3 + py[i + 2] * b4;
            glVertex2d(x, y);
        }
    }

    /* Handle the last set of 4 points between t=1.0 and t=2.0 separately. */
    for (t = 1.0 + DELTA_T; t < 2.0 + DELTA_T / 2.0; t += DELTA_T)
    {
        b1 = B(1, t);
        b2 = B(2, t);
        b3 = B(3, t);
        b4 = B(4, t);
        x = px[number_of_points - 4] * b1 + px[number_of_points - 3] * b2 +
            px[number_of_points - 2] * b3 + px[number_of_points - 1] * b4;
        y = py[number_of_points - 4] * b1 + py[number_of_points - 3] * b2 +
            py[number_of_points - 2] * b3 + py[number_of_points - 1] * b4;
        glVertex2d(x, y);
    }
    glEnd();
    glEndList();

    /* Render the title into a display list. */

    glNewList(LAGRANGE_TITLE_LIST, GL_COMPILE);
    glColor3f(0.0, 0.0, 0.0);  /* Draw title in black. */
    for (i = 0; i < (int)strlen(title); i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, title[i]);
    }
    glEndList();
}

/* This function approximates the data with Bezier curves. */
void Bezier()
{
    int i, n;
    double ax, bx, cx, dx, ay, by, dy, cy, t, x, y;
    double delta_t = DELTA_T / 4.0;
    char title[] = "Bezier Approximation";

    /* Make sure number of points is one more than a multiple of 3. */

    switch (number_of_points % 3)
    {
    case 0: px[number_of_points] = px[number_of_points - 1];
        py[number_of_points] = py[number_of_points - 1];
        n = number_of_points + 1;
        break;
    case 1: n = number_of_points;
        break;
    case 2: n = number_of_points + 2;
        px[n - 1] = px[n - 2] = px[number_of_points - 1];
        py[n - 1] = py[n - 2] = py[number_of_points - 1];
        break;
    }

    /* Construct Bezier curves for each grouping of four points. */
    glNewList(BEZIER_LIST, GL_COMPILE);
    glColor3f(0.0, 0.0, 0.0);  /* Draw curve in black. */
    glBegin(GL_LINE_STRIP);
    for (i = 0; i < n - 1; i += 3)
    {
        ax = -px[i] + 3.0 * (px[i + 1] - px[i + 2]) + px[i + 3];
        ay = -py[i] + 3.0 * (py[i + 1] - py[i + 2]) + py[i + 3];
        bx = 3.0 * (px[i] - 2.0 * px[i + 1] + px[i + 2]);
        by = 3.0 * (py[i] - 2.0 * py[i + 1] + py[i + 2]);
        cx = -3.0 * (px[i] - px[i + 1]);
        cy = -3.0 * (py[i] - py[i + 1]);
        x = dx = px[i];
        y = dy = py[i];
        glVertex2d(x, y);
        for (t = delta_t; t < 1.0 + delta_t / 2.0; t += delta_t)
        {
            x = ((ax * t + bx) * t + cx) * t + dx;
            y = ((ay * t + by) * t + cy) * t + dy;
            glVertex2d(x, y);
        }
    }
    glEnd();
    glEndList();

    /* Render the title into a display list. */
    glNewList(BEZIER_TITLE_LIST, GL_COMPILE);
    glColor3f(0.0, 0.0, 0.0);  /* Draw title in black. */
    for (i = 0; i < (int)strlen(title); i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, title[i]);
    }
    glEndList();
}

/* This function evaluates the uniform cubic B-spline. */
double b(double t)
{
    double tp2, tp1, tm2, tm1;

    if (t <= -2.0)
    {
        return 0.0;
    }
    else if (t <= -1.0)
    {
        tp2 = t + 2.0;
        return tp2 * tp2 * tp2 / 6.0;
    }
    else if (t <= 0.0)
    {
        tp2 = t + 2.0;
        tp1 = t + 1.0;
        tp2 = tp2 * tp2 * tp2 / 6.0;
        tp1 = 2.0 * tp1 * tp1 * tp1 / 3.0;
        return tp2 - tp1;
    }
    else if (t <= 1.0)
    {
        tm1 = 1.0 - t;
        tm2 = 2.0 - t;
        tm1 = 2.0 * tm1 * tm1 * tm1 / 3.0;
        tm2 = tm2 * tm2 * tm2 / 6.0;
        return tm2 - tm1;
    }
    else if (t <= 2.0)
    {
        tm2 = 2.0 - t;
        return tm2 * tm2 * tm2 / 6.0;
    }
    else
    {
        return 0.0;
    }
}

/* This function approximates the data with spline curves. */
void spline()
{
    double xs[MAX_POINTS + 4], ys[MAX_POINTS + 4];
    double x, y, t, bt1, bt2, bt3, bt4;
    int i;
    char title[] = "Spline Approximation";

    /* Load local arrays with data and make the two endpoints multiple so that
     * they are interpolated. */

    xs[0] = xs[1] = px[0];
    ys[0] = ys[1] = py[0];
    for (i = 0; i < number_of_points; i++)
    {
        xs[i + 2] = px[i];
        ys[i + 2] = py[i];
    }
    xs[number_of_points + 2] = xs[number_of_points + 3] = px[number_of_points - 1];
    ys[number_of_points + 2] = ys[number_of_points + 3] = py[number_of_points - 1];

    /* Compute the values to plot. */

    glNewList(SPLINE_LIST, GL_COMPILE);
    glColor3f(0.0, 0.0, 0.0);  /* Draw curve in black. */
    glBegin(GL_LINE_STRIP);
    glVertex2d(px[0], py[0]);
    for (i = 0; i <= number_of_points; i++)
    {
        for (t = DELTA_T; t < 1.0 + DELTA_T / 2.0; t += DELTA_T)
        {
            bt1 = b(t - 2.0);
            bt2 = b(t - 1.0);
            bt3 = b(t);
            bt4 = b(t + 1.0);
            x = xs[i] * bt4 + xs[i + 1] * bt3 + xs[i + 2] * bt2 + xs[i + 3] * bt1;
            y = ys[i] * bt4 + ys[i + 1] * bt3 + ys[i + 2] * bt2 + ys[i + 3] * bt1;
            glVertex2d(x, y);
        }
    }
    glEnd();
    glEndList();

    /* Render the title into a display list. */

    glNewList(SPLINE_TITLE_LIST, GL_COMPILE);
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
    Bezier();               /* Generate the lines for Bezier approximation.     */
    spline();               /* Generate the lines for the spline approximation. */
}

int main(int argc, char** argv)
{
    /* Get input data. */
    interact();
    
    const char* windowName = "Curve Fitting";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape, keyboard0);

    gfxinit();

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
