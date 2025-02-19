#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "../../Common.h"

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#define PI 3.141592657

enum {
    NORMAL = 0,
    WEIRD = 1
};

enum {
    STREAK = 0,
    CIRCLE = 1
};

#define MAXSTARS 400
#define MAXPOS 10000
#define MAXWARP 10
#define MAXANGLES 6000

typedef struct _starRec {
    GLint type;
    float x[2], y[2], z[2];
    float offsetX, offsetY, offsetR, rotation;
} starRec;

GLint windW = 600;
GLint windH = 600;

GLenum flag = NORMAL;
GLint starCount = MAXSTARS / 2;
float speed = 1.0;
GLint nitro = 0;
starRec stars[MAXSTARS];
float sinTable[MAXANGLES];

float Sin(float angle)
{
    return (sinTable[(GLint)angle]);
}

float Cos(float angle)
{
    return (sinTable[((GLint)angle + (MAXANGLES / 4)) % MAXANGLES]);
}

void NewStar(GLint n, GLint d)
{
    if (rand() % 4 == 0)
    {
        stars[n].type = CIRCLE;
    }
    else
    {
        stars[n].type = STREAK;
    }
    stars[n].x[0] = (float)(rand() % MAXPOS - MAXPOS / 2);
    stars[n].y[0] = (float)(rand() % MAXPOS - MAXPOS / 2);
    stars[n].z[0] = (float)(rand() % MAXPOS + d);

    if (rand() % 4 == 0 && flag == WEIRD)
    {
        stars[n].offsetX = (float)(rand() % 100 - 100 / 2);
        stars[n].offsetY = (float)(rand() % 100 - 100 / 2);
        stars[n].offsetR = (float)(rand() % 25 - 25 / 2);
    }
    else
    {
        stars[n].offsetX = 0.0;
        stars[n].offsetY = 0.0;
        stars[n].offsetR = 0.0;
    }
}

void RotatePoint(float* x, float* y, float rotation)
{
    float tmpX, tmpY;

    tmpX = *x * Cos(rotation) - *y * Sin(rotation);
    tmpY = *y * Cos(rotation) + *x * Sin(rotation);
    *x = tmpX;
    *y = tmpY;
}

void MoveStars(void)
{
    float offset;
    GLint n;

    offset = speed * 60.0;

    for (n = 0; n < starCount; n++)
    {
        stars[n].x[1] = stars[n].x[0];
        stars[n].y[1] = stars[n].y[0];
        stars[n].z[1] = stars[n].z[0];
        stars[n].x[0] += stars[n].offsetX;
        stars[n].y[0] += stars[n].offsetY;
        stars[n].z[0] -= offset;
        stars[n].rotation += stars[n].offsetR;
        if (stars[n].rotation > MAXANGLES)
        {
            stars[n].rotation = 0.0;
        }
    }
}

GLenum StarPoint(GLint n)
{
    float x0, y0, x1, y1, width;
    GLint i;

    x0 = stars[n].x[0] * windW / stars[n].z[0];
    y0 = stars[n].y[0] * windH / stars[n].z[0];
    RotatePoint(&x0, &y0, stars[n].rotation);
    x0 += windW / 2.0;
    y0 += windH / 2.0;

    if (x0 >= 0.0 && x0 < windW && y0 >= 0.0 && y0 < windH)
    {
        if (stars[n].type == STREAK)
        {
            x1 = stars[n].x[1] * windW / stars[n].z[1];
            y1 = stars[n].y[1] * windH / stars[n].z[1];
            RotatePoint(&x1, &y1, stars[n].rotation);
            x1 += windW / 2.0;
            y1 += windH / 2.0;

            glLineWidth(MAXPOS / 100.0 / stars[n].z[0] + 1.0);
            glColor3f(1.0, (MAXWARP - speed) / MAXWARP, (MAXWARP - speed) / MAXWARP);
            if (fabs(x0 - x1) < 1.0 && fabs(y0 - y1) < 1.0)
            {
                glBegin(GL_POINTS);
                glVertex2f(x0, y0);
                glEnd();
            }
            else
            {
                glBegin(GL_LINES);
                glVertex2f(x0, y0);
                glVertex2f(x1, y1);
                glEnd();
            }
        }
        else
        {
            width = MAXPOS / 10.0 / stars[n].z[0] + 1.0;
            glColor3f(1.0, 0.0, 0.0);
            glBegin(GL_POLYGON);
            for (i = 0; i < 8; i++)
            {
                float x = x0 + width * Cos((float)i * MAXANGLES / 8.0);
                float y = y0 + width * Sin((float)i * MAXANGLES / 8.0);
                glVertex2f(x, y);
            };
            glEnd();
        }
        return GL_TRUE;
    }
    else
    {
        return GL_FALSE;
    }
}

void ShowStars(void)
{
    GLint n;

    glClear(GL_COLOR_BUFFER_BIT);

    for (n = 0; n < starCount; n++)
    {
        if (stars[n].z[0] > speed || (stars[n].z[0] > 0.0 && speed < MAXWARP))
        {
            if (StarPoint(n) == GL_FALSE)
            {
                NewStar(n, MAXPOS);
            }
        }
        else
        {
            NewStar(n, MAXPOS);
        }
    }
}

static void Init(void)
{
    float angle;
    GLint n;

    srand((unsigned int)time(NULL));

    for (n = 0; n < MAXSTARS; n++)
    {
        NewStar(n, 100);
    }

    angle = 0.0;
    for (n = 0; n < MAXANGLES; n++)
    {
        sinTable[n] = sin(angle);
        angle += PI / (MAXANGLES / 2.0);
    }

    glClearColor(0.0, 0.0, 0.0, 0.0);

    glDisable(GL_DITHER);
}

void reshape(int width, int height)
{
    windW = width;
    windH = height;

    glViewport(0, 0, windW, windH);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-0.5, windW + 0.5, -0.5, windH + 0.5);	//窗口座標範圍, 2D
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case ' ':
        flag = (flag == NORMAL) ? WEIRD : NORMAL;
        break;
    case 't':
        nitro = 1;
        break;
    case 27:
        exit(0);
    }
}

void Idle(void)
{
    MoveStars();
    ShowStars();
    if (nitro > 0)
    {
        speed = (float)(nitro / 10) + 1.0;
        if (speed > MAXWARP)
        {
            speed = MAXWARP;
        }
        if (++nitro > MAXWARP * 10)
        {
            nitro = -nitro;
        }
    }
    else if (nitro < 0)
    {
        nitro++;
        speed = (float)(-nitro / 10) + 1.0;
        if (speed > MAXWARP)
        {
            speed = MAXWARP;
        }
    }

    draw_boundary(color_y, 580.0f); //畫視窗邊界

    glFlush();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

    glutInitWindowSize(windW, windH);   // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Stars");	//開啟視窗 並顯示出視窗 Title

    Init();

    //glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    //glutSpecialFunc(special);    //設定callback function
    glutIdleFunc(Idle);             //設定callback function   Idle像是display
    glutDisplayFunc(Idle);          //設定callback function   Idle像是display

    glutMainLoop();	//開始主循環繪製

    return 0;
}
