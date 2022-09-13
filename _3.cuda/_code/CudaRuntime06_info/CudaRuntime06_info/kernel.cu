//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>

void PrintArray(float* data, int n);
void PrintArray(int* data, int n);
void RandomInit(float*, int);
void RandomInit(int*, int);

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
