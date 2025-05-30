#ifndef __H_RESIZE_CONVERT__
#define __H_RESIZE_CONVERT__

#include <iostream>
#include <helper_cuda.h>

// nv12 resize
extern "C"
void resizeNV12Batch(
    uint8_t * dpSrc, int nSrcPitch, int nSrcWidth, int nSrcHeight,
    uint8_t * dpDst, int nDstPitch, int nDstWidth, int nDstHeight,
    int nBatchSize, cudaStream_t stream = 0);

// bgr resize
extern "C"
void resizeBGRplanarBatch(
    float* dpSrc, int nSrcPitch, int nSrcWidth, int nSrcHeight,
    float* dpDst, int nDstPitch, int nDstWidth, int nDstHeight,
    int nBatchSize, cudaStream_t stream = 0,
    int cropX = 0, int cropY = 0, int cropW = 0, int cropH = 0,
    bool whSameResizeRatio = false);

//NV12 to bgr planar
extern "C"
void nv12ToBGRplanarBatch(uint8_t * pNv12, int nNv12Pitch,
    float* pRgb, int nRgbPitch, int nWidth, int nHeight,
    int nBatchSize, cudaStream_t stream = 0);
#endif
