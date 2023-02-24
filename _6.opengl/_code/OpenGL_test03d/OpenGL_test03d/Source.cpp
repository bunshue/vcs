#include "../../Common.h"

int display_mode = 1;

int full_screen = 0;

void reset_default_setting()
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

    glLineWidth(1.0f);	//設定線寬

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
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
    printf("draw_math_function1()\n");
    //畫數學函數曲線
    float x_st = -(float)PI / 4.0f;
    float x_sp = (float)PI / 4.0f;
    int steps = 30;
    plotCurve(my_function, color_r, x_st, x_sp, steps);
}

#define POINTS     50
Point pt[POINTS];
int pt_count = 0;

void draw_math_function2(void)
{
    printf("draw_math_function2()\n");

    int i;
    float x;
    float y;
    pt_count = 0;
    for (i = 0; i < POINTS; i++)
    {
        x = -1.0f + 2.0f * (float)i / POINTS;
        y = sin(x * 4) / 2;

        pt[pt_count].x = x;
        pt[pt_count].y = y;
        pt_count++;
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

void print_data()
{
    printf("共 %d 筆資料, 內容:\n", POINTS);
    for (int i = 0; i < POINTS; i++)
    {
        printf("(%d, %f)", (int)(pt[i].x), pt[i].y);
        if (i % 6 == 5)
            printf("\n");
        else
            printf(" ");
    }
    printf("\n");

    for (int i = 0; i < POINTS; i++)
    {
        printf("%0.10f  %0.10f\n", pt[i].x, pt[i].x);
    }

    return;
}

void display1()
{
    reset_default_setting();

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    draw_math_function1();
    glFlush();  // 執行繪圖命令
}

void display2()
{
    reset_default_setting();

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    draw_math_function2();
    glFlush();  // 執行繪圖命令

}

/* Drawing constants. */
#define STEPS        10  /* number of steps to draw each segment over */
#define PATCHES      32  /* number of surfaces in the teapot          */
#define VERTICES    306  /* number of control points                  */

double points[VERTICES + 1][3];
int patch_vertices[PATCHES][16];

void make_teapot_data(void)
{
    ifstream vertices_file;
    ifstream patches_file;
    int i;
    int j;

    //開啟檔案
    printf("開啟檔案: data/teapot.vertices\n");
    vertices_file.open("data/teapot.vertices", ios::in);
    if (vertices_file.fail())
    {
        printf("找不到檔案: data/teapot.vertices\n");
        patches_file.close();
        exit(EXIT_FAILURE);
    }

    printf("開啟檔案: data/teapot.patches\n");
    patches_file.open("data/teapot.patches", ios::in);
    if (patches_file.fail())
    {
        printf("找不到檔案: data/teapot.patches\n");
        exit(EXIT_FAILURE);
    }

    //讀取檔案資料
    for (i = 1; i <= VERTICES; i++)
    {
        vertices_file >> points[i][0] >> points[i][1] >> points[i][2];  //C++之讀取檔案資料
    }
    for (i = 0; i < PATCHES; i++)
    {
        for (j = 0; j < 16; j++)
        {
            patches_file >> patch_vertices[i][j];   //C++之讀取檔案資料
        }
    }
    vertices_file.close();
    patches_file.close();
}

void init_teapot_data(void)
{
    int i;
    int j;
    int k;
    int vertex;
    double coords[48];
    double* p;

    glClearColor(1.0, 1.0, 1.0, 0.0);   //背景為白色
    glEnable(GL_MAP2_VERTEX_3);

    /* Generate the display lists for the surfaces. */
    for (k = 0; k < PATCHES; k++)
    {
        for (i = 0, p = coords; i < 16; i++)
        {
            vertex = patch_vertices[k][i];
            for (j = 0; j < 3; j++, p++)
            {
                *p = points[vertex][j];
            }
        }
        glNewList(k + 1, GL_COMPILE);
        glColor3d(1.0, 1.0, 0.0);   //黃色
        glMap2d(GL_MAP2_VERTEX_3, 0.0, 1.0, 12, 4, 0.0, 1.0, 3, 4, coords);
        glMapGrid2d(STEPS, 0.0, 1.0, STEPS, 0.0, 1.0);
        glEvalMesh2(GL_FILL, 0, STEPS, 0, STEPS);
        glEndList();
    }
}

void display3()
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    glLoadIdentity();

    glOrtho(-4.0, 4.0, -4.0, 4.0, -4.0, 4.0);

    for (int i = 1; i <= PATCHES; i++)
    {
        glCallList(i);
    }

    //已旋轉後之座標軸
    draw_coordinates(2.5f);     //畫座標軸

    glFlush();  // 執行繪圖命令
}

void display4()
{

}

void display5()
{

}

void display6()
{

}

void display7()
{

}

void display8()
{

}

void display9()
{

}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        reset_default_setting();
    }
    else if (display_mode == 1)
    {
        display1();
    }
    else if (display_mode == 2)
    {
        display2();
    }
    else if (display_mode == 3)
    {
        display3();
    }
    else if (display_mode == 4)
    {
        display4();
    }
    else if (display_mode == 5)
    {
        display5();
    }
    else if (display_mode == 6)
    {
        display6();
    }
    else if (display_mode == 7)
    {
        display7();
    }
    else if (display_mode == 8)
    {
        display8();
    }
    else if (display_mode == 9)
    {
        display9();
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }
    glFlush();  // 執行繪圖命令
    glutSwapBuffers();  // 將後緩沖區繪製到前臺
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
        break;
    case ' ':
        if (full_screen == 0)
        {
            full_screen = 1;
            printf("全螢幕\n");
            glutFullScreen();   //全螢幕顯示
        }
        else
        {
            //恢復成一般螢幕, 有問題
            full_screen = 0;
            printf("一般螢幕\n");
            glutInitWindowSize(600, 600);       // 設定視窗大小
            glutInitWindowPosition(1100, 200);  // 設定視窗位置
        }
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
        printf("猶太茶壺\n");
        make_teapot_data();		//讀取資料
        init_teapot_data();
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
}

int main(int argc, char** argv)
{
    const char* windowName = "簡單2D OpenGL畫圖 0 ~ 9";
    const char* message = "簡單2D OpenGL畫圖 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    glutMainLoop();	//開始主循環繪製

    return 0;
}


