//使用 OpenGL evaluators 畫圖, 畫 Bezier curve

#include "../../Common.h"

 /* Drawing constants. */
#define STEPS        20  /* number of steps to draw each segment over */

#define POINTS     100
float points[POINTS + 2][3];    //多兩點給 Bezier curve 用
//Point points[POINTS]; reserved
int number_of_points = 0;

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
    while (points_file >> points[number_of_points][0] >> points[number_of_points][1])
    {
        points[number_of_points][2] = 0.0;
        number_of_points++;
        if (number_of_points == POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }
    points_file.close();

    /* Load two additional copies of last point to make sure the right number of
       data points are available for a Bezier curve. */

    points[number_of_points + 1][0] = points[number_of_points][0] = points[number_of_points - 1][0];
    points[number_of_points + 1][1] = points[number_of_points][1] = points[number_of_points - 1][1];
    points[number_of_points + 1][2] = points[number_of_points][2] = 0.0;
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
        //printf("%0.10f  %0.10f\n", points[i][0], points[i][1]);

        if (points[i][0] < minx)
        {
            minx = points[i][0];
        }
        if (points[i][0] > maxx)
        {
            maxx = points[i][0];
        }
        if (points[i][1] < miny)
        {
            miny = points[i][1];
        }
        if (points[i][1] > maxy)
        {
            maxy = points[i][1];
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    printf("取得 X 範圍(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("取得 Y 範圍(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
}

void print_data(void)
{
    printf("共有 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i][0], points[i][1]);
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    int i, j;

    glClearColor(1.0, 1.0, 1.0, 0.0);   //背景白色
    glEnable(GL_MAP1_VERTEX_3);

    for (i = 0; i < number_of_points; i++)
    {
        draw_point(color_b, 6, points[i][0], points[i][1]);
    }

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

    glFlush();  // 執行繪圖命令
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //已知數據的範圍 才能這麼寫
}

int main(int argc, char** argv)
{
    make_data_4_file();    //製作資料4. 讀檔案

    find_data_boundary();
    //print_data();

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

