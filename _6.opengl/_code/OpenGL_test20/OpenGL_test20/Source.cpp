#include "../../Common.h"

void gfxinit()
{
    int i, index = 0;

    gluOrtho2D(-1.0, 9.0, -0.2, 2.2);

    /* Generate the colors on the screen. */
    glNewList(1, GL_COMPILE);
    /* default color map entries */
    for (i = 0; i < 8; i++, index++)
    {
        printf("index = %d\n", index);
        glIndexi(index);
        printf("Color %d = (%f, %f, %f)\n", index, glutGetColor(index, GLUT_RED), glutGetColor(index, GLUT_GREEN), glutGetColor(index, GLUT_BLUE));
        cout << "Color " << index << " = (" << glutGetColor(index, GLUT_RED)
            << ", " << glutGetColor(index, GLUT_GREEN) << ", "
            << glutGetColor(index, GLUT_BLUE) << ")" << endl;
        glRecti(i, 0, i + 1, 1);  //下排
    }

    index += 2;
    for (i = 0; i < 8; i++, index++)
    {
        printf("---index = %d\n", index);
        glIndexi(index);
        printf("Color %d = (%f, %f, %f)\n", index, glutGetColor(index, GLUT_RED), glutGetColor(index, GLUT_GREEN), glutGetColor(index, GLUT_BLUE));
        cout << "Color " << index << " = (" << glutGetColor(index, GLUT_RED)
            << ", " << glutGetColor(index, GLUT_GREEN) << ", "
            << glutGetColor(index, GLUT_BLUE) << ")" << endl;
        glRecti(i, 1, i + 1, 2);    //上排
    }
    glEndList();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    glCallList(1);

    glutSwapBuffers();  // 執行繪圖命令   不會閃爍
    //glFlush();  // 執行繪圖命令 會閃爍
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);    //宣告顯示模式為 Single Buffer 和 INDEX
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_INDEX);    //宣告顯示模式為 Double Buffer 和 INDEX

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("OpenGL測試");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");
    printf("\n空白範例\n");

    gfxinit();

    glutMainLoop();	//開始主循環繪製
    return 0;
}

