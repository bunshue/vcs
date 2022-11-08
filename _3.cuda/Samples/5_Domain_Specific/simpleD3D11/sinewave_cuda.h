#ifndef SINEWAVE_CUDA_H
#define SINEWAVE_CUDA_H

#include <stdio.h>
#include "ShaderStructs.h"
#include "helper_cuda.h"

void RunSineWaveKernel(cudaExternalSemaphore_t& extSemaphore, uint64_t& key, unsigned int timeoutMs, size_t mesh_width, size_t mesh_height, Vertex* cudaDevVertptr, cudaStream_t streamToRun);
Vertex* cudaImportVertexBuffer(void* sharedHandle, cudaExternalMemory_t& externalMemory, int meshWidth, int meshHeight);
void cudaImportKeyedMutex(void* sharedHandle, cudaExternalSemaphore_t& extSemaphore);
#endif
