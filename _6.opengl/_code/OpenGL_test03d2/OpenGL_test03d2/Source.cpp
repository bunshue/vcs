#include "../../Common.h"

int display_mode = 5;

const char* data_filename = "data/points.dat";

#define SEED srand
#define RANDNUM rand
#define RANDMAX RAND_MAX

#define POINTS     361
#define MAX_POINTS     361
Point points[MAX_POINTS];
int number_of_points = POINTS;

float minx = 1.0e38f;
float maxx = -1.0e38f;
float miny = 1.0e38f;
float maxy = -1.0e38f;
float xrange = 0.0f;
float yrange = 0.0f;

//display5
//使用 OpenGL evaluators 畫圖, 畫 Bezier curve

 /* Drawing constants. */
#define STEPS        20  /* number of steps to draw each segment over */

#define POINTS2     100
#define MAX_POINTS2     100
float points2[POINTS2 + 2][3];    //多兩點給 Bezier curve 用

int t = 0;
void make_data_2_sine(void)
{
    number_of_points = 361;
    points[0].x = 0.0f;
    points[0].y = 0.0f;
    for (int i = 1; i < number_of_points; i++)
    {
        points[i].x = (float)i;
        points[i].y = 10.0f * sin(PI * (float)(i + t) / 180);
    }
    t++;
    //points[number_of_points / 2].y = 20.0f;     //故意造一個特大點
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
    number_of_points = 100;

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
    //points[number_of_points / 2].y = 20.0f;     //故意造一個特大點
    return;
}

