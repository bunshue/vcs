#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#define MAXOBJS 10000
#define MAXSELECT 100
#define MAXFEED 300
#define	SOLID 1
#define	LINE 2
#define	POINT 3

GLint windW = 300;
GLint windH = 300;

GLuint selectBuf[MAXSELECT];
GLfloat feedBuf[MAXFEED];
GLint vp[4];
float zRotation = 90.0;
float zoom = 1.0;
GLint objectCount;
GLint numObjects;

struct object {
    float v1[2];
    float v2[2];
    float v3[2];
    float color[3];
} objects[MAXOBJS];

GLenum linePoly = GL_FALSE;

void InitObjects(GLint num)
{
    GLint i;
    float x, y;

    if (num > MAXOBJS)
    {
        num = MAXOBJS;
    }

    if (num < 1)
    {
        num = 1;
    }
    objectCount = num;

    srand((unsigned int)time(NULL));

    for (i = 0; i < num; i++)
    {
        x = (rand() % 300) - 150;
        y = (rand() % 300) - 150;

        objects[i].v1[0] = x + (rand() % 50) - 25;
        objects[i].v2[0] = x + (rand() % 50) - 25;
        objects[i].v3[0] = x + (rand() % 50) - 25;
        objects[i].v1[1] = y + (rand() % 50) - 25;
        objects[i].v2[1] = y + (rand() % 50) - 25;
        objects[i].v3[1] = y + (rand() % 50) - 25;
        objects[i].color[0] = ((rand() % 100) + 50) / 150.0;
        objects[i].color[1] = ((rand() % 100) + 50) / 150.0;
        objects[i].color[2] = ((rand() % 100) + 50) / 150.0;
    }
}

void Init(void)
{
    numObjects = 10;
    InitObjects(numObjects);
    glGetIntegerv(GL_VIEWPORT, vp);
}

void reshape(int width, int height)
{
    windW = width;
    windH = height;
}

void Render(GLenum mode)
{
    GLint i;

    for (i = 0; i < objectCount; i++)
    {
        if (mode == GL_SELECT)
        {
            glLoadName(i);
        }
        glColor3fv(objects[i].color);
        glBegin(GL_POLYGON);
        glVertex2fv(objects[i].v1);
        glVertex2fv(objects[i].v2);
        glVertex2fv(objects[i].v3);
        glEnd();
    }
}

GLint DoSelect(GLint x, GLint y)
{
    GLint hits;

    glSelectBuffer(MAXSELECT, selectBuf);
    glRenderMode(GL_SELECT);
    glInitNames();
    glPushName(~0);

    glPushMatrix();

    glViewport(0, 0, windW, windH);
    glGetIntegerv(GL_VIEWPORT, vp);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPickMatrix(x, windH - y, 4, 4, vp);
    gluOrtho2D(-175, 175, -175, 175);	//窗口座標範圍, 2D
    glMatrixMode(GL_MODELVIEW);

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);

    glScalef(zoom, zoom, zoom);
    glRotatef(zRotation, 0, 0, 1);

    Render(GL_SELECT);

    glPopMatrix();

    hits = glRenderMode(GL_RENDER);
    if (hits <= 0)
    {
        return -1;
    }

    return selectBuf[(hits - 1) * 4 + 3];
}

void RecolorTri(GLint h)
{
    objects[h].color[0] = ((rand() % 100) + 50) / 150.0;
    objects[h].color[1] = ((rand() % 100) + 50) / 150.0;
    objects[h].color[2] = ((rand() % 100) + 50) / 150.0;
}

void DeleteTri(GLint h)
{
    objects[h] = objects[objectCount - 1];
    objectCount--;
}

void GrowTri(GLint h)
{
    float v[2];
    float* oldV;
    GLint i;

    v[0] = objects[h].v1[0] + objects[h].v2[0] + objects[h].v3[0];
    v[1] = objects[h].v1[1] + objects[h].v2[1] + objects[h].v3[1];
    v[0] /= 3;
    v[1] /= 3;

    oldV = (float*)malloc(sizeof(GLint));

    for (i = 0; i < 3; i++)
    {
        switch (i)
        {
        case 0:
            oldV = objects[h].v1;
            break;
        case 1:
            oldV = objects[h].v2;
            break;
        case 2:
            oldV = objects[h].v3;
            break;
        }
        oldV[0] = 1.5 * (oldV[0] - v[0]) + v[0];
        oldV[1] = 1.5 * (oldV[1] - v[1]) + v[1];
    }
}

