#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void draw_coordinates(float len);

int mx; //position of mouse;
int my; //position of mouse;
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
	draw_coordinates(1.0);

	glFlush();
	glutSwapBuffers();
}

void draw_coordinates(float len)
{
	glLineWidth(3.0f);	//設定線寬

	glColor3f(1.0f, 0.0f, 0.0f); //畫紅色的x軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(len, 0.0f, 0.0f);	//x軸 len,0,0
	glEnd();

	glColor3f(0.0, 1.0, 0.0); //畫綠色的y軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(0.0f, len, 0.0f);	//y軸 0,len,0
	glEnd();

	glColor3f(0.0, 0.0, 1.0); //畫藍色的z軸
	glBegin(GL_LINES);
	glVertex3f(0.0f, 0.0f, 0.0f);	//原點
	glVertex3f(0.0f, 0.0f, len);	//z軸 0,0,len
	glEnd();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
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

	y_angle += dx * 0.01f;
	x_angle += dy * 0.01f;

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
	
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function
	glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫

	glutMainLoop();	//開始主循環繪製

	return 0;
}

