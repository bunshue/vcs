#include "Common.h"
#include "BmpUtil.h"

/**
*  The number of DCT kernel calls
*/
#define BENCHMARK_SIZE 10

/**
*  The PSNR values over this threshold indicate images equality
*/
#define PSNR_THRESHOLD_EQUAL 40

// includes kernels
#include "dct8x8_kernel1.cuh"
#include "dct8x8_kernel_quantization.cuh"

/**
**************************************************************************
*  Wrapper function for 1st CUDA version of DCT, quantization and IDCT
*implementations
*
* \param ImgSrc         [IN] - Source byte image plane
* \param ImgDst         [IN] - Quantized result byte image plane
* \param Stride         [IN] - Stride for both source and result planes
* \param Size           [IN] - Size of both planes
*
* \return Execution time in milliseconds
*/
float WrapperCUDA1(byte* ImgSrc, byte* ImgDst, int Stride, ROI Size)
{
    // prepare channel format descriptor for passing texture into kernels
    cudaChannelFormatDesc floattex = cudaCreateChannelDesc<float>();

    // allocate device memory
    cudaArray* Src;
    float* Dst;
    size_t DstStride;
    checkCudaErrors(cudaMallocArray(&Src, &floattex, Size.width, Size.height));
    checkCudaErrors(cudaMallocPitch((void**)(&Dst), &DstStride, Size.width * sizeof(float), Size.height));
    DstStride /= sizeof(float);

    // convert source image to float representation
    int ImgSrcFStride;
    float* ImgSrcF = MallocPlaneFloat(Size.width, Size.height, &ImgSrcFStride);
    CopyByte2Float(ImgSrc, Stride, ImgSrcF, ImgSrcFStride, Size);
    AddFloatPlane(-128.0f, ImgSrcF, ImgSrcFStride, Size);

    // copy from host memory to device
    checkCudaErrors(cudaMemcpy2DToArray(Src, 0, 0, ImgSrcF, ImgSrcFStride * sizeof(float), Size.width * sizeof(float), Size.height, cudaMemcpyHostToDevice));

    // setup execution parameters
    dim3 threads(BLOCK_SIZE, BLOCK_SIZE);
    dim3 grid(Size.width / BLOCK_SIZE, Size.height / BLOCK_SIZE);

    // create and start CUDA timer
    StopWatchInterface* timerCUDA = 0;
    sdkCreateTimer(&timerCUDA);
    sdkResetTimer(&timerCUDA);

    // execute DCT kernel and benchmark
    cudaTextureObject_t TexSrc;
    cudaResourceDesc texRes;
    memset(&texRes, 0, sizeof(cudaResourceDesc));

    texRes.resType = cudaResourceTypeArray;
    texRes.res.array.array = Src;

    cudaTextureDesc texDescr;
    memset(&texDescr, 0, sizeof(cudaTextureDesc));

    texDescr.normalizedCoords = false;
    texDescr.filterMode = cudaFilterModeLinear;
    texDescr.addressMode[0] = cudaAddressModeWrap;
    texDescr.addressMode[1] = cudaAddressModeWrap;
    texDescr.readMode = cudaReadModeElementType;

    checkCudaErrors(cudaCreateTextureObject(&TexSrc, &texRes, &texDescr, NULL));

    printf("Size.width = %d\n", Size.width);
    printf("Size.height = %d\n", Size.height);
    for (int i = 0; i < BENCHMARK_SIZE; i++)
    {
        sdkStartTimer(&timerCUDA);
        CUDAkernel1DCT << <grid, threads >> > (Dst, (int)DstStride, 0, 0, TexSrc);
        checkCudaErrors(cudaDeviceSynchronize());
        sdkStopTimer(&timerCUDA);
    }

    getLastCudaError("Kernel execution failed");

    // finalize CUDA timer
    float TimerCUDASpan = sdkGetAverageTimerValue(&timerCUDA);
    sdkDeleteTimer(&timerCUDA);

    // execute Quantization kernel
    CUDAkernelQuantizationFloat << <grid, threads >> > (Dst, (int)DstStride);
    getLastCudaError("Kernel execution failed");

    // copy quantized coefficients from host memory to device array
    checkCudaErrors(cudaMemcpy2DToArray(Src, 0, 0, Dst, DstStride * sizeof(float), Size.width * sizeof(float), Size.height, cudaMemcpyDeviceToDevice));

    // execute IDCT kernel
    CUDAkernel1IDCT << <grid, threads >> > (Dst, (int)DstStride, 0, 0, TexSrc);
    getLastCudaError("Kernel execution failed");

    // copy quantized image block to host
    checkCudaErrors(cudaMemcpy2D(ImgSrcF, ImgSrcFStride * sizeof(float), Dst, DstStride * sizeof(float), Size.width * sizeof(float), Size.height, cudaMemcpyDeviceToHost));

    // convert image back to byte representation
    AddFloatPlane(128.0f, ImgSrcF, ImgSrcFStride, Size);
    CopyFloat2Byte(ImgSrcF, ImgSrcFStride, ImgDst, Stride, Size);

    // clean up memory
    checkCudaErrors(cudaDestroyTextureObject(TexSrc));
    checkCudaErrors(cudaFreeArray(Src));
    checkCudaErrors(cudaFree(Dst));
    FreePlane(ImgSrcF);

    // return time taken by the operation
    return TimerCUDASpan;
}

