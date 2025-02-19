#include "../../Common.h"

#define PIXEL_CENTER(x) ((long)(x) + 0.5)

#define GAP 10
#define ROWS 3
#define COLS 4

#define OPENGL_WIDTH 48
#define OPENGL_HEIGHT 13

GLenum rgb;
GLint windW = 800;
GLint windH = 600;

GLenum mode1;
GLenum mode2;
GLint boxW;
GLint boxH;

GLubyte OpenGL_bits[] = {
   0x00, 0x03, 0x00, 0x00, 0x00, 0x00,
   0x7f, 0xfb, 0xff, 0xff, 0xff, 0x01,
   0x7f, 0xfb, 0xff, 0xff, 0xff, 0x01,
   0x00, 0x03, 0x00, 0x00, 0x00, 0x00,
   0x3e, 0x8f, 0xb7, 0xf9, 0xfc, 0x01,
   0x63, 0xdb, 0xb0, 0x8d, 0x0d, 0x00,
   0x63, 0xdb, 0xb7, 0x8d, 0x0d, 0x00,
   0x63, 0xdb, 0xb6, 0x8d, 0x0d, 0x00,
   0x63, 0x8f, 0xf3, 0xcc, 0x0d, 0x00,
   0x63, 0x00, 0x00, 0x0c, 0x4c, 0x0a,
   0x63, 0x00, 0x00, 0x0c, 0x4c, 0x0e,
   0x63, 0x00, 0x00, 0x8c, 0xed, 0x0e,
   0x3e, 0x00, 0x00, 0xf8, 0x0c, 0x00,
};

void Init(void)
{
    mode1 = GL_TRUE;
    mode2 = GL_TRUE;
}

void RotateColorMask(void)
{
    static GLint rotation = 0;

    rotation = (rotation + 1) & 0x3;
    switch (rotation)
    {
    case 0:
        glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE);
        glIndexMask(0xff);
        break;
    case 1:
        glColorMask(GL_FALSE, GL_TRUE, GL_TRUE, GL_TRUE);
        glIndexMask(0xFE);
        break;
    case 2:
        glColorMask(GL_TRUE, GL_FALSE, GL_TRUE, GL_TRUE);
        glIndexMask(0xFD);
        break;
    case 3:
        glColorMask(GL_TRUE, GL_TRUE, GL_FALSE, GL_TRUE);
        glIndexMask(0xFB);
        break;
    }
}

static void SetColor(int index)
{
    if (rgb)
    {
        switch (index)
        {
        case 0:
            glColor3f(0.0, 0.0, 0.0);
            break;
        case 1:
            glColor3f(1.0, 0.0, 0.0);
            break;
        case 2:
            glColor3f(0.0, 1.0, 0.0);
            break;
        case 3:
            glColor3f(1.0, 1.0, 0.0);
            break;
        case 4:
            glColor3f(0.0, 0.0, 1.0);
            break;
        case 5:
            glColor3f(1.0, 0.0, 1.0);
            break;
        case 6:
            glColor3f(0.0, 1.0, 1.0);
            break;
        case 7:
            glColor3f(1.0, 1.0, 1.0);
            break;
        }
    }
    else
    {
        glIndexi(index);
    }
}

void Viewport(GLint row, GLint column)
{
    GLint x, y;

    boxW = (windW - (COLS + 1) * GAP) / COLS;
    boxH = (windH - (ROWS + 1) * GAP) / ROWS;

    printf("Viewport, Row = %d, Column = %d\n", row, column);
    printf("windW = %d, windH = %d\t", windW, windH);
    printf("COLS = %d, ROWS = %d, GAP = %d\n", COLS, ROWS, GAP);
    printf("boxW = %d, boxH = %d\t", boxW, boxH);

    x = GAP + column * (boxW + GAP);
    y = GAP + row * (boxH + GAP);

    printf("x = %d, y = %d\n", x, y);

    glViewport(x, y, boxW, boxH);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-boxW / 2, boxW / 2, -boxH / 2, boxH / 2, 0.0, 1.0);
    glMatrixMode(GL_MODELVIEW);

    glEnable(GL_SCISSOR_TEST);
    glScissor(x, y, boxW, boxH);
}

