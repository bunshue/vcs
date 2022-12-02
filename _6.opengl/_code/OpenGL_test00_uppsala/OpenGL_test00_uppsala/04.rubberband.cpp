#include "../../Common.h"

#define RED 110
#define WHITE 111
#define SIZE 500

int transp_color;
GLint pt1x = 0, pt2x = 0, pt1y = 0, pt2y = 0;

void instructions();
void gfxinit();
void display(void);
void mouseFunc(int button, int state, int x, int y);
void mouseMoveFunc(int x, int y);

void instructions()
/* This function presents the instructions on how to use this program to the
   user. */
{
	printf("\nInstructions on using the rubberband program:\n");
	printf("   To create a rubberbanded area, press and drag the LEFT mouse button.\n");
	printf("   To clear the rubberbanded area, click the RIGHT mouse button.\n");
	printf("   To quit the program, choose CLOSE or EXIT from the window menu.\n");
}

void gfxinit()
/* This routine handles the initialization of the graphics. */
{
	/* Set window for normal plane. */

	glutSetColor(RED, 1.0, 0.0, 0.0);
	glClearIndex(RED);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	glutSetColor(WHITE, 1.0, 1.0, 1.0);

	/* Make sure we're drawing in the normal plane to begin with. */

	glutUseLayer(GLUT_NORMAL);
}

void display(void)
/* This is the function that gets executed when the normal display needs to be
   updated. */
{
	glClear(GL_COLOR_BUFFER_BIT);

	glIndexi(WHITE);
	glRecti(pt1x, pt1y, pt2x, pt2y);



	glRecti(-0.5, -0.5, 0.3, 0.3);
}

void mouseFunc(int button, int state, int x, int y)
/* This is the function that gets called whenever a mouse button event occurs. */
{
	switch (button)
	{
	case GLUT_LEFT_BUTTON:
		if (state == GLUT_DOWN)            /* left mouse button was pressed */
		{
			glIndexi(transp_color);       /* set color for clearing overlay */
			glRecti(pt1x, pt1y, pt2x, pt2y);              /* clear the existing box */
			pt2x = pt1x = x; 	              /* set corners of new rectangle to */
			pt2y = pt1y = SIZE - y;           /*       where mouse is            */
		}
		else			                     /* left mouse button was let go */
			glutUseLayer(GLUT_NORMAL);       /* rubberbanding finished; use */
		break;                               /*       normal draw plane     */
	case GLUT_RIGHT_BUTTON:
		if (state == GLUT_DOWN)           /* right mouse button was pressed */
		{
			glClearIndex(transp_color);                  /* set clear color */
			glClear(GL_COLOR_BUFFER_BIT);        /* clear the overlay plane */
		}
		break;
	}
}

void mouseMoveFunc(int x, int y)
/* This is the function that gets called whenever the mouse is moved. */
{
	glIndexi(transp_color);  		               /* set erase color */
	glRecti(pt1x, pt1y, pt2x, pt2y);            /* redraw the box to erase it */
	pt2x = x;  pt2y = SIZE - y;    /* set corner at current mouse position */
	glIndexi(WHITE);                          /* change to draw color */
	glRecti(pt1x, pt1y, pt2x, pt2y);                          /* draw new box */
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitWindowSize(SIZE, SIZE);
	glutInitWindowPosition(250, 300);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);

	glutCreateWindow("Rubberbanding");

	/* Present instructions to the user. */

	instructions();

	//transp_color = glutLayerGet(GLUT_TRANSPARENT_INDEX);
	transp_color = 3;
	glutUseLayer(GLUT_NORMAL);

	/* Register the callback functions. */

	glutDisplayFunc(display);   //設定callback function
	glutReshapeFunc(reshape0);   //設定callback function
	glutKeyboardFunc(keyboard0); //設定callback function

	glutMouseFunc(mouseFunc);		   /* callback for mouse button events */
	glutMotionFunc(mouseMoveFunc);	   /* callback for mouse drag events   */

	/* Set up initial graphics and enter the event handling loop. */

	gfxinit();

	glutMainLoop();	//開始主循環繪製

	return 0;
}




