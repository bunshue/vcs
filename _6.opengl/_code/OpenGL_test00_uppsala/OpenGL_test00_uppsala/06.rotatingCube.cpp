#include "../../Common.h"

 // Vertices of the cube, centered at the origin.
GLfloat vertices[][3] =
{
	{-1.0, -1.0, -1.0},		//0
	{1.0, -1.0, -1.0},		//1
	{1.0, 1.0, -1.0},		//2
	{-1.0, 1.0, -1.0},		//3
	{-1.0, -1.0, 1.0},		//4
	{1.0, -1.0, 1.0},		//5
	{1.0, 1.0, 1.0},		//6
	{-1.0, 1.0, 1.0}		//7
};

// Colors of the vertices.
GLfloat colors[][3] =
{
	{1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
	{0.0, 0.0, 1.0},		//�� B
	{1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
	{0.0, 1.0, 1.0},		//�� Cyan�ѫC
	{1.0, 1.0, 0.0},		//�U Y
	{1.0, 0.0, 1.0},		//�k Magenta���
	{0.0, 1.0, 0.0},		//�W G
	{1.0, 0.0, 0.0}			//�e R
};

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//��
	2, 3, 7, 6,		//�W
	0, 4, 7, 3,		//��
	1, 2, 6, 5,		//�k
	4, 5, 6, 7,		//�e
	0, 1, 5, 4		//�U
};

// Angles of rotation about each axis.
GLfloat theta[] = { 0.0, 0.0, 0.0 };

GLint axis = 0;	//0: ¶x�b����, 1: ¶y�b����, 2: ¶z�b����

int spinning = 0;

// This function sets up the vertex arrays for the color cube and the projection matrix.
void colorcube(void)
{
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, colors);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);
}

// This is the display callback function.
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	//������e���y�жb
	//draw_coordinates(1.3f);     //�e�y�жb

	glRotatef(theta[0], 1.0, 0.0, 0.0);	//��x�b����S�w����
	glRotatef(theta[1], 0.0, 1.0, 0.0);	//��y�b����S�w����
	glRotatef(theta[2], 0.0, 0.0, 1.0);	//��z�b����S�w����
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

	//�w����ᤧ�y�жb
	draw_coordinates(1.5f);     //�e�y�жb

	/*
	//�� GL_LINE_LOOP �e�@�ӪŤ߯x��
	glColor3f(1.0, 0.0, 0.0);	//��
	float dd = 1.3f;
	float point1[3] = { -dd, -dd, 1.0 };	//���U
	float point2[3] = { dd, -dd, 1.0 };	//�k�U
	float point3[3] = { dd,  dd, 1.0 };	//�k�W
	float point4[3] = { -dd,  dd, 1.0 };	//���W
	glBegin(GL_LINE_LOOP);
	glVertex3fv(point1);	//���U
	glVertex3fv(point2);	//�k�U
	glVertex3fv(point3);	//�k�W
	glVertex3fv(point4);	//���W
	glEnd();
	*/

	glColor3f(1.0f, 1.0f, 1.0f);
	glRasterPos3fv((GLfloat*)vertices[0]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0');
	glRasterPos3fv((GLfloat*)vertices[1]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '1');
	glRasterPos3fv((GLfloat*)vertices[2]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '2');
	glRasterPos3fv((GLfloat*)vertices[3]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '3');
	glRasterPos3fv((GLfloat*)vertices[4]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '4');
	glRasterPos3fv((GLfloat*)vertices[5]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '5');
	glRasterPos3fv((GLfloat*)vertices[6]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '6');
	glRasterPos3fv((GLfloat*)vertices[7]);
	glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '7');

	glutSwapBuffers();
}

// This function spins the cube around the current axis by incrementing the angle of rotation by 2 degrees.
void idle(void)
{
	if (spinning == 1)
	{
		theta[axis] += 1.0;
		if (theta[axis] > 360.0)
		{
			theta[axis] -= 360.0;
		}
		glutPostRedisplay();
		sleep(25);
	}
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
	//printf("�A�ҫ����䪺�X�O%x\t���ɵ��������ƹ��y�ЬO(%d,%d)\n", key, x, y);

	switch (key)
	{
	case 27:
	case 'q':
	case 'Q':
		//���}����
		glutDestroyWindow(glutGetWindow());
		return;
	case 'x':
		printf("¶ x�b ����\n");
		axis = 0;
		spinning = 1;
		break;
	case 'y':
		printf("¶ x�b ����\n");
		axis = 1;
		spinning = 1;
		break;
	case 'z':
		printf("¶ x�b ����\n");
		axis = 2;
		spinning = 1;
		break;
	case 's':
		spinning = !spinning;
		break;
	}
}

int main(int argc, char** argv)
{
	const char* windowName = "Rotating Color Cube";
	const char* message = "��x, y, z ��ܱ���b, ��s�Ұ�, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	glutIdleFunc(idle);

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);

	colorcube();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
