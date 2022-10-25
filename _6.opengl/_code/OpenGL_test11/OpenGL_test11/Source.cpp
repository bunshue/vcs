#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void drawCoordinates(void);
void drawTetrahedron(void);

int mx, my; //position of mouse
int m_state = 0; //mouse usage
float x_angle = 0.0f, y_angle = 0.0f; //angle of eye
float dist = 10.0f; //distance from the eye

void init(void)
{
	glEnable(GL_DEPTH_TEST);
}

// 繪圖回調函數
void display(void)
{
	float lit_position[] = { 0.0f, 0.0f, 1.0f, 0.0f };
	float mat_yellow[] = { 1.0f, 1.0f, 0.0f, 1.0f };
	float mat_cyan[] = { 0.0f, 1.0f, 1.0f, 1.0f };
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = rect[2];
	h = rect[3];

	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
	glClearDepth(1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣

	if (h < 1)
	{
		h = 1;
	}
	gluPerspective(30.0, w / h, 0.1, 20.0); //對應變換陣T0

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣

	glLightfv(GL_LIGHT0, GL_POSITION, lit_position);
	glTranslated(0.0, 0.0, -dist); //對應變換陣T1
	glRotatef(x_angle, 1.0f, 0.0f, 0.0f); //對應變換陣T2
	glRotatef(y_angle, 0.0f, 1.0f, 0.0f);  //對應變換陣T3
	glDisable(GL_LIGHTING);
	//glLightfv(GL_LIGHT0, GL_POSITION, lit_position);
	drawCoordinates(); //顯示坐標軸，設X軸的兩端點為v1、v2，考慮這兩點經受的變換
	glutWireTeapot(0.5); //顯示茶壺
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glPushMatrix(); //下壓堆棧并復制棧頂
	glTranslatef(1.0f, 0.0f, 0.0f); //對應變換陣T4
	glScalef(0.5f, 0.5f, 0.5f); //對應變換陣T5
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_yellow);
	drawTetrahedron(); //顯示直角四面體，設某個三角形的頂點為v1'、v2'、v3'，考慮這三點經受的變換
	glPopMatrix(); //上彈堆棧，棧頂被放棄
	glPushMatrix();
	glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 1);
	glTranslatef(-1.0f, 0.0f, 0.0f); //對應變換陣T6
	glRotatef(-90.0f, 1.0f, 0.0f, 0.0f); //對應變換陣T7
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_cyan);
	glMaterialfv(GL_BACK, GL_DIFFUSE, mat_yellow);
	glutSolidCone(0.4, 1.0, 100, 10); //顯示圓錐體
	glPopMatrix();

	glFlush();
	glutSwapBuffers();
}

void drawCoordinates(void)
{
	glColor3f(1.0f, 0.0f, 0.0f); //畫紅色的x軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(1.0f, 0.0f, 0.0f);
	glEnd();
	glColor3f(0.0, 1.0, 0.0); //畫綠色的y軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 1.0f, 0.0f);
	glEnd();
	glColor3f(0.0, 0.0, 1.0); //畫藍色的z軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);
	glVertex3f(0.0f, 0.0f, 1.0f);
	glEnd();
}

void drawTetrahedron(void)
{
	float pnt[4][3] = { {0.0,0.0,0.0},{1.0,0.0,0.0}, {0.0,1.0,0.0}, {0.0,0.0,1.0} };
	int tetra[4][3] = { {0,2,1}, {0,3,2}, {0,1,3}, {1,2,3} };

	glNormal3f(0.0f, 0.0f, -1.0f);
	glBegin(GL_POLYGON); //X-Y
	glVertex3fv(pnt[tetra[0][0]]);
	glVertex3fv(pnt[tetra[0][1]]);
	glVertex3fv(pnt[tetra[0][2]]);
	glEnd();
	glNormal3f(-1.0f, 0.0f, 0.0f);
	glBegin(GL_POLYGON); //Y-Z
	glVertex3fv(pnt[tetra[1][0]]);
	glVertex3fv(pnt[tetra[1][1]]);
	glVertex3fv(pnt[tetra[1][2]]);
	glEnd();
	glNormal3f(0.0f, -1.0f, 0.0f);
	glBegin(GL_POLYGON); //Z-X
	glVertex3fv(pnt[tetra[2][0]]);
	glVertex3fv(pnt[tetra[2][1]]);
	glVertex3fv(pnt[tetra[2][2]]);
	glEnd();
	glNormal3f(1.0f, 1.0f, 1.0f);
	glBegin(GL_POLYGON); //slope
	glVertex3fv(pnt[tetra[3][0]]);
	glVertex3fv(pnt[tetra[3][1]]);
	glVertex3fv(pnt[tetra[3][2]]);
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
	int dx, dy; //offset of mouse;

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

	glutCreateWindow("畫茶壺圓椎三角塊");	//開啟視窗 並顯示出視窗 Title

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