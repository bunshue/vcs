#include "../../Common.h"

int display_mode = 1;

int full_screen = 0;

void reset_default_setting()
{
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

    glLineWidth(1.0f);	//設定線寬

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
}

void display1(void)
{
    float width = 1.0f;
    glLineWidth(width);         //設定線寬

    double size = 0.4;

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    glutWireTeapot(size);       //畫茶壺, 線框

    glTranslatef(0.0f, -1.0f, 0.0f);		//平移至指定地方(累積)
    glutSolidTeapot(size);    //畫茶壺, 實心

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    draw_boundary(color_y, 0.96f); //畫視窗邊界
}

void display2(void)
{
    double size = 0.4f;

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    glutWireCube(size);       //畫茶壺, 線框

    glTranslatef(0.0f, -1.0f, 0.0f);		//平移至指定地方(累積)
    glutSolidCube(size);    //畫茶壺, 實心

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    draw_boundary(color_y, 0.96f); //畫視窗邊界
}

void display3(void)
{
    double radius = 0.4f;
    int slices = 20;
    int stacks = 10;

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    glutWireSphere(radius, slices, stacks); //畫 網格 球

    glTranslatef(0.0f, -1.0f, 0.0f);		//平移至指定地方(累積)
    glutSolidSphere(radius, slices, stacks); //畫 實心 球

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    draw_boundary(color_y, 0.96f); //畫視窗邊界
}

void display4(void)
{
    double base = 0.3;
    double height = 0.4;
    int slices = 20;
    int stacks = 10;

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    glutWireCone(base, height, slices, stacks); //畫 網格 圓錐

    glTranslatef(0.0f, -1.0f, 0.0f);		//平移至指定地方(累積)
    glutSolidCone(base, height, slices, stacks); ////畫 實心 圓錐

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    draw_boundary(color_y, 0.96f); //畫視窗邊界
}

void display5(void)
{
    GLdouble innerRadius = 0.2;
    GLdouble outerRadius = 0.3;
    int sides = 10;
    int rings = 10;

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    glutWireTorus(innerRadius, outerRadius, sides, rings);  //畫 網格 環形曲面

    glTranslatef(0.0f, -1.0f, 0.0f);		//平移至指定地方(累積)
    glutSolidTorus(innerRadius, outerRadius, sides, rings); //畫 實心 環形曲面

    glTranslatef(0.0f, 0.5f, 0.0f);		//平移至指定地方(累積)
    draw_boundary(color_y, 0.96f); //畫視窗邊界
}

void display6(void)
{
    //無大小, 滿框
    glutWireDodecahedron(); //無畫面
    glutSolidDodecahedron();    //無畫面
    glutWireOctahedron();   //ok
    //glutSolidOctahedron();    ok
}

void display7(void)
{
    //無大小, 滿框
    glutWireTetrahedron();
    //glutSolidTetrahedron();
}

void display8(void)
{
    //無大小, 滿框
    glutWireIcosahedron();
    //glutSolidIcosahedron();
}

void display9(void)
{
    //無大小, 滿框
}

// 繪圖回調函數
void display(void)
{
    reset_default_setting();
    if (display_mode == 0)
    {
    }
    else if (display_mode == 1)
    {
        display1();
    }
    else if (display_mode == 2)
    {
        display2();
    }
    else if (display_mode == 3)
    {
        display3();
    }
    else if (display_mode == 4)
    {
        display4();
    }
    else if (display_mode == 5)
    {
        display5();
    }
    else if (display_mode == 6)
    {
        display6();
    }
    else if (display_mode == 7)
    {
        display7();
    }
    else if (display_mode == 8)
    {
        display8();
    }
    else if (display_mode == 9)
    {
        display9();
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }
    glFlush();  // 執行繪圖命令
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
        break;
    case ' ':
        if (full_screen == 0)
        {
            full_screen = 1;
            printf("全螢幕\n");
            glutFullScreen();   //全螢幕顯示
        }
        else
        {
            //恢復成一般螢幕, 有問題
            full_screen = 0;
            printf("一般螢幕\n");
            glutInitWindowSize(600, 600);       // 設定視窗大小
            glutInitWindowPosition(1100, 200);  // 設定視窗位置
        }
        break;
    case '0':
        display_mode = 0;
        break;
    case '1':
        display_mode = 1;
        break;
    case '2':
        display_mode = 2;
        break;
    case '3':
        display_mode = 3;
        break;
    case '4':
        display_mode = 4;
        break;
    case '5':
        display_mode = 5;
        break;
    case '6':
        display_mode = 6;
        break;
    case '7':
        display_mode = 7;
        break;
    case '8':
        display_mode = 8;
        break;
    case '9':
        display_mode = 9;
        break;
    }
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

int main(int argc, char* argv[])
{
    const char* windowName = "繪製基本圖元 0 ~ 9";
    const char* message = "繪製基本圖元 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

