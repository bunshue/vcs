#ifndef IMAGE_DENOISING_H
#define IMAGE_DENOISING_H

typedef unsigned int TColor;

////////////////////////////////////////////////////////////////////////////////
// Filter configuration
////////////////////////////////////////////////////////////////////////////////

#define BLOCKDIM_X 8
#define BLOCKDIM_Y 8

#ifndef MAX
#define MAX(a, b) ((a < b) ? b : a)
#endif
#ifndef MIN
#define MIN(a, b) ((a < b) ? a : b)
#endif

// functions to load images
extern "C" void LoadBMPFile(uchar4 * *dst, int* width, int* height, const char* name);

// CUDA wrapper functions for allocation/freeing texture arrays

extern "C" cudaTextureObject_t texImage1;
extern "C" cudaTextureObject_t texImage2;

extern "C" cudaError_t CUDA_MallocArray(cudaTextureObject_t * texImage, uchar4 * *h_Src, int imageW, int imageH);
extern "C" cudaError_t CUDA_FreeArray();

// CUDA kernel functions
extern "C" void cuda_Copy(TColor * d_dst, int imageW, int imageH, cudaTextureObject_t texImage);
extern "C" void cuda_Mix(TColor * d_dst, int alpha, int imageW, int imageH, cudaTextureObject_t texImage1, cudaTextureObject_t texImage2);
extern "C" void cuda_Wave(TColor * d_dst, int alpha, int imageW, int imageH);

#endif
