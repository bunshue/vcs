#include "../../Common.h"

int list_number = 1;

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

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    glCallList(list_number);

    glFlush();  // 執行繪圖命令
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
        list_number = 1;
        break;

    case '2':
        printf("2\n");
        list_number = 2;
        break;

    case '3':
        list_number = 3;
        break;

    case '4':
        break;

    case '?':
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

    printf("僅顯示, 無控制, 按 Esc 離開\n");
    printf("\nglList 測試\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

