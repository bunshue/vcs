// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

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

void key(unsigned char key, int /*x*/, int /*y*/)
{
	switch (key) {
	case ' ':
		//bPause = !bPause;
		break;

	case 13:
		break;

	case '\033':
	case 'q':
		printf("你按了 離開\n");
		glutDestroyWindow(glutGetWindow());
		return;
	case '1':
		printf("你按了 選單項目1\n");
		break;

	case '2':
		printf("你按了 選單項目2\n");
		break;

	case '3':
		printf("你按了 選單項目3\n");
		break;

	case '4':
		printf("你按了 選單項目4\n");
		break;

	case 'u':
		break;

	case 'r':
		break;

	}
	glutPostRedisplay();
}

void mainMenu(int i) { key((unsigned char)i, 0, 0); }

void initMenus()
{
	glutCreateMenu(mainMenu);
	glutAddMenuEntry("Menu Item 1", '1');
	glutAddMenuEntry("Menu Item 2", '2');
	glutAddMenuEntry("Menu Item 3", '3');
	glutAddMenuEntry("Menu Item 4", '4');
	glutAddMenuEntry("Exit (esc)", '\033');
	glutAttachMenu(GLUT_RIGHT_BUTTON);
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
	glutInitWindowPosition(1100, 200);	//視窗起始位置

	glutCreateWindow("開啟視窗");		//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	initMenus();

	glutMainLoop();

	return 0;
}


