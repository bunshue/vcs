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

/**
 * CUDA Kernel Device code
 *
 * Computes the vector addition of A and B into C. The 3 vectors have the same
 * number of elements numElements.
 */
__global__ void vectorAdd(const byte* A, const byte* B, byte* C, int numElements)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < numElements)
    {
        //C[i] = (A[i] + B[i]) % 256;
        C[i] = (A[i]/2 + B[i]/2) % 256;
    }
}

void printData(byte* h_A, byte* h_B, byte* h_C, int len);

int main(int argc, char **argv)
{
  // initialize CUDA
  findCudaDevice(argc, (const char **)argv);

  int ImgWidth;
  int ImgHeight;
  int ColorDepth;
  ROI ImgSize;
  int res;
  int ImgStride;
  int ImgDataSize;

  char filename_read1[] = "C:\\______test_files1\\ims01.bmp";
  char filename_read2[] = "C:\\______test_files1\\ims03.bmp";

  printf("讀取檔案 : %s\n", filename_read1);
  res = PreLoadBmp2(filename_read1, &ImgWidth, &ImgHeight, &ColorDepth);
  if (res != 0)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;
  ImgDataSize = ImgWidth * (ColorDepth / 8) * ImgHeight;
  printf("W = %d, H = %d\t", ImgSize.width, ImgSize.height);
  printf("圖片位元深度 : %d 位元\n", ColorDepth);
  byte* ImageData1 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
  //printf("ImgStride = %d\n", ImgStride);
  LoadBmpAsData(filename_read1, ImgStride, ImgSize, ImageData1, ColorDepth);

  printf("讀取檔案 : %s\n", filename_read2);
  res = PreLoadBmp2(filename_read2, &ImgWidth, &ImgHeight, &ColorDepth);
  if (res != 0)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;
  printf("W = %d, H = %d\t", ImgSize.width, ImgSize.height);
  printf("圖片位元深度 : %d 位元\n", ColorDepth);
  byte* ImageData2 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
  //printf("ImgStride = %d\n", ImgStride);
  LoadBmpAsData(filename_read2, ImgStride, ImgSize, ImageData2, ColorDepth);

  byte* ImageData3 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
  for (int i = 0; i < ImgWidth * (ColorDepth / 8) * ImgHeight; i++)
  {
      ImageData3[i] = 0x11;
  }

  // Error code to check return values for CUDA calls
  cudaError_t err = cudaSuccess;

  byte* d_A = NULL;
  err = cudaMalloc((void**)&d_A, ImgDataSize);

  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to allocate device vector A (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  byte* d_B = NULL;
  err = cudaMalloc((void**)&d_B, ImgDataSize);

  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to allocate device vector B (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  byte* d_C = NULL;
  err = cudaMalloc((void**)&d_C, ImgDataSize);

  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to allocate device vector C (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  // Copy the host input vectors A and B in host memory to the device input vectors in device memory
  printf("Copy input data from the host memory to the CUDA device\n");
  err = cudaMemcpy(d_A, ImageData1, ImgDataSize, cudaMemcpyHostToDevice);
  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to copy vector A from host to device (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  err = cudaMemcpy(d_B, ImageData2, ImgDataSize, cudaMemcpyHostToDevice);
  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to copy vector B from host to device (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  int numElements = ImgDataSize/2;  //應為總大小

  // Launch the Vector Add CUDA Kernel
  int threadsPerBlock = 256;
  int blocksPerGrid = (numElements + threadsPerBlock - 1) / threadsPerBlock;
  printf("CUDA kernel launch with %d blocks of %d threads\n", blocksPerGrid, threadsPerBlock);
  vectorAdd << <blocksPerGrid, threadsPerBlock >> > (d_A, d_B, d_C, numElements);
  //                   blocks, threads

  err = cudaGetLastError();
  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to launch vectorAdd kernel (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  // Copy the device result vector in device memory to the host result vector
  // in host memory.
  printf("Copy output data from the CUDA device to the host memory\n");

  //printf("old\n");
  //printData(ImageData1, ImageData2, ImageData3, 20);

  err = cudaMemcpy(ImageData3, d_C, ImgDataSize, cudaMemcpyDeviceToHost);

  //printf("new\n");
  //printData(ImageData1, ImageData2, ImageData3, 20);

  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to copy vector C from device to host (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

/*
  // Launch kernel on 1M elements on the GPU
  int blockSize = 256;
  int numBlocks = (N + blockSize - 1) / blockSize;

  //addKernel << <numBlocks, blockSize >> > (N, ImageData1, ImageData2);
  //addKernel << <1, size >> > (dev_c, dev_a, dev_b);
  //__global__ void addKernel(byte * c, const byte * a, const byte * b)
  int size = 1;
  addKernel << <1, size >> > (ImageData3, ImageData1, ImageData2);
*/

  // Wait for GPU to finish before accessing on host
  //cudaDeviceSynchronize();

  //製作一個特定位元深度之bmp檔案 ST
  char filename_write1[] = "ims.new1.bmp";
  char filename_write2[] = "ims.new2.bmp";
  char filename_write3[] = "ims.new3.bmp";
  printf("製作一個bmp檔案 : %s\n", filename_write1);
  printf("製作一個bmp檔案 : %s\n", filename_write2);
  printf("製作一個bmp檔案 : %s\n", filename_write3);
  //ImgStride = 320;

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

  FreePlane(ImageData1);
  FreePlane(ImageData2);
  FreePlane(ImageData3);


  cudaFree(data1);
  cudaFree(data2);
  cudaFree(data3);


  printf("Test PASSED\n");

  err = cudaFree(d_A);
  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to free device vector A (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  err = cudaFree(d_B);
  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to free device vector B (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }

  err = cudaFree(d_C);
  if (err != cudaSuccess)
  {
      fprintf(stderr, "Failed to free device vector C (error code %s)!\n", cudaGetErrorString(err));
      exit(EXIT_FAILURE);
  }


  // finalize
  printf("Test passed\n");
  exit(EXIT_SUCCESS);
}

void printData(byte* h_A, byte* h_B, byte* h_C, int len)
{
    for (int i = 0; i < len; i++)
    {
        printf("%4d", h_A[i]);
    }
    printf("\n");
    for (int i = 0; i < len; i++)
    {
        printf("%4d", h_B[i]);
    }
    printf("\n");
    for (int i = 0; i < len; i++)
    {
        printf("%4d", h_C[i]);
    }
    printf("\n");
}


