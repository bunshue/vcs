#include <helper_cuda.h>

__global__ void cudaProcess(int* g_odata, int imgw)
{
	
	int tx = threadIdx.x;	//0~15
	int ty = threadIdx.y;	//0~15
	int bw = blockDim.x;	//16
	int bh = blockDim.y;	//16

	//blockIdx.x 0~31
	//blockIdx.y 0~31

	int x = blockIdx.x * bw + tx;
	int y = blockIdx.y * bh + ty;

	//printf("tx = %d, ty = %d, bw = %d, bh = %d, x = %d, y = %d\n", tx, ty, bw, bh, x, y);
	//printf("xx = %d, yy = %d\n", blockIdx.x, blockIdx.y);

	int rr = x % 256;
	int gg = y % 256;
	int bb = 0;

	g_odata[y * imgw + x] = (bb << 16) | (gg << 8) | rr;
}

extern "C" void launch_cudaProcess(dim3 grid, dim3 block, int sbytes, int* g_odata, int imgw)
{
	cudaProcess << <grid, block, sbytes >> > (g_odata, imgw);
}


