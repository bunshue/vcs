
//���ջy�k�M��

#include "../../Common.h"

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //���϶¦�

	glLoadIdentity();
	gluOrtho2D(-5, 5, -5, 5);
	
	glRecti(0, 0, 4, 4);

    glFlush();  // ����ø�ϩR�O
}

void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		printf("�ƹ����� + ���U\n");
	}
	else if (button == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
	{
		printf("�ƹ����� + ���U\n");
	}
	else if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
	{
		printf("�ƹ��k�� + ���U\n");
	}
	else if (button == GLUT_LEFT_BUTTON && state == GLUT_UP)
	{
		printf("�ƹ����� + ��}\n");
	}
	else if (button == GLUT_MIDDLE_BUTTON && state == GLUT_UP)
	{
		printf("�ƹ����� + ��}\n");
	}
	else if (button == GLUT_RIGHT_BUTTON && state == GLUT_UP)
	{
		printf("�ƹ��k�� + ��}\n");
	}
	else if (button == 3 && state == GLUT_DOWN)
	{
		printf("�ƹ��u���V�W + �}�l\n");
	}
	else if (button == 3 && state == GLUT_UP)
	{
		printf("�ƹ��u���V�W + ����\n");
	}
	else if (button == 4 && state == GLUT_DOWN)
	{
		printf("�ƹ��u���V�U + �}�l\n");
	}
	else if (button == 4 && state == GLUT_UP)
	{
		printf("�ƹ��u���V�U + ����\n");
	}
	else
	{
		printf("��L�ƹ��ʧ@ %d %d @(%d, %d)\t", button, state, x, y);
	}
}

int main(int argc, char** argv)
{
    const char* windowName = "���ջy�k";
    const char* message = "���ջy�k �M��, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMouseFunc(mouse);		//�]�wcallback function
    //glutMotionFunc(motion);		//�]�wcallback function

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

