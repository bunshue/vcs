// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

// CUDA Library Headers
#include <curand.h>
#include <cuda_gl_interop.h>

// CUDA utilities and system includes
#include <helper_cuda.h>
#include <rendercheck_gl.h>

// System includes
#include <stdexcept>
#include <sstream>
#include <iomanip>
#include <math.h>

// Includes
#include "rng.h"

// standard utility and system includes
#include <helper_timer.h>

// RNG instance
RNG *g_pRng = NULL;

// CheckRender instance (for QA)
CheckRender *g_pCheckRender = NULL;

// Simple struct which contains the position and color of a vertex
struct SVertex
{
  GLfloat x, y, z;
  GLfloat r, g, b;
};

// Data for the vertices
SVertex *g_pVertices = NULL;
int g_nVertices;           // Size of the vertex array
int g_nVerticesPopulated;  // Number currently populated

// Control the randomness
int nSkip1 = 0;  // Number of samples to discard between x,y
int nSkip2 = 0;  // Number of samples to discard between y,z
int nSkip3 = 0;  // Number of samples to discard between z,x

// Control the display
enum Shape_t { Sphere, Cube, Plane };

Shape_t g_currentShape = Sphere;

bool g_bShowAxes = true;
bool g_bTenXZoom = false;
int g_lastShapeX = 1024;
int g_lastShapeY = 1024;

const float PI = 3.14159265359f;

void createSphere(void)
{
    printf("nSkip(%d, %d, %d) ", nSkip1, nSkip2, nSkip3);

    int startVertex = 0;

    for (int i = startVertex; i < g_nVerticesPopulated; i++)
    {
        float r;
        float rho;
        float theta;

            r = g_pRng->getNextU01();
            r = powf(r, 1.f / 3.f);

            for (int j = 0; j < nSkip3; j++)
            {
                printf("XXXXXXXX\n");
                g_pRng->getNextU01();
            }

        rho = g_pRng->getNextU01() * PI * 2.0f;

        for (int j = 0; j < nSkip1; j++)
        {
            printf("XXXXXXXX\n");
            g_pRng->getNextU01();
        }

        theta = (g_pRng->getNextU01() * 2.0f) - 1.0f;
        theta = asin(theta);

        for (int j = 0; j < nSkip2; j++)
        {
            printf("XXXXXXXX\n");
            g_pRng->getNextU01();
        }

        g_pVertices[i].x = r * fabs(cos(theta)) * cos(rho);
        g_pVertices[i].y = r * fabs(cos(theta)) * sin(rho);
        g_pVertices[i].z = r * sin(theta);

        g_pVertices[i].r = 1.0f;
        g_pVertices[i].g = 1.0f;
        g_pVertices[i].b = 1.0f;
    }
}

void createAxes(void)
{
    // z axis:
    g_pVertices[200000].x = 0.0f;
    g_pVertices[200000].y = 0.0f;
    g_pVertices[200000].z = -1.5f;
    g_pVertices[200001].x = 0.0f;
    g_pVertices[200001].y = 0.0f;
    g_pVertices[200001].z = 1.5f;
    g_pVertices[200000].r = 1.0f;
    g_pVertices[200000].g = 0.0f;
    g_pVertices[200000].b = 0.0f;
    g_pVertices[200001].r = 0.0f;
    g_pVertices[200001].g = 1.0f;
    g_pVertices[200001].b = 1.0f;
    // y axis:
    g_pVertices[200002].x = 0.0f;
    g_pVertices[200002].y = -1.5f;
    g_pVertices[200002].z = 0.0f;
    g_pVertices[200003].x = 0.0f;
    g_pVertices[200003].y = 1.5f;
    g_pVertices[200003].z = 0.0f;
    g_pVertices[200002].r = 0.0f;
    g_pVertices[200002].g = 1.0f;
    g_pVertices[200002].b = 0.0f;
    g_pVertices[200003].r = 1.0f;
    g_pVertices[200003].g = 0.0f;
    g_pVertices[200003].b = 1.0f;
    // x axis:
    g_pVertices[200004].x = -1.5f;
    g_pVertices[200004].y = 0.0f;
    g_pVertices[200004].z = 0.0f;
    g_pVertices[200005].x = 1.5f;
    g_pVertices[200005].y = 0.0f;
    g_pVertices[200005].z = 0.0f;
    g_pVertices[200004].r = 0.0f;
    g_pVertices[200004].g = 0.0f;
    g_pVertices[200004].b = 1.0f;
    g_pVertices[200005].r = 1.0f;
    g_pVertices[200005].g = 1.0f;
    g_pVertices[200005].b = 0.0f;
}

void drawPoints(void)
{
    if (g_bShowAxes)
    {
        glDrawArrays(GL_LINE_STRIP, 200000, 2);
        glDrawArrays(GL_LINE_STRIP, 200002, 2);
        glDrawArrays(GL_LINE_STRIP, 200004, 2);
    }

    glDrawArrays(GL_POINTS, 0, g_nVerticesPopulated);
}

