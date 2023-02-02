#include "../../Common.h"

void gfxinit1()
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 12.0, 0.0, 12.0);   //窗口座標範圍2D, 顯示範圍 : X軸(0 ~ 12) Y軸(0 ~ 12), 左下為原點

    glNewList(1, GL_COMPILE);
    for (int index = 0; index < 30; index++)
    {
        //超過20的都是黑色
        if (index >= 20)
        {
            glIndexi(2);
        }
        else
        {
            glIndexi(index);
        }
        printf("Color %d = (%f, %f, %f)\n",
            index, glutGetColor(index, GLUT_RED), glutGetColor(index, GLUT_GREEN), glutGetColor(index, GLUT_BLUE));
        glRectf((float)(index % 10), 3.0f * (index / 10), (float)(index % 10) + 1.0f, 3.0f * (index / 10) + 3.0f);
    }
    glEndList();
}

void gfxinit2()
{
    glNewList(2, GL_COMPILE);

    GLint index = 0;
    float x_st = -0.9f;
    float y_st = -0.9f;
    float w = 0.4f;
    float h = 0.15f;

    int i;

    for (i = 0; i < 30; i++)
    {
        index = i;
        glIndexi(index);    //index應該只能從 0 ~ 19 共20個

        x_st = -0.9f + (i / 10) * (w + 0.02f);
        y_st = -0.9f + (i % 10) * (h + 0.02f);
        glRectf(x_st, y_st, x_st + w, y_st + h);  //實心矩形
    }

    glEndList();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    glCallList(1);

    glutSwapBuffers();  // 執行繪圖命令
    //glFlush();          // 執行繪圖命令


    /*
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    glClearIndex(1.5f);

    glCallList(2);

    glutSwapBuffers();  // 執行繪圖命令
    //glFlush();          // 執行繪圖命令
    */

}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);    //宣告顯示模式為 Single Buffer 和 INDEX
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_INDEX);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("OpenGL測試 GLUT_INDEX");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");
    printf("Number of bits in color index = %d\n", glutGet(GLUT_WINDOW_BUFFER_SIZE));
    printf("Single Buffer 可以看到畫面閃爍, Double Buffer則無\n");

    gfxinit1();
    //gfxinit2();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

