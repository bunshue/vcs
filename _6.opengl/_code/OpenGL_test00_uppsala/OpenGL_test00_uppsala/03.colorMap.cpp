#include "../../Common.h"

void gfxinit()
{
    int i;
    int index = 0;

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

        //�γ\ glutGetColor �\��w����
        printf("a Color %d = (%d, %d, %d)\n", index, glutGetColor(index, GLUT_RED),
            glutGetColor(index, GLUT_GREEN), glutGetColor(index, GLUT_BLUE));

        glRecti(i, 0, i + 1, 1);
    }
    /* loaded color map entries */
    index += 2;
    for (i = 0; i < 8; i++, index++)
    {
        glIndexi(index);

        //�γ\ glutGetColor �\��w����
        printf("b Color %d = (%d, %d, %d)\n", index, glutGetColor(index, GLUT_RED),
            glutGetColor(index, GLUT_GREEN), glutGetColor(index, GLUT_BLUE));

        glRecti(i, 1, i + 1, 2);
    }
    glEndList();
}

// This is the callback function that gets executed every time the display needs to be updated.
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glCallList(1);
    glFlush();  // ����ø�ϩR�O
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_INDEX);

    glutInitWindowSize(600, 600);       // �]�w�����j�p
    glutInitWindowPosition(1100, 200);  // �]�w������m

    glutCreateWindow("Color Map");

    glutDisplayFunc(display);   //�]�wcallback function
    glutReshapeFunc(reshape0);   //�]�wcallback function
    glutKeyboardFunc(keyboard0); //�]�wcallback function

    printf("Number of bits in color index = %d\n", glutGet(GLUT_WINDOW_BUFFER_SIZE));

    printf("Single Buffer �i�H�ݨ�e���{�{, Double Buffer�h�L\n");

    gfxinit();

    glutMainLoop();	//�}�l�D�`��ø�s

    return 0;
}
