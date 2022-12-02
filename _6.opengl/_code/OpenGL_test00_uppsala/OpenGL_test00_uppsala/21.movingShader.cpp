/******************************************************************************
 * movingShader.c                                                             *
 *                                                                            *
 * This is an OpenGL shading language program that demonstrates moving        *
 * vertices. It is based on the shader.c program, and uses the moving vertex  *
 * shader from chapter 9 of the Angel text.                                   *
 ******************************************************************************/

#include "../../Common.h"

#include <stdio.h>
#include <stdlib.h>
#include <GL/glew.h>
#include <GL/glut.h>
#include <math.h>
#include <time.h>

#define SIZE 400  /* the size, in pixels, of the square window to open */

GLuint program;
GLint timeParam;
GLfloat myTime, timeInc=0.075;

void display (void);
void gfxinit ();
void shader_init ();
void keyboard(unsigned char key, int x, int y);
void idleFunc (void);
void sleep (clock_t wait);

void main(int argc, char **argv)
{
	GLenum err;
	
	glutInit(&argc, argv);
	glutInitWindowSize(SIZE, SIZE);
	glutInitWindowPosition(50, 100);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutCreateWindow("Maxwell's Shader Triangle");
	glutDisplayFunc(display);
	glutKeyboardFunc(keyboard);
	glutIdleFunc(idleFunc);
	gfxinit();
	err = glewInit();
	if (err != GLEW_OK) printf("GLEW error\n");
	printf("Status: Using GLEW %s\n", glewGetString(GLEW_VERSION));
	if (glewGetExtension("GL_ARB_fragment_shader")      != GL_TRUE ||
		glewGetExtension("GL_ARB_vertex_shader")        != GL_TRUE ||
		glewGetExtension("GL_ARB_shader_objects")       != GL_TRUE ||
		glewGetExtension("GL_ARB_shading_language_100") != GL_TRUE)
	{
		printf("Driver does not support OpenGL Shading Language\n");
		exit(1);
	}
	glutMainLoop();
}

void display (void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_TRIANGLES);
	{
		glColor3f(1.0, 0.0, 0.0);
		glVertex2f(0.0, 0.0);
		glColor3f(0.0, 1.0, 0.0);
		glVertex2f(1.0, 0.0);
		glColor3f(0.0, 0.0, 1.0);
		glVertex2f(0.5, sqrt(3.0) * 0.5);
	}
	glEnd();
	glutSwapBuffers();
}

void gfxinit()
{
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-0.4, 1.4, -0.4, 1.4);
	glClearColor(1.0, 1.0, 1.0, 1.0);
}

void idleFunc (void)
{
    myTime += timeInc;
	glUniform1f (timeParam, myTime);
	glutPostRedisplay ();
	sleep (25);
}

void keyboard(unsigned char key, int x, int y)
{
	static int useShader = 0;
	
	switch (key) {
 	   case 's':
		  useShader = !useShader;
		  if (useShader)
		  {
			shader_init();
			timeParam = glGetUniformLocation (program, "time");
			myTime = 0.0;
			glutIdleFunc (idleFunc);
		  }
 		  else
		  {
		    glutIdleFunc (NULL);
			glUseProgram(0);
		    glutPostRedisplay();
		  }
		  break;
	   case 27:	// exit if esc is pushed
		  exit(0);
		  break;
	}
}

void shader_init()
{
	GLint param;
	GLuint vshader, fshader;

	static const char *vcode = {
"/* vertex shader that moves vertex locations sinusoidally */"
"uniform float time; /* value provided by application program */"
"void main()"
"{"
" float s;"
" s = 1.0 + 0.5*sin(time);"
" gl_Position = vec4(s, s, s, 1.0) * (gl_ModelViewProjectionMatrix * gl_Vertex);"
"}"
	};
	
	static const char *fcode = {
"void main()"
"{"
"	gl_FragColor = vec4(0.8471, 0.7490, 0.8471, 1.0);"
"}"
	};

	vshader = glCreateShader(GL_VERTEX_SHADER);
	glShaderSource(vshader, 1, &vcode, NULL);
	glCompileShader(vshader);
	glGetShaderiv(vshader, GL_COMPILE_STATUS, &param);
	if (param == GL_TRUE)
		printf("Vertex shader successfully compiled\n");
	else
		printf("Vertex shader did not compile\n");
	fshader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fshader, 1, &fcode, NULL);
	glCompileShader(fshader);
	glGetShaderiv(fshader, GL_COMPILE_STATUS, &param);
	if (param != GL_FALSE)
		printf("Fragment shader successfully compiled\n");
	else
		printf("Fragment shader did not compile\n");
	program = glCreateProgram();
	glAttachShader(program, vshader);
	glAttachShader(program, fshader);
	glLinkProgram(program);
	glGetShaderiv(program, GL_LINK_STATUS, &param);
	if (param != GL_FALSE)
		printf("Program successfully linked\n");
	else
		printf("Program did not link\n");
	glUseProgram(program);
}

/* Pauses for a specified number of milliseconds. */
void sleep (clock_t wait)
{
	clock_t goal;
	goal = wait + clock();
	while (goal > clock());
}