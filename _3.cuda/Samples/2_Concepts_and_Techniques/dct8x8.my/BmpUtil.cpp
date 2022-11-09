/**
**************************************************************************
* \file BmpUtil.cpp
* \brief Contains basic image operations implementation.
*
* This file contains implementation of basic bitmap loading, saving,
* conversions to different representations and memory management routines.
*/

#include "Common.h"
#include "BmpUtil.h"

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
#pragma warning(disable : 4996)  // disable deprecated warning
#endif

/**
**************************************************************************
*  The routine clamps the input value to integer byte range [0, 255]
*
* \param x          [IN] - Input value
*
* \return Pointer to the created plane
*/
int clamp_0_255(int x) { return (x < 0) ? 0 : ((x > 255) ? 255 : x); }

/**
**************************************************************************
*  Float round to nearest value
*
* \param num            [IN] - Float value to round
*
* \return The closest to the input float integer value
*/
float round_f(float num)
{
  float NumAbs = fabs(num);
  int NumAbsI = (int)(NumAbs + 0.5f);
  float sign = num > 0 ? 1.0f : -1.0f;
  return sign * NumAbsI;
}

/**
**************************************************************************
*  Memory allocator, returns aligned format frame with 8bpp pixels.
*
* \param width          [IN] - Width of image buffer to be allocated
* \param height         [IN] - Height of image buffer to be allocated
* \param pStepBytes     [OUT] - Step between two sequential rows
*
* \return Pointer to the created plane
*/
byte *MallocPlaneByte(int width, int height, int *pStepBytes)
{
  byte *ptr;
  *pStepBytes = ((int)ceil(width / 16.0f)) * 16;
  //#ifdef __ALLOW_ALIGNED_MEMORY_MANAGEMENT
  //  ptr = (byte *)_aligned_malloc(*pStepBytes * height, 16);
  //#else
  ptr = (byte *)malloc(*pStepBytes * height);
  //#endif
  printf("MallocPlaneByte, width = %d, strides = %d\n", width, *pStepBytes);
  return ptr;
}

/**
**************************************************************************
*  Memory allocator, returns aligned format frame with 16bpp float pixels.
*
* \param width          [IN] - Width of image buffer to be allocated
* \param height         [IN] - Height of image buffer to be allocated
* \param pStepBytes     [OUT] - Step between two sequential rows
*
* \return Pointer to the created plane
*/
short *MallocPlaneShort(int width, int height, int *pStepBytes) {
  short *ptr;
  *pStepBytes = ((int)ceil((width * sizeof(short)) / 16.0f)) * 16;
  //#ifdef __ALLOW_ALIGNED_MEMORY_MANAGEMENT
  //  ptr = (float *)_aligned_malloc(*pStepBytes * height, 16);
  //#else
  ptr = (short *)malloc(*pStepBytes * height);
  //#endif
  *pStepBytes = *pStepBytes / sizeof(short);
  return ptr;
}

/**
**************************************************************************
*  Memory allocator, returns aligned format frame with 32bpp float pixels.
*
* \param width          [IN] - Width of image buffer to be allocated
* \param height         [IN] - Height of image buffer to be allocated
* \param pStepBytes     [OUT] - Step between two sequential rows
*
* \return Pointer to the created plane
*/
float* MallocPlaneFloat(int width, int height, int* pStepBytes)
{
  float *ptr;
  *pStepBytes = ((int)ceil((width * sizeof(float)) / 16.0f)) * 16;
  //#ifdef __ALLOW_ALIGNED_MEMORY_MANAGEMENT
  //  ptr = (float *)_aligned_malloc(*pStepBytes * height, 16);
  //#else
  ptr = (float *)malloc(*pStepBytes * height);
  //#endif
  *pStepBytes = *pStepBytes / sizeof(float);
  return ptr;
}

/**
**************************************************************************
*  Copies byte plane to float plane
*
* \param ImgSrc             [IN] - Source byte plane
* \param StrideB            [IN] - Source plane stride
* \param ImgDst             [OUT] - Destination float plane
* \param StrideF            [IN] - Destination plane stride
* \param Size               [IN] - Size of area to copy
*
* \return None
*/
void CopyByte2Float(byte* ImgSrc, int StrideB, float* ImgDst, int StrideF, ROI Size)
{
    for (int i = 0; i < Size.height; i++)
    {
        for (int j = 0; j < Size.width; j++)
        {
      ImgDst[i * StrideF + j] = (float)ImgSrc[i * StrideB + j];
    }
  }
}

