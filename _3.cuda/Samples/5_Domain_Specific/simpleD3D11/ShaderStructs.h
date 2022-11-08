#pragma once

//#include "stdafx.h"
#include <cuda_runtime.h>
#include <DirectXMath.h>
#include "helper_cuda.h"

using namespace DirectX;

struct Vertex
{
	XMFLOAT3 position;
	XMFLOAT4 color;
};

void RunSineWaveKernel(size_t mesh_width, size_t mesh_height, Vertex* cudaDevVertptr, cudaStream_t streamToRun, float AnimTime);