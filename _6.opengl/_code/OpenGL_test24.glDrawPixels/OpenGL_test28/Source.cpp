#include "../../Common.h"

#define    W 256
#define    H 256
unsigned char image_data[H][W][3];

static GLfloat zoomFactor = 0.7f;
static GLint height;

void makeImageData(void)
{
    int i, j, c;

    for (i = 0; i < H; i++)
    {
        for (j = 0; j < W; j++)
        {
            c = (i + j) / 2;
            image_data[i][j][0] = (unsigned char)c;
            image_data[i][j][1] = (unsigned char)c;
            image_data[i][j][2] = (unsigned char)c;
        }
    }
}

void init(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glShadeModel(GL_FLAT);
    makeImageData();
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //glRasterPos2i(0, 0);
    glRasterPos2f(-0.9f, -0.9f);
    glDrawPixels(W, H, GL_RGB, GL_UNSIGNED_BYTE, image_data);
    //           W, H, format,       type,         pixels

    //glPixelZoom(zoomFactor, zoomFactor);  //縮放圖片, 水平3倍, 垂直3倍

    glRasterPos2f(0.0f, 0.0f);
    //複製圖片, 從(0,0)複製WXH
    glCopyPixels(0, 0, W, H, GL_COLOR);    //有Zoom之後要做很久

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

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL測試";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    init();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
