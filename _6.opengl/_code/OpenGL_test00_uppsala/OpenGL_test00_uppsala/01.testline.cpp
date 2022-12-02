/* This program demonstrates some very simple OpenGL graphics using the
   GLUT toolkit to interface with the windowing system. It is meant to
   serve as a template for the Computer Graphics students. The program
   simply draws a diagonal line across the window.
*/

#include "../../Common.h"

#define SIZE 500  /* the size, in pixels, of the square window to open */

void display (void);
void gfxinit (void);

void main (int argc, char **argv)
{
   glutInit (&argc, argv);
   glutInitWindowSize (SIZE, SIZE);
   glutInitWindowPosition (50, 100);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
   glutCreateWindow ("Test Line");
   glutDisplayFunc (display);
   gfxinit ();
   glutMainLoop ();
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

void gfxinit ()
/* This is the function that gets executed to draw the original graphic
   image.
*/
{
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   gluOrtho2D (0, SIZE-1, 0, SIZE-1);
   glNewList (1, GL_COMPILE);
      glBegin (GL_LINES);
         glVertex2i (0, 0);
         glVertex2i (SIZE-1, SIZE-1);
      glEnd ();
   glEndList ();
}
   
   
