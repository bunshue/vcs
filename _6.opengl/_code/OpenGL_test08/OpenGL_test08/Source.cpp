#include "../../Common.h"

int display_mode = 1;

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

        //畫數學函數曲線
        float x_st = -(float)PI / 4.0f;
        float x_sp = (float)PI / 4.0f;
        int steps = 30;
        plotCurve(my_function, color_r, x_st, x_sp, steps);
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
    sprintf_s(info, 10, "%d", display_mode);

    glutSetWindowTitle(info);
}

int main(int argc, char** argv)
{
    //初始化GLUT庫，這個函數只是傳說命令參數并且初始化glut庫
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("OpenGL測試");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function
    glutMouseFunc(mouse0);       //設定callback function
    glutMotionFunc(motion0);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

