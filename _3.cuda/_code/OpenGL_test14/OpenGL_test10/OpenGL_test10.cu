// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <GL/glut.h>  //32位元用的


#include <windows.h>

#include <stdio.h>

void reshape(int w, int h);
void display(void);

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void display(void)
{
	float mat[16];
	int i;

	glEnable(GL_DEPTH_TEST);
	glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
	glClearDepth(1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);
	glGetFloatv(GL_PROJECTION_MATRIX, mat);
	for (i = 0; i < 16; i++)
	{
		printf("%10.7f", mat[i]);
		if ((i + 1) % 4) printf(" ");
		else printf("\n");
	}

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glColor3f(1.0f, 0.0f, 0.0f); //在右上角画红色平面：应该在后面
	glBegin(GL_POLYGON);
	glVertex3f(0.0f, 0.0f, -1.0f + 0.001f);
	glVertex3f(1.0f, 0.0f, -1.0f + 0.001f);
	glVertex3f(1.0f, 1.0f, -1.0f + 0.001f);
	glVertex3f(0.0f, 1.0f, -1.0f + 0.001f);
	glEnd();
	glColor3f(0.0f, 1.0f, 0.0f); //在左下角画绿色的平面：应该在前面
	glBegin(GL_POLYGON);
	glVertex3f(-1.0f, -1.0f, 1.0f - 0.001f);
	glVertex3f(0.0f + 0.5f, -1.0f, 1.0f - 0.001f);
	glVertex3f(0.0f + 0.5f, 0.0f + 0.5f, 1.0f - 0.001f);
	glVertex3f(-1.0f, 0.0f + 0.5f, 1.0f - 0.001f);
	glEnd();
	glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("畫顏色色塊");

	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutMainLoop();

	return 0;
}

