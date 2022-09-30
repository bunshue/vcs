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

#define MAX_EPSILON_ERROR 5e-3f

// Define the files that are to be save and the reference images for validation
const char* imageFilename = "teapot512.pgm";
const char* refFilename = "ref_rotated.pgm";

////////////////////////////////////////////////////////////////////////////////
// Constants
const float angle = 0.5f;  // angle to rotate image by (in radians)

// Auto-Verification Code
bool testResult = true;

////////////////////////////////////////////////////////////////////////////////
//! Transform an image using texture lookups
//! @param outputData  output data in global memory
////////////////////////////////////////////////////////////////////////////////
__global__ void transformKernel(float* outputData, int width, int height, float theta, cudaTextureObject_t tex)
{
    // calculate normalized texture coordinates
    unsigned int x = blockIdx.x * blockDim.x + threadIdx.x;
    unsigned int y = blockIdx.y * blockDim.y + threadIdx.y;

    float u = (float)x - (float)width / 2;
    float v = (float)y - (float)height / 2;
    float tu = u * cosf(theta) - v * sinf(theta);
    float tv = v * cosf(theta) + u * sinf(theta);

    tu /= (float)width;
    tv /= (float)height;

    // read from texture and write to global memory
    outputData[y * width + x] = tex2D<float>(tex, tu + 0.5f, tv + 0.5f);
}

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    int devID = findCudaDevice(argc, (const char**)argv);

    // load image from disk
    float* hData = NULL;
    unsigned int width, height;

    printf("imageFilename = %s\n", imageFilename);
    char* imagePath = sdkFindFilePath(imageFilename, argv[0]);

    if (imagePath == NULL)
    {
        printf("Unable to source image file: %s\n", imageFilename);
        exit(EXIT_FAILURE);
    }
    printf("imageFilename : %s\n", imagePath);

    sdkLoadPGM(imagePath, &hData, &width, &height);

    unsigned int size = width * height * sizeof(float);
    printf("Loaded '%s', %d x %d pixels\n", imageFilename, width, height);

    // Load reference image from image (output)
    float* hDataRef = (float*)malloc(size);

    printf("refFilename = %s\n", refFilename);
    char* refPath = sdkFindFilePath(refFilename, argv[0]);
    printf("refFilename : %s\n", refPath);

    if (refPath == NULL)
    {
        printf("Unable to find reference image file: %s\n", refFilename);
        exit(EXIT_FAILURE);
    }

    sdkLoadPGM(refPath, &hDataRef, &width, &height);

    // Allocate device memory for result
    float* dData = NULL;
    checkCudaErrors(cudaMalloc((void**)&dData, size));

    // Allocate array and copy image data
    cudaChannelFormatDesc channelDesc = cudaCreateChannelDesc(32, 0, 0, 0, cudaChannelFormatKindFloat);
    cudaArray* cuArray;
    checkCudaErrors(cudaMallocArray(&cuArray, &channelDesc, width, height));
    checkCudaErrors(cudaMemcpyToArray(cuArray, 0, 0, hData, size, cudaMemcpyHostToDevice));

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

    dim3 dimBlock(8, 8, 1);
    dim3 dimGrid(width / dimBlock.x, height / dimBlock.y, 1);

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

    checkCudaErrors(cudaDeviceSynchronize());
    sdkStopTimer(&timer);
    printf("Processing time: %f (ms)\n", sdkGetTimerValue(&timer));
    printf("%.2f Mpixels/sec\n", (width * height / (sdkGetTimerValue(&timer) / 1000.0f)) / 1e6);
    sdkDeleteTimer(&timer);

    // Allocate mem for the result on host side
    float* hOutputData = (float*)malloc(size);
    // copy result from device to host
    checkCudaErrors(cudaMemcpy(hOutputData, dData, size, cudaMemcpyDeviceToHost));

    // Write result to file
    char outputFilename[1024];
    strcpy(outputFilename, imagePath);
    strcpy(outputFilename + strlen(imagePath) - 4, "_out.pgm");

    sdkSavePGM(outputFilename, hOutputData, width, height);

    printf("outputFilename = %s\n", outputFilename);

    sdkWriteFile<float>("./dump_data.dat", hOutputData, width * height, 0.0f, false);

    // We need to reload the data from disk,
    // because it is inverted upon output
    sdkLoadPGM(outputFilename, &hOutputData, &width, &height);

    printf("Comparing files\n");
    printf("\toutput:    <%s>\n", outputFilename);
    printf("\treference: <%s>\n", refPath);

    testResult = compareData(hOutputData, hDataRef, width * height, MAX_EPSILON_ERROR, 0.15f);

    checkCudaErrors(cudaDestroyTextureObject(tex));
    checkCudaErrors(cudaFree(dData));
    checkCudaErrors(cudaFreeArray(cuArray));
    free(imagePath);
    free(refPath);

    printf("Completed, returned %s\n", testResult ? "OK" : "ERROR!");
    exit(testResult ? EXIT_SUCCESS : EXIT_FAILURE);
}

