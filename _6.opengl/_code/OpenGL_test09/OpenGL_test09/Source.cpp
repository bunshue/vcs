#include "../../Common.h"

float angle = 0;

// 初始化參數
void init()
{
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);
    glClearColor(0.1f, 0.1f, 0.4f, 0.0f);   //設定背景色
    glShadeModel(GL_SMOOTH);

    //CBMPLoader bmpLoader;
    //bmpLoader.LoadBmp("/123-bmp.bmp");

    //glGenTextures(1, &tex2D);	//生成紋理對象
    //glBindTexture(GL_TEXTURE_2D, tex2D);	//綁定紋理

    // 紋理濾波參數設置
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP);

    // 設置紋理數據
    //glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, bmpLoader.imageWidth, bmpLoader.imageHeight, 0, GL_RGB, GL_UNSIGNED_BYTE, bmpLoader.image);
}

// 繪圖回調函數
void display(void)
{
    // 清除之前幀數據
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glPushMatrix();
    glTranslatef(0.0f, 0.0f, -5.0f);
    glRotated(angle, 1, 1, 0);

    draw_coordinates(2.0);

    draw_teapot(color_r, 1.0, 1.6);	//畫一個茶壺

    draw_box(color_g);  //繪製木箱

    glPopMatrix();

    glFlush();  // 執行繪圖命令

    angle += 0.02f;
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

static void idle(void)
{
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    
    //glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("開啟視窗");	//開啟視窗 並顯示出視窗 Title

    init();

    glutDisplayFunc(display);	//設定callback function
    glutReshapeFunc(reshape);	//設定callback function
    glutKeyboardFunc(keyboard0);    //設定callback function
    glutIdleFunc(idle);			//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}


