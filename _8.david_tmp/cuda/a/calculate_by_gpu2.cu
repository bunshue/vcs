#include <iostream>
#include <math.h>
// Kernel function to add the elements of two arrays
__global__
void add(int n, float *x, float *y)
{
  int index = threadIdx.x;
  int stride = blockDim.x;
  for (int i = index; i < n; i += stride)
      y[i] = x[i] + y[i];

  for (int j = index; j < n; j += stride)
  {
      for (int i = index; i < (n-stride); i += stride)
      {
          y[i] = sqrt(x[j] * y[i+stride]);
      }

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
  for (int i = 0; i < N; i++) {
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

  // Free memory
  cudaFree(x);
  cudaFree(y);
  
  std::cout << "OK" << std::endl;
  
  return 0;
}
