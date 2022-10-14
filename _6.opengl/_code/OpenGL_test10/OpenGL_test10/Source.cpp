#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <math.h>
#include <windows.h>

#define _USE_MATH_DEFINES

#define M_PI       3.14159265358979323846   // pi

#include <iostream>

int mx, my; //position of mouse
int m_state = 0; //mouse usage
float x_angle = 0.0f, y_angle = 0.0f; //angle of eye
float dist = 10.0f; //distance from the eye

void drawCoordinates(void);
void drawTetrahedron(void);

void init(void)
{
	glEnable(GL_DEPTH_TEST);
}

// 繪圖回調函數
void display(void)
{
	double x, y, z, eyex, eyey, eyez;
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = rect[2];
	h = rect[3];

	glClearColor(1.0f, 1.0f, 1.0f, 0.0f);
	glClearDepth(1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	if (h < 1)
	{
		h = 1;
	}
	gluPerspective(30.0, w / h, 0.1, 20.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	//glTranslated(0.0, 0.0, -dist);
	//glRotatef(x_angle, 1.0f, 0.0f, 0.0f);
	//glRotatef(y_angle, 0.0f, 1.0f, 0.0f);
	x = 0.0;
	y = 0.0;
	z = dist;
	eyex = x;
	eyey = y * cos(-x_angle * M_PI / 180.0) - z * sin(-x_angle * M_PI / 180.0);
	eyez = y * sin(-x_angle * M_PI / 180.0) + z * cos(-x_angle * M_PI / 180.0);
	x = eyex;
	y = eyey;
	z = eyez;
	eyex = x * cos(-y_angle * M_PI / 180.0) + z * sin(-y_angle * M_PI / 180.0);
	eyey = y;
	eyez = -x * sin(-y_angle * M_PI / 180.0) + z * cos(-y_angle * M_PI / 180.0);
	gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
	drawCoordinates();
	glPushMatrix();
	glTranslatef(-1.0f, 0.0f, 0.0f);
	glutWireTeapot(0.5);
	glPopMatrix();
	glPushMatrix();
	glTranslatef(1.0f, 0.0f, 0.0f);
	glScalef(0.5f, 0.5f, 0.5f);
	drawTetrahedron();	//畫四面體
	glPopMatrix();

	glFlush();
	glutSwapBuffers();
}

void drawCoordinates(void)
{
	glBegin(GL_LINES);
	glColor3f(1.0f, 0.0f, 0.0f); //画红色的x轴
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(1.0f, 0.0f, 0.0f);
	glColor3f(0.0, 1.0, 0.0); //画绿色的y轴
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 1.0f, 0.0f);
	glColor3f(0.0, 0.0, 1.0); //画蓝色的z轴
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 0.0f, 1.0f);
	glEnd();
}

void drawTetrahedron(void)	//畫四面體
{
	float pnt[4][3] = { {0.0,0.0,0.0}, {1.0,0.0,0.0}, {0.0,1.0,0.0}, {0.0,0.0,1.0} };
	int tetra[4][3] = { {0,2,1}, {0,3,2}, {0,1,3}, {1,2,3} };

	glBegin(GL_TRIANGLES);
	glColor3f(1.0f, 0.0f, 0.0f);
	glVertex3fv(pnt[tetra[0][0]]);
	glVertex3fv(pnt[tetra[0][1]]);
	glVertex3fv(pnt[tetra[0][2]]);

	glColor3f(0.0f, 1.0f, 0.0f);
	glVertex3fv(pnt[tetra[1][0]]);
	glVertex3fv(pnt[tetra[1][1]]);
	glVertex3fv(pnt[tetra[1][2]]);

	glColor3f(0.0f, 0.0f, 1.0f);
	glVertex3fv(pnt[tetra[2][0]]);
	glVertex3fv(pnt[tetra[2][1]]);
	glVertex3fv(pnt[tetra[2][2]]);

	glColor3f(0.0f, 1.0f, 1.0f);	glVertex3fv(pnt[tetra[3][0]]); //补色
	glColor3f(1.0f, 0.0f, 1.0f);	glVertex3fv(pnt[tetra[3][1]]);
	glColor3f(1.0f, 1.0f, 0.0f);	glVertex3fv(pnt[tetra[3][2]]);
	glEnd();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
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
	case '0':
		m_state = 0;
		break;
	case '1':
		m_state = 1;
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

void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		mx = x;
		my = y;
	}
}

void motion(int x, int y)
{
	GLint dx, dy; //offset of mouse;

	dx = x - mx;
	dy = y - my;

	if (m_state == 0)
	{
		y_angle += dx * 0.1f;
		x_angle += dy * 0.1f;
	}
	else if (m_state == 1)
	{
		dist += (dx + dy) * 0.01f;
	}

	mx = x;
	my = y;

	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	//glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	//glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("畫茶壺");	//開啟視窗 並顯示出視窗 Title

	init();

	printf("0 keydown means control the angle of the eye\n");
	printf("1 keydown means control the distance of the eye\n");

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	glutMainLoop();

	return 0;
}
