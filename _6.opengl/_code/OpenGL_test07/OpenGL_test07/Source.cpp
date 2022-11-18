#include "../../Common.h"

//eyex, eyey, eyez, centerx, centery, centerz
double eyex = 0.0;
double eyey = 0.0;
double eyez = 5.0;
double upx = 0;
double upy = 1.0;
double upz = 0;

void init(void)
{
	glClearColor(0.0, 0.0, 0.0, 0.0); //背景黑色
}

// 繪圖回調函數
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0); //畫筆白色

	glLoadIdentity();  //加載單位矩陣

	gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upx, upy, upz);

	draw_coordinates(2.0);

	//畫一個茶壺
	draw_teapot(color_r, 1.0, 1.6);

	glutSwapBuffers();
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
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	init();

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse0);		//設定callback function
	glutMotionFunc(motion0);	//設定callback function

	glutMainLoop();	//開始主循環繪製

	return 0;
}
