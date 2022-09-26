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

//int total_thread = 0;
__global__ void testKernel(int val)
{
    /*
    printf("blockIdx.x = %d\n", blockIdx.x);
    printf("blockIdx.y = %d\n", blockIdx.y);
    printf("gridDim.x = %d\n", gridDim.x);
    printf("gridDim.y = %d\n", gridDim.y);
    printf("blockDim.x = %d\n", blockDim.x);
    printf("blockDim.y = %d\n", blockDim.y);
    printf("threadIdx.x = %d\n", threadIdx.x);
    printf("threadIdx.y = %d\n", threadIdx.y);
    printf("threadIdx.z = %d\n", threadIdx.z);
    */

    printf("testKernel [%d, %d]:\tValue is : %d\n",
        blockIdx.y * gridDim.x + blockIdx.x,
        threadIdx.z * blockDim.x * blockDim.y + threadIdx.y * blockDim.x + threadIdx.x,
        val);
    //total_thread++;
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

    dim3 dimGrid(3, 3);     //MXN個block
    dim3 dimBlock(2, 2, 2); //每個block內有AXBXC個thread

    testKernel << <dimGrid, dimBlock >> > (10);

    cudaDeviceSynchronize();

    //printf("total_thread  = %d\n", total_thread);

    return EXIT_SUCCESS;
}


