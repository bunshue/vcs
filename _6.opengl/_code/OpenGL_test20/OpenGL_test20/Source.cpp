#include "../../Common.h"

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
}

// ���f�j�p�ܤƦ^�ը��
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //���}����
        glutDestroyWindow(glutGetWindow());
        return;

    case '1':
        printf("1\n");
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
    const char* windowName = "OpenGL����";
    const char* message = "�����, �L����, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //�]�wcallback function
    glutMotionFunc(motion);     //�]�wcallback function

    printf("\n�ťսd��\n");

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

