#include "../../Common.h"

int display_mode = 1;

int full_screen = 0;

void Init_List()
{
    glNewList(1, GL_COMPILE);
    draw_teapot(color_r, 1, 0.5);   //畫一個茶壺
    glEndList();

    glNewList(2, GL_COMPILE);
    glColor3f(0.0, 1.0, 1.0);   //設定顏色 cc
    float dd = 0.3f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形
    glEndList();

    glNewList(3, GL_COMPILE);
    glColor3f(1.0, 0.0, 1.0);   //設定顏色 cc
    dd = 0.6f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形
    glEndList();
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

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    glCallList(display_mode);

    glFlush();  // 執行繪圖命令
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
    const char* windowName = "glList 測試, 3種list, 用 1~3 切換";
    const char* message = "glList 測試, 3種list, 用 1~3 切換\n";

    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    Init_List();
    printf("\nglList 測試\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}


