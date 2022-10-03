#include <GL/glut.h>      //32 bits
//#include <GL/freeglut.h>    //64 bits

void display(void)
{
	/*
	glClear(GL_COLOR_BUFFER_BIT);
	glRectf(-0.5f, -0.5f, 0.5f, 0.5f);
	glFlush();
	*/
	glClearColor(1.0, 1.0, 1.0, 0.0);
glClear(GL_COLOR_BUFFER_BIT);

glBegin(GL_TRIANGLES);
   glColor3f(1.0, 0.0, 0.0);
  glVertex2f(50.f, 50.f);
   glVertex2f(150.f, 50.f);
   glVertex2f(100.f, 150.f);
glEnd();

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