/**
**************************************************************************
*  Copies float plane to byte plane (with clamp)
*
* \param ImgSrc             [IN] - Source float plane
* \param StrideF            [IN] - Source plane stride
* \param ImgDst             [OUT] - Destination byte plane
* \param StrideB            [IN] - Destination plane stride
* \param Size               [IN] - Size of area to copy
*
* \return None
*/
void CopyFloat2Byte(float* ImgSrc, int StrideF, byte* ImgDst, int StrideB, ROI Size)
{
    for (int i = 0; i < Size.height; i++)
    {
        for (int j = 0; j < Size.width; j++)
        {
            ImgDst[i * StrideB + j] = (byte)clamp_0_255((int)(round_f(ImgSrc[i * StrideF + j])));
    }
  }
}

/**
**************************************************************************
*  Memory deallocator, deletes aligned format frame.
*
* \param ptr            [IN] - Pointer to the plane
*
* \return None
*/
void FreePlane(void* ptr)
{
  //#ifdef __ALLOW_ALIGNED_MEMORY_MANAGEMENT
  //  if (ptr)
  //  {
  //      _aligned_free(ptr);
  //  }
  //#else
    if (ptr)
    {
    free(ptr);
  }

  //#endif
}

/**
**************************************************************************
*  Performs addition of given value to each pixel in the plane
*
* \param Value              [IN] - Value to add
* \param ImgSrcDst          [IN/OUT] - Source float plane
* \param StrideF            [IN] - Source plane stride
* \param Size               [IN] - Size of area to copy
*
* \return None
*/
void AddFloatPlane(float Value, float* ImgSrcDst, int StrideF, ROI Size)
{
    for (int i = 0; i < Size.height; i++)
    {
        for (int j = 0; j < Size.width; j++)
        {
      ImgSrcDst[i * StrideF + j] += Value;
    }
  }
}

/**
**************************************************************************
*  Performs multiplication of given value with each pixel in the plane
*
* \param Value              [IN] - Value for multiplication
* \param ImgSrcDst          [IN/OUT] - Source float plane
* \param StrideF            [IN] - Source plane stride
* \param Size               [IN] - Size of area to copy
*
* \return None
*/
void MulFloatPlane(float Value, float* ImgSrcDst, int StrideF, ROI Size)
{
    for (int i = 0; i < Size.height; i++)
    {
        for (int j = 0; j < Size.width; j++)
        {
      ImgSrcDst[i * StrideF + j] *= Value;
    }
  }
}

/**
**************************************************************************
*  This function performs acquisition of image dimensions
*
* \param FileName       [IN] - Image name to load
* \param Width          [OUT] - Image width from file header
* \param Height         [OUT] - Image height from file header
*
* \return Status code
*/
int PreLoadBmp(char *FileName, int *Width, int *Height)
{
  BMPFileHeader FileHeader;
  BMPInfoHeader InfoHeader;
  FILE *fh;

  if (!(fh = fopen(FileName, "rb")))
  {
    return 1;  // invalid filename
  }

  fread(&FileHeader, sizeof(BMPFileHeader), 1, fh);

  if (FileHeader._bm_signature != 0x4D42)
  {
    return 2;  // invalid file format
  }

  fread(&InfoHeader, sizeof(BMPInfoHeader), 1, fh);

  printf("圖片位元深度 : %d 位元\n", InfoHeader._bm_color_depth);

  if (InfoHeader._bm_color_depth != 24)
  {
    return 3;  // invalid color depth
  }

  if (InfoHeader._bm_compressed)
  {
    return 4;  // invalid compression property
  }

  *Width = InfoHeader._bm_image_width;
  *Height = InfoHeader._bm_image_height;

  fclose(fh);
  return 0;
}

