#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#ifndef WIN32
#define CALLBACK
#endif

#define INREAL float

#define S_NUMPOINTS 13
#define S_ORDER     3   
#define S_NUMKNOTS  (S_NUMPOINTS + S_ORDER)
#define T_NUMPOINTS 3
#define T_ORDER     3 
#define T_NUMKNOTS  (T_NUMPOINTS + T_ORDER)
#define SQRT_TWO    1.41421356237309504880

typedef INREAL Point[4];

GLenum expectedError;
GLint rotX = 40;
GLint rotY = 40;

INREAL sknots[S_NUMKNOTS] = {
	-1.0, -1.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0,
	4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 9.0, 9.0
};

INREAL glutnots[T_NUMKNOTS] = {
	1.0, 1.0, 1.0, 2.0, 2.0, 2.0
};

Point ctlpoints[S_NUMPOINTS][T_NUMPOINTS] = {
	{
	{
		4.0, 2.0, 2.0, 1.0
	},
	{
		4.0, 1.6, 2.5, 1.0
	},
	{
		4.0, 2.0, 3.0, 1.0
	}
	},
	{
	{
		5.0, 4.0, 2.0, 1.0
	},
	{
		5.0, 4.0, 2.5, 1.0
	},
	{
		5.0, 4.0, 3.0, 1.0
	}
	},
	{
	{
		6.0, 5.0, 2.0, 1.0
	},
	{
		6.0, 5.0, 2.5, 1.0
	},
	{
		6.0, 5.0, 3.0, 1.0
	}
	},
	{
	{
		SQRT_TWO * 6.0, SQRT_TWO * 6.0, SQRT_TWO * 2.0, SQRT_TWO
	},
	{
		SQRT_TWO * 6.0, SQRT_TWO * 6.0, SQRT_TWO * 2.5, SQRT_TWO
	},
	{
		SQRT_TWO * 6.0, SQRT_TWO * 6.0, SQRT_TWO * 3.0, SQRT_TWO
	}
	},
	{
	{
		5.2, 6.7, 2.0, 1.0
	},
	{
		5.2, 6.7, 2.5, 1.0
	},
	{
		5.2, 6.7, 3.0, 1.0
	}
	},
	{
	{
		SQRT_TWO * 4.0, SQRT_TWO * 6.0, SQRT_TWO * 2.0, SQRT_TWO
	},
	{
		SQRT_TWO * 4.0, SQRT_TWO * 6.0, SQRT_TWO * 2.5, SQRT_TWO
	},
	{
		SQRT_TWO * 4.0, SQRT_TWO * 6.0, SQRT_TWO * 3.0, SQRT_TWO
	}
	},
	{
	{
		4.0, 5.2, 2.0, 1.0
	},
	{
		4.0, 4.6, 2.5, 1.0
	},
	{
		4.0, 5.2, 3.0, 1.0
	}
	},
	{
	{
		SQRT_TWO * 4.0, SQRT_TWO * 6.0, SQRT_TWO * 2.0, SQRT_TWO
	},
	{
		SQRT_TWO * 4.0, SQRT_TWO * 6.0, SQRT_TWO * 2.5, SQRT_TWO
	},
	{
		SQRT_TWO * 4.0, SQRT_TWO * 6.0, SQRT_TWO * 3.0, SQRT_TWO
	}
	},
	{
	{
		2.8, 6.7, 2.0, 1.0
	},
	{
		2.8, 6.7, 2.5, 1.0
	},
	{
		2.8, 6.7, 3.0, 1.0
	}
	},
	{
	{
		SQRT_TWO * 2.0, SQRT_TWO * 6.0, SQRT_TWO * 2.0, SQRT_TWO
	},
	{
		SQRT_TWO * 2.0, SQRT_TWO * 6.0, SQRT_TWO * 2.5, SQRT_TWO
	},
	{
		SQRT_TWO * 2.0, SQRT_TWO * 6.0, SQRT_TWO * 3.0, SQRT_TWO
	}
	},
	{
	{
		2.0, 5.0, 2.0, 1.0
	},
	{
		2.0, 5.0, 2.5, 1.0
	},
	{
		2.0, 5.0, 3.0, 1.0
	}
	},
	{
	{
		3.0, 4.0, 2.0, 1.0
	},
	{
		3.0, 4.0, 2.5, 1.0
	},
	{
		3.0, 4.0, 3.0, 1.0
	}
	},
	{
	{
		4.0, 2.0, 2.0, 1.0
	},
	{
		4.0, 1.6, 2.5, 1.0
	},
	{
		4.0, 2.0, 3.0, 1.0
	}
	}
};
GLUnurbsObj* theNurbs;

void CALLBACK ErrorCallback(GLenum which)
{
	if (which != expectedError)
	{
		fprintf(stderr, "Unexpected error occured (%d):\n", which);
		fprintf(stderr, "    %s\n", gluErrorString(which));
	}
}

void Init(void)
{
	theNurbs = gluNewNurbsRenderer();
	gluNurbsCallback(theNurbs, GLU_ERROR, ErrorCallback);

	gluNurbsProperty(theNurbs, GLU_SAMPLING_TOLERANCE, 15.0);
	gluNurbsProperty(theNurbs, GLU_DISPLAY_MODE, GLU_OUTLINE_PATCH);

	expectedError = GLU_INVALID_ENUM;
	gluNurbsProperty(theNurbs, ~0, 15.0);
	expectedError = GLU_NURBS_ERROR13;
	gluEndSurface(theNurbs);
	expectedError = 0;

	glColor3f(1.0, 1.0, 1.0);
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);

	glPushMatrix();

	glTranslatef(4.0, 4.5, 2.5);
	glRotatef(rotY, 1, 0, 0);
	glRotatef(rotX, 0, 1, 0);
	glTranslatef(-4.0, -4.5, -2.5);

	gluBeginSurface(theNurbs);
	gluNurbsSurface(theNurbs, S_NUMKNOTS, sknots, T_NUMKNOTS, glutnots, 4 * T_NUMPOINTS, 4, &ctlpoints[0][0][0], S_ORDER, T_ORDER, GL_MAP2_VERTEX_4);
	gluEndSurface(theNurbs);

	glPopMatrix();

	glFlush();
}

void reshape(int width, int height)
{
	glViewport(0, 0, width, height);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glFrustum(-2.0, 2.0, -2.0, 2.0, 0.8, 10.0);
	gluLookAt(7.0, 4.5, 4.0, 4.5, 4.5, 2.5, 6.0, -3.0, 2.0);
	glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 27:
		exit(0);
	}
}

void special(int key, int x, int y)
{
	switch (key)
	{
	case GLUT_KEY_DOWN:
		rotX -= 5;
		glutPostRedisplay();
		break;
	case GLUT_KEY_UP:
		rotX += 5;
		glutPostRedisplay();
		break;
	case GLUT_KEY_LEFT:
		rotY -= 5;
		glutPostRedisplay();
		break;
	case GLUT_KEY_RIGHT:
		rotY += 5;
		glutPostRedisplay();
		break;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("NURBS Test");	//開啟視窗 並顯示出視窗 Title

	Init();

	glutDisplayFunc(display);		//設定callback function
	glutReshapeFunc(reshape);		//設定callback function
	glutKeyboardFunc(keyboard);		//設定callback function
	glutSpecialFunc(special);		//設定callback function

	printf("按 上 下 左 右 控制\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}
