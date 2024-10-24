#include <stdlib.h>
#include <stdio.h>


// Managed variable declaration is an extra annotation with __device__
__device__ __managed__  int  x;
__global__  void  kernel() {
    // Reference "x" directly - it's a normal variable on the GPU.
    printf( "GPU sees: x = %d\n" , x);
} 
int  main() {
    // Set "x" from Host code. Note it's just a normal variable on the CPU.
    x = 1234;
 
    // Launch a kernel which uses "x" from the GPU.
    kernel<<< 1, 1 >>>(); 
    cudaDeviceSynchronize(); 
    return  0;
}

