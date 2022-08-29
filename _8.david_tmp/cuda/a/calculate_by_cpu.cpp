#include <iostream>
#include <math.h>

// function to add the elements of two arrays
void add(int n, float *x, float *y)
{
  for (int i = 0; i < n; i ++)
  {
      y[i] = x[i] + y[i];
  }
  //float z = sqrt(5);

  for (int j = 0; j < n; j ++)
  {
      for (int i = 0; i < (n-1); i ++)
      {
          y[i] = sqrt(x[j] * y[i+1]);
      }

  }



}

int main(void)
{
  int N = 1<<16;	//1M elements

  std::cout << "N = " <<N <<std::endl;

  float *x = new float[N];
  float *y = new float[N];

  // initialize x and y arrays on the host
  for (int i = 0; i < N; i++) {
    x[i] = 3.0f;
    y[i] = 7.0f;
  }

  // Run kernel on 1M elements on the CPU
  add(N, x, y);

  // Free memory
  delete [] x;
  delete [] y;

  std::cout << "OK" << std::endl;

  return 0;
}
