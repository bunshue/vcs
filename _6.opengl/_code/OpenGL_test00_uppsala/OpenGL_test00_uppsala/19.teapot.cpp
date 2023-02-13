/*****************************************************************************
 * teapot.cpp                                                                *
 *     This program models the famous Utah teapot using Bezier patches.      *
 * OpenGL evaluators are used to draw the surfaces.                          *
 *****************************************************************************/

#include "../../Common.h"

 /* Drawing constants. */
#define STEPS        10  /* number of steps to draw each segment over */
#define PATCHES      32  /* number of surfaces in the teapot          */
#define VERTICES    306  /* number of control points                  */

double points[VERTICES + 1][3];
int patch_vertices[PATCHES][16];
static GLfloat theta[] = { 270.0, 0.0, 180.0 };

void make_teapot_data(void)
{
    ifstream vertices_file;
    ifstream patches_file;
    int i;
    int j;

    //開啟檔案
    printf("開啟檔案: data/19.teapot.vertices\n");
    vertices_file.open("data/19.teapot.vertices", ios::in);
    if (vertices_file.fail())
    {
        printf("找不到檔案: data/19.teapot.vertices\n");
        patches_file.close();
        exit(EXIT_FAILURE);
    }

    printf("開啟檔案: data/19.teapot.patches\n");
    patches_file.open("data/19.teapot.patches", ios::in);
    if (patches_file.fail())
    {
        printf("找不到檔案: data/19.teapot.patches\n");
        exit(EXIT_FAILURE);
    }

    //讀取檔案資料
    for (i = 1; i <= VERTICES; i++)
    {
        vertices_file >> points[i][0] >> points[i][1] >> points[i][2];  //C++之讀取檔案資料
    }
    for (i = 0; i < PATCHES; i++)
    {
        for (j = 0; j < 16; j++)
        {
            patches_file >> patch_vertices[i][j];   //C++之讀取檔案資料
        }
    }
    vertices_file.close();
    patches_file.close();
}

void init_teapot_data(void)
{
    int i;
    int j;
    int k;
    int vertex;
    double coords[48];
    double* p;

    glClearColor(1.0, 1.0, 1.0, 0.0);   //背景為白色
    glEnable(GL_MAP2_VERTEX_3);

    /* Generate the display lists for the surfaces. */
    for (k = 0; k < PATCHES; k++)
    {
        for (i = 0, p = coords; i < 16; i++)
        {
            vertex = patch_vertices[k][i];
            for (j = 0; j < 3; j++, p++)
            {
                *p = points[vertex][j];
            }
        }
        glNewList(k + 1, GL_COMPILE);
        glColor3d(1.0, 0.0, 0.0);   //紅色
        glMap2d(GL_MAP2_VERTEX_3, 0.0, 1.0, 12, 4, 0.0, 1.0, 3, 4, coords);
        glMapGrid2d(STEPS, 0.0, 1.0, STEPS, 0.0, 1.0);
        glEvalMesh2(GL_FILL, 0, STEPS, 0, STEPS);
        glEndList();
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();

    //未旋轉前之座標軸
    //draw_coordinates(1.3f);     //畫座標軸

    glRotatef(theta[0], 1.0, 0.0, 0.0); //對x軸旋轉特定角度
    glRotatef(theta[1], 0.0, 1.0, 0.0); //對y軸旋轉特定角度
    glRotatef(theta[2], 0.0, 0.0, 1.0); //對z軸旋轉特定角度
    for (int i = 1; i <= PATCHES; i++)
    {
        glCallList(i);
    }

    //已旋轉後之座標軸
    draw_coordinates(2.5f);     //畫座標軸

    glFlush();  // 執行繪圖命令
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (width <= height)
    {
        glOrtho(-4.0, 4.0, -4.0 * (GLdouble)height / (GLdouble)width, 4.0 * (GLdouble)height / (GLdouble)width, -10.0, 10.0);
    }
    else
    {
        glOrtho(-4.0 * (GLdouble)width / (GLdouble)height, 4.0 * (GLdouble)width / (GLdouble)height, -4.0, 4.0, -10.0, 10.0);
    }
    glMatrixMode(GL_MODELVIEW);
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
    case 'X':
        printf("繞 x軸 旋轉+\n");
        theta[0] += 4.0;
        if (theta[0] > 360.0)
        {
            theta[0] -= 360.0;
        }
        break;
    case 'x':
        printf("繞 x軸 旋轉-\n");
        theta[0] -= 4.0;
        if (theta[0] < 0.0)
        {
            theta[0] += 360.0;
        }
        break;
    case 'Y':
        printf("繞 y軸 旋轉+\n");
        theta[1] += 4.0;
        if (theta[1] > 360.0)
        {
            theta[1] -= 360.0;
        }
        break;
    case 'y':
        printf("繞 y軸 旋轉-\n");
        theta[1] -= 4.0;
        if (theta[1] < 0.0)
        {
            theta[1] += 360.0;
        }
        break;
    case 'Z':
        printf("繞 z軸 旋轉+\n");
        theta[2] += 4.0;
        if (theta[2] > 360.0)
        {
            theta[2] -= 360.0;
        }
        break;
    case 'z':
        printf("繞 z軸 旋轉-\n");
        theta[2] -= 4.0;
        if (theta[2] < 0.0)
        {
            theta[2] += 360.0;
        }
        break;
    }
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    make_teapot_data();		//讀取資料

    const char* windowName = "猶太茶壺";
    const char* message = "猶太茶壺, 按 X x Y y Z z 控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    init_teapot_data();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
