#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

//#include <GL/glut.h>      //32 bits
#include <GL/freeglut.h>    //64 bits

#include "rgb.h"

typedef struct _rawImageRec {
    unsigned short imagic;
    unsigned short type;
    unsigned short dim;
    unsigned short sizeX, sizeY, sizeZ;
    unsigned long min, max;
    unsigned long wasteBytes;
    char name[80];
    unsigned long colorMap;
    FILE* file;
    unsigned char* tmp, * tmpR, * tmpG, * tmpB;
    unsigned long rleEnd;
    GLuint* rowStart;
    GLint* rowSize;
} rawImageRec;

void ConvertShort(unsigned short* array, long length)
{
    unsigned long b1, b2;
    unsigned char* ptr;

    ptr = (unsigned char*)array;
    while (length--)
    {
        b1 = *ptr++;
        b2 = *ptr++;
        *array++ = (unsigned short)((b1 << 8) | (b2));
    }
}

void ConvertLong(GLuint* array, long length)
{
    unsigned long b1, b2, b3, b4;
    unsigned char* ptr;

    ptr = (unsigned char*)array;
    while (length--)
    {
        b1 = *ptr++;
        b2 = *ptr++;
        b3 = *ptr++;
        b4 = *ptr++;
        *array++ = (b1 << 24) | (b2 << 16) | (b3 << 8) | (b4);
    }
}

rawImageRec* RawImageOpen(char* fileName)
{
    union {
        int testWord;
        char testByte[4];
    } endianTest;
    rawImageRec* raw;
    GLenum swapFlag;
    int x;

    endianTest.testWord = 1;
    if (endianTest.testByte[0] == 1)
    {
        swapFlag = GL_TRUE;
    }
    else
    {
        swapFlag = GL_FALSE;
    }

    raw = (rawImageRec*)malloc(sizeof(rawImageRec));
    if (raw == NULL)
    {
        return NULL;
    }

    errno_t err;
    err = fopen_s(&(raw->file), fileName, "rb");
    if (err == 0)
    {
        printf("The file %s was opened\n", fileName);
    }
    else
    {
        printf("The file %s was not opened\n", fileName);
        return NULL;
    }

    /* old
    if ((raw->file = fopen_s(fileName, "rb")) == NULL)
    {
        return NULL;
    }
    */

    fread(raw, 1, 12, raw->file);

    if (swapFlag)
    {
        ConvertShort(&raw->imagic, 6);
    }

    raw->tmp = (unsigned char*)malloc(raw->sizeX * 256);
    raw->tmpR = (unsigned char*)malloc(raw->sizeX * 256);
    raw->tmpG = (unsigned char*)malloc(raw->sizeX * 256);
    raw->tmpB = (unsigned char*)malloc(raw->sizeX * 256);
    if (raw->tmp == NULL || raw->tmpR == NULL || raw->tmpG == NULL || raw->tmpB == NULL)
    {
        return NULL;
    }

    if ((raw->type & 0xFF00) == 0x0100)
    {
        x = raw->sizeY * raw->sizeZ * sizeof(GLuint);
        raw->rowStart = (GLuint*)malloc(x);
        raw->rowSize = (GLint*)malloc(x);
        if (raw->rowStart == NULL || raw->rowSize == NULL)
        {
            return NULL;
        }
        raw->rleEnd = 512 + (2 * x);
        fseek(raw->file, 512, SEEK_SET);
        fread(raw->rowStart, 1, x, raw->file);
        fread(raw->rowSize, 1, x, raw->file);
        if (swapFlag)
        {
            ConvertLong(raw->rowStart, x / sizeof(GLuint));
            ConvertLong((GLuint*)raw->rowSize, x / sizeof(GLint));
        }
    }
    return raw;
}

void RawImageClose(rawImageRec* raw)
{
    fclose(raw->file);
    free(raw->tmp);
    free(raw->tmpR);
    free(raw->tmpG);
    free(raw->tmpB);
    free(raw->rowStart);
    free(raw->rowSize);
    free(raw);
}

void RawImageGetRow(rawImageRec* raw, unsigned char* buf, int y, int z)
{
    unsigned char* iPtr, * oPtr, pixel;
    int count;

    if ((raw->type & 0xFF00) == 0x0100)
    {
        fseek(raw->file, raw->rowStart[y + z * raw->sizeY], SEEK_SET);
        fread(raw->tmp, 1, (unsigned int)raw->rowSize[y + z * raw->sizeY], raw->file);

        iPtr = raw->tmp;
        oPtr = buf;
        while (1)
        {
            pixel = *iPtr++;
            count = (int)(pixel & 0x7F);
            if (!count)
            {
                return;
            }
            if (pixel & 0x80)
            {
                while (count--)
                {
                    *oPtr++ = *iPtr++;
                }
            }
            else
            {
                pixel = *iPtr++;
                while (count--)
                {
                    *oPtr++ = pixel;
                }
            }
        }
    }
    else
    {
        fseek(raw->file, 512 + (y * raw->sizeX) + (z * raw->sizeX * raw->sizeY), SEEK_SET);
        fread(buf, 1, raw->sizeX, raw->file);
    }
}

void RawImageGetData(rawImageRec* raw, RGBImageRec* final)
{
    unsigned char* ptr;
    int i, j;

    final->data = (unsigned char*)malloc((raw->sizeX + 1) * (raw->sizeY + 1) * 4);
    if (final->data == NULL)
    {
        return;
    }

    ptr = final->data;
    for (i = 0; i < raw->sizeY; i++)
    {
        RawImageGetRow(raw, raw->tmpR, i, 0);
        RawImageGetRow(raw, raw->tmpG, i, 1);
        RawImageGetRow(raw, raw->tmpB, i, 2);
        for (j = 0; j < raw->sizeX; j++)
        {
            *ptr++ = *(raw->tmpR + j);
            *ptr++ = *(raw->tmpG + j);
            *ptr++ = *(raw->tmpB + j);
        }
    }
}

RGBImageRec* rgbImageLoad(char* fileName)
{
    rawImageRec* raw;
    RGBImageRec* final;

    raw = RawImageOpen(fileName);
    if (raw == NULL)
    {
        return NULL;
    }

    final = (RGBImageRec*)malloc(sizeof(RGBImageRec));
    if (final == NULL)
    {
        RawImageClose(raw);
        return NULL;
    }
    final->sizeX = raw->sizeX;
    final->sizeY = raw->sizeY;

    RawImageGetData(raw, final);
    RawImageClose(raw);

    return final;
}
