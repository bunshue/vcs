/* Copyright (c) 2022, NVIDIA CORPORATION. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *  * Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *  * Neither the name of NVIDIA CORPORATION nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

/**
**************************************************************************
* \file dct8x8.cu
* \brief Contains entry point, wrappers to host and device code and benchmark.
*
* This sample implements forward and inverse Discrete Cosine Transform to blocks
* of image pixels (of 8x8 size), as in JPEG standard. The typical work flow is
*as
* follows:
* 1. Run CPU version (Host code) and measure execution time;
* 2. Run CUDA version (Device code) and measure execution time;
* 3. Output execution timings and calculate CUDA speedup.
*/

#include <stdio.h>
#include "Common.h"
#include "DCT8x8_Gold.h"
#include "BmpUtil.h"

/**
*  The number of DCT kernel calls
*/
#define BENCHMARK_SIZE 10

/**
*  The PSNR values over this threshold indicate images equality
*/
#define PSNR_THRESHOLD_EQUAL 40

// includes kernels
#include "dct8x8_kernel1.cuh"
#include "dct8x8_kernel2.cuh"
#include "dct8x8_kernel_short.cuh"
#include "dct8x8_kernel_quantization.cuh"

// CUDA kernel to add elements of two arrays
/*
__global__
void addKernel(int n, byte* x, byte* y)
{
    int index = blockIdx.x * blockDim.x + threadIdx.x;
    int stride = blockDim.x * gridDim.x;

    printf("index = %d\tn=%d\tstride = %d\n", index, n, stride);

    for (int i = index; i < n; i += stride)
    {
        //目前都沒有進來這裡
        //y[i] = x[i] + y[i];
        y[i] = 0;
        printf(".");
    }
}
*/

__global__ void addKernel(byte* c, const byte* a, const byte* b)
{
    printf("Q");
    int i = threadIdx.x;
    //c[i] = (a[i]/10 + b[i]/10) % 256;
    c[i] = a[i];
    printf("Z");
}

__global__ void vecAdd(byte* a, byte* b, byte* c)
{
    int i = threadIdx.x;
    //c[i] = (a[i] + b[i])%256;
    //c[i] = 0;
    c[i] = (a[i] + b[i]) % 256;
}

/**
**************************************************************************
*  Program entry point
*
* \param argc       [IN] - Number of command-line arguments
* \param argv       [IN] - Array of command-line arguments
*
* \return Status code
*/

