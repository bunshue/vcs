#include <stdio.h>

__global__ void addVectorsInto(float *result, float *a, float *b, int N)
{
  int index = threadIdx.x + blockIdx.x * blockDim.x;
  int stride = blockDim.x * gridDim.x;

  for(int i = index; i < N; i += stride)
    result[i] = a[i] + b[i];
}

void initWith(float num, float *a, int N)
{
	for(int i=0;i<N;i++)
	{
		a[i]=num;
	
	}


}

int main()
{
  const int N = 2<<24;
  size_t size = N * sizeof(float);

  float *a;
  float *b;
  float *c;

  cudaMallocManaged(&a, size);
  cudaMallocManaged(&b, size);
  cudaMallocManaged(&c, size);

  initWith(3, a, N);	//??代?不再?述。就是在CPU下位???初值。
  initWith(4, b, N);
  initWith(0, c, N);

  addVectorsInto<<<1, 1>>>(c, a, b, N);
  cudaDeviceSynchronize();

  cudaFree(a);
  cudaFree(b);
  cudaFree(c);
}

