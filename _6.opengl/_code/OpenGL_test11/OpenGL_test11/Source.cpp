#include "../../Common.h"

void draw_something()
{
	float mat_yellow[] = { 1.0f, 1.0f, 0.0f, 1.0f };
	float mat_cyan[] = { 0.0f, 1.0f, 1.0f, 1.0f };

	draw_coordinates(1.0);	//顯示座標軸，設X軸的兩端點為v1、v2，考慮這兩點經受的變換

	draw_teapot(color_r, 1.0, 0.5);	//畫一個茶壺

	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);

	glPushMatrix(); //下壓堆棧并復制棧頂	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslatef(1.0f, 0.0f, 0.0f); //對應變換陣T4
	glScalef(0.5f, 0.5f, 0.5f); //對應變換陣T5
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_yellow);
	draw_tetrahedron2(); //顯示直角四面體，設某個三角形的頂點為v1'、v2'、v3'，考慮這三點經受的變換
	glPopMatrix(); //上彈堆棧，棧頂被放棄

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 1);
	glTranslatef(-1.0f, 0.0f, 0.0f); //對應變換陣T6
	glRotatef(-90.0f, 1.0f, 0.0f, 0.0f); //對應變換陣T7
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_cyan);
	glMaterialfv(GL_BACK, GL_DIFFUSE, mat_yellow);

	glutSolidCone(0.4, 1.0, 100, 10); //畫圓錐體

	glPopMatrix();

	glFlush();  // 執行繪圖命令
}

// 繪圖回調函數
void display(void)
{
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = (float)rect[2];
	h = (float)rect[3];

	glClear(GL_COLOR_BUFFER_BIT);

	draw_boundary(color_y, 2.5f); //畫視窗邊界

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣

	if (h < 1)
	{
		h = 1;
	}
	gluPerspective(30.0, w / h, 0.1, 20.0); //對應變換陣T0

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣

	float lit_position[] = { 0.0f, 0.0f, 1.0f, 0.0f };

	glLightfv(GL_LIGHT0, GL_POSITION, lit_position);
	glTranslated(0.0, 0.0, -dist); //對應變換陣T1
	glRotatef(x_angle, 1.0f, 0.0f, 0.0f); //對應變換陣T2
	glRotatef(y_angle, 0.0f, 1.0f, 0.0f);  //對應變換陣T3
	glDisable(GL_LIGHTING);
	//glLightfv(GL_LIGHT0, GL_POSITION, lit_position);

	draw_something();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("畫茶壺圓椎三角塊");	//開啟視窗 並顯示出視窗 Title

	printf("0 keydown means control the angle of the eye\n");
	printf("1 keydown means control the distance of the eye\n");

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape0);	//設定callback function
	glutKeyboardFunc(keyboard_r);	//設定callback function
	glutMouseFunc(mouse_r);		//設定callback function
	glutMotionFunc(motion_r);		//設定callback function

	glutMainLoop();	//開始主循環繪製

	return 0;
}