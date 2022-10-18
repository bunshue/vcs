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

	// 设置当前的绘制颜色 , 4 个 unsigned byte 
	// 每个颜色的分量占一个字节
	// 参数数据是 R 红色 G 绿色 B 蓝色 A 透明度
	// 下面设置的含义是白色, 绘制点的时候, 每次都使用白色绘制
	glColor4ub(255, 255, 255, 255);

	glLineWidth(4.0f);	// 设置线的宽度

	// 绘制线时, 会将从 glBegin 到 glEnd 之间的所有的点都绘制出来
	// 可以调用 glVertex3f 方法 成对 设置多条线
	// 注意必须成对设置 , 如果设置奇数个点 , 最后一个点会被丢弃
	
	glBegin(GL_LINES);	// 绘制线段开始

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
	glEnd();	// 绘制点结束


	//兩個線段組合成一個閉合三角形
	glBegin(GL_LINE_LOOP);	// 绘制线段开始

	glVertex3f(0.7f, 0.5f, 0.0f);
	glVertex3f(0.7f, 0.1f, 0.0f);

	glVertex3f(0.7f, 0.1f, 0.0f);
	glVertex3f(0.3f, 0.1f, 0.0f);

	glEnd();	// 绘制点结束



	//繪製彩色的線
	glLineWidth(12.0f);

	glBegin(GL_LINE_LOOP);

	// 绘制线 , 每两个点组成一条线
// glVertex3f (GLfloat x, GLfloat y, GLfloat z)
	glVertex3f(0.0f, -0.8f, 0.0f);

	// 设置绿色 
	glColor4ub(0, 255, 0, 255);

	glVertex3f(0.8f, -0.8f, 0.0f);

	// 上面的设置会从 (0,0,-10) 坐标向 (-5,0,-10) 坐标绘制一条线

	// 设置蓝色
	glColor4ub(0, 0, 255, 255);

	//glVertex3f(-5.0f, 0.0f, -10.0f);
	glVertex3f(0.8f, 0.3f, 0.0f);

	glColor4ub(255, 255, 255, 255);

	// 上面的设置会从 (-5,0,-10) 坐标向 (-5,-2,-10) 坐标绘制一条线

		// 绘制点结束
	glEnd();



    glPopMatrix();

	// 将后缓冲区绘制到前台
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

	case '1':
		printf("1\n");
		break;

	case '2':
		printf("2\n");
		break;

	case '3':
		break;

	case '4':
		break;

	case '?':
		break;
	}
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
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
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function

    glutMainLoop();
	
    return 0;
}
