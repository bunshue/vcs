#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <helper_gl.h>

// includes, cuda
#include <vector_types.h>
#include <cuda_runtime.h>
#include <cuda_gl_interop.h>

// CUDA utilities and system includes
#include <helper_cuda.h>
#include <helper_functions.h>
#include <vector_types.h>

typedef unsigned int uint;
typedef unsigned char uchar;

const uint width = 512;
const uint height = 512;

#define MAX(a, b) ((a > b) ? a : b)

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    // use command-line specified CUDA device, otherwise use device with highest Gflops/s
    int cuda_device = findCudaDevice(argc, (const char**)argv);
    // check the compute capability of the device
    int num_devices = 0;
    checkCudaErrors(cudaGetDeviceCount(&num_devices));

    if (num_devices == 0)
    {
        printf("your system does not have a CUDA capable device, waiving test...\n");
        return EXIT_WAIVED;
    }

    // check if the command-line chosen device ID is within range, exit if not
    if (cuda_device >= num_devices)
    {
        printf("cuda_device=%d is invalid, must choose device ID between 0 and %d\n", cuda_device, num_devices - 1);
        return EXIT_FAILURE;
    }
    checkCudaErrors(cudaSetDevice(cuda_device));

    // Checking for compute capabilities
    cudaDeviceProp deviceProp;
    checkCudaErrors(cudaGetDeviceProperties(&deviceProp, cuda_device));
    printf("Device: <%s> canMapHostMemory: %s\n", deviceProp.name,deviceProp.canMapHostMemory ? "Yes" : "No");

    if (deviceProp.canMapHostMemory == 0)
    {
        printf("Using cudaMallocHost, CUDA device does not support mapping of generic host memory\n");
        //bPinGenericMemory = false;
    }

    // This will pick the best possible CUDA capable device
    //cudaDeviceProp deviceProp;
    int devID = findCudaDevice(argc, (const char**)argv);

    if (devID < 0)
    {
        printf("exiting...\n");
        exit(EXIT_SUCCESS);
    }

    checkCudaErrors(cudaGetDeviceProperties(&deviceProp, devID));
    if (!deviceProp.managedMemory)
    {
        // This sample requires being run on a device that supports Unified Memory
        fprintf(stderr, "Unified Memory not supported on this device\n");
        exit(EXIT_WAIVED);
    }

    // This sample requires being run on a device that supports Cooperative Kernel
// Launch
    if (!deviceProp.cooperativeLaunch)
    {
        printf("\nSelected GPU (%d) does not support Cooperative Kernel Launch, Waiving the run\n", devID);
        exit(EXIT_WAIVED);
    }

    // Statistics about the GPU device
    printf("> GPU device has %d Multi-Processors, SM %d.%d compute capabilities\n\n",        deviceProp.multiProcessorCount, deviceProp.major, deviceProp.minor);

    int numSms = deviceProp.multiProcessorCount;
    printf("numSms = %d\n", numSms);

    float scale_factor = 1.0f;

    scale_factor =        MAX((32.0f / (_ConvertSMVer2Cores(deviceProp.major, deviceProp.minor) *            (float)deviceProp.multiProcessorCount)),            1.0f);
    int n = 16 * 1024 * 1024;      // number of ints in the data set
    n = (int)rint((float)n / scale_factor);

    printf("> CUDA Capable: SM %d.%d hardware\n", deviceProp.major,
        deviceProp.minor);
    printf("> %d Multiprocessor(s) x %d (Cores/Multiprocessor) = %d (Cores)\n",
        deviceProp.multiProcessorCount,
        _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor),
        _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor) *
        deviceProp.multiProcessorCount);

    printf("> scale_factor = %1.4f\n", 1.0f / scale_factor);
    printf("> array_size   = %d\n\n", n);


    // Find/set the device.
// The test requires an architecture SM35 or greater (CDP capable).
    cuda_device = findCudaDevice(argc, (const char**)argv);
    cudaDeviceProp deviceProps;
    checkCudaErrors(cudaGetDeviceProperties(&deviceProps, cuda_device));
    int cdpCapable = (deviceProps.major == 3 && deviceProps.minor >= 5) || deviceProps.major >= 4;

    printf("GPU device %s has compute capabilities (SM %d.%d)\n", deviceProps.name, deviceProps.major, deviceProps.minor);

    if (!cdpCapable)
    {
        std::cerr << "cdpQuadTree requires SM 3.5 or higher to use CUDA Dynamic Parallelism.  Exiting...\n" << std::endl;
        exit(EXIT_WAIVED);
    }

    printf("warpSize = %d\n", deviceProps.warpSize);

    printf("ª©¥»¸ê°T\n");
    //printf("Header version:  %u.%u\n", NVMEDIA_2D_VERSION_MAJOR, NVMEDIA_2D_VERSION_MINOR);
    printf("CUDART_VERSION : %d\n", CUDART_VERSION);
    //printf("__CUDA_API_VERSION : %d\n", __CUDA_API_VERSION);
    //printf("NVTX_VERSION : %d\n", NVTX_VERSION);
    printf("GL_VERSION : %d\n", GL_VERSION);


#if __CUDA_ARCH__ >= 800
    printf("111111111111111111\n");
#else
    printf("222222222222222222222\n");
#endif

#if defined(__arm__) || defined(__aarch64__)
    printf("Not supported on ARM\n");
#else
    printf("Supported on __arm__ / __aarch64__\n");
#endif

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
    printf("WIN32 _WIN32 WIN64 _WIN64\n");
#endif

#if defined(__APPLE__) || defined(MACOSX)
    printf("__APPLE__  MACOSX");
#else
    printf("XXXX __APPLE__  MACOSX\n");
#endif



    exit(EXIT_SUCCESS);
}



