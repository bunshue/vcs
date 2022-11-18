#include "../../Common.h"

// 繪圖回調函數
void display()
{
    //printf("d ");
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT);

    // 繪製三角形	3D
    glBegin(GL_TRIANGLES);
    float dd = 2.5f;
    glColor3f(1, 0, 0);     //紅
    glVertex3f(-dd, -dd, -5); //左下

    glColor3f(0, 1, 0);     //綠
    glVertex3f(dd, -dd, -5);  //右下

    glColor3f(0, 0, 1);     //藍
    glVertex3f(0, dd, -5);   //上
    glEnd();

    // 執行繪圖命令
    glFlush();
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluPerspective(60.0, (GLfloat)w / (GLfloat)h, 0.1, 100000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
}

int main(int argc, char** argv)
{
    // 初始化顯示模式
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Color Map");		//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard0);	//設定callback function

    printf("僅顯示, 無控制, 按 Esc 離開\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
