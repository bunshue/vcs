//使用 OpenGL evaluators 畫圖, 畫 Bezier curve

#include "../../Common.h"

 /* Drawing constants. */
#define STEPS        20  /* number of steps to draw each segment over */

#define POINTS     100
float points[POINTS + 2][3];    //多兩點給 Bezier curve 用
//Point points[POINTS]; reserved
int number_of_points = 0;

float minx;
float maxx;
float miny;
float maxy;
float xrange;
float yrange;

void make_data_4_file(void)
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
    while (points_file >> points[number_of_points][0] >> points[number_of_points][1])
    {
        if (points[number_of_points][0] < minx)
        {
            minx = points[number_of_points][0];
        }
        if (points[number_of_points][0] > maxx)
        {
            maxx = points[number_of_points][0];
        }
        if (points[number_of_points][1] < miny)
        {
            miny = points[number_of_points][1];
        }
        if (points[number_of_points][1] > maxy)
        {
            maxy = points[number_of_points][1];
        }
        points[number_of_points][2] = 0.0;
        number_of_points++;
        if (number_of_points == POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    /* Load two additional copies of last point to make sure the right number of
       data points are available for a Bezier curve. */

    points[number_of_points + 1][0] = points[number_of_points][0] = points[number_of_points - 1][0];
    points[number_of_points + 1][1] = points[number_of_points][1] = points[number_of_points - 1][1];
    points[number_of_points + 1][2] = points[number_of_points][2] = 0.0;

    printf("讀取資料 SP, 共取得 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i][0], points[i][1]);
    }
}

void init_data_4()
{
    int i, j;

    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */
    glEnable(GL_MAP1_VERTEX_3);

    /* Generate the display list for the points. */
    //在 List 1 製作第1張圖
    glNewList(1, GL_COMPILE);
    glColor3f(1.0f, 0.0f, 0.0f);    //紅點
    glPointSize(4.0);
    glBegin(GL_POINTS);
    for (i = 0; i < number_of_points; i++)
    {
        glVertex3fv(&points[i][0]);
    }
    glEnd();
    glEndList();

    /* Generate the display list for the curve. */
    //在 List 2 製作第1張圖
    glNewList(2, GL_COMPILE);
    glColor3f(0.0f, 0.0f, 0.0f);   //黑線
    for (j = 0; j < number_of_points; j += 3)
    {
        glMap1f(GL_MAP1_VERTEX_3, 0.0, STEPS, 3, 4, &points[j][0]);
        glBegin(GL_LINE_STRIP);
        for (i = 0; i <= STEPS; i++)
        {
            glEvalCoord1f(i);
        }
        glEnd();
    }
    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glCallList(1);  //顯示第1張圖
    glCallList(2);  //顯示第2張圖

    glFlush();  // 執行繪圖命令
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    //gluOrtho2D(minx - 0.05 * xrange, maxx + 0.05 * xrange, miny - 0.05 * yrange, maxy + 0.05 * yrange);
    //printf("%f %f %f %f\n", minx - 0.05 * xrange, maxx + 0.05 * xrange, miny - 0.05 * yrange, maxy + 0.05 * yrange);

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);
}

int main(int argc, char** argv)
{
    make_data_4_file();    //製作資料4. 讀檔案

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    init_data_4();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

