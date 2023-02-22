#include "../../Common.h"

#define REFRESH_DELAY 1000  // ms

int time_elapsed = 0;

// ø�Ϧ^�ը��
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //�M���I��

    draw_boundary(color_y, 0.9f); //�e�������

    //�e�@�ӹ�߯x��
    glColor3f(0.0, 1.0, 1.0);   //�]�w�C�� cc
    float dd = 0.3f;
    glRectf(-dd, -dd, dd, dd);  //��߯x��

    draw_teapot(color_r, 1, 0.3);   //�e�@�ӯ���

    float x_st = -0.7f;
    float y_st = 0.5f;
    const char str1[30] = "Empty example";
    draw_string1(str1, color_r, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

    glFlush();  // ����ø�ϩR�O

    char info[20];
    //sprintf(info, "%d", (char)display_mode);  //�L��, x64�����
    sprintf_s(info, sizeof(info), "�g�L %d ��", time_elapsed);
    glutSetWindowTitle(info);
}

void keyboardup(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("keyboardup ");
    //keyDown[key] = false;
}

void timerEvent(int value)
{
    time_elapsed++;
    //printf("%d ", time_elapsed);
    glutPostRedisplay();
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
}

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL����";
    const char* message = "��Lcallback��ƨϥνd��, �����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutKeyboardUpFunc(keyboardup);//�]�wcallback function
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
