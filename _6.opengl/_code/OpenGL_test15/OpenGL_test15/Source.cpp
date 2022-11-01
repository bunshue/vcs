#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void draw_window_boundary(float* color, float dd)
{
	//用 GL_LINE_LOOP 畫一個空心矩形
	//glColor3f(0.0, 1.0, 0.0);
	glColor3fv((GLfloat*)color);
	float point1[3] = { -dd, -dd, 0 };	//左下
	float point2[3] = { dd, -dd, 0 };		//右下
	float point3[3] = { dd,  dd, 0 };		//右上
	float point4[3] = { -dd,  dd, 0 };	//左上
	glBegin(GL_LINE_LOOP);
	glVertex3fv(point1);	//左下
	glVertex3fv(point2);	//右下
	glVertex3fv(point3);	//右上
	glVertex3fv(point4);	//左上
	glEnd();
}

void draw_coordinates(float len)
{
	glLineWidth(3.0f);	//設定線寬

	glColor3f(1.0f, 0.0f, 0.0f); //畫紅色的x軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(len, 0.0f, 0.0f);	//x軸 len,0,0
	glEnd();

	glColor3f(0.0, 1.0, 0.0); //畫綠色的y軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(0.0f, len, 0.0f);	//y軸 0,len,0
	glEnd();

	glColor3f(0.0, 0.0, 1.0); //畫藍色的z軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(0.0f, 0.0f, len);	//z軸 0,0,len
	glEnd();
}

// 繪圖回調函數
void display(void)
{
	glPushMatrix();		//這個 Matrix Push/Pop 好像沒什麼用??

	glClearColor(1.0, 0.0, 0.0, 1.0);	//使用紅色背景
	glClear(GL_COLOR_BUFFER_BIT);

	// 設置當前的繪製顏色 , 4 個 unsigned byte 
	// 每個顏色的分量占一個字節
	// 參數數據是 R 紅色 G 綠色 B 藍色 A 透明度
	// 下面設置的含義是白色, 繪製點的時候, 每次都使用白色繪製
	glColor4ub(255, 255, 255, 255);

	//畫視窗邊界
	float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
	draw_window_boundary(color_yellow, 0.9);

	draw_coordinates(0.9);

	glLineWidth(4.0f);	//設定線寬

	// 繪製線時, 會將從 glBegin 到 glEnd 之間的所有的點都繪製出來
	// 可以調用 glVertex3f 方法 成對 設置多條線
	// 注意必須成對設置 , 如果設置奇數個點 , 最後一個點會被丟棄

	glBegin(GL_LINES);	// 繪製線段開始

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
	glEnd();	// 繪製點結束

	//兩個線段組合成一個閉合三角形
	glBegin(GL_LINE_LOOP);	// 繪製線段開始

	glVertex3f(0.7f, 0.5f, 0.0f);
	glVertex3f(0.7f, 0.1f, 0.0f);

	glVertex3f(0.7f, 0.1f, 0.0f);
	glVertex3f(0.3f, 0.1f, 0.0f);

	glEnd();	// 繪製點結束


	//繪製彩色的線

	glLineWidth(12.0f);	//設定線寬

	glBegin(GL_LINE_LOOP);

	// 繪製線 , 每兩個點組成一條線
// glVertex3f (GLfloat x, GLfloat y, GLfloat z)
	glVertex3f(0.0f, -0.8f, 0.0f);

	// 設置綠色 
	glColor4ub(0, 255, 0, 255);

	glVertex3f(0.8f, -0.8f, 0.0f);

	// 上面的設置會從 (0,0,-10) 座標向 (-5,0,-10) 座標繪製一條線

	// 設置藍色
	glColor4ub(0, 0, 255, 255);

	//glVertex3f(-5.0f, 0.0f, -10.0f);
	glVertex3f(0.8f, 0.3f, 0.0f);

	glColor4ub(255, 255, 255, 255);

	// 上面的設置會從 (-5,0,-10) 座標向 (-5,-2,-10) 座標繪製一條線

		// 繪製點結束
	glEnd();

	glPopMatrix();

	// 將後緩沖區繪製到前臺
	glutSwapBuffers();
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
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
	
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function

	glutMainLoop();	//開始主循環繪製

	return 0;
}
