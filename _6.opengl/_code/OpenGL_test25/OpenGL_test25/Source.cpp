#include "../../Common.h"

int board[3][3];	/*  amount of color for each square	*/

/*	Clear color value for every square on the board	    */
void myinit(void)
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            board[i][j] = 0;
        }
    }
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

/*  The nine squares are drawn.  In selection mode, each
 *  square is given two names:  one for the row and the
 *  other for the column on the grid.  The color of each
 *  square is determined by its position on the grid, and
 *  the value in the board[][] array.
 */
void drawSquares(GLenum mode)
{
    GLuint i, j;

    for (i = 0; i < 3; i++)
    {
        if (mode == GL_SELECT)
        {
            glLoadName(i);
        }
        for (j = 0; j < 3; j++)
        {
            if (mode == GL_SELECT)
            {
                glPushName(j);
            }
            glColor3f((GLfloat)i / 3.0f, (GLfloat)j / 3.0f, (GLfloat)board[i][j] / 3.0f);

            glRecti(i, j, i + 1, j + 1);

            if (mode == GL_SELECT)
            {
                glPopName();
            }
        }
    }
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    drawSquares(GL_RENDER);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 3.0, 0.0, 3.0);
    //gluOrtho2D(-3.0, 3.0, -3.0, 3.0);
}

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL測試";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    printf("\n空白範例\n");

    myinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

