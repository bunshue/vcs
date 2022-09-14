//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>

typedef unsigned int uint;
typedef unsigned char uchar;

void PrintArray(float* data, int n);
void PrintArray(int* data, int n);
void PrintArray(uchar* data, int n);
void RandomInit(float*, int);
void RandomInit(int*, int);
void init_input(float* a, size_t size);

float RandFloat(float low, float high)
{
    float t = (float)rand() / (float)RAND_MAX;
    return (1.0f - t) * low + t * high;
}

int main()
{
    printf("測cuda訊息用\n");

    int i;
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

    uchar* h_Data;
    //uint byteCount = 64 * 1048576;
    uint byteCount = 64 * 1024;

    printf("...allocating CPU memory.\n");
    h_Data = (uchar*)malloc(byteCount);

    PrintArray(h_Data, 100);

    printf("...generating input data\n");
    //srand(2009);

    for (i = 0; i < byteCount; i++)
    {
        h_Data[i] = rand() % 256;
    }

    PrintArray(h_Data, 100);

    free(h_Data);


    printf("測試RandFloat\n");
    int DATA_N = 100;
    float* h_AA;

    int DATA_SZ = DATA_N * sizeof(float);

    h_AA = (float*)malloc(DATA_SZ);

    PrintArray(h_AA, 100);

    // Generating input data on CPU
    for (i = 0; i < DATA_N; i++)
    {
        h_AA[i] = RandFloat(0.0f, 1.0f);
    }
    PrintArray(h_AA, 100);

    free(h_AA);




    int random_r;
    int random_g;
    int random_b;

    for (i = 0; i < 100; i++)
    {
        random_r = rand() % 10 - 5;
        random_g = rand() % 10 - 5;
        random_b = rand() % 10 - 5;

        printf("(%d, %d, %d) ", random_r, random_g, random_b);
    }
    printf("\n");


    printf("random 測試 0~1中間的小數\n");
    for (i = 0; i < 10; i++)
    {
        float f;
        f = (float)rand() / (float)RAND_MAX;
        printf("i = %4d\t%g\n", i, f);
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

void PrintArray(uchar* data, int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%3d ", data[i]);
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