int PreLoadBmp2(char* FileName, int* Width, int* Height)
{
    BMPFileHeader FileHeader;
    BMPInfoHeader InfoHeader;
    FILE* fh;

    //printf("PreLoadBmp2, filename : %s\n", FileName);

    if (!(fh = fopen(FileName, "rb")))
    {
        printf("xxxx 1\n");
        return 1;  // invalid filename
    }

    fread(&FileHeader, sizeof(BMPFileHeader), 1, fh);

    if (FileHeader._bm_signature != 0x4D42)
    {
        printf("xxxx 2\n");
        return 2;  // invalid file format
    }
    /*
    printf("_bm_signature = 0x%04x\n", FileHeader._bm_signature);
    printf("_bm_file_size = 0x%08x = %d\n", FileHeader._bm_file_size, FileHeader._bm_file_size);
    printf("_bm_reserved = 0x%04x\n", FileHeader._bm_reserved);
    printf("_bm_bitmap_data = 0x%04x\n", FileHeader._bm_bitmap_data);
    */

    fread(&InfoHeader, sizeof(BMPInfoHeader), 1, fh);

    /*
    printf("圖片位元深度 : %d 位元\n", InfoHeader._bm_color_depth);
    printf("InfoHeader._bm_color_depth = %d\n", InfoHeader._bm_color_depth);
    printf("InfoHeader._bm_info_header_size = %x\n", InfoHeader._bm_info_header_size);
    printf("InfoHeader._bm_image_width = %x\n", InfoHeader._bm_image_width);
    printf("InfoHeader._bm_image_height = %x\n", InfoHeader._bm_image_height);
    printf("InfoHeader._bm_num_of_planes = %x\n", InfoHeader._bm_num_of_planes);
    printf("InfoHeader._bm_color_depth = %x\n", InfoHeader._bm_color_depth);
    printf("InfoHeader._bm_compressed = %x\n", InfoHeader._bm_compressed);
    printf("InfoHeader._bm_bitmap_size = %x\n", InfoHeader._bm_bitmap_size);
    printf("InfoHeader._bm_hor_resolution = %x\n", InfoHeader._bm_hor_resolution);
    printf("InfoHeader._bm_ver_resolution = %x\n", InfoHeader._bm_ver_resolution);
    printf("InfoHeader._bm_num_colors_used = %x\n", InfoHeader._bm_num_colors_used);
    printf("InfoHeader._bm_num_important_colors = %x\n", InfoHeader._bm_num_important_colors);
    */

    if (InfoHeader._bm_compressed)
    {
        printf("xxxx 4\n");
        return 4;  // invalid compression property
    }

    *Width = InfoHeader._bm_image_width;
    *Height = InfoHeader._bm_image_height;

    fclose(fh);
    return 0;
}

int GetBmpColorDepth(char* FileName)
{
    BMPFileHeader FileHeader;
    BMPInfoHeader InfoHeader;
    FILE* fh;

    //printf("GetBmpColorDepth, filename : %s\n", FileName);

    if (!(fh = fopen(FileName, "rb")))
    {
        printf("xxxx 1\n");
        return 1;  // invalid filename
    }

    fread(&FileHeader, sizeof(BMPFileHeader), 1, fh);

    if (FileHeader._bm_signature != 0x4D42)
    {
        printf("xxxx 2\n");
        return 2;  // invalid file format
    }

    fread(&InfoHeader, sizeof(BMPInfoHeader), 1, fh);

    printf("圖片位元深度 : %d 位元\n", InfoHeader._bm_color_depth);

    fclose(fh);

    return InfoHeader._bm_color_depth;
}

/**
**************************************************************************
*  This function performs loading of bitmap luma
*
* \param FileName       [IN] - Image name to load
* \param Stride         [IN] - Image stride
* \param ImSize         [IN] - Image size
* \param Img            [OUT] - Prepared buffer
*
* \return None
*/

//僅支持位元深度24位元
void LoadBmpAsGray(char *FileName, int Stride, ROI ImSize, byte *Img)
{
  BMPFileHeader FileHeader;
  BMPInfoHeader InfoHeader;

  FILE *fh;

  /*
  printf("LoadBmpAsGray, filename : %s, stride = %d, W = %d, H = %d\n", FileName, Stride, ImSize.width, ImSize.height);

  printf("sizeof(FileHeader) = %d\n", sizeof(FileHeader));  // 14
  printf("sizeof(InfoHeader) = %d\n", sizeof(InfoHeader));  // 40
  */

  fh = fopen(FileName, "rb");

  fread(&FileHeader, sizeof(BMPFileHeader), 1, fh);
  fread(&InfoHeader, sizeof(BMPInfoHeader), 1, fh);

  //printf("W = %d, H = %d\n", ImSize.width, ImSize.height);

  for (int j = 0; j < ImSize.height; j++)
  {
    for (int i = 0; i < ImSize.width; i++)
    {
      int r = 0, g = 0, b = 0;
      fread(&b, 1, 1, fh);
      fread(&g, 1, 1, fh);
      fread(&r, 1, 1, fh);

      int val = (313524 * r + 615514 * g + 119537 * b + 524288) >> 20;
      Img[j * Stride + i] = (byte)clamp_0_255(val);
    }
  }

  fclose(fh);
  return;
}