static void draw_point(void)
{
    GLint i;

    //畫點
    glPointSize(5.0f);	//設定點的大小, N X N
    glBegin(GL_POINTS);
    for (i = 1; i < 8; i++)
    {
        GLint j = i * 10;
        SetColor(i);

        glVertex2i(-j, -j);
        glVertex2i(-j, 0);
        glVertex2i(-j, j);
        glVertex2i(0, j);
        glVertex2i(j, j);
        glVertex2i(j, 0);
        glVertex2i(j, -j);
        glVertex2i(0, -j);
    }
    glEnd();
}

static void Lines(void)
{
    GLint i;

    glPushMatrix();

    glTranslatef(-12, 0, 0);
    for (i = 1; i < 8; i++)
    {
        SetColor(i);
        glBegin(GL_LINES);
        glVertex2i(-boxW / 4, -boxH / 4);
        glVertex2i(boxW / 4, boxH / 4);
        glEnd();
        glTranslatef(4, 0, 0);
    }

    glPopMatrix();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_LINES);
    glVertex2i(0, 0);
    glEnd();
}

static void LineStrip(void)
{
    glBegin(GL_LINE_STRIP);
    SetColor(1);
    glVertex2f(PIXEL_CENTER(-boxW / 4), PIXEL_CENTER(-boxH / 4));
    SetColor(2);
    glVertex2f(PIXEL_CENTER(-boxW / 4), PIXEL_CENTER(boxH / 4));
    SetColor(3);
    glVertex2f(PIXEL_CENTER(boxW / 4), PIXEL_CENTER(boxH / 4));
    SetColor(4);
    glVertex2f(PIXEL_CENTER(boxW / 4), PIXEL_CENTER(-boxH / 4));
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_LINE_STRIP);
    glVertex2i(0, 0);
    glEnd();
}

static void LineLoop(void)
{
    glBegin(GL_LINE_LOOP);
    SetColor(1);
    glVertex2f(PIXEL_CENTER(-boxW / 4), PIXEL_CENTER(-boxH / 4));
    SetColor(2);
    glVertex2f(PIXEL_CENTER(-boxW / 4), PIXEL_CENTER(boxH / 4));
    SetColor(3);
    glVertex2f(PIXEL_CENTER(boxW / 4), PIXEL_CENTER(boxH / 4));
    SetColor(4);
    glVertex2f(PIXEL_CENTER(boxW / 4), PIXEL_CENTER(-boxH / 4));
    glEnd();

    glEnable(GL_LOGIC_OP);
    glLogicOp(GL_XOR);

    glEnable(GL_BLEND);
    glBlendFunc(GL_ONE, GL_ONE);

    SetColor(5);
    glBegin(GL_LINE_LOOP);
    glVertex2f(PIXEL_CENTER(-boxW / 8), PIXEL_CENTER(-boxH / 8));
    glVertex2f(PIXEL_CENTER(-boxW / 8), PIXEL_CENTER(boxH / 8));
    glEnd();
    glBegin(GL_LINE_LOOP);
    glVertex2f(PIXEL_CENTER(-boxW / 8), PIXEL_CENTER(boxH / 8 + 5));
    glVertex2f(PIXEL_CENTER(boxW / 8), PIXEL_CENTER(boxH / 8 + 5));
    glEnd();
    glDisable(GL_LOGIC_OP);
    glDisable(GL_BLEND);

    SetColor(6);
    glBegin(GL_POINTS);
    glVertex2i(0, 0);
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_LINE_LOOP);
    glVertex2i(0, 0);
    glEnd();
}

static void Bitmap(void)
{
    glBegin(GL_LINES);
    SetColor(1);
    glVertex2i(-boxW / 2, 0);
    glVertex2i(boxW / 2, 0);
    glVertex2i(0, -boxH / 2);
    glVertex2i(0, boxH / 2);
    SetColor(2);
    glVertex2i(0, -3);
    glVertex2i(0, -3 + OPENGL_HEIGHT);
    SetColor(3);
    glVertex2i(0, -3);
    glVertex2i(OPENGL_WIDTH, -3);
    glEnd();

    SetColor(4);

    glPixelStorei(GL_UNPACK_LSB_FIRST, GL_TRUE);
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);

    glRasterPos2i(0, 0);
    glBitmap(OPENGL_WIDTH, OPENGL_HEIGHT, 0, 3, 0.0, 0.0, OpenGL_bits);
}

