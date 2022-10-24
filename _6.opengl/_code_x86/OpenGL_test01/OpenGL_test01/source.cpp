//#include <GL/freeglut.h>	//64位元用的
#include <GL/glut.h>		//32位元用的

#include <stdio.h>
#include <stdlib.h>

// 繪圖回調函數
void display()
{
	/*
	//用黃色塗背景	要兩行一起寫，若不寫，則是以黑色為背景
   glClearColor(1.0, 1.0, 0.0, 1.0);   
	glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);	//清除背景
   */

glPolygonMode(GL_FRONT, GL_LINE);

	float dd;

	glBegin(GL_QUADS);	//畫矩形
		//逆時針為空心
		//畫一個白色外框
		dd = 9.5f;
		glVertex3f(-dd, dd, 0.0f);	//左上
		glVertex3f(-dd, -dd, 0.0f);	//左下
		glVertex3f(dd, -dd, 0.0f);	//右下
		glVertex3f(dd, dd, 0.0f);	//右上

		//順時針為實心
		//畫一個白色實心矩形
		dd = 3.0f;
		glVertex3f(-dd, dd, 0.0f);	//左上
		glVertex3f(dd, dd, 0.0f);	//右上
		glVertex3f(dd, -dd, 0.0f);	//右下
		glVertex3f(-dd, -dd, 0.0f);	//左下
	glEnd();

	glBegin(GL_TRIANGLES);	//畫三角形 2D
		glColor3f(1.0, 0.0, 0.0);	//R
		//逆時針為空心
		glVertex2f(2.0, 4.0);	//左下
		glVertex2f(8.0, 4.0);	//右下
		glVertex2f(5.0, 9.0);	//上
	glEnd();

	glBegin(GL_TRIANGLES);	//畫三角形 3D
		//逆時針為空心
		for(dd = 7.0f;dd<=9.0f;dd+=1.0f)
		{
			glColor3f( 1, 0, 0);	//R
			glVertex3f( dd, -dd, 0);	//右下
			glColor3f( 0, 1, 0);	//G
			glVertex3f( 0, dd, 0);	//上
			glColor3f( 0, 0, 1);	//B
			glVertex3f(-dd, -dd, 0);	//左下
		}

		/*
		//順時針為實心
		dd = 1.0f;
		{
			glColor3f( 0, 0, 1);	//B
			glVertex3f(-dd, -dd, 0);	//左下
			glColor3f( 0, 1, 0);	//G
			glVertex3f( 0, dd, 0);	//上
			glColor3f( 1, 0, 0);	//R
			glVertex3f( dd, -dd, 0);	//右下
		}
		*/
	glEnd();

	//畫矩形
	float x_st = -8.0f;
	float y_st = 2.0f;
	float w = 4.0f;
	float h = 4.0f;
	     //左下x,  左下y,  右上x,  右上y
	glRectf(x_st, y_st, x_st+w, y_st+h);

	for(dd = 1.0f;dd<=2.0f;dd+=0.5f)
	{
		      //左下x,  左下y,  右上x,  右上y
		//glRectf(dd, dd, dd+3.0f, dd+3.0f);
		glRectf(x_st+dd, y_st+dd, x_st+w+dd, y_st+h+dd);
	}

	glFlush();
	glutSwapBuffers();
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

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
//glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

   glutCreateWindow("這裡是視窗標題");      // 設定視窗標題

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

	glutMainLoop();	// 開始主循環繪制
	
   return 0;
}	
