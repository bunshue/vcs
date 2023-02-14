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

    printf("取得 %d 點資料\n", POINTS);

    for (int i = 0; i < POINTS; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }

    points[POINTS / 8].y = 1.0f;     //故意造一個特大點

    return;
}

void init_data_2()
{
    glClearColor(1.0, 1.0, 1.0, 0.0); /* Make the background white. */

    //在 List 1 製作第 1 張圖
    glNewList(1, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);  /* Draw the marks in red. */

    //畫X標記
    glBegin(GL_LINES);
    float markd = 0.01f;
    for (int i = 0; i < POINTS; i++)
    {
        glVertex2d(points[i].x - markd, points[i].y - markd);   //左下
        glVertex2d(points[i].x + markd, points[i].y + markd);   //右上
        glVertex2d(points[i].x - markd, points[i].y + markd);   //左上
        glVertex2d(points[i].x + markd, points[i].y - markd);   //右下
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
    glLoadIdentity();   //設置單位矩陣

    //窗口座標範圍, 2D	//顯示範圍 x(0 ~ WindowSizeX), y(0 ~ WindowSizeY)
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);
    //照著窗口座標範圍畫一個框
    draw_rectangle(color_m, 1, 10.0f, 10.0f, WindowSizeX - 20, WindowSizeY - 20);    //左下開始 w h

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
    //窗口座標範圍, 2D	//顯示範圍 x(0.0f ~ 1.0f), y(0.0f ~ 1.0f)
    gluOrtho2D(0.0f - dd, 1.0f + dd, 0.0f - dd, 1.0f + dd);
    //draw_rectangle(color_purple, 1, 0.0f+dd, 0.0f+dd, 1.0f-dd*2, 1.0f-dd*2);    //左下開始 w h

    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);
    //gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    //printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);

    glColor3f(1.0, 0.0, 0.0);  //紅色線

    //移至上圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 上 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    draw_rectangle(color_r, 1, 0.0f, 0.0f, 1.0f, 1.0f);    //左下開始 w h

    //移至中圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 中 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 1, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    draw_rectangle(color_g, 1, 0.0f, 0.0f, 1.0f, 1.0f);    //左下開始 w h

    //移至下圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 下 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 0, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    draw_rectangle(color_b, 1, 0.0f, 0.0f, 1.0f, 1.0f);    //左下開始 w h

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

    const char* windowName = "Curve Fitting";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, WindowSizeX, WindowSizeY, 1100, 200, display, reshape, keyboard0);

    init_data_2();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
