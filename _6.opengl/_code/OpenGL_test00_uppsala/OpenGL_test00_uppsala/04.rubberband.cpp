//�ƹ��ؿ�|���

#include "../../Common.h"

#define SIZE 600

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
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);

	glutUseLayer(GLUT_OVERLAY);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);	//�e�Ť߯x��

	glutUseLayer(GLUT_NORMAL);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
}

void overlayDisplay(void)
{
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
			glClear(GL_COLOR_BUFFER_BIT);        /* clear the overlay plane */
			glutUseLayer(GLUT_NORMAL);       /* return to normal draw plane */
		}
		break;
	}
}

// This is the function that gets called whenever the mouse is moved.
void motion(int x, int y)
{
	glRecti(pt1x, pt1y, pt2x, pt2y);            /* redraw the box to erase it */

	pt2x = x;
	pt2y = SIZE - y;    /* set corner at current mouse position */
	glRecti(pt1x, pt1y, pt2x, pt2y);                          /* draw new box */
}

int main(int argc, char** argv)
{
	const char* windowName = "Rubberbanding �ƹ��ؿ�|���";
	const char* message = "�ƹ��ؿ�|���, �ƹ������k��, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, SIZE, SIZE, 1100, 200, display, reshape0, keyboard0);

	instructions();

	glutEstablishOverlay();
	glutUseLayer(GLUT_NORMAL);

	glutMouseFunc(mouse);		//�]�wcallback function, callback for mouse button events
	glutMotionFunc(motion);		//�]�wcallback function, callback for mouse drag events

	glutOverlayDisplayFunc(overlayDisplay);/* callback for overlay plane   */

	gfxinit();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
