#include <stdio.h>
#include <iostream>

// STL.
#include <vector>

// CUDA runtime.
#include <cuda_runtime.h>

// Helper functions and utilities to work with CUDA.
#include <helper_functions.h>
#include <helper_cuda.h>

// Device library includes.
#include "simpleDeviceLibrary.cuh"

using std::cout;
using std::endl;

using std::vector;

#define EPS 1e-5

typedef unsigned int uint;
typedef float (*deviceFunc)(float);

////////////////////////////////////////////////////////////////////////////////
// Auto-Verification Code
bool testResult = true;

////////////////////////////////////////////////////////////////////////////////
// Static device pointers to __device__ functions.
__device__ deviceFunc dMultiplyByTwoPtr = multiplyByTwo;
__device__ deviceFunc dDivideByTwoPtr = divideByTwo;

////////////////////////////////////////////////////////////////////////////////
// Kernels
////////////////////////////////////////////////////////////////////////////////
//! Transforms vector.
//! Applies the __device__ function "f" to each element of the vector "v".
////////////////////////////////////////////////////////////////////////////////
__global__ void transformVector(float* v, deviceFunc f, uint size)
{
    uint tid = blockIdx.x * blockDim.x + threadIdx.x;

    if (tid < size)
    {
        v[tid] = (*f)(v[tid]);
    }
}

int main(int argc, char** argv)
{
    cout << "Starting..." << endl;

    try
    {
        // This will pick the best possible CUDA capable device.
        findCudaDevice(argc, (const char**)argv);

        // Create host vector.
        const uint kVectorSize = 1000;

        vector<float> hVector(kVectorSize);

        for (uint i = 0; i < kVectorSize; ++i)
        {
            hVector[i] = rand() / static_cast<float>(RAND_MAX);
        }

        // Create and populate device vector.
        float* dVector;
        checkCudaErrors(cudaMalloc(&dVector, kVectorSize * sizeof(float)));

        checkCudaErrors(cudaMemcpy(dVector, &hVector[0], kVectorSize * sizeof(float), cudaMemcpyHostToDevice));

        // Kernel configuration, where a one-dimensional
        // grid and one-dimensional blocks are configured.
        const int nThreads = 1024;
        const int nBlocks = 1;

        dim3 dimGrid(nBlocks);
        dim3 dimBlock(nThreads);

        // Test library functions.
        deviceFunc hFunctionPtr;

        cudaMemcpyFromSymbol(&hFunctionPtr, dMultiplyByTwoPtr, sizeof(deviceFunc));
        transformVector << <dimGrid, dimBlock >> > (dVector, hFunctionPtr, kVectorSize);
        checkCudaErrors(cudaGetLastError());

        cudaMemcpyFromSymbol(&hFunctionPtr, dDivideByTwoPtr, sizeof(deviceFunc));
        transformVector << <dimGrid, dimBlock >> > (dVector, hFunctionPtr, kVectorSize);
        checkCudaErrors(cudaGetLastError());

        // Download results.
        vector<float> hResultVector(kVectorSize);

        checkCudaErrors(cudaMemcpy(&hResultVector[0], dVector, kVectorSize * sizeof(float), cudaMemcpyDeviceToHost));

        // Check results.
        for (int i = 0; i < kVectorSize; ++i)
        {
            if (fabs(hVector[i] - hResultVector[i]) > EPS)
            {
                cout << "Computations were incorrect..." << endl;
                testResult = false;
                break;
            }
        }

        // Free resources.
        if (dVector) checkCudaErrors(cudaFree(dVector));
    }
    catch (...)
    {
        cout << "Error occured, exiting..." << endl;
        exit(EXIT_FAILURE);
    }
    cout << "Completed, returned " << (testResult ? "OK" : "ERROR") << endl;

    exit(testResult ? EXIT_SUCCESS : EXIT_FAILURE);
}

