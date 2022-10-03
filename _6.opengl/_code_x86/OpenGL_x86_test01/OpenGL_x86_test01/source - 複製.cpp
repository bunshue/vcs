#include <GL/glut.h>      //32 bits
//#include <GL/freeglut.h>    //64 bits

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glRectf(-0.5f, -0.5f, 0.5f, 0.5f);
	glFlush();
}

int main(int argc, char *argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
	glutInitWindowSize(600, 600);
	glutInitWindowPosition(1100, 200);
	
	glutCreateWindow("OpenGLµ{¦¡");
	
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}

