#include "../../Common.h"

int window_width = 0;
int window_height = 0;

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_coordinates(0.8f);

    draw_teapot(color_r, 1, 0.3);   //畫一個茶壺
    draw_rectangle(color_y, 1, -0.3f, -0.3f, 0.6f, 0.6f);

    draw_rectangle(color_y, 1, -0.95f, -0.95f, 1.90f, 1.90f);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    window_width = w;
    window_height = h;

    //視口設定為全部視窗
    int viewportx = 0;
    int viewporty = 0;
    int viewportw = window_width;
    int viewporth = window_height;
    glViewport(viewportx, viewporty, viewportw, viewporth);
    //printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\n", viewportx, viewporty, viewportw, viewporth);
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
    case '+':
        printf("0\n");
        gluOrtho2D(-0.5, 0.5, -0.5, 0.5);   //窗口座標範圍2D, 顯示範圍 : X軸(-1.0 ~ 1.0) Y軸(-1.0 ~ 1.0), 左下為原點
        break;
    case '-':
        printf("1\n");
        gluOrtho2D(-2.0f, 2.0f, -2.0f, 2.0f);
        break;

    case 'V':
        printf("V\n");
        int viewportx = 0;
        int viewporty = 0;
        int viewportw = window_width;
        int viewporth = window_height;
        glViewport(viewportx, viewporty, viewportw, viewporth);
        //printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\n", viewportx, viewporty, viewportw, viewporth);


        break;
    }
    glutPostRedisplay();
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL測試";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    printf("\n空白範例\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}




