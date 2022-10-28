#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include "rgb.h"

GLint windW = 600;
GLint windH = 600;

RGBImageRec* image = NULL;
float point[3];
float zoom;
GLint x;
GLint y;

void Init(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);

    x = 0;
    y = windH;
    zoom = 1.8;
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    point[0] = (windW / 2) - (image->sizeX / 2);
    point[1] = (windH / 2) - (image->sizeY / 2);
    point[2] = 0;
    glRasterPos3fv(point);

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glPixelZoom(1.0, 1.0);
    glDrawPixels(image->sizeX, image->sizeY, GL_RGB, GL_UNSIGNED_BYTE, image->data);

    point[0] = (float)x;
    point[1] = windH - (float)y;
    point[2] = 0.0;
    glRasterPos3fv(point);

    glPixelZoom(zoom, zoom);
    glCopyPixels((windW / 2) - (image->sizeX / 2), (windH / 2) - (image->sizeY / 2), image->sizeX, image->sizeY, GL_COLOR);

    glFlush();
}

void reshape(int width, int height)
{
    windW = width;
    windH = height;

    glViewport(0, 0, windW, windH);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, windW, 0, windH);	//窗口座標範圍, 2D
    glMatrixMode(GL_MODELVIEW);
}

void special(int key, int x, int y)
{
    switch (key)
    {
    case GLUT_KEY_UP:
        zoom += 0.2;
        glutPostRedisplay();
        break;
    case GLUT_KEY_DOWN:
        if (zoom >= 0.4)
        {
            zoom -= 0.2;
            glutPostRedisplay();
        }
        break;
    }
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 27:
        exit(0);
    }
}

void mouse(int button, int state, int mouseX, int mouseY)
{
    if (state == GLUT_DOWN)
    {
        x = mouseX;
        y = mouseY;
        glutPostRedisplay();
    }
}

static void Args(int argc, char** argv)
{
    GLint i;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-f") == 0)
        {
            if (i + 1 >= argc || argv[i + 1][0] == '-')
            {
                printf("-f (No file name).\n");
                exit(1);
            }
            else
            {
                image = rgbImageLoad(argv[++i]);
                if (image == NULL)
                {
                    printf("-f (bad file name).\n");
                    exit(1);
                }
            }
        }
    }
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    Args(argc, argv);

    if (image == NULL)
    {
        char* filename = "data//3.rgb";
        image = rgbImageLoad(filename);
    }

    if (image == NULL)
    {
        printf("No texture file.\n");
        exit(1);
    }

    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(windW, windH);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Copy Test");	//開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    glutSpecialFunc(special);       //設定callback function
    glutMouseFunc(mouse);           //設定callback function

    printf("先滑鼠點一下, 再按 上 下控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

