#include "../../../_code/Common.h"    //32 bits
//#include "../../Common.h"   //64 bits

int display_mode = 1;

int full_screen = 0;

#define NGRID 10

void drawGrid(int xmin, int xmax, int ymin, int ymax)
{
    int i, j;
    for (j = ymin; j <= ymax; j++) //水平線
    {
        glBegin(GL_LINES);
        {
            glVertex2d(xmin, j);
            glVertex2d(xmax, j);
        }
        glEnd();
    }
    for (i = xmin; i <= xmax; i++) //豎線
    {
        glBegin(GL_LINES);
        {
            glVertex2d(i, ymin);
            glVertex2d(i, ymax);
        }
        glEnd();
    }
}

// 初始化參數
void init01(void)
{
    //好像做不做沒甚麼差別
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black

    //glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
    //glShadeModel(GL_SMOOTH);
}

// 繪圖回調函數
void display(void)
{
    if (display_mode == 0)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        printf("無畫面, TBD, display_mode = %d\n", display_mode);

        //設定預設大小...  TBD
    }
    else if (display_mode == 1)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景
        //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

        //畫一個矩形 R
        glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
        //左下x,左下y,右上x,右上y,
        glRectf(-0.9f, -0.9f, -0.3f, 0.9f);//畫一個矩形

        ////畫一個矩形 G
        glColor4f(0.0, 1.0, 0.0, 1.0);  //設置畫筆顏色為 G
        //左下x,左下y,右上x,右上y,
        glRectf(-0.4f, -0.8f, 0.4f, 0.8f);//畫一個矩形

        //畫一個矩形 B
        glColor4f(0.0, 0.0, 1.0, 1.0);  //設置畫筆顏色為 B
        //左下x,左下y,右上x,右上y,
        glRectf(0.3f, -0.7f, 0.7f, 0.7f);//畫一個矩形

        float x_st = -0.9f;
        float y_st = 0.1f;
        const char str1[30] = "draw_string_test 1";
        draw_string1(str1, color_c, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

        x_st = -0.9f;
        y_st = -0.1f;
        const char str2[30] = "draw_string_test 2";
        draw_string2(str2, color_c, GLUT_BITMAP_TIMES_ROMAN_24, x_st, y_st);

        draw_boundary(color_y, 0.9); //畫視窗邊界
    }
    else if (display_mode == 2)
    {
        //display_mode = 2  //畫 彩色三角形

		glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景
        //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D


        glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??
        // 繪製三角形
        glBegin(GL_TRIANGLES);          // 開始畫三角形
        {
            float dd = 0.5f;
            glColor3f(1.0f, 0.0f, 0.0f);    //設定顏色 R
            //glVertex2f(0.0f, dd);         //(x1,y1)=(0, dd), 上, 2D
            glVertex3f(0, dd, 0);           //(x1,y1)=(0, dd), 上, 3D

            glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G
            //glVertex2f(dd, -dd);          //(x2,y2)=(dd,-dd), 右下, 2D
            glVertex3f(dd, -dd, 0);         //(x2,y2)=(dd,-dd), 右下, 3D

            glColor3f(0.0f, 0.0f, 1.0f);    //設定顏色 B
            //glVertex2f(-dd, -dd);         //(x3,y3)=(-dd,-dd), 左下, 2D
            glVertex3f(-dd, -dd, 0);        //(x3,y3)=(-dd,-dd), 左下, 3D
        }
        glEnd();    // 結束畫三角形
        glPopMatrix();
    }
    else if (display_mode == 3)
    {
        int i;
        int n = 10;

		double pnts[][2] = {
		0, 5,
		1, 3,
		2, 7,
		3, 4,
		4, 0,
		5, 6,
		6, 2,
		7, 10,
		8, 4,
		9, 3,
		10, 7
		};

        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1, NGRID + 1, -1, NGRID + 1); //窗口座標範圍, 2D

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();	//設置單位矩陣

        //畫網格
        glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G
        drawGrid(0, NGRID, 0, NGRID);

        //畫控制點
        glColor3f(1.0f, 0.0f, 0.0f);    //設定顏色 R
        glPointSize(20.0f); 	//設定點的大小, N X N
        for (i = 0; i <= n; i++)
        {
            glBegin(GL_POINTS);
            {
                glVertex2d(pnts[i][0], pnts[i][1]);
            }
            glEnd();
        }

        //畫折線
        glColor3f(1.0f, 1.0f, 1.0f);    //設定顏色 White
        for (i = 0; i < n; i++)
        {
            glBegin(GL_LINES);
            {
                glVertex2d(pnts[i][0], pnts[i][1]);
                glVertex2d(pnts[i + 1][0], pnts[i + 1][1]);
            }
            glEnd();
        }
    }
    else if (display_mode == 4)
    {
        //畫網格
        int i;

        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1.0, 11.0, -1.0, 11.0); //窗口座標範圍, 2D

        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();	//設置單位矩陣

        //畫10*10網格
        glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G
        for (i = 0; i <= 10; i++) //11條水平線
        {
            glBegin(GL_LINES);
            {
                glVertex2d(0.0, i * 1.0);
                glVertex2d(10.0, i * 1.0);
            }
            glEnd();
        }

        glBegin(GL_LINES); //11條豎線
        {
            for (i = 0; i <= 10; i++)
            {
                glVertex2d(i * 1.0, 0.0);
                glVertex2d(i * 1.0, 10.0);
            }
        }
        glEnd();

        //在對角線畫點
        glColor3f(1.0f, 1.0f, 1.0f);    //設定顏色 White
        glPointSize(10.0f); 	//設定點的大小, N X N
        glBegin(GL_POINTS);
        {
            for (i = 0; i <= 10; i++)
            {
                glVertex2d(i * 1.0, i * 1.0);
            }
        }
        glEnd();
        for (i = 0; i <= 10; i++)
        {
            glBegin(GL_POINTS);
            {
                glVertex2d(i * 1.0, 10.0 - i * 1.0);
            }
            glEnd();
        }
    }
    else if (display_mode == 5)
    {
        //display_mode = 5  //畫實心Polygon
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

		glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
		glMatrixMode(GL_PROJECTION);
		glLoadIdentity();	//設置單位矩陣
		glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0); //設置窗口座標系大小

        glColor3f(1.0, 1.0, 0.0);   //設定顏色 Yellow

        glBegin(GL_POLYGON);    //實心多邊形
        {
            glVertex3f(0.25, 0.25, 0.0);
            glVertex3f(0.75, 0.25, 0.0);
            glVertex3f(0.75, 0.75, 0.0);
            glVertex3f(0.5, 1.0, 0.0);
            glVertex3f(0.25, 0.75, 0.0);
        }
        glEnd();
    }
    else if (display_mode == 6)
    {
        //畫顏色色塊
        float mat[16];
        int i;

        //glEnable(GL_DEPTH_TEST);	//若Enable, 會留下痕跡
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClearDepth(1.0);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);   //設置窗口座標系大小
        glGetFloatv(GL_PROJECTION_MATRIX, mat);
        /*
        for (i = 0; i < 16; i++)
        {
            printf("%10.7f", mat[i]);
            if ((i + 1) % 4)
            {
                printf(" ");
            }
            else
            {
                printf("\n");
            }
        }
        */
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();	//設置單位矩陣

        glColor3f(1.0f, 0.0f, 0.0f);    //設定顏色 R //在右上角畫紅色平面：應該在後面
        glBegin(GL_POLYGON);
        {
            glVertex3f(0.0f, 0.0f, -1.0f + 0.001f);
            glVertex3f(1.0f, 0.0f, -1.0f + 0.001f);
            glVertex3f(1.0f, 1.0f, -1.0f + 0.001f);
            glVertex3f(0.0f, 1.0f, -1.0f + 0.001f);
        }
        glEnd();

        glColor3f(0.0f, 1.0f, 0.0f);    //設定顏色 G //在左下角畫綠色的平面：應該在前面
        glBegin(GL_POLYGON);
        {
            glVertex3f(-1.0f, -1.0f, 1.0f - 0.001f);
            glVertex3f(0.0f + 0.5f, -1.0f, 1.0f - 0.001f);
            glVertex3f(0.0f + 0.5f, 0.0f + 0.5f, 1.0f - 0.001f);
            glVertex3f(-1.0f, 0.0f + 0.5f, 1.0f - 0.001f);
        }
        glEnd();


    }
    else if (display_mode == 7)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        float x_st = -0.6;
        float y_st = -0.6;
        float w = 1.2;
        float h = 1.2;
        draw_rectangle_s(color_c, x_st, y_st, w, h);

        //畫實心矩形
        glColor3f(1.0f, 1.0f, 0.0f);    //設定顏色 Yellow
        glRectf(-0.4f, -0.4f, 0.4f, 0.4f);

        //畫實心四邊形
        float dd = 0.5f;
        float x1 = dd;
        float y1 = 0;
        float x2 = 0;
        float y2 = -dd;
        float x3 = -dd;
        float y3 = 0;
        float x4 = 0;
        float y4 = dd;
        draw_quad_s(color_r, x1, y1, x2, y2, x3, y3, x4, y4);
    }
    else if (display_mode == 8)
    {
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        printf("無畫面, TBD, display_mode = %d\n", display_mode);
    }
    else if (display_mode == 9)
    {

        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        printf("無畫面, TBD, display_mode = %d\n", display_mode);

    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

    glFlush();  //強制刷新緩存區
    glutSwapBuffers();  // 將後緩沖區繪製到前臺
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
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
        init01();
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

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, 10, "%d", display_mode);

    glutSetWindowTitle(info);
}

