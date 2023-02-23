#include "../../Common.h"

void  init()
{
    glClearColor(1.0, 1.0, 1.0, 0.0);   //設置顯示窗口背景為白色

    glMatrixMode(GL_PROJECTION);     //設置投影模式
    glLoadIdentity();
    gluOrtho2D(0.0, 500.0, 0.0, 500.0);     //設置觀察參數
};


// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    int  p0[] = { 100, 200 };
    int  p1[] = { 250, 100 };
    int  p2[] = { 400, 200 };
    int  p3[] = { 400, 300 };
    int  p4[] = { 250, 400 };
    int  p5[] = { 100, 300 };

    printf("畫點 紅\n");
    glPointSize(20.0f);	            //設定點的大小, N X N
    glBegin(GL_POINTS);
    glColor3f(1.0, 0.0, 0.0);
    glVertex2i(p0[0], p0[1]);
    glVertex2i(p1[0], p1[1]);
    glVertex2i(p2[0], p2[1]);
    glEnd();

    printf("畫點 綠\n");
    glPointSize(30.0f);	            //設定點的大小, N X N
    glBegin(GL_POINTS);
    glColor3f(0.0, 1.0, 0.0);
    glVertex2iv(p3);
    glVertex2iv(p4);
    glVertex2iv(p5);
    glEnd();

    printf("畫點 藍\n");
    glPointSize(30.0f);	            //設定點的大小, N X N
    glBegin(GL_POINTS);
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3f(338.05f, 269.72f, 0.0f);
    glVertex3f(168.91f, 234.67f, 0.0f);
    glEnd();

    printf("畫直線段 黃\n");
    //使用OpenGL的圖元常量​​GL_LINES​​可連接每一對相鄰端點而得到一組直線段
    glLineWidth(10.0f);	//設定線寬
    glBegin(GL_LINES);
    glColor3f(1.0, 1.0, 0.0);
    glVertex2iv(p0);
    glVertex2iv(p1);
    glVertex2iv(p2);
    glVertex2iv(p3);
    glVertex2iv(p4);
    glVertex2iv(p5);
    glEnd();

    printf("畫折線 桃\n");
    //使用OpenGL的圖元常量​​GL_LINE_STRIP​​可以獲得折線
    glLineWidth(6.0f);	//設定線寬
    glBegin(GL_LINE_STRIP);
    glColor3f(1.0, 0.0, 1.0);
    glVertex2iv(p0);
    glVertex2iv(p1);
    glVertex2iv(p2);
    glVertex2iv(p3);
    glVertex2iv(p4);
    glVertex2iv(p5);
    glEnd();

    printf("畫封閉折線 青\n");
    //使用OpenGL的圖元常量​​GL_LINE_LOOP​​可以獲得封閉折線
    glLineWidth(2.0f);	//設定線寬
    glBegin(GL_LINE_LOOP);
    glColor3f(0.0, 1.0, 1.0);
    glVertex2iv(p0);
    glVertex2iv(p1);
    glVertex2iv(p2);
    glVertex2iv(p3);
    glVertex2iv(p4);
    glVertex2iv(p5);
    glEnd();

    draw_line(color_silver, 6.0f, 338.05f, 269.72f, 168.91f, 234.67f);

    //使用OpenGL常量​​GL_POLYGON​​繪製一個凸多邊形
    glBegin(GL_POLYGON);
    glColor3f(1.0, 0.0, 0.0);
    glVertex2i(200, 350);
    glVertex2i(150, 300);
    glVertex2i(150, 200);
    glVertex2i(200, 150);
    glVertex2i(300, 150);
    glVertex2i(350, 200);
    glVertex2i(350, 300);
    glVertex2i(300, 350);
    glEnd();

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

int main(int argc, char** argv)
{
    const char* windowName = "OpenGL測試";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    glutMouseFunc(mouse);       //設定callback function
    glutMotionFunc(motion);     //設定callback function

    init();

    printf("\n空白範例\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

