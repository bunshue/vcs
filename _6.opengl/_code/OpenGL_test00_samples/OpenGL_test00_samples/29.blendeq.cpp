/*
** blendeq.c - Demonstrates the use of the blend_minmax, blend_subtract,
**    and blend_logic_op extensions using glBlendEquationEXT.
**
**    Over a two-color backround, draw rectangles using twelve blend
**    options. The values are read back as UNSIGNED_BYTE and printed
**    in hex over each value. These values are useful for logic
**    op comparisons when channels are 8 bits deep.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include "font.h"

#if defined(GL_EXT_blend_color) && \
    defined(GL_EXT_blend_minmax) && \
    defined(GL_EXT_blend_logic_op) && \
    defined(GL_EXT_blend_subtract)

GLenum doubleBuffer;
GLint windW = 800, windH = 800;
int dithering = 0;
int doPrint = 1;
int deltaY;
GLuint bitmapBase;

void Init(void)
{
    bitmapBase = glGenLists(256);
    fontCreateBitmap(bitmapBase);

    glDisable(GL_DITHER);
    glShadeModel(GL_FLAT);
}

void Reshape(int width, int height)
{
    windW = width;
    windH = height;

    glViewport(0, 0, windW, windH);
    deltaY = windH / 16;

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, windW, 0, windH);	//窗口座標範圍, 2D
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 'd':
        dithering = !dithering;
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
    }
}

void PrintColorStrings()
{
    GLubyte ubbuf[3], ubcolor[3];
    int i, xleft, xright;
    char colorString[18];

    xleft = 5 + windW / 4;
    xright = 5 + windW / 2;

    for (i = windH - deltaY + 4; i > 0; i -= deltaY)
    {
        glReadPixels(xleft, i + 10, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, ubbuf);
        sprintf(colorString, "(0x%x, 0x%x, 0x%x)", ubbuf[0], ubbuf[1], ubbuf[2]);
        glRasterPos2f(xleft, i);
        fontDrawStr(bitmapBase, colorString);
        glReadPixels(xright, i + 10, 1, 1, GL_RGB, GL_UNSIGNED_BYTE, ubbuf);
        sprintf(colorString, "(0x%x, 0x%x, 0x%x)", ubbuf[0], ubbuf[1], ubbuf[2]);
        glRasterPos2f(xright, i);
        fontDrawStr(bitmapBase, colorString);
    }
    /* sprintf usage
    char info[10];
    //sprintf(info, "%d", (char)display_mode);  //過時, x64不能用
    sprintf_s(info, sizeof(info), "%d", display_mode);
    glutSetWindowTitle(info);
    */
}

void Draw(void)
{
    float xscale, yscale;
    GLfloat x, y;
    int i, j;
    GLfloat buf[3];
    GLubyte ubbuf[3], ubcolor[3];
    int stringOffset = 5, stringx = 8;
    int x1, x2, xleft, xright;

    (dithering) ? glEnable(GL_DITHER) : glDisable(GL_DITHER);
    glDisable(GL_BLEND);

    glClearColor(0.5, 0.6, 0.1, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);

    /* Draw background */
    glColor3f(0.1, 0.1, 1.0);
    glRectf(0.0, 0.0, windW / 2, windH);

    /* Draw labels */
    glColor3f(0.8, 0.8, 0.0);
    i = windH - deltaY + stringOffset;
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "SOURCE");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "DEST");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "min");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "max");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "subtract");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "reverse_subtract");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "clear");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "set");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "copy");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "noop");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "and");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "invert");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "or");
    glRasterPos2f(stringx, i); i -= deltaY;
    fontDrawStr(bitmapBase, "xor");

    i = windH - deltaY;
    x1 = windW / 4;
    x2 = 3 * windW / 4;
    xleft = 5 + windW / 4;
    xright = 5 + windW / 2;

    /* Draw foreground color for comparison */
    glColor3f(0.9, 0.2, 0.8);
    glRectf(x1, i, x2, i + deltaY);

    /* Leave one rectangle of background color */

    /* Begin test cases */
    glEnable(GL_BLEND);
    glBlendFunc(GL_ONE, GL_ONE);

    i -= 2 * deltaY;
    glBlendEquationEXT(GL_MIN_EXT);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_MAX_EXT);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_FUNC_SUBTRACT_EXT);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_FUNC_REVERSE_SUBTRACT_EXT);
    glRectf(x1, i, x2, i + deltaY);

    glBlendFunc(GL_ONE, GL_ZERO);
    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_CLEAR);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_SET);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_COPY);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_NOOP);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_AND);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_INVERT);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_OR);
    glRectf(x1, i, x2, i + deltaY);

    i -= deltaY;
    glBlendEquationEXT(GL_LOGIC_OP);
    glLogicOp(GL_XOR);
    glRectf(x1, i, x2, i + deltaY);
    glRectf(x1, i + 10, x2, i + 5);

    if (doPrint)
    {
        glDisable(GL_BLEND);
        glColor3f(1.0, 1.0, 1.0);
        PrintColorStrings();
    }

    if (doubleBuffer)
    {
        glutSwapBuffers();
    }
    else
    {
        glFlush();
    }
}

void Args(int argc, char** argv)
{
    GLint i;

    doubleBuffer = GL_FALSE;

    for (i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-sb") == 0)
        {
            doubleBuffer = GL_FALSE;
        }
        else if (strcmp(argv[i], "-db") == 0)
        {
            doubleBuffer = GL_TRUE;
        }
    }
}

GLboolean QueryExtension(char* extName)
{
    /*
    ** Search for extName in the extensions string. Use of strstr()
    ** is not sufficient because extension names can be prefixes of
    ** other extension names. Could use strtok() but the constant
    ** string returned by glGetString can be in read-only memory.
    */
    char* p = (char*)glGetString(GL_EXTENSIONS);
    char* end = p + strlen(p);
    while (p < end)
    {
        int n = strcspn(p, " ");
        if ((strlen(extName) == n) && (strncmp(extName, p, n) == 0))
        {
            return GL_TRUE;
        }
        p += (n + 1);
    }
    return GL_FALSE;
}

int main(int argc, char** argv)
{
    GLenum type;

    glutInit(&argc, argv);
    Args(argc, argv);

    type = GLUT_RGB;
    type |= (doubleBuffer) ? GLUT_DOUBLE : GLUT_SINGLE;
    glutInitDisplayMode(type);
    glutInitWindowSize(windW, windH);
    glutCreateWindow("Blend Equation");	//開啟視窗 並顯示出視窗 Title

    if (!QueryExtension("GL_EXT_blend_logic_op"))
    {
        printf("Blend_logic_op extension is not present.\n");
        exit(0);
    }

    if (!QueryExtension("GL_EXT_blend_minmax"))
    {
        printf("Blend_minmax extension is not present.\n");
        exit(0);
    }

    if (!QueryExtension("GL_EXT_blend_subtract"))
    {
        printf("Blend_subtract extension is not present.\n");
        exit(0);
    }

    Init();

    glutReshapeFunc(Reshape);
    glutKeyboardFunc(keyboard);
    glutDisplayFunc(Draw);
    glutMainLoop();	//開始主循環繪製

    return 0;
}

#else

int main(int argc, char** argv)
{
    printf("GL_EXT_blend_logic_op extension is not present.\n");
    printf("GL_EXT_blend_minmax extension is not present.\n");
    printf("GL_EXT_blend_subtract extension is not present.\n");
}

#endif
