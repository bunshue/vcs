/* Rotating cube with viewer movement from Chapter 5 of Ed Angel text.*/
/* Cube definition and display similar to rotating--cube program. */

/* We use the Lookat function in the display callback to point
the viewer, whose position can be altered by the x,X,y,Y,z, and Z keys.
The perspective view is set in the reshape callback */

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
GLfloat vertex_color[][3] = {						//沒用到 R B
	{1.0,0.0,0.0}, {0.0,1.0,0.0}, {0.0,0.0,1.0},	//R G B
	{1.0,1.0,0.0}, {0.0,1.0,1.0}, {1.0,0.0,1.0},	//黃 天青 桃紅
	{0.0,0.0,0.0}, {1.0,1.0,1.0} };					//黑 白

// Colors of the vertices.
GLfloat colors[][3] =
{
	{1.0, 1.0, 1.0},		//未用到 白色  XXXX
	{0.0, 0.0, 1.0},		//後 B
	{1.0, 1.0, 1.0},		//未用到 白色  XXXX
	{0.0, 1.0, 1.0},		//左 Cyan天青
	{1.0, 1.0, 0.0},		//下 Y
	{1.0, 0.0, 1.0},		//右 Magenta桃紅
	{0.0, 1.0, 0.0},		//上 G
	{1.0, 0.0, 0.0}			//前 R
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

GLfloat theta[] = { 0.0, 0.0, 0.0 };  /* initial rotation angles  */
GLint axis = 2;                     /* initial axis of rotation */
GLdouble viewer[] = { 0.0, 0.0, 5.0 }; /* initial viewer location  */

int spinning = 0;

// This function sets up the vertex arrays for the color cube.
void colorcube(void)
{
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, vertex_color);
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

	/* Draw the cube and switch buffers */

	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
	glutSwapBuffers();
}

/* This function is the idle callback. It spins the cube 2 degrees about the selected axis. */
void idle(void)
{
	if (spinning ==1)
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
		spinning = 1;
	}
	if (btn == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
	{
		axis = 1;
		spinning = 1;
	}
	if (btn == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
	{
		axis = 2;
		spinning = 1;
	}
}

void keyboard(unsigned char key, int x, int y)
{
	if (key == 27)
	{
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;
	}
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
		spinning = 1 - spinning;
	}
	glutPostRedisplay();
}

/* This is the reshape callback function. It produces a perspective projection of the cube. */
void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45.0, (double)w / (double)h, 2.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv)
{
	const char* windowName = "Color Cube";
	const char* message = "滑鼠控制, 按S啟停, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

	//先保留
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫
	glutMouseFunc(mouse);

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);
	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
