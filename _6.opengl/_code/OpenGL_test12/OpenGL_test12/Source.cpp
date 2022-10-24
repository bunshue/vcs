#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

#define PI_F             3.141592654F

// 初始化參數
void init()
{
    glClearColor(0.0, 0.0, 0.0, 1.0);   //黑色背景
    glShadeModel(GL_SMOOTH);
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   // 清除之前幀數據

    float x_st = 0.0f;
    float y_st = 12.0f;
    float dd = 0;
    //畫點
    glBegin(GL_POINTS);
    for (x_st = -14.0; x_st < -5.0f; x_st += 0.5f)
    {
        glColor3f(1.0, 0.0, 0.0);	//紅
        glVertex2f(x_st, y_st);

        glColor3f(0.0, 1.0, 0.0);	//綠
        glVertex2f(x_st, y_st - 0.5f);

        glColor3f(1.0, 1.0, 0);	//黃
        glVertex2f(x_st, y_st - 1.0f);
    }
    glEnd();

    //畫直線連線
    //畫繞視窗周圍之直線連線 紅色
    float offset = 13.0;
    glBegin(GL_LINES);
    glColor3f(1.0, 0.0, 0.0);       //紅色
    glVertex2f(-offset, -offset);   //左下
    glVertex2f(-offset, offset);    //左上

    glVertex2f(-offset, offset);    //左上
    glVertex2f(offset, offset);     //右上

    glVertex2f(offset, offset);     //右上
    glVertex2f(offset, -offset);    //右下

    glVertex2f(offset, -offset);    //右下
    glVertex2f(-offset, -offset);   //左下

    glVertex2f(0, offset);      //中上
    glVertex2f(0, -offset);     //中下

    glVertex2f(-offset, 0);     //中左
    glVertex2f(offset, 0);      //中右
    glEnd();

    //畫線
    //畫直線連線
    glBegin(GL_LINE_STRIP);
    glColor3f(0.0, 1.0, 0.0);
    for (x_st = -14.0; x_st <= -5.0f; x_st += 0.5f)
    {
        if (y_st != 7.0f)
            y_st = 7.0f;
        else
            y_st = 10.0f;

        glVertex2f(x_st, y_st);
    }
    glEnd();

    //畫線
    //畫封閉曲線
    glBegin(GL_LINE_LOOP);
    glColor3f(0.0, 1.0, 0.0);
    for (x_st = -14.0; x_st <= -5.0f; x_st += 0.5f)
    {
        if (y_st != 4.0f)
            y_st = 4.0f;
        else
            y_st = 7.0f;

        glVertex2f(x_st, y_st);
    }
    glVertex2f(-5.0, 3.0);
    glEnd();

    //畫多邊形
    float cx = 0.0f;
    float cy = 9.0f;
    float r = 4.0f;
    glBegin(GL_POLYGON);
    glColor3f(0.5, 0.3, 0.7);
    for (int angle = 0; angle < 360; angle += 36)
    {
        x_st = cx + r * cosf(2 * PI_F * angle / 360);
        y_st = cy + r * sinf(2 * PI_F * angle / 360);
        glVertex2f(x_st, y_st);
    }
    glEnd();

    //畫四邊形, 4個頂點為一組
    glBegin(GL_QUADS);
    glColor3f(0.7, 0.5, 0.2);
    cx = -4.0f;
    cy = -2.0f;
    dd = 2.0f;
    glVertex2f(cx, cy + dd);  //上
    glVertex2f(cx + dd, cy);  //右
    glVertex2f(cx, cy - dd);  //下
    glVertex2f(cx - dd, cy);  //左

    glColor3f(0.5, 0.7, 0.2);
    cx = -4.0f;
    cy = -2.0f - 4.0f;
    dd = 2.0f;
    glVertex2f(cx, cy + dd);  //上
    glVertex2f(cx - dd, cy);  //左
    glVertex2f(cx, cy - dd);  //下
    glVertex2f(cx + dd, cy);  //右

    glEnd();

    //畫三角形, 三個頂點為一組
    glBegin(GL_TRIANGLES);
    glColor3f(0.2, 0.5, 0.7);
    x_st = -9.0;
    y_st = -0.0;
    dd = 3.0;
    glVertex2f(x_st, y_st);    //上
    glVertex2f(x_st - dd, y_st - dd);   //左下
    glVertex2f(x_st + dd, y_st - dd);   //右下

    y_st -= dd;
    glVertex2f(x_st, y_st);    //上
    glVertex2f(x_st - dd, y_st - dd);   //左下
    glVertex2f(x_st + dd, y_st - dd);   //右下

    y_st -= dd;
    glVertex2f(x_st, y_st);    //上
    glVertex2f(x_st - dd, y_st - dd);   //左下
    glVertex2f(x_st + dd, y_st - dd);   //右下

    glEnd();

    //畫三角形帶
    x_st = 0.0;
    y_st = -5.0;
    dd = 2.0;
    glBegin(GL_TRIANGLE_STRIP);
    glColor3f(1.0, 0.0, 0.0);   //紅區
    glVertex2f(x_st, y_st);
    glVertex2f(x_st - dd, y_st + dd);

    glColor3f(0.0, 1.0, 0.0);   //綠區
    glVertex2f(x_st + dd, y_st);

    glColor3f(0.0, 0.0, 1.0);   //藍區
    glVertex2f(x_st, y_st + dd * 2);

    glColor3f(1.0, 1.0, 0.0);   //黃區
    glVertex2f(x_st + dd, y_st + dd);

    glEnd();

    //畫三角形扇
    x_st = 0.0;
    y_st = -8.0;
    dd = 2.0;
    glBegin(GL_TRIANGLE_FAN);
    glColor3f(1.0, 0.0, 0.0);   //紅區
    glVertex2f(x_st, y_st);
    glVertex2f(x_st + dd, y_st + dd);

    glColor3f(0.0, 1.0, 0.0);   //綠區
    glVertex2f(x_st + dd * 2, y_st);

    glColor3f(0.0, 0.0, 1.0);   //藍區
    glVertex2f(x_st + dd * 2, y_st - dd);

    glColor3f(1.0, 1.0, 0.0);   //黃區
    glVertex2f(x_st, y_st - dd);
    glEnd();

    x_st = 8.0f;
    y_st = -12.0f;
    dd = 2.5;
    glBegin(GL_QUAD_STRIP); //多邊形帶
    glColor3f(1.0, 0.0, 0.0);   //紅區
    glVertex2f(x_st, y_st);  //正下
    glVertex2f(x_st - dd, y_st + dd);   //左下
    glVertex2f(x_st + dd, y_st + dd);  //右下

    glColor3f(0.0, 1.0, 0.0);   //綠區
    glVertex2f(x_st - dd, y_st + dd * 2);   //左
    glVertex2f(x_st + dd, y_st + dd * 2);  //右

    glColor3f(0.0, 0.0, 1.0);   //藍區
    glVertex2f(x_st - dd, y_st + dd * 3);   //左
    glVertex2f(x_st + dd, y_st + dd * 3);  //右

    glColor3f(1.0, 1.0, 0.0);   //黃區
    glVertex2f(x_st, y_st + dd * 4);  //正上
    glEnd();



    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    //printf("reshape is called\n");
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();   //設置單位矩陣
    gluLookAt(0, 0, 25, 0, 0, -1, 0, 1, 0);
}

void keyboard(unsigned char k, int /*x*/, int /*y*/)
{
    switch (k)
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
    case '?':
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
    glutInit(&argc, argv);
    //glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
    glutInitWindowPosition(1100, 200);	//視窗起始位置

    glutCreateWindow("幾何圖形繪制");	//開啟視窗 並顯示出視窗 Title

    init();

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function

    glutMainLoop();     // 開始主循環繪制

    return 0;
}

