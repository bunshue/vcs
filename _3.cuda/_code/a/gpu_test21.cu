#include <stdlib.h>
#include <stdio.h>

struct S {
 int *ptr;
 S() : ptr(nullptr) { }
 S(const S &) { cudaMallocManaged(&ptr, sizeof(int)); }
 ~S() { cudaFree(ptr); }
};

__global__ void foo(S in) {
 
  //error: This store may write to memory that has already been
  //       freed (see below).
  *(in.ptr) = 4;
 
}

int main() {
 S V;
 
 /* The object 'V' is first copied by value to a compiler-generated
  * stub function that does the kernel launch, and the stub function
  * bitwise copies the contents of the argument to kernel parameter
  * memory.
  * However, GPU kernel execution is asynchronous with host
  * execution. 
  * As a result, S::~S() will execute when the stub function   returns, releasing allocated memory, even though the kernel may not have finished execution.
  */
 foo<<<1,1>>>(V);
 cudaDeviceSynchronize();
}




