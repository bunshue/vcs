// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// 初始化參數
void init()
{
	glClearColor(0.1, 0.1, 0.4, 0.0);
	glShadeModel(GL_SMOOTH);
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

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
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT);

    // 繪制三角形
    glBegin(GL_TRIANGLES);
    glColor3f(1, 0, 0);     //紅
    glVertex3f(-2, -2, -5); //左下

    glColor3f(0, 1, 0);     //綠
    glVertex3f(2, -2, -5);  //右下

    glColor3f(0, 0, 1);     //藍
    glVertex3f(0, 2, -5);   //上
    glEnd();

    // 執行繪圖命令
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

    glutMainLoop();     // 開始主循環繪制

    return 0;
}


