/****************************************************************************
 * bilinear.cpp                                                             *
 *                                                                          *
 *    This graphics program constructs a bilinear patch for a surface       *
 * defined by four corners.                                                 *
 *                                                                          *
 * NOTE:  At this time the z component of the surface is ignored, giving a  *
 *        parallel projection onto the x,y-plane, which is assumed to be    *
 *        the display device.                                               *
 ****************************************************************************/

#include "../../Common.h"

 //#include <iostream>
 //#include <GL/glut.h>

float x[2][2], y[2][2], z[2][2];

void input(void);
void gfxinit(void);
void display(void);

void input(void)
{
    cout << "Bilinear Patches" << endl << endl;
    cout << "Please enter the four points in the following sequence." << endl;
    cout << "The first two points define the v=0 edge and the last two points" << endl;
    cout << "define the v=1 edge." << endl << endl;
    cout << "Enter coordinates of p[0][0]:  ";
    cin >> x[0][0] >> y[0][0] >> z[0][0];
    cout << "Enter coordinates of p[1][0]:  ";
    cin >> x[1][0] >> y[1][0] >> z[1][0];
    cout << "Enter coordinates of p[0][1]:  ";
    cin >> x[0][1] >> y[0][1] >> z[0][1];
    cout << "Enter coordinates of p[1][1]:  ";
    cin >> x[1][1] >> y[1][1] >> z[1][1];
}

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

    /* Draw the rulings of u (constant u values) at values of 0.0, 0.1, 0.2,
       ..., 1.0. */

    glBegin(GL_LINES);
    for (u = 0.0; u < 1.001; u += 0.1)
    {
        u1 = 1.0 - u;
        x1 = u1 * x[0][0] + u * x[1][0];   y1 = u1 * y[0][0] + u * y[1][0];
        x2 = u1 * x[0][1] + u * x[1][1];   y2 = u1 * y[0][1] + u * y[1][1];
        glVertex2f(x1, y1);
        glVertex2f(x2, y2);
    }

    /* Draw the rulings of v (constant v values) at values of 0.0, 0.1, 0.2,
       ..., 1.0. */

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
/* This is the callback function that gets executed every time the display
   needs to be updated.
*/
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glutSwapBuffers();
}

int main(int argc, char** argv)
{
    /* Get input values from user. */

    input();

    /* Set graphics window parameters. */

    glutInit(&argc, argv);

    glutInitWindowSize(400, 400);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

    glutCreateWindow("Bilinear Patch");

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}


