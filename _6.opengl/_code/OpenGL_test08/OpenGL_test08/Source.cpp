#include "../../Common.h"

#define REFRESH_DELAY 1000  // ms

int display_mode = 1;

void reset_default_setting()
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

    glLineWidth(1.0f);	//設定線寬
}

float my_function(float a)
{
    return sin(a * 4) / 2;
}

void plotCurve(float (*func)(float), float* color, float x_st, float x_sp, const int steps)
{
    if (x_st >= x_sp)
    {
        printf("格式錯誤\n");
        return;
    }

    float dd = x_sp - x_st;

    glColor3fv((GLfloat*)color);    //設定顏色

    glBegin(GL_LINE_STRIP);	//繪製前後連接的點組成的線
    for (int i = 0; i < steps; i++)
    {
        Point pt;

        pt.x = dd * i / (float)(steps - 1) + x_st;
        pt.y = func(pt.x);

        glVertex2f(pt.x, pt.y);
        //printf("i = %d (%f, %f)\n", i, pt.x, pt.y);
    }
    glEnd();
}

void draw_math_function1(void)
{
    //畫數學函數曲線
    float x_st = -(float)PI / 4.0f;
    float x_sp = (float)PI / 4.0f;
    int steps = 30;
    plotCurve(my_function, color_r, x_st, x_sp, steps);
}

Point pt[50];
int pt_count = 0;

void SetPoint(float x, float y)
{
    pt[pt_count].x = x;
    pt[pt_count].y = y;
    pt_count++;
}

void draw_math_function2(void)
{
    int i;

    printf("draw_math_function2()\n");

    printf("Make some data\n");

    pt_count = 0;

    float x;
    float y;
    for (i = 0; i < 50; i++)
    {
        x = -1.0f + 2.0f * (float)i / 50;
        y = sin(x * 4) / 2;
        SetPoint(x, y);
    }

    glColor3f(1.0, 0.0, 1.0);
    glPointSize(10.0f); 	//設定點的大小, N X N
    glBegin(GL_POINTS);
    for (i = 0; i < pt_count; i++)
    {
        glVertex2f(pt[i].x, pt[i].y);
    }
    glEnd();

    glFlush();  // 執行繪圖命令
}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        printf("無畫面, TBD, display_mode = %d\n", display_mode);

        //設定預設大小...  TBD
    }
    else if (display_mode == 1)
    {

        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        draw_boundary(color_y, 0.9f); //畫視窗邊界

        draw_math_function1();
    }
    else if (display_mode == 2)
    {
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        draw_boundary(color_y, 0.9f); //畫視窗邊界

        draw_math_function2();
    }
    else if (display_mode == 3)
    {


    }

    glFlush();  // 執行繪圖命令
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;
        break;
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
    }

    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

void timerEvent(int value)
{
    //printf("%d ", display_mode);

    if (display_mode == 3)
    {
        printf("經過1秒 ");
        //glutPostRedisplay();

    }
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
}

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL測試";
    const char* message = "OpenGL測試\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    glutMouseFunc(mouse0);      //設定callback function
    glutMotionFunc(motion0);    //設定callback function
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    printf("按 1 2 控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

