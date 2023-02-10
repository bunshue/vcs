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

    glNewList(1, GL_COMPILE);

    sphere();

    glEndList();
    glutPostRedisplay();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    const char* windowName = "Sphere";
    const char* message = "按 1~2 選擇, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    show_figure();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
