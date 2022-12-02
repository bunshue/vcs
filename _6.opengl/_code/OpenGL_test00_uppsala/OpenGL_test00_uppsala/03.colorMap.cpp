/*****************************************************************************
 *                                                                           *
 * This program demonstrates the color map in OpenGL and glut.               *
 *****************************************************************************/

#include "../../Common.h"

//#include <iostream>
//#include <stdlib.h>
//#include <GL/glut.h>

#define SIZE 300

void gfxinit ();
void display (void);

using namespace std;

void main (int argc, char** argv)
{
    /* Set graphics window parameters. */

    glutInit (&argc, argv);
    glutInitWindowSize (SIZE, SIZE);
    glutInitWindowPosition (200, 150);
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_INDEX);
    if (glutGet(GLUT_DISPLAY_MODE_POSSIBLE))
        cout << "Color index mode possible." << endl;
    else
    {
        cout << "Color index mode NOT possible." << endl;
        exit (-1);
    }
    glutCreateWindow ("Color Map");
    glutDisplayFunc (display);
    cout << "Number of bits in color index = " << glutGet (GLUT_WINDOW_BUFFER_SIZE) << endl;
    gfxinit ();
    glutMainLoop ();
}

void gfxinit ()
/* This is the routine that initializes some graphics parameters. */
{
    int i, index=0;

    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    gluOrtho2D (0.0, 8.0, 0.0, 2.0);
   
    /* Set the true colors in entries 10-17 for comparison. */

    glutSetColor (10, 0.0, 0.0, 0.0);  /* black   */
    glutSetColor (11, 1.0, 0.0, 0.0);  /* red     */
    glutSetColor (12, 0.0, 1.0, 0.0);  /* green   */
    glutSetColor (13, 1.0, 1.0, 0.0);  /* yellow  */
    glutSetColor (14, 0.0, 0.0, 1.0);  /* blue    */
    glutSetColor (15, 1.0, 0.0, 1.0);  /* magenta */
    glutSetColor (16, 0.0, 1.0, 1.0);  /* cyan    */
    glutSetColor (17, 1.0, 1.0, 1.0);  /* white   */

    /* Generate the colors on the screen. */

    glNewList (1, GL_COMPILE);
        /* default color map entries */
        for (i=0; i<8; i++, index++)
        {
            glIndexi (index); 
            cout << "Color " << index << " = (" << glutGetColor (index, GLUT_RED)
				 << ", " << glutGetColor (index, GLUT_GREEN) << ", "
				 << glutGetColor (index, GLUT_BLUE) << ")" << endl;
            glRecti (i, 0, i+1, 1);
        }
        /* loaded color map entries */
		index += 2;
        for (i=0; i<8; i++, index++)
        {
            glIndexi (index); 
            cout << "Color " << index << " = (" << glutGetColor (index, GLUT_RED)
				 << ", " << glutGetColor (index, GLUT_GREEN) << ", "
				 << glutGetColor (index, GLUT_BLUE) << ")" << endl;
            glRecti (i, 1, i+1, 2);
        }
    glEndList ();
}

void display (void)
/* This is the callback function that gets executed every time the display
   needs to be updated.
*/
{
    glClear (GL_COLOR_BUFFER_BIT);
    glCallList (1);
    glutSwapBuffers ();
}
