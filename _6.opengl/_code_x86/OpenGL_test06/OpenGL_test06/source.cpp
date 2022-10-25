#include <iostream>
#include <helper_gl.h>

//#include <GL/freeglut.h>	//64位元用的
#include <GL/glut.h>		//32位元用的

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

GLenum doubleBuffer;
GLint thing1, thing2, thing3, thing4;
float alpha = 0.5;

static void Init(void)
{
    //           R    G    B     A
    glClearColor(0.0, 0.0, 0.0, 0.0);   //設定背景色(0 0 0為黑色)

    glClearAccum(0.0, 0.0, 0.0, 0.0);

    thing1 = glGenLists(1);
    glNewList(thing1, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);   //R
    glRectf(-1.0, -0.8, 1.0, 0.8);
    glEndList();

    thing2 = glGenLists(1);
    glNewList(thing2, GL_COMPILE);
    glColor3f(0.0, 1.0, 0.0);   //G
    glRectf(-0.8, -1.0, 0.2, 1.0);
    glEndList();

    thing3 = glGenLists(1);
    glNewList(thing3, GL_COMPILE);
    glColor3f(0.0, 0.0, 1.0);   //B
    glRectf(-0.2, -1.0, 0.8, 1.0);

    /*
    thing4 = glGenLists(1);
    glNewList(thing4, GL_COMPILE);
    glColor3f(1.0, 0.0, 0.0);   //xxxx
    glRectf(-1.2, -1.2, 1.2, 1.2);
    */

    glEndList();
}


static void display(void)
{
    glPushMatrix();	//這個 Matrix Push/Pop 好像沒什麼用??

    glScalef(0.8, 0.8, 0.8);	//X Y Z所佔整個視窗的比例 最大為1.0 就是100%

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing1);
    glAccum(GL_LOAD, alpha);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing2);
    glAccum(GL_ACCUM, alpha);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing3);
    glAccum(GL_ACCUM, alpha);

    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(thing4);
    glAccum(GL_ACCUM, alpha);

    char mesg[20];
    sprintf(mesg, "Alpha = %3.3f", alpha);
    glutSetWindowTitle(mesg);

    alpha += 0.1;
    if (alpha > 1.01)
    {
        alpha = 0;
    }

    glAccum(GL_RETURN, 1.0);

    glPopMatrix();

    if (doubleBuffer)
    {
        glutSwapBuffers();
    }
    else
    {
        glFlush();
    }
}

static void reshape(int width, int height)
{
    glViewport(0, 0, width, height);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
}

static void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case '1':
        printf("畫實心色塊\n");
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        glutPostRedisplay();	//重做display()
        break;
    case '2':
        printf("畫空心色塊(外框)\n");
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        glutPostRedisplay();	//重做display()
        break;
    case 'r':
        printf("重畫 alpha = %f ", alpha);
        glutPostRedisplay();	//重做display()
        break;
    case 27:
        exit(0);
    }
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);

    type = GLUT_RGB | GLUT_ACCUM;
    type |= (doubleBuffer) ? GLUT_DOUBLE : GLUT_SINGLE;
    glutInitDisplayMode(type);	//設定Single Buffer 或是 Double Buffer

	glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("顏色重疊測試");	// 設定視窗標題

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

	printf("按1 2 3 控制\n");

	glutMainLoop();	// 開始主循環繪制

	return 0;
}


