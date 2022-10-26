#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include "rgb.h"

GLenum doubleBuffer;
GLint windW = 600;
GLint windH = 600;

RGBImageRec* image = NULL;
float point[3];
float zoom;
GLint x, y;

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

    if (doubleBuffer)
    {
        glutSwapBuffers();
    }
    else
    {
        glFlush();
    }
}

void reshape(int width, int height)
{
    windW = width;
    windH = height;

    glViewport(0, 0, windW, windH);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, windW, 0, windH);
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
        zoom -= 0.2;
        if (zoom < 0.2)
        {
            zoom = 0.2;
        }
        glutPostRedisplay();
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

    doubleBuffer = GL_FALSE;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-sb") == 0)
        {
            doubleBuffer = GL_FALSE;
        }
        else if (strcmp(argv[i], "-db") == 0)
        {
            doubleBuffer = GL_TRUE;
        }
        else if (strcmp(argv[i], "-f") == 0)
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
    GLenum type;

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

    type = GLUT_RGB;
    type |= (doubleBuffer) ? GLUT_DOUBLE : GLUT_SINGLE;
    glutInitDisplayMode(type);
    glutInitWindowSize(windW, windH);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Copy Test");	//�}�ҵ��� ����ܥX���� Title

    Init();

    glutDisplayFunc(display);       //�]�wcallback function
    glutReshapeFunc(reshape);       //�]�wcallback function
    glutKeyboardFunc(keyboard);     //�]�wcallback function
    glutSpecialFunc(special);       //�]�wcallback function
    glutMouseFunc(mouse);           //�]�wcallback function

    printf("�� �W �U����\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

