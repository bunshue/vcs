#include "../../Common.h"

int display_mode = 1;

void reset_default_setting()
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

    glLineWidth(1.0f);	//設定線寬

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

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

void draw_picture1()
{

}

void draw_picture2()
{
    draw_boundary(color_y, 0.9f); //畫視窗邊界

    float x_st = 0.0f;
    float y_st = 0.0f;
    float dd = 0.15f;

    //畫線
    //兩點為一直線
    glBegin(GL_LINES);
    glVertex2f(-0.9f, -dd);
    glVertex2f(0.9f, dd);
    glVertex2f(-0.9f, dd);
    glVertex2f(0.9f, -dd);
    glEnd();

    //畫線
    //畫直線連線
    glBegin(GL_LINE_STRIP);	//繪製前後連接的點組成的線
    glColor3f(1.0, 1.0, 0.0);
    for (x_st = -0.9f; x_st <= 1.0f; x_st += 0.1f)
    {
        if (y_st != 0.9f)
            y_st = 0.9f;
        else
            y_st = 0.6f;

        glVertex2f(x_st, y_st);
    }
    glEnd();

    //畫線
    //畫封閉曲線
    glBegin(GL_LINE_LOOP);
    glColor3f(1.0, 0.0, 1.0);
    for (x_st = -0.9f; x_st <= 1.0f; x_st += 0.1f)
    {
        if (y_st != 0.5f)
            y_st = 0.5f;
        else
            y_st = 0.2f;

        glVertex2f(x_st, y_st);
    }
    glVertex2f(0.8f, 0.6f);
    glEnd();

    //畫正弦波
    glBegin(GL_LINE_STRIP);	//繪製前後連接的點組成的線
    glColor3f(0.0, 1.0, 1.0);
    for (x_st = -0.9f; x_st <= 1.0f; x_st += 0.1f)
    {
        y_st = 0.2f * sin(x_st * 10) - 0.6f;
        glVertex2f(x_st, y_st);
    }
    glEnd();

    glFlush();  // 執行繪圖命令
}

void draw_picture3()
{
    draw_boundary(color_y, 0.9f); //畫視窗邊界
}

void draw_picture4()
{
    draw_boundary(color_y, 0.9f); //畫視窗邊界

    float x_st = 0.0f;
    float y_st = 0.0f;

    //畫多邊形
    float cx = 0.0f;
    float cy = 0.0f;
    float r = 0.5f;
    glBegin(GL_POLYGON);
    glColor3f(0.5f, 0.3f, 0.7f);
    for (int angle = 0; angle < 360; angle += 36)
    {
        x_st = cx + r * cosf(2 * PI * angle / 360);
        y_st = cy + r * sinf(2 * PI * angle / 360);
        glVertex2f(x_st, y_st);
    }
    glEnd();

    glFlush();  // 執行繪圖命令
}

void draw_picture5()
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

void draw_picture6()
{
    draw_boundary(color_y, 0.9f); //畫視窗邊界

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

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        printf("無畫面, TBD, display_mode = %d\n", display_mode);

        //設定預設大小...  TBD
    }
    else if (display_mode == 1)
    {
        reset_default_setting();

        draw_picture1();
    }
    else if (display_mode == 2)
    {
        reset_default_setting();

        draw_picture2();
    }
    else if (display_mode == 3)
    {
        reset_default_setting();
        draw_picture3();
    }
    else if (display_mode == 4)
    {
        reset_default_setting();
        draw_picture4();
    }
    else if (display_mode == 5)
    {
        reset_default_setting();
        draw_picture5();
    }
    else if (display_mode == 6)
    {
        reset_default_setting();
        draw_picture6();
    }
    else if (display_mode == 7)
    {
        reset_default_setting();
    }
    else if (display_mode == 8)
    {
        reset_default_setting();
    }
    else if (display_mode == 9)
    {
        reset_default_setting();
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

    glFlush();  //強制刷新緩存區
    glutSwapBuffers();  // 將後緩沖區繪製到前臺
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
        break;
    case '0':
        display_mode = 0;
        break;
    case '1':
        display_mode = 1;
        break;
    case '2':
        display_mode = 2;
        break;
    case '3':
        display_mode = 3;
        break;
    case '4':
        display_mode = 4;
        break;
    case '5':
        display_mode = 5;
        break;
    case '6':
        display_mode = 6;
        break;
    case '7':
        display_mode = 7;
        break;
    case '8':
        display_mode = 8;
        break;
    case '9':
        display_mode = 9;
        break;
    }
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

int main(int argc, char* argv[])
{
    const char* windowName = "繪製基本圖元 0 ~ 9";
    const char* message = "繪製基本圖元 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    glutSetCursor(GLUT_CURSOR_DESTROY); //改變視窗上的鼠標標記

    glutMainLoop();	//開始主循環繪製     // Enter the event-processing loop

    return 0;
}

