/*****************************************************************************
 * teapot.cpp                                                                *
 *                                                                           *
 *     This program models the famous Utah teapot using Bezier patches.      *
 * OpenGL evaluators are used to draw the surfaces.                          *
 *****************************************************************************/

#include "../../Common.h"

#include <stdlib.h>
#include <GL/glut.h>
#include <iostream>
#include <fstream>
#include <conio.h>

/* Drawing constants. */
#define WINDOW_SIZE 540  /* initial size of window                    */
#define STEPS        10  /* number of steps to draw each segment over */
#define PATCHES      32  /* number of surfaces in the teapot          */
#define VERTICES    306  /* number of control points                  */


double points[VERTICES+1][3];
int patch_vertices[PATCHES][16];
static GLfloat theta[] = {270.0, 0.0, 180.0};

void interact (void);
void gfxinit (void);
void display (void);
void reshape (int width, int height);
void arrows (int key, int x, int y);

using namespace std;

void main (int argc, char** argv)
{
   /* Get input data. */

   interact ();

   /* Set graphics window parameters. */

   glutInit (&argc, argv);
   glutInitWindowSize (WINDOW_SIZE, WINDOW_SIZE);
   glutInitWindowPosition (100, 0);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
   glutCreateWindow ("Utah Teapot");
   glutDisplayFunc (display);
   glutReshapeFunc (reshape);
   glutSpecialFunc (arrows);
   gfxinit ();
   glutMainLoop ();
}


void gfxinit (void)
/* This is the routine that generates the image to be displayed. */
{
   int i, j, k, vertex;
   double coords[48], *p;

   glClearColor (1.0, 1.0, 1.0, 0.0); /* Make the background white. */
   glEnable (GL_MAP2_VERTEX_3);

    /* Generate the display lists for the surfaces. */

    for (k=0; k<PATCHES; k++)
    {
       for (i=0, p=coords; i<16; i++)
       {
          vertex = patch_vertices[k][i];
          for (j=0; j<3; j++, p++) *p = points[vertex][j];
       }
       glNewList (k+1, GL_COMPILE);
          glColor3d (0.0, 1.0, 0.0);
          glMap2d (GL_MAP2_VERTEX_3, 0.0, 1.0, 12, 4, 0.0, 1.0, 3, 4, coords);
          glMapGrid2d (STEPS, 0.0, 1.0, STEPS, 0.0, 1.0);
          glEvalMesh2 (GL_FILL, 0, STEPS, 0, STEPS);
       glEndList ();
    }
}

void reshape (int width, int height)
/* This is the callback function that gets executed every time the display
   size has changed. */
{
    glViewport (0, 0, width, height);
    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    if (width <= height)
       glOrtho (-4.0, 4.0, -4.0 * (GLdouble) height / (GLdouble) width,
                4.0 * (GLdouble) height / (GLdouble) width, -10.0, 10.0);
    else
       glOrtho (-4.0 * (GLdouble) width / (GLdouble) height,
                4.0 * (GLdouble) width / (GLdouble) height, -4.0, 4.0, -10.0, 10.0);
    glMatrixMode(GL_MODELVIEW);
}

void display (void)
/* This is the callback function that gets executed every time the display
   needs to be updated.
*/
{
   int i;

   glClear (GL_COLOR_BUFFER_BIT);
   glLoadIdentity();
   glRotatef(theta[0], 1.0, 0.0, 0.0);
   glRotatef(theta[1], 0.0, 1.0, 0.0);
   glRotatef(theta[2], 0.0, 0.0, 1.0);
   for (i=1; i<=PATCHES; i++) glCallList (i);
   glutSwapBuffers ();
}

void arrows (int key, int x, int y)
/* This function handles rotation via the arrow keys. */
{
   switch (key)
   {
      case GLUT_KEY_DOWN: /* rotate around the x-axis in a negative direction */
         theta[0] -= 2.0;
         if (theta[0] < 0.0) theta[0] += 360.0;
         break;
      case GLUT_KEY_UP: /* rotate around the x-axis in a positive direction */
         theta[0] += 2.0;
         if (theta[0] > 360.0) theta[0] -= 360.0;
         break;
      case GLUT_KEY_RIGHT: /* rotate around the z-axis in a negative direction */
         theta[2] -= 2.0;
         if (theta[2] < 0.0) theta[2] += 360.0;
         break;
      case GLUT_KEY_LEFT: /* rotate around the z-axis in a positive direction */
         theta[2] += 2.0;
         if (theta[2] > 360.0) theta[2] -= 360.0;
         break;
   }
   glutPostRedisplay ();
}

void interact (void)
/* This function gets the input data for the program to process. */
{
   ifstream patches_file, vertices_file;
   int i, j;

   /* Open data files. */

   patches_file.open ("teapot.patches", ios::in);
   if (patches_file.fail())
   {
      cerr << "File teapot.patches not found." << endl;
      exit (EXIT_FAILURE);
   }
   vertices_file.open ("teapot.vertices", ios::in);
   if (vertices_file.fail())
   {
      cerr << "File teapot.vertices not found." << endl;
      patches_file.close ();
      exit (EXIT_FAILURE);
   }

   /* Read files into arrays. */

   for (i=1; i<=VERTICES; i++)
      vertices_file >> points[i][0] >> points[i][1] >> points[i][2];
   for (i=0; i<PATCHES; i++)
      for (j=0; j<16; j++)
         patches_file >> patch_vertices[i][j];

   /* Close files. */

   vertices_file.close ();
   patches_file.close ();
}
