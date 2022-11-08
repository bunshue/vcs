#include <helper_gl.h>
#include <GL/freeglut.h>

#include <stdio.h>
#include <iostream>

void draw_coordinates(float len)
{
    float dd = len / 10;
    glLineWidth(3.0f);	//設定線寬

    glColor3f(1.0f, 0.0f, 0.0f); //畫紅色的x軸
    glBegin(GL_LINES);
    glVertex3f(0.0f, 0.0f, 0.0f);	//原點
    glVertex3f(len, 0.0f, 0.0f);	//x軸 len,0,0
    glVertex3f(len, 0.0f, 0.0f);	//x軸 len,0,0
    glVertex3f(len - dd, 0.0f + dd, 0.0f);	//x軸 len,0,0
    glVertex3f(len, 0.0f, 0.0f);	//x軸 len,0,0
    glVertex3f(len - dd, 0.0f - dd, 0.0f);	//x軸 len,0,0
    glEnd();
    glRasterPos3f(len, 0.05, 0);
    glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, 'x');

    glColor3f(0.0, 1.0, 0.0); //畫綠色的y軸
    glBegin(GL_LINES);
    glVertex3f(0.0f, 0.0f, 0.0f);	//原點
    glVertex3f(0.0f, len, 0.0f);	//y軸 0,len,0
    glVertex3f(0.0f, len, 0.0f);	//y軸 0,len,0
    glVertex3f(0.0f - dd, len - dd, 0.0f);	//y軸 0,len,0
    glVertex3f(0.0f, len, 0.0f);	//y軸 0,len,0
    glVertex3f(0.0f + dd, len - dd, 0.0f);	//y軸 0,len,0
    glEnd();
    glRasterPos3f(0, len, 0);
    glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, 'y');

    glColor3f(0.0, 0.0, 1.0); //畫藍色的z軸
    glBegin(GL_LINES);
    glVertex3f(0.0f, 0.0f, 0.0f);	//原點
    glVertex3f(0.0f, 0.0f, len);	//z軸 0,0,len
    glVertex3f(0.0f, 0.0f, len);	//z軸 0,0,len
    glVertex3f(0.0f - dd, 0.0f, len - dd);	//z軸 0,0,len
    glVertex3f(0.0f, 0.0f, len);	//z軸 0,0,len
    glVertex3f(0.0f + dd, 0.0f, len - dd);	//z軸 0,0,len
    glEnd();
    glRasterPos3f(0, 0, len);
    glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, 'z');
}

void draw_boundary(float* color, float dd)
{
    //用 GL_LINE_LOOP 畫一個空心矩形
    glColor3fv((GLfloat*)color);    //設定顏色
    float point1[3] = { -dd, -dd, 0 };	//左下
    float point2[3] = { dd, -dd, 0 };	//右下
    float point3[3] = { dd,  dd, 0 };	//右上
    float point4[3] = { -dd,  dd, 0 };	//左上
    glBegin(GL_LINE_LOOP);
    glVertex3fv(point1);	//左下
    glVertex3fv(point2);	//右下
    glVertex3fv(point3);	//右上
    glVertex3fv(point4);	//左上
    glEnd();

    //畫中心十字
    glBegin(GL_LINES);
    glColor3f(1.0, 0.0, 0.0);		//R
    glVertex3f(-dd, 0.0f, 0.0f);    //左
    glVertex3f(dd, 0.0f, 0.0f);     //右
    glColor3f(0.0, 1.0, 0.0);		//G
    glVertex3f(0.0f, dd, 0.0f);     //上
    glVertex3f(0.0f, -dd, 0.0f);    //下
    glColor3f(0.0, 0.0, 1.0);		//B
    glVertex3f(0.0f, 0.0f, 0.0f);	//中
    glVertex3f(0.0f, 0.0f, dd);		//前
    glEnd();
}

void draw_teapot(float* color, float width, double size)
{
    //畫一個茶壺
    glColor3fv((GLfloat*)color);    //設定顏色

    glLineWidth(width);     //設定線寬
    glutWireTeapot(size);  //線框茶壺
    //glutSolidTeapot(size);  //實心茶壺
}

