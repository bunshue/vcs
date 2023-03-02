#include "../../Common.h"

//從 06.rotatingCube1.cpp 和 06.rotatingCube2.cpp 之間抓出來的繞軸旋轉部分

GLfloat theta[] = { 0.0f, 0.0f, 0.0f };	//對各軸的旋轉角度
GLint axis = 0;	//0: 繞x軸旋轉, 1: 繞y軸旋轉, 2: 繞z軸旋轉
GLdouble viewer[] = { 0.0, 0.0, 5.0 }; /* initial viewer location  */

int flag_rotating = 0;
int flag_rotating_direction = 0;	//0: CW, 1:CCW
float dd = 1.0f;
float ddd = 0.06f;

//啟始時的視點
double eyex = 0.0f;
double eyey = 0.0f;
double eyez = 0.0f;
double eye_distance = 2.0f;

// 繪圖回調函數
void display(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	//已旋轉後之座標軸
	draw_coordinates(1.5f);     //畫座標軸

	draw_teapot(color_purple, 1.0f, 1.5f);	//畫茶壺

	glColor3f(1.0f, 1.0f, 1.0f);

	glFlush();  // 執行繪圖命令
}

// This is the reshape callback function. It resets the viewport to the entire window and
// the projection matrix to keep the cube centered in the window.
void reshape(int w, int h)
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
    if (w <= h)
    {
        glOrtho(-2.0, 2.0, -2.0 * (GLfloat)h / (GLfloat)w, 2.0 * (GLfloat)h / (GLfloat)w, 1.0, 5.0);
    }
    else
    {
        glOrtho(-2.0 * (GLfloat)w / (GLfloat)h, 2.0 * (GLfloat)w / (GLfloat)h, -2.0, 2.0, 1.0, 5.0);
    }
	glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
    case 'x':
        printf("從 正X軸 由外向內看\n");
        glLoadIdentity();
        eyex = eye_distance;
        eyey = 0.0f;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 'X':
        printf("從 負X軸 由外向內看\n");
        glLoadIdentity();
        eyex = -eye_distance;
        eyey = 0.0f;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 'y': /* positive y-axis */
        printf("從 正Y軸 由外向內看\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = eye_distance;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0);
        break;
    case 'Y': /* negative y-axis */
        printf("從 負Y軸 由外向內看\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = -eye_distance;
        eyez = 0.0f;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0);
        break;
    case 'z':
        printf("從 正Z軸 由外向內看\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = 0.0f;
        eyez = eye_distance;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
    case 'Z':
        printf("從 負Z軸 由外向內看\n");
        glLoadIdentity();
        eyex = 0.0f;
        eyey = 0.0f;
        eyez = -eye_distance;
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
        break;
        /*   TBD
    case '+':
        printf("Zoom in\n");
        eye_distance -= 0.02f;
        if (eye_distance < 0.1f)
            eye_distance = 0.1f;
        break;
    case '-':
        printf("Zoom out\n");
        eye_distance += 0.02f;
        if (eye_distance > 5.0f)
            eye_distance = 5.0f;
        break;
        */
    }
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

int main(int argc, char** argv)
{
	const char* windowName = "LookAt範例";
	const char* message = "按 x X y Y z Z 由各個方向去看方塊, 按 Esc 離開\n";
	common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

	printf("\nLookAt 範例\n");
    //先保留
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glEnable(GL_DEPTH_TEST);

    /* Set initial view to positive x-axis. */
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    printf("從 正X軸 由外向內看\n");
    eyex = eye_distance;
    gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0); //正X軸

    glutMainLoop();	//開始主循環繪製
	return 0;
}

