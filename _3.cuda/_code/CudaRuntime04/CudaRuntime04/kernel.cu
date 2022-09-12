
#include "cuda_runtime.h"
#include "device_launch_parameters.h"

//CUDA Runtime API

//下列的範例是以相較於 Driver API 來說比較簡便的 CUDA Runtime API （頁面存檔備份，存於網際網路檔案館） 做列向量的加法：

// 本範例修改自Nvidia官方的CUDA開發指引: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#kernels
// 編譯指令 nvcc vector_add.cu -arch=native -o vector_add.exe
// -arch=native 代表將 device code 編譯成當前電腦 Nvidia GPU 架構的機器碼，拿掉就是照預設編譯成 PTX 中間碼。

#include <stdio.h>
#include <stdlib.h>     //# 引用動態分配 malloc、隨機函數 rand() 和隨機上限 RAND_MAX

typedef unsigned char byte;

#define N 100 // 列向量長度

// Device code: 送入GPU執行的部分

__global__ void VecAdd(byte* A, byte* B, byte* C)
{
	//int kk = blockDim.x * blockIdx.x + threadIdx.x;
	//printf("_%2d%2d%2d%3d\n", blockDim.x, blockIdx.x, threadIdx.x, kk);

	int tid = threadIdx.x; // thread 的 x 座標

	//printf("%4d", tid);

	//C[tid] = (A[tid] + B[tid]) % 256; // 每個 thread 作一次加法	//若使用N個thread, 則每個thread只要做一次加法

	int i;
	for (i = 0; i < 10; i++)
	{
		C[tid*10+i] = (A[tid * 10 + i] + B[tid * 10 + i]) % 256; // 每個 thread 作10次加法	//若使用N/10個thread, 則每個thread要做10次加法
	}

}

// Host code: 送入CPU執行的部分

void printData(byte* h_A, byte* h_B, byte* h_C, int len);

int main()
{
	size_t size = N * sizeof(byte); // 向量的實際大小，以位元組(bytes)為單位

	int i; // 迴圈計數

	// 動態分配位於"host(CPU) 記憶體" 的向量
	byte* h_A = (byte*)malloc(size);
	byte* h_B = (byte*)malloc(size);
	byte* h_C = (byte*)malloc(size);

	// 隨機初始化輸入向量
	for (i = 0; i < N; i++)
	{
		h_A[i] = (byte)(i % 256);
		h_B[i] = (byte)(i % 256);
		h_C[i] = 0;
	}

	printf("size = %d\n", size);
	printf("old\n");
	printData(h_A, h_B, h_C, N);

	// 動態分配位於"device(GPU) 記憶體"的向量
	byte* d_A;
	cudaMalloc(&d_A, size); // cudaError_t cudaMalloc ( void** devPtr, size_t size )
	byte* d_B;
	cudaMalloc(&d_B, size);
	byte* d_C;
	cudaMalloc(&d_C, size);

	// 將向量從 CPU 複製到 GPU
	cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
	cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

	// 將 device code 送入 GPU 並執行，執行時一個 Grid 只有一個 block ，一個 block 有 N 個 thread
	VecAdd << <1, N/10 >> > (d_A, d_B, d_C);	//會執行50次

	// 將算好的向量從 GPU 複製到 CPU
	cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

	// 印出運算結果
	printf("new\n");
	printData(h_A, h_B, h_C, N);

	// 釋放 GPU 記憶體
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);

	// 釋放 CPU 記憶體
	free(h_A);
	free(h_B);
	free(h_C);
}

void printData(byte* h_A, byte* h_B, byte* h_C, int len)
{
	for (int i = 0; i < len; i++)
	{
		printf("%4d", h_A[i]);
	}
	printf("\n");
	for (int i = 0; i < len; i++)
	{
		printf("%4d", h_B[i]);
	}
	printf("\n");
	for (int i = 0; i < len; i++)
	{
		printf("%4d", h_C[i]);
	}
	printf("\n");
}



