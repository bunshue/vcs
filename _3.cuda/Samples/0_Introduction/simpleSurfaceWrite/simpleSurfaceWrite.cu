/*
 * This sample demonstrates how use texture fetches in CUDA
 *
 * This sample takes an input PGM image (imageFilename) and generates
 * an output PGM image (imageFilename_out).  This CUDA kernel performs
 * a simple 2D transform (rotation) on the texture coordinates (u,v).
 */

 // Includes, system
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <math.h>

#ifdef _WIN32
#define WINDOWS_LEAN_AND_MEAN
#define NOMINMAX
#include <windows.h>
#endif

// Includes CUDA
#include <cuda_runtime.h>

// Utilities and timing functions
#include <helper_functions.h>  // includes cuda.h and cuda_runtime_api.h

// CUDA helper functions
#include <helper_cuda.h>  // helper functions for CUDA error check

#define MIN_EPSILON_ERROR 5e-3f

////////////////////////////////////////////////////////////////////////////////
// Define the files that are to be save and the reference images for validation
const char* imageFilename = "teapot512.pgm";
const char* refFilename = "ref_rotated.pgm";
float angle = 0.5f;  // angle to rotate image by (in radians)

// Auto-Verification Code
bool testResult = true;

////////////////////////////////////////////////////////////////////////////////
// Kernels
////////////////////////////////////////////////////////////////////////////////
//! Write to a cuArray (texture data source) using surface writes
//! @param gIData input data in global memory
////////////////////////////////////////////////////////////////////////////////
__global__ void surfaceWriteKernel(float* gIData, int width, int height, cudaSurfaceObject_t outputSurface)
{
    // calculate surface coordinates
    unsigned int x = blockIdx.x * blockDim.x + threadIdx.x;
    unsigned int y = blockIdx.y * blockDim.y + threadIdx.y;

    // read from global memory and write to cuarray (via surface reference)
    surf2Dwrite(gIData[y * width + x], outputSurface, x * 4, y, cudaBoundaryModeTrap);
}

