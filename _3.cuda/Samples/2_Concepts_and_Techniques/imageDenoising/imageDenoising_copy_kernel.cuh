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
