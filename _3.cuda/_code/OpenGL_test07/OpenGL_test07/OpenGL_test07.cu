// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//#include <GL/glut.h>  //32位元用的

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除窗口
    
    glClear(GL_COLOR_BUFFER_BIT);   // 示例：执行画面清除
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    //glClearColor(0.1f, 0.2f, 1.f, 1.f); //清除背景 設定顏色

    //glClearColor(1.0, 0.0, 0.0, 1.0);   //清除背景 設定顏色

    glColor4f(1.0, 0.0, 0.0, 1.0);  //設置畫筆顏色為 R
    glRectf(-0.9f, -0.9f, -0.3f, 0.9f);//畫一個矩形

    glColor4f(0.0, 1.0, 0.0, 1.0);  //設置畫筆顏色為 G
    glRectf(-0.4f, -0.8f, 0.4f, 0.8f);//畫一個矩形

    glColor4f(0.0, 0.0, 1.0, 1.0);  //設置畫筆顏色為 B
    glRectf(0.3f, -0.7f, 0.7f, 0.7f);//畫一個矩形


    glFlush();//保證前面的OpenGL命令立即執行   glFlush​​負責刷新繪制緩沖器，保證繪圖命令立即執行。
}

int main(int argc, char* argv[])
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowPosition(1100, 200);
    glutInitWindowSize(600, 600);

    glutCreateWindow("第一個OpenGL程序");

    glutDisplayFunc(display);       //設定callback function

    glutMainLoop();

    return 0;
}