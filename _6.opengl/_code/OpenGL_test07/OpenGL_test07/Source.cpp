#include "../../Common.h"

//eyex, eyey, eyez, centerx, centery, centerz
double eyex = 0.0;
double eyey = 0.0;
double eyez = 5.0;
double upx = 0;
double upy = 1.0;	//y軸向上
double upz = 0;

// 繪圖回調函數
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0); //畫筆白色

	glLoadIdentity();  //加載單位矩陣

	gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);

	draw_coordinates(2.0);

	draw_teapot(color_purple, 1.0, 1.6);	//畫一個茶壺

	glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 1.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
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
	case 'x':
		printf("x\n");
		eyex = 5.0;
		eyey = 0.0;
		eyez = 0.0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case 'X':
		printf("X\n");
		eyex = -5.0;
		eyey = 0.0;
		eyez = 0.0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case 'y':
		printf("y\n");
		eyex = 0.0;
		eyey = 5.0;
		eyez = 0.0;
		upx = 1.0;	//x軸向上
		upy = 0;
		upz = 0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case 'Y':
		printf("Y\n");
		eyex = 0.0;
		eyey = -5.0;
		eyez = 0.0;
		upx = 1.0;	//x軸向上
		upy = 0;
		upz = 0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case 'z':
		printf("z\n");
		eyex = 0.0;
		eyey = 0.0;
		eyez = 5.0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case 'Z':
		printf("Z\n");
		eyex = 0.0;
		eyey = 0.0;
		eyez = -5.0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case '1':
		printf("1\n");
		upx = 0;
		upy = 1.0;
		upz = 0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;
	case '2':
		printf("2\n");
		upx = 0;
		upy = -1.0;
		upz = 0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;

	case '3':
		upx = 1.0;
		upy = 0;
		upz = 0;
		gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);
		glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
		break;

	case '4':
		break;

	case '?':
		break;
	}
}

int main(int argc, char** argv)
{
	const char* windowName = "簡單2D OpenGL畫圖 0 ~ 9";
	const char* message = "簡單2D OpenGL畫圖 0 ~ 9\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

	glutMainLoop();	//開始主循環繪製

	return 0;
}
