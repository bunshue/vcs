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
GLfloat vertex_color[][3] =
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

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//對各軸的旋轉角度
GLint axis = 0;	//0: 繞x軸旋轉, 1: 繞y軸旋轉, 2: 繞z軸旋轉

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

//啟始時的視點
double eyex = 0.0f;
double eyey = 0.0f;
double eyez = 5.0f;
//double eye_distance = 5.0f;

// This function sets up the vertex arrays for the color cube.
void colorcube(void)
{
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_VERTEX_ARRAY);
	glVertexPointer(3, GL_FLOAT, 0, vertices);
	glColorPointer(3, GL_FLOAT, 0, vertex_color);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	/* Update viewer position in modelview matrix */

	glLoadIdentity();

	gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

	/* Rotate cube */

	glRotatef(theta[0], 1.0, 0.0, 0.0);
	glRotatef(theta[1], 0.0, 1.0, 0.0);
	glRotatef(theta[2], 0.0, 0.0, 1.0);

	/* Draw the cube and switch buffers */

	glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, cubeIndices);
	glutSwapBuffers();
}

/* This function is the idle callback. It spins the cube 2 degrees about the selected axis. */
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
		printf("In ");
		if (axis == 0)
		{
			eyex -= 0.5f;
			if (eyex < 0.5f)
				eyex = 0.5f;
		}
		else if (axis == 1)
		{
			eyey -= 0.5f;
			if (eyey < 0.5f)
				eyey = 0.5f;
		}
		else if (axis == 2)
		{
			eyez -= 0.5f;
			if (eyez < 0.5f)
				eyez = 0.5f;
		}
		break;
	case '-':
		printf("Out ");
		if (axis == 0)
		{
			eyex += 0.5f;
			if (eyex > 15.0f)
				eyex = 15.0f;
		}
		else if (axis == 1)
		{
			eyey += 0.5f;
			if (eyey > 15.0f)
				eyey = 15.0f;
		}
		else if (axis == 2)
		{
			eyez += 0.5f;
			if (eyez > 15.0f)
				eyez = 15.0f;
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

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45.0, (double)w / (double)h, 2.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv)
{
	const char* windowName = "Color Cube";
	const char* message = "滑鼠控制, 按S啟停, 按 Esc 離開\n";
	//const char* message = "按x, y, z 選擇旋轉軸, 按 空白鍵 啟停, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

	//先保留
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glEnable(GL_DEPTH_TEST);
	glShadeModel(GL_FLAT);
	colorcube();

	glutMainLoop();	//開始主循環繪製

	return 0;
}
