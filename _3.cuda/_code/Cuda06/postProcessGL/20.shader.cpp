// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

// CUDA includes
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// CUDA utilities and system includes
#include <helper_cuda.h>

#include <helper_functions.h>
#include <rendercheck_gl.h>

//------以上固定---------------------------------------------------

/******************************************************************************
 * shader.c                                                                   *
 *                                                                            *
 * This is a simple OpenGL shading language program. It produces a standard   *
 * Maxwell's triangle, and the triangle can be shaded through the GLSL by     *
 * pressing key 's' (actually 's' toggles the shading back and forth).        *
 * When it's shaded by the GLSL, the triangle's y vertices are scaled by 3/4  *
 * and the color is thistle.                                                  *
 ******************************************************************************/

#define SIZE 400  /* the size, in pixels, of the square window to open */

void shader_init()
{
	GLint param;
	GLuint vshader, fshader, program;

	static const char* vcode = {
"void main()"
"{"
" gl_Position = gl_ProjectionMatrix * gl_ModelViewMatrix * gl_Vertex;"
" gl_Position.y *= 0.75;"
"}"
	};

	static const char* fcode = {
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
	{
		printf("Vertex shader successfully compiled\n");
	}
	else
	{
		printf("Vertex shader did not compile\n");
	}
	fshader = glCreateShader(GL_FRAGMENT_SHADER);
	glShaderSource(fshader, 1, &fcode, NULL);
	glCompileShader(fshader);
	glGetShaderiv(fshader, GL_COMPILE_STATUS, &param);
	if (param != GL_FALSE)
	{
		printf("Fragment shader successfully compiled\n");
	}
	else
	{
		printf("Fragment shader did not compile\n");
	}
	program = glCreateProgram();
	glAttachShader(program, vshader);
	glAttachShader(program, fshader);
	glLinkProgram(program);
	glGetShaderiv(program, GL_LINK_STATUS, &param);
	if (param != GL_FALSE)
	{
		printf("Program successfully linked\n");
	}
	else
	{
		printf("Program did not link\n");
	}
	glUseProgram(program);
}


void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_TRIANGLES);
	{
		glColor3f(1.0, 0.0, 0.0);
		glVertex2f(0.0, 0.0);
		glColor3f(0.0, 1.0, 0.0);
		glVertex2f(1.0, 0.0);
		glColor3f(0.0, 0.0, 1.0);
		glVertex2f(0.5f, (float)sqrt(3.0) * 0.5f);
	}
	glEnd();
	glutSwapBuffers();
}

void gfxinit()
{
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-0.1, 1.1, -0.1, 1.1);
	glClearColor(1.0, 1.0, 1.0, 1.0);
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
}

void keyboard(unsigned char key, int x, int y)
{
	static int useShader = 0;

	switch (key)
	{
	case 's':
		useShader = !useShader;
		if (useShader)
			shader_init();
		else
			glUseProgram(0);
		glutPostRedisplay();
		break;
	case 27:
		exit(0);
		break;
	}
}
int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

	glutInitWindowSize(SIZE, SIZE);		// 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置

	glutCreateWindow("Maxwell's Shader Triangle");

	glutDisplayFunc(display);   //設定callback function
	glutReshapeFunc(reshape);   //設定callback function
	//glutKeyboardFunc(keyboard0); //設定callback function

	glutKeyboardFunc(keyboard);

	gfxinit();

	GLenum err;
	err = glewInit();
	if (err != GLEW_OK) printf("GLEW error\n");
	printf("Status: Using GLEW %s\n", glewGetString(GLEW_VERSION));
	if (glewGetExtension("GL_ARB_fragment_shader") != GL_TRUE ||
		glewGetExtension("GL_ARB_vertex_shader") != GL_TRUE ||
		glewGetExtension("GL_ARB_shader_objects") != GL_TRUE ||
		glewGetExtension("GL_ARB_shading_language_100") != GL_TRUE)
	{
		printf("Driver does not support OpenGL Shading Language\n");
		exit(1);
	}

	glutMainLoop();	//開始主循環繪製

	return 0;
}
