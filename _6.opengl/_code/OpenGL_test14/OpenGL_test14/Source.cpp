#include "../../Common.h"

void draw_something()
{
    draw_boundary(color_y, 0.9f); //畫視窗邊界

    //畫一個實心矩形
    glColor3f(1.0, 0.0, 0.0);   //設定顏色 R
    float dd = 0.1f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形

    //畫一個茶壺
    draw_teapot(color_r, 1.0f, 0.3f);

    glFlush();  // 執行繪圖命令
}

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_something();
}

void mainMenu(int i)
{
    printf("你按了第 %c 項\n", i);
    return;
}

void initMenus1()
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

/* This is the callback function for the color menu. */
void colorMenu(int id)
{
    //glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
    switch (id)
    {
    case 1: /* change color to red */
        printf("你按了第 1 項顏色, 紅色\n");
        glColor3d(1.0, 0.0, 0.0);
        break;
    case 2: /* change color to green */
        printf("你按了第 2 項顏色, 綠色\n");
        glColor3d(0.0, 1.0, 0.0);
        break;
    case 3: /* change color to blue */
        printf("你按了第 3 項顏色, 藍色\n");
        glColor3d(0.0, 0.0, 1.0);
        break;
    case 4: /* change color to black */
        printf("你按了第 4 項顏色, 黑色\n");
        glColor3d(0.0, 0.0, 0.0);
        break;
    default: /* for any case not covered above, leave color unchanged */
        break;
    }
    glEndList();
    //pointsChosen = 0;
}

void sizeMenu(int id)
/* This is the callback function for the size menu. */
{
    //glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
    switch (id)
    {
    case 1: /* change line thickness to 1 */
        printf("你按了第 1 項大小, 1.0\n");
        glLineWidth(1.0);
        break;
    case 2: /* change line thickness to 2 */
        printf("你按了第 1 項大小, 2.0\n");
        glLineWidth(2.0);
        break;
    case 3: /* change line thickness to 3 */
        printf("你按了第 1 項大小, 3.0\n");
        glLineWidth(3.0);
        break;
    default: /* for any case not covered above, leave line thickness unchanged */
        break;
    }
    glEndList();
}

void initMenus2()
{
    int color_menu, size_menu;

    /* Create the menu structure and attach it to the right mouse button. */
    color_menu = glutCreateMenu(colorMenu);
    glutAddMenuEntry("Red", 1);
    glutAddMenuEntry("Green", 2);
    glutAddMenuEntry("Blue", 3);
    glutAddMenuEntry("Black", 4);
    size_menu = glutCreateMenu(sizeMenu);

    glutAddMenuEntry("1", 1);
    glutAddMenuEntry("2", 2);
    glutAddMenuEntry("3", 3);
    glutCreateMenu(mainMenu);

    glutAddSubMenu("Color, with SubMenu", color_menu);
    glutAddSubMenu("Size, with SubMenu", size_menu);

    glutAddMenuEntry("Reset defaults", 1);
    glutAddMenuEntry("Clear window", 2);
    glutAddMenuEntry("Exit", 3);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}

/* 保留範例
void mainMenu(int id)
{
    double lineWidth, color[4];

    switch (id)
    {
    case 1: // reset default values
        //glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
        printf("你按了 第 1 項  Reset Default, 1.0\n");
        glColor3d(0.0, 0.0, 0.0);
        glLineWidth(1.0);
        glEndList();
        break;
    case 2: // clear the screen
        //glDeleteLists(1, numberOfLists);
        //numberOfLists = 0;
        printf("你按了 第 2 項  Clear Screen, 1.0\n");
        glGetDoublev(GL_LINE_WIDTH, &lineWidth);
        glGetDoublev(GL_CURRENT_COLOR, color);
        //glNewList(++numberOfLists, GL_COMPILE);
        glColor4dv(color);
        glLineWidth(lineWidth);
        glEndList();
        glutPostRedisplay();
        break;
    case 3: // exit the program
        printf("你按了 第 3 項  Exit, 1.0\n");
        exit(0);
        break;
    default: // in case none of the above occur
        break;
    }
}
*/

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("基本的OpenGL架構");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape0);	//設定callback function
    glutKeyboardFunc(keyboard0);	//設定callback function

    //initMenus1();        //設定表單按鈕, 無次選單
    initMenus2();        //設定表單按鈕, 有次選單

    glutMainLoop();	//開始主循環繪製

    return 0;
}
