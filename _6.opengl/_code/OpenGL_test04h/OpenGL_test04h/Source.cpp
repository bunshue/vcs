#include "../../Common.h"

static int slices = 16;
static int stacks = 16;

// 繪圖回調函數
void display(void)
{
	const double t = glutGet(GLUT_ELAPSED_TIME) / 1000.0;
	const double a = t * 90.0;

	glClear(GL_COLOR_BUFFER_BIT);
	glColor3d(1, 0, 0);

	glPushMatrix();
	glTranslated(-2.4, -1.2, -6);
	draw_coordinates(1.1f);     //畫座標軸
	glColor3d(1, 0, 0);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);	//轉動
	glutWireSphere(1, slices, stacks);		//畫 網格 球
	glPopMatrix();

	glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	const float ar = (float)w / (float)h;

	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣
	glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣
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

	case '+':
		slices++;
		stacks++;
		break;

	case '-':
		if (slices > 3 && stacks > 3)
		{
			slices--;
			stacks--;
		}
		break;
	}

	glutPostRedisplay();
}

static void idle(void)
{
	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	const char* windowName = "球體旋轉";
	const char* message = "球體旋轉, 無控制, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 640, 480, 1100, 200, display, reshape, keyboard);

	glutIdleFunc(idle);			//設定callback function

	glClearColor(1, 1, 1, 1);	//白色背景

	glutMainLoop();	//開始主循環繪製

	return 0;
}


