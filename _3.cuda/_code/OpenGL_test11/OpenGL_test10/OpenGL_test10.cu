// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <GL/glut.h>  //32位元用的

#include <windows.h>

void init(void);
void reshape(int w, int h);
void display(void);
void drawGrid(int xmin, int xmax, int ymin, int ymax);

#define NGRID 6

double pnts[][2] = {
	0, 6,
	1, 0,
	2, 6,
	3, 0,
	4, 6,
	5, 0,
	6, 6
};

void init(void)
{
}

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void display(void)
{
	int i, n = 6;

	glClearColor(0.0, 0.0, 0.0, 0.0);
	glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, NGRID, 0.0, NGRID); //窗口坐标范围

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	//画网格
	glColor3f(0.0f, 1.0f, 0.0f); //绿色
	drawGrid(0, NGRID, 0, NGRID);

	//画控制点
	glColor3f(1.0f, 0.0f, 0.0f); //红色
	glPointSize(10.0f); //点大小
	for (i = 0; i <= n; i++)
	{
		glBegin(GL_POINTS);
		glVertex2d(pnts[i][0], pnts[i][1]);
		glEnd();
	}

	//画折线
	glColor3f(1.0f, 1.0f, 1.0f); //白色
	for (i = 0; i < n; i++)
	{
		glBegin(GL_LINES);
		glVertex2d(pnts[i][0], pnts[i][1]);
		glVertex2d(pnts[i + 1][0], pnts[i + 1][1]);
		glEnd();
	}

	glFlush();
}

void drawGrid(int xmin, int xmax, int ymin, int ymax)
{
	int i, j;
	for (j = ymin; j <= ymax; j++) //水平线
	{
		glBegin(GL_LINES);
		glVertex2d(xmin, j);
		glVertex2d(xmax, j);
		glEnd();
	}
	for (i = xmin; i <= xmax; i++) //竖线
	{
		glBegin(GL_LINES);
		glVertex2d(i, ymin);
		glVertex2d(i, ymax);
		glEnd();
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);

	glutCreateWindow("畫線範例");
	init();

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMainLoop();

	return 0;
}

