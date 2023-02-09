/*
Recursive subdivision of tetrahedron (Chapter 6).
Three display modes:
wire frame, constant, and interpolative shading
*/

/*Program also illustrates defining materials and light sources in myiit() */

/*
mode 0 = wire frame,
mode 1 = constant shading,
mode 2 = interpolative shading
*/

#include "../../Common.h"

typedef double point[3];

/* initial tetrahedron */
point v[] =
{
    {0.0, 0.0, 1.0},
    {0.0, 0.942809, -0.33333},
    {-0.816497, -0.471405, -0.333333},
    {0.816497, -0.471405, -0.333333}
};

static GLfloat theta[] = { 0.0,0.0,0.0 };

int num = 3;
int mode;

/* display one triangle using a line loop for wire frame, a single
normal for constant shading, or three normals for interpolative shading */
void triangle(point a, point b, point c)
{
    if (mode == 0)
    {
        glBegin(GL_LINE_LOOP);
    }
    else
    {
        glBegin(GL_POLYGON);
    }

    if (mode == 1 || mode == 2)
    {
        glNormal3dv(a);
    }
    glVertex3dv(a);
    if (mode == 2)
    {
        glNormal3dv(b);
    }
    glVertex3dv(b);
    if (mode == 2)
    {
        glNormal3dv(c);
    }
    glVertex3dv(c);
    glEnd();
}

/* normalize a vector */
void normal(point p)
{
    double d = 0.0;
    int i;
    for (i = 0; i < 3; i++)
    {
        d += p[i] * p[i];
    }
    d = sqrt(d);
    if (d > 0.0)
    {
        for (i = 0; i < 3; i++)
        {
            p[i] /= d;
        }
    }
}

/* triangle subdivision using vertex numbers
righthand rule applied to create outward pointing faces */
void divide_triangle(point a, point b, point c, int num)
{
    point v1, v2, v3;
    int j;
    if (num > 0)
    {
        for (j = 0; j < 3; j++)
        {
            v1[j] = a[j] + b[j];
        }
        normal(v1);
        for (j = 0; j < 3; j++)
        {
            v2[j] = a[j] + c[j];
        }
        normal(v2);
        for (j = 0; j < 3; j++)
        {
            v3[j] = b[j] + c[j];
        }
        normal(v3);
        divide_triangle(a, v1, v2, num - 1);
        divide_triangle(c, v2, v3, num - 1);
        divide_triangle(b, v3, v1, num - 1);
        divide_triangle(v1, v3, v2, num - 1);
    }
    else
    {
        triangle(a, b, c); /* draw triangle at end of recursion */
    }
}

/* Apply triangle subdivision to faces of tetrahedron */
void tetrahedron(int num)
{
    divide_triangle(v[0], v[1], v[2], num);
    divide_triangle(v[3], v[2], v[1], num);
    divide_triangle(v[0], v[3], v[1], num);
    divide_triangle(v[0], v[2], v[3], num);
}

/* Displays all three modes, side by side */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    //畫個參考座標軸
    draw_coordinates(3.5f);     //畫座標軸

    glTranslated(-2.0, 0.0, 0.0);
    mode = 0;
    tetrahedron(num);   //左圖

    glTranslated(2.0, 0.0, 0.0);
    mode = 1;
    tetrahedron(num);   //中圖

    glTranslated(2.0, 0.0, 0.0);
    mode = 2;
    tetrahedron(num); //右圖

    glutSwapBuffers();
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    if (w <= h)
    {
        glOrtho(-4.0, 4.0, -4.0 * (GLfloat)h / (GLfloat)w, 4.0 * (GLfloat)h / (GLfloat)w, -10.0, 10.0);
    }
    else
    {
        glOrtho(-4.0 * (GLfloat)w / (GLfloat)h, 4.0 * (GLfloat)w / (GLfloat)h, -4.0, 4.0, -10.0, 10.0);
    }
    glMatrixMode(GL_MODELVIEW);
    glutPostRedisplay();
}

void myinit()
{
    GLfloat mat_specular[] = { 0.5, 0.0, 0.0, 1.0 };
    GLfloat mat_diffuse[] = { 1.0, 0.0, 0.0, 1.0 };
    GLfloat mat_ambient[] = { 1.0, 0.0, 0.0, 1.0 };
    GLfloat mat_shininess = { 100.0 };
    GLfloat light_ambient[] = { 0.0, 0.0, 0.0, 1.0 };
    GLfloat light_diffuse[] = { 1.0, 1.0, 1.0, 1.0 };
    GLfloat light_specular[] = { 1.0, 1.0, 1.0, 1.0 };

    /* set up ambient, diffuse, and specular components for light 0 */

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);

    /* define material proerties for front face of all polygons */

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess);

    glEnable(GL_SMOOTH);        //enable smooth shading
    glEnable(GL_LIGHTING);      //enable lighting
    glEnable(GL_LIGHT0);        //enable light 0
    glEnable(GL_DEPTH_TEST);    //enable z buffer

    glClearColor(1.0, 1.0, 1.0, 1.0);
    glColor3f(0.0, 0.0, 0.0);
}

int main(int argc, char** argv)
{
    const char* windowName = "Sphere";
    const char* message = "僅顯示, 無控制, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard0);

    //先保留
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

    myinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

