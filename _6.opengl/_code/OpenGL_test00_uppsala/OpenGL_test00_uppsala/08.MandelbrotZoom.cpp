/****************************************************************************
 * MandelbrotZoom.cpp                                                       *
 *                                                                          *
 *    This program draws a color Mandelbrot Set. It allows defining a       *
 * region to zoom in on using rubberbanding.                                *
 ****************************************************************************/

#include "../../Common.h"

#include <math.h>
#include <iostream>
#include <strstream>
#include <stdlib.h>
#include <GL/glut.h>

double dx, dy, minX, minY, maxX, maxY;
GLushort *points;
int maxIterations, size, xmin, xmax, ymin, ymax, color_size;

void display (void);
void gfxinit (void);
void change_colors (int ncolors);
GLushort zSqrPointColor (double cx, double cy);
void interact (void);
void calcMandelbrot ();
void mouseFunc (int button, int state, int x, int y);
void mouseMove (int x, int y);

using namespace std;

void main (int argc, char **argv)
{
   strstream title;

   /* Get user input parameters for generating the Mandelbrot set. */

   interact ();
   title << "Mandelbrot Set - " << maxIterations << " Iterations";
 
   /* Set graphics window characteristics and open the window. */

   glutInit (&argc, argv);
   glutInitWindowSize (size, size);
   glutInitWindowPosition (100, 50);
   glutInitDisplayMode (GLUT_SINGLE | GLUT_INDEX);
   glutCreateWindow (title.str());
   glutDisplayFunc (display);
   glutMouseFunc (mouseFunc);
   glutMotionFunc (mouseMove);
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
   glFlush ();
}

void gfxinit ()
/* This is the function that gets executed to draw the original graphic
   image.
*/
{
   color_size = glutGet (GLUT_WINDOW_COLORMAP_SIZE) - 64;
   if (maxIterations > color_size)
   {
      cout << endl <<"Can't display " << maxIterations << " colors. MaxIterations changed to "
		   << color_size << "." << endl;
      maxIterations = color_size;
   }
   change_colors (maxIterations);
   glClearIndex (63);
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   gluOrtho2D (0, size, 0, size);
   calcMandelbrot ();
   glPolygonMode (GL_FRONT_AND_BACK, GL_LINE);
}
 
void change_colors (int ncolors)
/* This routine changes the colormap to equally spaced colors. */
{
   double incr=330.0/ncolors, f, h, s=1.0;
   int ih, i;
   GLfloat p1, p2, p3, v=1.0;

   glutSetColor (63, 1, 1, 1);
   for (i=64, h=0.0; i<64+ncolors; i++, h+=incr)
   {
      ih = (int) (h/60.0); 
      f = h/60.0 - ih;
      p1 = v * (1 - s);
      p2 = v * (1 - s * f);
      p3 = v * (1 - s * (1 - f));
      switch (ih)
		{
		case 0 : glutSetColor (i, v, p3, p1);  break;
		case 1 : glutSetColor (i, p2, v, p1);  break;
		case 2 : glutSetColor (i, p1, v, p3);  break;
		case 3 : glutSetColor (i, p1, p2, v);  break;
		case 4 : glutSetColor (i, p3, p1, v);  break;
		case 5 : glutSetColor (i, v, p1, p2);  break;
		}
   }
}

GLushort zSqrPointColor (double cx, double cy)
/* This routine determines the color to place at point (x, y) for the 
   iteration F(z) = z^2 + c. */
{
   GLushort i;
   double newzx, newzy, x, y;
   
   x = y = 0.0;
   for (i=0; i<maxIterations; i++)
   {
      newzx = x*x - y*y + cx;
      newzy = 2*x*y + cy;
      if (newzx*newzx+newzy*newzy>4) return 64+i;
      x = newzx;
      y = newzy;
   }
   return (0);  /* Black */
}

void interact (void)
{
   cout << endl <<"How many iterations to test for convergence?  ";
   cin >> maxIterations;
   minX = -2.1;   maxX = 0.6;
   minY = -1.35;   maxY = 1.35;
   cout << "How many pixels wide do you want the image?  ";
   cin >> size;
   points = (GLushort *) calloc (size*size, sizeof(GLushort));
}

void calcMandelbrot ()
{
   /* This routine calculates the points to be displayed. */

   double x, y;
   int i, j;
   GLushort *p;

   dx = (maxX - minX) / (size - 1);
   dy = (maxY - minY) / (size - 1);
   for (j=0, y=minY, p=points; j<size; j++, y+=dy)
      for (i=0, x=minX; i<size; i++, x+=dx, p++) *p = zSqrPointColor (x, y);
   glNewList (1, GL_COMPILE);
      glDrawPixels (size, size, GL_COLOR_INDEX, GL_UNSIGNED_SHORT, points);
   glEndList ();
}

void mouseFunc (int button, int state, int x, int y)
{
	double xrange, yrange;
	int temp;
	strstream title;

	/* This routine is the callback function for mouse events. */

	switch (button)
	{
	case GLUT_LEFT_BUTTON:
		if (state == GLUT_DOWN)  // start dragging
		{
			glEnable (GL_INDEX_LOGIC_OP);
			glLogicOp (GL_XOR);
			glIndexi (63);
			xmin = xmax = x;
			ymin = ymax = size - y;
		}
		else  // stop dragging; zoom in on selected region
		{
			glDisable (GL_INDEX_LOGIC_OP);
			xrange = maxX - minX;
			yrange = maxY - minY;
			if (xmax < xmin)
			{
				temp = xmax; xmax = xmin; xmin = temp;
			}
			if (ymax < ymin)
			{
				temp = ymax; ymax = ymin; ymin = temp;
			}
			maxX = minX + ((double)xmax / size) * xrange;
			minX = minX + ((double)xmin / size) * xrange;
			maxY = minY + ((double)ymax / size) * yrange;
			minY = minY + ((double)ymin / size) * yrange;
			glDeleteLists (1, 1);
			glClear (GL_COLOR_BUFFER_BIT);
			glFlush ();
			if (maxIterations < color_size - 20)
				maxIterations += 20;
			else
				maxIterations = color_size;
			change_colors (maxIterations);
			calcMandelbrot ();
			title << "Mandelbrot Set - " << maxIterations << " Iterations";
			glutSetWindowTitle (title.str());
			glutPostRedisplay ();
		}
	}
}

void mouseMove (int x, int y)
{
	/* This routine is the callback function for mouse drag events. It draws the
	   rubberbanding triangle. */

	glRecti (xmin, ymin, xmax, ymax);
	xmax = x;
	ymax = size - y;
	glRecti (xmin, ymin, xmax, ymax);
	glFlush ();
}

