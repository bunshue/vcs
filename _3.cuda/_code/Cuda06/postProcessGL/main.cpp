#define WINDOWS_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>
#pragma warning(disable : 4996)

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

// CheckFBO/BackBuffer class objects
CheckRender* g_CheckRender = NULL;

////////////////////////////////////////////////////////////////////////////////
// constants / global variables
unsigned int window_width = 512;
unsigned int window_height = 512;
unsigned int image_width = 512;
unsigned int image_height = 512;
int iGLUTWindowHandle = 0;  // handle to the GLUT window

// pbo and fbo variables
GLuint pbo_dest;
struct cudaGraphicsResource* cuda_pbo_dest_resource;
extern cudaTextureObject_t inTexObject;

GLuint fbo_source;
struct cudaGraphicsResource* cuda_tex_screen_resource;

unsigned int size_tex_data;
unsigned int num_texels;
unsigned int num_values;

// (offscreen) render target fbo variables
GLuint framebuffer;     // to bind the proper targets
GLuint depth_buffer;    // for proper depth test while rendering the scene
GLuint tex_screen;      // where we render the image
GLuint tex_cudaResult;  // where we will copy the CUDA result

float rotate[3];

int blur_radius = 8;
int max_blur_radius = 16;

GLuint shDrawPot;  // colors the teapot

// GL functionality
bool initGL(int* argc, char** argv);

void createPBO(GLuint* pbo, struct cudaGraphicsResource** pbo_resource);
void deletePBO(GLuint* pbo);
void createTextureDst(GLuint* tex_cudaResult, unsigned int size_x, unsigned int size_y);
void createTextureSrc(GLuint* tex_screen, unsigned int size_x, unsigned int size_y);
void deleteTexture(GLuint* tex);
void createDepthBuffer(GLuint* depth, unsigned int size_x, unsigned int size_y);
void deleteDepthBuffer(GLuint* depth);
void createFramebuffer(GLuint* fbo, GLuint color, GLuint depth);
void deleteFramebuffer(GLuint* fbo);

// rendering callbacks
void display();
void idle();
void keyboard(unsigned char key, int x, int y);
void reshape(int w, int h);

////////////////////////////////////////////////////////////////////////////////
//! Create PBO
////////////////////////////////////////////////////////////////////////////////
void createPBO(GLuint* pbo, struct cudaGraphicsResource** pbo_resource)
{
    // set up vertex data parameter
    num_texels = image_width * image_height;
    num_values = num_texels * 4;
    size_tex_data = sizeof(GLubyte) * num_values;
    void* data = malloc(size_tex_data);

    // create buffer object
    glGenBuffers(1, pbo);
    glBindBuffer(GL_ARRAY_BUFFER, *pbo);
    glBufferData(GL_ARRAY_BUFFER, size_tex_data, data, GL_DYNAMIC_DRAW);
    free(data);

    glBindBuffer(GL_ARRAY_BUFFER, 0);

    // register this buffer object with CUDA
    checkCudaErrors(cudaGraphicsGLRegisterBuffer(pbo_resource, *pbo, cudaGraphicsMapFlagsNone));

}

void deletePBO(GLuint* pbo)
{
    glDeleteBuffers(1, pbo);
    *pbo = 0;
}

const GLenum fbo_targets[] = {
    GL_COLOR_ATTACHMENT0_EXT, GL_COLOR_ATTACHMENT1_EXT,
    GL_COLOR_ATTACHMENT2_EXT, GL_COLOR_ATTACHMENT3_EXT };

static const char* glsl_drawpot_fragshader_src =
// WARNING: seems like the gl_FragColor doesn't want to output >1 colors...
// you need version 1.3 so you can define a uvec4 output...
// but MacOSX complains about not supporting 1.3 !!
// for now, the mode where we use RGBA8UI may not work properly for Apple : only
// RGBA16F works (default)
"#version 130\n"
"in vec4 inColor;\n"
"out uvec4 FragColor;\n"
"void main()\n"
"{"
"  FragColor = uvec4(inColor.xyz * 255.0, 255.0);\n"
"}\n";

void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣
    glTranslatef(0.0, 0.0, -3.0);
    glRotatef(rotate[0], 1.0, 0.0, 0.0);
    glRotatef(rotate[1], 0.0, 1.0, 0.0);
    glRotatef(rotate[2], 0.0, 0.0, 1.0);

    glViewport(0, 0, 512, 512);

    glEnable(GL_LIGHTING);
    glEnable(GL_DEPTH_TEST);

    glutSolidTeapot(0.7);

    glFlush();  //強制刷新緩存區
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case (27):
        exit(0);
        break;
    }
}

