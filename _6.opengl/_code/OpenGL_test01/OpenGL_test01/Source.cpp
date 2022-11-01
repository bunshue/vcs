#include <helper_gl.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include <iostream>

int display_mode = 1;

int full_screen = 0;

#define NGRID 6

double pnts[][2] = {
    0, 6,
    1, 0,
    2, 6,
    3, 0,
    4, 6,
    5, 0,
    6, 6
};

void drawGrid(int xmin, int xmax, int ymin, int ymax)
{
    int i, j;
    for (j = ymin; j <= ymax; j++) //水平線
    {
        glBegin(GL_LINES);
        {
            glVertex2d(xmin, j);
            glVertex2d(xmax, j);
        }
        glEnd();
    }
    for (i = xmin; i <= xmax; i++) //豎線
    {
        glBegin(GL_LINES);
        {
            glVertex2d(i, ymin);
            glVertex2d(i, ymax);
        }
        glEnd();
    }
}

// 初始化參數
void init01(void)
{
    //好像做不做沒甚麼差別
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glClearColor(0.0, 0.0, 0.0, 0.0);   //設置背景色

    //glClearColor(0.1, 0.1, 0.4, 0.0); //設置背景色
    //glShadeModel(GL_SMOOTH);

    //glClearColor(0.1, 0.1, 0.4, 0.0); //設置背景色
    //glShadeModel(GL_SMOOTH);
}

//display_mode = 8  //畫茶壺
void init08()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);   //設置背景色
    glMatrixMode(GL_PROJECTION);
    glOrtho(-5, 5, -5, 5, 5, 15);   //設置窗口座標系大小
    glMatrixMode(GL_MODELVIEW);
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0);
}

//display_mode = 9  //畫矩形

void init09(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);   //設置背景色
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0); //設置窗口座標系大小
}

void drawString1(void)
{
    using std::string;
    using std::stringstream;

    glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
    glLoadIdentity();	//設置單位矩陣
    glRasterPos2f(-0.8f, 0.6f);

    string infoString;
    stringstream ss;
    ss << "Write Something to Screen";
    infoString.append(ss.str());

    for (unsigned int i = 0; i < infoString.size(); i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, infoString[i]);
    }
    glPopMatrix();
}

inline void glPrint(int x, int y, const char* s, void* font)
{
    glRasterPos2f((GLfloat)x, (GLfloat)y);
    int len = (int)strlen(s);

    for (int i = 0; i < len; i++)
    {
        glutBitmapCharacter(font, s[i]);
    }
}

inline void glPrintShadowed(int x, int y, const char* s, void* font, float* color)
{
    glColor3f(0.0, 0.0, 0.0);   //設定顏色 Black
    glPrint(x - 1, y - 1, s, font);

    glColor3fv((GLfloat*)color);    //設定顏色
    glPrint(x, y, s, font);
}

void drawString2(void)
{
    glPrint(-1.2, 0, "111Write Something to Screen", GLUT_BITMAP_TIMES_ROMAN_24);

    float* color = new float[4];
    color[0] = 0.0f;
    color[1] = 1.0f;
    color[2] = 0.0f;
    color[3] = 1.0f;

    glPrintShadowed(-1.2, -1.2, "222Write Something to Screen", GLUT_BITMAP_TIMES_ROMAN_24, color);
}

