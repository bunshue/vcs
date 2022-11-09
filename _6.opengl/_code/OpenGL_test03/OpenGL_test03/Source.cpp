//#include "../../../_code/Common.h"    //32 bits
#include "../../Common.h"   //64 bits

int mx; //position of mouse
int my; //position of mouse
float x_angle;	 //angle of eye
float y_angle;	 //angle of eye

// 繪圖回調函數
void display(void)
{
	//printf("d ");
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = (float)rect[2];
	h = (float)rect[3];

	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
	glClear(GL_COLOR_BUFFER_BIT);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣

	if (w > h)
	{
		glOrtho(-w / h, w / h, -1.0f, 1.0f, -1.0f, 1.0f);
	}
	else
	{
		glOrtho(-1.0f, 1.0f, -h / w, h / w, -1.0f, 1.0f);
	}

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣

	glRotatef(x_angle, 1.0f, 0.0f, 0.0f);
	glRotatef(y_angle, 0.0f, 1.0f, 0.0f);

	draw_boundary(color_y, 0.9); //畫視窗邊界

	draw_coordinates(0.9f);	//畫座標軸

	//畫一個茶壺
	draw_teapot(color_c, 1, 0.2);

	glFlush();  // 執行繪圖命令

	//顯示資訊
	char info[20];
	sprintf_s(info, 20, "(%3.1f,   %3.1f)", x_angle, y_angle);

	glutSetWindowTitle(info);
}

void mouse(int button, int state, int x, int y)
{
	//MouseDown
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		mx = x;
		my = y;
		printf("D(%d, %d) ", mx, my);
	}
}

void motion(int x, int y)
{
	//MouseMove
	int dx, dy; //offset of mouse;

	dx = x - mx;
	dy = y - my;

	y_angle += dx * 0.1f;
	x_angle += dy * 0.1f;

	mx = x;
	my = y;

	//printf("M(%d, %d) ", mx, my);
	glutPostRedisplay();
}

void idle()
{
	//printf("i");

	x_angle += 0.1f;
	y_angle += 0.1f;

	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape0);	//設定callback function
	glutKeyboardFunc(keyboard0);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function
	//glutIdleFunc(idle);		//設定callback function, 利用idle事件進行重畫

	glutMainLoop();	//開始主循環繪製

	return 0;
}

