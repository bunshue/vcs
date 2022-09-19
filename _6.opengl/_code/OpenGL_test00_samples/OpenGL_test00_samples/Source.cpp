// OpenGL Graphics includes
#include <iostream>
#include <helper_gl.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

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
	w = (float)rect[2];
	h = (float)rect[3];

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

void keyboard(unsigned char k, int /*x*/, int /*y*/)
{
	switch (k)
	{
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;

	case '1':
		printf("1\n");
		break;

	case '2':
		printf("2\n");
		break;

	case '3':
		break;

	case '4':
		break;

	case '?':
		break;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);
	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	init();

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	glutMainLoop();

	return 0;
}


