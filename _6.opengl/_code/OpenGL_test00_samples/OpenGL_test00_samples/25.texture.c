#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <math.h>
#include <sys/types.h>
#include <sys/stat.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include "rgb.h"

RGBImageRec* image = NULL;

float* minFilter, * magFilter, * sWrapMode, * tWrapMode;
float decal[] = { GL_DECAL };
float modulate[] = { GL_MODULATE };
float repeat[] = { GL_REPEAT };
float clamp[] = { GL_CLAMP };
float nr[] = { GL_NEAREST };
float ln[] = { GL_LINEAR };
float nr_mipmap_nr[] = { GL_NEAREST_MIPMAP_NEAREST };
float nr_mipmap_ln[] = { GL_NEAREST_MIPMAP_LINEAR };
float ln_mipmap_nr[] = { GL_LINEAR_MIPMAP_NEAREST };
float ln_mipmap_ln[] = { GL_LINEAR_MIPMAP_LINEAR };
GLint sphereMap[] = { GL_SPHERE_MAP };

GLenum doSphere = GL_FALSE;
float xRotation = 0.0;
float yRotation = 0.0;
float zTranslate = -3.125;

GLint cube;
float c[6][4][3] = {
	{
	{
		1.0, 1.0, -1.0
	},
	{
		-1.0, 1.0, -1.0
	},
	{
		-1.0, -1.0, -1.0
	},
	{
		1.0, -1.0, -1.0
	}
	},
	{
	{
		1.0, 1.0, 1.0
	},
	{
		1.0, 1.0, -1.0
	},
	{
		1.0, -1.0, -1.0
	},
	{
		1.0, -1.0, 1.0
	}
	},
	{
	{
		-1.0, 1.0, 1.0
	},
	{
		1.0, 1.0, 1.0
	},
	{
		1.0, -1.0, 1.0
	},
	{
		-1.0, -1.0, 1.0
	}
	},
	{
	{
		-1.0, 1.0, -1.0
	},
	{
		-1.0, 1.0, 1.0
	},
	{
		-1.0, -1.0, 1.0
	},
	{
		-1.0, -1.0, -1.0
	}
	},
	{
	{
		-1.0, 1.0, 1.0
	},
	{
		-1.0, 1.0, -1.0
	},
	{
		1.0, 1.0, -1.0
	},
	{
		1.0, 1.0, 1.0
	}
	},
	{
	{
		-1.0, -1.0, -1.0
	},
	{
		-1.0, -1.0, 1.0
	},
	{
		1.0, -1.0, 1.0
	},
	{
		1.0, -1.0, -1.0
	}
	}
};

float n[6][3] = {
	{
	0.0, 0.0, -1.0
	},
	{
	1.0, 0.0, 0.0
	},
	{
	0.0, 0.0, 1.0
	},
	{
	-1.0, 0.0, 0.0
	},
	{
	0.0, 1.0, 0.0
	},
	{
	0.0, -1.0, 0.0
	}
};

float t[6][4][2] = {
	{
	{
		1.1,  1.1
	},
	{
		-0.1, 1.1
	},
	{
		-0.1, -0.1
	},
	{
		1.1,  -0.1
	}
	},
	{
	{
		1.1,  1.1
	},
	{
		-0.1, 1.1
	},
	{
		-0.1, -0.1
	},
	{
		1.1,  -0.1
	}
	},
	{
	{
		-0.1,  1.1
	},
	{
		1.1, 1.1
	},
	{
		1.1, -0.1
	},
	{
		-0.1,  -0.1
	}
	},
	{
	{
		1.1,  1.1
	},
	{
		-0.1, 1.1
	},
	{
		-0.1, -0.1
	},
	{
		1.1,  -0.1
	}
	},
	{
	{
		1.1,  1.1
	},
	{
		-0.1, 1.1
	},
	{
		-0.1, -0.1
	},
	{
		1.1,  -0.1
	}
	},
	{
	{
		1.1,  1.1
	},
	{
		-0.1, 1.1
	},
	{
		-0.1, -0.1
	},
	{
		1.1,  -0.1
	}
	},
};

void BuildCube(void)
{
	GLint i;

	glNewList(cube, GL_COMPILE);
	for (i = 0; i < 6; i++)
	{
		glBegin(GL_POLYGON);
		glNormal3fv(n[i]); glTexCoord2fv(t[i][0]); glVertex3fv(c[i][0]);
		glNormal3fv(n[i]); glTexCoord2fv(t[i][1]); glVertex3fv(c[i][1]);
		glNormal3fv(n[i]); glTexCoord2fv(t[i][2]); glVertex3fv(c[i][2]);
		glNormal3fv(n[i]); glTexCoord2fv(t[i][3]); glVertex3fv(c[i][3]);
		glEnd();
	}
	glEndList();
}

