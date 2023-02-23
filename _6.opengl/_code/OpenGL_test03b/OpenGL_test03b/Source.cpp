#include "../../Common.h"

int display_mode = 1;

int full_screen = 0;

float x[2][2];
float y[2][2];
float z[2][2];  //沒用到, 預留
void gfxinit2(void)
{
    //第一條線之起點, 左下
    x[0][0] = -8;
    y[0][0] = -8;
    z[0][0] = -85;   //z先不管

    //第一條線之終點, 右下
    x[0][1] = 8;
    y[0][1] = -3;
    z[0][1] = 85;    //z先不管

    //第二條線之起點, 左上
    x[1][0] = -8;
    y[1][0] = 8;
    z[1][0] = 25;    //z先不管

    //第二條線之終點, 右上
    x[1][1] = 8;
    y[1][1] = 3;
    z[1][1] = -35;   //z先不管

    float u, u1, v, v1, x1, y1, x2, y2;

    /* Initialize graphics mode.  Assume all coordinates are in [-10,10]. */

    glClearColor(1.0, 1.0, 1.0, 0.0);  //背景白色
    glColor3f(1.0, 1.0, 0.0);          //畫黃線
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0);   //設定畫圖邊界 x= -10 ~ 10, y = -10 ~ 10

    //在 List 1 製作第1張圖
    glNewList(1, GL_COMPILE);   //for bilinear patch

    /* Draw the rulings of u (constant u values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    glBegin(GL_LINES);
    for (u = 0.0f; u < 1.001f; u += 0.1f)
    {
        u1 = 1.0f - u;
        x1 = u1 * x[0][0] + u * x[1][0];
        y1 = u1 * y[0][0] + u * y[1][0];
        x2 = u1 * x[0][1] + u * x[1][1];
        y2 = u1 * y[0][1] + u * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }

    /* Draw the rulings of v (constant v values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    for (v = 0.0f; v < 1.001f; v += 0.1f)
    {
        v1 = 1.0f - v;
        x1 = v1 * x[0][0] + v * x[0][1];
        y1 = v1 * y[0][0] + v * y[0][1];
        x2 = v1 * x[1][0] + v * x[1][1];
        y2 = v1 * y[1][0] + v * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }
    glEnd();

    glEndList();
}

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

void gfxinit1()
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-0.1, 1.1, -0.1, 1.1);
    glClearColor(1.0, 1.0, 1.0, 1.0);
}

#define R  2.0f
#define M_PI 3.141592654

double M_PI_2 = M_PI / 2.0;
float TwoR = 2.0 * R;

/* This function evaluates the x(u, v) function for the sphere. */
float spherex(float u, float v)
{
    return R * cos(v) * cos(u);
}

/* This function evaluates the y(u, v) function for the sphere. */
float spherey(float u, float v)
{
    return R * sin(v);
}

/* This function evaluates the z(u, v) function for the sphere. */
float spherez(float u, float v)
{
    return R * cos(v) * sin(u);
}

/* This function draws a sphere as a surface of revolution. */
void sphere(void)
{
    float u, v;

    /* Draw the meridians (constant u values). */

    for (u = 0.0; u < 2 * M_PI + M_PI / 10; u += M_PI / 5)
    {
        glBegin(GL_LINE_STRIP);
        for (v = -M_PI_2; v < M_PI_2 + 0.005; v += 0.01)
        {
            glVertex3f(spherex(u, v), spherey(u, v), spherez(u, v));
        }
        glEnd();
    }

    /* Draw the parallels (constant v values). */

    for (v = -M_PI_2; v < M_PI_2 + M_PI / 20; v += M_PI / 10)
    {
        glBegin(GL_LINE_STRIP);
        for (u = 0.0; u < 2 * M_PI + 0.005; u += 0.01)
        {
            glVertex3f(spherex(u, v), spherey(u, v), spherez(u, v));
        }
        glEnd();
    }
    glEnd();
}

