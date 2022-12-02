/****************************************************************************
 * rubberband.c                                                             *
 *                                                                          *
 *    This program demonstrates rubberbanding. It uses OpenGL graphics with *
 * the GLUT interface. The program is also a good demonstration of overlay  *
 * planes and event callbacks.                                              *
 ****************************************************************************/

#include "../../Common.h"

//#include <stdio.h>
//#include <stdlib.h>
//#include <GL/glut.h>

#define RED 110
#define WHITE 111
#define SIZE 500

int transp_color;
GLint x1=0, x2=0, y1=0, y2=0;

void instructions ();
void gfxinit ();
void display (void);
void overlayDisplay (void);
void mouseFunc (int button, int state, int x, int y);
void mouseMoveFunc (int x, int y);

void main (int argc, char** argv)
{
   /* Initialize window parameters. In order to use an overlay plane, the
      window needs to be single buffered and use a color index. */

   glutInit (&argc, argv);
   glutInitWindowSize (SIZE, SIZE);
   glutInitWindowPosition (250, 300);
   glutInitDisplayMode (GLUT_SINGLE | GLUT_INDEX);
   if (!glutGet (GLUT_DISPLAY_MODE_POSSIBLE))
   {
       printf ("Color index mode not supported.\n");
       exit (1);
   }
   
   /* Create window and make sure an overlay is possible. If it's not, exit the program. */

   glutCreateWindow ("Rubberbanding");
   if (!glutLayerGet (GLUT_OVERLAY_POSSIBLE))
   {
      printf ("No overlay possible.\n");
      exit (1);
   }

   /* Present instructions to the user. */

   instructions ();

   /* Establish the overlay, get its transparent color index, and make sure
      we're using the normal plane to begin with. */

   glutEstablishOverlay ();
   transp_color = glutLayerGet (GLUT_TRANSPARENT_INDEX);
   glutUseLayer (GLUT_NORMAL);

   /* Register the callback functions. */

   glutDisplayFunc (display);		       /* callback for normal plane    */
   glutOverlayDisplayFunc (overlayDisplay);/* callback for overlay plane   */
   glutMouseFunc (mouseFunc);		   /* callback for mouse button events */
   glutMotionFunc (mouseMoveFunc);	   /* callback for mouse drag events   */

   /* Set up initial graphics and enter the event handling loop. */

   gfxinit ();
   glutMainLoop ();
}

void instructions ()
/* This function presents the instructions on how to use this program to the
   user. */
{
   printf ("\nInstructions on using the rubberband program:\n");
   printf ("   To create a rubberbanded area, press and drag the LEFT mouse button.\n");
   printf ("   To clear the rubberbanded area, click the RIGHT mouse button.\n");
   printf ("   To quit the program, choose CLOSE or EXIT from the window menu.\n");
}

void gfxinit ()
/* This routine handles the initialization of the graphics. */
{
   /* Set window for normal plane. */

   glutSetColor (RED, 1.0, 0.0, 0.0);
   glClearIndex (RED);
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   gluOrtho2D (0.0, SIZE - 1, 0.0, SIZE - 1);

   /* Set window for overlay plane. Make sure rubberbanding rectangle is drawn
      in outline only and that the outline color is white. */

   glutUseLayer (GLUT_OVERLAY);
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   gluOrtho2D (0.0, SIZE - 1, 0.0, SIZE - 1);
   glPolygonMode (GL_FRONT_AND_BACK, GL_LINE);
   glutSetColor (WHITE, 1.0, 1.0, 1.0);

   /* Make sure we're drawing in the normal plane to begin with. */

   glutUseLayer (GLUT_NORMAL);
}

void display (void)
/* This is the function that gets executed when the normal display needs to be
   updated. */
{
   glClear (GL_COLOR_BUFFER_BIT);
}

void overlayDisplay (void)
/* This is the function that gets executed when the overlay needs to be
   updated. */
{
   glIndexi (WHITE);
   glRecti (x1, y1, x2, y2);
}

void mouseFunc (int button, int state, int x, int y)
/* This is the function that gets called whenever a mouse button event occurs. */
{
   switch (button)
   {
      case GLUT_LEFT_BUTTON:
         if (state == GLUT_DOWN)            /* left mouse button was pressed */
		 {
	        glutUseLayer (GLUT_OVERLAY); /* start rubberbanding; use overlay */
	        glIndexi (transp_color);       /* set color for clearing overlay */
	        glRecti (x1, y1, x2, y2);              /* clear the existing box */
	        x2 = x1 = x; 	              /* set corners of new rectangle to */
	        y2 = y1 = SIZE - y;           /*       where mouse is            */
		 }
	     else			                     /* left mouse button was let go */
	        glutUseLayer (GLUT_NORMAL);       /* rubberbanding finished; use */
	     break;                               /*       normal draw plane     */
      case GLUT_RIGHT_BUTTON:
	     if (state == GLUT_DOWN)           /* right mouse button was pressed */
		 {
	        glutUseLayer (GLUT_OVERLAY);              /* go to overlay plane */
	        glClearIndex (transp_color);                  /* set clear color */
	        glClear (GL_COLOR_BUFFER_BIT);        /* clear the overlay plane */
	        glutUseLayer (GLUT_NORMAL);       /* return to normal draw plane */
		 }
	     break;
   }
}

void mouseMoveFunc (int x, int y)
/* This is the function that gets called whenever the mouse is moved. */
{
   glIndexi (transp_color);  		               /* set erase color */
   glRecti (x1, y1, x2, y2);            /* redraw the box to erase it */
   x2 = x;  y2 = SIZE - y;    /* set corner at current mouse position */
   glIndexi (WHITE);                          /* change to draw color */
   glRecti (x1, y1, x2, y2);                          /* draw new box */
}
