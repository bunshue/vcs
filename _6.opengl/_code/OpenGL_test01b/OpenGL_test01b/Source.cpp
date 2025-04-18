﻿#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
    float x_st = 0.0f;
    float y_st = 0.0f;
    float dd = 0.3f;

    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    draw_teapot(color_r, 1, 0.3);   //畫一個茶壺

    x_st = -0.8f;
    y_st = -0.8f;
    const char str1[30] = "Common.cpp useage";
    draw_string1(str1, color_r, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

    x_st = 0.0f;
    y_st = 12.0f;
    //畫點
    float size = 50.0;  //設定點的大小, N X N
    x_st = -0.9f;
    y_st = 0.9f;
    draw_point(color_r, size, x_st, y_st);

    size = 10.0f;    //設定點的大小, N X N
    x_st = 0.0f;
    y_st = 0.8f;
    for (x_st = -0.9f; x_st < -0.3f; x_st += 0.05f)
    {
        draw_point(color_r, size, x_st, y_st);
        draw_point(color_g, size, x_st, y_st - 0.08f);
        draw_point(color_b, size, x_st, y_st - 0.16f);
    }

    //畫實心四邊形, 4個頂點為一組
    float cx = 0.0f;
    float cy = 0.0f;
    float r = 0.5f;
    cx = -0.6f;
    cy = -0.2f;
    dd = 0.2f;
    float x1 = cx;  //第1點
    float y1 = cy + dd;
    float x2 = cx + dd;
    float y2 = cy;
    float x3 = cx;
    float y3 = cy - dd;
    float x4 = cx - dd;
    float y4 = cy;
    draw_quad_s(color_r, x1, y1, x2, y2, x3, y3, x4, y4);

    x_st = -0.6f;
    y_st = -0.4f;
    dd = 0.2f;
    x1 = x_st;    //第1點
    y1 = y_st;
    x2 = x_st - dd / 2;
    y2 = y_st - dd;
    x3 = x_st + dd / 2;
    y3 = y_st - dd;
    draw_triangle_s(color_g, x1, y1, x2, y2, x3, y3);

    GLdouble base = 0.2;
    GLdouble height = 0.6;
    GLint slices = 100;
    GLint stacks = 10;
    float width = 1.0f;
    draw_cone(color_y, width, base, height, slices, stacks); //畫圓錐體

    draw_cube(color_g, 2, 0.9);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;

    case '1':
        printf("1\n");
        break;

    case '2':
        printf("2\n");
        break;

    case '3':
        break;

    case '4':
        break;

    case '?':
        break;
    }
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

int main(int argc, char** argv)
{
    const char* windowName = "我的Common使用範例";
    const char* message = "我的Common使用範例\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    printf("1\n");
    sleep(100);    //暫停 xx msec
    printf("2\n");
    sleep(100);

    printf("3\n");
    sleep(100);

    printf("4\n");
    sleep(100);
    printf("5\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