/**
**************************************************************************
*  Program entry point
*
* \param argc       [IN] - Number of command-line arguments
* \param argv       [IN] - Array of command-line arguments
*
* \return Status code
*/

int main(int argc, char** argv)
{
    printf("Starting...\n\n");

    // initialize CUDA
    findCudaDevice(argc, (const char**)argv);

    // source and results image filenames
    char SampleImageFname[] = "teapot512.bmp";
    char SampleImageFnameResCUDA1[] = "teapot512_cuda1.bmp";
    char SampleImageFnameResCUDA2[] = "teapot512_cuda2.bmp";
    char SampleImageFnameResCUDAshort[] = "teapot512_cuda_short.bmp";

    char* pSampleImageFpath = sdkFindFilePath(SampleImageFname, argv[0]);

    if (pSampleImageFpath == NULL)
    {
        printf("dct8x8 could not locate Sample Image <%s>\nExiting...\n", pSampleImageFpath);
        exit(EXIT_FAILURE);
    }

    // preload image (acquire dimensions)
    int ImgWidth, ImgHeight;
    ROI ImgSize;
    int res = PreLoadBmp(pSampleImageFpath, &ImgWidth, &ImgHeight);
    ImgSize.width = ImgWidth;
    ImgSize.height = ImgHeight;

    // CONSOLE INFORMATION: saying hello to user
    printf("CUDA sample DCT/IDCT implementation\n");
    printf("===================================\n");
    printf("Loading test image: %s... ", SampleImageFname);

    if (res)
    {
        printf("\nError: Image file not found or invalid!\n");
        exit(EXIT_FAILURE);
        return 1;
    }

    // check image dimensions are multiples of BLOCK_SIZE
    if (ImgWidth % BLOCK_SIZE != 0 || ImgHeight % BLOCK_SIZE != 0)
    {
        printf("\nError: Input image dimensions must be multiples of 8!\n");
        exit(EXIT_FAILURE);
        return 1;
    }

    printf("[%d x %d]... ", ImgWidth, ImgHeight);

    // allocate image buffers
    int ImgStride;
    byte* ImgSrc = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);
    byte* ImgDstCUDA1 = MallocPlaneByte(ImgWidth, ImgHeight, &ImgStride);

    // load sample image
    LoadBmpAsGray(pSampleImageFpath, ImgStride, ImgSize, ImgSrc);

    //
    // RUNNING WRAPPERS
    //

    // compute CUDA 1 version of DCT/quantization/IDCT
    printf("Success\nRunning CUDA 1 (GPU) version... ");
    float TimeCUDA1 = WrapperCUDA1(ImgSrc, ImgDstCUDA1, ImgStride, ImgSize);

    //
    // Execution statistics, result saving and validation
    //

    // dump result of CUDA 1 processing
    printf("Success\nDumping result to %s... ", SampleImageFnameResCUDA1);
    DumpBmpAsGray(SampleImageFnameResCUDA1, ImgDstCUDA1, ImgStride, ImgSize);

    // print speed info
    printf("Success\n");

    printf("Processing time (CUDA 1)    : %f ms \n", TimeCUDA1);

    //
    // Finalization
    //

    // release byte planes
    FreePlane(ImgSrc);
    FreePlane(ImgDstCUDA1);

    // finalize
    printf("Test passed\n");
    exit(EXIT_SUCCESS);
}
