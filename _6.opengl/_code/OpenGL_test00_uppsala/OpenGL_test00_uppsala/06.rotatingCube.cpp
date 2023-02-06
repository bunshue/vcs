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
	{1.0, 1.0, 1.0},		//未用到 白色
	{0.0, 0.0, 1.0},		//向下拉的第2面
	{1.0, 1.0, 1.0},		//未用到 白色
	{0.0, 0.0, 0.0},		//左面 黑
	{1.0, 1.0, 0.0},		//向下拉的第3面
	{1.0, 1.0, 0.0},		//右面 黃
	{0.0, 1.0, 0.0},		//向下拉的第1面
	{1.0, 0.0, 0.0}			//看到的正面 紅
};

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//後
	2, 3, 7, 6,		//上
	0, 4, 7, 3,		//左
	1, 2, 6, 5,		//右
	4, 5, 6, 7,		//前
	0, 1, 5, 4		//下
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
	//draw_boundary(color_y, 1.3f); //畫視窗邊界

	//用 GL_LINE_LOOP 畫一個空心矩形
	glColor3f(1.0, 0.0, 0.0);	//紅
	float dd = 1.3f;
	float point1[3] = { -dd, -dd, 1.0 };	//左下
	float point2[3] = { dd, -dd, 1.0 };	//右下
	float point3[3] = { dd,  dd, 1.0 };	//右上
	float point4[3] = { -dd,  dd, 1.0 };	//左上
	glBegin(GL_LINE_LOOP);
	glVertex3fv(point1);	//左下
	glVertex3fv(point2);	//右下
	glVertex3fv(point3);	//右上
	glVertex3fv(point4);	//左上
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
		//離開視窗
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
	const char* message = "按滑鼠與s控制, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	glutIdleFunc(idle);
	glutMouseFunc(mouse);

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);

	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
