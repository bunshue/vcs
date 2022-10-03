//#include <GL/glut.h>      //32 bits
//#include <GL/freeglut.h>    //64 bits


//-----------------------------------------------------------------------------
//                                                              2008/6/26
//                          A First Sample Code
//                                                              by�٬O�s��
//-----------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <GL\glut.h>//�ϥ�DevC++���ܭn�אּ�ФJ #include <GL\openglut.h>

void WindowSize(int , int );            //�t�d������ø�Ϥ��e�����
void Keyboard(unsigned char , int, int );   //�����L��J
void Display(void);                     //�yø

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
   glutInitWindowSize(400,400);         //�������e
   glutInitWindowPosition(600,80);         //�������W������m
   glutCreateWindow("�o�̬O�������D");      //�إߵ���
   
   //�U���T�ӬO�Ψӫ��wCallback���
   glutReshapeFunc(WindowSize);
   glutKeyboardFunc(Keyboard);
   glutDisplayFunc(Display);
   glutMainLoop();
   return 0;
}

void Display(void)
{
   glClearColor(1.0, 1.0, 1.0, 1.0);   //�Υզ��I��
   glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   gluLookAt(0,0,10.0f,0,0,0,0,1,0);   //���u���y�ФΤ�V
   glBegin(GL_TRIANGLES);
      glColor3f( 1, 0, 0);glVertex3f( 8.6603, -5, 0);
      glColor3f( 0, 1, 0);glVertex3f(      0, 10, 0);
      glColor3f( 0, 0, 1);glVertex3f(-8.6603, -5, 0);
   glEnd();
   glutSwapBuffers();
}

void Keyboard(unsigned char key, int x, int y)
{
   printf("�A�ҫ����䪺�X�O%x\t���ɵ��������ƹ��y�ЬO(%d,%d)\n", key, x, y);
}

void WindowSize(int w, int h)
{
   printf("�ثe�����j�p��%dX%d\n",w,h);
   glViewport(0, 0, w, h);            //��������e���ܮɡA�e���]�����
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glOrtho(-10,10,-10,10,-10,10);      //�����v
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
} 

