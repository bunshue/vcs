#include <stdio.h>
#include "Common.h"
#include "BmpUtil.h"

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
        //�ثe���S���i�ӳo��
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

__global__ void vectorAdd(const byte* A, const byte* B, byte* C, int numElements)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;

    if (i < numElements)
    {
        //C[i] = (A[i] + B[i]) % 256;
        C[i] = (A[i] / 2 + B[i] / 2) % 256;
    }
}

void printData(byte* h_A, byte* h_B, byte* h_C, int len);

int main(int argc, char** argv)
{
    // initialize CUDA
    findCudaDevice(argc, (const char**)argv);

    int ImgWidth;
    int ImgHeight;
    int ColorDepth;
    ROI ImgSize;
    int res;
    int ImgStride;
    int ImgDataSize;

    char filename_read1[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims01.bmp";
    char filename_read2[] = "C:\\_git\\vcs\\_1.data\\______test_files1\\ims03.bmp";

    printf("Ū���ɮ� : %s\n", filename_read1);
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
    printf("�Ϥ��줸�`�� : %d �줸\n", ColorDepth);
    byte* ImageData1 = MallocPlaneByte(ImgWidth * (ColorDepth / 8), ImgHeight, &ImgStride);
    //printf("ImgStride = %d\n", ImgStride);
    LoadBmpAsData(filename_read1, ImgStride, ImgSize, ImageData1, ColorDepth);

    printf("Ū���ɮ� : %s\n", filename_read2);
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
    printf("�Ϥ��줸�`�� : %d �줸\n", ColorDepth);
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

    int numElements = ImgDataSize / 2;  //�����`�j�p

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

    //�s�@�@�ӯS�w�줸�`�פ�bmp�ɮ� ST
    char filename_write1[] = "x64\\Debug\\ims.new1.bmp";
    char filename_write2[] = "x64\\Debug\\ims.new2.bmp";
    char filename_write3[] = "x64\\Debug\\ims.new3.bmp";
    printf("�s�@�@��bmp�ɮ� : %s\n", filename_write1);
    printf("�s�@�@��bmp�ɮ� : %s\n", filename_write2);
    printf("�s�@�@��bmp�ɮ� : %s\n", filename_write3);
    //ImgStride = 320;

    ImgSize.width = ImgWidth;
    ImgSize.height = ImgHeight;

    ColorDepth = 32;
    DumpBmpData(filename_write1, ImageData1, ImgStride, ImgSize, ColorDepth);
    DumpBmpData(filename_write2, ImageData2, ImgStride, ImgSize, ColorDepth);
    DumpBmpData(filename_write3, ImageData3, ImgStride, ImgSize, ColorDepth);

    //�s�@�@�ӯS�w�줸�`�פ�bmp�ɮ� SP

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
