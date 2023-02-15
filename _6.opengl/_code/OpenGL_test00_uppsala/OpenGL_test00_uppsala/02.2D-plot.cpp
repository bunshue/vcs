#include "../../Common.h"

#define SEED srand
#define RANDNUM rand
#define RANDMAX RAND_MAX

#define POINTS     151
Point points[POINTS];
int number_of_points = POINTS;

float minx = 1.0e38f;
float maxx = -1.0e38f;
float miny = 1.0e38f;
float maxy = -1.0e38f;
float xrange = 0.0f;
float yrange = 0.0f;

int t = 0;
void make_data_2_sine(void)
{
    points[0].x = 0.0f;
    points[0].y = 0.0f;
    for (int i = 1; i < number_of_points; i++)
    {
        points[i].x = (float)i;
        points[i].y = 10.0f * sin(PI * (float)(i + t) / 180);
    }
    t++;
    points[number_of_points / 2].y = 20.0f;     //故意造一個特大點
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
    points[number_of_points / 2].y = 20.0f;     //故意造一個特大點
    return;
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

    printf("取得 X 範圍(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("取得 Y 範圍(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
}

void print_data(void)
{
    printf("共有 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //全圖黑色

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(minx, maxx, miny, maxy);
    printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx, maxx, miny, maxy);

    glClearColor(1.0, 1.0, 1.0, 0.0);   //背景白色
    glColor3f(1.0, 0.0, 0.0);           //畫筆紅色

    glBegin(GL_LINE_STRIP);        /* Draw a line defined by some points.*/
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2f(points[i].x, points[i].y);
    }
    glEnd();

    draw_rectangle(color_m, 10, minx, miny, xrange - 10, yrange - 1);    //左下開始 w h
    printf("取得 X 範圍(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("取得 Y 範圍(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
    printf("rectangle %0.10f  %0.10f  %0.10f  %0.10f\n", minx, miny, xrange - 10, yrange - 1);

    glFlush();  // 執行繪圖命令
}

void idle(void)
{
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

int main(int argc, char** argv)
{
    //make_data_1_array();    //製作資料1, 設定陣列, TBD
    make_data_2_sine();	//製作資料2, 計算
    //make_data_3_gaussian();//製作資料3, 高斯計算
    //make_data_4_file();    //製作資料4. 讀檔案, TBD

    find_data_boundary();
    //print_data();

    const char* windowName = "Open GL 2D 畫圖";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    //glutIdleFunc(idle);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