int main(int argc, char **argv)
{
  // initialize CUDA
  findCudaDevice(argc, (const char **)argv);

  char filename1[] = "portrait_noise.bmp";
  char filename2[] = "portrait_noise.ok.bmp";

  // preload image (acquire dimensions)
  int ImgWidth;
  int ImgHeight;
  int ColorDepth;
  ROI ImgSize;

  printf("PreLoadBmp, file : %s\n", filename1);
  int res = PreLoadBmp(filename1, &ImgWidth, &ImgHeight);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }

  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;

  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);
  printf("讀取檔案 : %s\n", filename1);

  // check image dimensions are multiples of BLOCK_SIZE
  if (ImgWidth % BLOCK_SIZE != 0 || ImgHeight % BLOCK_SIZE != 0)
  {
    printf("\nError: Input image dimensions must be multiples of 8!\n");
    exit(EXIT_FAILURE);
    return 1;
  }

  // allocate image buffers
  int ImgStride;
  byte *ImgSrc = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);
  byte *ImgDst = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);

  printf("ImgStride = %d\n", ImgStride);

  // load sample image
  LoadBmpAsGray(filename1, ImgStride, ImgSize, ImgSrc);

  printf("寫入檔案 : %s\n", filename2);
  DumpBmpAsGray(filename2, ImgDst, ImgStride, ImgSize);

  //製作一個24位元深度之bmp檔案 ST
  char filename3[] = "my_bmp333b.bmp";
  printf("製作一個bmp檔案 : %s\n", filename3);
  ImgStride = 320;

  ImgWidth = 16;
  ImgHeight = 16;
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;

  byte* ImgDst333 = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);
  for (int i = 0; i < ImgWidth * ImgHeight; i++)
  {
      ImgDst333[i] = (i % 256);
  }
  DumpBmpAsGray(filename3, ImgDst333, ImgStride, ImgSize);
  FreePlane(ImgDst333);
  //製作一個24位元深度之bmp檔案 SP

  // release byte planes
  FreePlane(ImgSrc);
  FreePlane(ImgDst);

  //讀取一個bmp檔案 ST, 判斷位元深度
  char filename_read[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\pic_256X100b.bmp";
  printf("讀取檔案 : %s\n", filename_read);

  res = PreLoadBmp2(filename_read, &ImgWidth, &ImgHeight, &ColorDepth);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }

  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;

  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);
  printf("圖片位元深度 : %d 位元\n", ColorDepth);

  byte* ImageData = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);

  printf("ImgStride = %d\n", ImgStride);

  LoadBmpAsData(filename_read, ImgStride, ImgSize, ImageData, ColorDepth);

  /*
  for (int i = 0; i < 100; i++)
  {
      printf("%02X ", ImageData[i]);


  }
  printf("\n");
  */

  //把資料存成另一個bmp檔案

  //製作一個特定位元深度之bmp檔案 ST
  char filename_write[] = "pic_256X100b.32.new.bmp";
  printf("製作一個bmp檔案 : %s\n", filename_write);
  //ImgStride = 320;

  //ImgWidth = 16;
  //ImgHeight = 16;
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;

  ColorDepth = 32;
  DumpBmpData(filename_write, ImageData, ImgStride, ImgSize, ColorDepth);

  //製作一個特定位元深度之bmp檔案 SP


  FreePlane(ImageData);

  char filename_read1[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims01.bmp";
  char filename_read2[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims03.bmp";

  printf("讀取檔案 : %s\n", filename_read1);
  res = PreLoadBmp2(filename_read1, &ImgWidth, &ImgHeight, &ColorDepth);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;
  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);
  printf("圖片位元深度 : %d 位元\n", ColorDepth);
  byte* ImageData1 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
  printf("ImgStride = %d\n", ImgStride);
  LoadBmpAsData(filename_read1, ImgStride, ImgSize, ImageData1, ColorDepth);

  printf("讀取檔案 : %s\n", filename_read2);
  res = PreLoadBmp2(filename_read2, &ImgWidth, &ImgHeight, &ColorDepth);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;
  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);
  printf("圖片位元深度 : %d 位元\n", ColorDepth);
  byte* ImageData2 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
  printf("ImgStride = %d\n", ImgStride);
  LoadBmpAsData(filename_read2, ImgStride, ImgSize, ImageData2, ColorDepth);


  byte* ImageData3 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
  for (int i = 0; i < ImgWidth * (ColorDepth / 8) * ImgHeight; i++)
  {
      ImageData3[i] = 0x11;
  }

  //int N = 640 * 480 * (32 / 8);


  int N = 256;
  vecAdd << <1, N >> > (ImageData1, ImageData2, ImageData3);
  //         1 block, N threads



  /*
  byte* ImageData1;
  byte* ImageData2;

  // Allocate Unified Memory - accessible from CPU or GPU
  cudaMallocManaged(&ImageData1, N * sizeof(byte));
  cudaMallocManaged(&ImageData2, N * sizeof(byte));

  // initialize ImageData1 and ImageData2 arrays on the host
  for (int i = 0; i < N; i++)
  {
      ImageData1[i] = 3.0f;
      ImageData2[i] = 7.0f;
  }
  */

  for (int i = 0; i < 10; i++)
  {
      printf("ImageData1[%d] = %d\t", i, ImageData1[i]);
      printf("ImageData2[%d] = %d\t", i, ImageData2[i]);
      printf("ImageData3[%d] = %d\n", i, ImageData3[i]);
  }
  printf("\n");

  // Launch kernel on 1M elements on the GPU
  int blockSize = 256;
  int numBlocks = (N + blockSize - 1) / blockSize;

  //addKernel << <numBlocks, blockSize >> > (N, ImageData1, ImageData2);
  //addKernel << <1, size >> > (dev_c, dev_a, dev_b);
  //__global__ void addKernel(byte * c, const byte * a, const byte * b)
  
  int size = 480;
  addKernel << <1, size >> > (ImageData3, ImageData1, ImageData2);

  // Wait for GPU to finish before accessing on host
  cudaDeviceSynchronize();

  printf("\n");
  for (int i = 0; i < 10; i++)
  {
      printf("ImageData1[%d] = %d\t", i, ImageData1[i]);
      printf("ImageData2[%d] = %d\t", i, ImageData2[i]);
      printf("ImageData3[%d] = %d\n", i, ImageData3[i]);
  }

  //製作一個特定位元深度之bmp檔案 ST
  char filename_write1[] = "ims.new1.bmp";
  char filename_write2[] = "ims.new2.bmp";
  char filename_write3[] = "ims.new3.bmp";
  printf("製作一個bmp檔案 : %s\n", filename_write1);
  printf("製作一個bmp檔案 : %s\n", filename_write2);
  printf("製作一個bmp檔案 : %s\n", filename_write3);
  //ImgStride = 320;

  //ImgWidth = 16;
  //ImgHeight = 16;
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;

  ColorDepth = 32;
  DumpBmpData(filename_write1, ImageData1, ImgStride, ImgSize, ColorDepth);
  DumpBmpData(filename_write2, ImageData2, ImgStride, ImgSize, ColorDepth);
  DumpBmpData(filename_write3, ImageData3, ImgStride, ImgSize, ColorDepth);

  //製作一個特定位元深度之bmp檔案 SP

  /*
  // Free memory
  cudaFree(ImageData1);
  cudaFree(ImageData2);
  */

  printf("ImgWidth = %d\tImgHeight=%d\n", ImgWidth, ImgHeight);
  printf("ColorDepth = %d\n", ColorDepth);
  printf("ImgStride = %d\n", ImgStride);
  printf("DataSize = %d\n", ImgWidth * (ColorDepth / 8) * ImgHeight);

  int DataSize = ImgWidth * (ColorDepth / 8) * ImgHeight;

  /*
  byte* data1 = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);
  byte* data2 = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);
  byte* data3 = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);
  */

  byte* data1;
  byte* data2;
  byte* data3;

  cudaMalloc((void**)&data1, DataSize);
  cudaMalloc((void**)&data2, DataSize);
  cudaMalloc((void**)&data3, DataSize);

  cudaMemcpy(data1, ImageData1, DataSize, cudaMemcpyHostToDevice);
  cudaMemcpy(data2, ImageData2, DataSize, cudaMemcpyHostToDevice);

  /*
  for (int i = 0; i < ImgWidth * ImgHeight; i++)
  {
      data1[i] = (i % 256);
      data2[i] = (i % 256);
      data3[i] = 0x17;
  }

  for (int i = 0; i < 10; i++)
  {
      printf("data1[%d] = %d\t", i, data1[i]);
      printf("data2[%d] = %d\t", i, data2[i]);
      printf("data3[%d] = %d\n", i, data3[i]);
  }
  */

  for (int i = 0; i < 10; i++)
  {
      //fail
      //printf("data1[%d] = %d\t", i, *(&data1[0] + i));
      //printf("data2[%d] = %d\t", i, *(&data2[0] + i));
      //printf("data3[%d] = %d\n", i, data3[i]);
  }

  N = 256;
  vecAdd << <1, N >> > (data1, data2, data3);
  //         1 block, N threads

  cudaMemcpy(ImageData3, data3, DataSize, cudaMemcpyDeviceToHost);

  for (int i = 0; i < 10; i++)
  {
      //fail
      //printf("data1[%d] = %d\t", i, *(data1 + i));
      //printf("data2[%d] = %d\t", i, *(data2 + i));
      //printf("data3[%d] = %d\n", i, *(data3 + i));
  }

  FreePlane(ImageData1);
  FreePlane(ImageData2);
  FreePlane(ImageData3);


  cudaFree(data1);
  cudaFree(data2);
  cudaFree(data3);



  // finalize
  printf("Test passed\n");
  exit(EXIT_SUCCESS);
}