int make_data_4_file(const char* filename)
{
    number_of_points = 0;

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
    minx = 1.0e38f;
    maxx = -1.0e38f;
    miny = 1.0e38f;
    maxy = -1.0e38f;
    xrange = 0.0f;
    yrange = 0.0f;

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

void find_data_boundary2()
{
    minx = 1.0e38f;
    maxx = -1.0e38f;
    miny = 1.0e38f;
    maxy = -1.0e38f;
    xrange = 0.0f;
    yrange = 0.0f;

    for (int i = 0; i < number_of_points; i++)
    {
        //printf("%0.10f  %0.10f\n", points2[i][0], points2[i][1]);

        if (points2[i][0] < minx)
        {
            minx = points2[i][0];
        }
        if (points2[i][0] > maxx)
        {
            maxx = points2[i][0];
        }
        if (points2[i][1] < miny)
        {
            miny = points2[i][1];
        }
        if (points2[i][1] > maxy)
        {
            maxy = points2[i][1];
        }
    }
    xrange = maxx - minx;
    yrange = maxy - miny;

    printf("取得 X 範圍(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("取得 Y 範圍(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
}

void print_data2(void)
{
    printf("共有 %d 點資料\n", number_of_points);
    for (int i = 0; i < number_of_points; i++)
    {
        printf("%0.10f  %0.10f\n", points2[i][0], points2[i][1]);
    }
}

int make_data_4_file2(const char* filename)
{
    number_of_points = 0;

    ifstream points_file;

    //開啟檔案
    points_file.open(filename, ios::in);
    if (points_file.is_open() == false)
    {
        cout << "無法開啟檔案 : " << filename << endl;
        return 1;
    }

    //讀取檔案資料
    while (points_file >> points2[number_of_points][0] >> points2[number_of_points][1])	////C++之讀取檔案資料
    {
        points2[number_of_points][2] = 0.0;
        number_of_points++;
        if (number_of_points == MAX_POINTS2)
        {
            cout << "到達點數上限, 先行離開" << endl;
            break;
        }
    }
    points_file.close();

    /* Load two additional copies of last point to make sure the right number of
       data points are available for a Bezier curve. */

    points2[number_of_points + 1][0] = points2[number_of_points][0] = points2[number_of_points - 1][0];
    points2[number_of_points + 1][1] = points2[number_of_points][1] = points2[number_of_points - 1][1];
    points2[number_of_points + 1][2] = points2[number_of_points][2] = 0.0;

    return 0;
}

void make_data(int display_mode)
{
    if (display_mode == 0)
    {

    }
    else if (display_mode == 1)
    {
        //make_data_1_array();    //製作資料1, 設定陣列, TBD
    }
    else if (display_mode == 2)
    {
        make_data_2_sine();	//製作資料2, 計算
    }
    else if (display_mode == 3)
    {
        make_data_3_gaussian();//製作資料3, 高斯計算
    }
    else if (display_mode == 4)
    {
        make_data_4_file(data_filename);    //製作資料4a. 讀檔案
    }
    else if (display_mode == 5)
    {
        make_data_4_file2(data_filename);    //製作資料4b. 讀檔案
    }

    if (display_mode < 5)
    {
        find_data_boundary();
        //print_data();
    }
    else if (display_mode == 5)
    {
        find_data_boundary2();
        //print_data2();
    }
}

void reset_default_setting()
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluOrtho2D(-1.0f, 1.0f, -1.0f, 1.0f); //窗口座標範圍, 2D

    glLineWidth(1.0f);	//設定線寬

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

void display1234(void)
{
    reset_default_setting();

    glClear(GL_COLOR_BUFFER_BIT);   //全圖黑色
    glClearColor(1.0, 1.0, 1.0, 0.0);   //白色背景

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣

    //gluOrtho2D(-0.5f, 1.1f, -0.5f, 1.1f);   //設定座標範圍 2D
    gluOrtho2D(minx, maxx, miny, maxy);
    printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx, maxx, miny, maxy);

    glClearColor(1.0, 1.0, 1.0, 0.0);   //背景白色
    glColor3f(1.0, 0.0, 0.0);           //畫筆紅色

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

    //畫連線
    glBegin(GL_LINE_STRIP);
    for (int i = 0; i < number_of_points; i++)
    {
        glVertex2f(points[i].x, points[i].y);
    }
    glEnd();

    /*
    //待比較
    //畫連線
    glBegin(GL_LINES);
    for (int i = 0; i < (number_of_points - 1); i++)
    {
        glVertex2d(points[i].x, points[i].y);
        glVertex2d(points[i + 1].x, points[i + 1].y);
    }
    glEnd();
    */

    //畫點
    for (int i = 0; i < number_of_points; i++)
    {
        draw_point(color_g, 10, points[i].x, points[i].y);
    }

    //畫外框
    //draw_rectangle(color_m, 10, minx, miny, xrange - 10, yrange - 1);    //左下開始 w h
    printf("取得 X 範圍(%0.10f ~ %0.10f), range : %0.10f\n", minx, maxx, xrange);
    printf("取得 Y 範圍(%0.10f ~ %0.10f), range : %0.10f\n", miny, maxy, yrange);
    printf("rectangle %0.10f  %0.10f  %0.10f  %0.10f\n", minx, miny, xrange - 10, yrange - 1);

    glFlush();  // 執行繪圖命令
}

void display5(void)
{
    //gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //已知數據的範圍 才能這麼寫

    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);   //設置背景色 與 透明度, Black
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    //gluOrtho2D(-1.0f, 1.0f, -1.0f, 1.0f); //窗口座標範圍, 2D

    //gluOrtho2D(-0.5f, 1.1f, -0.5f, 1.1f);   //設定座標範圍 2D

    gluOrtho2D(minx, maxx, miny, maxy);
    printf("窗口座標範圍2D, 顯示範圍 : X軸(%f ~ %f) Y軸(%f ~ %f), 左下為原點\n", minx, maxx, miny, maxy);

    glClear(GL_COLOR_BUFFER_BIT);

    int i, j;

    glClearColor(1.0, 1.0, 1.0, 0.0);   //背景白色
    glEnable(GL_MAP1_VERTEX_3);

    for (i = 0; i < number_of_points; i++)
    {
        draw_point(color_b, 6, points2[i][0], points2[i][1]);
    }

    glColor3f(0.0f, 0.0f, 0.0f);   //黑線

    //number_of_points = 51;
    for (j = 0; j < number_of_points; j += 3)   //每間隔2點算一次
    {
        //printf("j=%d v = %f ", j, points2[j][0]);

                 //target,        u1,  u2,  stride, order, *points
        glMap1f(GL_MAP1_VERTEX_3, 0.0, STEPS, 3, 4, &points2[j][0]);
        glBegin(GL_LINE_STRIP);
        for (i = 0; i <= STEPS; i++)
        {
            //0~20, 共21次
            glEvalCoord1f((float)i);
        }
        glEnd();
    }

    glFlush();  // 執行繪圖命令
}

void display6(void)
{

}

void display7(void)
{

}

void display8(void)
{

}

void display9(void)
{

}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        reset_default_setting();
    }
    else if (display_mode < 5)
    {
        display1234();
    }
    else if (display_mode == 5)
    {
        display5();
    }
    else
    {
        reset_default_setting();
    }

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    gluOrtho2D(-0.1f, 1.1f, -0.1f, 1.1f);   //已知數據的範圍 才能這麼寫
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
    case '0':
        display_mode = 0;
        break;
    case '1':
        display_mode = 1;
        break;
    case '2':
        display_mode = 2;
        break;
    case '3':
        display_mode = 3;
        break;
    case '4':
        display_mode = 4;
        break;
    case '5':
        display_mode = 5;
        break;
    case '6':
        display_mode = 6;
        break;
    case '7':
        display_mode = 7;
        break;
    case '8':
        display_mode = 8;
        break;
    case '9':
        display_mode = 9;
        break;
    case '?':
        break;
    }
    make_data(display_mode);
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

void idle(void)
{
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

int main(int argc, char** argv)
{
    const char* windowName = "簡單2D OpenGL畫圖 0 ~ 9";
    const char* message = "簡單2D OpenGL畫圖 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    //glutIdleFunc(idle);

    make_data(display_mode);

    glutMainLoop();	//開始主循環繪製

    return 0;
}
