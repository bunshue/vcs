#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_m, 0.95f); //畫視窗邊界
    draw_boundary(color_y, 0.9f); //畫視窗邊界

    //使用 GL_QUAD_STRIP
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    glBegin(GL_QUAD_STRIP);
    glVertex3f(0.1f, 0.0f, 0.0f);   //v1
    glVertex3f(0.1f, 0.8f, 0.0f);   //v2
    glVertex3f(0.4f, 0.0f, 0.0f);   //v3
    glVertex3f(0.4f, 0.8f, 0.0f);   //v4
    glVertex3f(0.7f, 0.0f, 0.0f);   //v5
    glVertex3f(0.7f, 0.8f, 0.0f);   //v6
    glEnd();

    // 设置线的宽度 

    glLineWidth(5.0f);

    glBegin(GL_QUAD_STRIP);		// 绘制四边形

    glColor4ub(255, 0, 0, 255);	//R
    glVertex3f(-0.6f, -0.8f, 0.0f);

    glColor4ub(0, 255, 0, 255);	//G
    glVertex3f(-0.3f, -0.8f, 0.0f);

    glColor4ub(0, 0, 255, 255);	//B
    glVertex3f(0.0f, 0.0f, 0.0f);

    glColor4ub(255, 255, 0, 255);	//Y
    glVertex3f(-0.3f, 0.8f, 0.0f);

    glColor4ub(255, 0, 255, 255);	//M
    glVertex3f(-0.6f, 0.8f, 0.0f);

    glColor4ub(0, 255, 255, 255);	//C
    glVertex3f(-0.8f, 0.0f, 0.0f);

    glEnd();


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

