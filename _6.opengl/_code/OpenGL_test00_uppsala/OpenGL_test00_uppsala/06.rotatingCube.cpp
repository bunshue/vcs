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
GLfloat theta[] = { 0.0f, 0.0f, 0.0f };

GLint axis = 0;	//0: ¶x�b����, 1: ¶y�b����, 2: ¶z�b����

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

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

	//draw_teapot(color_purple, 1.0f, 1.0f);	//�e����

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

	int i;
	for (i = 0; i < 8; i++)
	{
		glRasterPos3fv((GLfloat*)vertices[i]);
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0' + i);
	}
	glutSwapBuffers();
}

// This function spins the cube around the current axis by incrementing the angle of rotation by 2 degrees.
void idle(void)
{
	if (flag_rotating == 1)
	{
		if (flag_rotating_direction == 0)	//CW
		{
			theta[axis] += dd;
			if (theta[axis] > 360.0f)
			{
				theta[axis] = 0.0f;
			}
		}
		else   //CCW
		{
			theta[axis] -= dd;
			if (theta[axis] < 0.0f)
			{
				theta[axis] = 360.0f;
			}
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
		flag_rotating_direction = 0;	//CW
		if (flag_rotating == 0)
		{
			printf("¶ x�b ����\n");
			axis = 0;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("����\n");
		}
		break;
	case 'y':
		flag_rotating_direction = 0;	//CW
		if (flag_rotating == 0)
		{
			printf("¶ y�b ����\n");
			axis = 1;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("����\n");
		}
		break;
	case 'z':
		flag_rotating_direction = 0;	//CW
		if (flag_rotating == 0)
		{
			printf("¶ z�b ����\n");
			axis = 2;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("����\n");
		}
		break;
	case 'X':
		flag_rotating_direction = 1;	//CCW
		if (flag_rotating == 0)
		{
			printf("¶ x�b ���� ����\n");
			axis = 0;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("����\n");
		}
		break;
	case 'Y':
		flag_rotating_direction = 1;	//CCW
		if (flag_rotating == 0)
		{
			printf("¶ y�b ���� ����\n");
			axis = 1;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("����\n");
		}
		break;
	case 'Z':
		flag_rotating_direction = 1;	//CCW
		if (flag_rotating == 0)
		{
			printf("¶ z�b ���� ����\n");
			axis = 2;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("����\n");
		}
		break;
	case '+':
		dd += ddd;
		if (dd > 20.0f)
		{
			dd = 10.0f;
		}
		break;
	case '-':
		if (dd > 0.1)
		{
			dd -= ddd;
		}
		break;
	case ' ':
	case 's':
		flag_rotating = 1 - flag_rotating;
		break;
	case 'r':
		printf("���m\n");
		flag_rotating = 0;

		break;
	}
}

int main(int argc, char** argv)
{
	const char* windowName = "Rotating Color Cube";
	const char* message = "��x, y, z ��ܱ���b, �� �ť��� �Ұ�, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	glutIdleFunc(idle);         //�]�wcallback function, �Q��idle�ƥ�i�歫�e

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);

	colorcube();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}


//�[�e���������

