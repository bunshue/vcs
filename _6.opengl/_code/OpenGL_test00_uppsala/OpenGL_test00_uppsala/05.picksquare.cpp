/*
 *  picksquare.cpp
 *  Use of multiple names and picking are demonstrated.
 *  A 3x3 grid of squares is drawn.  When the left mouse
 *  button is pressed, all squares under the cursor position
 *  have their color changed.
 *
 *  This is Listing 12-3 on pages 366-368 of the "OpenGL Programming
 *  Guide". It has been modified (by Cary Laxer on September 23, 1997)
 *  to use the glut interface rather than the aux interface, to improve
 *  readability, and to improve visibility. It has been further modified
 *  (by Cary Laxer on September 12, 2000) to change the I/O from C-style to C++.
 */

#include "../../Common.h"

#define BUFSIZE 512

void myinit(void);
void drawSquares(GLenum mode);
void processHits(GLint hits, GLuint buffer[]);
void pickSquares(int button, int state, int x, int y);
void display(void);
void reshape(int w, int h);

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
    GLuint i, j;

    for (i = 0; i < 3; i++)
    {
        if (mode == GL_SELECT) glLoadName(i);
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

/*  processHits() prints out the contents of the
 *  selection array. */
void processHits(GLint hits, GLuint buffer[])
{
    GLint i;
    GLuint ii = 0;
    GLuint jj = 0;
    GLuint j = 0;
    GLuint names = 0;
    GLuint* ptr;

    cout << "hits = " << hits << endl;
    ptr = (GLuint*)buffer;
    for (i = 0; i < hits; i++)
    {	/*  for each hit  */
        names = *ptr;
        cout << " number of names for this hit = " << names << endl;
        ptr++;
        cout << "  z1 is " << *ptr;
        ptr++;
        cout << "; z2 is " << *ptr << endl;
        ptr++;
        cout << "   names are ";
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
        cout << endl;
        board[ii][jj] = (board[ii][jj] + 1) % 3;
    }
}

/*  pickSquares() sets up selection mode, name stack,
 *  and projection matrix for picking.  Then the
 *  objects are drawn.
 */
void pickSquares(int button, int state, int x, int y)
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
        processHits(hits, selectBuf);
        glutPostRedisplay();
    }
}

void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    drawSquares(GL_RENDER);
    glutSwapBuffers();
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 3.0, 0.0, 3.0);
}

/*  Main Loop
 *  Open window with initial window size, title bar,
 *  RGBA display mode, and handle input events.
 */

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(300, 300);
    glutCreateWindow(argv[0]);

    myinit();

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    glutMouseFunc(pickSquares);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

