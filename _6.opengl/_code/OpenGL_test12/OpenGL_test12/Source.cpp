#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>
#include "../../Common.h"

#define PI_F             3.141592654F

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   // 清除之前幀數據

    float x_st = 0.0f;
    float y_st = 12.0f;
    float dd = 0;

    //畫點
    glPointSize(50.0f);	//設定點的大小, N X N
    glBegin(GL_POINTS);
    glColor3f(1.0, 0.0, 0.0);	//紅
    glVertex2f(0, 0);
    glEnd();

    glPointSize(2.0f); 	//設定點的大小, N X N
    glBegin(GL_POINTS);
    for (x_st = -14.0; x_st < -5.0f; x_st += 0.5f)
    {
        glColor3f(1.0, 0.0, 0.0);	//紅
        glVertex2f(x_st, y_st);

        glColor3f(0.0, 1.0, 0.0);	//綠
        glVertex2f(x_st, y_st - 0.5f);

        glColor3f(1.0, 1.0, 0);	//黃
        glVertex2f(x_st, y_st - 1.0f);
    }
    glEnd();

    //畫直線連線
    float offset = 13.0;

    //畫視窗邊界
    float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
    draw_boundary(color_yellow, offset);

    //畫線
    //畫直線連線
    glBegin(GL_LINE_STRIP);	//繪製前後連接的點組成的線
    glColor3f(0.0, 1.0, 0.0);
    for (x_st = -14.0; x_st <= -5.0f; x_st += 0.5f)
    {
        if (y_st != 7.0f)
            y_st = 7.0f;
        else
            y_st = 10.0f;

        glVertex2f(x_st, y_st);
    }
    glEnd();

    //畫正弦波
    glBegin(GL_LINE_STRIP);	//繪製前後連接的點組成的線
    glColor3f(0.0, 1.0, 1.0);
    for (x_st = -14.0; x_st <= -5.0f; x_st += 0.1f)
    {
        y_st = sin(x_st * 2) + 1.0;
        glVertex2f(x_st, y_st);
    }
    glEnd();

    //畫線
    //畫封閉曲線
    glBegin(GL_LINE_LOOP);
    glColor3f(0.0, 1.0, 0.0);
    for (x_st = -14.0; x_st <= -5.0f; x_st += 0.5f)
    {
        if (y_st != 4.0f)
            y_st = 4.0f;
        else
            y_st = 7.0f;

        glVertex2f(x_st, y_st);
    }
    glVertex2f(-5.0, 3.0);
    glEnd();

    //畫多邊形
    float cx = 6.0f;
    float cy = 6.0f;
    float r = 6.0f;
    glBegin(GL_POLYGON);
    glColor3f(0.5, 0.3, 0.7);
    for (int angle = 0; angle < 360; angle += 36)
    {
        x_st = cx + r * cosf(2 * PI_F * angle / 360);
        y_st = cy + r * sinf(2 * PI_F * angle / 360);
        glVertex2f(x_st, y_st);
    }
    glEnd();

    //畫四邊形, 4個頂點為一組
    glBegin(GL_QUADS);
    glColor3f(0.7, 0.5, 0.2);
    cx = -4.0f;
    cy = -2.0f;
    dd = 2.0f;
    glVertex2f(cx, cy + dd);  //上
    glVertex2f(cx + dd, cy);  //右
    glVertex2f(cx, cy - dd);  //下
    glVertex2f(cx - dd, cy);  //左

    glColor3f(0.5, 0.7, 0.2);
    cx = -4.0f;
    cy = -2.0f - 4.0f;
    dd = 2.0f;
    glVertex2f(cx, cy + dd);  //上
    glVertex2f(cx - dd, cy);  //左
    glVertex2f(cx, cy - dd);  //下
    glVertex2f(cx + dd, cy);  //右

    glEnd();

    //畫三角形, 三個頂點為一組
    glBegin(GL_TRIANGLES);
    glColor3f(0.2, 0.5, 0.7);
    x_st = -9.0;
    y_st = -0.0;
    dd = 3.0;
    glVertex2f(x_st, y_st);    //上
    glVertex2f(x_st - dd, y_st - dd);   //左下
    glVertex2f(x_st + dd, y_st - dd);   //右下

    y_st -= dd;
    glVertex2f(x_st, y_st);    //上
    glVertex2f(x_st - dd, y_st - dd);   //左下
    glVertex2f(x_st + dd, y_st - dd);   //右下

    y_st -= dd;
    glVertex2f(x_st, y_st);    //上
    glVertex2f(x_st - dd, y_st - dd);   //左下
    glVertex2f(x_st + dd, y_st - dd);   //右下

    glEnd();

    //畫三角形帶
    x_st = 4.0;
    y_st = -5.0;
    dd = 2.0;
    glBegin(GL_TRIANGLE_STRIP);
    glColor3f(1.0, 0.0, 0.0);   //紅區
    glVertex2f(x_st, y_st);
    glVertex2f(x_st - dd, y_st + dd);

    glColor3f(0.0, 1.0, 0.0);   //綠區
    glVertex2f(x_st + dd, y_st);

    glColor3f(0.0, 0.0, 1.0);   //藍區
    glVertex2f(x_st, y_st + dd * 2);

    glColor3f(1.0, 1.0, 0.0);   //黃區
    glVertex2f(x_st + dd, y_st + dd);

    glEnd();

    //畫三角形扇
    x_st = 2.0;
    y_st = -8.0;
    dd = 2.0;
    glBegin(GL_TRIANGLE_FAN);
    glColor3f(1.0, 0.0, 0.0);   //紅區
    glVertex2f(x_st, y_st);
    glVertex2f(x_st + dd, y_st + dd);

    glColor3f(0.0, 1.0, 0.0);   //綠區
    glVertex2f(x_st + dd * 2, y_st);

    glColor3f(0.0, 0.0, 1.0);   //藍區
    glVertex2f(x_st + dd * 2, y_st - dd);

    glColor3f(1.0, 1.0, 0.0);   //黃區
    glVertex2f(x_st, y_st - dd);
    glEnd();

    x_st = 10.0f;
    y_st = -12.0f;
    dd = 2.5;
    glBegin(GL_QUAD_STRIP); //多邊形帶
    glColor3f(1.0, 0.0, 0.0);   //紅區
    glVertex2f(x_st, y_st);  //正下
    glVertex2f(x_st - dd, y_st + dd);   //左下
    glVertex2f(x_st + dd, y_st + dd);  //右下

    glColor3f(0.0, 1.0, 0.0);   //綠區
    glVertex2f(x_st - dd, y_st + dd * 2);   //左
    glVertex2f(x_st + dd, y_st + dd * 2);  //右

    glColor3f(0.0, 0.0, 1.0);   //藍區
    glVertex2f(x_st - dd, y_st + dd * 3);   //左
    glVertex2f(x_st + dd, y_st + dd * 3);  //右

    glColor3f(1.0, 1.0, 0.0);   //黃區
    glVertex2f(x_st, y_st + dd * 4);  //正上
    glEnd();

    float color[4] = { 0.0f, 1.0f, 0.0f, 1.0f };
    x_st = -1.2;
    y_st = 0;
    const char str[30] = "Write Something";
    draw_string1(str, color, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    //printf("reshape is called\n");
    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();   //設置單位矩陣

    gluLookAt(0, 0, 25, 0, 0, -1, 0, 1, 0);
    //eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz
    //第一組eyex, eyey, eyez 相機在世界坐標的位置
    //第二組centerx, centery, centerz 相機鏡頭對準的物體在世界坐標的位置
    //第三組upx, upy, upz 相機向上的方向在世界坐標中的方向
    //你把相機想象成為你自己的腦袋：
    //第一組數據就是腦袋的位置
    //第二組數據就是眼睛看的物體的位置
    //第三組就是頭頂朝向的方向（因為你可以歪著頭看同一個物體）。
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(1200, 600);		// 設定視窗大小
    glutInitWindowPosition(600, 200);	// 設定視窗位置

    glutCreateWindow("幾何圖形繪製");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard0);	//設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

