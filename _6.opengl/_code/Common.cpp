#include <helper_gl.h>

//#include <GL/glut.h>		//32 bits
#include <GL/freeglut.h>	//64 bits

//供旋轉座標系用
int mx;	//position of mouse
int my;	//position of mouse
int m_state = 0; //mouse usage
float x_angle = 0.0f;	//angle of eye
float y_angle = 0.0f;	//angle of eye
float dist = 10.0f; //distance from the eye

//畫座標軸
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
    glRasterPos3f(len, 0.05f, 0.0f);
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
    glRasterPos3f(0.0f, len + dd / 3, 0.0f);
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
    glRasterPos3f(0.0f, 0.0f, len + dd * 2);
    glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, 'z');
}

//畫視窗邊界
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

    glLineWidth(width);         //設定線寬
    glutWireTeapot(size);       //畫茶壺, 線框
    //glutSolidTeapot(size);    //畫茶壺, 實心
}

void draw_cone(float* color, float width, GLdouble base, GLdouble height, GLint slices, GLint stacks)
{
    //畫一個圓錐體
    glColor3fv((GLfloat*)color);    //設定顏色

    glLineWidth(width);     //設定線寬

    glutWireCone(base, height, slices, stacks); //畫圓錐體, 線框
    //glutSolidCone(base, height, slices, stacks); //畫圓錐體, 實心
}

void draw_cube(float* color, float width, GLdouble size)
{
    //畫一個立方體
    glColor3fv((GLfloat*)color);    //設定顏色

    glLineWidth(width);     //設定線寬

    glutWireCube(size);     //畫立方體, 線框
    //glutSolidCube(size);   //畫立方體, 實心
}

/*
* 
glutWireCube(1.0);//绘制立方体线框图

FGAPI void    FGAPIENTRY glutWireCube(GLdouble size);
FGAPI void    FGAPIENTRY glutSolidCube(GLdouble size);
FGAPI void    FGAPIENTRY glutWireSphere(GLdouble radius, GLint slices, GLint stacks);
FGAPI void    FGAPIENTRY glutSolidSphere(GLdouble radius, GLint slices, GLint stacks);
FGAPI void    FGAPIENTRY glutWireCone(GLdouble base, GLdouble height, GLint slices, GLint stacks);
FGAPI void    FGAPIENTRY glutSolidCone(GLdouble base, GLdouble height, GLint slices, GLint stacks);
*/

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

