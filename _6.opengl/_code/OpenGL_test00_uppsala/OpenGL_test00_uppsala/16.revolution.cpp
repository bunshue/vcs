/****************************************************************************
 * revolution.cpp                                                           *
 *    This graphics program constructs surfaces of revolution.              *
 ****************************************************************************/

#include "../../Common.h"

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

void sphere_profile(void)
/* This function draws the profile of the sphere. */
{
    float v;

    glBegin(GL_LINE_STRIP);
    for (v = -M_PI_2; v < M_PI_2 + 0.005; v += 0.01)
    {
        glVertex2f(spherex(0.0, v), spherey(0.0, v));
    }
    glEnd();
}

/* This function evaluates the x(v) function for the goblet. */
float gobletx(float v)
{
    if (v >= 0.95)
    {
        return R;
    }
    if (v >= 0.8)
    {
        return R - (0.95 - v) / 0.15 * 0.75 * R;
    }
    if (v >= 0.3)
    {
        return R / 4;
    }
    if (v >= 0.2)
    {
        return R / 4 + (0.3 - v) / 0.1 * R;
    }
    if (v >= 0.1)
    {
        return 0.15 * R * cos(-M_PI_2 + 10.0 * (v - 0.1) * M_PI) + 1.25 * R;
    }
    return 0.15 * R * cos(M_PI_2 + 10.0 * v * M_PI) + 1.25 * R;
}

/* This function evaluates the y(v) function for the goblet. */
float goblety(float v)
{
    if (v >= 0.95)
    {
        return 3 * R * (0.5 - v);
    }
    if (v >= 0.8)
    {
        return -3 * R * 0.45;
    }
    if (v >= 0.3)
    {
        return 3 * R * (0.35 - v);
    }
    if (v >= 0.2)
    {
        return 3 * R * (0.05);
    }
    if (v >= 0.1)
    {
        return -0.15 * R * sin(-M_PI_2 + 10.0 * (v - 0.1) * M_PI) + 0.3 * R;
    }
    return 0.15 * R * sin(M_PI_2 + 10.0 * v * M_PI) + 0.6 * R;
}

/* This function evaluates the x(u, v) function for the goblet. */
float gobletxuv(float u, float v)
{
    return gobletx(v) * cos(u);
}

/* This function evaluates the y(u, v) function for the goblet. */
float gobletyuv(float u, float v)
{
    return goblety(v);
}

/* This function evaluates the z(u, v) function for the goblet. */
float gobletzuv(float u, float v)
{
    return gobletx(v) * sin(u);
}

/* This function draws a goblet as a surface of revolution. */
void goblet(void)
{
    float u, v;

    /* Draw the end meridians (constant u values). */
    for (u = 0.0; u < 2 * M_PI + M_PI / 10; u += M_PI_2)
    {
        glBegin(GL_LINE_STRIP);
        for (v = 0.0; v < 1.005; v += 0.01)
        {
            glVertex3f(gobletxuv(u, v), gobletyuv(u, v), gobletzuv(u, v));
        }
        glEnd();
    }

    /* Draw the parallels (constant v values). */
    for (v = 0.0; v < 1.025; v += 0.05)
    {
        glBegin(GL_LINE_STRIP);
        for (u = 0.0; u < 2 * M_PI + 0.005; u += 0.01)
        {
            glVertex3f(gobletxuv(u, v), gobletyuv(u, v), gobletzuv(u, v));
        }
        glEnd();
        if (fabs(v - 0.2) < 1e-6)
        {
            v = 0.25;
        }
        if (fabs(v - 0.3) < 1e-6)
        {
            v = 0.75;
        }
        if (fabs(v - 0.8) < 1e-6)
        {
            v = 0.9;
        }
    }
}

/* This function draws the profile of the goblet. */
void goblet_profile(void)
{
    float v;

    glBegin(GL_LINE_STRIP);
    for (v = 0.0; v < 1.005; v += 0.01)
    {
        glVertex2f(gobletx(v), goblety(v));
    }
    glEnd();
}

void show_figure(int figure)
{
    printf("你按了 %d\n", figure);
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

    glNewList(1, GL_COMPILE);
    switch (figure)
    {
    case 1:
        sphere();
        break;
    case 2:
        sphere_profile();
        break;
    case 3:
        goblet();
        break;
    case 4:
        goblet_profile();
        break;
    }
    glEndList();
    glutPostRedisplay();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glFlush();  // 執行繪圖命令
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
    case '1':
        printf("你選擇了 1 : Sphere (orthographic)\n");
        show_figure(1);
        break;
    case '2':
        printf("你選擇了 2 : Sphere (profile only)\n");
        show_figure(2);
        break;
    case '3':
        printf("你選擇了 3 : Goblet (orthographic)\n");
        show_figure(3);
        break;
    case '4':
        printf("你選擇了 4 : Goblet (profile only)\n");
        show_figure(4);
        break;
    }
}

int main(int argc, char** argv)
{
    const char* windowName = "Surfaces of Revolution";
    const char* message = "按 1~6 選擇, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    show_figure(1);

    glutMainLoop();	//開始主循環繪製

    return 0;
}
