#include <GL/glut.h>      //32 bits
//#include <GL/freeglut.h>    //64 bits

#include <stdio.h>
#include <stdlib.h>

//�����L��J
void keyboard(unsigned char key, int x, int y)
{
   //printf("�A�ҫ����䪺�X�O%x\t���ɵ��������ƹ��y�ЬO(%d,%d)\n", key, x, y);

	switch (key)
{
    case 27:
        exit(0);
    case '1':
        break;
    case '2':
        break;
    case 'r':
        break;
}
}

//�t�d������ø�Ϥ��e�����
void reshape(int w, int h)
{
   printf("�ثe�����j�p��%dX%d\n",w,h);
   glViewport(0, 0, w, h);            //��������e���ܮɡA�e���]�����
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glOrtho(-10,10,-10,10,-10,10);      //�����v
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
} 

//�yø
void display(void)
{
	/*
	//�ζ����I��	�n���@�_�g�A�Y���g�A�h�O�H�¦⬰�I��
   glClearColor(1.0, 1.0, 0.0, 1.0);   
   glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);
   */

glPolygonMode(GL_FRONT, GL_LINE);

glBegin(GL_QUADS);	//�e�x��
	//�f�ɰw���Ť�
	glVertex3f(-9.0f, 9.0f, 0.0f);	//���W
	glVertex3f(-9.0f, -9.0f, 0.0f);	//���U
	glVertex3f(9.0f, -9.0f, 0.0f);	//�k�U
	glVertex3f(9.0f, 9.0f, 0.0f);	//�k�W

	//���ɰw�����
	glVertex3f(-3.0f, 3.0f, 0.0f);	//���W
	glVertex3f(3.0f, 3.0f, 0.0f);	//�k�W
	glVertex3f(3.0f, -3.0f, 0.0f);	//�k�U
	glVertex3f(-3.0f, -3.0f, 0.0f);	//���U

glEnd();

	glBegin(GL_TRIANGLES);	//�e�T���� 3D
		//�f�ɰw���Ť�
		glColor3f( 1, 0, 0);glVertex3f( 8, -8, 0);	//R �k�U
		glColor3f( 0, 1, 0);glVertex3f( 0, 8, 0);	//G �W
		glColor3f( 0, 0, 1);glVertex3f(-8, -8, 0);	//B ���U

		//���ɰw�����
		glColor3f( 0, 0, 1);glVertex3f(-3, -7, 0);	//B ���U
		glColor3f( 0, 1, 0);glVertex3f( 0, -2, 0);	//G �W
		glColor3f( 1, 0, 0);glVertex3f( 3, -7, 0);	//R �k�U

	glEnd();

	glBegin(GL_TRIANGLES);	//�e�T���� 2D
		glColor3f(1.0, 0.0, 0.0);	//R
		//�f�ɰw���Ť�
		glVertex2f(2.0, 4.0);	//���U
		glVertex2f(8.0, 4.0);	//�k�U
		glVertex2f(5.0, 9.0);	//�W
	glEnd();


	//�M���I��
	//glClear(GL_COLOR_BUFFER_BIT);
	//�e�@�ӯx��

	     //���Ux,  ���Uy,  �k�Wx,  �k�Wy
	glRectf(-8.0f, 4.0f, -4.0f, 8.0f);
	glRectf(-0.5f, -0.5f, 0.5f, 0.5f);

	glFlush();
	glutSwapBuffers();
}

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
//glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

   glutInitWindowSize(600,600);         //�������e
   glutInitWindowPosition(1100,200);         //�������W������m

   glutCreateWindow("�o�̬O�������D");      //�إߵ���

    glutDisplayFunc(display);       //�]�wcallback function
    glutReshapeFunc(reshape);       //�]�wcallback function
    glutKeyboardFunc(keyboard);     //�]�wcallback function

   glutMainLoop();
   return 0;
}	
