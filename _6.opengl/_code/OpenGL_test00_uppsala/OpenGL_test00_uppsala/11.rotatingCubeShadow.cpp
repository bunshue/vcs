/* Rotating cube with viewer movement and shadow from Chapter 5 */
/* Cube definition and display similar to rotating--cube program */

/* We use the Lookat function in the display callback to point
the viewer, whose position can be altered by the x,X,y,Y,z, and Z keys.
The perspective view is set in the reshape callback */

#include "../../Common.h"

// Vertices of the cube, centered at the origin.
GLfloat vertices[][3] =
{
	{-1.0,1.0,-1.0},
	{1.0,1.0,-1.0},
	{1.0,3.0,-1.0},
	{-1.0,3.0,-1.0},
	{-1.0,1.0,1.0},
	{1.0,1.0,1.0},
	{1.0,3.0,1.0},
	{-1.0,3.0,1.0}
};

// Colors of the vertices.
GLfloat vertex_color[][3] =
{
	{0.0,0.0,0.0},
	{1.0,0.0,0.0},
	{1.0,1.0,0.0},
	{0.0,1.0,0.0},
	{0.0,0.0,1.0},
	{1.0,0.0,1.0},
	{1.0,1.0,1.0},
	{0.0,1.0,1.0}
};

// Shadow colors.
GLfloat shadowcolors[][3] =
{
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0},
	{0.0,0.0,0.0}
};

// Indices of the vertices to make up the six faces of the cube.
//							   下          後        左         右         上          前
GLubyte cubeIndices[24] = { 0,3,2,1,   2,3,7,6,   0,4,7,3,   1,2,6,5,   4,5,6,7,    0,1,5,4 };

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//對各軸的旋轉角度
GLint axis = 0;	//0: 繞x軸旋轉, 1: 繞y軸旋轉, 2: 繞z軸旋轉
GLdouble viewer[] = { 5.0, 5.0, 5.0 }; /* initial viewer location      */
GLfloat light[3] = { 0.0, 10.0, 0.0 }; /* position of light            */
GLfloat m[16];                       /* shadow transformation matrix */
float dd = 1.0f;
float ddd = 0.06f;

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW

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
	m[7] = (GLfloat)(-1.0 / light[1]);
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

	glColorPointer(3, GL_FLOAT, 0, vertex_color);
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

	/* Draw the shadow */

	glPushMatrix();
	glTranslatef(light[0], light[1], light[2]);
	glMultMatrixf(m);
	glTranslatef(-light[0], -light[1], -light[2]);
	glColorPointer(3, GL_FLOAT, 0, shadowcolors);
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
	glPopMatrix();

	glutSwapBuffers();
}

/* This function is the idle callback. It spins the cube 2 degrees about the selected axis. */
void idle(void)
{
	if (flag_rotating ==1)
	{
		if (flag_rotating_direction == 0)	//CW
		{
			theta[axis] += dd;
			if (theta[axis] > 360.0f)
			{
				theta[axis] = 0.0f;
			}
		}
		else   //CCW
		{
			theta[axis] -= dd;
			if (theta[axis] < 0.0f)
			{
				theta[axis] = 360.0f;
			}
		}
		glutPostRedisplay();
		sleep(25);
	}
}

void mouse(int btn, int state, int x, int y)
{
	if (btn == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		axis = 0;
		flag_rotating = 1;
	}
	if (btn == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
	{
		axis = 1;
		flag_rotating = 1;
	}
	if (btn == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
	{
		axis = 2;
		flag_rotating = 1;
	}
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
	if (key == 27)
	{
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
		flag_rotating = 1 - flag_rotating;
	}
	glutPostRedisplay();
}

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(50.0, (double)w / (double)h, 2.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv)
{
	const char* windowName = "Color Cube with Shadow";
	const char* message = "滑鼠控制, 按S啟停, 按 Esc 離開\n";
	//const char* message = "按x, y, z 選擇旋轉軸, 按 空白鍵 啟停, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

	//先保留
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutMouseFunc(mouse);		//設定callback function
	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glEnable(GL_DEPTH_TEST);

	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
