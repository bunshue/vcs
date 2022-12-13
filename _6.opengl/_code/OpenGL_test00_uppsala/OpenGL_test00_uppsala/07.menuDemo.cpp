/**************************************************************
 * This program demonstrates menus in OpenGL and GLUT. It     *
 * uses a menu to change the drawing color and the line       *
 * thickness. The drawing area can also be cleared and the    *
 * program exited from the menu.                              *
 **************************************************************/

#include "../../Common.h"

#define SIZE 600

int pointsChosen, x_st, y_st, numberOfLists = 0;
GLsizei ysize;

void gfxinit()
/* This is the routine that initializes some graphics parameters. */
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, SIZE - 1, 0.0, SIZE - 1);
    glClearColor(1.0, 1.0, 1.0, 0.0);  /* make the background white */
    glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
    glColor3d(0.0, 0.0, 0.0);          /* initial drawing color is black */
    glLineWidth(1.0);                  /* initial thickness is 1 */
    glEndList();
    pointsChosen = 0;
    ysize = SIZE - 1;
}

/* This is the callback function for the color menu. */
void colorMenu(int id)
{
    glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
    switch (id)
    {
    case 1: /* change color to red */
        glColor3d(1.0, 0.0, 0.0);
        break;
    case 2: /* change color to green */
        glColor3d(0.0, 1.0, 0.0);
        break;
    case 3: /* change color to blue */
        glColor3d(0.0, 0.0, 1.0);
        break;
    case 4: /* change color to black */
        glColor3d(0.0, 0.0, 0.0);
        break;
    default: /* for any case not covered above, leave color unchanged */
        break;
    }
    glEndList();
    pointsChosen = 0;
}

void sizeMenu(int id)
/* This is the callback function for the size menu. */
{
    glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
    switch (id)
    {
    case 1: /* change line thickness to 1 */
        glLineWidth(1.0);
        break;
    case 2: /* change line thickness to 2 */
        glLineWidth(2.0);
        break;
    case 3: /* change line thickness to 3 */
        glLineWidth(3.0);
        break;
    default: /* for any case not covered above, leave line thickness unchanged */
        break;
    }
    glEndList();
}

void mainMenu(int id)
/* This is the callback function for the main menu. */
{
    double lineWidth, color[4];

    switch (id)
    {
    case 1: /* reset default values */
        glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
        glColor3d(0.0, 0.0, 0.0);
        glLineWidth(1.0);
        glEndList();
        break;
    case 2: /* clear the screen */
        glDeleteLists(1, numberOfLists);
        numberOfLists = 0;
        glGetDoublev(GL_LINE_WIDTH, &lineWidth);
        glGetDoublev(GL_CURRENT_COLOR, color);
        glNewList(++numberOfLists, GL_COMPILE);
        glColor4dv(color);
        glLineWidth(lineWidth);
        glEndList();
        glutPostRedisplay();
        break;
    case 3: /* exit the program */
        exit(0);
        break;
    default: /* in case none of the above occur */
        break;
    }
}

void initMenus()
{
    int color_menu, size_menu;

    /* Create the menu structure and attach it to the right mouse button. */
    color_menu = glutCreateMenu(colorMenu);
    glutAddMenuEntry("Red", 1);
    glutAddMenuEntry("Green", 2);
    glutAddMenuEntry("Blue", 3);
    glutAddMenuEntry("Black", 4);
    size_menu = glutCreateMenu(sizeMenu);
    glutAddMenuEntry("1", 1);
    glutAddMenuEntry("2", 2);
    glutAddMenuEntry("3", 3);
    glutCreateMenu(mainMenu);
    glutAddSubMenu("Color", color_menu);
    glutAddSubMenu("Size", size_menu);
    glutAddMenuEntry("Reset defaults", 1);
    glutAddMenuEntry("Clear window", 2);
    glutAddMenuEntry("Exit", 3);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}

void instructions()
/* This function displays the instructions to the user. */
{
    cout << "This is a simple program to demonstrate menus in OpenGL and glut." << endl;
    cout << "Press the right mouse button over the graphics window to display the menu." << endl;
    cout << "Click the left mouse button twice to define two endpoints of a line segment to be drawn." << endl;
}

/* This is the callback function that gets executed every time the display needs to be updated. */
void display(void)
{
    int i;

    glClear(GL_COLOR_BUFFER_BIT);
    for (i = 1; i <= numberOfLists; i++)
    {
        glCallList(i);
    }
    glFlush();
}

/* This is the callback function that gets executed when a mouse button is pressed. */
void mouse(int button, int state, int x, int y)
{
    if ((button == GLUT_LEFT_BUTTON) && (state == GLUT_DOWN))
    {
        if (pointsChosen == 0)
        {
            x_st = x;
            y_st = ysize - y;
            pointsChosen = 1;
        }
        else
        {
            glNewList(++numberOfLists, GL_COMPILE_AND_EXECUTE);
            glBegin(GL_LINES);
            glVertex2i(x_st, y_st);
            glVertex2i(x, ysize - y);
            glEnd();
            glEndList();
            glFlush();
            pointsChosen = 0;
        }
    }
}

/* This function gets called whenever the window is resized. */
void reshape(GLsizei w, GLsizei h)
{
    /* Adjust the clipping rectangle. */

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, w - 1, 0.0, h - 1);
    ysize = h - 1;

    /* Adjust the viewport. */

    glViewport(0, 0, w, h);
}

int main(int argc, char** argv)
{
    instructions();

    /* Set graphics window parameters. */

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

    glutInitWindowSize(SIZE, SIZE);     // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("Menu Demonstration");

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard0); //設定callback function
    glutMouseFunc(mouse);   //設定callback function

    /* Initialize the graphics and enter the event loop. */
    gfxinit();

    initMenus();        //設定表單按鈕

    glutMainLoop();	//開始主循環繪製

    return 0;
}
