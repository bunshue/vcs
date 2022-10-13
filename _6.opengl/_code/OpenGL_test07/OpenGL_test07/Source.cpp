// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// 窗口大小變化回調函數
void reshape(int w, int h)
{
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
    glClearColor(0.5f, 0.5f, 0.5f, 0.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    //设置颜色
    glColor3f(0.2f, 0.6f, 0.5f);

    //开始渲染
    glBegin(GL_POLYGON);

    //圆的顶点数：数越大越趋近于圆
    const int n = 55;
    const GLfloat R = 0.5f;
    const GLfloat pi = 3.1415926f;

    for (int i = 0; i < n; i++)
    {
        glVertex2f(R * cos(2 * pi / n * i), R * sin(2 * pi / n * i));
    }

    //结束渲染
    glEnd();

    //强制刷新缓存区
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

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function

    glutMainLoop();     // 開始主循環繪制

    return 0;
}


