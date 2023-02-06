/********************************************************************************
 * rotatingCube.c                                                               *
 * This program demonstrates a rotating cube with colored sides. It also        *
 * demonstrate use of homogeneous coordinate transformations and vertex arrays  *
 * for representing the cube from Chapter 4 of the Edward Angel computer        *
 * graphics text, from which this code has been adapted.                        *
 ********************************************************************************/

#include "../../Common.h"

 // Vertices of the cube, centered at the origin.
GLfloat vertices[][3] =
{
	{-1.0, -1.0, -1.0},		//0
	{1.0, -1.0, -1.0},		//1
	{1.0, 1.0, -1.0},		//2
	{-1.0, 1.0, -1.0},		//3
	{-1.0, -1.0, 1.0},		//4
	{1.0, -1.0, 1.0},		//5
	{1.0, 1.0, 1.0},		//6
	{-1.0, 1.0, 1.0}		//7
};

// Colors of the vertices.
GLfloat colors[][3] =
{
	{1.0, 1.0, 1.0},		//���Ψ� �զ�
	{0.0, 0.0, 1.0},		//�V�U�Ԫ���2��
	{1.0, 1.0, 1.0},		//���Ψ� �զ�
	{0.0, 0.0, 0.0},		//���� ��
	{1.0, 1.0, 0.0},		//�V�U�Ԫ���3��
	{1.0, 1.0, 0.0},		//�k�� ��
	{0.0, 1.0, 0.0},		//�V�U�Ԫ���1��
	{1.0, 0.0, 0.0}			//�ݨ쪺���� ��
};

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//��
	2, 3, 7, 6,		//�W
	0, 4, 7, 3,		//��
	1, 2, 6, 5,		//�k
	4, 5, 6, 7,		//�e
	0, 1, 5, 4		//�U
};

// Angles of rotation about each axis.
GLfloat theta[] = { 0.0, 0.0, 0.0 };

// Current axis of rotation.
GLint axis = 2;

int spinning = 0;

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

	/*
	//draw_boundary(color_y, 1.3f); //�e�������

	//�� GL_LINE_LOOP �e�@�ӪŤ߯x��
	glColor3f(1.0, 0.0, 0.0);	//��
	float dd = 1.3f;
	float point1[3] = { -dd, -dd, 1.0 };	//���U
	float point2[3] = { dd, -dd, 1.0 };	//�k�U
	float point3[3] = { dd,  dd, 1.0 };	//�k�W
	float point4[3] = { -dd,  dd, 1.0 };	//���W
	glBegin(GL_LINE_LOOP);
	glVertex3fv(point1);	//���U
	glVertex3fv(point2);	//�k�U
	glVertex3fv(point3);	//�k�W
	glVertex3fv(point4);	//���W
	glEnd();
	*/

	glutSwapBuffers();
}

// This function spins the cube around the current axis by incrementing the angle of rotation by 2 degrees.
void idle(void)
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
	if (key == 27)
	{
		//���}����
		glutDestroyWindow(glutGetWindow());
		return;
	}
	if (key == 's')
	{
		spinning = !spinning;
	}
}

int main(int argc, char** argv)
{
	const char* windowName = "Rotating Color Cube";
	const char* message = "���ƹ��Ps����, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	glutIdleFunc(idle);
	glutMouseFunc(mouse);

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);

	colorcube();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
