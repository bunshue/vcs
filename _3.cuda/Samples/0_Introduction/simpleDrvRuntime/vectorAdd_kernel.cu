/* Vector addition: C = A + B.
 *
 * This sample is a very basic sample that implements element by element
 * vector addition. It is the same as the sample illustrating Chapter 3
 * of the programming guide with some additions like error checking.
 *
 */

// Device code
extern "C" __global__ void VecAdd_kernel(const float *A, const float *B,
                                         float *C, int N) {
  int i = blockDim.x * blockIdx.x + threadIdx.x;

  if (i < N) C[i] = A[i] + B[i];
}
