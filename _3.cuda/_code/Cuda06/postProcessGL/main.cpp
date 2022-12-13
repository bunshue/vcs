// OpenGL Graphics includes
#include <helper_gl.h>
#include <GL/freeglut.h>

// CUDA includes
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// CUDA utilities and system includes
#include <helper_cuda.h>

#include <helper_functions.h>
#include <rendercheck_gl.h>

////////////////////////////////////////////////////////////////////////////////
// constants / global variables
unsigned int window_width = 600;
unsigned int window_height = 600;
unsigned int image_width = 600;
unsigned int image_height = 600;

// pbo and fbo variables
GLuint pbo_dest;
struct cudaGraphicsResource* cuda_pbo_dest_resource;

GLuint fbo_source;
struct cudaGraphicsResource* cuda_tex_screen_resource;

// (offscreen) render target fbo variables
GLuint tex_screen;      // where we render the image
GLuint tex_cudaResult;  // where we will copy the CUDA result

////////////////////////////////////////////////////////////////////////////////
//! Create PBO
////////////////////////////////////////////////////////////////////////////////
void createPBO(GLuint* pbo, struct cudaGraphicsResource** pbo_resource)
{
    // set up vertex data parameter
    unsigned int num_texels = image_width * image_height;
    unsigned int num_values = num_texels * 4;
    unsigned int size_tex_data = sizeof(GLubyte) * num_values;
    void* data = malloc(size_tex_data);

    // create buffer object
    glGenBuffers(1, pbo);
    glBindBuffer(GL_ARRAY_BUFFER, *pbo);
    glBufferData(GL_ARRAY_BUFFER, size_tex_data, data, GL_DYNAMIC_DRAW);
    free(data);

    glBindBuffer(GL_ARRAY_BUFFER, 0);

    // register this buffer object with CUDA
    cudaGraphicsGLRegisterBuffer(pbo_resource, *pbo, cudaGraphicsMapFlagsNone);
}

void deletePBO(GLuint* pbo)
{
    glDeleteBuffers(1, pbo);
    *pbo = 0;
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
    glTranslatef(0.0, 0.0, -3.0);

    glViewport(0, 0, 600, 600);

    glEnable(GL_LIGHTING);
    glEnable(GL_DEPTH_TEST);

    //glutSolidTeapot(0.7);       //畫茶壺, 實心
    glutWireTeapot(0.7);       //畫茶壺, 線框

    glFlush();  //強制刷新緩存區
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    //printf("你所按按鍵的碼是%x\t此時視窗內的滑鼠座標是(%d,%d)\n", key, x, y);

    switch (key)
    {
    case 27:
    case 'q':
    case 'Q':
        //離開視窗
        glutDestroyWindow(glutGetWindow());
        return;
    }
}

// 窗口大小變化回調函數
void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
}

void createTextureSrc(GLuint* tex_screen, unsigned int size_x, unsigned int size_y)
{
    // create a texture
    glGenTextures(1, tex_screen);	//生成紋理對象
    glBindTexture(GL_TEXTURE_2D, *tex_screen);	//綁定紋理

    // set basic parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    // buffer data
    //printf("Creating a Texture render target GL_RGBA16F_ARB\n");
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA16F_ARB, size_x, size_y, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);

    // register this texture with CUDA
    cudaGraphicsGLRegisterImage(&cuda_tex_screen_resource, *tex_screen, GL_TEXTURE_2D, cudaGraphicsMapFlagsReadOnly);
}

void createTextureDst(GLuint* tex_cudaResult, unsigned int size_x, unsigned int size_y)
{
    // create a texture
    glGenTextures(1, tex_cudaResult);	//生成紋理對象
    glBindTexture(GL_TEXTURE_2D, *tex_cudaResult);	//綁定紋理

    // set basic parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, size_x, size_y, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);
}

void deleteTexture(GLuint* tex)
{
    glDeleteTextures(1, tex);
    *tex = 0;
}

void FreeResource()
{
    // unregister this buffer object with CUDA
    cudaGraphicsUnregisterResource(cuda_tex_screen_resource);
    cudaGraphicsUnregisterResource(cuda_pbo_dest_resource);
    deletePBO(&pbo_dest);
    deleteTexture(&tex_screen);
    deleteTexture(&tex_cudaResult);
    glutDestroyWindow(glutGetWindow());
}

////////////////////////////////////////////////////////////////////////////////
//! Allocate the "render target" of CUDA
////////////////////////////////////////////////////////////////////////////////
void initGLBuffers()
{
    printf("initGLBuffers() 1\n");
    // create pbo
    createPBO(&pbo_dest, &cuda_pbo_dest_resource);
    // create texture that will receive the result of CUDA
    createTextureDst(&tex_cudaResult, image_width, image_height);

    // create texture for blitting onto the screen
    createTextureSrc(&tex_screen, image_width, image_height);
}

bool initGL(int* argc, char** argv)
{
    // Create GL context
    glutInit(argc, argv);

    glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(600, 600);       // 設定視窗大小
    glutInitWindowPosition(1100, 200);  // 設定視窗位置

    glutCreateWindow("CUDA OpenGL post-processing");

    glewInit();

    // default initialization
    glClearColor(0.5, 0.5, 0.5, 1.0);
    glDisable(GL_DEPTH_TEST);

    // projection
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();	//設置單位矩陣
    gluPerspective(60.0, (GLfloat)window_width / (GLfloat)window_height, 0.1f, 10.0f);

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

    glEnable(GL_LIGHT0);
    float red[] = { 1.0f, 0.1f, 0.1f, 1.0f };
    float white[] = { 1.0f, 1.0f, 1.0f, 1.0f };
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, red);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white);
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 60.0f);

    return true;
}

int main(int argc, char** argv)
{
    printf("Starting...\n\n");

    initGL(&argc, argv);

    glutDisplayFunc(display);   //設定callback function
    glutReshapeFunc(reshape);   //設定callback function
    glutKeyboardFunc(keyboard); //設定callback function

    initGLBuffers();

    glutMainLoop();	//開始主循環繪製

    FreeResource();
}