////////////////////////////////////////////////////////////////////////////////
//! Transform an image using texture lookups
//! @param gOData  output data in global memory
////////////////////////////////////////////////////////////////////////////////
__global__ void transformKernel(float* gOData, int width, int height, float theta, cudaTextureObject_t tex)
{
    // calculate normalized texture coordinates
    unsigned int x = blockIdx.x * blockDim.x + threadIdx.x;
    unsigned int y = blockIdx.y * blockDim.y + threadIdx.y;

    float u = x / (float)width;
    float v = y / (float)height;

    // transform coordinates
    u -= 0.5f;
    v -= 0.5f;
    float tu = u * cosf(theta) - v * sinf(theta) + 0.5f;
    float tv = v * cosf(theta) + u * sinf(theta) + 0.5f;

    // read from texture and write to global memory
    gOData[y * width + x] = tex2D<float>(tex, tu, tv);
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    printf("Starting...\n");

    // Use command-line specified CUDA device,
// otherwise use device with highest Gflops/s
    int devID = findCudaDevice(argc, (const char**)argv);

    // Get number of SMs on this GPU
    cudaDeviceProp deviceProps;

    checkCudaErrors(cudaGetDeviceProperties(&deviceProps, devID));
    printf("CUDA device [%s] has %d Multi-Processors, SM %d.%d\n\n", deviceProps.name, deviceProps.multiProcessorCount, deviceProps.major, deviceProps.minor);

    // Load image from disk
    float* hData = NULL;
    unsigned int width, height;
    char* imagePath = sdkFindFilePath(imageFilename, argv[0]);

    printf("imagePath : %s\n", imagePath);

    if (imagePath == NULL)
    {
        printf("Unable to source image input file: %s\n", imageFilename);
        exit(EXIT_FAILURE);
    }

    sdkLoadPGM(imagePath, &hData, &width, &height);

    unsigned int size = width * height * sizeof(float);
    printf("Loaded '%s', %d x %d pixels\n\n", imageFilename, width, height);

    // Load reference image from image (output)
    float* hDataRef = (float*)malloc(size);
    char* refPath = sdkFindFilePath(refFilename, argv[0]);
    printf("refPath : %s\n", refPath);

    if (refPath == NULL)
    {
        printf("Unable to find reference image file: %s\n", refFilename);
        exit(EXIT_FAILURE);
    }
    sdkLoadPGM(refPath, &hDataRef, &width, &height);

    printf("Loaded '%s', %d x %d pixels\n\n", refPath, width, height);

    // Allocate device memory for result
    float* dData = NULL;
    checkCudaErrors(cudaMalloc((void**)&dData, size));

    // Allocate array and copy image data
    cudaChannelFormatDesc channelDesc = cudaCreateChannelDesc(32, 0, 0, 0, cudaChannelFormatKindFloat);
    cudaArray* cuArray;
    checkCudaErrors(cudaMallocArray(&cuArray, &channelDesc, width, height, cudaArraySurfaceLoadStore));

    dim3 dimBlock(8, 8, 1);
    dim3 dimGrid(width / dimBlock.x, height / dimBlock.y, 1);

    cudaSurfaceObject_t outputSurface;
    cudaResourceDesc surfRes;
    memset(&surfRes, 0, sizeof(cudaResourceDesc));
    surfRes.resType = cudaResourceTypeArray;
    surfRes.res.array.array = cuArray;

    checkCudaErrors(cudaCreateSurfaceObject(&outputSurface, &surfRes));
#if 1
    checkCudaErrors(cudaMemcpy(dData, hData, size, cudaMemcpyHostToDevice));
    surfaceWriteKernel << <dimGrid, dimBlock >> > (dData, width, height, outputSurface);
#else  // This is what differs from the example simpleTexture
    checkCudaErrors(cudaMemcpyToArray(cuArray, 0, 0, hData, size, cudaMemcpyHostToDevice));
#endif

    cudaTextureObject_t tex;
    cudaResourceDesc texRes;
    memset(&texRes, 0, sizeof(cudaResourceDesc));

    texRes.resType = cudaResourceTypeArray;
    texRes.res.array.array = cuArray;

    cudaTextureDesc texDescr;
    memset(&texDescr, 0, sizeof(cudaTextureDesc));

    texDescr.normalizedCoords = true;
    texDescr.filterMode = cudaFilterModeLinear;
    texDescr.addressMode[0] = cudaAddressModeWrap;
    texDescr.addressMode[1] = cudaAddressModeWrap;
    texDescr.readMode = cudaReadModeElementType;

    checkCudaErrors(cudaCreateTextureObject(&tex, &texRes, &texDescr, NULL));

    // Warmup
    transformKernel << <dimGrid, dimBlock, 0 >> > (dData, width, height, angle, tex);

    checkCudaErrors(cudaDeviceSynchronize());

    StopWatchInterface* timer = NULL;
    sdkCreateTimer(&timer);
    sdkStartTimer(&timer);

    // Execute the kernel
    transformKernel << <dimGrid, dimBlock, 0 >> > (dData, width, height, angle, tex);

    // Check if kernel execution generated an error
    getLastCudaError("Kernel execution failed");

    cudaDeviceSynchronize();
    sdkStopTimer(&timer);
    printf("Processing time: %f (ms)\n", sdkGetTimerValue(&timer));
    printf("%.2f Mpixels/sec\n", (width * height / (sdkGetTimerValue(&timer) / 1000.0f)) / 1e6);
    sdkDeleteTimer(&timer);

    // Allocate mem for the result on host side
    float* hOData = (float*)malloc(size);
    // copy result from device to host
    checkCudaErrors(cudaMemcpy(hOData, dData, size, cudaMemcpyDeviceToHost));

    // Write result to file
    char outputFilename[1024];
    strcpy(outputFilename, "output.pgm");
    sdkSavePGM("output.pgm", hOData, width, height);
    printf("outputFilename : %s\n", outputFilename);

    // Write regression file if necessary
    if (checkCmdLineFlag(argc, (const char**)argv, "regression"))
    {
        // Write file for regression test
        sdkWriteFile<float>("./data/regression.dat", hOData, width * height, 0.0f, false);
    }
    else
    {
        // We need to reload the data from disk,
        // because it is inverted upon output
        sdkLoadPGM(outputFilename, &hOData, &width, &height);

        printf("Comparing files\n");
        printf("\toutput:    <%s>\n", outputFilename);
        printf("\treference: <%s>\n", refPath);
        testResult = compareData(hOData, hDataRef, width * height, MIN_EPSILON_ERROR, 0.0f);
    }

    checkCudaErrors(cudaDestroySurfaceObject(outputSurface));
    checkCudaErrors(cudaDestroyTextureObject(tex));
    checkCudaErrors(cudaFree(dData));
    checkCudaErrors(cudaFreeArray(cuArray));
    free(imagePath);
    free(refPath);





    printf("Completed, returned %s\n", testResult ? "OK" : "ERROR!");

    exit(testResult ? EXIT_SUCCESS : EXIT_FAILURE);
}

