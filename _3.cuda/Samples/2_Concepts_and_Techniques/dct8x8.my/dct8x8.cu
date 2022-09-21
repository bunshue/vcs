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
  char filename_read[] = "C:\\______test_files\\pic_256X100b.bmp";
  printf("讀取檔案 : %s\n", filename_read);

  res = PreLoadBmp2(filename_read, &ImgWidth, &ImgHeight);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }

  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;

  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);

  int color_depth = GetBmpColorDepth(filename_read);
  printf("圖片位元深度 : %d 位元\n", color_depth);


  byte* ImageData = MallocPlaneByte(ImgWidth*(color_depth/8), ImgHeight, &ImgStride);

  printf("ImgStride = %d\n", ImgStride);

  LoadBmpAsData(filename_read, ImgStride, ImgSize, ImageData, color_depth);

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

  color_depth = 32;
  DumpBmpData(filename_write, ImageData, ImgStride, ImgSize, color_depth);

  //製作一個特定位元深度之bmp檔案 SP


  FreePlane(ImageData);



  char filename_read1[] = "C:\\______test_files\\ims01.bmp";
  char filename_read2[] = "C:\\______test_files\\ims03.bmp";

  printf("讀取檔案 : %s\n", filename_read1);
  res = PreLoadBmp2(filename_read1, &ImgWidth, &ImgHeight);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;
  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);
  color_depth = GetBmpColorDepth(filename_read1);
  printf("圖片位元深度 : %d 位元\n", color_depth);
  byte* ImageData1 = MallocPlaneByte(ImgWidth * (color_depth / 8), ImgHeight, &ImgStride);
  printf("ImgStride = %d\n", ImgStride);
  LoadBmpAsData(filename_read1, ImgStride, ImgSize, ImageData1, color_depth);

  printf("讀取檔案 : %s\n", filename_read2);
  res = PreLoadBmp2(filename_read2, &ImgWidth, &ImgHeight);
  if (res)
  {
      printf("\nError: Image file not found or invalid!\n");
      exit(EXIT_FAILURE);
      return 1;
  }
  ImgSize.width = ImgWidth;
  ImgSize.height = ImgHeight;
  printf("W = %d, H = %d, BLOCK_SIZE = %d\n", ImgSize.width, ImgSize.height, BLOCK_SIZE);
  color_depth = GetBmpColorDepth(filename_read2);
  printf("圖片位元深度 : %d 位元\n", color_depth);
  byte* ImageData2 = MallocPlaneByte(ImgWidth * (color_depth / 8), ImgHeight, &ImgStride);
  printf("ImgStride = %d\n", ImgStride);
  LoadBmpAsData(filename_read2, ImgStride, ImgSize, ImageData2, color_depth);

  byte* ImageData3 = MallocPlaneByte(ImgWidth * (color_depth / 8), ImgHeight, &ImgStride);
  for (int i = 0; i < ImgWidth * (color_depth / 8) * ImgHeight; i++)
  {
      ImageData3[i] = 0;
  }

  int N = 640 * 480 * (32 / 8);

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

  color_depth = 32;
  DumpBmpData(filename_write1, ImageData1, ImgStride, ImgSize, color_depth);
  DumpBmpData(filename_write2, ImageData2, ImgStride, ImgSize, color_depth);
  DumpBmpData(filename_write3, ImageData3, ImgStride, ImgSize, color_depth);

  //製作一個特定位元深度之bmp檔案 SP





  /*
  // Free memory
  cudaFree(ImageData1);
  cudaFree(ImageData2);
  */

  FreePlane(ImageData1);
  FreePlane(ImageData2);
  FreePlane(ImageData3);

  // finalize
  printf("Test passed\n");
  exit(EXIT_SUCCESS);
}


