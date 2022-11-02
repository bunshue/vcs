#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

#define REFRESH_DELAY 1000  // ms

void draw_boundary(float* color, float dd)
{
    //用 GL_LINE_LOOP 畫一個空心矩形
    glColor3fv((GLfloat*)color);    //設定顏色
    float point1[3] = { -dd, -dd, 0 };	//左下
    float point2[3] = { dd, -dd, 0 };	//右下
    float point3[3] = { dd,  dd, 0 };	//右上
    float point4[3] = { -dd,  dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();

    //畫中心十字
    glBegin(GL_LINES);
    glVertex3f(-dd, 0.0f, 0.0f);    //左
    glVertex3f(dd, 0.0f, 0.0f);     //右
    glVertex3f(0.0f, dd, 0.0f);     //上
    glVertex3f(0.0f, -dd, 0.0f);    //下

    glEnd();
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //畫視窗邊界
    float color_yellow[4] = { 1.0f, 1.0f, 0.0f, 1.0f };
    draw_boundary(color_yellow, 0.9);

    glColor3f(1.0, 0.0, 0.0);   //設定顏色 R
    float dd = 0.1f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{

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
    }
}

void keyboardup(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("keyboardup ");
    //keyDown[key] = false;
}

//key 枚举值，x、y是位置
void special(int key, int x, int y)
{
    if (key == GLUT_KEY_UP)
    {
        printf("上 ");
    }
    if (key == GLUT_KEY_DOWN)
    {
        printf("下 ");
    }
    if (key == GLUT_KEY_LEFT)
    {
        printf("左 ");
    }
    if (key == GLUT_KEY_RIGHT)
    {
        printf("右 ");
    }
}

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

void idle()
{
    //printf("i");
    //glutPostRedisplay();
}

void cleanup()
{
    printf("cleanup()\n");
}

void mainMenu(int i)
{
    keyboard((unsigned char)i, 0, 0);
}

void timerEvent(int value)
{
    printf("經過1秒 ");
    glutPostRedisplay();
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
}

void initMenus()
{
    glutCreateMenu(mainMenu);   //選單管理
    glutAddMenuEntry("Nearest      [1]", '1');  //新增一個選單條目
    glutAddMenuEntry("Bilinear     [2]", '2');
    glutAddMenuEntry("Bicubic      [3]", '3');
    glutAddMenuEntry("Fast Bicubic [4]", '4');
    glutAddMenuEntry("Catmull-Rom  [5]", '5');
    glutAddMenuEntry("Zoom in      [=]", '=');
    glutAddMenuEntry("Zoom out     [-]", '-');
    glutAddMenuEntry("Benchmark    [b]", 'b');
    glutAddMenuEntry("DrawCurves   [c]", 'c');
    glutAddMenuEntry("Quit       [esc]", 27);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("基本的OpenGL架構");	//開啟視窗 並顯示出視窗 Title

    //init();       //TBD
    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutKeyboardUpFunc(keyboardup);//設定callback function
    glutSpecialFunc(special);   //設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function
    glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫
    glutCloseFunc(cleanup);     //設定callback function
    //timer TBD
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    initMenus();        //設定表單按鈕

    glutMainLoop();	//開始主循環繪製

    return 0;
}


