// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <GL/glut.h>  //32位元用的

#include <iostream>

int display_mode = 1;

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
        glVertex2d(xmin, j);
        glVertex2d(xmax, j);
        glEnd();
    }
    for (i = xmin; i <= xmax; i++) //豎線
    {
        glBegin(GL_LINES);
        glVertex2d(i, ymin);
        glVertex2d(i, ymax);
        glEnd();
    }
}

//display_mode = 8  //畫茶壺

void init8()
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_PROJECTION);
    glOrtho(-5, 5, -5, 5, 5, 15);
    glMatrixMode(GL_MODELVIEW);
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0);
}

//display_mode = 9  //畫矩形

void init9(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);/* select clearing color   */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0);/* initialize viewing values   */
}

//display_mode = 10  //畫矩形

void init10(void)
{
    glOrtho(0.0f, 300.0f, 0.0f, 300.0f, 1.0, -1.0);//設置窗口坐標系大小
    glClearColor(0.4f, 1.f, 0.8f, 1.0f);//設置背景色
}

void drawText1(void)
{
    using std::string;
    using std::stringstream;

    glPushMatrix();
    glLoadIdentity();
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
    glColor3f(0.0, 0.0, 0.0);
    glPrint(x - 1, y - 1, s, font);

    glColor3fv((GLfloat*)color);
    glPrint(x, y, s, font);
}

