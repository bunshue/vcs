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
GLfloat vertex_color[][3] =
{
	{1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
	{0.0, 0.0, 1.0},		//-z �� ��
	{1.0, 1.0, 1.0},		//���Ψ� �զ�  XXXX
	{0.0, 1.0, 1.0},		//-x �� Cyan �ѫC
	{1.0, 1.0, 0.0},		//-y �U ��
	{1.0, 0.0, 1.0},		//+x �k Magenta���
	{0.0, 1.0, 0.0},		//+y �W ��
	{1.0, 0.0, 0.0}			//+z �e ��
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

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//��U�b�����ਤ��
GLint axis = 0;	//0: ¶x�b����, 1: ¶y�b����, 2: ¶z�b����

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

//�ҩl�ɪ����I
double eyex = 0.0f;
double eyey = 0.0f;
double eyez = 5.0f;
//double eye_distance = 5.0f;

// This function sets up the vertex arrays for the color cube.
void colorcube(void)
{
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, vertex_color);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glLoadIdentity();

	gluLookAt(eyex, eyey, eyez, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f);

	glRotatef(theta[0], 1.0f, 0.0f, 0.0f);	//��x�b����S�w����
	glRotatef(theta[1], 0.0f, 1.0f, 0.0f);	//��y�b����S�w����
	glRotatef(theta[2], 0.0f, 0.0f, 1.0f);	//��z�b����S�w����

	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

	//�w����ᤧ�y�жb
	draw_coordinates(1.5f);     //�e�y�жb

	draw_teapot(color_purple, 1.0f, 1.0f);	//�e����

	//draw_cube(color_silver, 1.0f, 2.5f);	//cubic �~��
	//draw_cube(color_purple, 1.0f, 3.0f);	//cubic �~��

	for (int i = 0; i < 8; i++)
	{
		glColor3f(1.0f, 1.0f, 1.0f);
		glRasterPos3fv((GLfloat*)vertices[i]);
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0' + i);
	}

	glutSwapBuffers();
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
		printf("In ");
		if (axis == 0)
		{
			eyex -= 0.5f;
			if (eyex < 0.5f)
				eyex = 0.5f;
		}
		else if (axis == 1)
		{
			eyey -= 0.5f;
			if (eyey < 0.5f)
				eyey = 0.5f;
		}
		else if (axis == 2)
		{
			eyez -= 0.5f;
			if (eyez < 0.5f)
				eyez = 0.5f;
		}
		break;
	case '-':
		printf("Out ");
		if (axis == 0)
		{
			eyex += 0.5f;
			if (eyex > 15.0f)
				eyex = 15.0f;
		}
		else if (axis == 1)
		{
			eyey += 0.5f;
			if (eyey > 15.0f)
				eyey = 15.0f;
		}
		else if (axis == 2)
		{
			eyez += 0.5f;
			if (eyez > 15.0f)
				eyez = 15.0f;
		}
		break;
	case ' ':
	case 's':
		flag_rotating = 1 - flag_rotating;
		break;

	case 'r':
		printf("���m\n");
		/*
		flag_rotating = 0;
		theta[0] = 0.0f;
		theta[1] = 0.0f;
		theta[2] = 0.0f;
		glutPostRedisplay();
		*/
		break;

	}
	glutPostRedisplay();
}

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45.0, (double)w / (double)h, 2.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
}

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

int main(int argc, char** argv)
{
	const char* windowName = "Color Cube";
	const char* message = "�ƹ�����, ��S�Ұ�, �� Esc ���}\n";
	//const char* message = "��x, y, z ��ܱ���b, �� �ť��� �Ұ�, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

	//���O�d
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutIdleFunc(idle);         //�]�wcallback function, �Q��idle�ƥ�i�歫�e

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);
	colorcube();

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
