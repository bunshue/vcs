#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    gluOrtho2D(-2.0, 2.0, -2.0, 2.0);   //窗口座標範圍, 2D	//顯示範圍 x(-125 ~ 125), y(-125 ~ 125)

    draw_boundary(color_y, 3.8f); //畫視窗邊界

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
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Translate用法");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard); //設定callback function
    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");
    printf("\nTranslate用法\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

