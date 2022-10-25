#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void init(void)
{
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glClearColor(0.0, 0.0, 0.0, 0.0);
}

/*
void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z = 0, GLdouble w = 1);
void glRasterPos4dv(const GLdouble* v);
//確定當前光柵位置，x,y,z,w指定了當前光柵位置的坐標

glWindowPos(Type x, Type y, Type z);
//用窗口坐標指定當前光柵位置，不必進行矩陣變換、裁剪、或紋理坐標生成。z值被變換為由glDepthRange()設置的當前近側平面值和遠側平面值

void glBitmap(GLsizei, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat, GLfloat, const GLubyte* bitmap);
//繪製由bitmap指定的位圖，bitmap是一個指向位圖圖像的指針，位圖的原點是當前光柵位置，如果當前光柵位置無效，則這個函數不會繪製任何東西。
//width和height表示位圖的寬度和高度，xorig和yorig定義了位圖的原點，他是根據當期光柵位置確定的，右上為正。
//xmove和ymove表示位圖光柵化之后光柵坐標的x增加值和y增加值
*/

// 繪圖回調函數
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(1.0, 0.0, 0.0);	//設定顏色

	//光柵的位置
	glRasterPos2i(0, 0);//確定當前光柵位置，x,y,z,w指定了當前光柵位置的坐標

	//畫一個64*64
	int i;
	int len = 64 / 8 * 64;
	GLubyte rasters[64 / 8 * 64] = {
	};
	for (i = 0; i < len; i++)
	{
		if (i % 2 == 0)
			rasters[i] = 0xff;
		else
			rasters[i] = 0xff;
	}

	float offsetx = 0.0;
	float offsety = 0.0;
	float dx = 100.0;
	float dy = 100.0;

	//畫完bmp後, 下次位置加上dx dy
	glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);
	glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);
	glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);
	glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);

	for (i = 0; i < len; i++)
	{
		if (i % 2 == 0)
			rasters[i] = 0x55;
		else
			rasters[i] = 0x55;
	}
	glBitmap(64, 64, offsetx, offsety, dx, dy, rasters);


	//繪製由bitmap指定的位圖，bitmap是一個指向位圖圖像的指針，位圖的原點是當前光柵位置，如果當前光柵位置無效，則這個函數不會繪製任何東西。
	//width和height表示位圖的寬度和高度，xorig和yorig定義了位圖的原點，他是根據當期光柵位置確定的，右上為正。
	//xmove和ymove表示位圖光柵化之后光柵坐標的x增加值和y增加值
	glFlush();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣
	glOrtho(0, w, 0, h, -1.0, 1.0);
	glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char k, int /*x*/, int /*y*/)
{
	switch (k)
	{
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;
	}
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	//glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	init();

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	glutMainLoop();	//開始主循環繪製

	return 0;
}

