#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

//eyex, eyey, eyez, centerx, centery, centerz
float upx = 0;
float upy = 1.0;
float upz = 0;

void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0); //背景黑色
}

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
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0); //画笔白色

	glLoadIdentity();  //加载单位矩阵

	gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, upx, upy, upz);

	draw_coordinates(2.0);

	glColor3f(1.0f, 1.0f, 1.0f); //白色線
	glLineWidth(1.0f);

	glutWireTeapot(1.6);

	glutSwapBuffers();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 1.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, upx, upy, upz);
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
		upx = 0;
		upy = 1.0;
		upz = 0;
		gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;

	case '2':
		printf("2\n");
		upx = 0;
		upy = -1.0;
		upz = 0;
		gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;

	case '3':
		upx = 1.0;
		upy = 0;
		upz = 0;
		gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
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

	glutMainLoop();	//開始主循環繪製

	return 0;
}
