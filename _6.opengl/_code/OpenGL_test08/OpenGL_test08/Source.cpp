//#include "../../../_code/Common.h"    //32 bits
#include "../../Common.h"               //64 bits

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
        float x = dd * i / (float)(steps - 1) + x_st;
        glVertex2f(x, func(x));
        //printf("i = %d (%f, %f)\n", i, x, func(x));
    }
    glEnd();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    //畫數學函數曲線
    float x_st = -(float)PI / 4.0f;
    float x_sp = (float)PI / 4.0f;
    int steps = 30;
    plotCurve(my_function, color_r, x_st, x_sp, steps);

    glFlush();  // 執行繪圖命令
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

