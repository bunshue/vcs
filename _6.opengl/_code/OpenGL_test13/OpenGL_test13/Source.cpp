#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

static int slices = 16;
static int stacks = 16;

const GLfloat light_ambient[] = { 0.0f, 0.0f, 0.0f, 1.0f };
const GLfloat light_diffuse[] = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_specular[] = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat light_position[] = { 2.0f, 5.0f, 5.0f, 0.0f };

const GLfloat mat_ambient[] = { 0.7f, 0.7f, 0.7f, 1.0f };
const GLfloat mat_diffuse[] = { 0.8f, 0.8f, 0.8f, 1.0f };
const GLfloat mat_specular[] = { 1.0f, 1.0f, 1.0f, 1.0f };
const GLfloat high_shininess[] = { 100.0f };

// 繪圖回調函數
void display(void)
{
	const double t = glutGet(GLUT_ELAPSED_TIME) / 1000.0;
	const double a = t * 90.0;

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glColor3d(1, 0, 0);

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslated(-2.4, 1.2, -6);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);
	glutSolidSphere(1, slices, stacks);
	glPopMatrix();

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslated(0, 1.2, -6);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);
	glutSolidCone(1, 1, slices, stacks);
	glPopMatrix();

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslated(2.4, 1.2, -6);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);
	glutSolidTorus(0.2, 0.8, slices, stacks);
	glPopMatrix();

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslated(-2.4, -1.2, -6);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);
	glutWireSphere(1, slices, stacks);
	glPopMatrix();

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslated(0, -1.2, -6);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);
	glutWireCone(1, 1, slices, stacks);
	glPopMatrix();

	glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
	glTranslated(2.4, -1.2, -6);
	glRotated(60, 1, 0, 0);
	glRotated(a, 0, 0, 1);
	glutWireTorus(0.2, 0.8, slices, stacks);
	glPopMatrix();

	glutSwapBuffers();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	const float ar = (float)w / (float)h;

	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();	//設置單位矩陣
	glFrustum(-ar, ar, -1.0, 1.0, 2.0, 100.0);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();	//設置單位矩陣
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

	case '+':
		slices++;
		stacks++;
		break;

	case '-':
		if (slices > 3 && stacks > 3)
		{
			slices--;
			stacks--;
		}
		break;
	}

	glutPostRedisplay();
}

static void idle(void)
{
	glutPostRedisplay();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	
	//glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

	glutInitWindowSize(640, 480);		// 設定視窗大小
	glutInitWindowPosition(1100, 200);	// 設定視窗位置

	glutCreateWindow("球體旋轉");	//開啟視窗 並顯示出視窗 Title

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutIdleFunc(idle);			//設定callback function

	glClearColor(1, 1, 1, 1);
	glEnable(GL_CULL_FACE);
	glCullFace(GL_BACK);

	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LESS);

	glEnable(GL_LIGHT0);
	glEnable(GL_NORMALIZE);
	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_LIGHTING);

	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
	glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
	glLightfv(GL_LIGHT0, GL_POSITION, light_position);

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess);

	glutMainLoop();	//開始主循環繪製

	return 0;
}


