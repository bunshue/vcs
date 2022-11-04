#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../../Common.h"

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#define OPENGL_WIDTH 24
#define OPENGL_HEIGHT 13

GLenum rgb;

//boxA��m, ��
float boxA[3] =
{
    0, 0, 0
};

//boxB��m, ��
float boxB[3] =
{
    -100, 0, 0
};

//boxC��m, �k
float boxC[3] =
{
    100, 0, 0
};

//boxD��m, �W
float boxD[3] =
{
    0, 95, 0
};

//boxE��m, �U
float boxE[3] =
{
    0, -105, 0
};

GLubyte OpenGL_bits1[] =
{
   0x00, 0x03, 0x00,
   0x7f, 0xfb, 0xff,
   0x7f, 0xfb, 0xff,
   0x00, 0x03, 0x00,
   0x3e, 0x8f, 0xb7,
   0x63, 0xdb, 0xb0,
   0x63, 0xdb, 0xb7,
   0x63, 0xdb, 0xb6,
   0x63, 0x8f, 0xf3,
   0x63, 0x00, 0x00,
   0x63, 0x00, 0x00,
   0x63, 0x00, 0x00,
   0x3e, 0x00, 0x00,
};

GLubyte OpenGL_bits2[] =
{
   0x00, 0x00, 0x00,
   0xff, 0xff, 0x01,
   0xff, 0xff, 0x01,
   0x00, 0x00, 0x00,
   0xf9, 0xfc, 0x01,
   0x8d, 0x0d, 0x00,
   0x8d, 0x0d, 0x00,
   0x8d, 0x0d, 0x00,
   0xcc, 0x0d, 0x00,
   0x0c, 0x4c, 0x0a,
   0x0c, 0x4c, 0x0e,
   0x8c, 0xed, 0x0e,
   0xf8, 0x0c, 0x00,
};

GLubyte logo_bits[] =
{
   0x00, 0x66, 0x66,
   0xff, 0x66, 0x66,
   0x00, 0x00, 0x00,
   0xff, 0x3c, 0x3c,
   0x00, 0x42, 0x40,
   0xff, 0x42, 0x40,
   0x00, 0x41, 0x40,
   0xff, 0x21, 0x20,
   0x00, 0x2f, 0x20,
   0xff, 0x20, 0x20,
   0x00, 0x10, 0x90,
   0xff, 0x10, 0x90,
   0x00, 0x0f, 0x10,
   0xff, 0x00, 0x00,
   0x00, 0x66, 0x66,
   0xff, 0x66, 0x66,
};

void Init(void)
{
    if (!rgb)
    {
        glutSetColor(0, 0.0, 0.0, 0.0);
        glutSetColor(1, 1.0, 0.0, 0.0);
        glutSetColor(2, 0.0, 1.0, 0.0);
        glutSetColor(3, 1.0, 1.0, 0.0);
        glutSetColor(4, 0.0, 0.0, 1.0);
        glutSetColor(5, 1.0, 0.0, 1.0);
        glutSetColor(6, 0.0, 1.0, 1.0);
        glutSetColor(7, 1.0, 1.0, 1.0);
    }

    glClearColor(0.0, 0.0, 0.0, 0.0);   //�¦�
    glClearIndex(0.0);
}

void display(void)
{
    float x_st = 0.0f;
    float y_st = 0.0f;

    glClear(GL_COLOR_BUFFER_BIT);

    glRasterPos3fv(boxA);   //�]�w��m, ��
    glPixelStorei(GL_UNPACK_ROW_LENGTH, 24);
    glPixelStorei(GL_UNPACK_SKIP_PIXELS, 8);
    glPixelStorei(GL_UNPACK_SKIP_ROWS, 2);
    glPixelStorei(GL_UNPACK_LSB_FIRST, GL_FALSE);
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glBitmap(16, 12, 8.0, 0.0, 0.0, 0.0, logo_bits);

    glPixelStorei(GL_UNPACK_ROW_LENGTH, 0);
    glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0);
    glPixelStorei(GL_UNPACK_SKIP_ROWS, 0);
    glPixelStorei(GL_UNPACK_LSB_FIRST, GL_TRUE);
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

    //                Red
    (rgb) ? glColor3f(1.0, 0.0, 0.0) : glIndexi(7);
    glRasterPos3fv(boxB);   //�]�w��m, ��
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits1);
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits2);

    //                Green
    (rgb) ? glColor3f(0.0, 1.0, 0.0) : glIndexi(6);
    glRasterPos3fv(boxC);   //�]�w��m, �k
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits1);
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits2);

    //                Blue
    (rgb) ? glColor3f(0.0, 0.0, 1.0) : glIndexi(5);
    glRasterPos3fv(boxD);   //�]�w��m, �W
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits1);
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits2);

    //                Yellow
    (rgb) ? glColor3f(1.0, 1.0, 0.0) : glIndexi(3);
    glRasterPos3fv(boxE);   //�]�w��m, �U
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits1);
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, OPENGL_WIDTH, 0.0, OPENGL_WIDTH, 0.0, OpenGL_bits2);

    glFlush();
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-125, 125, -125, 125);   //���f�y�нd��, 2D	//��ܽd�� x(-125 ~ 125), y(-125 ~ 125)
    glMatrixMode(GL_MODELVIEW);
}

void Args(int argc, char** argv)
{
    GLint i;

    rgb = GL_TRUE;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-ci") == 0)
        {
            rgb = GL_FALSE;
        }
        else if (strcmp(argv[i], "-rgb") == 0)
        {
            rgb = GL_TRUE;
        }
    }
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);
    Args(argc, argv);

    //���PRGB�Ҧ�, �ݰ_�Ӥ��@��

    type = (rgb) ? GLUT_RGB : GLUT_INDEX;
    type |= GLUT_SINGLE;
    glutInitDisplayMode(type);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Bitmap Test");	//�}�ҵ��� ����ܥX���� Title

    Init();

    glutDisplayFunc(display);       //�]�wcallback function
    glutReshapeFunc(reshape);       //�]�wcallback function
    glutKeyboardFunc(keyboard0);     //�]�wcallback function

    printf("�����, �L����, �� Esc ���}\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
