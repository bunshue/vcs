#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <helper_functions.h>
#include <helper_cuda.h>

////////////////////////////////////////////////////////////////////////////////
// Reference CPU FWT
////////////////////////////////////////////////////////////////////////////////
extern "C" void fwtCPU(float* h_Output, float* h_Input, int log2N);
extern "C" void slowWTcpu(float* h_Output, float* h_Input, int log2N);
extern "C" void dyadicConvolutionCPU(float* h_Result, float* h_Data, float* h_Kernel, int log2dataN, int log2kernelN);

////////////////////////////////////////////////////////////////////////////////
// GPU FWT
////////////////////////////////////////////////////////////////////////////////
#include "fastWalshTransform_kernel.cuh"

////////////////////////////////////////////////////////////////////////////////
// Data configuration
////////////////////////////////////////////////////////////////////////////////
const int log2Kernel = 7;
const int log2Data = 23;

const int dataN = 1 << log2Data;
const int kernelN = 1 << log2Kernel;

const int DATA_SIZE = dataN * sizeof(float);
const int KERNEL_SIZE = kernelN * sizeof(float);

const double NOPS = 3.0 * (double)dataN * (double)log2Data / 2.0;

////////////////////////////////////////////////////////////////////////////////
// Main program
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char* argv[])
{
    float* h_Data, * h_Kernel, * h_ResultCPU, * h_ResultGPU;
    float* d_Data, * d_Kernel;
    double delta, ref, sum_delta2, sum_ref2, L2norm, gpuTime;

    StopWatchInterface* hTimer = NULL;
    int i;

    printf("Starting...\n\n");

    // use command-line specified CUDA device, otherwise use device with highest Gflops/s
    findCudaDevice(argc, (const char**)argv);

    sdkCreateTimer(&hTimer);

    printf("Initializing data...\n");
    printf("...allocating CPU memory\n");
    h_Kernel = (float*)malloc(KERNEL_SIZE);
    h_Data = (float*)malloc(DATA_SIZE);
    h_ResultCPU = (float*)malloc(DATA_SIZE);
    h_ResultGPU = (float*)malloc(DATA_SIZE);

    printf("...allocating GPU memory\n");
    checkCudaErrors(cudaMalloc((void**)&d_Kernel, DATA_SIZE));
    checkCudaErrors(cudaMalloc((void**)&d_Data, DATA_SIZE));

    printf("...generating data\n");
    printf("Data length: %i; kernel length: %i\n", dataN, kernelN);
    srand(2007);

    for (i = 0; i < kernelN; i++)
    {
        h_Kernel[i] = (float)rand() / (float)RAND_MAX;
    }

    for (i = 0; i < dataN; i++)
    {
        h_Data[i] = (float)rand() / (float)RAND_MAX;
    }

    checkCudaErrors(cudaMemset(d_Kernel, 0, DATA_SIZE));
    checkCudaErrors(cudaMemcpy(d_Kernel, h_Kernel, KERNEL_SIZE, cudaMemcpyHostToDevice));
    checkCudaErrors(cudaMemcpy(d_Data, h_Data, DATA_SIZE, cudaMemcpyHostToDevice));

    printf("Running GPU dyadic convolution using Fast Walsh Transform...\n");
    checkCudaErrors(cudaDeviceSynchronize());
    sdkResetTimer(&hTimer);
    sdkStartTimer(&hTimer);
    fwtBatchGPU(d_Data, 1, log2Data);
    fwtBatchGPU(d_Kernel, 1, log2Data);
    modulateGPU(d_Data, d_Kernel, dataN);
    fwtBatchGPU(d_Data, 1, log2Data);
    checkCudaErrors(cudaDeviceSynchronize());
    sdkStopTimer(&hTimer);
    gpuTime = sdkGetTimerValue(&hTimer);

    printf("GPU time: %f ms; GOP/s: %f\n", gpuTime, NOPS / (gpuTime * 0.001 * 1E+9));

    printf("Reading back GPU results...\n");
    checkCudaErrors(cudaMemcpy(h_ResultGPU, d_Data, DATA_SIZE, cudaMemcpyDeviceToHost));

    printf("Running straightforward CPU dyadic convolution...\n");
    dyadicConvolutionCPU(h_ResultCPU, h_Data, h_Kernel, log2Data, log2Kernel);

    printf("Comparing the results...\n");
    sum_delta2 = 0;
    sum_ref2 = 0;

    for (i = 0; i < dataN; i++)
    {
        delta = h_ResultCPU[i] - h_ResultGPU[i];
        ref = h_ResultCPU[i];
        sum_delta2 += delta * delta;
        sum_ref2 += ref * ref;
    }

    L2norm = sqrt(sum_delta2 / sum_ref2);

    printf("Shutting down...\n");
    sdkDeleteTimer(&hTimer);
    checkCudaErrors(cudaFree(d_Data));
    checkCudaErrors(cudaFree(d_Kernel));
    free(h_ResultGPU);
    free(h_ResultCPU);
    free(h_Data);
    free(h_Kernel);

    printf("L2 norm: %E\n", L2norm);
    printf(L2norm < 1e-6 ? "Test passed\n" : "Test failed!\n");
}
