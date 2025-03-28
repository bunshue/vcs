﻿#include "../../Common.h"

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
	int viewportw = W;
	int viewporth = H;

	//畫分割線，分成四個視見區, 以畫素為單位
	glViewport(viewportx, viewporty, viewportw, viewporth);		//視口設定為全部視窗
												//後面這兩個參數是高度和寬度，而不是座標
	printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\t全部\n", viewportx, viewporty, viewportw, viewporth);

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

	draw_rectangle(color_b, 3, -0.93f, -0.93f, 1.86f, 1.86f);    //左下開始 w h

	draw_teapot(color_r, 1, 0.5 / 2);   //畫一個茶壺

	//定義在左下角的區域, 紅色方塊
	glColor3f(1.0, 0.0, 0.0);	//紅色
	viewportx = 0;
	viewporty = 0;
	viewportw = W / 2;
	viewporth = H / 2;
	glViewport(viewportx, viewporty, viewportw, viewporth);	//視口設定為全部視窗的左下四分之一
	printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\t左下\n", viewportx, viewporty, viewportw, viewporth);

	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();
	draw_teapot(color_g, 1, 0.5);   //畫一個茶壺

	//定義在左上角的區域, 綠色方塊
	glColor3f(0.0, 1.0, 0.0);	//綠色
	viewportx = 0;
	viewporty = H / 2;
	viewportw = W / 2;
	viewporth = H / 2;
	glViewport(viewportx, viewporty, viewportw, viewporth);	//視口設定為全部視窗的左上四分之一
	printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\t左上\n", viewportx, viewporty, viewportw, viewporth);

	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();
	draw_teapot(color_b, 1, 0.5);   //畫一個茶壺

	//定義在右上角的區域, 藍色方塊
	glColor3f(0.0, 0.0, 1.0);	//藍色
	viewportx = W / 2;
	viewporty = H / 2;
	viewportw = W / 2;
	viewporth = H / 2;
	glViewport(viewportx, viewporty, viewportw, viewporth);	//視口設定為全部視窗的右上四分之一
	printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\t右上\n", viewportx, viewporty, viewportw, viewporth);

	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();
	draw_teapot(color_y, 1, 0.5);   //畫一個茶壺

	//定義在右下角的區域, 黃色方塊
	glColor3f(1.0, 1.0, 0.0);	//黃色
	viewportx = W / 2;
	viewporty = 0;
	viewportw = W / 2;
	viewporth = H / 2;
	glViewport(viewportx, viewporty, viewportw, viewporth);	//視口設定為全部視窗的右下四分之一
	printf("把所有要畫的東西顯示在視窗的(%d ,%d)開始的(%d, %d)\t右下\n", viewportx, viewporty, viewportw, viewporth);

	glBegin(GL_POLYGON);	//畫實心多邊形
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();
	draw_teapot(color_r, 1, 0.5);   //畫一個茶壺

	glFlush();  // 執行繪圖命令
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
	switch (key)
	{
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;

	case '0':
		printf("0\n");
		break;

	case '1':
		printf("1\n");
		break;

	case '2':
		printf("2\n");
		break;

	case '3':
		printf("3\n");
		break;

	case '4':
		printf("4\n");
		break;

	case '?':
		break;
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

	glutDisplayFunc(display);		//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function

	printf("僅顯示, 無控制, 按 Esc 離開\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}

