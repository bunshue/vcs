#include "../../Common.h"

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_TRIANGLES);
	{
		glColor3f(1.0, 0.0, 0.0);
		glVertex2f(0.0, 0.0);
		glColor3f(0.0, 1.0, 0.0);
		glVertex2f(1.0, 0.0);
		glColor3f(0.0, 0.0, 1.0);
		glVertex2f(0.5f, (float)sqrt(3.0) * 0.5f);
	}
	glEnd();
	glFlush();  // 執行繪圖命令
}

void gfxinit()
{
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-0.1, 1.1, -0.1, 1.1);
	glClearColor(1.0, 1.0, 1.0, 1.0);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);       // 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置

	glutCreateWindow("Maxwell's Triangle");

	glutDisplayFunc(display);   //設定callback function
	glutReshapeFunc(reshape0);   //設定callback function
	glutKeyboardFunc(keyboard0); //設定callback function

	gfxinit();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
