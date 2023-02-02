/****************************************************************************
 * MandelbrotZoom.cpp                                                       *
 ****************************************************************************/

 // �L�� �ݻy�k

#include "../../Common.h"

double dx, dy, minX, minY, maxX, maxY;
int xmin, xmax, ymin, ymax;
int W;
int H;

void mouse(int button, int state, int x, int y)
{
	double xrange, yrange;
	int temp;

	/* This routine is the callback function for mouse events. */
	switch (button)
	{
	case GLUT_LEFT_BUTTON:
		if (state == GLUT_DOWN)  // start dragging
		{
			glEnable(GL_INDEX_LOGIC_OP);
			glLogicOp(GL_XOR);
			glIndexi(63);
			xmin = xmax = x;
			ymin = ymax = H - y;
		}
		else  // stop dragging; zoom in on selected region
		{
			glDisable(GL_INDEX_LOGIC_OP);
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
			maxX = minX + ((double)xmax / W) * xrange;
			minX = minX + ((double)xmin / W) * xrange;
			maxY = minY + ((double)ymax / H) * yrange;
			minY = minY + ((double)ymin / H) * yrange;
			glDeleteLists(1, 1);
			glClear(GL_COLOR_BUFFER_BIT);
			glFlush();
		}
	}
}

void motion(int x, int y)
{
	// This routine is the callback function for mouse drag events. It draws the rubberbanding triangle.
	glRecti(xmin, ymin, xmax, ymax);
	xmax = x;
	ymax = H - y;
	glRecti(xmin, ymin, xmax, ymax);

	glFlush();
}

// This is the callback function that gets executed every time the display needs to be updated.
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glCallList(1);
	glFlush();
}

// This is the function that gets executed to draw the original graphic image.
void gfxinit()
{
	glClearIndex(63);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0, W, 0, H);
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);

	glutInitWindowSize(600, 600);       // �]�w�����j�p
	glutInitWindowPosition(1100, 200);  // �]�w������m

	glutCreateWindow("OpenGL���� GLUT_INDEX");	//�}�ҵ��� ����ܥX���� Title

	glutDisplayFunc(display);   //�]�wcallback function
	glutReshapeFunc(reshape0);   //�]�wcallback function
	glutKeyboardFunc(keyboard0); //�]�wcallback function
	glutMouseFunc(mouse);		//�]�wcallback function
	glutMotionFunc(motion);		//�]�wcallback function

	gfxinit();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
