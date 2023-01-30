/****************************************************************************
 * revolution.cpp                                                           *
 *    This graphics program constructs surfaces of revolution.              *
 ****************************************************************************/

#include "../../Common.h"

#define R  2.0f
#define M_PI 3.141592654

double M_PI_2 = M_PI / 2.0;
float TwoR = 2.0 * R;

void gfxinit(void)
{
    /* Set graphics background and foreground colors. */

    glClearColor(1.0, 1.0, 1.0, 0.0);  /* Make the background white. */
    glColor3f(0.0, 0.0, 0.0);          /* Draw in black.             */
}

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
        if (fabs(v - 0.2) < 1e-6) v = 0.25;
        if (fabs(v - 0.3) < 1e-6) v = 0.75;
        if (fabs(v - 0.8) < 1e-6) v = 0.9;
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

/* This is the callback function for the menu selection to determine which
   figure to draw on the screen. */
void figureMenu(int figure)
{
    float xview, yview, zview, nearPlane, farPlane, dist, angle, fovy;

    /* Initialize graphics mode and set the window based on R. */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    printf("你按了 %d\n", figure);
    if (figure < 5) // set up orthographic projection
    {
        glOrtho(-TwoR, TwoR, -TwoR, TwoR, -TwoR, TwoR);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
    }
    else // set up perspective projection
    {
        cout << endl << "Enter coordinates of viewing point: ";
        cin >> xview >> yview >> zview;
        cout << endl << "Enter near and far clipping planes: ";
        cin >> nearPlane >> farPlane;
        dist = sqrt(xview * xview + yview * yview + zview * zview);
        if (figure == 5)
        {
            angle = 2.0 * atan2(R, dist);
        }
        else
        {
            angle = 2.0 * atan2(1.5f * R, dist);
        }
        fovy = 180.0 * angle / M_PI;
        gluPerspective(fovy, 1.0, nearPlane, farPlane);
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        glTranslatef(0.0, 0.0, -R - 1);
        gluLookAt(xview, yview, zview, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    }
    glDeleteLists(1, 1);  // erase the current figure
    glNewList(1, GL_COMPILE);
    switch (figure)
    {
    case 1:
    case 5: sphere();
        break;
    case 2: sphere_profile();
        break;
    case 3:
    case 6:  goblet();
        break;
    case 4: goblet_profile();
        break;
    }
    glEndList();
    glutPostRedisplay();
}

/* This is the callback function that gets executed every time the display needs to be updated. */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
    const char* windowName = "Surfaces of Revolution";
    const char* message = "按 滑鼠右鍵選單 切換, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    //滑鼠右鍵選單
    glutCreateMenu(figureMenu);
    glutAddMenuEntry("Sphere (orthographic)", 1);
    glutAddMenuEntry("Sphere (perspective) XXX", 5);
    glutAddMenuEntry("Sphere (profile only)", 2);
    glutAddMenuEntry("Goblet (orthographic)", 3);
    glutAddMenuEntry("Goblet (perspective) XXX", 6);
    glutAddMenuEntry("Goblet (profile only)", 4);
    glutAttachMenu(GLUT_RIGHT_BUTTON);

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
