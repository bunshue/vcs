/*  texgen.c
 *  This program draws a texture mapped teapot with
 *  automatically generated texture coordinates.  The
 *  texture is rendered as stripes on the teapot.
 */

#include "../../Common.h"

#define	ImageWidth 64
#define ImageLength 64

 // Define targa header.
#pragma pack(1)
typedef struct
{
    GLbyte	identsize;              // Size of ID field that follows header (0)
    GLbyte	colorMapType;           // 0 = None, 1 = paletted
    GLbyte	imageType;              // 0 = none, 1 = indexed, 2 = rgb, 3 = grey, +8=rle
    unsigned short	colorMapStart;  // First colour map entry
    unsigned short	colorMapLength; // Number of colors
    unsigned char 	colorMapBits;   // bits per palette entry
    unsigned short	xstart;         // image x origin
    unsigned short	ystart;         // image y origin
    unsigned short	width;          // width in pixels
    unsigned short	height;         // height in pixels
    GLbyte	bits;                   // bits per pixel (8 16, 24, 32)
    GLbyte	descriptor;             // image descriptor
} TGAHEADER;
#pragma pack(8)

GLubyte Image[ImageLength][ImageWidth][3];

int image_type = 1;     //1 : 線條的, 2: 圖片的

/* glTexGen stuff */
GLfloat sgenparams[] = { 1.0, 0.0, 0.0, 0.0 };
GLfloat tgenparams[] = { 0.0, 0.0, 1.0, 0.0 };

void makeImage(void)
{
    printf("makeImage,  W = %d, H = %d\n", ImageWidth, ImageLength);
    int i, j, w2, l2, cond;

    w2 = ImageWidth >> 2;
    l2 = ImageLength >> 2;
    for (i = 0; i < ImageLength; i++)
    {
        for (j = 0; j < ImageWidth; j++)
        {
            cond = (i < l2) || (j < w2);
            Image[i][j][0] = cond ? 255 : 0;
            Image[i][j][1] = (!cond) ? 255 : 0;
            Image[i][j][2] = 0;

            /* debug 顯示單一色
            Image[i][j][0] = 255;
            Image[i][j][1] = 0;
            Image[i][j][2] = 0;
            */
        }
    }
}

////////////////////////////////////////////////////////////////////
// Allocate memory and load targa bits. Returns pointer to new buffer,
// height, and width of texture, and the OpenGL format of data.
// Call free() on buffer when finished!
// This only works on pretty vanilla targas... 8, 24, or 32 bit color
// only, no palettes, no RLE encoding.
GLbyte* gltLoadTGA(const char* szFileName, GLint* iWidth, GLint* iHeight, GLint* iComponents, GLenum* eFormat)
{
    FILE* pFile;			// File pointer
    TGAHEADER tgaHeader;		// TGA file header
    unsigned long lImageSize;		// Size in bytes of image
    short sDepth;			// Pixel depth;
    GLbyte* pBits = NULL;          // Pointer to bits

    // Default/Failed values
    *iWidth = 0;
    *iHeight = 0;
    *eFormat = GL_BGR_EXT;
    *iComponents = GL_RGB8;

    // Attempt to open the file
    fopen_s(&pFile, szFileName, "rb");
    if (pFile == NULL)
    {
        printf("XXXXXX 1 無此檔案\n");
        return NULL;
    }

    // Read in header (binary)
    fread(&tgaHeader, 18/* sizeof(TGAHEADER)*/, 1, pFile);

    // Get width, height, and depth of texture
    *iWidth = tgaHeader.width;
    *iHeight = tgaHeader.height;
    sDepth = tgaHeader.bits / 8;

    // Put some validity checks here. Very simply, I only understand
    // or care about 8, 24, or 32 bit targa's.
    if (tgaHeader.bits != 8 && tgaHeader.bits != 24 && tgaHeader.bits != 32)
    {
        printf("XXXXXX 2\n");
        return NULL;
    }

    // Calculate size of image buffer
    lImageSize = tgaHeader.width * tgaHeader.height * sDepth;
    printf("gltLoadTGA, W = %d, H = %d, Size = %d\n", tgaHeader.width, tgaHeader.height, lImageSize);

    // Allocate memory and check for success
    pBits = (GLbyte*)malloc(lImageSize * sizeof(GLbyte));
    if (pBits == NULL)
    {
        printf("XXXXXX 3\n");
        return NULL;
    }

    // Read in the bits
    // Check for read error. This should catch RLE or other 
    // weird formats that I don't want to recognize
    if (fread(pBits, lImageSize, 1, pFile) != 1)
    {
        printf("XXXXXX 4\n");
        free(pBits);
        return NULL;
    }

    // Set OpenGL format expected
    switch (sDepth)
    {
    case 3:     // Most likely case
        *eFormat = GL_BGR_EXT;
        *iComponents = GL_RGB8;
        break;
    case 4:
        *eFormat = GL_BGRA_EXT;
        *iComponents = GL_RGBA8;
        break;
    case 1:
        *eFormat = GL_LUMINANCE;
        *iComponents = GL_LUMINANCE8;
        break;
    };

    // Done with File
    fclose(pFile);

    // Return pointer to image data
    return pBits;
}

