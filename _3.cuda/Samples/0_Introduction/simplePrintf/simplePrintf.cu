// System includes
#include <stdio.h>
#include <assert.h>

// CUDA runtime
#include <cuda_runtime.h>

// helper functions and utilities to work with CUDA
#include <helper_functions.h>
#include <helper_cuda.h>

#ifndef MAX
#define MAX(a, b) (a > b ? a : b)
#endif

__global__ void testKernel(int val)
{
    printf("blockIdx.x = %d\n", blockIdx.x);
    printf("blockIdx.y = %d\n", blockIdx.y);
    printf("gridDim.x = %d\n", gridDim.x);
    printf("gridDim.y = %d\n", gridDim.y);
    printf("blockDim.x = %d\n", blockDim.x);
    printf("blockDim.y = %d\n", blockDim.y);
    printf("threadIdx.x = %d\n", threadIdx.x);
    printf("threadIdx.y = %d\n", threadIdx.y);
    printf("threadIdx.z = %d\n", threadIdx.z);

    printf("testKernel [%d, %d]:\tValue is : %d\n",
        blockIdx.y * gridDim.x + blockIdx.x, threadIdx.z * blockDim.x * blockDim.y + threadIdx.y * blockDim.x + threadIdx.x, val);
}

int main(int argc, char** argv)
{
    /* 沒甚麼用的
    int devID;
    cudaDeviceProp props;

    // This will pick the best possible CUDA capable device
    devID = findCudaDevice(argc, (const char**)argv);
    printf("devID = %d\n", devID);

    // Get GPU information
    checkCudaErrors(cudaGetDevice(&devID));
    checkCudaErrors(cudaGetDeviceProperties(&props, devID));
    printf("Device %d: \"%s\" with Compute %d.%d capability\n", devID, props.name, props.major, props.minor);

    printf("printf() is called. Output:\n\n");
    */

    // Kernel configuration, where a two-dimensional grid and three-dimensional blocks are configured.

    dim3 dimGrid(2, 2);
    dim3 dimBlock(2, 2, 2);

    testKernel << <dimGrid, dimBlock >> > (10);

    cudaDeviceSynchronize();

    return EXIT_SUCCESS;
}


