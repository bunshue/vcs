#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Paint a 3D texture with a gradient in X (blue) and Z (green), and have every
 * other Z slice have full red.
 */
__global__ void cuda_kernel_texture_volume(unsigned char* surface, int width, int height, int depth, size_t pitch, size_t pitchSlice)
{
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    // in the case where, due to quantization into grids, we have
    // more threads than pixels, skip the threads which don't correspond to valid pixels
    if (x >= width || y >= height) return;

    // walk across the Z slices of this texture.  it should be noted that
    // this is far from optimal data access.
    for (int z = 0; z < depth; ++z)
    {
        // get a pointer to this pixel
        unsigned char* pixel = surface + z * pitchSlice + y * pitch + 4 * x;
        pixel[0] = 255 * x / (width - 1);  // blue
        pixel[1] = 255 * z / (depth - 1);  // green
        pixel[2] = 255 * (z % 2);          // red
        pixel[3] = 255;                    // alpha
    }
}

extern "C" void cuda_texture_volume(void* surface, int width, int height, int depth, size_t pitch, size_t pitchSlice, float t)
{
    cudaError_t error = cudaSuccess;

    dim3 Db = dim3(16, 16);  // block dimensions are fixed to be 256 threads
    dim3 Dg = dim3((width + Db.x - 1) / Db.x, (height + Db.y - 1) / Db.y);

    cuda_kernel_texture_volume << <Dg, Db >> > ((unsigned char*)surface, width, height, depth, pitch, pitchSlice);

    error = cudaGetLastError();

    if (error != cudaSuccess)
    {
        printf("cuda_kernel_texture_volume() failed to launch error = %d\n", error);
    }
}
