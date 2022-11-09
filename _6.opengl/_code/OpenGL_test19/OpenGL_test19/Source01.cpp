//#include "../../../_code/Common.h"    //32 bits
#include "../../Common.h"               //64 bits

// ø�Ϧ^�ը��
void display()
{
	/*
	//�ζ����I��	�n���@�_�g�A�Y���g�A�h�O�H�¦⬰�I��
   glClearColor(1.0, 1.0, 0.0, 1.0);
	glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);	//�M���I��
   */

	glPolygonMode(GL_FRONT, GL_LINE);

	draw_boundary(color_y, 9.6f); //�e�������

	float dd;
	glColor3f(1.0, 1.0, 1.0);	//White
	glBegin(GL_QUADS);	//�e�x��
	//�f�ɰw���Ť�
	//�e�@�ӥզ�~��
	dd = 9.4f;
	glVertex3f(-dd, dd, 0.0f);	//���W
	glVertex3f(-dd, -dd, 0.0f);	//���U
	glVertex3f(dd, -dd, 0.0f);	//�k�U
	glVertex3f(dd, dd, 0.0f);	//�k�W

	//���ɰw�����
	//�e�@�ӥզ��߯x��
	dd = 3.0f;
	glVertex3f(-dd, dd, 0.0f);	//���W
	glVertex3f(dd, dd, 0.0f);	//�k�W
	glVertex3f(dd, -dd, 0.0f);	//�k�U
	glVertex3f(-dd, -dd, 0.0f);	//���U
	glEnd();

	//�e�T���� 2D
	glBegin(GL_TRIANGLES);
	glColor3f(1.0, 0.0, 0.0);	//R
	//�f�ɰw���Ť�
	glVertex2f(2.0, 4.0);	//���U
	glVertex2f(8.0, 4.0);	//�k�U
	glVertex2f(5.0, 9.0);	//�W
	glEnd();

	//�e�T���� 3D
	glBegin(GL_TRIANGLES);
	//�f�ɰw���Ť�
	for (dd = 7.0f; dd <= 9.0f; dd += 1.0f)
	{
		glColor3f(1, 0, 0);	//R
		glVertex3f(dd, -dd, 0);	//�k�U
		glColor3f(0, 1, 0);	//G
		glVertex3f(0, dd, 0);	//�W
		glColor3f(0, 0, 1);	//B
		glVertex3f(-dd, -dd, 0);	//���U
	}

	/*
	//���ɰw�����
	dd = 1.0f;
	{
		glColor3f( 0, 0, 1);	//B
		glVertex3f(-dd, -dd, 0);	//���U
		glColor3f( 0, 1, 0);	//G
		glVertex3f( 0, dd, 0);	//�W
		glColor3f( 1, 0, 0);	//R
		glVertex3f( dd, -dd, 0);	//�k�U
	}
	*/
	glEnd();

	//�e�x��
	float x_st = -8.0f;
	float y_st = 2.0f;
	float w = 4.0f;
	float h = 4.0f;
	//���Ux,  ���Uy,  �k�Wx,  �k�Wy
	glRectf(x_st, y_st, x_st + w, y_st + h);

	for (dd = 1.0f; dd <= 2.0f; dd += 0.5f)
	{
		//���Ux,  ���Uy,  �k�Wx,  �k�Wy
		//glRectf(dd, dd, dd+3.0f, dd+3.0f);
		glRectf(x_st + dd, y_st + dd, x_st + w + dd, y_st + h + dd);
	}

	glFlush();
}

// ���f�j�p�ܤƦ^�ը��, �t�d������ø�Ϥ��e�����
void reshape(int w, int h)
{
	//printf("�ثe�����j�p�� %d X %d\n", w, h);
	glViewport(0, 0, w, h);            //��������e���ܮɡA�e���]�����
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//�]�m���x�}
	glOrtho(-10, 10, -10, 10, -10, 10);      //�����v
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//�]�m���x�}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

	glutInitWindowSize(600, 600);       // �]�w�����j�p
	glutInitWindowPosition(1100, 200);  // �]�w������m

	glutCreateWindow("�o�̬O�������D");      //�}�ҵ��� ����ܥX���� Title

	glutDisplayFunc(display);       //�]�wcallback function
	glutReshapeFunc(reshape);       //�]�wcallback function
	glutKeyboardFunc(keyboard0);	//�]�wcallback function

	printf("�����, �L����, �� Esc ���}\n");

	glutMainLoop();	//�}�l�D�`��ø�s

	return 0;
}
