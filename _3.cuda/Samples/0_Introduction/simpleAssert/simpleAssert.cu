#ifdef _WIN32
#define WINDOWS_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>
#else
#include <sys/utsname.h>
#endif

// Includes, system
#include <stdio.h>
#include <cassert>

// Includes CUDA
#include <cuda_runtime.h>

// Utilities and timing functions
#include <helper_functions.h>  // includes cuda.h and cuda_runtime_api.h

// CUDA helper functions
#include <helper_cuda.h>  // helper functions for CUDA error check

////////////////////////////////////////////////////////////////////////////////
// Auto-Verification Code
bool testResult = true;

////////////////////////////////////////////////////////////////////////////////
// Kernels
////////////////////////////////////////////////////////////////////////////////
//! Tests assert function.
//! Thread whose id > N will print assertion failed error message.
////////////////////////////////////////////////////////////////////////////////
__global__ void testKernel(int N)
{
    int gtid = blockIdx.x * blockDim.x + threadIdx.x;
    assert(gtid < N);
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    printf("Starting...\n");

    int Nblocks = 2;
    int Nthreads = 32;
    cudaError_t error;

    // This will pick the best possible CUDA capable device
    findCudaDevice(argc, (const char**)argv);

    // Kernel configuration, where a one-dimensional
    // grid and one-dimensional blocks are configured.
    dim3 dimGrid(Nblocks);
    dim3 dimBlock(Nthreads);

    printf("Launch kernel to generate assertion failures\n");
    testKernel << <dimGrid, dimBlock >> > (60);

    // Synchronize (flushes assert output).
    printf("\n-- Begin assert output\n\n");
    error = cudaDeviceSynchronize();
    printf("\n-- End assert output\n\n");

    // Check for errors and failed asserts in asynchronous kernel launch.
    if (error == cudaErrorAssert)
    {
        printf("Device assert failed as expected, CUDA error message is: %s\n\n", cudaGetErrorString(error));
    }

    testResult = error == cudaErrorAssert;

    printf("Completed, returned %s\n", testResult ? "OK" : "ERROR!");
    exit(testResult ? EXIT_SUCCESS : EXIT_FAILURE);

}
