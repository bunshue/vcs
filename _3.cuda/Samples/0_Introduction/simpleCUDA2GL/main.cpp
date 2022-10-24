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

// Shared Library Test Functions
#define MAX_EPSILON 10
#define REFRESH_DELAY 10  // ms

unsigned int g_TotalErrors = 0;

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

GLuint fbo_source;
struct cudaGraphicsResource* cuda_tex_screen_resource;

unsigned int size_tex_data;
unsigned int num_texels;
unsigned int num_values;

// (offscreen) render target fbo variables
GLuint tex_screen;      // where we render the image
GLuint tex_cudaResult;  // where we will copy the CUDA result

// Timer
static int fpsCount = 0;
static int fpsLimit = 1;
StopWatchInterface* timer = NULL;

////////////////////////////////////////////////////////////////////////////////
extern "C" void launch_cudaProcess(dim3 grid, dim3 block, int sbytes, unsigned int* g_odata, int imgw);

void FreeResource();
void Cleanup(int iExitCode);

// GL functionality
bool initGL(int* argc, char** argv);

void createPBO(GLuint* pbo, struct cudaGraphicsResource** pbo_resource);
void deletePBO(GLuint* pbo);

void createTextureDst(GLuint* tex_cudaResult, unsigned int size_x, unsigned int size_y);
void deleteTexture(GLuint* tex);

// rendering callbacks
void display();
void idle();
void keyboard(unsigned char key, int x, int y);
void reshape(int w, int h);
void mainMenu(int i);

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

    SDK_CHECK_ERROR_GL();
}

void deletePBO(GLuint* pbo)
{
    glDeleteBuffers(1, pbo);
    SDK_CHECK_ERROR_GL();
    *pbo = 0;
}

const GLenum fbo_targets[] = {
    GL_COLOR_ATTACHMENT0_EXT, GL_COLOR_ATTACHMENT1_EXT,
    GL_COLOR_ATTACHMENT2_EXT, GL_COLOR_ATTACHMENT3_EXT };

// copy image and process using CUDA
void generateCUDAImage()
{
    // run the Cuda kernel
    unsigned int* out_data;

    checkCudaErrors(cudaGraphicsMapResources(1, &cuda_pbo_dest_resource, 0));
    size_t num_bytes;
    checkCudaErrors(cudaGraphicsResourceGetMappedPointer((void**)&out_data, &num_bytes, cuda_pbo_dest_resource));
    //printf("CUDA mapped pointer of pbo_out: May access %ld bytes, expected %d\n", num_bytes, size_tex_data);

    // calculate grid size
    dim3 block(16, 16, 1);
    dim3 grid(image_width / block.x, image_height / block.y, 1);
    // execute CUDA kernel

    //printf("num_bytes = %d\n", num_bytes);    //1048576
    //printf("image_width = %d\n", image_width);    //512

    //printf("image_width = %d\timage_height = %d\n", image_width, image_height); //512 X 512
    //printf("block.x = %d\tblock.y = %d\n", block.x, block.y);   //16, 16
    launch_cudaProcess(grid, block, 0, out_data, image_width);

    // CUDA generated data in cuda memory or in a mapped PBO made of BGRA 8 bits
    // 2 solutions, here :
    // - use glTexSubImage2D(), there is the potential to loose performance in
    // possible hidden conversion
    // - map the texture and blit the result thanks to CUDA API

    checkCudaErrors(cudaGraphicsUnmapResources(1, &cuda_pbo_dest_resource, 0));
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, pbo_dest);

    glBindTexture(GL_TEXTURE_2D, tex_cudaResult);	//綁定紋理
    glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, image_width, image_height, GL_RGBA, GL_UNSIGNED_BYTE, NULL);
    SDK_CHECK_ERROR_GL();
    glBindBuffer(GL_PIXEL_PACK_BUFFER_ARB, 0);
    glBindBuffer(GL_PIXEL_UNPACK_BUFFER_ARB, 0);
}

// display image to the screen as textured quad
void displayImage(GLuint texture)
{
    glBindTexture(GL_TEXTURE_2D, texture);	//綁定紋理
    glEnable(GL_TEXTURE_2D);
    glDisable(GL_DEPTH_TEST);
    glDisable(GL_LIGHTING);
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);

    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();	//設置單位矩陣
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣

    glViewport(0, 0, window_width, window_height);

    glBegin(GL_QUADS);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, -1.0, 0.5);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, -1.0, 0.5);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, 0.5);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, 0.5);
    glEnd();

    glMatrixMode(GL_PROJECTION);
    glPopMatrix();

    glDisable(GL_TEXTURE_2D);

    SDK_CHECK_ERROR_GL();
}

