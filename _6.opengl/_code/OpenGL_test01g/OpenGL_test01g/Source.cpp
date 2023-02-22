#include "../../Common.h"

#define REFRESH_DELAY 1000  // ms

int time_elapsed = 0;

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    //畫一個實心矩形
    glColor3f(0.0, 1.0, 1.0);   //設定顏色 cc
    float dd = 0.3f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形

    draw_teapot(color_r, 1, 0.3);   //畫一個茶壺

    float x_st = -0.7f;
    float y_st = 0.5f;
    const char str1[30] = "Empty example";
    draw_string1(str1, color_r, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

    glFlush();  // 執行繪圖命令

    char info[20];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "經過 %d 秒", time_elapsed);
    glutSetWindowTitle(info);
}

void keyboardup(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("keyboardup ");
    //keyDown[key] = false;
}

void timerEvent(int value)
{
    time_elapsed++;
    //printf("%d ", time_elapsed);
    glutPostRedisplay();
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
}

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL測試";
    const char* message = "其他callback函數使用範例, 僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutKeyboardUpFunc(keyboardup);//設定callback function
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}
