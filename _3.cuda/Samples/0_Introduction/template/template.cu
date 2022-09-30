// includes, system
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// includes CUDA
#include <cuda_runtime.h>

// includes, project
#include <helper_cuda.h>
#include <helper_functions.h> // helper functions for SDK examples

extern "C" void computeGold(float* reference, float* idata, const unsigned int len);

////////////////////////////////////////////////////////////////////////////////
//! Simple test kernel for device functionality
//! @param g_idata  input data in global memory
//! @param g_odata  output data in global memory
////////////////////////////////////////////////////////////////////////////////
__global__ void testKernel(float* g_idata, float* g_odata)
{
    // shared memory
    // the size is determined by the host application
    extern __shared__ float sdata[];

    // access thread id
    const unsigned int tid = threadIdx.x;
    // access number of threads in this block
    const unsigned int num_threads = blockDim.x;

    // read in input data from global memory
    sdata[tid] = g_idata[tid];
    __syncthreads();

    // perform some computations
    sdata[tid] = (float)num_threads * sdata[tid];
    __syncthreads();

    // write data to global memory
    g_odata[tid] = sdata[tid];
}

void test_sdkWriteFile()
{
    char* filename = "test.bin";

    unsigned int num_threads = 32;
    unsigned int mem_size = sizeof(float) * num_threads;
    float* h_odata = (float*)malloc(mem_size);

    int i;
    for (i = 0; i < num_threads; i++)
    {
        h_odata[i] = (float)i;
    }

    sdkWriteFile(filename, h_odata, num_threads, 0.0f, false);


    free(h_odata);

}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    bool bTestResult = true;

    printf("Starting...\n\n");

    // use command-line specified CUDA device, otherwise use device with highest Gflops/s
    // int devID = findCudaDevice(argc, (const char**)argv);

    StopWatchInterface* timer = 0;
    sdkCreateTimer(&timer);
    sdkStartTimer(&timer);

    unsigned int num_threads = 32;
    unsigned int mem_size = sizeof(float) * num_threads;

    // allocate host memory
    float* h_idata = (float*)malloc(mem_size);

    // initalize the memory
    for (unsigned int i = 0; i < num_threads; ++i)
    {
        h_idata[i] = (float)i;
    }

    // allocate device memory
    float* d_idata;
    checkCudaErrors(cudaMalloc((void**)&d_idata, mem_size));
    // copy host memory to device
    checkCudaErrors(cudaMemcpy(d_idata, h_idata, mem_size, cudaMemcpyHostToDevice));

    // allocate device memory for result
    float* d_odata;
    checkCudaErrors(cudaMalloc((void**)&d_odata, mem_size));

    // setup execution parameters
    dim3 grid(1, 1, 1);
    dim3 threads(num_threads, 1, 1);

    // execute the kernel
    testKernel << <grid, threads, mem_size >> > (d_idata, d_odata);

    // check if kernel execution generated and error
    getLastCudaError("Kernel execution failed");

    // allocate mem for the result on host side
    float* h_odata = (float*)malloc(mem_size);
    // copy result from device to host
    checkCudaErrors(cudaMemcpy(h_odata, d_odata, sizeof(float) * num_threads, cudaMemcpyDeviceToHost));

    sdkStopTimer(&timer);
    printf("Processing time: %f (ms)\n", sdkGetTimerValue(&timer));
    sdkDeleteTimer(&timer);

    // compute reference solution
    float* reference = (float*)malloc(mem_size);
    computeGold(reference, h_idata, num_threads);

    sdkWriteFile("./dump_data.dat", h_odata, num_threads, 0.0f, false);

    // custom output handling when no regression test running
    // in this case check if the result is equivalent to the expected solution
    bTestResult = compareData(reference, h_odata, num_threads, 0.0f, 0.0f);

    // cleanup memory
    free(h_idata);
    free(h_odata);
    free(reference);
    checkCudaErrors(cudaFree(d_idata));
    checkCudaErrors(cudaFree(d_odata));

    printf("do test_sdkWriteFile\n");

    test_sdkWriteFile();

    exit(bTestResult ? EXIT_SUCCESS : EXIT_FAILURE);
}


