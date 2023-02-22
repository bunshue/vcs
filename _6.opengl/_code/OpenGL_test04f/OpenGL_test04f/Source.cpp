#include "../../Common.h"

#define WINDOW_SIZE  600  /* initial size of window                             */
#define BORDER        10  /* border width in each viewport                      */

#define POINTS     61
Point points[POINTS];
int number_of_points = POINTS;

float minx = 1.0e38f;
float maxx = -1.0e38f;
float miny = 1.0e38f;
float maxy = -1.0e38f;
float xrange = 0.0f;
float yrange = 0.0f;

int WindowSizeX = WINDOW_SIZE;
int WindowSizeY = WINDOW_SIZE;
int WindowSizeY3 = WINDOW_SIZE / 3;

int t = 0;
void make_data_2_sine(void)
{
    for (int i = 0; i < POINTS; i++)
    {
        points[i].x = (1.0f / POINTS) * i;
        points[i].y = sin(PI * (float)(i * 6) / 180);
        //points[i].y = 25.0f * sin(PI * (float)(i + t) / 180);
    }
    //t++;
    points[POINTS / 8].y = 1.0f;     //故意造一個特大點
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

void init_data_2()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    //在 List 1 製作第 1 張圖
    glNewList(1, GL_COMPILE);
    //畫點
    for (int i = 0; i < number_of_points; i++)
    {
        draw_point(color_r, 5, points[i].x, points[i].y);
    }
    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    int viewportx = 0;
    int viewporty = 0;
    int viewportw = WindowSizeX;
    int viewporth = WindowSizeY;

    //以畫素為單位
    glViewport(viewportx, viewporty, viewportw, viewporth);		//把所有要畫的東西顯示在視窗的(0,0)開始的(W, H), 即 全部顯示
    printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\t全部\n", viewportx, viewporty, viewportw, viewporth);

    /* Draw line separators between viewports. */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣

    //窗口座標範圍, 2D	//顯示範圍 x(0 ~ WindowSizeX), y(0 ~ WindowSizeY)
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);

    //照著窗口座標範圍畫一個框
    float border = 10.0f;
    draw_rectangle(color_m, 1, border, border, (float)WindowSizeX - border * 2, (float)WindowSizeY - border * 2);    //左下開始 w h

    glColor3f(0.0, 0.0, 0.0);  //黑色線

    //劃三分格線
    glBegin(GL_LINES);
    glVertex2i(0, WindowSizeY3);
    glVertex2i(WindowSizeX, WindowSizeY3);
    glVertex2i(0, 2 * WindowSizeY3);
    glVertex2i(WindowSizeX, 2 * WindowSizeY3);
    glEnd();

    /* Do Lagrange interpolation in top third of window. */
    glLoadIdentity();   //設置單位矩陣
    float dd = 0.008f;
    //窗口座標範圍, 2D	//顯示範圍 x(0.0f ~ 1.0f), y(-1.0f ~ 1.0f)
    gluOrtho2D(0.0f - dd, 1.0f + dd, -1.0f - dd, 1.0f + dd);
    //draw_rectangle(color_purple, 1, 0.0f+dd, 0.0f+dd, 1.0f-dd*2, 1.0f-dd*2);    //左下開始 w h

    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);
    //gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    //printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);

    glColor3f(1.0, 0.0, 0.0);  //紅色線

    //移至上圖
    viewportx = BORDER;
    viewporty = BORDER + WindowSizeY3 * 2;
    viewportw = WindowSizeX - 2 * BORDER;
    viewporth = WindowSizeY3 - 2 * BORDER;
    glViewport(viewportx, viewporty, viewportw, viewporth);
    //printf("glViewport 上 x_st = %d, y_st = %d, W = %d, H = %d\n", viewportx, viewporty, viewportw, viewporth);
    printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d), 上圖\n", viewportx, viewporty, viewportw, viewporth);
    glCallList(1);      //1
    draw_rectangle(color_r, 1, 0.0f, -1.0f, 1.0f, 2.0f);    //左下開始 w h

    //移至中圖
    viewportx = BORDER;
    viewporty = BORDER + WindowSizeY3 * 1;
    viewportw = WindowSizeX - 2 * BORDER;
    viewporth = WindowSizeY3 - 2 * BORDER;
    glViewport(viewportx, viewporty, viewportw, viewporth);
    //printf("glViewport 中 x_st = %d, y_st = %d, W = %d, H = %d\n", viewportx, viewporty, viewportw, viewporth);
    printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d), 中圖\n", viewportx, viewporty, viewportw, viewporth);
    glCallList(1);      //1
    draw_rectangle(color_g, 1, 0.0f, -1.0f, 1.0f, 2.0f);    //左下開始 w h

    //移至下圖
    viewportx = BORDER;
    viewporty = BORDER + WindowSizeY3 * 0;
    viewportw = WindowSizeX - 2 * BORDER;
    viewporth = WindowSizeY3 - 2 * BORDER;
    glViewport(viewportx, viewporty, viewportw, viewporth);
    //printf("glViewport 下 x_st = %d, y_st = %d, W = %d, H = %d\n", viewportx, viewporty, viewportw, viewporth);
    printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d), 下圖\n", viewportx, viewporty, viewportw, viewporth);
    glCallList(1);      //1
    draw_rectangle(color_b, 1, 0.0f, -1.0f, 1.0f, 2.0f);    //左下開始 w h

    glFlush();  // 執行繪圖命令
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
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape, keyboard0);

    init_data_2();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
