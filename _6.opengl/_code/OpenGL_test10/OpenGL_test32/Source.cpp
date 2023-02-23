#include "../../Common.h"

int hh = 0;
int mm = 0;
int ss = 0;

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //draw_boundary(color_y, 0.9f); //畫視窗邊界

    //float PI = 3.1415926f;
    float R = 0.5f;
    float TR = R - 0.05f;
    float h_Length = 0.0f;
    float m_Length = 0.0f;
    float s_Length = 0.0f;
    float s_Angle = 0.0f;
    float m_Angle = 0.0f;
    float h_Angle = 0.0f;

    glLineWidth(5.0f);
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < 100; i++)
    {
        glVertex2f(R * cos(2 * PI / 100 * i), R * sin(2 * PI / 100 * i));
    }
    glEnd();
    glLineWidth(2);
    for (int i = 0; i < 100; i++)
    {
        glBegin(GL_LINES);
        glVertex2f(TR * sin(2 * PI / 12 * i), TR * cos(2 * PI / 12 * i));
        glVertex2f(R * sin(2 * PI / 12 * i), R * cos(2 * PI / 12 * i));
        glEnd();
    }
    glLineWidth(1);
    h_Length = 0.2f;
    m_Length = 0.3f;
    s_Length = 0.4f;
    float count = 60.0;
    s_Angle = ss / count;
    count *= 60;
    m_Angle = (mm * 60 + ss) / count;
    count *= 12;
    h_Angle = (hh * 60 * 60 + mm * 60 + ss) / count;
    glLineWidth(1);
    glBegin(GL_LINES);
    glVertex2f(0.0, 0.0);
    glVertex2f(s_Length * sin(2 * PI * s_Angle), s_Length * cos(2 * PI * s_Angle));
    glEnd();
    glLineWidth(5);
    glBegin(GL_LINES);
    glVertex2f(0.0, 0.0);
    glVertex2f(h_Length * sin(2 * PI * h_Angle), h_Length * cos(2 * PI * h_Angle));
    glEnd();
    glLineWidth(3);
    glBegin(GL_LINES);
    glVertex2f(0.0, 0.0);
    glVertex2f(m_Length * sin(2 * PI * m_Angle), m_Length * cos(2 * PI * m_Angle));
    glEnd();
    glLineWidth(1);
    glBegin(GL_POLYGON);
    for (int i = 0; i < 100; i++)
    {
        glVertex2f(0.03 * cos(2 * PI / 100 * i), 0.03 * sin(2 * PI / 100 * i));
    }
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

void idle(void)
{
    ss++;
    if (ss >= 60)
    {
        ss = 0;
        mm++;
        if (mm >= 60)
        {
            mm = 0;
            hh++;
            if (hh >= 24)
            {
                hh = 0;
            }
        }
    }
    glutPostRedisplay();
    sleep(10);
}

int main(int argc, char** argv)
{
    const char* windowName = "時鐘範例";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 400, 400, 1100, 200, display, reshape, keyboard);

    glutIdleFunc(idle);			//設定callback function

    printf("\n時鐘範例\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
