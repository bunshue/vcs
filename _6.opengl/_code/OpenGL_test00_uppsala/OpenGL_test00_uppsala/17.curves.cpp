#include "../../Common.h"

const char* data_filename = "data/17.points.dat";

#define POINTS     151
#define MAX_POINTS     151
Point points[MAX_POINTS];
int number_of_points = 0;

float minx = 1.0e38f;
float maxx = -1.0e38f;
float miny = 1.0e38f;
float maxy = -1.0e38f;
float xrange = 0.0f;
float yrange = 0.0f;

int make_data_4_file(const char* filename)
{
    ifstream points_file;

    //開啟檔案
    points_file.open(filename, ios::in);
    if (points_file.is_open() == false)
    {
        cout << "無法開啟檔案 : " << filename << endl;
        return 1;
    }

    //讀取檔案資料
    while (points_file >> points[number_of_points].x >> points[number_of_points].y) //C++之讀取檔案資料
    {
        number_of_points++;
        if (number_of_points == MAX_POINTS)
        {
            cout << "到達點數上限, 先行離開" << endl;
            break;
        }
    }
    points_file.close();
    return 0;
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
    printf("讀取資料 SP, 共取得 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣

    //用點數為基準畫框
    gluOrtho2D(0.0f, 600.0f, 0.0f, 600.0f); //設定座標範圍 2D
    float offset = 25.0f;
    draw_rectangle(color_m, 1, offset, offset, 600.0f - offset * 2, 600.0f - offset * 2);    //左下開始 w h

    glLoadIdentity();   //設置單位矩陣
    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //設定座標範圍 2D
    //gluOrtho2D(0.0f, 1.0f, 0.0f, 1.0f);

    //用比例為基準畫框
    glColor3f(0.0, 0.0, 1.0);  //藍色線
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);    //空心矩形
    //glLineWidth(5.0f);	//設定線寬
    float x_st = 0.0f;
    float y_st = 0.0f;
    float x_sp = 1.0f;
    float y_sp = 1.0f;
    glRectf(x_st, y_st, x_sp, y_sp);  //從 左下 到 右上

    glClearColor(1.0, 1.0, 1.0, 0.0);   //白色背景

    glColor3f(1.0, 0.0, 0.0);  //紅色線

    //畫X標記
    glBegin(GL_LINES);
    float markd = 0.01f;
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2d(points[i].x - markd, points[i].y - markd);   //左下
        glVertex2d(points[i].x + markd, points[i].y + markd);   //右上
        glVertex2d(points[i].x - markd, points[i].y + markd);   //左上
        glVertex2d(points[i].x + markd, points[i].y - markd);   //右下
    }
    glEnd();

    //連線
    glBegin(GL_LINES);
    for (int i = 0; i < (number_of_points - 1); i++)
    {
        glVertex2d(points[i].x, points[i].y);
        glVertex2d(points[i + 1].x, points[i + 1].y);
    }
    glEnd();

    //畫點
    for (int i = 0; i < number_of_points; i++)
    {
        draw_point(color_b, 5, points[i].x, points[i].y);
    }

    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    int ret = make_data_4_file(data_filename);    //製作資料4. 讀檔案
    printf("ret = %d\n", ret);

    find_data_boundary();
    //print_data();

    const char* windowName = "Curve Fitting";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}
