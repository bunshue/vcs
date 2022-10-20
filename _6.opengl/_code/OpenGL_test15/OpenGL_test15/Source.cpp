#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void init(void)
{
}

// 繪圖回調函數
void display(void)
{
	glPushMatrix();

	glClearColor(1.0, 0.0, 0.0, 1.0);	//使用紅色背景
	glClear(GL_COLOR_BUFFER_BIT);

	// 設置當前的繪制顏色 , 4 個 unsigned byte 
	// 每個顏色的分量占一個字節
	// 參數數據是 R 紅色 G 綠色 B 藍色 A 透明度
	// 下面設置的含義是白色, 繪制點的時候, 每次都使用白色繪制
	glColor4ub(255, 255, 255, 255);

	glLineWidth(4.0f);	// 設置線的寬度

	// 繪制線時, 會將從 glBegin 到 glEnd 之間的所有的點都繪制出來
	// 可以調用 glVertex3f 方法 成對 設置多條線
	// 注意必須成對設置 , 如果設置奇數個點 , 最后一個點會被丟棄

	glBegin(GL_LINES);	// 繪制線段開始

	// glVertex3f (GLfloat x, GLfloat y, GLfloat z)
	//畫直線, 每兩個點組成一條線

	glVertex3f(0.0f, 0.0f, -1.0f);
	glVertex3f(-1.0f, 0.0f, -1.0f);

	glVertex3f(-0.8f, -0.8f, 0.0f);
	glVertex3f(0.8f, 0.8f, 0.0f);

	float xx = 0.0f;
	float yy = 0.0f;
	float dx = 0.0f;
	float dy = 0.0f;
	for (xx = -0.8f; xx <= 0.8f; xx += 0.1f)
	{
		dx = xx + 0.8;
		glVertex3f(-0.8f + dx, -0.8f, 0.0f);
		dy = xx + 0.8;
		glVertex3f(-0.8f, 0.8f - dy, 0.0f);
	}
	glEnd();	// 繪制點結束


	//兩個線段組合成一個閉合三角形
	glBegin(GL_LINE_LOOP);	// 繪制線段開始

	glVertex3f(0.7f, 0.5f, 0.0f);
	glVertex3f(0.7f, 0.1f, 0.0f);

	glVertex3f(0.7f, 0.1f, 0.0f);
	glVertex3f(0.3f, 0.1f, 0.0f);

	glEnd();	// 繪制點結束



	//繪製彩色的線
	glLineWidth(12.0f);

	glBegin(GL_LINE_LOOP);

	// 繪制線 , 每兩個點組成一條線
// glVertex3f (GLfloat x, GLfloat y, GLfloat z)
	glVertex3f(0.0f, -0.8f, 0.0f);

	// 設置綠色 
	glColor4ub(0, 255, 0, 255);

	glVertex3f(0.8f, -0.8f, 0.0f);

	// 上面的設置會從 (0,0,-10) 坐標向 (-5,0,-10) 坐標繪制一條線

	// 設置藍色
	glColor4ub(0, 0, 255, 255);

	//glVertex3f(-5.0f, 0.0f, -10.0f);
	glVertex3f(0.8f, 0.3f, 0.0f);

	glColor4ub(255, 255, 255, 255);

	// 上面的設置會從 (-5,0,-10) 坐標向 (-5,-2,-10) 坐標繪制一條線

		// 繪制點結束
	glEnd();



	glPopMatrix();

	// 將后緩沖區繪制到前臺
	glutSwapBuffers();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
}

void keyboard(unsigned char k, int /*x*/, int /*y*/)
{
	switch (k)
	{
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	//glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	init();

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function

	glutMainLoop();

	return 0;
}
