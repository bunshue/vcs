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

  char filename_read1[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims01.bmp";
  char filename_read2[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims03.bmp";

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
  
  int size = 1;
  addKernel << <1, size >> > (ImageData3, ImageData1, ImageData2);

  for (int i = 0; i < 5; i++)
  {
      //ImageData3[i] = (ImageData1[i] + ImageData2[i]) % 256;


  }

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
  char filename_write1[] = "x64\\Debug\\ims.new1.bmp";
  char filename_write2[] = "x64\\Debug\\ims.new2.bmp";
  char filename_write3[] = "x64\\Debug\\ims.new3.bmp";

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
