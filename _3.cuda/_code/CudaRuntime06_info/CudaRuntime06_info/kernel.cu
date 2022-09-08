//#include "cuda_runtime.h"
//#include "device_launch_parameters.h"

#include <stdio.h>

int main()
{
    printf("測cuda訊息用\n");

    cudaError_t cudaStatus;




    // cudaDeviceReset must be called before exiting in order for profiling and
    // tracing tools such as Nsight and Visual Profiler to show complete traces.
    cudaStatus = cudaDeviceReset();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDeviceReset failed!");
        return 1;
    }

    return 0;
}

