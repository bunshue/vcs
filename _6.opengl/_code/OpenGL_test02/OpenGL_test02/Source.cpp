//#include "../../../_code/Common.h"    //32 bits
#include "../../Common.h"   //64 bits

int display_mode = 1;

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
        //display_mode = 1
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景
        //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

        //畫實心矩形
        glColor3f(1.0f, 1.0f, 0.0f);    //設定顏色 Yellow
        glRectf(-0.4f, -0.4f, 0.4f, 0.4f);

    }
    else if (display_mode == 2)
    {
        //display_mode = 2
        glClearColor(0.0f, 0.0f, 0.0f, 1.0f);   //設置背景色 與 透明度, Black
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景
        //glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();	//設置單位矩陣
        gluOrtho2D(-1, 1, -1, 1); //窗口座標範圍, 2D

        // 設置當前的繪製顏色 , 4 個 unsigned byte 
        // 每個顏色的分量占一個字節
        // 參數數據是 R 紅色 G 綠色 B 藍色 A 透明度
        // 下面設置的含義是白色, 繪製點的時候, 每次都使用白色繪製
        glColor4ub(255, 255, 255, 255);

        glPointSize(5.0f); 	//設定點的大小, N X N

        glLineWidth(5.0f);	//設定線寬

        float dd = 0.6f;
        // 繪製三角形
        glBegin(GL_TRIANGLES);

        glNormal3f(0.0f, -1.0f, 0.0f);	//設置法線
        glColor4ub(255, 0, 0, 255);     //R
        glVertex3f(-dd, -dd, 0);    //左下

        glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 255, 0, 255);     //G
        glVertex3f(dd, -dd, 0); //右下

        glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
        glColor4ub(0, 0, 255, 255);     //B
        glVertex3f(0.0f, dd, 0); //上

        // 繪製三角形結束
        glEnd();

        // 矩陣出棧 
        //glPopMatrix();
    }
    else if (display_mode == 3)
    {
        //display_mode = 3

        glOrtho(-10, 10, -10, 10, -10, 10);      //正交投影

            /*
    //用黃色塗背景	要兩行一起寫，若不寫，則是以黑色為背景
   glClearColor(1.0, 1.0, 0.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT);	//清除背景
   */

        glPolygonMode(GL_FRONT, GL_LINE);

        draw_boundary(color_y, 9.6f); //畫視窗邊界

        float dd;
        glColor3f(1.0, 1.0, 1.0);	//White
        glBegin(GL_QUADS);	//畫矩形
        //逆時針為空心
        //畫一個白色外框
        dd = 9.4f;
        glVertex3f(-dd, dd, 0.0f);	//左上
        glVertex3f(-dd, -dd, 0.0f);	//左下
        glVertex3f(dd, -dd, 0.0f);	//右下
        glVertex3f(dd, dd, 0.0f);	//右上

        //順時針為實心
        //畫一個白色實心矩形
        dd = 3.0f;
        glVertex3f(-dd, dd, 0.0f);	//左上
        glVertex3f(dd, dd, 0.0f);	//右上
        glVertex3f(dd, -dd, 0.0f);	//右下
        glVertex3f(-dd, -dd, 0.0f);	//左下
        glEnd();

        //畫三角形 2D
        glBegin(GL_TRIANGLES);
        glColor3f(1.0, 0.0, 0.0);	//R
        //逆時針為空心
        glVertex2f(2.0, 4.0);	//左下
        glVertex2f(8.0, 4.0);	//右下
        glVertex2f(5.0, 9.0);	//上
        glEnd();

        //畫三角形 3D
        glBegin(GL_TRIANGLES);
        //逆時針為空心
        for (dd = 7.0f; dd <= 9.0f; dd += 1.0f)
        {
            glColor3f(1, 0, 0);	//R
            glVertex3f(dd, -dd, 0);	//右下
            glColor3f(0, 1, 0);	//G
            glVertex3f(0, dd, 0);	//上
            glColor3f(0, 0, 1);	//B
            glVertex3f(-dd, -dd, 0);	//左下
        }

        /*
        //順時針為實心
        dd = 1.0f;
        {
            glColor3f( 0, 0, 1);	//B
            glVertex3f(-dd, -dd, 0);	//左下
            glColor3f( 0, 1, 0);	//G
            glVertex3f( 0, dd, 0);	//上
            glColor3f( 1, 0, 0);	//R
            glVertex3f( dd, -dd, 0);	//右下
        }
        */
        glEnd();

        //畫矩形
        float x_st = -8.0f;
        float y_st = 2.0f;
        float w = 4.0f;
        float h = 4.0f;
        //左下x,  左下y,  右上x,  右上y
        glRectf(x_st, y_st, x_st + w, y_st + h);

        for (dd = 1.0f; dd <= 2.0f; dd += 0.5f)
        {
            //左下x,  左下y,  右上x,  右上y
            //glRectf(dd, dd, dd+3.0f, dd+3.0f);
            glRectf(x_st + dd, y_st + dd, x_st + w + dd, y_st + h + dd);
        }

    }
    else if (display_mode == 4)
    {
        //display_mode = 4
    }
    else if (display_mode == 5)
    {
        //display_mode = 5
    }
    else if (display_mode == 6)
    {
        //display_mode = 6  //畫
    }
    else if (display_mode == 7)
    {
        //display_mode = 7  //畫
    }
    else if (display_mode == 8)
    {
        //display_mode = 8  //畫
    }
    else if (display_mode == 9)
    {
        //display_mode = 9  //畫
    }
    else
    {
        printf("XXXXXXXXXXXXXXXXXXXXX\n");
    }

    glFlush();  //強制刷新緩存區
    glutSwapBuffers();  // 將後緩沖區繪製到前臺
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    /* 有問題
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
    */
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;
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

    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, 10, "%d", display_mode);

    glutSetWindowTitle(info);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

    glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
    glutInitWindowPosition(1100, 200);	//視窗起始位置

    glutCreateWindow("簡單2D OpenGL畫圖 0 ~ 9");    // 設定視窗標題

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape0);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function
    glutMouseFunc(mouse0);		//設定callback function
    glutMotionFunc(motion0);    //設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}


