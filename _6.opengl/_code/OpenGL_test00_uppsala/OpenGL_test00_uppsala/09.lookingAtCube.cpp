/* This program is modified from the rotating cube program to demonstrate
   the synthetic camera approach to viewing a scene. 
*/

#include "../../Common.h"

//#include <stdlib.h>
//#include <GL/glut.h>


// Vertices of the cube, centered at the origin.
GLfloat vertices[][3] = { {-1.0,-1.0,-1.0}, {1.0,-1.0,-1.0}, {1.0,1.0,-1.0},
	{-1.0,1.0,-1.0}, {-1.0,-1.0,1.0}, {1.0,-1.0,1.0}, {1.0,1.0,1.0}, {-1.0,1.0,1.0} };

// Colors of the vertices.
GLfloat colors[][3] = { {0.0,0.0,0.0}, {1.0,0.0,0.0}, {1.0,1.0,0.0}, {0.0,1.0,0.0},
	{0.0,0.0,1.0}, {1.0,0.0,1.0}, {1.0,1.0,1.0}, {0.0,1.0,1.0} };

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] = {0,3,2,1, 2,3,7,6, 0,4,7,3, 1,2,6,5, 4,5,6,7, 0,1,5,4};

void colorcube(void);
void viewMenu (int code);
void display(void);
void myReshape(int w, int h);

void main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition (100, 50);
    glutCreateWindow("Color Cube");
    glutReshapeFunc(myReshape);
    glutDisplayFunc(display);
	glEnable(GL_DEPTH_TEST); 
    colorcube ();

    /* Create menu for changing views. */

    glutCreateMenu (viewMenu);
    glutAddMenuEntry ("Positive x-axis", 1);
    glutAddMenuEntry ("Negative x-axis", 2);
    glutAddMenuEntry ("Positive y-axis", 3);
    glutAddMenuEntry ("Negative y-axis", 4);
    glutAddMenuEntry ("Positive z-axis", 5);
    glutAddMenuEntry ("Negative z-axis", 6);
    glutAttachMenu (GLUT_RIGHT_BUTTON);

    /* Set initial view to positive x-axis. */

    glMatrixMode (GL_MODELVIEW);
    glLoadIdentity ();
    gluLookAt (2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

    /* Enter glut event loop. */

    glutMainLoop();
}

// This function sets up the vertex arrays for the color cube.
void colorcube(void)
{
	glEnableClientState (GL_COLOR_ARRAY);
	glEnableClientState (GL_VERTEX_ARRAY);
	glVertexPointer (3, GL_FLOAT, 0, vertices);
	glColorPointer (3, GL_FLOAT, 0, colors);
}

// This function handles the menu choices during the program's execution. The menu choices
// change the view in which the cube is seen.
void viewMenu (int code)
{
    switch (code)
    {
    case 1: /* positive x-axis */
        glLoadIdentity ();
        gluLookAt (2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 2: /* negative x-axis */
        glLoadIdentity ();
        gluLookAt (-2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 3: /* positive y-axis */
        glLoadIdentity ();
        gluLookAt (0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0);
        break;
    case 4: /* negative y-axis */
        glLoadIdentity ();
        gluLookAt (0.0, -2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
        break;
    case 5: /* positive z-axis */
        glLoadIdentity ();
        gluLookAt (0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 6: /* negative z-axis */
        glLoadIdentity ();
        gluLookAt (0.0, 0.0, -2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    }
    glutPostRedisplay ();
}

// This function is the display callback. It draws the cube from the current viewing point.
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glDrawElements (GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
	glutSwapBuffers();
}

// This is the reshape callback function. It resets the viewport to the entire window and
// the projection matrix to keep the cube centered in the window.
void myReshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
        glOrtho(-2.0, 2.0, -2.0 * (GLfloat) h / (GLfloat) w,
            2.0 * (GLfloat) h / (GLfloat) w, 1.0, 5.0);
    else
        glOrtho(-2.0 * (GLfloat) w / (GLfloat) h,
            2.0 * (GLfloat) w / (GLfloat) h, -2.0, 2.0, 1.0, 5.0);
    glMatrixMode(GL_MODELVIEW);
}