void drawText2(void)
{
    glPrint(-1.2, 0, "111Write Something to Screen", GLUT_BITMAP_TIMES_ROMAN_24);

    float* color = new float[4];
    color[0] = 0.0f;
    color[1] = 1.0f;
    color[2] = 0.0f;
    color[3] = 1.0f;

    glPrintShadowed(-1.2, -1.2, "222Write Something to Screen", GLUT_BITMAP_TIMES_ROMAN_24, color);
}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        //or
        glClearColor(1.0f, 1.0f, 1.0f, 1.0f);   // 設置清除窗口背景色為白色
        glClear(GL_COLOR_BUFFER_BIT);// 進行窗口清理
        glFlush();       // 刷新OpenGL中的命令列和，使所有尚未被行的命令行

        //設定預設大小...
    }
    else if (display_mode == 1)
    {
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        //glClearColor(0.1f, 0.2f, 1.f, 1.f); //清除背景 設定顏色

        //glClearColor(1.0, 0.0, 0.0, 1.0);   //清除背景 設定顏色

        glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
        glRectf(-0.9f, -0.9f, -0.3f, 0.9f);//畫一個矩形

        glColor4f(0.0, 1.0, 0.0, 1.0);  //設置畫筆顏色為 G
        glRectf(-0.4f, -0.8f, 0.4f, 0.8f);//畫一個矩形

        glColor4f(0.0, 0.0, 1.0, 1.0);  //設置畫筆顏色為 B
        glRectf(0.3f, -0.7f, 0.7f, 0.7f);//畫一個矩形

        //drawText1();

        drawText2();

        glFlush();//保證前面的OpenGL命令立即執行   glFlush​​負責刷新繪制緩沖器，保證繪圖命令立即執行。
    }
    else if (display_mode == 2)
    {
        glClearColor(0.5f, 0.5f, 0.5f, 0.0f);
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        //設置顏色
        glColor3f(0.2f, 0.6f, 0.5f);

        //開始渲染
        glBegin(GL_POLYGON);

        //圓的頂點數：數越大越趨近于圓
        const int n = 55;
        const GLfloat R = 0.5f;
        const GLfloat pi = 3.1415926f;

        for (int i = 0; i < n; i++)
        {
            glVertex2f(R * cos(2 * pi / n * i), R * sin(2 * pi / n * i));
        }
        //結束渲染
        glEnd();

        //強制刷新緩存區
        glFlush();
    }
    else if (display_mode == 3)
    {
        int i, n = 6;

        glClearColor(0.0, 0.0, 0.0, 0.0);
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluOrtho2D(0.0, NGRID, 0.0, NGRID); //窗口坐標范圍

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        //畫網格
        glColor3f(0.0f, 1.0f, 0.0f); //綠色
        drawGrid(0, NGRID, 0, NGRID);

        //畫控制點
        glColor3f(1.0f, 0.0f, 0.0f); //紅色
        glPointSize(10.0f); //點大小
        for (i = 0; i <= n; i++)
        {
            glBegin(GL_POINTS);
            glVertex2d(pnts[i][0], pnts[i][1]);
            glEnd();
        }

        //畫折線
        glColor3f(1.0f, 1.0f, 1.0f); //白色
        for (i = 0; i < n; i++)
        {
            glBegin(GL_LINES);
            glVertex2d(pnts[i][0], pnts[i][1]);
            glVertex2d(pnts[i + 1][0], pnts[i + 1][1]);
            glEnd();
        }

        glFlush();

    }
    else if (display_mode == 4)
    {
        //畫顏色色塊
        float mat[16];
        int i;

        glEnable(GL_DEPTH_TEST);
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
        glClearDepth(1.0);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);
        glGetFloatv(GL_PROJECTION_MATRIX, mat);
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

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        glColor3f(1.0f, 0.0f, 0.0f); //在右上角畫紅色平面：應該在后面
        glBegin(GL_POLYGON);
        glVertex3f(0.0f, 0.0f, -1.0f + 0.001f);
        glVertex3f(1.0f, 0.0f, -1.0f + 0.001f);
        glVertex3f(1.0f, 1.0f, -1.0f + 0.001f);
        glVertex3f(0.0f, 1.0f, -1.0f + 0.001f);
        glEnd();
        glColor3f(0.0f, 1.0f, 0.0f); //在左下角畫綠色的平面：應該在前面
        glBegin(GL_POLYGON);
        glVertex3f(-1.0f, -1.0f, 1.0f - 0.001f);
        glVertex3f(0.0f + 0.5f, -1.0f, 1.0f - 0.001f);
        glVertex3f(0.0f + 0.5f, 0.0f + 0.5f, 1.0f - 0.001f);
        glVertex3f(-1.0f, 0.0f + 0.5f, 1.0f - 0.001f);
        glEnd();
        glFlush();
    }
    else if (display_mode == 5)
    {
        //畫網格
        int i;

        glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluOrtho2D(-1.0, 11.0, -1.0, 11.0); //窗口坐標范圍

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        //畫10*10網格
        glColor3f(0.0f, 1.0f, 0.0f); //綠色
        for (i = 0; i <= 10; i++) //11條水平線
        {
            glBegin(GL_LINES);
            glVertex2d(0.0, i * 1.0);
            glVertex2d(10.0, i * 1.0);
            glEnd();
        }
        glBegin(GL_LINES); //11條豎線
        for (i = 0; i <= 10; i++)
        {
            glVertex2d(i * 1.0, 0.0);
            glVertex2d(i * 1.0, 10.0);
        }
        glEnd();

        //在對角線畫點
        glColor3f(1.0f, 1.0f, 1.0f); //白色
        glPointSize(10.0f); //點大小
        glBegin(GL_POINTS);
        for (i = 0; i <= 10; i++)
        {
            glVertex2d(i * 1.0, i * 1.0);
        }
        glEnd();
        for (i = 0; i <= 10; i++)
        {
            glBegin(GL_POINTS);
            glVertex2d(i * 1.0, 10.0 - i * 1.0);
            glEnd();
        }
        glFlush();
    }
    else if (display_mode == 6)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // Set background color to black and opaque
        glClear(GL_COLOR_BUFFER_BIT);         // Clear the color buffer (background)

        // Draw a Red 1x1 Square centered at origin
        glBegin(GL_QUADS);              // Each set of 4 vertices form a quad
        glColor3f(1.0f, 0.0f, 0.0f); // Red
        glVertex2f(-0.5f, -0.5f);    // x, y
        glVertex2f(0.5f, -0.5f);
        glVertex2f(0.5f, 0.5f);
        glVertex2f(-0.5f, 0.5f);
        glEnd();

        glFlush();  // Render now
    }
    else if (display_mode == 7)
    {
        glPushMatrix();
        glBegin(GL_TRIANGLES);          // 開始劃三角形
        glColor3f(1.0f, 0.0f, 0.0f);         // 設定輸出色為紅色
        glVertex2f(0.0f, 1.0f);           //(x1,y1)=(0, 1)
        glColor3f(0.0f, 1.0f, 0.0f);         // 設定輸出色為綠色
        glVertex2f(0.87f, -0.5f);            //(x2,y2)=(0.87,-0.5)
        glColor3f(0.0f, 0.0f, 1.0f);         // 設定輸出色為藍色
        glVertex2f(-0.87f, -0.5f);           //(x3,y3)=(-0.87,-0.5)
        glEnd();                               // 結束劃三角形
        glPopMatrix();
        glutSwapBuffers();
    }
    else if (display_mode == 8)
    {
        //畫茶壺
        glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

        glClear(GL_COLOR_BUFFER_BIT);
        glColor3f(1.0, 0, 0);
        glutWireTeapot(3);
        glFlush();
    }
    else if (display_mode == 9)
    {
        //display_mode = 9  //畫矩形
        glClear(GL_COLOR_BUFFER_BIT);/* clear all pixels   */
        glColor3f(1.0, 1.0, 1.0);
        glBegin(GL_POLYGON);/* draw white polygon with corners at(0.25, 0.25, 0.0) and (0.75, 0.75, 0.0)*/
        glVertex3f(0.25, 0.25, 0.0);
        glVertex3f(0.75, 0.25, 0.0);
        glVertex3f(0.75, 0.75, 0.0);
        glVertex3f(0.25, 0.75, 0.0);
        glEnd();
        glFlush();/* start processing buffered OpenGL routines   */
    }
    else if (display_mode == 10)
    {
        //display_mode = 10  //畫
        glClear(GL_COLOR_BUFFER_BIT);//清空顏色緩沖池
        glColor3f(1.0f, 1.0f, 0.0f);//設置繪圖顏色
        glRectf(100.0f, 100.0f, 200.0f, 200.0f);//繪制矩形
        glFlush();//刷新緩沖
    }
    else if (display_mode == 11)
    {
        //display_mode = 11  //畫 彩色三角形

        glPushMatrix();
        glBegin(GL_TRIANGLES);          // 開始劃三角形
        glColor3f(1.0f, 0.0f, 0.0f);         // 設定輸出色為紅色
        glVertex2f(0.0f, 1.0f);           //(x1,y1)=(0, 1)
        glColor3f(0.0f, 1.0f, 0.0f);         // 設定輸出色為綠色
        glVertex2f(0.87f, -0.5f);            //(x2,y2)=(0.87,-0.5)
        glColor3f(0.0f, 0.0f, 1.0f);         // 設定輸出色為藍色
        glVertex2f(-0.87f, -0.5f);           //(x3,y3)=(-0.87,-0.5)
        glEnd();                               // 結束劃三角形
        glPopMatrix();
        glutSwapBuffers();
    }
    else if (display_mode == 12)
    {
        //display_mode = 12  //畫矩形
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_MODELVIEW);                        // 選擇模型觀察矩陣
        glLoadIdentity();                                  // 重置模型觀察矩陣   
        glMatrixMode(GL_PROJECTION);                        // 選擇投影矩陣     
        glLoadIdentity();

        glEnable(GL_TEXTURE_2D);    //啟用2D紋理映射
        glBegin(GL_QUADS);
        glTexCoord2f(0.0f, 0.0f);
        glVertex3f(-0.5f, -0.5f, 0.0f);
        glTexCoord2f(1.0f, 0.0f);
        glVertex3f(0.5f, -0.5f, 0.0f);
        glTexCoord2f(1.0f, 1.0f);
        glVertex3f(0.5f, 0.5f, 0.0f);
        glTexCoord2f(0.0f, 1.0f);
        glVertex3f(-0.5f, 0.5f, 0.0f);
        glEnd();
        glDisable(GL_TEXTURE_2D);

        glutSwapBuffers();
    }
    else if (display_mode == 13)
    {
        //display_mode = 13  //畫 舉形 + 四邊形

        //Single/Double buffer 會不一樣
        //glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
        //glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

        glClear(GL_COLOR_BUFFER_BIT);

        glRectf(-0.5f, -0.5f, 0.5f, 0.5f);

        glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
        glBegin(GL_QUADS);
        {
            glTexCoord2f(0.8f, 0.0f);
            glVertex2f(0.8f, 0.0f);

            glTexCoord2f(0.0f, -0.8f);
            glVertex2f(0.0f, -0.8f);

            glTexCoord2f(-0.8f, 0.0f);
            glVertex2f(-0.8f, 0.0f);

            glTexCoord2f(0.0f, 0.8f);
            glVertex2f(0.0f, 0.8f);
        }
        glEnd();

        glFlush();
    }
    else if (display_mode == 14)
    {
        //display_mode = 14  //畫



    }
    else if (display_mode == 15)
    {
        //display_mode = 15  //畫



    }
    else if (display_mode == 16)
    {
        //display_mode = 16  //畫



    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

static void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
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
        init8();
        break;
    case '9':
        display_mode = 9;
        init9();
        break;
    case 'a':
        display_mode = 10;
        init10();
        break;
    case 'b':
        display_mode = 11;
        break;
    case 'c':
        display_mode = 12;
        break;
    case 'd':
        display_mode = 13;
        break;
    case 'e':
        display_mode = 14;
        break;
    case 'f':
        display_mode = 15;
        break;
    case 27:
        exit(0);
    }

    glutPostRedisplay();
}

