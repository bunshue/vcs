#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <helper_cuda.h>

#include "imageDenoising.h"

////////////////////////////////////////////////////////////////////////////////
// Helper functions
////////////////////////////////////////////////////////////////////////////////
float Max(float x, float y) { return (x > y) ? x : y; }

float Min(float x, float y) { return (x < y) ? x : y; }

int iDivUp(int a, int b) { return ((a % b) != 0) ? (a / b + 1) : (a / b); }

__device__ float lerpf(float a, float b, float c) { return a + (b - a) * c; }

__device__ float vecLen(float4 a, float4 b)
{
    return ((b.x - a.x) * (b.x - a.x) + (b.y - a.y) * (b.y - a.y) +
        (b.z - a.z) * (b.z - a.z));
}

__device__ TColor make_color(float r, float g, float b, float a)
{
    return ((int)(a * 255.0f) << 24) | ((int)(b * 255.0f) << 16) | ((int)(g * 255.0f) << 8) | ((int)(r * 255.0f) << 0);
}

////////////////////////////////////////////////////////////////////////////////
// Global data handlers and parameters
////////////////////////////////////////////////////////////////////////////////
// Texture object and channel descriptor for image texture
cudaTextureObject_t texImage;
cudaChannelFormatDesc uchar4tex = cudaCreateChannelDesc<uchar4>();

// CUDA array descriptor
cudaArray* a_Src;

////////////////////////////////////////////////////////////////////////////////
// Filtering kernels
////////////////////////////////////////////////////////////////////////////////
#include "imageDenoising_copy_kernel.cuh"

extern "C" cudaError_t CUDA_MallocArray(uchar4 * *h_Src, int imageW, int imageH)
{
    cudaError_t error;

    error = cudaMallocArray(&a_Src, &uchar4tex, imageW, imageH);
    error = cudaMemcpy2DToArray(a_Src, 0, 0, *h_Src, sizeof(uchar4) * imageW, sizeof(uchar4) * imageW, imageH, cudaMemcpyHostToDevice);

    cudaResourceDesc texRes;
    memset(&texRes, 0, sizeof(cudaResourceDesc));

    texRes.resType = cudaResourceTypeArray;
    texRes.res.array.array = a_Src;

    cudaTextureDesc texDescr;
    memset(&texDescr, 0, sizeof(cudaTextureDesc));

    texDescr.normalizedCoords = false;
    texDescr.filterMode = cudaFilterModeLinear;
    texDescr.addressMode[0] = cudaAddressModeWrap;
    texDescr.addressMode[1] = cudaAddressModeWrap;
    texDescr.readMode = cudaReadModeNormalizedFloat;

    checkCudaErrors(cudaCreateTextureObject(&texImage, &texRes, &texDescr, NULL));

    return error;
}

extern "C" cudaError_t CUDA_FreeArray() { return cudaFreeArray(a_Src); }