void reshape(int w, int h)
{
    window_width = w;
    window_height = h;
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
    printf("Creating a Texture render target GL_RGBA16F_ARB\n");
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA16F_ARB, size_x, size_y, 0, GL_RGBA, GL_UNSIGNED_BYTE, NULL);

    // register this texture with CUDA
    checkCudaErrors(cudaGraphicsGLRegisterImage(&cuda_tex_screen_resource, *tex_screen, GL_TEXTURE_2D, cudaGraphicsMapFlagsReadOnly));
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

void createDepthBuffer(GLuint* depth, unsigned int size_x, unsigned int size_y)
{
    // create a renderbuffer
    glGenRenderbuffersEXT(1, depth);
    glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, *depth);

    // allocate storage
    glRenderbufferStorageEXT(GL_RENDERBUFFER_EXT, GL_DEPTH_COMPONENT24, size_x, size_y);

    // clean up
    glBindRenderbufferEXT(GL_RENDERBUFFER_EXT, 0);

}

void deleteDepthBuffer(GLuint* depth)
{
    glDeleteRenderbuffersEXT(1, depth);

    *depth = 0;
}

void createFramebuffer(GLuint* fbo, GLuint color, GLuint depth)
{
    // create and bind a framebuffer
    glGenFramebuffersEXT(1, fbo);
    glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, *fbo);

    // attach images
    glFramebufferTexture2DEXT(GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT, GL_TEXTURE_2D, color, 0);
    // glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT, GL_RENDERBUFFER_EXT, color);
    glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_DEPTH_ATTACHMENT_EXT, GL_RENDERBUFFER_EXT, depth);

    // clean up
    glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, 0);
}

void deleteFramebuffer(GLuint* fbo)
{
    glDeleteFramebuffersEXT(1, fbo);
    *fbo = 0;
}

void FreeResource()
{
    // unregister this buffer object with CUDA
    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_tex_screen_resource));
    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_pbo_dest_resource));
    deletePBO(&pbo_dest);
    deleteTexture(&tex_screen);
    deleteTexture(&tex_cudaResult);
    deleteDepthBuffer(&depth_buffer);
    deleteFramebuffer(&framebuffer);

    if (iGLUTWindowHandle)
    {
        glutDestroyWindow(iGLUTWindowHandle);
    }

    // finalize logs and leave
    printf("postProcessGL.exe Exiting...\n");
}

GLuint compileGLSLprogram(const char* vertex_shader_src, const char* fragment_shader_src)
{
    GLuint f, p = 0;

    p = glCreateProgram();

    printf("compileGLSLprogram() 1\n");

    if (fragment_shader_src)
    {
        printf("compileGLSLprogram() 3\n");
        f = glCreateShader(GL_FRAGMENT_SHADER);
        glShaderSource(f, 1, &fragment_shader_src, NULL);
        glCompileShader(f);

        // check if shader compiled
        GLint compiled = 0;
        glGetShaderiv(f, GL_COMPILE_STATUS, &compiled);

        printf("compileGLSLprogram() 3b\n");
        glAttachShader(p, f);
    }

    glLinkProgram(p);

    GLint linked = 0;
    glGetProgramiv(p, GL_LINK_STATUS, &linked);

    printf("compileGLSLprogram() 4\n");

    return p;
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
    // createRenderBuffer(&tex_screen, image_width, image_height); // Doesn't work

    // create a depth buffer for offscreen rendering
    createDepthBuffer(&depth_buffer, image_width, image_height);

    // create a framebuffer for offscreen rendering
    createFramebuffer(&framebuffer, tex_screen, depth_buffer);

    printf("initGLBuffers() 2\n");

    // load shader programs
    shDrawPot = compileGLSLprogram(NULL, glsl_drawpot_fragshader_src);
}

bool initGL(int* argc, char** argv)
{
    // Create GL context
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(window_width, window_height);
    iGLUTWindowHandle = glutCreateWindow("CUDA OpenGL post-processing");

    glewInit();

    // default initialization
    glClearColor(0.5, 0.5, 0.5, 1.0);
    glDisable(GL_DEPTH_TEST);

    // viewport
    glViewport(0, 0, window_width, window_height);

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

    if (false == initGL(&argc, argv))
    {
        return 0;
    }

    // Now initialize CUDA context
    findCudaDevice(argc, (const char**)argv);

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);

    initGLBuffers();

    glutMainLoop();	//開始主循環繪製

    return 0;
}

