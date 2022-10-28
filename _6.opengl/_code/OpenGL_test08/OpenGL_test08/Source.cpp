#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// w0, w1, w2, and w3 are the four cubic B-spline basis functions
float bspline_w0(float a)
{
	return (1.0f / 6.0f) * (-a * a * a + 3.0f * a * a - 3.0f * a + 1.0f);
}

float bspline_w1(float a)
{
	return (1.0f / 6.0f) * (3.0f * a * a * a - 6.0f * a * a + 4.0f);
}

float bspline_w2(float a)
{
	return (1.0f / 6.0f) * (-3.0f * a * a * a + 3.0f * a * a + 3.0f * a + 1.0f);
}

float bspline_w3(float a)
{
	return (1.0f / 6.0f) * (a * a * a);
}

void plotCurve(float (*func)(float))
{
	const int steps = 100;
	glBegin(GL_LINE_STRIP);

	for (int i = 0; i < steps; i++)
	{
		float x = i / (float)(steps - 1);
		glVertex2f(x, func(x));
	}
	glEnd();
}

// 繪圖回調函數
void display(void)
{
	// draw spline curves
	glPushMatrix();
	glScalef(0.25, 0.25, 1.0);

	glTranslatef(0.0, 2.0, 0.0);
	glColor3f(1.0, 0.0, 0.0);
	plotCurve(bspline_w3);

	glTranslatef(1.0, 0.0, 0.0);
	glColor3f(0.0, 1.0, 0.0);
	plotCurve(bspline_w2);

	glTranslatef(1.0, 0.0, 0.0);
	glColor3f(0.0, 0.0, 1.0);
	plotCurve(bspline_w1);

	glTranslatef(1.0, 0.0, 0.0);
	glColor3f(1.0, 0.0, 1.0);
	plotCurve(bspline_w0);

	glPopMatrix();
	glColor3f(1.0, 1.0, 1.0);

	//暫放
	glColor3f(1.0, 0.0, 1.0);
	glBegin(GL_QUADS);
	//glTexCoord2f(0.0f, 0.0f);
	glVertex2f(0.0f, 0.0f);
	//glTexCoord2f(0.5f, 0.0f);
	glVertex2f(0.5f, 0.0f);
	//glTexCoord2f(0.5f, 0.5f);
	glVertex2f(0.5f, 0.5f);
	//glTexCoord2f(0.0f, 0.5f);
	glVertex2f(0.0f, 0.5f);
	glEnd();


	glutSwapBuffers();
	glFlush();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
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
}

void motion(int x, int y)
{
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	glutMainLoop();	//開始主循環繪製

	return 0;
}
