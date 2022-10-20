#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

int W = 600;
int H = 600;

// 初始化參數
void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glColor3f(1.0, 1.0, 1.0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	//定義剪裁面
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0);	//應該是預設就是這樣的數字
}

// 繪圖回調函數
void display(void)
{
	//glMatrixMode( GL_MODELVIEW );
	//glLoadIdentity();

	glClear(GL_COLOR_BUFFER_BIT);

	int viewportx = 0;
	int viewporty = 0;
	//畫分割線，分成四個視見區
	glViewport(viewportx, viewporty, W, H);		//視口設定為全部視窗
												//後面這兩個參數是高度和寬度，而不是座標

	glBegin(GL_LINES);
	glColor3f(1.0, 0.0, 0.0);	//紅色
	glVertex2f(-1.0, 0);	//畫橫線
	glVertex2f(1.0, 0);

	glColor3f(0.0, 1.0, 0.0);	//綠色
	glVertex2f(0.0, -1.0);	//畫直線
	glVertex2f(0.0, 1.0);
	glEnd();

	//定義在左下角的區域, 綠色方塊
	glColor3f(0.0, 1.0, 0.0);	//綠色

	viewportx = 0;
	viewporty = 0;
	glViewport(viewportx, viewporty, W / 2, H / 2);	//視口設定為全部視窗的左下四分之一
	glBegin(GL_POLYGON);
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
	glBegin(GL_POLYGON);
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();

	//定義在左上角的區域, 桃紅色方塊
	glColor3f(1.0, 0.0, 1.0);	//桃紅色
	viewportx = 0;
	viewporty = H / 2;
	glViewport(viewportx, viewporty, W / 2, H / 2);//視口設定為全部視窗的左上四分之一
	glBegin(GL_POLYGON);
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
	glBegin(GL_POLYGON);
	glVertex2f(-0.5, -0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glEnd();

	glFlush();
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

	glutInitWindowSize(W, H);
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

