#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

double xx = -5.0;
double yy = 5.0;
double zz = -5.0;

// 繪圖回調函數
void display(void)
{
	printf("d");
	glClearColor(1, 1, 1, 0);
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0, 0, 1.0); //畫筆藍色   
	glLoadIdentity();	//設置單位矩陣

	gluLookAt(xx, yy, zz, 0, 0, 0, 1.0, 0.0, 0);

	xx += 0.01;
	if (xx > 5.0)
		xx = -5.0;

	/*
	yy += 0.01;
	if (yy > 8.0)
		yy = 5.0;
	*/

	zz += 0.01;
	if (zz > 5.0)
		zz = -5.0;

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

	//glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title
	glutCreateWindow("gluPerspective ( X, X, 4,10 )");

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function
	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glutMainLoop();	//開始主循環繪製

	return 0;
}
