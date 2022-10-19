// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

int display_mode = 1;

//display_mode = 01  //畫矩形

void init01(void)
{
	glOrtho(0.0f, 300.0f, 0.0f, 300.0f, 1.0, -1.0); //設置窗口坐標系大小
	glClearColor(0.4f, 1.f, 0.8f, 1.0f);    //設置背景色
}

// 初始化參數
void init05()
{
    glClearColor(0.1, 0.1, 0.4, 0.0);   //設置背景色
    glShadeModel(GL_SMOOTH);
}

// 繪圖回調函數
void display(void)
{
	if (display_mode == 0)
	{
		glClear(GL_COLOR_BUFFER_BIT);   //清除背景

		//or
		glClearColor(1.0f, 1.0f, 1.0f, 1.0f);   // 設置清除窗口背景色為白色
		glClear(GL_COLOR_BUFFER_BIT);   //清除背景
		glFlush();       // 刷新OpenGL中的命令列和，使所有尚未被行的命令行

		//設定預設大小...
	}
    else if (display_mode == 1)
    {
        //display_mode = 1  //畫
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glColor3f(0.0f, 1.0f, 0.0f);//設置繪圖顏色
        glRectf(100.0f, 100.0f, 200.0f, 200.0f);//繪制矩形

        glFlush();//刷新緩沖
        glutSwapBuffers();
    }
    else if (display_mode == 2)
    {
        //display_mode = 2  //畫 彩色三角形
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glPushMatrix();
        glBegin(GL_TRIANGLES);          // 開始畫三角形
        {
            glColor3f(1.0f, 0.0f, 0.0f);         // 設定輸出色為紅色
            glVertex2f(0.0f, 1.0f);           //(x1,y1)=(0, 1)
            glColor3f(0.0f, 1.0f, 0.0f);         // 設定輸出色為綠色
            glVertex2f(0.87f, -0.5f);            //(x2,y2)=(0.87,-0.5)
            glColor3f(0.0f, 0.0f, 1.0f);         // 設定輸出色為藍色
            glVertex2f(-0.87f, -0.5f);           //(x3,y3)=(-0.87,-0.5)
        }
        glEnd();                               // 結束畫三角形
        glPopMatrix();
        glutSwapBuffers();
    }
    else if (display_mode == 3)
    {
        //display_mode = 3  //畫矩形
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        glMatrixMode(GL_MODELVIEW);                        // 選擇模型觀察矩陣
        glLoadIdentity();                                  // 重置模型觀察矩陣   
        glMatrixMode(GL_PROJECTION);                        // 選擇投影矩陣     
        glLoadIdentity();

        glEnable(GL_TEXTURE_2D);    //啟用2D紋理映射
        glBegin(GL_QUADS);
        {
            glTexCoord2f(0.0f, 0.0f);
            glVertex3f(-0.5f, -0.5f, 0.0f);
            glTexCoord2f(1.0f, 0.0f);
            glVertex3f(0.5f, -0.5f, 0.0f);
            glTexCoord2f(1.0f, 1.0f);
            glVertex3f(0.5f, 0.5f, 0.0f);
            glTexCoord2f(0.0f, 1.0f);
            glVertex3f(-0.5f, 0.5f, 0.0f);
        }
        glEnd();
        glDisable(GL_TEXTURE_2D);

        glutSwapBuffers();
    }
    else if (display_mode == 4)
    {
        //display_mode = 4  //畫 矩形 + 四邊形

        //Single/Double buffer 會不一樣
        //glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
        //glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        glRectf(-0.5f, -0.5f, 0.5f, 0.5f);

        glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
        glBegin(GL_QUADS);
        {
            glTexCoord2f(0.8f, 0.0f);
            glVertex2f(0.8f, 0.0f);

            glTexCoord2f(0.0f, -0.8f);
            glVertex2f(0.0f, -0.8f);

            glTexCoord2f(-0.8f, 0.0f);
            glVertex2f(-0.8f, 0.0f);

            glTexCoord2f(0.0f, 0.8f);
            glVertex2f(0.0f, 0.8f);
        }
        glEnd();

        glFlush();
    }
    else if (display_mode == 5)
    {
        //display_mode = 5
            // 清除之前幀數據
        glClear(GL_COLOR_BUFFER_BIT);   //清除背景

        // 繪制三角形
        glBegin(GL_TRIANGLES);
        {
            glColor3f(1, 0, 0);     //紅
            glVertex3f(-2, -2, -5); //左下

            glColor3f(0, 1, 0);     //綠
            glVertex3f(2, -2, -5);  //右下

            glColor3f(0, 0, 1);     //藍
            glVertex3f(0, 2, -5);   //上
        }
        glEnd();

        // 執行繪圖命令
        glFlush();
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
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

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
        init05();
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

void mouse(int button, int state, int x, int y)
{
}

void motion(int x, int y)
{
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);
    //glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //宣告顯示模式為 Single Buffer 和 RGBA

	glutInitWindowSize(600, 600);		//設定視窗大小, 直接拉大內容
	glutInitWindowPosition(1100, 200);	//視窗起始位置

    glutCreateWindow("簡單2D OpenGL畫圖 0 ~ 9");    // 設定視窗標題

    init01();

	glutDisplayFunc(display);	//設定callback function
	glutReshapeFunc(reshape);	//設定callback function
	glutKeyboardFunc(keyboard);	//設定callback function
	glutMouseFunc(mouse);		//設定callback function
	glutMotionFunc(motion);		//設定callback function

	glutMainLoop();

	return 0;
}


