#include "../../Common.h"

#define REFRESH_DELAY 1000  // ms

int time_elapsed = 0;

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    //畫一個實心矩形
    glColor3f(1.0, 0.0, 0.0);   //設定顏色 R
    float dd = 0.1f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形

    //畫一個茶壺
    draw_teapot(color_r, 1.0f, 0.3f);


    char info[20];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "經過 %d 秒", time_elapsed);
    glutSetWindowTitle(info);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{

}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
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

//key 枚舉值，x、y是位置
void special(int key, int /*x*/, int /*y*/)
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
    time_elapsed++;
    printf("%d ", time_elapsed);
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

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutKeyboardUpFunc(keyboardup);//設定callback function
    glutSpecialFunc(special);   //設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function
    glutIdleFunc(idle);         //設定callback function, 利用idle事件進行重畫
    glutCloseFunc(cleanup);     //設定callback function
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    initMenus();        //設定表單按鈕

    glutMainLoop();	//開始主循環繪製

    return 0;
}

