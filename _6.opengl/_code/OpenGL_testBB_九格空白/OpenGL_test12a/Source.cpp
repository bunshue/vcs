#include "../../Common.h"

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

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
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
        reset_default_setting();

        //畫一個矩形 R
        glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
        //左下x,左下y,右上x,右上y,
        glRectf(-0.9f, -0.9f, -0.3f, 0.9f);//畫一個矩形

        ////畫一個矩形 G
        glColor4f(0.0, 1.0, 0.0, 1.0);  //設置畫筆顏色為 G
        //左下x,左下y,右上x,右上y,
        glRectf(-0.4f, -0.8f, 0.4f, 0.8f);//畫一個矩形

        //畫一個矩形 B
        glColor4f(0.0, 0.0, 1.0, 1.0);  //設置畫筆顏色為 B
        //左下x,左下y,右上x,右上y,
        glRectf(0.3f, -0.7f, 0.7f, 0.7f);//畫一個矩形

        float x_st = -0.9f;
        float y_st = 0.1f;
        const char str1[30] = "draw_string_test 1";
        draw_string1(str1, color_c, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

        x_st = -0.9f;
        y_st = -0.1f;
        const char str2[30] = "draw_string_test 2";
        draw_string2(str2, color_c, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

        draw_boundary(color_y, 0.9f); //畫視窗邊界
    }
    else if (display_mode == 2)
    {
        reset_default_setting();
    }
    else if (display_mode == 3)
    {
        reset_default_setting();
    }
    else if (display_mode == 4)
    {
        reset_default_setting();
    }
    else if (display_mode == 5)
    {
        reset_default_setting();
    }
    else if (display_mode == 6)
    {
        reset_default_setting();
    }
    else if (display_mode == 7)
    {
        reset_default_setting();
    }
    else if (display_mode == 8)
    {
        reset_default_setting();
    }
    else if (display_mode == 9)
    {
        reset_default_setting();
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

    glFlush();  //強制刷新緩存區
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
}

int main(int argc, char* argv[])
{
    const char* windowName = "繪製基本圖元 0 ~ 9";
    const char* message = "繪製基本圖元 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    glutSetCursor(GLUT_CURSOR_DESTROY); //改變視窗上的鼠標標記

    glutMainLoop();	//開始主循環繪製     // Enter the event-processing loop

    return 0;
}

