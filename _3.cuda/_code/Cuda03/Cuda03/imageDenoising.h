#ifndef IMAGE_DENOISING_H
#define IMAGE_DENOISING_H

typedef unsigned int TColor;

////////////////////////////////////////////////////////////////////////////////
// Filter configuration
////////////////////////////////////////////////////////////////////////////////
#define KNN_WINDOW_RADIUS 3
#define NLM_WINDOW_RADIUS 3
#define NLM_BLOCK_RADIUS 3
#define KNN_WINDOW_AREA \
  ((2 * KNN_WINDOW_RADIUS + 1) * (2 * KNN_WINDOW_RADIUS + 1))
#define NLM_WINDOW_AREA \
  ((2 * NLM_WINDOW_RADIUS + 1) * (2 * NLM_WINDOW_RADIUS + 1))
#define INV_KNN_WINDOW_AREA (1.0f / (float)KNN_WINDOW_AREA)
#define INV_NLM_WINDOW_AREA (1.0f / (float)NLM_WINDOW_AREA)

#define KNN_WEIGHT_THRESHOLD 0.02f
#define KNN_LERP_THRESHOLD 0.79f
#define NLM_WEIGHT_THRESHOLD 0.10f
#define NLM_LERP_THRESHOLD 0.10f

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

extern "C" cudaTextureObject_t texImage;

extern "C" cudaError_t CUDA_MallocArray(uchar4 * *h_Src, int imageW, int imageH);
extern "C" cudaError_t CUDA_FreeArray();

// CUDA kernel functions
extern "C" void cuda_Copy(TColor * d_dst, int imageW, int imageH,
    cudaTextureObject_t texImage);
#endif
