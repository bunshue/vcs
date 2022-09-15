__global__ void Copy(TColor* dst, int imageW, int imageH, cudaTextureObject_t texImage)
{
    const int ix = blockDim.x * blockIdx.x + threadIdx.x;
    const int iy = blockDim.y * blockIdx.y + threadIdx.y;
    // Add half of a texel to always address exact texel centers
    const float x = (float)ix + 0.5f;
    const float y = (float)iy + 0.5f;

    if (ix < imageW && iy < imageH)
    {
        float4 fresult = tex2D<float4>(texImage, x, y);
        dst[imageW * iy + ix] = make_color(fresult.x, fresult.y, fresult.z, 0);
    }
}

extern "C" void cuda_Copy(TColor * d_dst, int imageW, int imageH, cudaTextureObject_t texImage)
{
    dim3 threads(BLOCKDIM_X, BLOCKDIM_Y);
    dim3 grid(iDivUp(imageW, BLOCKDIM_X), iDivUp(imageH, BLOCKDIM_Y));

    Copy << <grid, threads >> > (d_dst, imageW, imageH, texImage);
}


__global__ void Mix(TColor* dst, int alpha, int imageW, int imageH, cudaTextureObject_t texImage1, cudaTextureObject_t texImage2)
{
    const int ix = blockDim.x * blockIdx.x + threadIdx.x;
    const int iy = blockDim.y * blockIdx.y + threadIdx.y;

    if (ix < imageW && iy < imageH)
    {
        float4 fresult1 = tex2D<float4>(texImage1, ix, iy);
        float4 fresult2 = tex2D<float4>(texImage2, ix, iy);

        dst[imageW * iy + ix] = make_color(
            (fresult1.x * (100 - alpha) + fresult2.x * alpha) / 100,
            (fresult1.y * (100 - alpha) + fresult2.y * alpha) / 100,
            (fresult1.z * (100 - alpha) + fresult2.z * alpha) / 100,
            0);
    }
}

extern "C" void cuda_Mix(TColor * d_dst, int alpha, int imageW, int imageH, cudaTextureObject_t texImage1, cudaTextureObject_t texImage2)
{
    dim3 threads(BLOCKDIM_X, BLOCKDIM_Y);
    dim3 grid(iDivUp(imageW, BLOCKDIM_X), iDivUp(imageH, BLOCKDIM_Y));

    Mix << <grid, threads >> > (d_dst, alpha, imageW, imageH, texImage1, texImage2);
}
