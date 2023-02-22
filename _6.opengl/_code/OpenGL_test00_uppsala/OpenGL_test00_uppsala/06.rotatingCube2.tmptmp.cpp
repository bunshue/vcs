#include "../../Common.h"

// Vertices of the cube, centered at the origin.
//每3點為一組
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
//每3點為一組
GLfloat vertex_color[][3] =
{
	{1.0, 1.0, 1.0},		//0, 未用到 白色  XXXX
	{0.0, 0.0, 1.0},		//1, -z 後 藍
	{1.0, 1.0, 1.0},		//2, 未用到 白色  XXXX
	{0.0, 1.0, 1.0},		//3, -x 左 Cyan 天青
	{1.0, 1.0, 0.0},		//4, -y 下 黃
	{1.0, 0.0, 1.0},		//5, +x 右 Magenta桃紅
	{0.0, 1.0, 0.0},		//6, +y 上 綠
	{1.0, 0.0, 0.0}			//7, +z 前 紅
};

// Indices of the vertices to make up the six faces of the cube. 需要照順序 法線朝外才可以
GLubyte cubeIndices[24] =
{
	0, 3, 2, 1,		//後, -z軸 藍
	2, 3, 7, 6,		//上, +y軸 綠
	0, 4, 7, 3,		//左, -x軸 天青
	1, 2, 6, 5,		//右, +x軸 桃紅
	4, 5, 6, 7,		//前, +z軸 紅
	0, 1, 5, 4		//下, -y軸 黃
};
//以第4點為對應顏色

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//對各軸的旋轉角度
GLint axis = 0;	//0: 繞x軸旋轉, 1: 繞y軸旋轉, 2: 繞z軸旋轉

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

void display(void)
{
	//設定cubic之頂點與顏色
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);		//從 vertices 陣列找起, 每3點為一組, 共8個頂點
	glEnableClientState(GL_COLOR_ARRAY);
	glColorPointer(3, GL_FLOAT, 0, vertex_color);	//從 vertex_color 陣列找起, 每3點為一組, 共8種顏色, 用到其中6種

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0);

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glRotatef(theta[0], 1.0, 0.0, 0.0);	//對x軸旋轉特定角度
	glRotatef(theta[1], 0.0, 1.0, 0.0);	//對y軸旋轉特定角度
	glRotatef(theta[2], 0.0, 0.0, 1.0);	//對z軸旋轉特定角度
	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);	//從 cubeIndices 陣列 裡面找出 24 個索引數
	//用GL_QUADS就是每4個組成一個四邊形 => 共6個面

	//已旋轉後之座標軸
	draw_coordinates(1.5f);     //畫座標軸

	draw_teapot(color_purple, 1.0f, 1.0f);	//畫茶壺

	draw_cube(color_silver, 1.0f, 2.5f);	//cubic 外框
	draw_cube(color_purple, 1.0f, 3.0f);	//cubic 外框

	for (int i = 0; i < 8; i++)
	{
		glColor3f(1.0f, 1.0f, 1.0f);
		glRasterPos3fv((GLfloat*)vertices[i]);
		glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, '0' + i);
	}
	glutSwapBuffers();
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
	case ' ':
	case 's':
		flag_rotating = 1 - flag_rotating;
		break;

	case 'r':
		printf("重置\n");
		/*
		flag_rotating = 0;
		theta[0] = 0.0f;
		theta[1] = 0.0f;
		theta[2] = 0.0f;
		glutPostRedisplay();
		*/
		break;

	}
	glutPostRedisplay();
}

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

int main(int argc, char** argv)
{
	const char* windowName = "Rotating Color Cube";
	const char* message = "按x, y, z 選擇旋轉軸, 按 空白鍵 啟停, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

	//先保留
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glEnable(GL_DEPTH_TEST);

	glutMainLoop();	//開始主循環繪製

	return 0;
}