void LoadBmpAsData(char* FileName, int Stride, ROI ImSize, byte* Img, int color_depth)
{
    BMPFileHeader FileHeader;
    BMPInfoHeader InfoHeader;

    FILE* fh;

    /*
    printf("LoadBmpAsGray, filename : %s, stride = %d, W = %d, H = %d\n", FileName, Stride, ImSize.width, ImSize.height);
    printf("sizeof(FileHeader) = %d\n", sizeof(FileHeader));  // 14
    printf("sizeof(InfoHeader) = %d\n", sizeof(InfoHeader));  // 40
    */

    fh = fopen(FileName, "rb");

    fread(&FileHeader, sizeof(BMPFileHeader), 1, fh);
    fread(&InfoHeader, sizeof(BMPInfoHeader), 1, fh);

    //printf("W = %d, H = %d\n", ImSize.width, ImSize.height);

    for (int j = 0; j < ImSize.height; j++)
    {
        for (int i = 0; i < ImSize.width; i++)
        {
            int r = 0, g = 0, b = 0, a = 0;
            fread(&b, 1, 1, fh);
            fread(&g, 1, 1, fh);
            fread(&r, 1, 1, fh);
            if (color_depth == 32)
            {
                fread(&a, 1, 1, fh);
            }

            /*
            if (j == 0)
            {
                if (color_depth == 32)
                {
                    printf("[%02X %02X %02X %02X] ", b, g, r, a);
                    if ((i % 8) == 7)
                    {
                        printf("\n");
                    }
                }
            }
            */

            /*
            //int val = (313524 * r + 615514 * g + 119537 * b + 524288) >> 20;
            //Img[j * Stride + i] = (byte)clamp_0_255(val);

            Img[j * Stride + i + 0] = (byte)b;
            Img[j * Stride + i + 1] = (byte)g;
            Img[j * Stride + i + 2] = (byte)r;
            if (color_depth == 32)
            {
                Img[j * Stride + i + 3] = (byte)a;
            }
            */

            if (color_depth == 32)
            {
                Img[(i + j * ImSize.width) * 4 + 0] = (byte)b;
                Img[(i + j * ImSize.width) * 4 + 1] = (byte)g;
                Img[(i + j * ImSize.width) * 4 + 2] = (byte)r;
                Img[(i + j * ImSize.width) * 4 + 3] = (byte)a;
            }
            else
            {
                Img[(i + j * ImSize.width) * 3 + 0] = (byte)b;
                Img[(i + j * ImSize.width) * 3 + 1] = (byte)g;
                Img[(i + j * ImSize.width) * 3 + 2] = (byte)r;
            }
        }
    }
    fclose(fh);
    return;
}

/**
**************************************************************************
*  This function performs dumping of bitmap luma on HDD
*
* \param FileName       [OUT] - Image name to dump to
* \param Img            [IN] - Image luma to dump
* \param Stride         [IN] - Image stride
* \param ImSize         [IN] - Image size
*
* \return None
*/
void DumpBmpAsGray(char* FileName, byte* Img, int Stride, ROI ImSize)
{
    FILE* fp = NULL;
    fp = fopen(FileName, "wb");

    if (fp == NULL)
    {
        return;
    }

    BMPFileHeader FileHeader;
    BMPInfoHeader InfoHeader;

    // init headers
    FileHeader._bm_signature = 0x4D42;
    FileHeader._bm_file_size = 54 + 3 * ImSize.width * ImSize.height;
    FileHeader._bm_reserved = 0;
    FileHeader._bm_bitmap_data = 0x36;
    InfoHeader._bm_bitmap_size = 0;
    InfoHeader._bm_color_depth = 24;
    InfoHeader._bm_compressed = 0;
    InfoHeader._bm_hor_resolution = 0;
    InfoHeader._bm_image_height = ImSize.height;
    InfoHeader._bm_image_width = ImSize.width;
    InfoHeader._bm_info_header_size = 40;
    InfoHeader._bm_num_colors_used = 0;
    InfoHeader._bm_num_important_colors = 0;
    InfoHeader._bm_num_of_planes = 1;
    InfoHeader._bm_ver_resolution = 0;

    fwrite(&FileHeader, sizeof(BMPFileHeader), 1, fp);
    fwrite(&InfoHeader, sizeof(BMPInfoHeader), 1, fp);

    byte zero = 0x00;

    for (int j = 0; j < ImSize.height; j++)
    {
        for (int i = 0; i < ImSize.width; i++)
        {
            //B G R - B G R ...

            fwrite(&zero, 1, 1, fp);
            fwrite(&zero, 1, 1, fp);
            fwrite(&(Img[j * Stride + i]), 1, 1, fp);
            //fwrite(&(Img[j * Stride + i]), 1, 1, fp);
            //fwrite(&(Img[j * Stride + i]), 1, 1, fp);
            //fwrite(&zero, 1, 1, fp);
            //fwrite(&zero, 1, 1, fp);
        }
    }
    fclose(fp);
}

