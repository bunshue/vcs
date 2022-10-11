#include <GL/glut.h>      //32 bits
//#include <GL/freeglut.h>    //64 bits

#include <stdio.h>
#include <stdlib.h>

//獲取鍵盤輸入
void keyboard(unsigned char key, int x, int y)
{
   //printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

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

//負責視窗及繪圖內容的比例
void reshape(int w, int h)
{
   printf("目前視窗大小為%dX%d\n",w,h);
   glViewport(0, 0, w, h);            //當視窗長寬改變時，畫面也跟著變
   glMatrixMode(GL_PROJECTION);
   glLoadIdentity();
   glOrtho(-10,10,-10,10,-10,10);      //正交投影
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
} 

//描繪
void display(void)
{
	/*
	//用黃色塗背景	要兩行一起寫，若不寫，則是以黑色為背景
   glClearColor(1.0, 1.0, 0.0, 1.0);   
   glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);
   */

glPolygonMode(GL_FRONT, GL_LINE);

glBegin(GL_QUADS);	//畫矩形
	//逆時針為空心
	glVertex3f(-9.0f, 9.0f, 0.0f);	//左上
	glVertex3f(-9.0f, -9.0f, 0.0f);	//左下
	glVertex3f(9.0f, -9.0f, 0.0f);	//右下
	glVertex3f(9.0f, 9.0f, 0.0f);	//右上

	//順時針為實心
	glVertex3f(-3.0f, 3.0f, 0.0f);	//左上
	glVertex3f(3.0f, 3.0f, 0.0f);	//右上
	glVertex3f(3.0f, -3.0f, 0.0f);	//右下
	glVertex3f(-3.0f, -3.0f, 0.0f);	//左下

glEnd();

	glBegin(GL_TRIANGLES);	//畫三角形 3D
		//逆時針為空心
		glColor3f( 1, 0, 0);glVertex3f( 8, -8, 0);	//R 右下
		glColor3f( 0, 1, 0);glVertex3f( 0, 8, 0);	//G 上
		glColor3f( 0, 0, 1);glVertex3f(-8, -8, 0);	//B 左下

		//順時針為實心
		glColor3f( 0, 0, 1);glVertex3f(-3, -7, 0);	//B 左下
		glColor3f( 0, 1, 0);glVertex3f( 0, -2, 0);	//G 上
		glColor3f( 1, 0, 0);glVertex3f( 3, -7, 0);	//R 右下

	glEnd();

	glBegin(GL_TRIANGLES);	//畫三角形 2D
		glColor3f(1.0, 0.0, 0.0);	//R
		//逆時針為空心
		glVertex2f(2.0, 4.0);	//左下
		glVertex2f(8.0, 4.0);	//右下
		glVertex2f(5.0, 9.0);	//上
	glEnd();


	//清除背景
	//glClear(GL_COLOR_BUFFER_BIT);
	//畫一個矩形

	     //左下x,  左下y,  右上x,  右上y
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

   glutInitWindowSize(600,600);         //視窗長寬
   glutInitWindowPosition(1100,200);         //視窗左上角的位置

   glutCreateWindow("這裡是視窗標題");      //建立視窗

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

   glutMainLoop();
   return 0;
}	
