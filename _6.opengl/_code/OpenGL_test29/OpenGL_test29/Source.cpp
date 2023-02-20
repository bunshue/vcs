#include "../../Common.h"

void drawOneLine(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2)
{
    glBegin(GL_LINES);
    glVertex2f((x1), (y1));
    glVertex2f((x2), (y2));
    glEnd();
}

void drawLineWithArray()
{
    GLint vertices[] = { -1,-1,1,1 };
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(2, GL_INT, 0, vertices);
    glBegin(GL_LINES);  //每兩個Element為一組
    glArrayElement(0);
    glArrayElement(1);
    glEnd();

}

void drawTwoLineWithArray()
{
    //每2點為一組
    GLint vertices[] =
    {
        -1,-1,
        1,1,
        -1,1,
        1,-1
    };
    //每3點為一組
    GLfloat colors[] =
    {
        1.0, 0.0, 0.0,  //紅
        0.0, 1.0, 0.0,  //綠
        0.0, 0.0, 1.0,  //藍
        1.0, 1.0, 0.0   //黃
    };
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_COLOR_ARRAY);
    glVertexPointer(2, GL_INT, 0, vertices);    //從 vertices 陣列找起, 每2點為一組
    glColorPointer(3, GL_FLOAT, 0, colors);     //從 colors 陣列找起, 每3點為一組
    glBegin(GL_LINES);  //每兩個Element為一組
    glArrayElement(0);
    glArrayElement(1);
    glArrayElement(2);
    glArrayElement(3);
    glEnd();
}

void drawTwoLineWithArray2()
{
    //每2點為一組
    GLfloat vertices[] =
    {
        -0.8f,-0.8f,
        0.8f,-0.8f,
        0.8f,0.8f,
        -0.8f,0.8f
    };
    //每3點為一組
    GLfloat colors[] =
    {
        1.0, 0.0, 0.0,  //紅
        0.0, 1.0, 0.0,  //綠
        0.0, 0.0, 1.0,  //藍
        1.0, 1.0, 0.0   //黃
    };

    GLubyte index[] = { 0,1,1,2,2,3,3,0 };

    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_COLOR_ARRAY);
    glVertexPointer(2, GL_FLOAT, 0, vertices);    //從 vertices 陣列找起, 每2點為一組
    glColorPointer(3, GL_FLOAT, 0, colors);     //從 colors 陣列找起, 每3點為一組

    glDrawElements(GL_LINES, 8, GL_UNSIGNED_BYTE, index);   //從 index 陣列 裡面找出 8 個索引數
    //用 GL_LINES 就是每2個組成一條直線 => 共4條線

}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    float x1 = -0.3f;
    float y1 = -0.3f;
    float x2 = 0.6f;
    float y2 = 0.2f;

    drawOneLine(x1, y1, x2, y2);

    //drawLineWithArray();

    //drawTwoLineWithArray();
    drawTwoLineWithArray2();

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
    const char* windowName = "OpenGL測試";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    printf("\n空白範例\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

