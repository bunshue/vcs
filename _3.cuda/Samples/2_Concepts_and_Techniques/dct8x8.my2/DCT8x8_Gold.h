/**
**************************************************************************
* \file DCT8x8_Gold.h
* \brief Contains declaration of CPU versions of DCT, IDCT and quantization
* routines.
*
* Contains declaration of CPU versions of DCT, IDCT and quantization
* routines.
*/

#pragma once

#include "BmpUtil.h"

extern "C" {
	void computeDCT8x8Gold1(const float* fSrc, float* fDst, int Stride, ROI Size);
	void computeIDCT8x8Gold1(const float* fSrc, float* fDst, int Stride, ROI Size);
	void quantizeGoldFloat(float* fSrcDst, int Stride, ROI Size);
	void quantizeGoldShort(short* fSrcDst, int Stride, ROI Size);
	void computeDCT8x8Gold2(const float* fSrc, float* fDst, int Stride, ROI Size);
	void computeIDCT8x8Gold2(const float* fSrc, float* fDst, int Stride, ROI Size);
}