static void Triangles(void)
{
    glBegin(GL_TRIANGLES);
    SetColor(1);
    glVertex2i(-boxW / 4, -boxH / 4);
    SetColor(2);
    glVertex2i(-boxW / 8, -boxH / 16);
    SetColor(3);
    glVertex2i(boxW / 8, -boxH / 16);

    SetColor(4);
    glVertex2i(-boxW / 4, boxH / 4);
    SetColor(5);
    glVertex2i(-boxW / 8, boxH / 16);
    SetColor(6);
    glVertex2i(boxW / 8, boxH / 16);
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_TRIANGLES);
    glVertex2i(0, 0);
    glVertex2i(-100, 100);
    glEnd();
}

static void TriangleStrip(void)
{
    glBegin(GL_TRIANGLE_STRIP);
    SetColor(1);
    glVertex2i(-boxW / 4, -boxH / 4);
    SetColor(2);
    glVertex2i(-boxW / 4, boxH / 4);
    SetColor(3);
    glVertex2i(0, -boxH / 4);
    SetColor(4);
    glVertex2i(0, boxH / 4);
    SetColor(5);
    glVertex2i(boxW / 4, -boxH / 4);
    SetColor(6);
    glVertex2i(boxW / 4, boxH / 4);
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_TRIANGLE_STRIP);
    glVertex2i(0, 0);
    glVertex2i(-100, 100);
    glEnd();
}

static void TriangleFan(void)
{
    GLint vx[8][2];
    GLint x0, y0, x1, y1, x2, y2, x3, y3;
    GLint i;

    y0 = -boxH / 4;
    y1 = y0 + boxH / 2 / 3;
    y2 = y1 + boxH / 2 / 3;
    y3 = boxH / 4;
    x0 = -boxW / 4;
    x1 = x0 + boxW / 2 / 3;
    x2 = x1 + boxW / 2 / 3;
    x3 = boxW / 4;

    vx[0][0] = x0; vx[0][1] = y1;
    vx[1][0] = x0; vx[1][1] = y2;
    vx[2][0] = x1; vx[2][1] = y3;
    vx[3][0] = x2; vx[3][1] = y3;
    vx[4][0] = x3; vx[4][1] = y2;
    vx[5][0] = x3; vx[5][1] = y1;
    vx[6][0] = x2; vx[6][1] = y0;
    vx[7][0] = x1; vx[7][1] = y0;

    glBegin(GL_TRIANGLE_FAN);
    SetColor(7);
    glVertex2i(0, 0);
    for (i = 0; i < 8; i++)
    {
        SetColor(7 - i);
        glVertex2iv(vx[i]);
    }
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_TRIANGLE_FAN);
    glVertex2i(0, 0);
    glVertex2i(-100, 100);
    glEnd();
}

static void Rect(void)
{
    printf("boxW = %d, boxH = %d\n", boxW, boxH);
    (rgb) ? glColor3f(1.0, 0.0, 1.0) : glIndexi(5);
    glRecti(-boxW / 4, -boxH / 4, boxW / 4, boxH / 4);
}

static void Polygons(void)
{
    GLint vx[8][2];
    GLint x0, y0, x1, y1, x2, y2, x3, y3;
    GLint i;

    y0 = -boxH / 4;
    y1 = y0 + boxH / 2 / 3;
    y2 = y1 + boxH / 2 / 3;
    y3 = boxH / 4;
    x0 = -boxW / 4;
    x1 = x0 + boxW / 2 / 3;
    x2 = x1 + boxW / 2 / 3;
    x3 = boxW / 4;

    vx[0][0] = x0; vx[0][1] = y1;
    vx[1][0] = x0; vx[1][1] = y2;
    vx[2][0] = x1; vx[2][1] = y3;
    vx[3][0] = x2; vx[3][1] = y3;
    vx[4][0] = x3; vx[4][1] = y2;
    vx[5][0] = x3; vx[5][1] = y1;
    vx[6][0] = x2; vx[6][1] = y0;
    vx[7][0] = x1; vx[7][1] = y0;

    glBegin(GL_POLYGON);
    for (i = 0; i < 8; i++)
    {
        SetColor(7 - i);
        glVertex2iv(vx[i]);
    }
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_POLYGON);
    glVertex2i(0, 0);
    glVertex2i(100, 100);
    glEnd();
}