void show_figure()
{
    glClearColor(1.0, 1.0, 1.0, 0.0);   //設定背景為白色
    glColor3f(1.0, 0.0, 0.0);           //紅色線

    float xview, yview, zview, nearPlane, farPlane, dist, angle, fovy;

    /* Initialize graphics mode and set the window based on R. */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    // set up orthographic projection
    glOrtho(-TwoR, TwoR, -TwoR, TwoR, -TwoR, TwoR);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glDeleteLists(1, 1);  // erase the current figure

    glNewList(2, GL_COMPILE);   //for sphere

    sphere();

    glEndList();
    glutPostRedisplay();
}

/*  Initialize alpha blending function.  */
void gfxinit8(void)
{
    //以下未預設值, 寫不寫都一樣
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0);   //窗口座標範圍2D, 顯示範圍 : X軸(-1.0 ~ 1.0) Y軸(-1.0 ~ 1.0), 左下為原點

    printf("設定 alpha blending, 無恢復\n");
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glShadeModel(GL_FLAT);
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

void display1()
{
    reset_default_setting();

    //display_mode = 1

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

    //畫實心矩形
    glColor3f(1.0f, 1.0f, 0.0f);    //設定顏色 Yellow
    glRectf(-0.4f, -0.4f, 0.4f, 0.4f);

    //畫各種矩形
    glColor3f(0.0, 1.0, 1.0);   //設定顏色 cyan
    float dd = 0.6f;

    //GL_FRONT GL_BACK GL_FRONT_AND_BACK
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);    //空心矩形
    glLineWidth(5.0f);	//設定線寬
    glRectf(-dd, -dd, dd, dd);

    dd = 0.4f;
    glPolygonMode(GL_FRONT_AND_BACK, GL_POINT);    //畫點
    glPointSize(20.0f); //設定點的大小
    glRectf(-dd, -dd, dd, dd);

    dd = 0.2f;
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);    //實心矩形
    glRectf(-dd, -dd, dd, dd);

    draw_rectangle(color_purple, 3, -0.9f, -0.9f, 0.4f, 0.4f);
    fill_rectangle(color_purple, -0.8f, -0.8f, 0.2f, 0.2f);
}

void display2()
{
    reset_default_setting();

    //display_mode = 2  //畫 彩色三角形 Maxwell's Triangle

    // 繪製三角形
    glBegin(GL_TRIANGLES);
    {
        float dd = 0.5f;
        glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 0, 255, 255);     //B 上
        glVertex3f(0.0f, dd, 0); //上

        glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 255, 0, 255);     //G 右下
        glVertex3f(dd, -dd, 0); //右下

        glNormal3f(0.0f, -1.0f, 0.0f);	//設置法線
        glColor4ub(255, 0, 0, 255);     //R 左下
        glVertex3f(-dd, -dd, 0);    //左下
    }
    glEnd();    // 結束畫三角形
}

