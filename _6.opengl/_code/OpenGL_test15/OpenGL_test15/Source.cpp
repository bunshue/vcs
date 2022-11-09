//#include "../../../_code/Common.h"    //32 bits
#include "../../Common.h"               //64 bits

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
	glColor4ub(255, 255, 255, 255);	//設定顏色 White

	draw_boundary(color_y, 0.9f); //畫視窗邊界

	draw_coordinates(0.9f);

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
		dx = xx + 0.8f;
		glVertex3f(-0.8f + dx, -0.8f, 0.0f);
		dy = xx + 0.8f;
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
	glVertex3f(0.0f, -0.8f, 0.0f);

	glColor4ub(0, 255, 0, 255);	//設定顏色 G, 用256制

	glVertex3f(0.8f, -0.8f, 0.0f);

	// 上面的設置會從 (0,0,-10) 座標向 (-5,0,-10) 座標繪製一條線

	glColor4ub(0, 0, 255, 255);	//設定顏色 B, 用256制

	//glVertex3f(-5.0f, 0.0f, -10.0f);
	glVertex3f(0.8f, 0.3f, 0.0f);

	glColor4ub(255, 255, 255, 255);//設定顏色 White

	// 上面的設置會從 (-5,0,-10) 座標向 (-5,-2,-10) 座標繪製一條線

	glEnd();	// 繪製點結束

	glPopMatrix();

	glFlush();  // 執行繪圖命令
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);       // 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutKeyboardFunc(keyboard0);	//設定callback function

	printf("僅顯示, 無控制, 按 Esc 離開\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}
