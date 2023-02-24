#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //gluOrtho2D(-2.0, 2.0, -2.0, 2.0);   //窗口座標範圍, 2D	//顯示範圍 x(-125 ~ 125), y(-125 ~ 125)
    //draw_boundary(color_y, 3.8f); //畫視窗邊界

    draw_coordinates(1.1f);     //畫座標軸
    draw_boundary(color_y, 0.9f); //畫視窗邊界

    int i;
    int j;
    for (j = 0; j < 5; j++)
    {
        glPushMatrix();

        //glScalef(1.0f, 0.5f, 1.0f);		//縮放各方向顯示比例, 例如y軸減半

        glTranslatef(-0.9f, -0.9f + j * 0.45f, 0.0f);	//平移至指定地方(累積)

        for (i = 0; i < 5; i++)
        {
            //glScalef(0.8f, 1.0f, 1.0f);		//縮放各方向顯示比例, 例如x軸越來越窄

            draw_teapot(color_r, 1, 0.07f);   //畫一個茶壺
            glTranslatef(0.45f, 0.0f, 0.0f);	//平移至指定地方(累積)
        }

        glPopMatrix();
    }
    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    const char* windowName = "Translate用法";
    const char* message = "Translate用法, 僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

