#ifndef CONVOLUTIONFFT2D_COMMON_H
#define CONVOLUTIONFFT2D_COMMON_H

typedef unsigned int uint;

#ifdef __CUDACC__
typedef float2 fComplex;
#else
typedef struct {
    float x;
    float y;
} fComplex;
#endif

////////////////////////////////////////////////////////////////////////////////
// Helper functions
////////////////////////////////////////////////////////////////////////////////
// Round a / b to nearest higher integer value
inline int iDivUp(int a, int b) { return (a % b != 0) ? (a / b + 1) : (a / b); }

// Align a to nearest higher multiple of b
inline int iAlignUp(int a, int b) { return (a % b != 0) ? (a - a % b + b) : a; }

extern "C" void convolutionClampToBorderCPU(float* h_Result, float* h_Data, float* h_Kernel, int dataH,
    int dataW, int kernelH, int kernelW, int kernelY, int kernelX);

extern "C" void padKernel(float* d_PaddedKernel, float* d_Kernel, int fftH,
    int fftW, int kernelH, int kernelW, int kernelY, int kernelX);

extern "C" void padDataClampToBorder(float* d_PaddedData, float* d_Data, int fftH, int fftW, int dataH, int dataW,
    int kernelH, int kernelW, int kernelY, int kernelX);

extern "C" void modulateAndNormalize(fComplex * d_Dst, fComplex * d_Src, int fftH, int fftW, int padding);

extern "C" void spPostprocess2D(void* d_Dst, void* d_Src, uint DY, uint DX, uint padding, int dir);

extern "C" void spPreprocess2D(void* d_Dst, void* d_Src, uint DY, uint DX, uint padding, int dir);

extern "C" void spProcess2D(void* d_Data, void* d_Data0, void* d_Kernel0, uint DY, uint DX, int dir);

#endif  // CONVOLUTIONFFT2D_COMMON_H
