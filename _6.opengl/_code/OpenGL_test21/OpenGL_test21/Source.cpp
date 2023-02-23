#include "../../Common.h"

int main_w, w1, w2, w3, w4;

void time1(int value);
void time2(int value);
void time3(int value);
void time4(int value);
void time5(int value);
void time6(int value);
void time7(int value);
void time8(int value);

// 繪圖回調函數
void display(void)
{
    //glClear(GL_COLOR_BUFFER_BIT);   //清除背景

    //draw_boundary(color_y, 0.9f); //畫視窗邊界

    glClear(GL_COLOR_BUFFER_BIT);
    glutSwapBuffers();

    //glFlush();  // 執行繪圖命令
}

void time1(int value)
{
    printf("timer1 砍掉 w1, 設定 timer2 在 500 ms 後啟動\n");
    glutDestroyWindow(w1);
    glutTimerFunc(500, time2, 0);
}

void time2(int value)
{
    printf("timer2 砍掉 w2, 設定 timer3 在 500 ms 後啟動\n");
    glutDestroyWindow(w2);
    glutTimerFunc(500, time3, 0);
}

void time3(int value)
{
    printf("timer3 砍掉 w3, 設定 timer4 在 500 ms 後啟動\n");
    glutDestroyWindow(w3);
    glutTimerFunc(500, time4, 0);
}

void time4(int value)
{
    printf("timer4 砍掉 w4, 設定 timer5 在 500 ms 後啟動\n");
    glutDestroyWindow(w4);
    glutTimerFunc(500, time5, 0);
}

void time5(int value)
{
    w1 = glutCreateSubWindow(main_w, 10, 10, 10, 10);
    glutDisplayFunc(display);
    w2 = glutCreateSubWindow(w1, 10, 10, 30, 30);
    glutDisplayFunc(display);
    w3 = glutCreateSubWindow(w2, 10, 10, 50, 50);
    glutDisplayFunc(display);
    glutInitDisplayMode(GLUT_RGB);
    w4 = glutCreateSubWindow(w3, 10, 10, 70, 70);
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glutDisplayFunc(display);
    printf("timer5 設定 timer6 在 500 ms 後啟動\n");
    glutTimerFunc(500, time6, 0);
}

void time6(int value)
{
    printf("timer6 砍掉 w1, 設定 timer7 在 500 ms 後啟動\n");
    glutDestroyWindow(w1);
    glutTimerFunc(500, time7, 0);

    glutInitDisplayMode(GLUT_INDEX);

    w1 = glutCreateSubWindow(main_w, 10, 10, 10, 10);
    glutDisplayFunc(display);
    w2 = glutCreateSubWindow(w1, 10, 10, 30, 30);
    glutDisplayFunc(display);
    w3 = glutCreateSubWindow(w2, 10, 10, 50, 50);
    glutDisplayFunc(display);
    glutInitDisplayMode(GLUT_RGB);
    w4 = glutCreateSubWindow(w3, 10, 10, 70, 70);
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glutDisplayFunc(display);
}

void time7(int value)
{
    printf("timer7 砍掉 main_w, 設定 timer8 在 500 ms 後啟動\n");
    glutDestroyWindow(main_w);
    glutTimerFunc(500, time8, 0);
}

void time8(int value)
{
    printf("time8 time8 time8 time8\n");
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);    //宣告顯示模式為 Single Buffer 和 INDEX

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    main_w = glutCreateWindow("OpenGL測試");	//開啟視窗 並顯示出視窗 Title

    glClearColor(0.0, 0.0, 0.0, 0.0);  /* black */

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");
    printf("\n空白範例\n");

    int x_st = 10;
    int y_st = 200;
    int w = 50;
    int h = 50;
    int dx = w;
    int dy = h;
    w1 = glutCreateSubWindow(main_w, x_st, y_st, w, h);

    x_st += dx;
    y_st += dy;
    glClearIndex(1);    //第1種顏色
    glutDisplayFunc(display);
    w2 = glutCreateSubWindow(main_w, x_st, y_st, w, h);
    glutCopyColormap(w1);

    x_st += dx;
    y_st += dy;
    glClearIndex(2);    //第2種顏色
    glutDisplayFunc(display);
    w3 = glutCreateSubWindow(main_w, x_st, y_st, w, h);
    glutCopyColormap(w1);

    x_st += dx;
    y_st += dy;
    glClearIndex(3);    //第3種顏色
    glutDisplayFunc(display);
    w4 = glutCreateSubWindow(main_w, x_st, y_st, w, h);
    glutCopyColormap(w1);

    glClearIndex(3);    //第3種顏色
    glutDisplayFunc(display);
    printf("main   設定 timer1 在 500 ms 後啟動\n");
    glutTimerFunc(750, time1, 0);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

