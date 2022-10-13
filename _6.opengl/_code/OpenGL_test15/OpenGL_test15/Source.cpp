// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

GLubyte rasters[24] = {
   0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00,
   0xff, 0x00, 0xff, 0x00, 0xc0, 0x00, 0xc0, 0x00, 0xc0, 0x00,
   0xff, 0xc0, 0xff, 0xc0 };

void init(void)
{
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	glClearColor(0.0, 0.0, 0.0, 0.0);
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(0, w, 0, h, -1.0, 1.0);
	glMatrixMode(GL_MODELVIEW);

}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

// 繪圖回調函數
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 1.0, 1.0);
	glRasterPos2i(20, 20);//确定当前光栅位置，x,y,z,w指定了当前光栅位置的坐标
	glBitmap(10, 12, 0.0, 0.0, 11.0, 0.0, rasters);
	glBitmap(10, 12, 0.0, 0.0, 11.0, 0.0, rasters);
	glBitmap(10, 12, 0.0, 0.0, 11.0, 0.0, rasters);
	//绘制由bitmap指定的位图，bitmap是一个指向位图图像的指针，位图的原点是当前光栅位置，如果当前光栅位置无效，则这个函数不会绘制任何东西。
	//width和height表示位图的宽度和高度，xorig和yorig定义了位图的原点，他是根据当期光栅位置确定的，右上为正。
	//xmove和ymove表示位图光栅化之后光栅坐标的x增加值和y增加值
	glFlush();
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

	case '1':
		printf("1\n");
		break;

	case '2':
		printf("2\n");
		break;

	case '3':
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

    glutMainLoop();
	
    return 0;
}
