#ifndef CONVOLUTIONTEXTURE_COMMON_H
#define CONVOLUTIONTEXTURE_COMMON_H

#include <cuda_runtime.h>

////////////////////////////////////////////////////////////////////////////////
// Convolution kernel size (the only parameter inlined in the code)
////////////////////////////////////////////////////////////////////////////////
#define KERNEL_RADIUS 8
#define KERNEL_LENGTH (2 * KERNEL_RADIUS + 1)

////////////////////////////////////////////////////////////////////////////////
// Reference CPU convolution
////////////////////////////////////////////////////////////////////////////////
extern "C" void convolutionRowsCPU(float* h_Dst, float* h_Src, float* h_Kernel, int imageW, int imageH, int kernelR);

extern "C" void convolutionColumnsCPU(float* h_Dst, float* h_Src, float* h_Kernel, int imageW, int imageH, int kernelR);

////////////////////////////////////////////////////////////////////////////////
// GPU texture-based convolution
////////////////////////////////////////////////////////////////////////////////
extern "C" void setConvolutionKernel(float* h_Kernel);

extern "C" void convolutionRowsGPU(float* d_Dst, cudaArray * a_Src, int imageW, int imageH, cudaTextureObject_t texSrc);

extern "C" void convolutionColumnsGPU(float* d_Dst, cudaArray * a_Src, int imageW, int imageH, cudaTextureObject_t texSrc);

#endif
