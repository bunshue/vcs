#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void DrawBox();

float angle;

// 初始化參數
void init()
{
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);
    glClearColor(0.1, 0.1, 0.4, 0.0);
    glShadeModel(GL_SMOOTH);

    //CBMPLoader bmpLoader;
    //bmpLoader.LoadBmp("/123-bmp.bmp");

    //glGenTextures(1, &tex2D);	//生成紋理對象
    //glBindTexture(GL_TEXTURE_2D, tex2D);	//綁定紋理

    // 紋理濾波參數設置
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP);

    // 設置紋理數據
    //glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, bmpLoader.imageWidth, bmpLoader.imageHeight, 0, GL_RGB, GL_UNSIGNED_BYTE, bmpLoader.image);

    angle = 0;
}

// 繪圖回調函數
void display(void)
{
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glPushMatrix();
    glTranslatef(0.0f, 0.0f, -5.0f);
    glRotated(angle, 1, 1, 0);
    DrawBox();
    glPopMatrix();

    // 執行繪圖命令
    glFlush();

    //angle++;
    angle += 0.1;

    glutPostRedisplay();
}

/** 繪制木箱 */
void DrawBox()
{
    glEnable(GL_TEXTURE_2D);

    /** 選擇紋理 */
    //glBindTexture(GL_TEXTURE_2D, tex2D);	//綁定紋理

    /** 開始繪制四邊形 */
    glBegin(GL_QUADS);

    /// 前側面
    glNormal3f(0.0f, 0.0f, 1.0f);                               /**指定法線指向觀察者 */
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, 1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, 1.0f, 1.0f);

    /// 后側面
    glNormal3f(0.0f, 0.0f, -1.0f);                              /** 指定法線背向觀察者 */
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, 1.0f, -1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, -1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(1.0f, -1.0f, -1.0f);

    /// 頂面
    glNormal3f(0.0f, 1.0f, 0.0f);                               /**指定法線向上 */
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, 1.0f, 1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, 1.0f, 1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, -1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, 1.0f, -1.0f);

    /// 底面
    glNormal3f(0.0f, -1.0f, 0.0f);                              /** 指定法線朝下 */
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, -1.0f, -1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, -1.0f, -1.0f);

    /// 右側面
    glNormal3f(1.0f, 0.0f, 0.0f);                               /**指定法線朝右 */
    glTexCoord2f(0.0f, 0.0f); glVertex3f(1.0f, -1.0f, -1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, 1.0f, -1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, 1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(1.0f, -1.0f, 1.0f);

    /// 左側面
    glNormal3f(-1.0f, 0.0f, 0.0f);                              /**指定法線朝左 */
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, 1.0f, -1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(-1.0f, 1.0f, 1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, -1.0f, 1.0f);
    glEnd();
    glDisable(GL_TEXTURE_2D);
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
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

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

static void idle(void)
{
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    //glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    init();

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function
    glutIdleFunc(idle);			//設定callback function

    glutMainLoop(); // 開始主循環繪制

    return 0;
}


