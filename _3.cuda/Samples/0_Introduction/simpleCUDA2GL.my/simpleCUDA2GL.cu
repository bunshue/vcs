#include <helper_cuda.h>

// clamp x to range [a, b]
__device__ float clamp(float x, float a, float b) { return max(a, min(b, x)); }

__device__ int clamp(int x, int a, int b) { return max(a, min(b, x)); }

// convert floating point rgb color to 8-bit integer
__device__ int rgbToInt(float r, float g, float b)
{
	r = clamp(r, 0.0f, 255.0f);
	g = clamp(g, 0.0f, 255.0f);
	b = clamp(b, 0.0f, 255.0f);
	return (int(b) << 16) | (int(g) << 8) | int(r);
}

__global__ void cudaProcess(unsigned int* g_odata, int imgw)
{
	extern __shared__ uchar4 sdata[];

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

	unsigned char rr;
	unsigned char gg;
	unsigned char bb;
	unsigned char aa;

	if ((y & 0x20) > 0)
	{
		rr = 100;
	}
	else
	{
		rr = 0;
	}

	gg = 0;

	if ((x & 0x20) > 0)
	{
		bb = 100;
	}
	else
	{
		bb = 0;
	}

	aa = 255;

	//uchar4 c4 = make_uchar4((x & 0x20) ? 100 : 0, 0, (y & 0x20) ? 100 : 0, 0);

	//                      B   G   R   A
	uchar4 c4 = make_uchar4(bb, gg, rr, aa);

	//                                R      G    B
	//g_odata[y * imgw + x] = rgbToInt(c4.z, c4.y, c4.x);
	//g_odata[y * imgw + x] = rgbToInt(c4.z, c4.y, c4.x);
	g_odata[y * imgw + x] = rgbToInt(x % 256, y % 256, 0);

	//g_odata[y * imgw + x] = rgbToInt(0, 255, 0);

	//g_odata[y * imgw + x] = rgbToInt(0, 0, 255);
}

//¯}¸Ñ¥Î
__global__ void cudaProcess_my(unsigned int* g_odata, int imgw)
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

	g_odata[y * imgw + x] = rgbToInt(x % 256, y % 256, 0);
}

__global__ void cudaProcess2(unsigned int* g_odata, int imgw)
{
	extern __shared__ uchar4 sdata[];

	int tx = threadIdx.x;
	int ty = threadIdx.y;
	int bw = blockDim.x;
	int bh = blockDim.y;
	int x = blockIdx.x * bw + tx;
	int y = blockIdx.y * bh + ty;

	unsigned char rr;
	unsigned char gg;
	unsigned char bb;
	unsigned char aa;

	rr = 255;
	gg = 0;
	bb = 0;
	aa = 255;

	//                      B   G   R   A
	uchar4 c4 = make_uchar4(bb, gg, rr, aa);

	int i;
	if (imgw > 200)
	{
		for (i = 0; i < 1048576 / 2; i++)
		{
			//                                R      G    B
			//g_odata[j * imgw + i] = rgbToInt(c4.z, c4.y, c4.x);

			//g_odata[i] = rgbToInt(200, 0, 0);
		}
	}
}

extern "C" void launch_cudaProcess(dim3 grid, dim3 block, int sbytes, unsigned int* g_odata, int imgw)
{
	//cudaProcess << <grid, block, sbytes >> > (g_odata, imgw);

	cudaProcess_my << <grid, block, sbytes >> > (g_odata, imgw);

	//cudaProcess2 << <1, 1, 0 >> > (g_odata, imgw);
}

extern "C" void launch_cudaProcess2(unsigned int* g_odata, int imgw)
{
	//cudaProcess2 << <1, 1, 0 >> > (g_odata, imgw);
}



