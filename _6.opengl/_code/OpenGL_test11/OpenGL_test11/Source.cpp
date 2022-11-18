#include "../../Common.h"

int mx; //position of mouse
int my; //position of mouse
int m_state = 0; //mouse usage
float x_angle = 0.0f;	//angle of eye
float y_angle = 0.0f;	//angle of eye
float dist = 10.0f; //distance from the eye

void init(void)
{
	glEnable(GL_DEPTH_TEST);	//有無打開, 差很大
}

// 繪圖回調函數
void display(void)
{
	float lit_position[] = { 0.0f, 0.0f, 1.0f, 0.0f };
	float mat_yellow[] = { 1.0f, 1.0f, 0.0f, 1.0f };
	float mat_cyan[] = { 0.0f, 1.0f, 1.0f, 1.0f };
	int rect[4];
	float w, h;

	glGetIntegerv(GL_VIEWPORT, rect);
	w = (float)rect[2];
	h = (float)rect[3];

	glClearDepth(1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

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

	glLightfv(GL_LIGHT0, GL_POSITION, lit_position);
	glTranslated(0.0, 0.0, -dist); //對應變換陣T1
	glRotatef(x_angle, 1.0f, 0.0f, 0.0f); //對應變換陣T2
	glRotatef(y_angle, 0.0f, 1.0f, 0.0f);  //對應變換陣T3
	glDisable(GL_LIGHTING);
	//glLightfv(GL_LIGHT0, GL_POSITION, lit_position);
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

	GLdouble base = 0.5;
	GLdouble height = 1.0;
	GLint slices = 100;
	GLint stacks = 10;
	float width = 3;

	draw_cone(color_y, width, base, height, slices, stacks); //畫圓錐體
	//顏色沒有套用到

	glPopMatrix();

	glFlush();  // 執行繪圖命令
	glutSwapBuffers();
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
	case '0':
		m_state = 0;
		break;
	case '1':
		m_state = 1;
		break;
	}
}

void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		mx = x;
		my = y;
	}
}

void motion(int x, int y)
{
	int dx, dy; //offset of mouse;

	dx = x - mx;
	dy = y - my;

	if (m_state == 0)
	{
		y_angle += dx * 0.1f;
		x_angle += dy * 0.1f;
	}
	else if (m_state == 1)
	{
		dist += (dx + dy) * 0.01f;
	}

	mx = x;
	my = y;

	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	
	//glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("畫茶壺圓椎三角塊");	//開啟視窗 並顯示出視窗 Title

	init();

	printf("0 keydown means control the angle of the eye\n");
	printf("1 keydown means control the distance of the eye\n");

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape0);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	glutMainLoop();	//開始主循環繪製

	return 0;
}