//繪製木箱
void draw_box(float* color)
{
    glColor3fv((GLfloat*)color);    //設定顏色

    glEnable(GL_TEXTURE_2D);	//啟用2D紋理映射

/** 選擇紋理 */
//glBindTexture(GL_TEXTURE_2D, tex2D);	//綁定紋理

/** 開始繪製四邊形 */
    glBegin(GL_QUADS);

    /// 前側面
    glNormal3f(0.0f, 0.0f, 1.0f);                               /**指定法線指向觀察者 */	//設置法線
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, 1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, 1.0f, 1.0f);

    /// 後側面
    glNormal3f(0.0f, 0.0f, -1.0f);                              /** 指定法線背向觀察者 */	//設置法線
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, 1.0f, -1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, -1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(1.0f, -1.0f, -1.0f);

    /// 頂面
    glNormal3f(0.0f, 1.0f, 0.0f);                               /**指定法線向上 */	//設置法線
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, 1.0f, 1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, 1.0f, 1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, -1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, 1.0f, -1.0f);

    /// 底面
    glNormal3f(0.0f, -1.0f, 0.0f);                              /** 指定法線朝下 */	//設置法線
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, -1.0f, 1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, -1.0f, -1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, -1.0f, -1.0f);

    /// 右側面
    glNormal3f(1.0f, 0.0f, 0.0f);                               /**指定法線朝右 */	//設置法線
    glTexCoord2f(0.0f, 0.0f); glVertex3f(1.0f, -1.0f, -1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(1.0f, 1.0f, -1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(1.0f, 1.0f, 1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(1.0f, -1.0f, 1.0f);

    /// 左側面
    glNormal3f(-1.0f, 0.0f, 0.0f);                              /**指定法線朝左 */	//設置法線
    glTexCoord2f(0.0f, 0.0f); glVertex3f(-1.0f, -1.0f, -1.0f);
    glTexCoord2f(1.0f, 0.0f); glVertex3f(-1.0f, 1.0f, -1.0f);
    glTexCoord2f(1.0f, 1.0f); glVertex3f(-1.0f, 1.0f, 1.0f);
    glTexCoord2f(0.0f, 1.0f); glVertex3f(-1.0f, -1.0f, 1.0f);

    glEnd();
    glDisable(GL_TEXTURE_2D);
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
    glPrint(x + 0.01f, y + 0.01f, s, font);
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

//空心三角形
void draw_triangle(float* color, float width, float x1, float y1, float x2, float y2, float x3, float y3)
{
    //TBD
    return;

    glColor3fv((GLfloat*)color);    //設定顏色
    glLineWidth(width);	//設定線寬

    //畫實心三角形, 三個頂點為一組
    glBegin(GL_TRIANGLES);
    glVertex2f(x1, y1);
    glVertex2f(x2, y2);
    glVertex2f(x3, y3);
    glEnd();
}

//實心三角形
void draw_triangle_s(float* color, float x1, float y1, float x2, float y2, float x3, float y3)
{
    glColor3fv((GLfloat*)color);    //設定顏色

    //畫實心三角形, 三個頂點為一組
    glBegin(GL_TRIANGLES);
    glVertex2f(x1, y1);
    glVertex2f(x2, y2);
    glVertex2f(x3, y3);
    glEnd();
}

void draw_point(float* color, float size, float x_st, float y_st)
{
    //畫點
    glColor3fv((GLfloat*)color);    //設定顏色
    glPointSize(size);	            //設定點的大小, N X N
    glBegin(GL_POINTS);
    glVertex2f(x_st, y_st);
    glEnd();
}

//空心矩形, 左下為原點, 向右w, 向上h, 顏色color, 線寬width
void draw_rectangle(float* color, float width, float x_st, float y_st, float w, float h)
{
    //TBD
    /*
    //用 GL_LINE_LOOP 畫一個空心矩形
//glColor3f(0.0, 1.0, 0.0);
    glColor3fv((GLfloat*)color);

    //方法一, 使用 GL_QUADS
    glBegin(GL_QUADS);	//畫矩形
    //逆時針為空心
    //畫一個白色外框
    glVertex3f(-dd, dd, 0.0f);	//左上
    glVertex3f(-dd, -dd, 0.0f);	//左下
    glVertex3f(dd, -dd, 0.0f);	//右下
    glVertex3f(dd, dd, 0.0f);	//右上
    glEnd();
    */




}

//實心矩形, 左下為原點, 向右w, 向上h, 顏色color, 無線寬width
void draw_rectangle_s(float* color, float x_st, float y_st, float w, float h)
{
    glColor3fv((GLfloat*)color);    //設定顏色

    glEnable(GL_TEXTURE_2D);    //啟用2D紋理映射

    float dd = 0.5f;
    //GL_QUADS 使用
    glBegin(GL_QUADS);  //畫實心四邊形
    {
        glTexCoord2f(x_st, y_st); //紋理座標配置
        glVertex2f(x_st, y_st);     //左下座標
        glTexCoord2f(x_st + w, y_st);
        glVertex2f(x_st + w, y_st);       //右下座標
        glTexCoord2f(x_st + w, y_st + h);
        glVertex2f(x_st + w, y_st + h);         //右上座標
        glTexCoord2f(x_st, y_st + h);
        glVertex2f(x_st, y_st + h);       //左上座標
    }
    glEnd();

    glDisable(GL_TEXTURE_2D);
}

//實心矩形, 左下為原點, 向右w, 向上h, 顏色color, 無線寬width
void draw_rectangle_si(GLint index, float x_st, float y_st, float w, float h)
{
    glIndexi(index);            //設定顏色
    //glColor3fv((GLfloat*)color);    //設定顏色

    glEnable(GL_TEXTURE_2D);    //啟用2D紋理映射

    float dd = 0.5f;
    //GL_QUADS 使用
    glBegin(GL_QUADS);  //畫實心四邊形
    {
        glTexCoord2f(x_st, y_st); //紋理座標配置
        glVertex2f(x_st, y_st);     //左下座標
        glTexCoord2f(x_st + w, y_st);
        glVertex2f(x_st + w, y_st);       //右下座標
        glTexCoord2f(x_st + w, y_st + h);
        glVertex2f(x_st + w, y_st + h);         //右上座標
        glTexCoord2f(x_st, y_st + h);
        glVertex2f(x_st, y_st + h);       //左上座標
    }
    glEnd();

    glDisable(GL_TEXTURE_2D);
}

//空心四邊形, 左下為原點, 向右w, 向上h, 顏色color, 線寬width
void draw_quad(float* color, float width, float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4)
{


}

//實心四邊形, 左下為原點, 向右w, 向上h, 顏色color, 無線寬width
void draw_quad_s(float* color, float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4)
{
    glColor3fv((GLfloat*)color);    //設定顏色

    glEnable(GL_TEXTURE_2D);    //啟用2D紋理映射

    //GL_QUADS 使用
    glBegin(GL_QUADS);  //畫實心四邊形
    {
        glTexCoord2f(x1, y1); //紋理座標配置
        glVertex2f(x1, y1);     //第1點
        glTexCoord2f(x2, y2);
        glVertex2f(x2, y2);     //第2點
        glTexCoord2f(x3, y3);
        glVertex2f(x3, y3);//第3點
        glTexCoord2f(x4, y4);
        glVertex2f(x4, y4);//第4點
    }
    glEnd();

    glDisable(GL_TEXTURE_2D);
}

//OpenGL 之基本 callback function

// 窗口大小變化回調函數
void reshape0(int w, int h)
{
    glViewport(0, 0, w, h);
}

void keyboard0(unsigned char key, int /*x*/, int /*y*/)
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

//供旋轉座標系用
void keyboard_r(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
    case '0':
        m_state = 0;
        break;
    case '1':
        m_state = 1;
        break;
    }
}

void mouse_r(int button, int state, int x, int y)
{
    //MouseDown
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        mx = x;
        my = y;
        printf("D(%d, %d) ", mx, my);
    }
}

void motion_r(int x, int y)
{
    //MouseMove
    int dx, dy; //offset of mouse;

    dx = x - mx;
    dy = y - my;

    if (m_state == 0)
    {
        y_angle += dx * 0.1f;
        x_angle += dy * 0.1f;
    }
    else if (m_state == 1)
    {
        dist += (dx + dy) * 0.01f;
    }

    mx = x;
    my = y;

    //printf("M(%d, %d) ", mx, my);
    glutPostRedisplay();
}

void setup_rotation()
{
    //double x, y, z, eyex, eyey, eyez;
    int rect[4];
    float w, h;

    glGetIntegerv(GL_VIEWPORT, rect);
    w = (float)rect[2];
    h = (float)rect[3];

    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣

    if (w > h)
    {
        glOrtho(-w / h, w / h, -1.0f, 1.0f, -1.0f, 1.0f);
    }
    else
    {
        glOrtho(-1.0f, 1.0f, -h / w, h / w, -1.0f, 1.0f);
    }

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣

    glRotatef(x_angle, 1.0f, 0.0f, 0.0f);
    glRotatef(y_angle, 0.0f, 1.0f, 0.0f);

    //顯示資訊
    char info[20];
    sprintf_s(info, sizeof(info), "(%3.1f,   %3.1f)", x_angle, y_angle);
    glutSetWindowTitle(info);
}
