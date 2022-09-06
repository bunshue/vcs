#include <iostream>
#include <math.h>
// Kernel function to add the elements of two arrays
__global__
void add(int n, float *x, float *y)
{
  int index = threadIdx.x;
  int stride = blockDim.x;

  printf("index = %d\tn=%d\tstride = %d\n", index, n, stride);
  
  for (int i = index; i < n; i += stride)
  {
      y[i] = x[i] + y[i];
  }
}

int main(void)
{
  int N = 1<<16;
  
  std::cout << "N = " <<N <<std::endl;
  
  float *x, *y;

  // Allocate Unified Memory ¡V accessible from CPU or GPU
  cudaMallocManaged(&x, N*sizeof(float));
  cudaMallocManaged(&y, N*sizeof(float));

  // initialize x and y arrays on the host
  for (int i = 0; i < N; i++)
  {
    x[i] = 3.0f;
    y[i] = 7.0f;
  }

  // Run kernel on 1M elements on the GPU
  add<<<1, 256>>>(N, x, y);

  // Wait for GPU to finish before accessing on host
  cudaDeviceSynchronize();

  // Check for errors (all values should be 3.0f)
  float maxError = 0.0f;
  for (int i = 0; i < N; i++)
    maxError = fmax(maxError, fabs(y[i]-3.0f));
  //std::cout << "Max error: " << maxError << std::endl;
  
  
  for (int i = 0; i < 10; i++)
  {
    printf("x[%d] = %f\t", i, x[i]);
    printf("y[%d] = %f\n", i, y[i]);
  }
  
  

  // Free memory
  cudaFree(x);
  cudaFree(y);
  
  std::cout << "OK" << std::endl;
  
  return 0;
}