void mouse(int button, int state, int mouseX, int mouseY)
{
    GLint hit;

    if (state == GLUT_DOWN)
    {
        hit = DoSelect((GLint)mouseX, (GLint)mouseY);
        if (hit != -1)
        {
            if (button == GLUT_LEFT_BUTTON)
            {
                RecolorTri(hit);
            }
            else if (button == GLUT_MIDDLE_BUTTON)
            {
                GrowTri(hit);
            }
            else if (button == GLUT_RIGHT_BUTTON)
            {
                DeleteTri(hit);
            }
            glutPostRedisplay();
        }
    }
}

void display(void)
{
    glPushMatrix();

    glViewport(0, 0, windW, windH);
    glGetIntegerv(GL_VIEWPORT, vp);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-175, 175, -175, 175);	//窗口座標範圍, 2D
    glMatrixMode(GL_MODELVIEW);

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);

    glScalef(zoom, zoom, zoom);
    glRotatef(zRotation, 0, 0, 1);

    Render(GL_RENDER);

    glPopMatrix();

    glFlush();
}

void DumpFeedbackVert(GLint* i, GLint n)
{
    GLint index;

    index = *i;
    if (index + 7 > n)
    {
        *i = n;
        printf("  ???\n");
        return;
    }
    printf("  (%g %g %g), color = (%4.2f %4.2f %4.2f)\n",
        feedBuf[index],
        feedBuf[index + 1],
        feedBuf[index + 2],
        feedBuf[index + 3],
        feedBuf[index + 4],
        feedBuf[index + 5]);
    index += 7;
    *i = index;
}

void DrawFeedback(GLint n)
{
    GLint i;
    GLint verts;

    printf("Feedback results (%d floats):\n", n);
    for (i = 0; i < n; i++)
    {
        switch ((GLint)feedBuf[i])
        {
        case GL_POLYGON_TOKEN:
            printf("Polygon");
            i++;
            if (i < n)
            {
                verts = (GLint)feedBuf[i];
                i++;
                printf(": %d vertices", verts);
            }
            else
            {
                verts = 0;
            }
            printf("\n");
            while (verts)
            {
                DumpFeedbackVert(&i, n);
                verts--;
            }
            i--;
            break;
        case GL_LINE_TOKEN:
            printf("Line:\n");
            i++;
            DumpFeedbackVert(&i, n);
            DumpFeedbackVert(&i, n);
            i--;
            break;
        case GL_LINE_RESET_TOKEN:
            printf("Line Reset:\n");
            i++;
            DumpFeedbackVert(&i, n);
            DumpFeedbackVert(&i, n);
            i--;
            break;
        default:
            printf("%9.2f\n", feedBuf[i]);
            break;
        }
    }
    if (i == MAXFEED)
    {
        printf("...\n");
    }
    printf("\n");
}

void DoFeedback(void)
{
    GLint x;

    glFeedbackBuffer(MAXFEED, GL_3D_COLOR, feedBuf);
    (void)glRenderMode(GL_FEEDBACK);

    glPushMatrix();

    glViewport(0, 0, windW, windH);
    glGetIntegerv(GL_VIEWPORT, vp);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-175, 175, -175, 175);	//窗口座標範圍, 2D
    glMatrixMode(GL_MODELVIEW);

    glClearColor(0.0, 0.0, 0.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT);

    glScalef(zoom, zoom, zoom);
    glRotatef(zRotation, 0, 0, 1);

    Render(GL_FEEDBACK);

    glPopMatrix();

    x = glRenderMode(GL_RENDER);
    if (x == -1)
    {
        x = MAXFEED;
    }

    DrawFeedback((GLint)x);
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 'z':
        zoom /= 0.75;
        glutPostRedisplay();
        break;
    case 'Z':
        zoom *= 0.75;
        glutPostRedisplay();
        break;
    case 'f':
        DoFeedback();
        glutPostRedisplay();
        break;
    case 'l':
        linePoly = !linePoly;
        if (linePoly)
        {
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
        }
        else
        {
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
        }
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
    }
}

void special(int key, int x, int y)
{
    switch (key)
    {
    case GLUT_KEY_LEFT:
        zRotation += 2.5;
        glutPostRedisplay();
        break;
    case GLUT_KEY_RIGHT:
        zRotation -= 2.5;
        glutPostRedisplay();
        break;
    }
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);

    glutInitWindowSize(600, 600);
    glutInitWindowPosition(1100, 200);

    glutCreateWindow("Select Test");	//開啟視窗 並顯示出視窗 Title

    Init();

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function
    glutSpecialFunc(special);       //設定callback function
    glutMouseFunc(mouse);           //設定callback function

    printf("按 左 右 控制\n");

    glutMainLoop();	//開始主循環繪製

    return 0;
}

