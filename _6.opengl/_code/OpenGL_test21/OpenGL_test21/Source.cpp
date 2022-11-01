#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void draw_boundary(float* color, float dd)
{
    //用 GL_LINE_LOOP 畫一個空心矩形
    glColor3fv((GLfloat*)color);
    float point1[3] = { -dd, -dd, 0 };	//左下
    float point2[3] = { dd, -dd, 0 };		//右下
    float point3[3] = { dd,  dd, 0 };		//右上
    float point4[3] = { -dd,  dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   // 清除之前幀數據

    //畫視窗邊界
    float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
    draw_boundary(color_yellow, 13.0);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    //printf("reshape is called\n");
    glViewport(0, 0, w, h);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();   //設置單位矩陣
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();   //設置單位矩陣

    gluLookAt(0, 0, 25, 0, 0, -1, 0, 1, 0);
    //eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz
    //第一組eyex, eyey, eyez 相機在世界坐標的位置
    //第二組centerx, centery, centerz 相機鏡頭對準的物體在世界坐標的位置
    //第三組upx, upy, upz 相機向上的方向在世界坐標中的方向
    //你把相機想象成為你自己的腦袋：
    //第一組數據就是腦袋的位置
    //第二組數據就是眼睛看的物體的位置
    //第三組就是頭頂朝向的方向（因為你可以歪著頭看同一個物體）。
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
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

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
    glutInitWindowPosition(600, 200);	//視窗起始位置

    glutCreateWindow("OpenGL測試");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

