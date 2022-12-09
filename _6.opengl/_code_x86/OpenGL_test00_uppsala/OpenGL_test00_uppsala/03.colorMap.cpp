/*****************************************************************************
 * This program demonstrates the color map in OpenGL and glut.               *
 *****************************************************************************/

#include "../../Common.h"

#define SIZE 600

 /* This is the routine that initializes some graphics parameters. */
void gfxinit()
{
    int i, index = 0;

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, 8.0, 0.0, 2.0);

    /* Set the true colors in entries 10-17 for comparison. */

    glutSetColor(10, 0.0, 0.0, 0.0);  /* black   */
    glutSetColor(11, 1.0, 0.0, 0.0);  /* red     */
    glutSetColor(12, 0.0, 1.0, 0.0);  /* green   */
    glutSetColor(13, 1.0, 1.0, 0.0);  /* yellow  */
    glutSetColor(14, 0.0, 0.0, 1.0);  /* blue    */
    glutSetColor(15, 1.0, 0.0, 1.0);  /* magenta */
    glutSetColor(16, 0.0, 1.0, 1.0);  /* cyan    */
    glutSetColor(17, 1.0, 1.0, 1.0);  /* white   */

    /* Generate the colors on the screen. */

    glNewList(1, GL_COMPILE);
    /* default color map entries */
    for (i = 0; i < 8; i++, index++)
    {
        glIndexi(index);
        cout << "Color " << index << " = (" << glutGetColor(index, GLUT_RED)
            << ", " << glutGetColor(index, GLUT_GREEN) << ", "
            << glutGetColor(index, GLUT_BLUE) << ")" << endl;
        glRecti(i, 0, i + 1, 1);
    }
    /* loaded color map entries */
    index += 2;
    for (i = 0; i < 8; i++, index++)
    {
        glIndexi(index);
        cout << "Color " << index << " = (" << glutGetColor(index, GLUT_RED)
            << ", " << glutGetColor(index, GLUT_GREEN) << ", "
            << glutGetColor(index, GLUT_BLUE) << ")" << endl;
        glRecti(i, 1, i + 1, 2);
    }
    glEndList();
}

// This is the callback function that gets executed every time the display needs to be updated.
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glutSwapBuffers();
}

int main(int argc, char** argv)
{
    /* Set graphics window parameters. */

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_INDEX);

    glutInitWindowSize(SIZE, SIZE);     // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Color Map");

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape0);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function

    cout << "Number of bits in color index = " << glutGet(GLUT_WINDOW_BUFFER_SIZE) << endl;

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}
