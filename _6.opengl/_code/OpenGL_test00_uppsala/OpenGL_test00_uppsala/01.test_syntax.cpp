
//測試語法專用

#include "../../Common.h"

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //全圖黑色

	glLoadIdentity();
	gluOrtho2D(-5, 5, -5, 5);
	
	glRecti(0, 0, 4, 4);

    glFlush();  // 執行繪圖命令
}

void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		printf("滑鼠左鍵 + 按下\n");
	}
	else if (button == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
	{
		printf("滑鼠中鍵 + 按下\n");
	}
	else if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
	{
		printf("滑鼠右鍵 + 按下\n");
	}
	else if (button == GLUT_LEFT_BUTTON && state == GLUT_UP)
	{
		printf("滑鼠左鍵 + 放開\n");
	}
	else if (button == GLUT_MIDDLE_BUTTON && state == GLUT_UP)
	{
		printf("滑鼠中鍵 + 放開\n");
	}
	else if (button == GLUT_RIGHT_BUTTON && state == GLUT_UP)
	{
		printf("滑鼠右鍵 + 放開\n");
	}
	else if (button == 3 && state == GLUT_DOWN)
	{
		printf("滑鼠滾輪向上 + 開始\n");
	}
	else if (button == 3 && state == GLUT_UP)
	{
		printf("滑鼠滾輪向上 + 停止\n");
	}
	else if (button == 4 && state == GLUT_DOWN)
	{
		printf("滑鼠滾輪向下 + 開始\n");
	}
	else if (button == 4 && state == GLUT_UP)
	{
		printf("滑鼠滾輪向下 + 停止\n");
	}
	else
	{
		printf("其他滑鼠動作 %d %d @(%d, %d)\t", button, state, x, y);
	}
}

int main(int argc, char** argv)
{
    const char* windowName = "測試語法";
    const char* message = "測試語法 專用, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMouseFunc(mouse);		//設定callback function
    //glutMotionFunc(motion);		//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}

