#include "../../Common.h"

int display_mode = 1;

int full_screen = 0;

int num_polygon_edge = 3;

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

void draw_point_test(void)
{
    //畫點
    glPointSize(20.0f);	//設定點的大小, N X N
    glBegin(GL_POINTS);
    for (float i = 1; i < 8; i += 2)
    {
        float j = i * 1 / 10;

        glColor3f(1.0, 0.0, 0.0);	//紅

        glVertex2f(-j, -j);
        glVertex2f(-j, 0);
        glVertex2f(-j, j);
        glVertex2f(0, j);
        glVertex2f(j, j);
        glVertex2f(j, 0);
        glVertex2f(j, -j);
        glVertex2f(0, -j);
    }
    glEnd();
}

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
        reset_default_setting();

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

        draw_boundary(color_y, 0.9f); //畫視窗邊界
    }
    else if (display_mode == 2)
    {
        reset_default_setting();

        //display_mode = 2  //畫 彩色三角形

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
        reset_default_setting();

        int i;
        int n = 10;

        float pnts[11][2] = {
        };

        for (i = 0; i <= n; i++)
        {
            pnts[i][0] = (float)i;
            pnts[i][1] = sin((float)i / 1) * 5 + 5;
        }

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
                glVertex2f(pnts[i][0], pnts[i][1]);
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
        reset_default_setting();

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
        reset_default_setting();

        //display_mode = 5  //畫實心Polygon
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        //glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0); //設置窗口座標系大小, 若不設置, 預設為 (-1,1,-1,1,-1,1)

        glColor3f(1.0, 1.0, 0.0);   //設定顏色 Yellow

        float cx = 0.0f;
        float cy = 0.0f;
        float r = 0.9f;
        float angle_offset = 18;
        glBegin(GL_POLYGON);    //實心多邊形
        {
            for (float theta = angle_offset; theta < (angle_offset + 360.0f); theta += (360.0f / num_polygon_edge))
            {
                glVertex3f(cx + r * cos(PI * theta / 180), cy + r * sin(PI * theta / 180), 0.0);
                //printf("theta = %f x = %f, y = %f\n", theta, cx + r * cos(PI * theta / 180), cy + r * sin(PI * theta / 180));
            }
        }
        glEnd();
        num_polygon_edge++;
    }
    else if (display_mode == 6)
    {
        reset_default_setting();

        //畫顏色色塊
        float mat[16];

        //glEnable(GL_DEPTH_TEST);	//若Enable, 會留下痕跡

        glClearDepth(1.0);

        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);   //設置窗口座標系大小


        glGetFloatv(GL_PROJECTION_MATRIX, mat);
        /*
        int i;
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
        reset_default_setting();

        //畫實心矩形
        float x_st = -0.6f;
        float y_st = -0.6f;
        float w = 1.2f;
        float h = 1.2f;
        fill_rectangle(color_c, x_st, y_st, w, h);

        //畫實心矩形
        fill_rectangle(color_m, -0.4f, -0.4f, 0.8f, 0.8f);

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
        reset_default_setting();

        draw_boundary(color_y, 0.9f); //畫視窗邊界

        float width = 3;
        float x1 = 0;
        float y1 = 0.3f;
        float x2 = 0.3f;
        float y2 = -0.3f;
        float x3 = -0.3f;
        float y3 = -0.3f;
        //draw_triangle(color_y, width, x1, y1, x2, y2, x3, y3);

        draw_point_test();

        //畫多邊形
        glColor3f(0.2f, 0.6f, 0.5f);    //設定顏色
        glBegin(GL_POLYGON);
        {
            //多邊形的頂點數：數越大越趨近于圓
            const int n = 10;
            const GLfloat R = 0.3f;
            const GLfloat pi = 3.1415926f;
            for (int i = 0; i < n; i++)
            {
                glVertex2f(R * cos(2 * pi / n * i), R * sin(2 * pi / n * i));
            }
        }
        glEnd();

        //畫實心矩形
        float dd = 0.15f;
        glBegin(GL_QUADS);              //矩形
        {
            glColor3f(0.0f, 0.0f, 1.0f); //設定顏色, B
            glVertex2f(-dd, -dd);    // x, y
            glVertex2f(dd, -dd);
            glVertex2f(dd, dd);
            glVertex2f(-dd, dd);
        }
        glEnd();
    }
    else if (display_mode == 9)
    {
        reset_default_setting();

        glPushMatrix();		//這個 Matrix Push/Pop 好像沒什麼用??

        // 設置當前的繪製顏色 , 4 個 unsigned byte 
        // 每個顏色的分量占一個字節
        // 參數數據是 R 紅色 G 綠色 B 藍色 A 透明度
        // 下面設置的含義是白色, 繪製點的時候, 每次都使用白色繪製
        glColor4ub(255, 255, 255, 255);	//設定顏色 White

        draw_boundary(color_y, 0.9f); //畫視窗邊界

        draw_coordinates(0.9f);     //畫座標軸

        glLineWidth(4.0f);	//設定線寬

        // 繪製線時, 會將從 glBegin 到 glEnd 之間的所有的點都繪製出來
        // 可以調用 glVertex3f 方法 成對 設置多條線
        // 注意必須成對設置 , 如果設置奇數個點 , 最後一個點會被丟棄

        glBegin(GL_LINES);	// 繪製線段開始

        // glVertex3f (GLfloat x, GLfloat y, GLfloat z)
        //畫直線, 每兩個點組成一條線

        glVertex3f(0.0f, 0.0f, -1.0f);
        glVertex3f(-1.0f, 0.0f, -1.0f);

        glVertex3f(-0.8f, -0.8f, 0.0f);
        glVertex3f(0.8f, 0.8f, 0.0f);

        float xx = 0.0f;
        float yy = 0.0f;
        float dx = 0.0f;
        float dy = 0.0f;
        for (xx = -0.8f; xx <= 0.8f; xx += 0.1f)
        {
            dx = xx + 0.8f;
            glVertex3f(-0.8f + dx, -0.8f, 0.0f);
            dy = xx + 0.8f;
            glVertex3f(-0.8f, 0.8f - dy, 0.0f);
        }
        glEnd();	// 繪製點結束

        //兩個線段組合成一個閉合三角形
        glBegin(GL_LINE_LOOP);	// 繪製線段開始

        glVertex3f(0.7f, 0.5f, 0.0f);
        glVertex3f(0.7f, 0.1f, 0.0f);

        glVertex3f(0.7f, 0.1f, 0.0f);
        glVertex3f(0.3f, 0.1f, 0.0f);

        glEnd();	// 繪製點結束

        //繪製彩色的線

        glLineWidth(12.0f);	//設定線寬

        glBegin(GL_LINE_LOOP);

        // 繪製線 , 每兩個點組成一條線
        glVertex3f(0.0f, -0.8f, 0.0f);

        glColor4ub(0, 255, 0, 255);	//設定顏色 G, 用256制

        glVertex3f(0.8f, -0.8f, 0.0f);

        // 上面的設置會從 (0,0,-10) 座標向 (-5,0,-10) 座標繪製一條線

        glColor4ub(0, 0, 255, 255);	//設定顏色 B, 用256制

        //glVertex3f(-5.0f, 0.0f, -10.0f);
        glVertex3f(0.8f, 0.3f, 0.0f);

        glColor4ub(255, 255, 255, 255);//設定顏色 White

        // 上面的設置會從 (-5,0,-10) 座標向 (-5,-2,-10) 座標繪製一條線

        glEnd();	// 繪製點結束

        glPopMatrix();

        glLineWidth(1.0f);	//設定線寬
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
    const char* windowName = "簡單2D OpenGL畫圖 0 ~ 9";
    const char* message = "簡單2D OpenGL畫圖 0 ~ 9\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape0, keyboard);

    //int res = glutGetWindow();
    //printf("當前視窗的標記符 = %d\n", res);
    //printf("取得視窗寬度 : %d\n", glutGet(GLUT_WINDOW_WIDTH));
    //printf("取得視窗高度 : %d\n", glutGet(GLUT_WINDOW_HEIGHT));

    glutSetCursor(GLUT_CURSOR_DESTROY); //改變視窗上的鼠標標記

    glutMainLoop();	//開始主循環繪製     // Enter the event-processing loop

    return 0;
}

