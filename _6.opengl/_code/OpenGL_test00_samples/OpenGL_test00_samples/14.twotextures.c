#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include "rgb.h"

int winW = 600;
int winH = 600;

RGBImageRec* earthImage = NULL;
RGBImageRec* skyImage = NULL;
GLint skyList;
GLint earthList;

float* minFilter;
float* magFilter;
float* sWrapMode;
float* tWrapMode;
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

int horizon;
float texMinX;
float texMinY;
float texMaxX;
float texMaxY;

void Init(void)
{
	glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

	magFilter = nr;
	minFilter = nr;
	sWrapMode = repeat;
	tWrapMode = repeat;

	glTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, decal);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, magFilter);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, minFilter);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, sWrapMode);
	glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, tWrapMode);
	glEnable(GL_TEXTURE_2D);

	glClearColor(0.0, 0.0, 0.0, 0.0);

	horizon = winH / 2;

	texMinX = 0.25;
	texMaxX = 0.75;

	texMinY = 0.25;
	texMaxY = 0.75;

	skyList = glGenLists(1);
	glNewList(skyList, GL_COMPILE);
	gluBuild2DMipmaps(GL_TEXTURE_2D, 3, skyImage->sizeX, skyImage->sizeY, GL_RGB, GL_UNSIGNED_BYTE, skyImage->data);
	glEndList();

	earthList = glGenLists(1);
	glNewList(earthList, GL_COMPILE);
	gluBuild2DMipmaps(GL_TEXTURE_2D, 3, earthImage->sizeX, earthImage->sizeY, GL_RGB, GL_UNSIGNED_BYTE, earthImage->data);
	glEndList();
}

void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT);

	glPushMatrix();

	glCallList(skyList);
	glBegin(GL_POLYGON);
	glTexCoord2f(texMinX, texMinY);
	glVertex2i(0, horizon);
	glTexCoord2f(texMaxX, texMinY);
	glVertex2i(winW, horizon);
	glTexCoord2f(texMaxX, texMaxY);
	glVertex2i(winW, winH);
	glTexCoord2f(texMinX, texMaxY);
	glVertex2i(0, winH);
	glEnd();

	glCallList(earthList);
	glBegin(GL_POLYGON);
	glTexCoord2f(0.0, 0.0);
	glVertex2i(0, 0);
	glTexCoord2f(1.0, 0.0);
	glVertex2i(winW, 0);
	glTexCoord2f(1.0, 1.0);
	glVertex2i(winW, horizon);
	glTexCoord2f(0.0, 1.0);
	glVertex2i(0, horizon);
	glEnd();

	glPopMatrix();

	glFlush();
}

void reshape(int width, int height)
{
	winW = width;
	winH = height;

	glViewport(0, 0, winW, winH);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0, winW, 0, winH);
	glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case '1':
		horizon -= 5;
		texMinY -= 5.0 / (float)winH;
		texMinY += 5.0 / (float)winH;
		texMaxY += 5.0 / (float)winH;
		glutPostRedisplay();
		break;
	case '2':
		horizon += 5;
		texMinY += 5.0 / (float)winH;
		texMinY -= 5.0 / (float)winH;
		texMaxY -= 5.0 / (float)winH;
		glutPostRedisplay();
		break;
	case 27:
		exit(0);
	}
}

void special(int key, int x, int y)
{
	switch (key)
	{
	case GLUT_KEY_LEFT:
		texMinX -= 5.0 / (float)winW;
		texMaxX -= 5.0 / (float)winW;
		glutPostRedisplay();
		break;
	case GLUT_KEY_RIGHT:
		texMinX += 5.0 / (float)winW;
		texMaxX += 5.0 / (float)winW;
		glutPostRedisplay();
		break;
	case GLUT_KEY_UP:
		texMinY += 5.0 / (float)winH;
		texMaxY += 5.0 / (float)winH;
		glutPostRedisplay();
		break;
	case GLUT_KEY_DOWN:
		texMinY -= 5.0 / (float)winH;
		texMaxY -= 5.0 / (float)winH;
		glutPostRedisplay();
		break;
	}
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);

	char* filename1 = "data//1.rgb";
	earthImage = rgbImageLoad(filename1);

	if (earthImage == NULL)
	{
		printf("No earth texture file.\n");
		exit(1);
	}

	char* filename2 = "data//2.rgb";
	skyImage = rgbImageLoad(filename2);

	if (skyImage == NULL)
	{
		printf("No sky texture file.\n");
		exit(1);
	}

	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

	glutInitWindowSize(winW, winH);
	glutInitWindowPosition(1100, 200);

	glutCreateWindow("Two Texture Test");	//開啟視窗 並顯示出視窗 Title

	Init();

	glutDisplayFunc(display);       //設定callback function
	glutReshapeFunc(reshape);       //設定callback function
	glutKeyboardFunc(keyboard);     //設定callback function
	glutSpecialFunc(special);		//設定callback function

	printf("按 上 下 左 右 控制\n");

	glutMainLoop();	//開始主循環繪製

	return 0;
}
