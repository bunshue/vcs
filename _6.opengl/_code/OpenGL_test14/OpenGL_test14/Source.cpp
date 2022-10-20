#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// 繪圖回調函數
void display(void)
{

}

// 窗口大小變化回調函數
void reshape(int w, int h)
{

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
    }
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

void mainMenu(int i) { keyboard((unsigned char)i, 0, 0); }

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
    //glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("畫顏色色塊");	//開啟視窗 並顯示出視窗 Title

    //init();       //TBD
    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    //glutKeyboardUpFunc(keyup);  //設定callback function TBD
    glutSpecialFunc(special);   //設定callback function
    glutMouseFunc(mouse);		//設定callback function
    glutMotionFunc(motion);		//設定callback function
    glutIdleFunc(idle);         //設定callback function
    //cleanup TBD
    //timer TBD
    initMenus();        //設定表單按鈕

    glutMainLoop();

    return 0;
}


