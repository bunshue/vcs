/*
 * Copyright 1993-2012 NVIDIA Corporation.  All rights reserved.
 *
 * NOTICE TO USER:
 *
 * This source code is subject to NVIDIA ownership rights under U.S. and
 * international Copyright laws.  Users and possessors of this source code
 * are hereby granted a nonexclusive, royalty-free license to use this code
 * in individual and commercial software.
 *
 * NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOURCE
 * CODE FOR ANY PURPOSE.  IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR
 * IMPLIED WARRANTY OF ANY KIND.  NVIDIA DISCLAIMS ALL WARRANTIES WITH
 * REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
 * IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL,
 * OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
 * OF USE, DATA OR PROFITS,  WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
 * OR OTHER TORTIOUS ACTION,  ARISING OUT OF OR IN CONNECTION WITH THE USE
 * OR PERFORMANCE OF THIS SOURCE CODE.
 *
 * U.S. Government End Users.   This source code is a "commercial item" as
 * that term is defined at  48 C.F.R. 2.101 (OCT 1995), consisting  of
 * "commercial computer  software"  and "commercial computer software
 * documentation" as such terms are  used in 48 C.F.R. 12.212 (SEPT 1995)
 * and is provided to the U.S. Government only as a commercial end item.
 * Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through
 * 227.7202-4 (JUNE 1995), all U.S. Government End Users acquire the
 * source code with only those rights set forth herein.
 *
 * Any use of this source code in individual and commercial software must
 * include, in the user documentation and internal comments to the code,
 * the above Disclaimer and U.S. Government End Users Notice.
 */

/* Matrix multiplication: C = A * B.
 * Device code.
 */

#ifndef _MATRIXMUL_KERNEL_H_
#define _MATRIXMUL_KERNEL_H_

#include <stdio.h>

#define CHECK_BANK_CONFLICTS 0
#if CHECK_BANK_CONFLICTS
#define AS(i, j) cutilBankChecker(((float*)&As[0][0]), (block_size * i + j))
#define BS(i, j) cutilBankChecker(((float*)&Bs[0][0]), (block_size * i + j))
#else
#define AS(i, j) As[i][j]
#define BS(i, j) Bs[i][j]
#endif

////////////////////////////////////////////////////////////////////////////////
//! Matrix multiplication on the device: C = A * B
//! wA is A's width and wB is B's width
////////////////////////////////////////////////////////////////////////////////
template <int block_size, typename size_type> __device__ void
matrixMul(float *C, float *A, float *B, size_type wA, size_type wB)
{
    // Block index
    size_type bx = blockIdx.x;
    size_type by = blockIdx.y;

    // Thread index
    size_type tx = threadIdx.x;
    size_type ty = threadIdx.y;

    // Index of the first sub-matrix of A processed by the block
    size_type aBegin = wA * block_size * by;

    // Index of the last sub-matrix of A processed by the block
    size_type aEnd   = aBegin + wA - 1;

    // Step size used to iterate through the sub-matrices of A
    size_type aStep  = block_size;

    // Index of the first sub-matrix of B processed by the block
    size_type bBegin = block_size * bx;

    // Step size used to iterate through the sub-matrices of B
    size_type bStep  = block_size * wB;

    // Csub is used to store the element of the block sub-matrix
    // that is computed by the thread
    float Csub = 0;

    // Loop over all the sub-matrices of A and B
    // required to compute the block sub-matrix
    for (size_type a = aBegin, b = bBegin;
         a <= aEnd;
         a += aStep, b += bStep)
    {

        // Declaration of the shared memory array As used to
        // store the sub-matrix of A
        __shared__ float As[block_size][block_size];

        // Declaration of the shared memory array Bs used to
        // store the sub-matrix of B
        __shared__ float Bs[block_size][block_size];

        // Load the matrices from device memory
        // to shared memory; each thread loads
        // one element of each matrix
        AS(ty, tx) = A[a + wA * ty + tx];
        BS(ty, tx) = B[b + wB * ty + tx];

        // Synchronize to make sure the matrices are loaded
        __syncthreads();

        // Multiply the two matrices together;
        // each thread computes one element
        // of the block sub-matrix
#pragma unroll

        for (size_type k = 0; k < block_size; ++k)
            Csub += AS(ty, k) * BS(k, tx);

        // Synchronize to make sure that the preceding
        // computation is done before loading two new
        // sub-matrices of A and B in the next iteration
        __syncthreads();
    }

    // Write the block sub-matrix to device memory;
    // each thread writes one element
    size_type c = wB * block_size * by + block_size * bx;
    C[c + wB * ty + tx] = Csub;
}

// C wrappers around our template kernel
extern "C" __global__ void matrixMul_bs16_32bit(float *C, float *A, float *B, int wA, int wB)
{
    matrixMul<16, int>(C, A, B, wA, wB);
}
extern "C" __global__ void matrixMul_bs16_64bit(float *C, float *A, float *B, size_t wA, size_t wB)
{
    matrixMul<16, size_t>(C, A, B, wA, wB);
}
extern "C" __global__ void matrixMul_bs32_32bit(float *C, float *A, float *B, int wA, int wB)
{
    matrixMul<32, int>(C, A, B, wA, wB);
}
extern "C" __global__ void matrixMul_bs32_64bit(float *C, float *A, float *B, size_t wA, size_t wB)
{
    matrixMul<32, size_t>(C, A, B, wA, wB);
}

#endif // #ifndef _MATRIXMUL_KERNEL_H_
