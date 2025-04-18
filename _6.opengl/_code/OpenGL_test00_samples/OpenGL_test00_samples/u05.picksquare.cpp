/*
 *  picksquare.cpp
 *  Use of multiple names and picking are demonstrated.
 *  A 3x3 grid of squares is drawn.  When the left mouse
 *  button is pressed, all squares under the cursor position have their color changed.
 */

#include "../../Common.h"

#define BUFSIZE 512

int board[3][3];	/*  amount of color for each square	*/

/*	Clear color value for every square on the board	    */
void myinit(void)
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            board[i][j] = 0;
        }
    }
    glClearColor(0.0, 0.0, 0.0, 0.0);
}

/*  The nine squares are drawn.  In selection mode, each
 *  square is given two names:  one for the row and the
 *  other for the column on the grid.  The color of each
 *  square is determined by its position on the grid, and
 *  the value in the board[][] array.
 */
void drawSquares(GLenum mode)
{
    //printf("drawSquares\t");
    GLuint i, j;

    for (i = 0; i < 3; i++)
    {
        if (mode == GL_SELECT)
        {
            glLoadName(i);
        }
        for (j = 0; j < 3; j++)
        {
            if (mode == GL_SELECT)
            {
                glPushName(j);
            }
            glColor3f((GLfloat)i / 3.0f, (GLfloat)j / 3.0f, (GLfloat)board[i][j] / 3.0f);
            glRecti(i, j, i + 1, j + 1);
            if (mode == GL_SELECT)
            {
                glPopName();
            }
        }
    }
}

// processHits() prints out the contents of the selection array.
void processHits(GLint hits, GLuint buffer[])
{
    GLint i;
    GLuint ii = 0;
    GLuint jj = 0;
    GLuint j = 0;
    GLuint names = 0;
    GLuint* ptr;

    ptr = (GLuint*)buffer;
    for (i = 0; i < hits; i++)
    {	/*  for each hit  */
        names = *ptr;
        cout << "number of names for this hit = " << names << "\t";
        ptr++;
        //cout << "  z1 is " << *ptr << "\t";
        ptr++;
        //cout << "; z2 is " << *ptr << "\t";
        ptr++;
        cout << "names are ";
        for (j = 0; j < names; j++)
        {	/*  for each name */
            cout << *ptr << ' ';
            if (j == 0)	/*  set row and column  */
            {
                ii = *ptr;
            }
            else if (j == 1)
            {
                jj = *ptr;
            }
            ptr++;
        }
        cout << "\n";
        board[ii][jj] = (board[ii][jj] + 1) % 3;
    }
    //printf("\n");
}

/*  mouse() sets up selection mode, name stack,
 *  and projection matrix for picking.  Then the objects are drawn. */
void mouse(int button, int state, int x, int y)
{
    GLuint selectBuf[BUFSIZE];
    GLint hits;
    GLint viewport[4];

    if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN))
    {
        glGetIntegerv(GL_VIEWPORT, viewport);
        glSelectBuffer(BUFSIZE, selectBuf);
        glRenderMode(GL_SELECT);
        glInitNames();
        glPushName(-1);
        glMatrixMode(GL_PROJECTION);
        glPushMatrix();
        glLoadIdentity();
        /*  create 5x5 pixel picking region near cursor location	*/
        gluPickMatrix((GLdouble)x, (GLdouble)(viewport[3] - y), 5.0, 5.0, viewport);
        gluOrtho2D(0.0, 3.0, 0.0, 3.0);
        drawSquares(GL_SELECT);
        glMatrixMode(GL_PROJECTION);
        glPopMatrix();
        hits = glRenderMode(GL_RENDER);
        printf("hits = %d\t", hits);
        processHits(hits, selectBuf);
        glutPostRedisplay();
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);   //清除背景
    drawSquares(GL_RENDER);
    glFlush();  // 執行繪圖命令
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);    //切換到投影矩陣
    glLoadIdentity();
    gluOrtho2D(-0.5, 3.5, -0.5, 3.5);
}

int main(int argc, char** argv)
{
    const char* windowName = "點選方塊";
    const char* message = "按滑鼠點選方塊, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    myinit();

    glutMouseFunc(mouse);		//設定callback function

    glutMainLoop();	//開始主循環繪製

    return 0;
}