void BuildLists(void)
{
	cube = glGenLists(1);
	BuildCube();
}

void Init(void)
{
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
	gluBuild2DMipmaps(GL_TEXTURE_2D, 3, image->sizeX, image->sizeY, GL_RGB, GL_UNSIGNED_BYTE, image->data);
	glTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, decal);
	glEnable(GL_TEXTURE_2D);	//啟用2D紋理映射

	glFrontFace(GL_CCW);
	glCullFace(GL_FRONT);
	glEnable(GL_CULL_FACE);

	BuildLists();

	glClearColor(0.0, 0.0, 0.0, 0.0);

	magFilter = nr;
	minFilter = nr;
	sWrapMode = repeat;
	tWrapMode = repeat;
}

void reshape(int width, int height)
{
	glViewport(0, 0, width, height);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(145.0, 1.0, 0.01, 1000);
	glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
	switch (key)
	{
	case 'T':
		zTranslate += 0.25;
		glutPostRedisplay();
		break;
	case 't':
		zTranslate -= 0.25;
		glutPostRedisplay();
		break;
	case 's':
		doSphere = !doSphere;
		if (doSphere)
		{
			glTexGeniv(GL_S, GL_TEXTURE_GEN_MODE, sphereMap);
			glTexGeniv(GL_T, GL_TEXTURE_GEN_MODE, sphereMap);
			glEnable(GL_TEXTURE_GEN_S);
			glEnable(GL_TEXTURE_GEN_T);
		}
		else
		{
			glDisable(GL_TEXTURE_GEN_S);
			glDisable(GL_TEXTURE_GEN_T);
		}
		glutPostRedisplay();
		break;
	case '0':
		magFilter = nr;
		glutPostRedisplay();
		break;
	case '1':
		magFilter = ln;
		glutPostRedisplay();
		break;
	case '2':
		minFilter = nr;
		glutPostRedisplay();
		break;
	case '3':
		minFilter = ln;
		glutPostRedisplay();
		break;
	case '4':
		minFilter = nr_mipmap_nr;
		glutPostRedisplay();
		break;
	case '5':
		minFilter = nr_mipmap_ln;
		glutPostRedisplay();
		break;
	case '6':
		minFilter = ln_mipmap_nr;
		glutPostRedisplay();
		break;
	case '7':
		minFilter = ln_mipmap_ln;
		glutPostRedisplay();
		break;
	case 27:
	case 'q':
	case 'Q':
		//離開視窗
		glutDestroyWindow(glutGetWindow());
		return;
	}
}

void special(int key, int /*x*/, int /*y*/)
{
	switch (key)
	{
	case GLUT_KEY_LEFT:
		yRotation -= 4.5;
		glutPostRedisplay();
		break;
	case GLUT_KEY_RIGHT:
		yRotation += 4.5;
		glutPostRedisplay();
		break;
	case GLUT_KEY_UP:
		xRotation -= 4.5;
		glutPostRedisplay();
		break;
	case GLUT_KEY_DOWN:
		xRotation += 4.5;
		glutPostRedisplay();
		break;
	}
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);

	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, sWrapMode);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, tWrapMode);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, magFilter);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, minFilter);

	glPushMatrix();

	glTranslatef(0.0, 0.0, zTranslate);
	glRotatef(xRotation, 1, 0, 0);
	glRotatef(yRotation, 0, 1, 0);
	glCallList(cube);

	glPopMatrix();

	glFlush();
}

void Args(int argc, char** argv)
{
	GLint i;

	for (i = 1; i < argc; i++)
	{
		if (strcmp(argv[i], "-f") == 0)
		{
			if (i + 1 >= argc || argv[i + 1][0] == '-')
			{
				printf("-f (No file name).\n");
				exit(1);
			}
			else
			{
				image = rgbImageLoad(argv[++i]);
				if (image == NULL)
				{
					printf("-f (Bad file name).\n");
					exit(1);
				}
			}
		}
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
	Args(argc, argv);

	if (image == NULL)
	{
		char* filename = "data//1.rgb";
		image = rgbImageLoad(filename);
	}

	if (image == NULL)
	{
		printf("No texture file.\n");
		exit(1);
	}

	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

	glutInitWindowSize(600, 600);       // 設定視窗大小
	glutInitWindowPosition(1100, 200);  // 設定視窗位置

	glutCreateWindow("Texture Test");	//開啟視窗 並顯示出視窗 Title

	Init();

	glutDisplayFunc(display);       //設定callback function
	glutReshapeFunc(reshape);       //設定callback function
	glutKeyboardFunc(keyboard);     //設定callback function
	glutSpecialFunc(special);		//設定callback function

	printf("按 上 下 左 右 控制\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}
