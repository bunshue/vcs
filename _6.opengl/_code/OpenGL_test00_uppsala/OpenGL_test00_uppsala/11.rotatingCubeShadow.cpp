/* Rotating cube with viewer movement and shadow from Chapter 5 */
/* Cube definition and display similar to rotating--cube program */

/* We use the Lookat function in the display callback to point
the viewer, whose position can be altered by the x,X,y,Y,z, and Z keys.
The perspective view is set in the reshape callback */

#include "../../Common.h"

// Vertices of the cube, centered at the origin.
GLfloat vertices[][3] = { {-1.0,1.0,-1.0}, {1.0,1.0,-1.0}, {1.0,3.0,-1.0},
	{-1.0,3.0,-1.0}, {-1.0,1.0,1.0}, {1.0,1.0,1.0}, {1.0,3.0,1.0}, {-1.0,3.0,1.0} };

// Colors of the vertices.
GLfloat colors[][3] = { {0.0,0.0,0.0}, {1.0,0.0,0.0}, {1.0,1.0,0.0}, {0.0,1.0,0.0},
	{0.0,0.0,1.0}, {1.0,0.0,1.0}, {1.0,1.0,1.0}, {0.0,1.0,1.0} };

// Shadow colors.
GLfloat shadowcolors[][3] = { {0.0,0.0,0.0}, {0.0,0.0,0.0}, {0.0,0.0,0.0}, {0.0,0.0,0.0},
{0.0,0.0,0.0}, {0.0,0.0,0.0}, {0.0,0.0,0.0}, {0.0,0.0,0.0} };

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] = { 0,3,2,1, 2,3,7,6, 0,4,7,3, 1,2,6,5, 4,5,6,7, 0,1,5,4 };

GLfloat theta[] = { 0.0, 0.0, 0.0 };   /* initial rotation angles      */
GLint axis = 1;                      /* initial axis of rotation     */
GLdouble viewer[] = { 5.0, 5.0, 5.0 }; /* initial viewer location      */
GLfloat light[3] = { 0.0, 10.0, 0.0 }; /* position of light            */
GLfloat m[16];                       /* shadow transformation matrix */
bool rotating = false;               /* rotating initially off       */

void colorcube(void);
void display(void);
void spinCube(void);
void mouse(int btn, int state, int x, int y);
void keys(unsigned char key, int x, int y);
void myReshape(int w, int h);

// This function sets up the vertex arrays for the color cube and initializes other graphics parameters.
void colorcube(void)
{
	// Color cube set up.

	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);

	// Graphics parameters set up.

	glClearColor(1.0, 1.0, 1.0, 0.0);  // set clear color to white
	for (int i = 0; i < 16; i++)
	{
		m[i] = 0.0;   // set up shadow projection matrix
	}
	m[0] = m[5] = m[10] = 1.0;
	m[7] = -1.0 / light[1];
}

// This function is the display callback. It draws the cube from the current viewing point.
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	/* Update viewer position in modelview matrix */

	glLoadIdentity();
	gluLookAt(viewer[0], viewer[1], viewer[2], 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

	/* Rotate cube */

	glRotatef(theta[0], 1.0, 0.0, 0.0);
	glRotatef(theta[1], 0.0, 1.0, 0.0);
	glRotatef(theta[2], 0.0, 0.0, 1.0);
	glTranslatef(0.0, -2.0, 0.0);

	/* Draw the cube */

	glColorPointer(3, GL_FLOAT, 0, colors);
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

	/* Draw the shadow */

	glPushMatrix();
	glTranslatef(light[0], light[1], light[2]);
	glMultMatrixf(m);
	glTranslatef(-light[0], -light[1], -light[2]);
	glColorPointer(3, GL_FLOAT, 0, shadowcolors);
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
	glPopMatrix();

	/* Swap display buffers */

	glutSwapBuffers();
}

/* This function is the idle callback. It spins the cube 2 degrees about the selected axis. */
void spinCube(void)
{
	if (rotating)
	{
		theta[axis] += 2.0;
		if (theta[axis] > 360.0)
		{
			theta[axis] -= 360.0;
		}
		glutPostRedisplay();
		sleep(25);
	}
}

/* This is the mouse callback function. The mouse buttons determine which axis to rotate about. */
void mouse(int btn, int state, int x, int y)
{
	if (btn == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		axis = 0;
		rotating = true;
	}
	if (btn == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
	{
		axis = 1;
		rotating = true;
	}
	if (btn == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
	{
		axis = 2;
		rotating = true;
	}
}

/* This is the keyboard callback function. Keys change the viewer's position as well as turn
   rotation on and off. */
void keys(unsigned char key, int x, int y)
{
	if (key == 'x')
	{
		viewer[0] -= 1.0;
	}
	if (key == 'X')
	{
		viewer[0] += 1.0;
	}
	if (key == 'y')
	{
		viewer[1] -= 1.0;
	}
	if (key == 'Y')
	{
		viewer[1] += 1.0;
	}
	if (key == 'z')
	{
		viewer[2] -= 1.0;
	}
	if (key == 'Z')
	{
		viewer[2] += 1.0;
	}
	if ((key == 's') || (key == 'S'))
	{
		rotating = !rotating;
	}
	glutPostRedisplay();
}

/* This is the reshape callback function. It produces a perspective projection of the cube. */
void myReshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(50.0, (double)w / (double)h, 2.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutInitWindowSize(600, 600);       // 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置

	glutCreateWindow("Color Cube with Shadow");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);   //設定callback function
	//glutReshapeFunc(reshape0);   //設定callback function
	//glutKeyboardFunc(keyboard0); //設定callback function
	glutReshapeFunc(myReshape);
	glutKeyboardFunc(keys);
	glutMouseFunc(mouse);
	glutIdleFunc(spinCube);

	glEnable(GL_DEPTH_TEST);
	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
