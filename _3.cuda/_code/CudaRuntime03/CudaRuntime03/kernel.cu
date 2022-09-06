#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#define N 256
#include <stdio.h>

__global__ void vecAdd(int* a, int* b, int* c)
{
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
}
int main()
{
    int a[N], b[N], c[N];
    int* dev_a, * dev_b, * dev_c;
    // initialize a and b with real values (NOT SHOWN)
    int size = N * sizeof(int);
    cudaMalloc((void**)&dev_a, size);
    cudaMalloc((void**)&dev_b, size);
    cudaMalloc((void**)&dev_c, size);

    cudaMemcpy(dev_a, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(dev_b, b, size, cudaMemcpyHostToDevice);

    vecAdd << <1, N >> > (dev_a, dev_b, dev_c);
    //         1 block, N threads


    cudaMemcpy(c, dev_c, size, cudaMemcpyDeviceToHost);

    cudaFree(dev_a);
    cudaFree(dev_b);
    cudaFree(dev_c);

    return 0;
}