void draw_boundary(float* color, float dd)
{
    //用 GL_LINE_LOOP 畫一個空心矩形
    glColor3fv((GLfloat*)color);    //設定顏色
    float point1[3] = { -dd, -dd, 0 };	//左下
    float point2[3] = { dd, -dd, 0 };	//右下
    float point3[3] = { dd,  dd, 0 };	//右上
    float point4[3] = { -dd,  dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();
}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        //or
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);   // 設置清除窗口背景色為白色
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        //設定預設大小...  TBD
    }
    else if (display_mode == 1)
    {
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        //glClearColor(0.1f, 0.2f, 1.f, 1.f); //清除背景 設定顏色

        //glClearColor(1.0, 0.0, 0.0, 1.0);   //清除背景 設定顏色

        //畫一個矩形 R
        glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
        //左下x,左下y,右上x,右上y,
        glRectf(-0.9f, -0.9f, -0.3f, 0.9f);//畫一個矩形

        ////畫一個矩形 G
        glColor4f(0.0, 1.0, 0.0, 1.0);  //設置畫筆顏色為 G
        //左下x,左下y,右上x,右上y,
        glRectf(-0.4f, -0.8f, 0.4f, 0.8f);//畫一個矩形

        //畫一個矩形 B
        glColor4f(0.0, 0.0, 1.0, 1.0);  //設置畫筆顏色為 B
        //左下x,左下y,右上x,右上y,
        glRectf(0.3f, -0.7f, 0.7f, 0.7f);//畫一個矩形

        //drawString1();
        drawString2();

        //畫視窗邊界
        float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
        draw_boundary(color_yellow, 0.9);
    }
    else if (display_mode == 2)
    {
        glClearColor(0.5f, 0.5f, 0.5f, 0.0f);   //設定背景 與 透明度
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glColor3f(0.2f, 0.6f, 0.5f);    //設定顏色

        //開始渲染
        glBegin(GL_POLYGON);
        {
            //多邊形的頂點數：數越大越趨近于圓
            const int n = 10;
            const GLfloat R = 0.5f;
            const GLfloat pi = 3.1415926f;
            for (int i = 0; i < n; i++)
            {
                glVertex2f(R * cos(2 * pi / n * i), R * sin(2 * pi / n * i));
            }
        }
        //結束渲染
        glEnd();

        //畫矩形
        glBegin(GL_QUADS);              //矩形
        {
            glColor3f(1.0f, 0.0f, 0.0f); //設定顏色, R
            glVertex2f(-0.2f, -0.2f);    // x, y
            glVertex2f(0.2f, -0.2f);
            glVertex2f(0.2f, 0.2f);
            glVertex2f(-0.2f, 0.2f);
        }
        glEnd();

        //畫視窗邊界
        float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
        draw_boundary(color_yellow, 0.9);

    }
    else if (display_mode == 3)
    {
        int i;
        int n = 6;

        glClearColor(0.0, 0.0, 0.0, 0.0);   //設置背景色
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(0.0, NGRID, 0.0, NGRID); //窗口座標範圍, 2D

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();	//設置單位矩陣

        //畫網格
        glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G
        drawGrid(0, NGRID, 0, NGRID);

        //畫控制點
        glColor3f(1.0f, 0.0f, 0.0f);    //設定顏色 R
        glPointSize(20.0f); 	//設定點的大小, N X N
        for (i = 0; i <= n; i++)
        {
            glBegin(GL_POINTS);
            {
                glVertex2d(pnts[i][0], pnts[i][1]);
            }
            glEnd();
        }

        //畫折線
        glColor3f(1.0f, 1.0f, 1.0f);    //設定顏色 White
        for (i = 0; i < n; i++)
        {
            glBegin(GL_LINES);
            {
                glVertex2d(pnts[i][0], pnts[i][1]);
                glVertex2d(pnts[i + 1][0], pnts[i + 1][1]);
            }
            glEnd();
        }

        //畫視窗邊界
        float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
        draw_boundary(color_yellow, 5.5);
    }
    else if (display_mode == 4)
    {
        //畫顏色色塊
        float mat[16];
        int i;

        glEnable(GL_DEPTH_TEST);
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色
        glClearDepth(1.0);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);   //設置窗口座標系大小
        glGetFloatv(GL_PROJECTION_MATRIX, mat);
        /*
        for (i = 0; i < 16; i++)
        {
            printf("%10.7f", mat[i]);
            if ((i + 1) % 4)
            {
                printf(" ");
            }
            else
            {
                printf("\n");
            }
        }
        */
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();	//設置單位矩陣

        glColor3f(1.0f, 0.0f, 0.0f);    //設定顏色 R //在右上角畫紅色平面：應該在後面
        glBegin(GL_POLYGON);
        {
            glVertex3f(0.0f, 0.0f, -1.0f + 0.001f);
            glVertex3f(1.0f, 0.0f, -1.0f + 0.001f);
            glVertex3f(1.0f, 1.0f, -1.0f + 0.001f);
            glVertex3f(0.0f, 1.0f, -1.0f + 0.001f);
        }
        glEnd();

        glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G //在左下角畫綠色的平面：應該在前面
        glBegin(GL_POLYGON);
        {
            glVertex3f(-1.0f, -1.0f, 1.0f - 0.001f);
            glVertex3f(0.0f + 0.5f, -1.0f, 1.0f - 0.001f);
            glVertex3f(0.0f + 0.5f, 0.0f + 0.5f, 1.0f - 0.001f);
            glVertex3f(-1.0f, 0.0f + 0.5f, 1.0f - 0.001f);
        }
        glEnd();
    }
    else if (display_mode == 5)
    {
        //畫網格
        int i;

        glClearColor(0.0f, 0.0f, 0.0f, 0.0f);   //設置背景色
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1.0, 11.0, -1.0, 11.0); //窗口座標範圍, 2D

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();	//設置單位矩陣

        //畫10*10網格
        glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G
        for (i = 0; i <= 10; i++) //11條水平線
        {
            glBegin(GL_LINES);
            {
                glVertex2d(0.0, i * 1.0);
                glVertex2d(10.0, i * 1.0);
            }
            glEnd();
        }

        glBegin(GL_LINES); //11條豎線
        {
            for (i = 0; i <= 10; i++)
            {
                glVertex2d(i * 1.0, 0.0);
                glVertex2d(i * 1.0, 10.0);
            }
        }
        glEnd();

        //在對角線畫點
        glColor3f(1.0f, 1.0f, 1.0f);    //設定顏色 White
        glPointSize(10.0f); 	//設定點的大小, N X N
        glBegin(GL_POINTS);
        {
            for (i = 0; i <= 10; i++)
            {
                glVertex2d(i * 1.0, i * 1.0);
            }
        }
        glEnd();
        for (i = 0; i <= 10; i++)
        {
            glBegin(GL_POINTS);
            {
                glVertex2d(i * 1.0, 10.0 - i * 1.0);
            }
            glEnd();
        }
    }
    else if (display_mode == 6)
    {
    }
    else if (display_mode == 7)
    {
        //display_mode = 7  //畫 彩色三角形
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
        glBegin(GL_TRIANGLES);          // 開始畫三角形
        {
            glColor3f(1.0f, 0.0f, 0.0f);    //設定顏色 R
            glVertex2f(0.0f, 1.0f);         //(x1,y1)=(0, 1)
            glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G
            glVertex2f(0.87f, -0.5f);       //(x2,y2)=(0.87,-0.5)
            glColor3f(0.0f, 0.0f, 1.0f);    //設定顏色 B
            glVertex2f(-0.87f, -0.5f);      //(x3,y3)=(-0.87,-0.5)
        }
        glEnd();    // 結束畫三角形
        glPopMatrix();
    }
    else if (display_mode == 8)
    {
        //畫茶壺
        glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glColor3f(1.0, 0, 0);   //設定顏色 R

        glutWireTeapot(3);  //線框茶壺
        //glutSolidTeapot(3);  //實心茶壺
    }
    else if (display_mode == 9)
    {
        //display_mode = 9  //畫矩形
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glColor3f(1.0, 1.0, 1.0);   //設定顏色 White
        glBegin(GL_POLYGON);/* draw white polygon with corners at(0.25, 0.25, 0.0) and (0.75, 0.75, 0.0)*/
        {
            glVertex3f(0.25, 0.25, 0.0);
            glVertex3f(0.75, 0.25, 0.0);
            glVertex3f(0.75, 0.75, 0.0);
            glVertex3f(0.25, 0.75, 0.0);
        }
        glEnd();
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

    glFlush();  //強制刷新緩存區
    glutSwapBuffers();  // 將後緩沖區繪製到前臺
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;
        break;
    case ' ':
        if (full_screen == 0)
        {
            full_screen = 1;
            printf("全螢幕\n");
            glutFullScreen();
        }
        else
        {
            //恢復成一般螢幕, 有問題

            full_screen = 0;
            printf("一般螢幕\n");
            glutInitWindowSize(600, 600);       // 設定視窗大小
            glutInitWindowPosition(1100, 200);  // 設定視窗位置
        }
        break;
    case '0':
        display_mode = 0;
        break;
    case '1':
        display_mode = 1;
        init01();
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
        init08();
        break;
    case '9':
        display_mode = 9;
        init09();
        break;
    }

    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。

    /*
    char info[10];
    sprintf(info, "%d", (char)display_mode);
    glutSetWindowTitle(info);
    */
}