////////////////////////////////////////////////////////////////////////////////
//! Display callback
////////////////////////////////////////////////////////////////////////////////
void display()
{
    sdkStartTimer(&timer);

    generateCUDAImage();
    displayImage(tex_cudaResult);

    // NOTE: I needed to add this call so the timing is consistent.
    // Need to investigate why
    cudaDeviceSynchronize();
    sdkStopTimer(&timer);

    // flip backbuffer
    glutSwapBuffers();

    // Update fps counter, fps/title display and log
    //只在程式啟動時做一次
    if (++fpsCount == fpsLimit)
    {
        char cTitle[256];
        float fps = 1000.0f / sdkGetAverageTimerValue(&timer);
        sprintf(cTitle, "CUDA GL Post Processing (%d x %d): %.1f fps", window_width, window_height, fps);
        glutSetWindowTitle(cTitle);
        // printf("%s\n", cTitle);
        fpsCount = 0;
        fpsLimit = (int)((fps > 1.0f) ? fps : 1.0f);
        sdkResetTimer(&timer);
    }
}

void timerEvent(int value)
{
    glutPostRedisplay();
    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);
}

////////////////////////////////////////////////////////////////////////////////
//! Keyboard events handler
////////////////////////////////////////////////////////////////////////////////
void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case (27):
        Cleanup(EXIT_SUCCESS);
        break;

    case ' ':
        printf("space ");
        break;
    }
}

void reshape(int w, int h)
{
    window_width = w;
    window_height = h;
    //printf("w = %d, h = %d ", w, h);
}

void mainMenu(int i) { keyboard((unsigned char)i, 0, 0); }

////////////////////////////////////////////////////////////////////////////////
//!
////////////////////////////////////////////////////////////////////////////////
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
    SDK_CHECK_ERROR_GL();
}

void deleteTexture(GLuint* tex)
{
    glDeleteTextures(1, tex);
    SDK_CHECK_ERROR_GL();

    *tex = 0;
}

////////////////////////////////////////////////////////////////////////////////
//!
////////////////////////////////////////////////////////////////////////////////
void FreeResource()
{
    printf("離開程式時, FreeResource\n");

    sdkDeleteTimer(&timer);

    // unregister this buffer object with CUDA
    //    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_tex_screen_resource));
    checkCudaErrors(cudaGraphicsUnregisterResource(cuda_pbo_dest_resource));
    deletePBO(&pbo_dest);
    deleteTexture(&tex_screen);
    deleteTexture(&tex_cudaResult);

    if (iGLUTWindowHandle)
    {
        glutDestroyWindow(iGLUTWindowHandle);
    }

    // finalize logs and leave
    printf("simpleCUDA2GL Exiting...\n");
}

void Cleanup(int iExitCode)
{
    FreeResource();
    printf("PPM Images are %s\n", (iExitCode == EXIT_SUCCESS) ? "Matching" : "Not Matching");
    exit(iExitCode);
}

void initGLBuffers()
{
    // create pbo
    createPBO(&pbo_dest, &cuda_pbo_dest_resource);

    // create texture that will receive the result of CUDA
    createTextureDst(&tex_cudaResult, image_width, image_height);

    SDK_CHECK_ERROR_GL();
}

////////////////////////////////////////////////////////////////////////////////
//! Initialize GL
////////////////////////////////////////////////////////////////////////////////
bool initGL(int* argc, char** argv)
{
    // Create GL context
    printf("argc = %d, argv = %s\n\n", *argc, argv[0]);
    glutInit(argc, argv);
    glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH);
    printf("window_width = %d, window_height = %d\n", window_width, window_height);
    glutInitWindowSize(window_width, window_height);
    glutInitWindowPosition(1100, 200);

    iGLUTWindowHandle = glutCreateWindow("CUDA OpenGL post-processing");

    //以下為必要
    // initialize necessary OpenGL extensions
    if (!isGLVersionSupported(2, 0) || !areGLExtensionsSupported("GL_ARB_pixel_buffer_object GL_EXT_framebuffer_object"))
    {
        printf("ERROR: Support for necessary OpenGL extensions missing.");
        fflush(stderr);
        return false;
    }

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

    SDK_CHECK_ERROR_GL();

    return true;
}

int main(int argc, char** argv)
{
    printf("(Interactive OpenGL Demo)\n");

    // First initialize OpenGL context, so we can properly set the GL for CUDA.
    // This is necessary in order to achieve optimal performance with OpenGL/CUDA interop.
    if (false == initGL(&argc, argv))
    {
        return 0;
    }

    // Now initialize CUDA context (GL context has been created already)
    findCudaDevice(argc, (const char**)argv);

    sdkCreateTimer(&timer);
    sdkResetTimer(&timer);

    glutDisplayFunc(display);       //設定callback function
    glutReshapeFunc(reshape);       //設定callback function
    glutKeyboardFunc(keyboard);     //設定callback function

    glutTimerFunc(REFRESH_DELAY, timerEvent, 0);

    // create menu
    glutCreateMenu(mainMenu);
    glutAddMenuEntry("Quit (esc)", '\033');
    glutAttachMenu(GLUT_RIGHT_BUTTON);

    initGLBuffers();

    printf("按滑鼠右鍵 或 ESC 結束\n\n");

    // start rendering mainloop
    glutMainLoop();

    // Normally unused return path
    Cleanup(EXIT_SUCCESS);

    exit(EXIT_SUCCESS);
}

