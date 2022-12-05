#include "../../Common.h"

void draw_something()
{
	draw_boundary(color_y, 0.9f); //畫視窗邊界

	draw_coordinates(0.9f);	//畫座標軸

	//立體畫點
	//畫點
	float size = 2.0;  //設定點的大小, N X N
	float x_st = 0.0f;
	float y_st = 0.0f;
	float z_st = 0.0f;
	float r = 0.7f;

	//畫點
	glColor3fv(color_r);    //設定顏色
	glPointSize(size);		//設定點的大小, N X N
	glBegin(GL_POINTS);
	{
		for (y_st = -r; y_st <= r; y_st += 0.03f)
		{
			for (x_st = -r; x_st <= r; x_st += 0.03f)
			{
				z_st = sqrt(r * r - x_st * x_st - y_st * y_st);
				glVertex3f(x_st, y_st, z_st);
				//glVertex3f(x_st, y_st, -z_st);
			}
		}
	}
	glEnd();

	// 繪製三角形	3D
	glBegin(GL_TRIANGLES);
	float dd = 0.5f;
	glColor3f(1, 0, 0);     //紅
	glVertex3f(-dd, -dd, 0.3f); //左下

	glColor3f(0, 1, 0);     //綠
	glVertex3f(dd, -dd, 0.0f);  //右下

	glColor3f(0, 0, 1);     //藍
	glVertex3f(0, dd, -0.3f);   //上
	glEnd();

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
	common_setup(argc, argv, windowName, message, display, reshape0, keyboard_r);

	glutMouseFunc(mouse_r);		//設定callback function
	glutMotionFunc(motion_r);		//設定callback function

	printf("按 0 : keydown means control the angle of the eye\n");
	printf("按 1 : keydown means control the distance of the eye\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}

