#include "../../Common.h"

void draw_something()
{
	//draw_coordinates(0.8f);	//畫座標軸
	//draw_teapot(color_c, 1.0, 0.45);	//畫一個茶壺

	draw_coordinates(2.0);	//畫座標軸
	draw_teapot(color_c, 1.0, 0.5);	//畫一個茶壺

	glFlush();  // 執行繪圖命令
}

// 繪圖回調函數
void display(void)
{
	setup_rotation2();
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
