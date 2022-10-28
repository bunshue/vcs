#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

// 繪圖回調函數
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);

    // 設置當前的繪製顏色 , 4 個 unsigned byte 
    // 每個顏色的分量占一個字節
    // 參數數據是 R 紅色 G 綠色 B 藍色 A 透明度
    // 下面設置的含義是白色, 繪製點的時候, 每次都使用白色繪製
    glColor4ub(255, 255, 255, 255);

    // 設置當前點的大小
    glPointSize(5.0f);

    glLineWidth(5.0f);	//設定線寬

    // 繪製三角形
    glBegin(GL_TRIANGLES);

    glNormal3f(0.0f, -1.0f, 0.0f);	//設置法線
    glColor4ub(255, 0, 0, 255);     //R
    glVertex3f(-1.0f, -0.9f, -2.0f);    //左下

    glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
    glColor4ub(0, 255, 0, 255);     //G
    glVertex3f(1.0f, -0.9f, -2.0f); //右下

    glNormal3f(0.0f, 1.0f, 0.0f);	//設置法線
    glColor4ub(0, 0, 255, 255);     //B
    glVertex3f(0.0f, 2.5f, -10.0f); //上

    // 繪製三角形結束
    glEnd();

    // 矩陣出棧 
    //glPopMatrix();

    glFlush();  //強制刷新緩存區
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glClearColor(1.0, 0.0, 0.0, 1.0);   //設置背景顏色 R

// 矩陣環境初始化 , 主要是投影矩陣和模型矩陣 
// ( 選中投影矩陣 ) 設置矩陣模式 , 告知 GPU 當前要操作的矩陣是投影矩陣
    glMatrixMode(GL_PROJECTION);
    // ( 給投影矩陣設置值 ) 向投影矩陣設置參數
    // 參數一 : 50.0f 是攝像機的視口角度
    // 參數二 : 800.0f / 600.0f 是窗口的寬高比
    // 參數三 : 0.1f , 可視的最近的距離
    // 參數四 : 1000.0f , 可視的最遠距離
    gluPerspective(50.0f, 800.0f / 600.0f, 0.1f, 1000.0f);

    // 上述設置好了攝像機的參數 , 具體的攝像機能看什么東西 , 就需要模型視圖矩陣設置

    // ( 選中模型矩陣 )
    glMatrixMode(GL_MODELVIEW);
    // ( 設置模型矩陣值 ) , 這里設置的是單位矩陣
    glLoadIdentity();   //設置單位矩陣
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
    }
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard);	//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}
