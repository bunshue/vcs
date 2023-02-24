#include "../../Common.h"

void draw_something()
{
	//draw_coordinates(0.8f);	//畫座標軸
	//draw_teapot(color_c, 1.0, 0.45);	//畫一個茶壺

	draw_coordinates(2.0);	//畫座標軸
	draw_teapot(color_c, 1.0, 0.5);	//畫一個茶壺

	glFlush();  // 執行繪圖命令

	//顯示資訊
	char info[20];
	sprintf_s(info, sizeof(info), "(%3.1f,   %3.1f)", x_angle, y_angle);
	glutSetWindowTitle(info);
}

// 繪圖回調函數
void display(void)
{
	double x, y, z, eyex, eyey, eyez;
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = (float)rect[2];
	h = (float)rect[3];

	glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣

	if (h < 1)
	{
		h = 1;
	}
	gluPerspective(30.0, w / h, 0.1, 20.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣

	//glTranslated(0.0, 0.0, -dist);
	//glRotatef(x_angle, 1.0f, 0.0f, 0.0f);
	//glRotatef(y_angle, 0.0f, 1.0f, 0.0f);
	x = 0.0;
	y = 0.0;
	z = dist;
	eyex = x;
	eyey = y * cos(-x_angle * PI / 180.0) - z * sin(-x_angle * PI / 180.0);
	eyez = y * sin(-x_angle * PI / 180.0) + z * cos(-x_angle * PI / 180.0);
	x = eyex;
	y = eyey;
	z = eyez;
	eyex = x * cos(-y_angle * PI / 180.0) + z * sin(-y_angle * PI / 180.0);
	eyey = y;
	eyez = -x * sin(-y_angle * PI / 180.0) + z * cos(-y_angle * PI / 180.0);
	gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

	draw_something();
}

int main(int argc, char** argv)
{
	const char* windowName = "手動移動座標系範例";
	const char* message = "手動移動座標系範例\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard_r);

	glutMouseFunc(mouse_r);		//設定callback function
	glutMotionFunc(motion_r);		//設定callback function

	printf("按 0 : 用滑鼠拖曳旋轉\n");
	printf("按 1 : 改變視點遠近\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}
