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

//display_mode = 3
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
    for (j = ymin; j <= ymax; j++) //水平线
    {
        glBegin(GL_LINES);
        glVertex2d(xmin, j);
        glVertex2d(xmax, j);
        glEnd();
    }
    for (i = xmin; i <= xmax; i++) //竖线
    {
        glBegin(GL_LINES);
        glVertex2d(i, ymin);
        glVertex2d(i, ymax);
        glEnd();
    }
}

//display_mode = 6

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

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


        glFlush();//保證前面的OpenGL命令立即執行   glFlush​​負責刷新繪制緩沖器，保證繪圖命令立即執行。
    }
    else if (display_mode == 2)
    {
        glClearColor(0.5f, 0.5f, 0.5f, 0.0f);
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        //设置颜色
        glColor3f(0.2f, 0.6f, 0.5f);

        //开始渲染
        glBegin(GL_POLYGON);

        //圆的顶点数：数越大越趋近于圆
        const int n = 55;
        const GLfloat R = 0.5f;
        const GLfloat pi = 3.1415926f;

        for (int i = 0; i < n; i++) {
            glVertex2f(R * cos(2 * pi / n * i), R * sin(2 * pi / n * i));
        }
        //结束渲染
        glEnd();

        //强制刷新缓存区
        glFlush();
    }
    else if (display_mode == 3)
    {
        int i, n = 6;

        glClearColor(0.0, 0.0, 0.0, 0.0);
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        gluOrtho2D(0.0, NGRID, 0.0, NGRID); //窗口坐标范围

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        //画网格
        glColor3f(0.0f, 1.0f, 0.0f); //绿色
        drawGrid(0, NGRID, 0, NGRID);

        //画控制点
        glColor3f(1.0f, 0.0f, 0.0f); //红色
        glPointSize(10.0f); //点大小
        for (i = 0; i <= n; i++)
        {
            glBegin(GL_POINTS);
            glVertex2d(pnts[i][0], pnts[i][1]);
            glEnd();
        }

        //画折线
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
            if ((i + 1) % 4) printf(" ");
            else printf("\n");
        }

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        glColor3f(1.0f, 0.0f, 0.0f); //在右上角画红色平面：应该在后面
        glBegin(GL_POLYGON);
        glVertex3f(0.0f, 0.0f, -1.0f + 0.001f);
        glVertex3f(1.0f, 0.0f, -1.0f + 0.001f);
        glVertex3f(1.0f, 1.0f, -1.0f + 0.001f);
        glVertex3f(0.0f, 1.0f, -1.0f + 0.001f);
        glEnd();
        glColor3f(0.0f, 1.0f, 0.0f); //在左下角画绿色的平面：应该在前面
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
        gluOrtho2D(-1.0, 11.0, -1.0, 11.0); //窗口坐标范围

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();

        //画10*10网格
        glColor3f(0.0f, 1.0f, 0.0f); //绿色
        for (i = 0; i <= 10; i++) //11条水平线
        {
            glBegin(GL_LINES);
            glVertex2d(0.0, i * 1.0);
            glVertex2d(10.0, i * 1.0);
            glEnd();
        }
        glBegin(GL_LINES); //11条竖线
        for (i = 0; i <= 10; i++)
        {
            glVertex2d(i * 1.0, 0.0);
            glVertex2d(i * 1.0, 10.0);
        }
        glEnd();

        //在对角线画点
        glColor3f(1.0f, 1.0f, 1.0f); //白色
        glPointSize(10.0f); //点大小
        glBegin(GL_POINTS);
        for (i = 0; i <= 10; i++)
            glVertex2d(i * 1.0, i * 1.0);
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
    }
    else if (display_mode == 9)
    {
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
        break;
    case '9':
        display_mode = 9;
        break;
    case 27:
        exit(0);
    }

    glutPostRedisplay();
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
    //初始化GLUT库，这个函数只是传说命令参数并且初始化glut库
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("簡單2D OpenGL畫圖 0 ~ 9");    // 設定視窗標題

    init();

    glutDisplayFunc(display);       //設定callback function, 註冊顯示函數 // Register display callback handler for window re-paint
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    //glutSpecialFunc(SpecialKey);    //設定callback function

    glutMainLoop();     // Enter the event-processing loop

    return 0;
}



