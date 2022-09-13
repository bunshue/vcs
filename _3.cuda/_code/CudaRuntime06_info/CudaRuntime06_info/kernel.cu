//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>

void PrintArray(float* data, int n);
void PrintArray(int* data, int n);
void RandomInit(float*, int);
void RandomInit(int*, int);
void init_input(float* a, size_t size);

int main()
{
    printf("測cuda訊息用\n");

    int N = 100;

    size_t size = N * sizeof(float);
    float* h_A;
    h_A = (float*)malloc(size);
    PrintArray(h_A, N);
    RandomInit(h_A, N);
    PrintArray(h_A, N);

    size = N * sizeof(int);
    int* h_B;
    h_B = (int*)malloc(size);
    PrintArray(h_B, N);
    RandomInit(h_B, N);
    PrintArray(h_B, N);


    // Free host memory
    if (h_A)
    {
        free(h_A);
    }
    if (h_B)
    {
        free(h_B);
    }



    size = 1 << 24;  // number of elements to reduce

    size_t maxBlocks = 512;

    printf("%zu elements\n", size);

    float* inputVec_h = NULL;

    cudaMallocHost(&inputVec_h, sizeof(float) * size);


    init_input(inputVec_h, size);


    printf("david0913: %s:%s(%d) ST\n", __FILE__, __func__, __LINE__);
    printf("david0913: %s:%s(%d) ST\n", __FILE__, __FUNCTION__, __LINE__);

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
    printf("有定義\n");
#else
    printf("無定義\n");
#endif


    cudaError_t cudaStatus;




    // cudaDeviceReset must be called before exiting in order for profiling and
    // tracing tools such as Nsight and Visual Profiler to show complete traces.
    cudaStatus = cudaDeviceReset();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDeviceReset failed!");
        return 1;
    }

    return 0;
}

void PrintArray(float* data, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%g ", data[i]);
        if ((i % 10) == 9)
            printf("\n");
    }
    printf("\n");
}

void PrintArray(int* data, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", data[i]);
        if ((i % 10) == 9)
            printf("\n");
    }
    printf("\n");
}

// Allocates an array with random float entries.
void RandomInit(float* data, int n)
{
    for (int i = 0; i < n; i++)
    {
        data[i] = rand() / (float)RAND_MAX;
    }
}

// Allocates an array with random float entries.
void RandomInit(int* data, int n)
{
    for (int i = 0; i < n; i++)
    {
        //data[i] = rand() / (int)RAND_MAX;
        data[i] = rand() % 10000;
    }
}


void init_input(float* a, size_t size)
{
    for (size_t i = 0; i < size; i++)
    {
        a[i] = (rand() & 0xFF) / (float)RAND_MAX;
    }
}




