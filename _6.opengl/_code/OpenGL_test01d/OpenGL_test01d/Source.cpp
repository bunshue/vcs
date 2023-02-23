#include "../../Common.h"

#define REFRESH_DELAY 1000  // ms

int time_elapsed = 0;

// 繪圖回調函數
void display(void)
{
    display0();

    char info[20];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "經過 %d 秒", time_elapsed);
    glutSetWindowTitle(info);
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    printf("KBDDN ");
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
    }
}

void keyboardup(unsigned char key, int /*x*/, int /*y*/)
{
    printf("KBDUP ");
    //keyDown[key] = false;
}

void mouse(int button, int state, int x, int y)
{
    //MouseDown
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        printf("LD ");
        //printf("左鍵按下(%d, %d) ", mx, my);
    }
    else if (button == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN)
    {
        printf("MD ");
        //printf("中鍵按下(%d, %d) ", mx, my);
    }
    else if (button == GLUT_RIGHT_BUTTON && state == GLUT_DOWN)
    {
        printf("RD ");
        //printf("右鍵按下(%d, %d) ", mx, my);
    }
    else if (button == GLUT_LEFT_BUTTON && state == GLUT_UP)
    {
        printf("LU ");
        //printf("左鍵放開(%d, %d) ", mx, my);
    }
    else if (button == GLUT_MIDDLE_BUTTON && state == GLUT_UP)
    {
        printf("MU ");
        //printf("中鍵放開(%d, %d) ", mx, my);
    }
    else if (button == GLUT_RIGHT_BUTTON && state == GLUT_UP)
    {
        printf("RU ");
        //printf("右鍵放開(%d, %d) ", mx, my);
    }
    else if (button == 3 && state == GLUT_DOWN)
    {
        printf("SUST ");
        //printf("滾輪向上開始(%d, %d) ", mx, my);
    }
    else if (button == 3 && state == GLUT_UP)
    {
        printf("SUSP ");
        //printf("滾輪向上停止(%d, %d) ", mx, my);
    }
    else if (button == 4 && state == GLUT_DOWN)
    {
        printf("SDST ");
        //printf("滾輪向下開始(%d, %d) ", mx, my);
    }
    else if (button == 4 && state == GLUT_UP)
    {
        printf("SDSP ");
        //printf("滾輪向下停止(%d, %d) ", mx, my);
    }
    else
    {
        printf("button = %d, state = %d\n", button, state);
    }
}

void motion(int x, int y)
{
    //MouseMove
    printf("M ");
    //printf("M(%d, %d) ", x, y);
}

void timerEvent(int value)
{
    time_elapsed++;
    printf("經過 %d 秒 ", time_elapsed);
    glutPostRedisplay();
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
}

void cleanup(void)
{
    printf("\nclean up\n");
}

int main(int argc, char** argv)
{
    const char* windowName = "各種 callback function 使用範例";
    const char* message = "按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function
    glutCloseFunc(cleanup);     //設定callback function

    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);    //設定timer事件

    printf("\n各種 callback function 使用範例\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