void gfxinit(void)
{
    GLubyte* pBytes;
    GLint iWidth, iHeight, iComponents;
    GLenum eFormat;

    // Light values and coordinates
    GLfloat  whiteLight[] = { 0.05f, 0.05f, 0.05f, 1.0f };
    GLfloat  sourceLight[] = { 0.5f, 0.5f, 0.5f, 1.0f };
    GLfloat	 lightPos[] = { 0.0f, 0.0f, 5.0f, 1.0f };

    glClearColor(1.0, 1.0, 0.0, 0.0);		//設定背景顏色

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LESS);
    glEnable(GL_TEXTURE_2D);
    glEnable(GL_CULL_FACE);
    glEnable(GL_LIGHTING);
    glEnable(GL_AUTO_NORMAL);
    glEnable(GL_NORMALIZE);
    glFrontFace(GL_CW);
    glCullFace(GL_BACK);
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);

    // Setup and enable light 0
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, whiteLight);
    glLightfv(GL_LIGHT0, GL_AMBIENT, sourceLight);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, sourceLight);
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos);
    glEnable(GL_LIGHT0);

    // Enable color tracking
    glEnable(GL_COLOR_MATERIAL);

    // Set material properties to follow glColor values
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);

    //在 List 1 製作第1張圖   //線條的茶壺
    makeImage();
    glNewList(1, GL_COMPILE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ImageLength, ImageWidth, 0, GL_RGB, GL_UNSIGNED_BYTE, Image);

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR);
    glTexGenfv(GL_S, GL_OBJECT_PLANE, sgenparams);
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR);
    glTexGenfv(GL_T, GL_OBJECT_PLANE, tgenparams);

    glEnable(GL_TEXTURE_GEN_S);
    glEnable(GL_TEXTURE_GEN_T);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glRotatef(30.0, 0.0, 0.0, 1.0);   //逆時針旋轉30度
    glutSolidTeapot(2.0);
    glDisable(GL_TEXTURE_GEN_S);
    glDisable(GL_TEXTURE_GEN_T);
    glEndList();

    //在 List 2 製作第2張圖   //圖片的茶壺
    glNewList(2, GL_COMPILE);
    pBytes = (GLubyte*)gltLoadTGA("data/14.marble.tga", &iWidth, &iHeight, &iComponents, &eFormat);
    printf("pBytes = %p\n", pBytes);
    if (pBytes == NULL)
    {
        printf("開啟tga圖檔失敗\n");
    }

    //試著修改圖片內容
    //memset(pBytes, 0, sizeof(GLubyte) * 128*128);   //给*p指定的前100字节大小的内存空间设置为(只支持0, 1，以字节为单位赋初始值)

    glTexImage2D(GL_TEXTURE_2D, 0, iComponents, iWidth, iHeight, 0, eFormat, GL_UNSIGNED_BYTE, pBytes);
    free(pBytes);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glutSolidTeapot(2.0);
    glEndList();
}

/* The display callback function. */
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    if (image_type == 1)    //線條的
    {
        glCallList(1);  //顯示第1張圖
    }
    else if (image_type == 2)    //圖片的
    {
        glCallList(2);  //顯示第2張圖
    }
    glFlush();  // 執行繪圖命令
}

void reshape(int w, int h)
{
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    if (w <= h)
    {
        glOrtho(-3.5, 3.5, -3.5 * (GLfloat)h / (GLfloat)w, 3.5 * (GLfloat)h / (GLfloat)w, -3.5, 3.5);
    }
    else
    {
        glOrtho(-3.5 * (GLfloat)w / (GLfloat)h, 3.5 * (GLfloat)w / (GLfloat)h, -3.5, 3.5, -3.5, 3.5);
    }
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
        glutDestroyWindow(glutGetWindow());
        return;
        break;
    case '1':
        image_type = 1;  //線條的
        break;
    case '2':
        image_type = 2;  //圖片的
        break;
    }
    glutPostRedisplay();    //將當前視窗打上標記，標記其需要再次顯示。
}

int main(int argc, char** argv)
{
    const char* windowName = "Texture Generation";
    const char* message = "按 1 2 切換, 按 Esc 離開\n";
    common_setup(argc, argv, windowName, message, 0, 600, 600, 1100, 200, display, reshape, keyboard);

    //先保留
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);

    gfxinit();

    glutMainLoop();	//開始主循環繪製

    return 0;
}


