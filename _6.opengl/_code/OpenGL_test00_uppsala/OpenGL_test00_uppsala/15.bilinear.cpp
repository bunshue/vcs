/****************************************************************************
 * bilinear.cpp                                                             *
 *    This graphics program constructs a bilinear patch for a surface       *
 * defined by four corners.                                                 *
 * NOTE:  At this time the z component of the surface is ignored, giving a  *
 *        parallel projection onto the x,y-plane, which is assumed to be    *
 *        the display device.                                               *
 ****************************************************************************/

#include "../../Common.h"

float x[2][2];
float y[2][2];
float z[2][2];  //沒用到, 預留

void gfxinit(void)
{
    float u, u1, v, v1, x1, y1, x2, y2;

    /* Initialize graphics mode.  Assume all coordinates are in [-10,10]. */

    glClearColor(1.0, 1.0, 1.0, 0.0);  //背景白色
    glColor3f(1.0, 0.0, 0.0);          //畫紅線
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0);   //設定畫圖邊界 x= -10 ~ 10, y = -10 ~ 10

    //在 List 1 製作第1張圖
    glNewList(1, GL_COMPILE);

    /* Draw the rulings of u (constant u values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    glBegin(GL_LINES);
    for (u = 0.0f; u < 1.001f; u += 0.1f)
    {
        u1 = 1.0f - u;
        x1 = u1 * x[0][0] + u * x[1][0];
        y1 = u1 * y[0][0] + u * y[1][0];
        x2 = u1 * x[0][1] + u * x[1][1];
        y2 = u1 * y[0][1] + u * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }

    /* Draw the rulings of v (constant v values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    for (v = 0.0f; v < 1.001f; v += 0.1f)
    {
        v1 = 1.0f - v;
        x1 = v1 * x[0][0] + v * x[0][1];
        y1 = v1 * y[0][0] + v * y[0][1];
        x2 = v1 * x[1][0] + v * x[1][1];
        y2 = v1 * y[1][0] + v * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }
    glEnd();

    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 1.0, 0.0);          //畫黃線
    glCallList(1);  //顯示第1張圖

    draw_coordinates(8.0f);     //畫座標軸

    //用 GL_LINE_LOOP 畫一個空心矩形
    glColor3f(0.0, 1.0, 0.0);          //畫綠框
    float dd = 8.2f;
    float point1[3] = { -dd, -dd, 0 };	//左下
    float point2[3] = { dd, -dd, 0 };	//右下
    float point3[3] = { dd,  dd, 0 };	//右上
    float point4[3] = { -dd,  dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();

    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    //第一條線之起點, 左下
    x[0][0] = -8;
    y[0][0] = -8;
    z[0][0] = -85;   //z先不管

    //第一條線之終點, 右下
    x[0][1] = 8;
    y[0][1] = -3;
    z[0][1] = 85;    //z先不管

    //第二條線之起點, 左上
    x[1][0] = -8;
    y[1][0] = 8;
    z[1][0] = 25;    //z先不管

    //第二條線之終點, 右上
    x[1][1] = 8;
    y[1][1] = 3;
    z[1][1] = -35;   //z先不管

    const char* windowName = "Bilinear Patch";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
