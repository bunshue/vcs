/* This sample is a templatized version of the template project.
* It also shows how to correctly templatize dynamically allocated shared
* memory arrays.
* Host code.
*/

// System includes
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <math.h>

// CUDA runtime
#include <cuda_runtime.h>

// helper functions and utilities to work with CUDA
#include <helper_functions.h>
#include <helper_cuda.h>

#ifndef MAX
#define MAX(a, b) (a > b ? a : b)
#endif

// includes, kernels
#include "sharedmem.cuh"

int g_TotalFailures = 0;

////////////////////////////////////////////////////////////////////////////////
//! Simple test kernel for device functionality
//! @param g_idata  input data in global memory
//! @param g_odata  output data in global memory
////////////////////////////////////////////////////////////////////////////////
template <class T>
__global__ void testKernel(T* g_idata, T* g_odata)
{
    // Shared mem size is determined by the host app at run time
    SharedMemory<T> smem;
    T* sdata = smem.getPointer();

    // access thread id
    const unsigned int tid = threadIdx.x;
    // access number of threads in this block
    const unsigned int num_threads = blockDim.x;

    // read in input data from global memory
    sdata[tid] = g_idata[tid];
    __syncthreads();

    // perform some computations
    sdata[tid] = (T)num_threads * sdata[tid];
    __syncthreads();

    // write data to global memory
    g_odata[tid] = sdata[tid];
}

////////////////////////////////////////////////////////////////////////////////
// declaration, forward
template <class T>
void runTest(int argc, char** argv, int len);

template <class T>
void computeGold(T* reference, T* idata, const unsigned int len)
{
    const T T_len = static_cast<T>(len);

    for (unsigned int i = 0; i < len; ++i)
    {
        reference[i] = idata[i] * T_len;
    }
}

// To completely templatize runTest (below) with cutil, we need to use
// template specialization to wrap up CUTIL's array comparison and file writing
// functions for different types.

// Here's the generic wrapper for cutCompare*
template <class T>
class ArrayComparator
{
public:
    bool compare(const T* reference, T* data, unsigned int len)
    {
        fprintf(stderr, "Error: no comparison function implemented for this type\n");
        return false;
    }
};

// Here's the specialization for ints:
template <>
class ArrayComparator<int>
{
public:
    bool compare(const int* reference, int* data, unsigned int len)
    {
        return compareData(reference, data, len, 0.15f, 0.0f);
    }
};

// Here's the specialization for floats:
template <>
class ArrayComparator<float>
{
public:
    bool compare(const float* reference, float* data, unsigned int len)
    {
        return compareData(reference, data, len, 0.15f, 0.15f);
    }
};

// Here's the generic wrapper for cutWriteFile*
template <class T>
class ArrayFileWriter
{
public:
    bool write(const char* filename, T* data, unsigned int len, float epsilon)
    {
        fprintf(stderr, "Error: no file write function implemented for this type\n");
        return false;
    }
};

// Here's the specialization for ints:
template <>
class ArrayFileWriter<int>
{
public:
    bool write(const char* filename, int* data, unsigned int len, float epsilon)
    {
        return sdkWriteFile(filename, data, len, epsilon, false);
    }
};

// Here's the specialization for floats:
template <>
class ArrayFileWriter<float>
{
public:
    bool write(const char* filename, float* data, unsigned int len, float epsilon)
    {
        return sdkWriteFile(filename, data, len, epsilon, false);
    }
};

////////////////////////////////////////////////////////////////////////////////
//! Run a simple test for CUDA
////////////////////////////////////////////////////////////////////////////////
template <class T>
void runTest(int argc, char** argv, int len)
{
    int devID;
    cudaDeviceProp deviceProps;

    devID = findCudaDevice(argc, (const char**)argv);

    // get number of SMs on this GPU
    checkCudaErrors(cudaGetDeviceProperties(&deviceProps, devID));

    printf("Name = %s\n", deviceProps.name);
    printf("clockRate = %d\n", deviceProps.clockRate);
    printf("multiProcessorCount = %d\n", deviceProps.multiProcessorCount);
    printf("totalGlobalMem = %u\n", deviceProps.totalGlobalMem);
    printf("sharedMemPerBlock = %u\n", deviceProps.sharedMemPerBlock);
    printf("totalConstMem = %d\n", deviceProps.totalConstMem);
    printf("memoryClockRate = %d\n", deviceProps.memoryClockRate);
    printf("maxBlocksPerMultiProcessor = %d\n", deviceProps.maxBlocksPerMultiProcessor);

    printf("CUDA device [%s] has %d Multi-Processors\n", deviceProps.name, deviceProps.multiProcessorCount);

    // create and start timer
    StopWatchInterface* timer = NULL;
    sdkCreateTimer(&timer);

    // start the timer
    sdkStartTimer(&timer);

    unsigned int num_threads = len;
    unsigned int mem_size = sizeof(float) * num_threads;

    // allocate host memory
    T* h_idata = (T*)malloc(mem_size);

    // initialize the memory
    for (unsigned int i = 0; i < num_threads; ++i)
    {
        h_idata[i] = (T)i;
    }

    // allocate device memory
    T* d_idata;
    checkCudaErrors(cudaMalloc((void**)&d_idata, mem_size));
    // copy host memory to device
    checkCudaErrors(cudaMemcpy(d_idata, h_idata, mem_size, cudaMemcpyHostToDevice));

    // allocate device memory for result
    T* d_odata;
    checkCudaErrors(cudaMalloc((void**)&d_odata, mem_size));

    // setup execution parameters
    dim3 grid(1, 1, 1);
    dim3 threads(num_threads, 1, 1);

    // execute the kernel
    testKernel<T> << <grid, threads, mem_size >> > (d_idata, d_odata);

    // check if kernel execution generated and error
    getLastCudaError("Kernel execution failed");

    // allocate mem for the result on host side
    T* h_odata = (T*)malloc(mem_size);
    // copy result from device to host
    checkCudaErrors(cudaMemcpy(h_odata, d_odata, sizeof(T) * num_threads, cudaMemcpyDeviceToHost));

    sdkStopTimer(&timer);
    printf("Processing time: %f (ms)\n", sdkGetTimerValue(&timer));
    sdkDeleteTimer(&timer);

    // compute reference solution
    T* reference = (T*)malloc(mem_size);
    computeGold<T>(reference, h_idata, num_threads);

    ArrayComparator<T> comparator;
    ArrayFileWriter<T> writer;

    char filename[30];
    sprintf(filename, "./dump_data_%d.bin", len);
    writer.write(filename, h_odata, num_threads, 0.0f);

    //writer.write("./dump_data.dat", h_odata, num_threads, 0.0f);

    // custom output handling when no regression test running
    // in this case check if the result is equivalent to the expected solution
    bool res = comparator.compare(reference, h_odata, num_threads);
    printf("Compare %s\n\n", (1 == res) ? "OK" : "MISMATCH");
    g_TotalFailures += (1 != res);

    // cleanup memory
    free(h_idata);
    free(h_odata);
    free(reference);
    checkCudaErrors(cudaFree(d_idata));
    checkCudaErrors(cudaFree(d_odata));
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    printf("runTest<float,32>\n");
    runTest<float>(argc, argv, 32);

    printf("runTest<int,64>\n");
    runTest<int>(argc, argv, 64);

    printf("\n[simpleTemplates] -> Test Results: %d Failures\n", g_TotalFailures);

    exit(g_TotalFailures == 0 ? EXIT_SUCCESS : EXIT_FAILURE);
}

