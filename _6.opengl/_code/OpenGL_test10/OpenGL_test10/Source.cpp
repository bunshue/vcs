//#include "../../../_code/Common.h"    //32 bits
#include "../../Common.h"               //64 bits

int mx;	//position of mouse
int my;	//position of mouse
int m_state = 0; //mouse usage
float x_angle = 0.0f;	//angle of eye
float y_angle = 0.0f;	//angle of eye
float dist = 10.0f; //distance from the eye

void init(void)
{
	glEnable(GL_DEPTH_TEST);
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

	glClearDepth(1.0);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	draw_boundary(color_y, 2.5); //畫視窗邊界

	glLineWidth(2.0f);	//設定線寬

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

	draw_coordinates(2.0);

	glLineWidth(1.0f);	//設定線寬

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	//glTranslatef(-1.0f, 0.0f, 0.0f);	//平移至指定地方(累積)

	//畫一個茶壺
	draw_teapot(color_r, 1.0, 1.0);

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

	glutCreateWindow("畫茶壺與三角塊");	//開啟視窗 並顯示出視窗 Title

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
