// OpenGL Graphics includes
#include <helper_gl.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//#include <GL/freeglut.h>	//64位元用的
#include <GL/glut.h>		//32位元用的

//幾何圖形繪制

//#include <GLUT/GLUT.h>
//#include <OpenGL/OpenGL.h>

// 初始化參數
void init()
{
	glClearColor(0.1, 0.1, 0.4, 0.0);
	glShadeModel(GL_SMOOTH);
}

void DrawMyObjects(void)
{
    /* draw some points */
    glBegin(GL_POINTS);
		glColor3f(1.0, 0.0, 0.0);	//紅
		glVertex2f(-14.0, 12.0);

		glColor3f(0.0, 1.0, 0.0);	//綠
		glVertex2f(-12.0, 12.0);

		glColor3f(1.0, 1.0, 0);	//黃
		glVertex2f(-10.0, 12.0);
    glEnd();

    /* draw some line_segments */
    glBegin(GL_LINES);
		glColor3f(1.0, 1.0, 0.0);
		glVertex2f(-14.0, 10.0);
		glVertex2f(-6.0, 10.0);

		glColor3f(1.0, 0.0, 1.0);
		glVertex2f(-14.0, 8.0);
		glVertex2f(-6.0, 8.0);

		glColor3f(1.0, 0.0, 1.0);

		glVertex2f(-14.5, 2);
		glVertex2f(14.5, 2);

		glVertex2f(0, 14.5);
		glVertex2f(0, -14.5);
    glEnd();

    /* draw one opened_line */
    glBegin(GL_LINE_STRIP);
    glColor3f(0.0, 1.0, 0.0);
    glVertex2f(-3.0, 9.0);
    glVertex2f(2.0, 6.0);
    glVertex2f(3.0, 8.0);
    glVertex2f(-2.5, 6.5);
    glEnd();


    /* draw one closed_line */
    glBegin(GL_LINE_LOOP);
    glColor3f(0.0, 1.0, 1.0);
    glVertex2f(7.0, 7.0);
    glVertex2f(8.0, 8.0);
    glVertex2f(9.0, 6.5);
    glVertex2f(10.3, 7.5);
    glVertex2f(11.5, 6.0);
    glVertex2f(7.5, 6.0);
    glEnd();


    /* draw one filled_polygon */
    glBegin(GL_POLYGON);
    glColor3f(0.5, 0.3, 0.7);
    glVertex2f(-7.0, 2.0);
    glVertex2f(-8.0, 3.0);
    glVertex2f(-10.3, 0.5);
    glVertex2f(-7.5, -2.0);
    glVertex2f(-6.0, -1.0);
    glEnd();


    /* draw some filled_quandrangles */
    glBegin(GL_QUADS);
    glColor3f(0.7, 0.5, 0.2);
    glVertex2f(0.0, 2.0);
    glVertex2f(-1.0, 3.0);
    glVertex2f(-3.3, 0.5);
    glVertex2f(-0.5, -1.0);
    glColor3f(0.5, 0.7, 0.2);
    glVertex2f(3.0, 2.0);
    glVertex2f(2.0, 3.0);
    glVertex2f(0.0, 0.5);
    glVertex2f(2.5, -1.0);
    glEnd();

    /* draw some filled_strip_quandrangles */
    glBegin(GL_QUAD_STRIP);
    glVertex2f(6.0, -2.0);
    glVertex2f(5.5, 1.0);
    glVertex2f(8.0, -1.0);
    glColor3f(0.8, 0.0, 0.0);
    glVertex2f(9.0, 2.0);
    glVertex2f(11.0, -2.0);
    glColor3f(0.0, 0.0, 0.8);
    glVertex2f(11.0, 2.0);
    glVertex2f(13.0, -1.0);
    glColor3f(0.0, 0.8, 0.0);
    glVertex2f(14.0, 1.0);
    glEnd();


    /* draw some filled_triangles */

    glBegin(GL_TRIANGLES);
    glColor3f(0.2, 0.5, 0.7);
    glVertex2f(-10.0, -5.0);
    glVertex2f(-12.3, -7.5);
    glVertex2f(-8.5, -6.0);
    glColor3f(0.2, 0.7, 0.5);
    glVertex2f(-8.0, -7.0);
    glVertex2f(-7.0, -4.5);
    glVertex2f(-5.5, -9.0);
    glEnd();

    /* draw some filled_strip_triangles */
    glBegin(GL_TRIANGLE_STRIP);
    glVertex2f(-1.0, -8.0);
    glVertex2f(-2.5, -5.0);
    glColor3f(0.8, 0.8, 0.0);
    glVertex2f(1.0, -7.0);
    glColor3f(0.0, 0.8, 0.8);
    glVertex2f(2.0, -4.0);
    glColor3f(0.8, 0.0, 0.8);
    glVertex2f(4.0, -6.0);
    glEnd();


    /* draw some filled_fan_triangles */
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(8.0, -6.0);
    glVertex2f(10.0, -3.0);
    glColor3f(0.8, 0.2, 0.5);
    glVertex2f(12.5, -4.5);
    glColor3f(0.2, 0.5, 0.8);
    glVertex2f(13.0, -7.5);
    glColor3f(0.8, 0.5, 0.2);
    glVertex2f(10.5, -9.0);
    glEnd();

	/*
	GLfloat red, green, blue;
GLfloat x, y;
glBegin(GL_POINTS);
for (int i = 0; i < 10; i++) {
glColor3f(red, green, blue);
glVertex2f(x, y);
//... // change coord. values
}
glEnd();
*/

}

// 繪圖回調函數
void display()
{
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT);
    DrawMyObjects();
    // 執行繪圖命令
    glFlush();
}


// 窗口大小變化回調函數
void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0, 0, 25, 0, 0, -1, 0, 1, 0);
}

int main(int argc, const char* argv[])
{
    // 初始化顯示模式
    glutInit(&argc, const_cast<char**>(argv));
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    // 初始化窗口
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(100, 100);
    glutCreateWindow(argv[0]);

    init();

    glutReshapeFunc(reshape);
    glutDisplayFunc(display);

    // 開始主循環繪制
    glutMainLoop();
    return 0;
}
