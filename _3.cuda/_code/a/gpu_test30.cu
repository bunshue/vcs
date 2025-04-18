#include <stdlib.h>
#include <stdio.h>

__device__ __managed__ int x, y=2;
__global__  void  kernel() {
    x = 10;
}
int main() {
    cudaStream_t stream1;
    cudaStreamCreate(&stream1);
    cudaStreamAttachMemAsync(stream1, &x);// Associate “x” with stream1.
    cudaDeviceSynchronize();              // Wait for “x” attachment to occur.
    kernel<<< 1, 1, 0, stream1 >>>();     // Note: Launches into stream1.
    y = 20;                               // ERROR: “y” is still associated globally 
                                          // with all streams by default
    return  0;
}



