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
	glFlush();  // ����ø�ϩR�O
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

	glutInitWindowSize(600, 600);       // �]�w�����j�p
	glutInitWindowPosition(1100, 200);  // �]�w������m

	glutCreateWindow("Maxwell's Triangle");

	glutDisplayFunc(display);   //�]�wcallback function
	glutReshapeFunc(reshape0);   //�]�wcallback function
	glutKeyboardFunc(keyboard0); //�]�wcallback function

	gfxinit();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
