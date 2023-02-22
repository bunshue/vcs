#include "../../Common.h"

float angle = 0;

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glRotated(angle, 1, 1, 0);

    draw_coordinates(0.8);
    draw_teapot(color_y, 1.0, 0.5);	//畫一個茶壺

    glFlush();  // 執行繪圖命令

    angle += 0.2f;
}

static void idle(void)
{
    glutPostRedisplay();
    sleep(100);
}

int main(int argc, char** argv)
{
    const char* windowName = "簡單2D OpenGL畫圖 0 ~ 9";
    const char* message = "簡單2D OpenGL畫圖 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutIdleFunc(idle);			//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}
