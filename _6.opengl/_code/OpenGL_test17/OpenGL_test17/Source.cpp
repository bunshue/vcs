#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

//eyex, eyey, eyez, centerx, centery, centerz
double eyex = -5.0;
double eyey = 5.0;
double eyez = -5.0;
double upx = 0;
double upy = 1.0;
double upz = 0;

void draw_coordinates(float len)
{
	glLineWidth(3.0f);	//設定線寬

	glColor3f(1.0f, 0.0f, 0.0f); //畫紅色的x軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(len, 0.0f, 0.0f);	//x軸 len,0,0
	glEnd();

	glColor3f(0.0, 1.0, 0.0); //畫綠色的y軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(0.0f, len, 0.0f);	//y軸 0,len,0
	glEnd();

	glColor3f(0.0, 0.0, 1.0); //畫藍色的z軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(0.0f, 0.0f, len);	//z軸 0,0,len
	glEnd();
}

// 繪圖回調函數
void display(void)
{
	//printf("d");
	glClearColor(1, 1, 1, 0);
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0, 0, 1.0); //畫筆藍色   
	glLoadIdentity();	//設置單位矩陣

	gluLookAt(eyex, eyey, eyez, 0, 0, 0, 1.0, 0.0, 0);

	eyex += 0.01;
	if (eyex > 5.0)
		eyex = -5.0;

	/*
	eyey += 0.01;
	if (eyey > 8.0)
		eyey = 5.0;
	*/

	eyez += 0.01;
	if (eyez > 5.0)
		eyez = -5.0;

	draw_coordinates(3.0);

	glColor3f(1.0f, 1.0f, 0.0f); //Yellow
	glLineWidth(1.0f);

	glutWireTeapot(1.3);

	glutSwapBuffers();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣
	gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 4, 10.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣
	//gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;

	case '1':
		printf("1\n");
		gluLookAt(0.0, 5.0, 0.0, 0, 0, 0, 1.0, 0.0, 0);
		glutPostRedisplay();
		break;

	case '2':
		printf("2\n");
		gluLookAt(0.0, 10.0, 0.0, 0, 0, 0, 1.0, 0.0, 0);
		glutPostRedisplay();
		break;

	case '3':
		printf("3\n");
		gluLookAt(0.0, 15.0, 0.0, 0, 0, 0, 1.0, 0.0, 0);
		glutPostRedisplay();
		break;

	case '4':
		break;

	case '?':
		break;
	}
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

void idle()
{
	//printf("i");
	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("gluLookAt 測試");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function
	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glutMainLoop();	//開始主循環繪製

	return 0;
}