int main(int argc, char* argv[])
{
    //初始化GLUT庫，這個函數只是傳說命令參數并且初始化glut庫
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    /*
    設定圖形顯示模式。引數mode的可選值為：
    GLUT_RGBA：      當未指明GLUT - RGBA或GLUT - INDEX時，是預設使用的模式。表明欲建立RGBA模式的視窗。
    GLUT_RGB：       與GLUT - RGBA作用相同。
    GLUT_INDEX：     指明為顏色索引模式。
    GLUT_SINGLE：    只使用單快取
    GLUT_DOUBLE：    使用雙快取。以避免把計算機作圖的過程都表現出來，或者為了平滑地實現動畫。
    GLUT_DEPTH：     使用深度快取。
    GLUT_ACCUM：     讓視窗使用累加的快取。
    GLUT_ALPHA：     讓顏色緩衝區使用alpha元件。
    GLUT_STENCIL：   使用模板快取。
    GLUT_MULTISAMPLE：讓視窗支援多例程。
    GLUT_STEREO：    使視窗支援立體。
    GLUT_LUMINACE:  luminance是亮度的意思。但是很遺憾，在多數OpenGL平臺上，不被支援。
    */

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("簡單2D OpenGL畫圖 0 ~ 9");    // 設定視窗標題

    //int res = glutGetWindow();
    //printf("當前視窗的標記符 = %d\n", res);
    //printf("取得視窗寬度 : %d\n", glutGet(GLUT_WINDOW_WIDTH));
    //printf("取得視窗高度 : %d\n", glutGet(GLUT_WINDOW_HEIGHT));

    init01();

    glutSetCursor(GLUT_CURSOR_DESTROY); //改變視窗上的鼠標標記

    glutDisplayFunc(display);       //設定callback function, 註冊顯示函數 // Register display callback handler for window re-paint
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    //glutWireTeapot(200);
    //glutWireTeapot(3);

    //設置一組浮點數來表示紅色
    GLfloat vRed[] = { 1.0,1.00,0.0,0.5f };

    glutMainLoop();	//開始主循環繪製     // Enter the event-processing loop

    return 0;
}

