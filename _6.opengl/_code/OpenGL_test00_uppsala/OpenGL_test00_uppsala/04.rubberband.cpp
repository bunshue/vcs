//滑鼠框選四邊形

#include "../../Common.h"

#define RED 110
#define WHITE 111
#define SIZE 500

int transp_color;
GLint pt1x = 0;
GLint pt2x = 0;
GLint pt1y = 0;
GLint pt2y = 0;

// This function presents the instructions on how to use this program to the user.
void instructions()
{
	printf("\nInstructions on using the rubberband program:\n");
	printf("   To create a rubberbanded area, press and drag the LEFT mouse button.\n");
	printf("   To clear the rubberbanded area, click the RIGHT mouse button.\n");
	printf("   To quit the program, choose CLOSE or EXIT from the window menu.\n");
}

// This routine handles the initialization of the graphics.
void gfxinit()
{
	/* Set window for normal plane. */

	glutSetColor(RED, 1.0, 0.0, 0.0);
	glClearIndex(RED);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);

	/* Set window for overlay plane. Make sure rubberbanding rectangle is drawn
	   in outline only and that the outline color is white. */

	glutUseLayer(GLUT_OVERLAY);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	glutSetColor(WHITE, 1.0, 1.0, 1.0);

	/* Make sure we're drawing in the normal plane to begin with. */

	glutUseLayer(GLUT_NORMAL);
}

// This is the function that gets executed when the normal display needs to be updated.
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
}

void overlayDisplay(void)
{
	glIndexi(WHITE);
	glRecti(pt1x, pt1y, pt2x, pt2y);
}

// This is the function that gets called whenever a mouse button event occurs.
void mouse(int button, int state, int x, int y)
{
	switch (button)
	{
	case GLUT_LEFT_BUTTON:
		if (state == GLUT_DOWN)            /* left mouse button was pressed */
		{
			glutUseLayer(GLUT_OVERLAY); /* start rubberbanding; use overlay */
			glIndexi(transp_color);       /* set color for clearing overlay */
			glRecti(pt1x, pt1y, pt2x, pt2y);              /* clear the existing box */
			pt2x = pt1x = x; 	              /* set corners of new rectangle to */
			pt2y = pt1y = SIZE - y;           /*       where mouse is            */
		}
		else			                     /* left mouse button was let go */
		{
			glutUseLayer(GLUT_NORMAL);       /* rubberbanding finished; use */
		}
		break;                               /*       normal draw plane     */
	case GLUT_RIGHT_BUTTON:
		if (state == GLUT_DOWN)           /* right mouse button was pressed */
		{
			glutUseLayer(GLUT_OVERLAY);              /* go to overlay plane */
			glClearIndex((float)transp_color);                  /* set clear color */
			glClear(GL_COLOR_BUFFER_BIT);        /* clear the overlay plane */
			glutUseLayer(GLUT_NORMAL);       /* return to normal draw plane */
		}
		break;
	}
}

// This is the function that gets called whenever the mouse is moved.
void motion(int x, int y)
{
	glIndexi(transp_color);  		               /* set erase color */
	glRecti(pt1x, pt1y, pt2x, pt2y);            /* redraw the box to erase it */

	pt2x = x;
	pt2y = SIZE - y;    /* set corner at current mouse position */
	glIndexi(WHITE);                          /* change to draw color */
	glRecti(pt1x, pt1y, pt2x, pt2y);                          /* draw new box */
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);
	glutInitWindowSize(SIZE, SIZE);       // 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置


	glutCreateWindow("Rubberbanding 滑鼠框選四邊形");

	instructions();

	glutEstablishOverlay();
	//transp_color = glutLayerGet(GLUT_TRANSPARENT_INDEX);
	transp_color = 3;
	glutUseLayer(GLUT_NORMAL);

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape0);	//設定callback function
	glutKeyboardFunc(keyboard0);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function, callback for mouse button events
	glutMotionFunc(motion);		//設定callback function, callback for mouse drag events

	glutOverlayDisplayFunc(overlayDisplay);/* callback for overlay plane   */

	gfxinit();

	printf("\n滑鼠框選四邊形, 滑鼠分左右鍵\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}

