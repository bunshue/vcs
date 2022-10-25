//#include <GL/freeglut.h>	//64位元用的
#include <GL/glut.h>		//32位元用的

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 初始化參數
void init()
{
    //glClearColor(0.0, 0.0, 0.0, 1.0);
    glShadeModel(GL_SMOOTH);
}

// 繪圖回調函數
void display()
{
    //printf("d ");
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT);

    // 繪製三角形	3D
    glBegin(GL_TRIANGLES);
	float dd = 2.5f;
    glColor3f(1, 0, 0);     //紅
		glVertex3f(-dd, -dd, -5); //左下

    glColor3f(0, 1, 0);     //綠
		glVertex3f(dd, -dd, -5);  //右下

    glColor3f(0, 0, 1);     //藍
		glVertex3f(0, dd, -5);   //上
    glEnd();

    // 執行繪圖命令
    glFlush();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
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
		exit(0);
        return;
    }
}

int main(int argc, char** argv)
{
    // 初始化顯示模式
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Color Map");		// 設定視窗標題

    init();

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}

