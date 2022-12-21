/****************************************************************************
 * bilinear.cpp                                                             *
 *    This graphics program constructs a bilinear patch for a surface       *
 * defined by four corners.                                                 *
 * NOTE:  At this time the z component of the surface is ignored, giving a  *
 *        parallel projection onto the x,y-plane, which is assumed to be    *
 *        the display device.                                               *
 ****************************************************************************/

#include "../../Common.h"

float x[2][2], y[2][2], z[2][2];

void gfxinit(void)
{
    float u, u1, v, v1, x1, y1, x2, y2;

    /* Initialize graphics mode.  Assume all coordinates are in [-10,10]. */

    glClearColor(1.0, 1.0, 1.0, 0.0);  /* Make the background white. */
    glColor3f(0.0, 0.0, 0.0);          /* Draw in black.             */
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0);

    glNewList(1, GL_COMPILE);

    /* Draw the rulings of u (constant u values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    glBegin(GL_LINES);
    for (u = 0.0; u < 1.001; u += 0.1)
    {
        u1 = 1.0 - u;
        x1 = u1 * x[0][0] + u * x[1][0];   y1 = u1 * y[0][0] + u * y[1][0];
        x2 = u1 * x[0][1] + u * x[1][1];   y2 = u1 * y[0][1] + u * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }

    /* Draw the rulings of v (constant v values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    for (v = 0.0; v < 1.001; v += 0.1)
    {
        v1 = 1.0 - v;
        x1 = v1 * x[0][0] + v * x[0][1];   y1 = v1 * y[0][0] + v * y[0][1];
        x2 = v1 * x[1][0] + v * x[1][1];   y2 = v1 * y[1][0] + v * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }
    glEnd();

    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    cout << "Bilinear Patches" << endl << endl;
    cout << "Please enter the four points in the following sequence." << endl;
    cout << "The first two points define the v=0 edge and the last two points" << endl;
    cout << "define the v=1 edge." << endl << endl;
    /*
    cout << "Enter coordinates of p[0][0]:  ";
    cin >> x[0][0] >> y[0][0] >> z[0][0];
    cout << "Enter coordinates of p[1][0]:  ";
    cin >> x[1][0] >> y[1][0] >> z[1][0];
    cout << "Enter coordinates of p[0][1]:  ";
    cin >> x[0][1] >> y[0][1] >> z[0][1];
    cout << "Enter coordinates of p[1][1]:  ";
    cin >> x[1][1] >> y[1][1] >> z[1][1];
    */

    //第一條線之起點, 左下
    x[0][0] = -8;
    y[0][0] = -8;
    z[0][0] = -8;   //z先不管

    //第一條線之終點, 右下
    x[0][1] = 8;
    y[0][1] = -8;
    z[0][1] = 8;    //z先不管

    //第二條線之起點, 左上
    x[1][0] = -5;
    y[1][0] = 8;
    z[1][0] = 2;    //z先不管

    //第二條線之終點, 右上
    x[1][1] = 5;
    y[1][1] = 5;
    z[1][1] = -3;   //z先不管

    const char* windowName = "Bilinear Patch";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