void display3()
{
    reset_default_setting();

    //display_mode = 3

    glOrtho(-10, 10, -10, 10, -10, 10);      //正交投影
    glPolygonMode(GL_FRONT, GL_LINE);
    draw_boundary(color_y, 9.6f); //畫視窗邊界

    float dd;
    glColor3f(1.0, 1.0, 1.0);	//White
    glBegin(GL_QUADS);	//畫矩形
    //逆時針為空心
    //畫一個白色外框
    dd = 9.4f;
    glVertex3f(-dd, dd, 0.0f);	//左上
    glVertex3f(-dd, -dd, 0.0f);	//左下
    glVertex3f(dd, -dd, 0.0f);	//右下
    glVertex3f(dd, dd, 0.0f);	//右上

    //順時針為實心
    //畫一個白色實心矩形
    dd = 3.0f;
    glVertex3f(-dd, dd, 0.0f);	//左上
    glVertex3f(dd, dd, 0.0f);	//右上
    glVertex3f(dd, -dd, 0.0f);	//右下
    glVertex3f(-dd, -dd, 0.0f);	//左下
    glEnd();

    //畫三角形 2D
    glBegin(GL_TRIANGLES);
    glColor3f(1.0, 0.0, 0.0);	//R
    //逆時針為空心
    glVertex2f(2.0, 4.0);	//左下
    glVertex2f(8.0, 4.0);	//右下
    glVertex2f(5.0, 9.0);	//上
    glEnd();

    //畫三角形 3D
    glBegin(GL_TRIANGLES);
    //逆時針為空心
    for (dd = 7.0f; dd <= 9.0f; dd += 1.0f)
    {
        glColor3f(1, 0, 0);	//R
        glVertex3f(dd, -dd, 0);	//右下
        glColor3f(0, 1, 0);	//G
        glVertex3f(0, dd, 0);	//上
        glColor3f(0, 0, 1);	//B
        glVertex3f(-dd, -dd, 0);	//左下
    }

    /*
    //順時針為實心
    dd = 1.0f;
    {
        glColor3f( 0, 0, 1);	//B
        glVertex3f(-dd, -dd, 0);	//左下
        glColor3f( 0, 1, 0);	//G
        glVertex3f( 0, dd, 0);	//上
        glColor3f( 1, 0, 0);	//R
        glVertex3f( dd, -dd, 0);	//右下
    }
    */
    glEnd();

    //畫矩形
    float x_st = -8.0f;
    float y_st = 2.0f;
    float w = 4.0f;
    float h = 4.0f;
    //左下x,  左下y,  右上x,  右上y
    glRectf(x_st, y_st, x_st + w, y_st + h);

    for (dd = 1.0f; dd <= 2.0f; dd += 0.5f)
    {
        //左下x,  左下y,  右上x,  右上y
        //glRectf(dd, dd, dd+3.0f, dd+3.0f);
        glRectf(x_st + dd, y_st + dd, x_st + w + dd, y_st + h + dd);
    }
}

void display4()
{
    reset_default_setting();

    /*
    void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z = 0, GLdouble w = 1);
    void glRasterPos4dv(const GLdouble* v);
    //確定當前光柵位置，x,y,z,w指定了當前光柵位置的座標

    glWindowPos(Type x, Type y, Type z);
    //用窗口座標指定當前光柵位置，不必進行矩陣變換、裁剪、或紋理座標生成。z值被變換為由glDepthRange()設置的當前近側平面值和遠側平面值

    void glBitmap(GLsizei, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat, GLfloat, const GLubyte* bitmap);
    //繪製由bitmap指定的位圖，bitmap是一個指向位圖圖像的指針，位圖的原點是當前光柵位置，如果當前光柵位置無效，則這個函數不會繪製任何東西。
    //width和height表示位圖的寬度和高度，xorig和yorig定義了位圖的原點，他是根據當期光柵位置確定的，右上為正。
    //xmove和ymove表示位圖光柵化之後光柵座標的x增加值和y增加值
    */

    //display_mode = 4  測試Bipmap畫圖

    glOrtho(0, 600, 0, 600, -1.0, 1.0);	//改變投影變換	//改變窗口座標範圍, 3D

    glColor3f(1.0, 0.0, 0.0);	//設定顏色

    //光柵的位置
    glRasterPos2i(0, 0);//確定當前光柵位置，x,y,z,w指定了當前光柵位置的座標

    //畫一個64*64
    int i;
    int len = 64 / 8 * 64;
    GLubyte rasters[64 / 8 * 64] = {
    };
    for (i = 0; i < len; i++)
    {
        if (i % 2 == 0)
            rasters[i] = 0xff;
        else
            rasters[i] = 0xff;
    }

    float offsetx = 0.0;
    float offsety = 0.0;
    float dx = 100.0;
    float dy = 100.0;

    //畫完bmp後, 下次位置加上dx dy
    glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);
    glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);
    glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);
    glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);

    for (i = 0; i < len; i++)
    {
        if (i % 2 == 0)
            rasters[i] = 0x55;
        else
            rasters[i] = 0x55;
    }
    glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);

    //繪製由bitmap指定的位圖，bitmap是一個指向位圖圖像的指針，位圖的原點是當前光柵位置，如果當前光柵位置無效，則這個函數不會繪製任何東西。
    //width和height表示位圖的寬度和高度，xorig和yorig定義了位圖的原點，他是根據當期光柵位置確定的，右上為正。
    //xmove和ymove表示位圖光柵化之後光柵座標的x增加值和y增加值

    glFlush();  // 執行繪圖命令
}

