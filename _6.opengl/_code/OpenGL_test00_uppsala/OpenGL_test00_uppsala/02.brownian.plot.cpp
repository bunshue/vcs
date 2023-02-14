#include "../../Common.h"

#define POINTS     100
Point points[POINTS];
int number_of_points = 0;

/* This function gets the input data for the program to process. */
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
    while (points_file >> points[number_of_points].x >> points[number_of_points].y)
    {
        number_of_points++;
        if (number_of_points == POINTS)
        {
            cout << "Data arrays are full. If any more data is present it will not be plotted." << endl;
            break;
        }
    }

    printf("讀取資料 SP, 共取得 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points[i].x, points[i].y);
    }
}

void display(void)
{
    glClearColor(1.0, 1.0, 1.0, 0.0);   //黑色背景
    for (int i = 0; i < number_of_points; i++)
    {
        draw_point(color_r, 8, points[i].x, points[i].y);
    }
    glFlush();  // 執行繪圖命令
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glLoadIdentity();

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //已知數據的範圍 才能這麼寫
}

int main(int argc, char** argv)
{
    make_data_4_file();    //製作資料4. 讀檔案

    const char* windowName = "Curve Fitting with Evaluators";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";

    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