static void Quads(void)
{
    glBegin(GL_QUADS);
    SetColor(1);
    glVertex2i(-boxW / 4, -boxH / 4);
    SetColor(2);
    glVertex2i(-boxW / 8, -boxH / 16);
    SetColor(3);
    glVertex2i(boxW / 8, -boxH / 16);
    SetColor(4);
    glVertex2i(boxW / 4, -boxH / 4);

    SetColor(5);
    glVertex2i(-boxW / 4, boxH / 4);
    SetColor(6);
    glVertex2i(-boxW / 8, boxH / 16);
    SetColor(7);
    glVertex2i(boxW / 8, boxH / 16);
    SetColor(0);
    glVertex2i(boxW / 4, boxH / 4);
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_QUADS);
    glVertex2i(0, 0);
    glVertex2i(100, 100);
    glVertex2i(-100, 100);
    glEnd();
}

static void QuadStrip(void)
{
    glBegin(GL_QUAD_STRIP);
    SetColor(1);
    glVertex2i(-boxW / 4, -boxH / 4);
    SetColor(2);
    glVertex2i(-boxW / 4, boxH / 4);
    SetColor(3);
    glVertex2i(0, -boxH / 4);
    SetColor(4);
    glVertex2i(0, boxH / 4);
    SetColor(5);
    glVertex2i(boxW / 4, -boxH / 4);
    SetColor(6);
    glVertex2i(boxW / 4, boxH / 4);
    glEnd();

    (rgb) ? glColor3f(1.0, 1.0, 1.0) : glIndexi(7);
    glBegin(GL_QUAD_STRIP);
    glVertex2i(0, 0);
    glVertex2i(100, 100);
    glVertex2i(-100, 100);
    glEnd();
}

void display(void)
{
    glViewport(0, 0, windW, windH);
    glDisable(GL_SCISSOR_TEST);

    glPushAttrib(GL_COLOR_BUFFER_BIT);

    glColorMask(1, 1, 1, 1);
    glIndexMask(~0);

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);

    glPopAttrib();

    if (mode1)
    {
        glShadeModel(GL_SMOOTH);
    }
    else
    {
        glShadeModel(GL_FLAT);
    }

    if (mode2)
    {
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    }
    else
    {
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    }

    printf("畫第(0, 0)個, Point\n");
    Viewport(0, 0); draw_point();
    printf("畫第(0, 1)個, Lines\n");
    Viewport(0, 1); Lines();
    printf("畫第(0, 2)個, LineStrip\n");
    Viewport(0, 2); LineStrip();
    printf("畫第(0, 3)個, LineLoop\n");
    Viewport(0, 3); LineLoop();

    printf("畫第(1, 0)個, Bitmap\n");
    Viewport(1, 0); Bitmap();
    printf("畫第(1, 1)個, TriangleFan\n");
    Viewport(1, 1); TriangleFan();
    printf("畫第(1, 2)個, Triangles\n");
    Viewport(1, 2); Triangles();
    printf("畫第(1, 3)個, TriangleStrip\n");
    Viewport(1, 3); TriangleStrip();

    printf("畫第(2, 0)個, Rect\n");
    Viewport(2, 0); Rect();
    printf("畫第(2, 1)個, Polygons\n");
    Viewport(2, 1); Polygons();
    printf("畫第(2, 2)個, Quads\n");
    Viewport(2, 2); Quads();
    printf("畫第(2, 3)個, QuadStrip\n");
    Viewport(2, 3); QuadStrip();

    glFlush();
}

void reshape(int width, int height)
{
    windW = width;
    windH = height;
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case '1':
        mode1 = !mode1;
        glutPostRedisplay();
        break;
    case '2':
        mode2 = !mode2;
        glutPostRedisplay();
        break;
    case '3':
        RotateColorMask();
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
    }
}

void Args(int argc, char** argv)
{
    GLint i;

    rgb = GL_TRUE;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-ci") == 0)
        {
            rgb = GL_FALSE;
        }
        else if (strcmp(argv[i], "-rgb") == 0)
        {
            rgb = GL_TRUE;
        }
    }
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);
    Args(argc, argv);

    type = (rgb) ? GLUT_RGB : GLUT_INDEX;
    type |= GLUT_SINGLE;
    glutInitDisplayMode(type);

    glutInitWindowSize(windW, windH);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Primitive Test"); //開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    printf("按 1 2 3 控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}
