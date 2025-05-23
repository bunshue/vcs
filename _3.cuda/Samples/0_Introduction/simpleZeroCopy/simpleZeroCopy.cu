#include <assert.h>
#include <stdio.h>

// CUDA runtime
#include <cuda_runtime.h>

// helper functions and utilities to work with CUDA
#include <helper_cuda.h>
#include <helper_functions.h>

#ifndef MAX
#define MAX(a, b) (a > b ? a : b)
#endif

/* Add two vectors on the GPU */
__global__ void vectorAddGPU(float* a, float* b, float* c, int N)
{
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < N)
    {
        c[idx] = a[idx] + b[idx];
    }
}

// Allocate generic memory with malloc() and pin it laster instead of using
// cudaHostAlloc()
bool bPinGenericMemory = false;

// Macro to aligned up to the memory size in question
#define MEMORY_ALIGNMENT 4096
#define ALIGN_UP(x, size) (((size_t)x + (size - 1)) & (~(size - 1)))

int main(int argc, char** argv)
{
    int n, nelem, deviceCount;
    int idev = 0;  // use default device 0
    char* device = NULL;
    unsigned int flags;
    size_t bytes;
    float* a, * b, * c;           // Pinned memory allocated on the CPU
    float* a_UA, * b_UA, * c_UA;  // Non-4K Aligned Pinned memory on the CPU
    float* d_a, * d_b, * d_c;     // Device pointers for mapped memory
    float errorNorm, refNorm, ref, diff;
    cudaDeviceProp deviceProp;

    if (checkCmdLineFlag(argc, (const char**)argv, "help"))
    {
        printf("Usage:  simpleZeroCopy [OPTION]\n\n");
        printf("Options:\n");
        printf("  --device=[device #]  Specify the device to be used\n");
        printf("  --use_generic_memory (optional) use generic page-aligned for system memory\n");
        return EXIT_SUCCESS;
    }

    /* Get the device selected by the user or default to 0, and then set it. */
    if (getCmdLineArgumentString(argc, (const char**)argv, "device", &device))
    {
        cudaGetDeviceCount(&deviceCount);
        idev = atoi(device);

        if (idev >= deviceCount || idev < 0)
        {
            fprintf(stderr, "Device number %d is invalid, will use default CUDA device 0.\n", idev);
            idev = 0;
        }
    }

    // if GPU found supports SM 1.2, then continue, otherwise we exit
    if (!checkCudaCapabilities(1, 2))
    {
        exit(EXIT_SUCCESS);
    }

    if (checkCmdLineFlag(argc, (const char**)argv, "use_generic_memory"))
    {
        bPinGenericMemory = true;
    }

    if (bPinGenericMemory)
    {
        printf("> Using Generic System Paged Memory (malloc)\n");
    }
    else
    {
        printf("> Using CUDA Host Allocated (cudaHostAlloc)\n");
    }

    checkCudaErrors(cudaSetDevice(idev));

    /* Verify the selected device supports mapped memory and set the device
       flags for mapping host memory. */

    checkCudaErrors(cudaGetDeviceProperties(&deviceProp, idev));

    if (!deviceProp.canMapHostMemory)
    {
        fprintf(stderr, "Device %d does not support mapping CPU host memory!\n", idev);

        exit(EXIT_SUCCESS);
    }

    checkCudaErrors(cudaSetDeviceFlags(cudaDeviceMapHost));

    /* Allocate mapped CPU memory. */

    nelem = 1048576;
    bytes = nelem * sizeof(float);

    if (bPinGenericMemory)
    {
        a_UA = (float*)malloc(bytes + MEMORY_ALIGNMENT);
        b_UA = (float*)malloc(bytes + MEMORY_ALIGNMENT);
        c_UA = (float*)malloc(bytes + MEMORY_ALIGNMENT);

        // We need to ensure memory is aligned to 4K (so we will need to padd memory
        // accordingly)
        a = (float*)ALIGN_UP(a_UA, MEMORY_ALIGNMENT);
        b = (float*)ALIGN_UP(b_UA, MEMORY_ALIGNMENT);
        c = (float*)ALIGN_UP(c_UA, MEMORY_ALIGNMENT);

        checkCudaErrors(cudaHostRegister(a, bytes, cudaHostRegisterMapped));
        checkCudaErrors(cudaHostRegister(b, bytes, cudaHostRegisterMapped));
        checkCudaErrors(cudaHostRegister(c, bytes, cudaHostRegisterMapped));
    }
    else
    {
        flags = cudaHostAllocMapped;
        checkCudaErrors(cudaHostAlloc((void**)&a, bytes, flags));
        checkCudaErrors(cudaHostAlloc((void**)&b, bytes, flags));
        checkCudaErrors(cudaHostAlloc((void**)&c, bytes, flags));
    }

    /* Initialize the vectors. */
    for (n = 0; n < nelem; n++)
    {
        a[n] = rand() / (float)RAND_MAX;
        b[n] = rand() / (float)RAND_MAX;
    }

    // Get the device pointers for the pinned CPU memory mapped into the GPU memory space.

    checkCudaErrors(cudaHostGetDevicePointer((void**)&d_a, (void*)a, 0));
    checkCudaErrors(cudaHostGetDevicePointer((void**)&d_b, (void*)b, 0));
    checkCudaErrors(cudaHostGetDevicePointer((void**)&d_c, (void*)c, 0));

    // Call the GPU kernel using the CPU pointers residing in CPU mapped memory.
    printf("> vectorAddGPU kernel will add vectors using mapped CPU memory...\n");
    dim3 block(256);
    dim3 grid((unsigned int)ceil(nelem / (float)block.x));
    vectorAddGPU << <grid, block >> > (d_a, d_b, d_c, nelem);
    checkCudaErrors(cudaDeviceSynchronize());
    getLastCudaError("vectorAddGPU() execution failed");

    /* Compare the results */

    printf("> Checking the results from vectorAddGPU() ...\n");
    errorNorm = 0.f;
    refNorm = 0.f;

    for (n = 0; n < nelem; n++)
    {
        ref = a[n] + b[n];
        diff = c[n] - ref;
        errorNorm += diff * diff;
        refNorm += ref * ref;
    }

    errorNorm = (float)sqrt((double)errorNorm);
    refNorm = (float)sqrt((double)refNorm);

    /* Memory clean up */

    printf("> Releasing CPU memory...\n");

    if (bPinGenericMemory)
    {
        checkCudaErrors(cudaHostUnregister(a));
        checkCudaErrors(cudaHostUnregister(b));
        checkCudaErrors(cudaHostUnregister(c));
        free(a_UA);
        free(b_UA);
        free(c_UA);
    }
    else
    {
        checkCudaErrors(cudaFreeHost(a));
        checkCudaErrors(cudaFreeHost(b));
        checkCudaErrors(cudaFreeHost(c));
    }

    printf("CUDART_VERSION = %d\n", CUDART_VERSION);

    printf("CUDART version %d.%d\n", CUDART_VERSION / 1000, (CUDART_VERSION % 100) / 10);

    exit(errorNorm / refNorm < 1.e-6f ? EXIT_SUCCESS : EXIT_FAILURE);
}

