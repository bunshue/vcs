#include "../../Common.h"

// Vertices of the cube, centered at the origin.
GLfloat vertices[][3] =
{
	{-1.0, -1.0, -1.0},		//0
	{1.0, -1.0, -1.0},		//1
	{1.0, 1.0, -1.0},		//2
	{-1.0, 1.0, -1.0},		//3
	{-1.0, -1.0, 1.0},		//4
	{1.0, -1.0, 1.0},		//5
	{1.0, 1.0, 1.0},		//6
	{-1.0, 1.0, 1.0}		//7
};

// Colors of the vertices.
GLfloat colors[][3] =
{
	{1.0, 1.0, 1.0},		//未用到 白色  XXXX
	{0.0, 0.0, 1.0},		//後 B
	{1.0, 1.0, 1.0},		//未用到 白色  XXXX
	{0.0, 1.0, 1.0},		//左 Cyan天青
	{1.0, 1.0, 0.0},		//下 Y
	{1.0, 0.0, 1.0},		//右 Magenta桃紅
	{0.0, 1.0, 0.0},		//上 G
	{1.0, 0.0, 0.0}			//前 R
};

// Indices of the vertices to make up the six faces of the cube.
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//後
	2, 3, 7, 6,		//上
	0, 4, 7, 3,		//左
	1, 2, 6, 5,		//右
	4, 5, 6, 7,		//前
	0, 1, 5, 4		//下
};

// Angles of rotation about each axis.
GLfloat theta[] = { 0.0f, 0.0f, 0.0f };

GLint axis = 0;	//0: 繞x軸旋轉, 1: 繞y軸旋轉, 2: 繞z軸旋轉

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

// This function sets up the vertex arrays for the color cube and the projection matrix.
void colorcube(void)
{
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, colors);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	//未旋轉前之座標軸
	//draw_coordinates(1.3f);     //畫座標軸

	glRotatef(theta[0], 1.0, 0.0, 0.0);	//對x軸旋轉特定角度
	glRotatef(theta[1], 0.0, 1.0, 0.0);	//對y軸旋轉特定角度
	glRotatef(theta[2], 0.0, 0.0, 1.0);	//對z軸旋轉特定角度
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);

	//已旋轉後之座標軸
	draw_coordinates(1.5f);     //畫座標軸

	//draw_teapot(color_purple, 1.0f, 1.0f);	//畫茶壺

	/*
	//用 GL_LINE_LOOP 畫一個空心矩形
	glColor3f(1.0, 0.0, 0.0);	//紅
	float dd = 1.3f;
	float point1[3] = { -dd, -dd, 1.0 };	//左下
	float point2[3] = { dd, -dd, 1.0 };	//右下
	float point3[3] = { dd,  dd, 1.0 };	//右上
	float point4[3] = { -dd,  dd, 1.0 };	//左上
	glBegin(GL_LINE_LOOP);
	glVertex3fv(point1);	//左下
	glVertex3fv(point2);	//右下
	glVertex3fv(point3);	//右上
	glVertex3fv(point4);	//左上
	glEnd();
	*/

	glColor3f(1.0f, 1.0f, 1.0f);

	int i;
	for (i = 0; i < 8; i++)
	{
		glRasterPos3fv((GLfloat*)vertices[i]);
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0' + i);
	}
	glutSwapBuffers();
}

// This function spins the cube around the current axis by incrementing the angle of rotation by 2 degrees.
void idle(void)
{
	if (flag_rotating == 1)
	{
		if (flag_rotating_direction == 0)	//CW
		{
			theta[axis] += dd;
			if (theta[axis] > 360.0f)
			{
				theta[axis] = 0.0f;
			}
		}
		else   //CCW
		{
			theta[axis] -= dd;
			if (theta[axis] < 0.0f)
			{
				theta[axis] = 360.0f;
			}
		}

		glutPostRedisplay();
		sleep(25);
	}
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
	//printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

	switch (key)
	{
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;
	case 'x':
		flag_rotating_direction = 0;	//CW
		if (flag_rotating == 0)
		{
			printf("繞 x軸 旋轉\n");
			axis = 0;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("停止\n");
		}
		break;
	case 'y':
		flag_rotating_direction = 0;	//CW
		if (flag_rotating == 0)
		{
			printf("繞 y軸 旋轉\n");
			axis = 1;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("停止\n");
		}
		break;
	case 'z':
		flag_rotating_direction = 0;	//CW
		if (flag_rotating == 0)
		{
			printf("繞 z軸 旋轉\n");
			axis = 2;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("停止\n");
		}
		break;
	case 'X':
		flag_rotating_direction = 1;	//CCW
		if (flag_rotating == 0)
		{
			printf("繞 x軸 旋轉 反轉\n");
			axis = 0;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("停止\n");
		}
		break;
	case 'Y':
		flag_rotating_direction = 1;	//CCW
		if (flag_rotating == 0)
		{
			printf("繞 y軸 旋轉 反轉\n");
			axis = 1;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("停止\n");
		}
		break;
	case 'Z':
		flag_rotating_direction = 1;	//CCW
		if (flag_rotating == 0)
		{
			printf("繞 z軸 旋轉 反轉\n");
			axis = 2;
			flag_rotating = 1;
		}
		else
		{
			flag_rotating = 0;
			printf("停止\n");
		}
		break;
	case '+':
		dd += ddd;
		if (dd > 20.0f)
		{
			dd = 10.0f;
		}
		break;
	case '-':
		if (dd > 0.1)
		{
			dd -= ddd;
		}
		break;
	case ' ':
	case 's':
		flag_rotating = 1 - flag_rotating;
		break;
	case 'r':
		printf("重置\n");
		flag_rotating = 0;

		break;
	}
}

int main(int argc, char** argv)
{
	const char* windowName = "Rotating Color Cube";
	const char* message = "按x, y, z 選擇旋轉軸, 按 空白鍵 啟停, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);

	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}


//加畫茶壺做比對

