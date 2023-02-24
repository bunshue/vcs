#include "../../Common.h"

int display_mode = 1;

int full_screen = 0;

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

void display1(void)
{
    reset_default_setting();

    //dummy

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

    glFlush();  // 執行繪圖命令
}

#define W 128
#define H 128

void display2(void)
{
    reset_default_setting();

    int i = 0;
    int j = 0;
    unsigned char ubImage[W * H * 4];
    unsigned char* img;

    /* Create image */
    img = ubImage;
    for (j = 0; j < 32 * W; j++)
    {
        //紅
        *img++ = 0xff;  //A
        *img++ = 0x00;  //B
        *img++ = 0x00;  //G
        *img++ = 0xff;  //R
    }

    for (j = 0; j < 32 * W; j++)
    {
        //綠
        *img++ = 0xff;  //A
        *img++ = 0x00;  //B
        *img++ = 0xff;  //G
        *img++ = 0x00;  //R
    }

    for (j = 0; j < 32 * W; j++)
    {
        //藍
        *img++ = 0xff;  //A
        *img++ = 0xff;  //B
        *img++ = 0x00;  //G
        *img++ = 0x00;  //R
    }

    for (j = 0; j < 32 * W; j++)
    {
        //黃
        *img++ = 0x00;  //A
        *img++ = 0x00;  //B
        *img++ = 0xff;  //G
        *img++ = 0xff;  //R
    }

    //           w  h     format        type           pixels
    glDrawPixels(W, H, GL_ABGR_EXT, GL_UNSIGNED_BYTE, ubImage);

    glFlush();  // 執行繪圖命令
}

#define    WW 256
#define    HH 256
unsigned char image_data[HH][WW][3];

float zoomFactor = 0.7f;
int height;

void makeImageData(void)
{
    int i, j, c;

    for (i = 0; i < HH; i++)
    {
        for (j = 0; j < WW; j++)
        {
            c = (i + j) / 2;
            image_data[i][j][0] = (unsigned char)c;
            image_data[i][j][1] = (unsigned char)c;
            image_data[i][j][2] = (unsigned char)c;
        }
    }
}

void display3(void)
{
    reset_default_setting();

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glShadeModel(GL_FLAT);
    makeImageData();
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //glRasterPos2i(0, 0);
    glRasterPos2f(-0.9f, -0.9f);
    glDrawPixels(WW, HH, GL_RGB, GL_UNSIGNED_BYTE, image_data);
    //           W, H, format,       type,         pixels

    //glPixelZoom(zoomFactor, zoomFactor);  //縮放圖片, 水平3倍, 垂直3倍

    glRasterPos2f(0.0f, 0.0f);
    //複製圖片, 從(0,0)複製WXH
    glCopyPixels(0, 0, WW, HH, GL_COLOR);    //有Zoom之後要做很久

    glFlush();

    /*  TBD
    int W = 100;
    int H = 100;
    GLushort* points = (GLushort*)calloc(W * H, sizeof(GLushort));
    memset(points, 13, sizeof(GLushort) * W * H);   //给*p指定的前100字节大小的内存空间设置为(只支持0, 1，以字节为单位赋初始值)

    //setup locations
    glRasterPos2f(-0.9f, -0.9f);
    glDrawPixels(W, H, GL_COLOR_INDEX, GL_UNSIGNED_SHORT, points);

    //glDrawPixels(128, 128, GL_ABGR_EXT, GL_UNSIGNED_BYTE, ubImage);
    */
    glFlush();  // 執行繪圖命令
}

void display4(void)
{
    reset_default_setting();

    glFlush();  // 執行繪圖命令
}

void display5(void)
{
    reset_default_setting();

    glFlush();  // 執行繪圖命令
}

void display6(void)
{
    reset_default_setting();

    glFlush();  // 執行繪圖命令
}

void display7(void)
{
    reset_default_setting();

    glFlush();  // 執行繪圖命令
}

void display8(void)
{
    reset_default_setting();

    glFlush();  // 執行繪圖命令
}

void display9(void)
{
    reset_default_setting();

    glFlush();  // 執行繪圖命令
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

    glutMainLoop();	//開始主循環繪製

    return 0;
}