void draw_tetrahedron(void)	//畫四面體
{
    float pnt[4][3] = { {0.0,0.0,0.0}, {1.0,0.0,0.0}, {0.0,1.0,0.0}, {0.0,0.0,1.0} };
    int tetra[4][3] = { {0,2,1}, {0,3,2}, {0,1,3}, {1,2,3} };

    glBegin(GL_TRIANGLES);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex3fv(pnt[tetra[0][0]]);
    glVertex3fv(pnt[tetra[0][1]]);
    glVertex3fv(pnt[tetra[0][2]]);

    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex3fv(pnt[tetra[1][0]]);
    glVertex3fv(pnt[tetra[1][1]]);
    glVertex3fv(pnt[tetra[1][2]]);

    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3fv(pnt[tetra[2][0]]);
    glVertex3fv(pnt[tetra[2][1]]);
    glVertex3fv(pnt[tetra[2][2]]);

    glColor3f(0.0f, 1.0f, 1.0f);	glVertex3fv(pnt[tetra[3][0]]); //補色
    glColor3f(1.0f, 0.0f, 1.0f);	glVertex3fv(pnt[tetra[3][1]]);
    glColor3f(1.0f, 1.0f, 0.0f);	glVertex3fv(pnt[tetra[3][2]]);
    glEnd();
}

void draw_tetrahedron2(void)
{
    float pnt[4][3] = { {0.0,0.0,0.0},{1.0,0.0,0.0}, {0.0,1.0,0.0}, {0.0,0.0,1.0} };
    int tetra[4][3] = { {0,2,1}, {0,3,2}, {0,1,3}, {1,2,3} };

    glNormal3f(0.0f, 0.0f, -1.0f);	//設置法線
    glBegin(GL_POLYGON); //X-Y
    glVertex3fv(pnt[tetra[0][0]]);
    glVertex3fv(pnt[tetra[0][1]]);
    glVertex3fv(pnt[tetra[0][2]]);
    glEnd();

    glNormal3f(-1.0f, 0.0f, 0.0f);	//設置法線
    glBegin(GL_POLYGON); //Y-Z
    glVertex3fv(pnt[tetra[1][0]]);
    glVertex3fv(pnt[tetra[1][1]]);
    glVertex3fv(pnt[tetra[1][2]]);
    glEnd();

    glNormal3f(0.0f, -1.0f, 0.0f);	//設置法線
    glBegin(GL_POLYGON); //Z-X
    glVertex3fv(pnt[tetra[2][0]]);
    glVertex3fv(pnt[tetra[2][1]]);
    glVertex3fv(pnt[tetra[2][2]]);
    glEnd();

    glNormal3f(1.0f, 1.0f, 1.0f);	//設置法線
    glBegin(GL_POLYGON); //slope
    glVertex3fv(pnt[tetra[3][0]]);
    glVertex3fv(pnt[tetra[3][1]]);
    glVertex3fv(pnt[tetra[3][2]]);
    glEnd();
}

inline void glPrint(float x, float y, const char* s, void* font)
{
    glRasterPos2f((GLfloat)x, (GLfloat)y);
    int len = (int)strlen(s);

    for (int i = 0; i < len; i++)
    {
        glutBitmapCharacter(font, s[i]);
    }
}

inline void glPrintShadowed(float x, float y, const char* s, void* font, float* color)
{
    //背景字
    glColor3f(1.0, 1.0, 1.0);   //設定顏色 White
    glPrint(x, y, s, font);

    //前景字
    glColor3fv((GLfloat*)color);    //設定顏色
    glPrint(x + 0.01, y + 0.01, s, font);
}

void draw_string1(const char* str, float* color, void* font, float x_st, float y_st)
{
    //int len = (int)strlen(str);
    //printf("取得字串 [%s], 長度 %d\n", str, len);

    glColor3fv((GLfloat*)color);    //設定顏色
    glPrint(x_st, y_st, str, font);
}

void draw_string1s(std::string str, float* color, void* font, float x_st, float y_st)
{
    glColor3fv((GLfloat*)color);    //設定顏色

    glRasterPos2f(x_st, y_st);

    for (int i = 0; i < str.size(); i++)
    {
        glutBitmapCharacter(font, str[i]);
    }
}

void draw_string2(const char* str, float* color, void* font, float x_st, float y_st)
{
    glColor3fv((GLfloat*)color);    //設定顏色
    glPrintShadowed(x_st, y_st, str, font, color);
}

//實心三角形
void draw_triangle(float* color, float width, float x1, float y1, float x2, float y2, float x3, float y3)
{
    glColor3fv((GLfloat*)color);    //設定顏色
    glLineWidth(width);	//設定線寬

    glBegin(GL_TRIANGLES);
    glVertex2f(x1, y1);
    glVertex2f(x2, y2);
    glVertex2f(x3, y3);
    glEnd();
}


//OpenGL 之基本 callback function

// 窗口大小變化回調函數
void reshape0(int w, int h)
{
    glViewport(0, 0, w, h);
}

void keyboard0(unsigned char key, int x, int y)
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

    case '1':
        printf("1\n");
        break;

    case '2':
        printf("2\n");
        break;

    case '3':
        break;

    case '4':
        break;

    case '?':
        break;
    }
}

void mouse0(int button, int state, int x, int y)
{
}

void motion0(int x, int y)
{
}