void display5()
{
    reset_default_setting();

    //display_mode = 5  //畫 彩色三角形 Maxwell's Triangle

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);    //實心矩形
    //glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_TRIANGLES);
    {
        float dd = 0.5f;
        //glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 0, 255, 255);     //B 上
        glVertex3f(0.0f, dd, 0); //上

        //glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 255, 0, 255);     //G 右下
        glVertex3f(dd, -dd, 0); //右下

        //glNormal3f(0.0f, -1.0f, 0.0f);	//設置法線
        glColor4ub(255, 0, 0, 255);     //R 左下
        glVertex3f(-dd, -dd, 0);    //左下
    }
    glEnd();
    glFlush();  // 執行繪圖命令
}

void display6()
{
    reset_default_setting();

    //display_mode = 6  //畫 binear patch

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0);   //設定畫圖邊界 x= -10 ~ 10, y = -10 ~ 10

    //glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);  //顯示第1張圖

    draw_coordinates(8.0f);     //畫座標軸
    draw_rectangle(color_g, 2.0f, -8.2f, -8.2f, 16.4f, 16.4f);

    glFlush();  // 執行繪圖命令
}

void display7()
{
    reset_default_setting();

    //display_mode = 7  //畫 sphere

    show_figure();

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(2);
    glFlush();  // 執行繪圖命令
}

void display8()
{
    reset_default_setting();

    //display_mode = 8  //畫 alpha blending

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glMatrixMode(GL_MODELVIEW);

    draw_coordinates(0.85f);     //畫座標軸

    glColor4f(1.0, 0.0, 0.0, 0.5); //R
    glRectf(-0.6f, -0.2f, 0.6f, 0.8f);

    glColor4f(0.0, 1.0, 0.0, 0.5); //G
    glRectf(-0.8f, -0.8f, 0.2f, 0.5f);

    glColor4f(0.0, 0.0, 1.0, 0.5); //B
    glRectf(-0.2f, -0.8f, 0.8f, 0.5f);

    glColor4f(1.0, 0.0, 0.0, 1.0);
    glRectf(0.33f, 0.33f, 0.66f, 0.66f);
}

void display9()
{

}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        reset_default_setting();
    }
    else if (display_mode == 1)
    {
        display1();
    }
    else if (display_mode == 2)
    {
        display2();
    }
    else if (display_mode == 3)
    {
        display3();
    }
    else if (display_mode == 4)
    {
        display4();
    }
    else if (display_mode == 5)
    {
        display5();
    }
    else if (display_mode == 6)
    {
        display6();
    }
    else if (display_mode == 7)
    {
        display7();
    }
    else if (display_mode == 8)
    {
        display8();
    }
    else if (display_mode == 9)
    {
        display9();
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

    glFlush();  // 執行繪圖命令
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
    case ' ':
        if (full_screen == 0)
        {
            full_screen = 1;
            printf("全螢幕\n");
            glutFullScreen();   //全螢幕顯示
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
        printf("畫各種矩形\n");
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
        gfxinit1();
        break;
    case '6':
        display_mode = 6;
        printf("Bilinear Patch\n");
        gfxinit2();
        break;
    case '7':
        display_mode = 7;
        break;
    case '8':
        display_mode = 8;
        gfxinit8();
        break;
    case '9':
        display_mode = 9;
        break;

    }
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

int main(int argc, char** argv)
{
    const char* windowName = "簡單2D OpenGL畫圖 0 ~ 9";
    const char* message = "簡單2D OpenGL畫圖 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    glutMouseFunc(mouse0);		//設定callback function
    glutMotionFunc(motion0);    //設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}


