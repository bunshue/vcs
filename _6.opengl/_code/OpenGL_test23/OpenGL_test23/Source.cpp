#include "../../Common.h"

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    draw_boundary(color_y, 0.9f); //畫視窗邊界

    //畫一個實心矩形
    glColor3f(0.0, 1.0, 1.0);   //設定顏色 cc
    float dd = 0.3f;
    glRectf(-dd, -dd, dd, dd);  //實心矩形

    draw_teapot(color_r, 1, 0.3);   //畫一個茶壺

    float x_st = -0.7f;
    float y_st = 0.5f;
    const char str1[30] = "Empty example";
    draw_string1(str1, color_r, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

    glFlush();  // 執行繪圖命令
}

// 窗口大小變化回調函數
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
        //離開視窗
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

void mainMenu(int id)
/* This is the callback function for the main menu. */
{
    double lineWidth, color[4];

    switch (id)
    {
    case 1: /* reset default values */
        //glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
        printf("你按了 第 1 項  Reset Default, 1.0\n");
        glColor3d(0.0, 0.0, 0.0);
        glLineWidth(1.0);
        glEndList();
        break;
    case 2: /* clear the screen */
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
    case 3: /* exit the program */
        printf("你按了 第 3 項  Exit, 1.0\n");
        exit(0);
        break;
    default: /* in case none of the above occur */
        break;
    }
}

void initMenus()
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

int main(int argc, char** argv)
{
    const char* windowName = "右鍵選單範例";
    const char* message = "右鍵選單範例\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    initMenus();        //設定表單按鈕

    printf("\n右鍵選單範例\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

