#include "../../Common.h"

GLubyte ubImage[65536];

void setup_pixel_data()
{
    int i = 0;
    int j = 0;

    GLubyte* img;
    GLsizei imgWidth = 128;

    /* Create image */
    img = ubImage;
    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0x00;
        *img++ = 0xff;
    }

    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0xff;
        *img++ = 0x00;
    }

    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0xff;
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0x00;
    }

    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0x00;
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0xff;
    }

    glNewList(1, GL_COMPILE);
    //            w    h     format        type            pixels
    glDrawPixels(128, 128, GL_ABGR_EXT, GL_UNSIGNED_BYTE, ubImage);
    glEndList();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glFlush();
}

int main(int argc, char** argv)
{
    const char* windowName = "glDrawPixels 與 glCallList 使用範例";
    const char* message = "glDrawPixels 與 glCallList 使用範例\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    setup_pixel_data();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