void drawText(void)
{
    glLoadIdentity();	//設置單位矩陣
    glRasterPos2f(-1.2f, 1.2f);

    string infoString = "This is a lion-mouse.";
    for (unsigned int i = 0; i < infoString.size(); i++)
    {
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, infoString[i]);
    }
}

void reshape(int x, int y)
{
    printf("reshape\n");
    float xScale;
    float yScale;

    g_lastShapeX = x;
    g_lastShapeY = y;

    // Check if shape is visible
    if (x == 0 || y == 0)
    {
        return;
    }

    // Set a new projection matrix
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣

    // Adjust fit
    if (y > x)
    {
        xScale = 1.0f;
        yScale = (float)y / x;
    }
    else
    {
        xScale = (float)x / y;
        yScale = 1.0f;
    }

    // Angle of view:40 degrees
    // Near clipping plane distance: 10.0 (default)
    // Far clipping plane distance: 10.0 (default)
    if (g_bTenXZoom)
    {
        glOrtho(-.15f * xScale, .15f * xScale, -.15f * yScale, .15f * yScale, -5.0f, 5.0f);
    }
    else
    {
        glOrtho(-1.5f * xScale, 1.5f * xScale, -1.5f * yScale, 1.5f * yScale, -10.0f, 10.0f);
    }

    // Use the whole window for rendering
    glViewport(0, 0, x, y);
    glMatrixMode(GL_MODELVIEW);
}

void display(void)
{
    //printf("d");
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();	//設置單位矩陣
    glTranslatef(0.0f, 0.0f, -4.0f);
    //glRotatef(g_yRotated, 0.0f, 1.0f, 0.0f);
    //glRotatef(g_xRotated, 1.0f, 0.0f, 0.0f);
    drawPoints();
    drawText();
    glFlush();
    glutSwapBuffers();
}

void idle(void)
{
    //printf("I");
}

void reCreate(void)
{
    printf("reCreate ");
    switch (g_currentShape)
    {
    case Sphere:
        createSphere();
        break;

    default:
        break;
    }

    display();
}

void cleanup(int code)
{
    if (g_pRng)
    {
        delete g_pRng;
        g_pRng = NULL;
    }

    if (g_pVertices)
    {
        delete[] g_pVertices;
        g_pVertices = NULL;
    }

    if (g_pCheckRender)
    {
        delete g_pCheckRender;
        g_pCheckRender = NULL;
    }

    exit(code);
}

void glutClose() { cleanup(EXIT_SUCCESS); }

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
        // Select shape
    case 's':
    case 'S':
        g_currentShape = Sphere;
        createSphere();
        display();
        break;

        // Quit
    case 27:
    case 'q':
    case 'Q':
        glutDestroyWindow(glutGetWindow());
        return;
    }
}

int main(int argc, char** argv)
{
    // Initialize GL
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    // TODO use width/height?
    glutInitWindowSize(1000, 1000);     //設定視窗大小, 直接拉大內容
    glutInitWindowPosition(900, 50);    //視窗起始位置

    // Create a window with rendering context and everything else we need
    glutCreateWindow("Random Fog");

    if (!isGLVersionSupported(2, 0))
    {
        fprintf(stderr, "This sample requires at least OpenGL 2.0\n");
        exit(EXIT_WAIVED);
    }

    // Select CUDA device with OpenGL interoperability
    findCudaDevice(argc, (const char**)argv);

    // Create vertices
    g_nVertices = 200000;
    g_nVerticesPopulated = 200000;
    g_pVertices = new SVertex[g_nVertices + 6];

    // Setup the random number generators
    g_pRng = new RNG(12345, 1, 100000);
    printf("CURAND initialized\n");

    // Compute the initial vertices and indices, starting in spherical mode
    createSphere();
    createAxes();

    // As we do not yet use a depth buffer, we cannot fill our sphere
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
    // Enable the vertex array functionality:
    glEnableClientState(GL_VERTEX_ARRAY);
    // Enable the color array functionality (so we can specify a color for
    // each vertex)
    glEnableClientState(GL_COLOR_ARRAY);
    // Pass the vertex pointer:
    glVertexPointer(3,  // 3 components per vertex (x,y,z)
        GL_FLOAT, sizeof(SVertex), g_pVertices);
    // Pass the color pointer
    glColorPointer(3,  // 3 components per vertex (r,g,b)
        GL_FLOAT, sizeof(SVertex),
        &g_pVertices[0].r);  // Pointer to the first color
// Point size for point mode
    glPointSize(1.0f);
    glLineWidth(2.0f);
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard); //設定callback function
    glutIdleFunc(idle);		//設定callback function, 利用idle事件進行重畫
    glutCloseFunc(glutClose);   //設定callback function

    glutMainLoop();	//開始主循環繪製

    exit(EXIT_SUCCESS);
}