int main(int argc, char* argv[])
{
    //初始化GLUT庫，這個函數只是傳說命令參數并且初始化glut庫
    glutInit(&argc, argv);

    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    /*
    設定圖形顯示模式。引數mode的可選值為：
    GLUT_RGBA：      當未指明GLUT - RGBA或GLUT - INDEX時，是預設使用的模式。表明欲建立RGBA模式的視窗。
    GLUT_RGB：       與GLUT - RGBA作用相同。
    GLUT_INDEX：     指明為顏色索引模式。
    GLUT_SINGLE：    只使用單快取
    GLUT_DOUBLE：    使用雙快取。以避免把計算機作圖的過程都表現出來，或者為了平滑地實現動畫。
    GLUT_DEPTH：     使用深度快取。
    GLUT_ACCUM：     讓視窗使用累加的快取。
    GLUT_ALPHA：     讓顏色緩衝區使用alpha元件。
    GLUT_STENCIL：   使用模板快取。
    GLUT_MULTISAMPLE：讓視窗支援多例程。
    GLUT_STEREO：    使視窗支援立體。
    GLUT_LUMINACE:  luminance是亮度的意思。但是很遺憾，在多數OpenGL平臺上，不被支援。
    */

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("簡單2D OpenGL畫圖 0 ~ 9");    // 設定視窗標題

    //int res = glutGetWindow();
    //printf("當前視窗的標記符 = %d\n", res);
    //printf("取得視窗寬度 : %d\n", glutGet(GLUT_WINDOW_WIDTH));
    //printf("取得視窗高度 : %d\n", glutGet(GLUT_WINDOW_HEIGHT));

    init01();

    glutSetCursor(GLUT_CURSOR_DESTROY); //改變視窗上的鼠標標記

    glutDisplayFunc(display);       //設定callback function, 註冊顯示函數 // Register display callback handler for window re-paint
    glutReshapeFunc(reshape0);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    glutMainLoop();	//開始主循環繪製     // Enter the event-processing loop

    return 0;
}