void mainMenu(int i) { keyboard(i, 0, 0); }

void initMenus()
{
    glutCreateMenu(mainMenu);
    glutAddMenuEntry("Nearest      [1]", '1');
    glutAddMenuEntry("Bilinear     [2]", '2');
    glutAddMenuEntry("Bicubic      [3]", '3');
    glutAddMenuEntry("Fast Bicubic [4]", '4');
    glutAddMenuEntry("Catmull-Rom  [5]", '5');
    glutAddMenuEntry("Zoom in      [=]", '=');
    glutAddMenuEntry("Zoom out     [-]", '-');
    glutAddMenuEntry("Benchmark    [b]", 'b');
    glutAddMenuEntry("DrawCurves   [c]", 'c');
    glutAddMenuEntry("Quit       [esc]", 27);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}

// 初始化參數
void init(void)
{
    //好像做不做沒甚麼差別
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glClearColor(0.0, 0.0, 0.0, 0.0);

    //glClearColor(0.1, 0.1, 0.4, 0.0);
    //glShadeModel(GL_SMOOTH);

    //glClearColor(0.1, 0.1, 0.4, 0.0);
    //glShadeModel(GL_SMOOTH);
}

int main(int argc, char* argv[])
{
    //初始化GLUT庫，這個函數只是傳說命令參數并且初始化glut庫
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("簡單2D OpenGL畫圖 0 ~ 9");    // 設定視窗標題

    init();

    glutDisplayFunc(display);       //設定callback function, 註冊顯示函數 // Register display callback handler for window re-paint
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    //glutSpecialFunc(SpecialKey);    //設定callback function

    initMenus();        //設定表單按鈕

    printf("取得視窗寬度 : %d\n", glutGet(GLUT_WINDOW_WIDTH));
    printf("取得視窗高度 : %d\n", glutGet(GLUT_WINDOW_HEIGHT));

    glutMainLoop();     // Enter the event-processing loop



    return 0;
}


