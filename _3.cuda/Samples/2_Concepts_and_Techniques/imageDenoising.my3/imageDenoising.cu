#include <helper_cuda.h>

typedef unsigned int TColor;

extern "C" cudaTextureObject_t texImage;

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