void DumpBmpData(char* FileName, byte* Img, int Stride, ROI ImSize, int color_depth)
{
    if ((color_depth != 24) && (color_depth != 32))
    {
        printf("僅能製作 24/32 位元深度圖片\n");
        return;
    }

    FILE* fp = NULL;
    fp = fopen(FileName, "wb");

    if (fp == NULL)
    {
        return;
    }

    BMPFileHeader FileHeader;
    BMPInfoHeader InfoHeader;

    // init headers
    FileHeader._bm_signature = 0x4D42;
    FileHeader._bm_file_size = 54 + (color_depth / 8) * ImSize.width * ImSize.height;
    FileHeader._bm_reserved = 0;
    FileHeader._bm_bitmap_data = 0x36;
    InfoHeader._bm_bitmap_size = 0;
    InfoHeader._bm_color_depth = color_depth;
    InfoHeader._bm_compressed = 0;
    InfoHeader._bm_hor_resolution = 0x0ec4;
    InfoHeader._bm_image_height = ImSize.height;
    InfoHeader._bm_image_width = ImSize.width;
    InfoHeader._bm_info_header_size = 40;
    InfoHeader._bm_num_colors_used = 0;
    InfoHeader._bm_num_important_colors = 0;
    InfoHeader._bm_num_of_planes = 1;
    InfoHeader._bm_ver_resolution = 0x0ec4;

    fwrite(&FileHeader, sizeof(BMPFileHeader), 1, fp);
    fwrite(&InfoHeader, sizeof(BMPInfoHeader), 1, fp);

    //printf("www = % d, hhh = %d\n", InfoHeader._bm_image_width, InfoHeader._bm_image_height);

    for (int j = 0; j < ImSize.height; j++)
    {
        for (int i = 0; i < ImSize.width; i++)
        {
            //B G R - B G R ...
            //B G R A - B G R A...

            if (color_depth == 32)
            {
                fwrite(&(Img[(i + j * ImSize.width) * 4 + 0]), 1, 1, fp);   //B
                fwrite(&(Img[(i + j * ImSize.width) * 4 + 1]), 1, 1, fp);   //G
                fwrite(&(Img[(i + j * ImSize.width) * 4 + 2]), 1, 1, fp);   //R
                fwrite(&(Img[(i + j * ImSize.width) * 4 + 3]), 1, 1, fp);   //A
            }
            else
            {
                fwrite(&(Img[(i + j * ImSize.width) * 3 + 0]), 1, 1, fp);   //B
                fwrite(&(Img[(i + j * ImSize.width) * 3 + 1]), 1, 1, fp);   //G
                fwrite(&(Img[(i + j * ImSize.width) * 3 + 2]), 1, 1, fp);   //R
            }

            // 
            //fwrite(&zero, 1, 1, fp);
            //fwrite(&zero, 1, 1, fp);
        }
    }
    fclose(fp);
}


/**
**************************************************************************
*  This function performs dumping of 8x8 block from float plane
*
* \param PlaneF         [IN] - Image plane
* \param StrideF        [IN] - Image stride
* \param Fname          [OUT] - File name to dump to
*
* \return None
*/
void DumpBlockF(float *PlaneF, int StrideF, char *Fname)
{
  FILE *fp = fopen(Fname, "wb");

  for (int i = 0; i < 8; i++)
  {
    for (int j = 0; j < 8; j++)
    {
      fprintf(fp, "%.*f  ", 14, PlaneF[i * StrideF + j]);
    }
    fprintf(fp, "\n");
  }

  fclose(fp);
}

/**
**************************************************************************
*  This function performs dumping of 8x8 block from byte plane
*
* \param Plane          [IN] - Image plane
* \param Stride         [IN] - Image stride
* \param Fname          [OUT] - File name to dump to
*
* \return None
*/
void DumpBlock(byte *Plane, int Stride, char *Fname)
{
  FILE *fp = fopen(Fname, "wb");

  for (int i = 0; i < 8; i++)
  {
    for (int j = 0; j < 8; j++)
    {
      fprintf(fp, "%.3d  ", Plane[i * Stride + j]);
    }

    fprintf(fp, "\n");
  }

  fclose(fp);
}


