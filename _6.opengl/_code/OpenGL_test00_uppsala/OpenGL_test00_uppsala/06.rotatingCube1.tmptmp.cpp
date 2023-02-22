#include "../../Common.h"

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//��U�b�����ਤ��
GLint axis = 0;	//0: ¶x�b����, 1: ¶y�b����, 2: ¶z�b����

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

void display(void)
{
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);

	glClear(GL_COLOR_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glRotatef(theta[0], 1.0, 0.0, 0.0);	//��x�b����S�w����
	glRotatef(theta[1], 0.0, 1.0, 0.0);	//��y�b����S�w����
	glRotatef(theta[2], 0.0, 0.0, 1.0);	//��z�b����S�w����

	//�w����ᤧ�y�жb
	draw_coordinates(1.5f);     //�e�y�жb

	draw_teapot(color_purple, 1.0f, 1.0f);	//�e����
	draw_cube(color_silver, 1.0f, 2.5f);	//cubic �~��
	draw_cube(color_purple, 1.0f, 3.0f);	//cubic �~��

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
		theta[0] = 0.0f;
		theta[1] = 0.0f;
		theta[2] = 0.0f;
		glutPostRedisplay();
		break;
	case 't':
		theta[0] = 45.0f;
		theta[1] = 45.0f;
		theta[2] = 45.0f;
		glutPostRedisplay();
		break;
	}
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
	const char* windowName = "Rotating Color Cube";
	const char* message = "��x, y, z ��ܱ���b, �� �ť��� �Ұ�, �� Esc ���}\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	glutIdleFunc(idle);         //�]�wcallback function, �Q��idle�ƥ�i�歫�e

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
