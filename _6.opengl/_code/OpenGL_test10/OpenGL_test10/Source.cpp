#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
	double x, y, z, eyex, eyey, eyez;
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

	//顯示資訊
	char info[20];
	sprintf_s(info, sizeof(info), "(%3.1f,   %3.1f)", x_angle, y_angle);
	glutSetWindowTitle(info);
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

	//printf("M(%d, %d) ", mx, my);
	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	x_angle = 0.0f;	//angle of eye
	y_angle = 0.0f;	//angle of eye
	m_state = 0; //mouse usage
	dist = 10.0f; //distance from the eye

	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("手動移動座標系範例");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape0);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	printf("按 0 : keydown means control the angle of the eye\n");
	printf("按 1 : keydown means control the distance of the eye\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}

