#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    glClearIndex(1.5f);

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

    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);    //宣告顯示模式為 Single Buffer 和 INDEX

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("OpenGL測試 GLUT_INDEX");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

