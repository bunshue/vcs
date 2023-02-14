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

    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glViewport(0, 0, WindowSizeX, WindowSizeY);

    /* Draw line separators between viewports. */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣
    gluOrtho2D(0, WindowSizeX, 0, WindowSizeY);

    glColor3f(0.0, 0.0, 0.0);  //黑色線

    //在此畫線畫框
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
    glLoadIdentity();   //設置單位矩陣
    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);
    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);
    //gluOrtho2D(minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);
    //printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx - markd, maxx + markd, miny - 2.0 * markd, maxy + 2.0 * markd);

    glColor3f(0.0, 0.0, 1.0);  //藍色線
    float dd = 0.93f;
    float point1[3] = { 1.00f - dd, 1.00f - dd, 0 };	//左下
    float point2[3] = { dd, 1.00f - dd, 0 };	//右下
    float point3[3] = { dd, dd, 0 };	//右上
    float point4[3] = { 1.00f - dd, dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();

    draw_rectangle(color_purple, 3, 1.00f - dd, 1.00f - dd, 0.4f, 0.4f);

    glColor3f(1.0, 0.0, 0.0);  //紅色線

    //移至上圖
    glViewport(BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    printf("glViewport 上 x_st = %d, y_st = %d, W = %d, H = %d\n", BORDER, BORDER + WindowSizeY3 * 2, WindowSizeX - 2 * BORDER, WindowSizeY3 - 2 * BORDER);
    glCallList(1);      //1
    //draw_rectangle(color_purple, 3, -0.9f, -0.9f, 0.4f, 0.4f);

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
