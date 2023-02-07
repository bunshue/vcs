/****************************************************************************
 * bilinear.cpp                                                             *
 *    This graphics program constructs a bilinear patch for a surface       *
 * defined by four corners.                                                 *
 * NOTE:  At this time the z component of the surface is ignored, giving a  *
 *        parallel projection onto the x,y-plane, which is assumed to be    *
 *        the display device.                                               *
 ****************************************************************************/

#include "../../Common.h"

float x[2][2];
float y[2][2];
float z[2][2];  //�S�Ψ�, �w�d

void gfxinit(void)
{
    float u, u1, v, v1, x1, y1, x2, y2;

    /* Initialize graphics mode.  Assume all coordinates are in [-10,10]. */

    glClearColor(1.0, 1.0, 1.0, 0.0);  //�I���զ�
    glColor3f(1.0, 0.0, 0.0);          //�e���u
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-10.0, 10.0, -10.0, 10.0);   //�]�w�e����� x= -10 ~ 10, y = -10 ~ 10

    //�b List 1 �s�@��1�i��
    glNewList(1, GL_COMPILE);

    /* Draw the rulings of u (constant u values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    glBegin(GL_LINES);
    for (u = 0.0f; u < 1.001f; u += 0.1f)
    {
        u1 = 1.0f - u;
        x1 = u1 * x[0][0] + u * x[1][0];
        y1 = u1 * y[0][0] + u * y[1][0];
        x2 = u1 * x[0][1] + u * x[1][1];
        y2 = u1 * y[0][1] + u * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }

    /* Draw the rulings of v (constant v values) at values of 0.0, 0.1, 0.2, ..., 1.0. */

    for (v = 0.0f; v < 1.001f; v += 0.1f)
    {
        v1 = 1.0f - v;
        x1 = v1 * x[0][0] + v * x[0][1];
        y1 = v1 * y[0][0] + v * y[0][1];
        x2 = v1 * x[1][0] + v * x[1][1];
        y2 = v1 * y[1][0] + v * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }
    glEnd();

    glEndList();
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 1.0, 0.0);          //�e���u
    glCallList(1);  //��ܲ�1�i��

    draw_coordinates(8.0f);     //�e�y�жb

    //�� GL_LINE_LOOP �e�@�ӪŤ߯x��
    glColor3f(0.0, 1.0, 0.0);          //�e���
    float dd = 8.2f;
    float point1[3] = { -dd, -dd, 0 };	//���U
    float point2[3] = { dd, -dd, 0 };	//�k�U
    float point3[3] = { dd,  dd, 0 };	//�k�W
    float point4[3] = { -dd,  dd, 0 };	//���W
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//���U
    glVertex3fv(point2);	//�k�U
    glVertex3fv(point3);	//�k�W
    glVertex3fv(point4);	//���W
    glEnd();

    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    //�Ĥ@���u���_�I, ���U
    x[0][0] = -8;
    y[0][0] = -8;
    z[0][0] = -85;   //z������

    //�Ĥ@���u�����I, �k�U
    x[0][1] = 8;
    y[0][1] = -3;
    z[0][1] = 85;    //z������

    //�ĤG���u���_�I, ���W
    x[1][0] = -8;
    y[1][0] = 8;
    z[1][0] = 25;    //z������

    //�ĤG���u�����I, �k�W
    x[1][1] = 8;
    y[1][1] = 3;
    z[1][1] = -35;   //z������

    const char* windowName = "Bilinear Patch";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    gfxinit();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
