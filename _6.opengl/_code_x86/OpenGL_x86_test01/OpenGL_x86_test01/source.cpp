//#include <GL/glut.h>      //32 bits
//#include <GL/freeglut.h>    //64 bits


//-----------------------------------------------------------------------------
//                                                              2008/6/26
//                          A First Sample Code
//                                                              by還是零分
//-----------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <GL\glut.h>//使用DevC++的話要改為標入 #include <GL\openglut.h>

void WindowSize(int , int );            //負責視窗及繪圖內容的比例
void Keyboard(unsigned char , int, int );   //獲取鍵盤輸入
void Display(void);                     //描繪

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
   glutInitWindowSize(400,400);         //視窗長寬
   glutInitWindowPosition(600,80);         //視窗左上角的位置
   glutCreateWindow("這裡是視窗標題");      //建立視窗
   
   //下面三個是用來指定Callback函數
   glutReshapeFunc(WindowSize);
   glutKeyboardFunc(Keyboard);
   glutDisplayFunc(Display);
   glutMainLoop();
   return 0;
}

void Display(void)
{
   glClearColor(1.0, 1.0, 1.0, 1.0);   //用白色塗背景
   glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   gluLookAt(0,0,10.0f,0,0,0,0,1,0);   //視線的座標及方向
   glBegin(GL_TRIANGLES);
      glColor3f( 1, 0, 0);glVertex3f( 8.6603, -5, 0);
      glColor3f( 0, 1, 0);glVertex3f(      0, 10, 0);
      glColor3f( 0, 0, 1);glVertex3f(-8.6603, -5, 0);
   glEnd();
   glutSwapBuffers();
}

void Keyboard(unsigned char key, int x, int y)
{
   printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);
}

void WindowSize(int w, int h)
{
   printf("目前視窗大小為%dX%d\n",w,h);
   glViewport(0, 0, w, h);            //當視窗長寬改變時，畫面也跟著變
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glOrtho(-10,10,-10,10,-10,10);      //正交投影
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
} 

