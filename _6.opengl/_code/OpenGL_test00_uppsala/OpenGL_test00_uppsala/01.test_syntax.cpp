//���ջy�k�M��

#include "../../Common.h"

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //���϶¦�

    draw_boundary(color_y, 0.9f); //�e�������
    draw_teapot(color_r, 1, 0.3);   //�e�@�ӯ���

    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    const char* windowName = "���ջy�k";
    const char* message = "���ջy�k �M��, �� Esc ���}\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard0);

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}

