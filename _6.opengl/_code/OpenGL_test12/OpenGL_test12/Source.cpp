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

	glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
	glutInitWindowPosition(1100, 200);	//視窗起始位置

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function

    glutMainLoop();

    return 0;
}


