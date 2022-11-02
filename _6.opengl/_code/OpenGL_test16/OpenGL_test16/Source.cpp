#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

int W = 600;
int H = 600;

// 初始化參數
void init(void)
{
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣

	//定義剪裁面
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0);	//窗口座標範圍, 2D	//應該是預設就是這樣的數字
}

// 繪圖回調函數
void display(void)
{
	//glMatrixMode( GL_MODELVIEW );
	//glLoadIdentity();	//設置單位矩陣

	glClear(GL_COLOR_BUFFER_BIT);

	int viewportx = 0;
	int viewporty = 0;
	//畫分割線，分成四個視見區
	glViewport(viewportx, viewporty, W, H);		//視口設定為全部視窗
												//後面這兩個參數是高度和寬度，而不是座標
	glBegin(GL_LINES);
	//畫紅色橫線
	glColor3f(1.0, 0.0, 0.0);	//紅色
	glVertex2f(-1.0, 0);	//畫橫線
	glVertex2f(1.0, 0);

	//畫綠色直線
	glColor3f(0.0, 1.0, 0.0);	//綠色
	glVertex2f(0.0, -1.0);	//畫直線
	glVertex2f(0.0, 1.0);
	glEnd();

	/* 畫一個範圍矩形, TBD
	//畫一個矩形 B
	glColor3f(0.0, 0.0, 1.0);	//設置畫筆顏色為 B
	//左下x,左下y,右上x,右上y,
	glRectf(-0.9f, -0.9f, -0.3f, 0.9f);//畫一個矩形
	*/

	//定義在左下角的區域, 紅色方塊
	glColor3f(1.0, 0.0, 0.0);	//紅色
	viewportx = 0;
	viewporty = 0;
	glViewport(viewportx, viewporty, W / 2, H / 2);	//視口設定為全部視窗的左下四分之一
	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();

	//定義在左上角的區域, 綠色方塊
	glColor3f(0.0, 1.0, 0.0);	//綠色
	viewportx = 0;
	viewporty = H / 2;
	glViewport(viewportx, viewporty, W / 2, H / 2);//視口設定為全部視窗的左上四分之一
	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();

	//定義在右上角的區域, 藍色方塊
	glColor3f(0.0, 0.0, 1.0);	//藍色
	viewportx = W / 2;
	viewporty = H / 2;
	glViewport(viewportx, viewporty, W / 2, H / 2);	//視口設定為全部視窗的右上四分之一
	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();

	//定義在右下角的區域, 黃色方塊
	glColor3f(1.0, 1.0, 0.0);	//黃色
	viewportx = W / 2;
	viewporty = 0;
	glViewport(viewportx, viewporty, W / 2, H / 2);	//視口設定為全部視窗的右下四分之一
	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();

	glFlush();
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

	glutInitWindowSize(W, H);			// 設定視窗大小
	glutInitWindowPosition(1100, 200);	// 設定視窗位置

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	init();

	glutDisplayFunc(display);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function

	printf("僅顯示, 無控制, 按 Esc 離開\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}

