/********************************************************************************
 * rotatingCube.c                                                               *
 * This program demonstrates a rotating cube with colored sides. It also        *
 * demonstrate use of homogeneous coordinate transformations and vertex arrays  *
 * for representing the cube from Chapter 4 of the Edward Angel computer        *
 * graphics text, from which this code has been adapted.                        *
 ********************************************************************************/

#include "../../Common.h"

 // Vertices of the cube, centered at the origin.
GLfloat vertices[][3] = { {-1.0,-1.0,-1.0}, {1.0,-1.0,-1.0}, {1.0,1.0,-1.0},
	{-1.0,1.0,-1.0}, {-1.0,-1.0,1.0}, {1.0,-1.0,1.0}, {1.0,1.0,1.0}, {-1.0,1.0,1.0} };

// Colors of the vertices.
GLfloat colors[][3] = { {0.0,0.0,0.0}, {1.0,0.0,0.0}, {1.0,1.0,0.0}, {0.0,1.0,0.0},
	{0.0,0.0,1.0}, {1.0,0.0,1.0}, {1.0,1.0,1.0}, {0.0,1.0,1.0} };

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] = { 0,3,2,1, 2,3,7,6, 0,4,7,3, 1,2,6,5, 4,5,6,7, 0,1,5,4 };

// Angles of rotation about each axis.
GLfloat theta[] = { 0.0, 0.0, 0.0 };

// Current axis of rotation.
GLint axis = 2;

int spinning = 0;

void colorcube(void);
void display(void);
void spinCube(void);
void mouse(int btn, int state, int x, int y);
void keyboard(unsigned char key, int x, int y);

// This function sets up the vertex arrays for the color cube and the projection matrix.
void colorcube(void)
{
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, colors);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);
}

// This is the display callback function.
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glRotatef(theta[0], 1.0, 0.0, 0.0);
	glRotatef(theta[1], 0.0, 1.0, 0.0);
	glRotatef(theta[2], 0.0, 0.0, 1.0);
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
	glutSwapBuffers();
}

// This function spins the cube around the current axis by incrementing the angle of
// rotation by 2 degrees.
void spinCube(void)
{
	if (spinning)
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

// This is the mouse callback function. It selects the axis to rotate around.
void mouse(int btn, int state, int x, int y)
{
	if (btn == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		axis = 0;
	}
	else if (btn == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
	{
		axis = 1;
	}
	else if (btn == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
	{
		axis = 2;
	}
	spinning = 1;
}

// This is the keyboard callback function. It starts and stops spinning.
void keyboard(unsigned char key, int x, int y)
{
	if (key == 's')
	{
		spinning = !spinning;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutInitWindowSize(600, 600);       // 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置

	glutCreateWindow("Rotating Color Cube");

	glutDisplayFunc(display);   //設定callback function
	glutReshapeFunc(reshape0);   //設定callback function
	//glutKeyboardFunc(keyboard0); //設定callback function
	glutKeyboardFunc(keyboard);
	glutIdleFunc(spinCube);
	glutMouseFunc(mouse);
	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);

	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
