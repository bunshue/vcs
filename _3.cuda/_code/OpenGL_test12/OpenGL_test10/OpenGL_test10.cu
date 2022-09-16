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

void init(void)
{
}

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void display(void)
{
	int i;

	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
	glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-1.0, 11.0, -1.0, 11.0); //窗口坐标范围

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	//画10*10网格
	glColor3f(0.0f, 1.0f, 0.0f); //绿色
	for (i = 0; i <= 10; i++) //11条水平线
	{
		glBegin(GL_LINES);
		glVertex2d(0.0, i * 1.0);
		glVertex2d(10.0, i * 1.0);
		glEnd();
	}
	glBegin(GL_LINES); //11条竖线
	for (i = 0; i <= 10; i++)
	{
		glVertex2d(i * 1.0, 0.0);
		glVertex2d(i * 1.0, 10.0);
	}
	glEnd();

	//在对角线画点
	glColor3f(1.0f, 1.0f, 1.0f); //白色
	glPointSize(10.0f); //点大小
	glBegin(GL_POINTS);
	for (i = 0; i <= 10; i++)
		glVertex2d(i * 1.0, i * 1.0);
	glEnd();
	for (i = 0; i <= 10; i++)
	{
		glBegin(GL_POINTS);
		glVertex2d(i * 1.0, 10.0 - i * 1.0);
		glEnd();
	}

	glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("畫網格");

	init();

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMainLoop();

	return 0;
}
