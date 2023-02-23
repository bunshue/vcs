//測試語法專用

#include "../../Common.h"

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //全圖黑色

    draw_boundary(color_y, 0.9f); //畫視窗邊界
    draw_teapot(color_r, 1, 0.3);   //畫一個茶壺

    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    const char* windowName = "測試語法";
    const char* message = "測試語法 專用, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

