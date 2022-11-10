/*
** abgr.c - Demonstrates the use of the extension EXT_abgr.
**
** The same image data is used for both ABGR and RGBA formats
** in glDrawPixels and glTexImage2D.  The left side uses ABGR,
** the right side RGBA.  The top polygon demonstrates use of texture,
** and the bottom image is drawn with glDrawPixels.
**
** Note that the textures are defined as 3 component, so the alpha
** value is not used in applying the DECAL environment.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#if defined(GL_EXT_abgr)

GLubyte ubImage[65536];

void Init(void)
{
    int i, j;
    GLubyte* img;
    GLsizei imgWidth = 128;

    glDisable(GL_DITHER);

    /* Create image */
    img = ubImage;
    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0x00;
        *img++ = 0xff;
    }

    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0xff;
        *img++ = 0x00;
    }

    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0xff;
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0x00;
    }

    for (j = 0; j < 32 * imgWidth; j++)
    {
        *img++ = 0x00;
        *img++ = 0xff;
        *img++ = 0x00;
        *img++ = 0xff;
    }
}

void reshape(int width, int height)
{
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(60.0, 1.0, 0.1, 1000.0);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int /*x*/, int /*y*/)
{
    switch (key)
    {
    case 27:
        exit(0);
    }
}

void TexFunc(void)
{
    GLenum err;

    glTexImage2D(GL_TEXTURE_2D, 0, 3, 128, 128, 0, GL_ABGR_EXT, GL_UNSIGNED_BYTE, ubImage);

    err = glGetError();
    if (err)
    {
        printf("err %d\n", err);
    }

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    err = glGetError();
    if (err)
    {
        printf("err %d\n", err);
    }

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL);
    glEnable(GL_TEXTURE_2D);	//啟用2D紋理映射

    glBegin(GL_POLYGON);
    glTexCoord2f(1.0, 1.0); glVertex3f(-0.2, 0.8, -100.0);
    glTexCoord2f(0.0, 1.0); glVertex3f(-0.8, 0.8, -2.0);
    glTexCoord2f(0.0, 0.0); glVertex3f(-0.8, 0.2, -2.0);
    glTexCoord2f(1.0, 0.0); glVertex3f(-0.2, 0.2, -100.0);
    glEnd();

    glTexImage2D(GL_TEXTURE_2D, 0, 3, 128, 128, 0, GL_RGBA, GL_UNSIGNED_BYTE, ubImage);

    glBegin(GL_POLYGON);
    glTexCoord2f(1.0, 1.0); glVertex3f(0.8, 0.8, -2.0);
    glTexCoord2f(0.0, 1.0); glVertex3f(0.2, 0.8, -100.0);
    glTexCoord2f(0.0, 0.0); glVertex3f(0.2, 0.2, -100.0);
    glTexCoord2f(1.0, 0.0); glVertex3f(0.8, 0.2, -2.0);
    glEnd();

    glDisable(GL_TEXTURE_2D);
    err = glGetError();
    if (err)
    {
        printf("err %d\n", err);
    }
}

void Draw(void)
{

    glClearColor(0.0, 0.0, 0.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);

    glRasterPos3f(-0.8, -0.8, -1.5);
    glDrawPixels(128, 128, GL_ABGR_EXT, GL_UNSIGNED_BYTE, ubImage);

    glRasterPos3f(0.2, -0.8, -1.5);
    glDrawPixels(128, 128, GL_RGBA, GL_UNSIGNED_BYTE, ubImage);

    TexFunc();

    glFlush();
}

GLboolean QueryExtension(char* extName)
{
    /*
    ** Search for extName in the extensions string. Use of strstr()
    ** is not sufficient because extension names can be prefixes of
    ** other extension names. Could use strtok() but the constant
    ** string returned by glGetString can be in read-only memory.
    */
    char* p = (char*)glGetString(GL_EXTENSIONS);
    char* end = p + strlen(p);
    while (p < end)
    {
        int n = strcspn(p, " ");
        if ((strlen(extName) == n) && (strncmp(extName, p, n) == 0))
        {
            return GL_TRUE;
        }
        p += (n + 1);
    }
    return GL_FALSE;
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);

    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
    glutInitWindowSize(400, 400);

    glutCreateWindow("ABGR extension");	//開啟視窗 並顯示出視窗 Title

    if (!QueryExtension("GL_EXT_abgr"))
    {
        printf("Couldn't find ABGR extension.\n");
        exit(0);
    }

    Init();

    glutDisplayFunc(Draw);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);

    glutMainLoop();	//開始主循環繪製

    return 0;
}

#else

int main(int argc, char** argv)
{
    printf("Couldn't find GL_EXT_abgr extension.\n");
}

#endif
