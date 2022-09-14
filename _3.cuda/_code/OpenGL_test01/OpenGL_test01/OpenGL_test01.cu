// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#include <stdio.h>

void init(void);
void reshape(int w, int h);
void mouse(int button, int state, int x, int y);
void motion(int x, int y);
void display(void);
void drawCoordinates(void);

int mx, my; //position of mouse;
float x_angle, y_angle; //angle of eye

void init(void)
{
}

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void mouse(int button, int state, int x, int y)
{
	//MouseDown
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		mx = x;
		my = y;
		printf("D(%d, %d) ", mx, my);
	}
}

void motion(int x, int y)
{
	//MouseMove
	int dx, dy; //offset of mouse;

	dx = x - mx;
	dy = y - my;

	y_angle += dx * 0.01f;
	x_angle += dy * 0.01f;

	mx = x;
	my = y;

	printf("M(%d, %d) ", mx, my);

	glutPostRedisplay();
}

void display(void)
{
	printf("d ");
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = rect[2];
	h = rect[3];

	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
	glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if (w > h)
	{
		glOrtho(-w / h, w / h, -1.0f, 1.0f, -1.0f, 1.0f);
	}
	else
	{
		glOrtho(-1.0f, 1.0f, -h / w, h / w, -1.0f, 1.0f);
	}

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glRotatef(x_angle, 1.0f, 0.0f, 0.0f);
	glRotatef(y_angle, 0.0f, 1.0f, 0.0f);
	drawCoordinates();

	glFlush();
	glutSwapBuffers();
}

void drawCoordinates(void)
{
	glLineWidth(3.0f);

	glColor3f(1.0f, 0.0f, 0.0f); //画红色的x轴
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(1.0f, 0.0f, 0.0f);
	glEnd();

	glColor3f(0.0, 1.0, 0.0); //画绿色的y轴
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 1.0f, 0.0f);
	glEnd();

	glColor3f(0.0, 0.0, 1.0); //画蓝色的z轴
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 0.0f, 1.0f);
	glEnd();
}


int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("gl_1_2");
	init();

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMouseFunc(mouse);
	glutMotionFunc(motion);
	glutMainLoop();

	return 0;
}


