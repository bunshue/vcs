#include "cuda_runtime.h"
#include "device_launch_parameters.h"

#define N 256
#include <stdio.h>

typedef unsigned char byte;

__global__ void vecAdd(byte* a, byte* b, byte* c)
{
    int i = threadIdx.x;
    //c[i] = a[i] + b[i];
    c[i] = (a[i] + b[i])%256;
}

// Maximum value that can be returned by the rand function:
#define RAND_MAX 0x7fff

_ACRTIMP void __cdecl srand(_In_ unsigned int _Seed);

_Check_return_ _ACRTIMP int __cdecl rand(void);

#if defined _CRT_RAND_S || defined _CRTBLD
_ACRTIMP errno_t __cdecl rand_s(_Out_ unsigned int* _RandomValue);
#endif

int main()
{
    int a[N], b[N], c[N];

    int size = N * sizeof(byte);

    byte* data1;
    byte* data2;
    byte* data3;

    cudaMalloc((void**)&data1, size);
    cudaMalloc((void**)&data2, size);
    cudaMalloc((void**)&data3, size);

    for (int i = 0; i < N; i++)
    {
        a[i] = (i % 256);
        b[i] = (i % 256);
        c[i] = 0x17;
    }

    for (int i = 0; i < 10; i++)
    {
        printf("a[%d] = %d\tb[%d] = %d\tc[%d] = %d\n", i, a[i], i, b[i], i, c[i]);
    }

    cudaMemcpy(data1, a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(data2, b, size, cudaMemcpyHostToDevice);

    vecAdd << <1, N >> > (data1, data2, data3);
    //         1 block, N threads

    cudaMemcpy(c, data3, size, cudaMemcpyDeviceToHost);

    for (int i = 0; i < 10; i++)
    {
        printf("a[%d] = %d\tb[%d] = %d\tc[%d] = %d\n", i, a[i], i, b[i], i, c[i]);
    }

    cudaFree(data1);
    cudaFree(data2);
    cudaFree(data3);

    //固定種子之random

    srand(200);

    byte data[1000];

    for (int i = 0; i < 1000; i++)
    {
        data[i] = rand() % 256;
    }

    for (int i = 0; i < 1000; i++)
    {
        printf("%d ", data[i]);
        if ((i % 32) == 31)
            printf("\n");
    }
    printf("\n");




    return 0;
}
