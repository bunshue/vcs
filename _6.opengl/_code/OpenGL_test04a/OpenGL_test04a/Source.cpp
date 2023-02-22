#include "../../Common.h"

void draw_something()
{
	draw_boundary(color_y, 0.9f); //畫視窗邊界

	draw_coordinates(0.9f);	//畫座標軸

	draw_teapot(color_c, 1.0, 0.5);	//畫一個茶壺

	glLineWidth(5);     //設定線寬
	glColor3f(1.0, 1.0, 1.0);   //設定顏色
	glutWireOctahedron();

	glFlush();  // 執行繪圖命令
}

// 繪圖回調函數
void display(void)
{
	setup_rotation();
	draw_something();
}

int main(int argc, char** argv)
{
	const char* windowName = "手動移動座標系範例";
	const char* message = "手動移動座標系範例\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard_r);

	glutMouseFunc(mouse_r);		//設定callback function
	glutMotionFunc(motion_r);		//設定callback function

	printf("按 0 : keydown means control the angle of the eye\n");
	printf("按 1 : keydown means control the distance of the eye\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}
