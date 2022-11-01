const char *sSDKsample = "simpleStreams";

const char *sEventSyncMethod[] =
{
    "cudaEventDefault",
    "cudaEventBlockingSync",
    "cudaEventDisableTiming",
    NULL
};

const char *sDeviceSyncMethod[] =
{
    "cudaDeviceScheduleAuto",
    "cudaDeviceScheduleSpin",
    "cudaDeviceScheduleYield",
    "INVALID",
    "cudaDeviceScheduleBlockingSync",
    NULL
};

// System includes
#include <stdio.h>
#include <assert.h>

// CUDA runtime
#include <cuda_runtime.h>

// Helper functions and utilities to work with CUDA
#include <helper_cuda.h>
#include <check.h>

// Macro to aligned up to the memory size in question
#define MEMORY_ALIGNMENT  4096
#define ALIGN_UP(x,size) ( ((size_t)x+(size-1))&(~(size-1)) )

#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdio.h>
#include <crtdbg.h>
#define UNICODE

//////////////////////////////////////////////////////////////////////
// Nvidia Tools Extension

#define USE_NVTX 1

#if USE_NVTX

#include <nvToolsExt.h>
#include <malloc.h>    // _alloca
#include <stdarg.h>

#define NVTX_ASSERT( COND )    ASSERT_( (COND) )

namespace nvtx
{
    class ScopedRange
    {
    private:
        int m_level;

    public:
        ScopedRange(LPCWSTR wszName)
        {
            m_level = nvtxRangePush(wszName);
        }

        ~ScopedRange()
        {          
            int endLevel = nvtxRangePop();
            //  nvtxRangePop() mismatched level
            NVTX_ASSERT(m_level == endLevel);
        }
    };

    int Print(const char* fmt, ...)
    {
        // printf the string and use the return value of printf to
        // determine the size of the buffer used for vsprintf.
        va_list args;
        va_start(args, fmt);
        int chars = vprintf(fmt, args);

        do
        {
            CheckConditionBreak(chars > 0);

            char* buffer = (char*)_alloca(chars + 1);
            CheckConditionBreak(buffer);

            chars = vsprintf_s(buffer, chars + 1, fmt, args);
            CheckConditionBreak(chars > 0);
            
            nvtxMarkA(buffer);
        } while(0);
        va_end(args);

        return chars;
    }
}

#define NVTX_SCOPED_RANGE( WSTR )   nvtx::ScopedRange nvtxScopedRangeW( (WSTR) )
#define PRINT(FMT, ...)             nvtx::Print(FMT,__VA_ARGS__)

#else	// !USE_NVTX

#define NVTX_SCOPED_RANGE( WSTR )   (0)
#define PRINT(FMT, ...)             printf(FMT,##__VA_ARGS__)

#endif // USE_NVTX


__global__ void init_array(int *g_data, int *factor, int num_iterations)
{
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    for (int i=0; i<num_iterations; i++)
    {
        g_data[idx] += *factor;    // non-coalesced on purpose, to burn time
    }
}

int correct_data(int *a, const int n, const int c)
{
    for (int i = 0; i < n; i++)
    {
        if (a[i] != c)
        {
            printf("%d: %d %d\n", i, a[i], c);
            return 0;
        }
    }

    return 1;
}

inline void
AllocateHostMemory(bool bPinGenericMemory, int **pp_a, int **ppAligned_a, int nbytes)
{
#if CUDART_VERSION >= 4000

    if (bPinGenericMemory)
    {
        // allocate a generic page-aligned chunk of system memory
#ifdef WIN32
        printf("> VirtualAlloc() allocating %4.2f Mbytes of (generic page-aligned system memory)\n", (float)nbytes/1048576.0f);
        *pp_a = (int *) VirtualAlloc(NULL, (nbytes + MEMORY_ALIGNMENT), MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE);
#else
        printf("> mmap() allocating %4.2f Mbytes (generic page-aligned system memory)\n", (float)nbytes/1048576.0f);
        *pp_a = (int *) mmap(NULL, (nbytes + MEMORY_ALIGNMENT), PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANON, -1, 0);
#endif

        *ppAligned_a = (int *)ALIGN_UP(*pp_a, MEMORY_ALIGNMENT);

        printf("> cudaHostRegister() registering %4.2f Mbytes of generic allocated system memory\n", (float)nbytes/1048576.0f);
        // pin allocate memory
        checkCudaErrors(cudaHostRegister(*ppAligned_a, nbytes, cudaHostRegisterMapped));
    }
    else
#endif
    {
        printf("> cudaMallocHost() allocating %4.2f Mbytes of system memory\n", (float)nbytes/1048576.0f);
        // allocate host memory (pinned is required for achieve asynchronicity)
        checkCudaErrors(cudaMallocHost((void **)pp_a, nbytes));
        *ppAligned_a = *pp_a;
    }
}

inline void
FreeHostMemory(bool bPinGenericMemory, int **pp_a, int **ppAligned_a, int nbytes)
{
#if CUDART_VERSION >= 4000

    // CUDA 4.0 support pinning of generic host memory
    if (bPinGenericMemory)
    {
        // unpin and delete host memory
        checkCudaErrors(cudaHostUnregister(*ppAligned_a));
#ifdef WIN32
        VirtualFree(*pp_a, 0, MEM_RELEASE);
#else
        munmap(*pp_a, nbytes);
#endif
    }
    else
#endif
    {
        cudaFreeHost(*pp_a);
    }
}

static char *sSyncMethod[] =
{
    "0 (Automatic Blocking)",
    "1 (Spin Blocking)",
    "2 (Yield Blocking)",
    "3 (Undefined Blocking Method)",
    "4 (Blocking Sync Event) = low CPU utilization",
    NULL
};

void printHelp()
{
    printf("Usage: %s [options below]\n", sSDKsample);
    printf("\t--sync_method=n for CPU/GPU synchronization\n");
    printf("\t             n=%s\n", sSyncMethod[0]);
    printf("\t             n=%s\n", sSyncMethod[1]);
    printf("\t             n=%s\n", sSyncMethod[2]);
    printf("\t   <Default> n=%s\n", sSyncMethod[4]);
    printf("\t--use_generic_memory (default) use generic page-aligned for system memory\n");
    printf("\t--use_cuda_malloc_host (optional) use cudaMallocHost to allocate system memory\n");
}

#define DEFAULT_PINNED_GENERIC_MEMORY true

int main(int argc, char **argv)
{
    NVTX_SCOPED_RANGE(L"Main");

    int cuda_device = 0;
    int nstreams = 4;               // number of streams for CUDA calls
    int nreps = 10;                 // number of times each experiment is repeated
    int n = 16 * 1024 * 1024;       // number of ints in the data set
    int nbytes = n * sizeof(int);   // number of data bytes
    dim3 threads, blocks;           // kernel launch configuration
    float elapsed_time, time_memcpy, time_kernel;   // timing variables
    float scale_factor = 1.0f;

    // allocate generic memory and pin it laster instead of using cudaHostAlloc()

    bool bPinGenericMemory  = DEFAULT_PINNED_GENERIC_MEMORY; // we want this to be the default behavior
    int  device_sync_method = cudaDeviceBlockingSync; // by default we use BlockingSync

    int niterations;    // number of iterations for the loop inside the kernel

    printf("[ %s ]\n\n", sSDKsample);

    if (checkCmdLineFlag(argc, (const char **)argv, "help"))
    {
        printHelp();
        return EXIT_SUCCESS;
    }

    if ((device_sync_method = getCmdLineArgumentInt(argc, (const char **)argv, "sync_method")) >= 0)
    {
        if (device_sync_method == 0 || device_sync_method == 1 || device_sync_method == 2 || device_sync_method == 4)
        {
            printf("Device synchronization method set to = %s\n", sSyncMethod[device_sync_method]);
            printf("Setting reps to 100 to demonstrate steady state\n");
            nreps = 100;
        }
        else
        {
            printf("Invalid command line option sync_method=\"%d\"\n", device_sync_method);
            return EXIT_FAILURE;
        }
    }
    else
    {
        printHelp();
        return EXIT_SUCCESS;
    }

    if (checkCmdLineFlag(argc, (const char **)argv, "use_generic_memory"))
    {
        bPinGenericMemory = true;
    }

    if (checkCmdLineFlag(argc, (const char **)argv, "use_cuda_malloc_host"))
    {
        bPinGenericMemory = false;
    }

    printf("\n> ");
    cuda_device = findCudaDevice(argc, (const char **)argv);

    // check the compute capability of the device
    int num_devices=0;
    checkCudaErrors(cudaGetDeviceCount(&num_devices));

    if (0==num_devices)
    {
        printf("your system does not have a CUDA capable device, waiving test...\n");
        return EXIT_WAIVED;
    }

    // check if the command-line chosen device ID is within range, exit if not
    if (cuda_device >= num_devices)
    {
        printf("cuda_device=%d is invalid, must choose device ID between 0 and %d\n", cuda_device, num_devices-1);
        return EXIT_FAILURE;
    }

    cudaSetDevice(cuda_device);

    // Checking for compute capabilities
    cudaDeviceProp deviceProp;
    checkCudaErrors(cudaGetDeviceProperties(&deviceProp, cuda_device));

    if ((1 == deviceProp.major) && (deviceProp.minor < 1))
    {
        printf("%s does not have Compute Capability 1.1 or newer.  Reducing workload.\n", deviceProp.name);
    }

    if (deviceProp.major >= 2)
    {
        niterations = 100;
    }
    else
    {
        if (deviceProp.minor > 1)
        {
            niterations = 5;
        }
        else
        {
            niterations = 1; // reduced workload for compute capability 1.0 and 1.1
        }
    }

    // Check if GPU can map host memory (Generic Method), if not then we override bPinGenericMemory to be false
    if (bPinGenericMemory)
    {
        printf("Device: <%s> canMapHostMemory: %s\n", deviceProp.name, deviceProp.canMapHostMemory ? "Yes" : "No");

        if (deviceProp.canMapHostMemory == 0)
        {
            printf("Using cudaMallocHost, CUDA device does not support mapping of generic host memory\n");
            bPinGenericMemory = false;
        }
    }

    // Anything that is less than 32 Cores will have scaled down workload
    scale_factor = max((32.0f / (_ConvertSMVer2Cores(deviceProp.major, deviceProp.minor) * (float)deviceProp.multiProcessorCount)), 1.0f);
    n = (int)rint((float)n / scale_factor);

    printf("> CUDA Capable: SM %d.%d hardware\n", deviceProp.major, deviceProp.minor);
    printf("> %d Multiprocessor(s) x %d (Cores/Multiprocessor) = %d (Cores)\n",
           deviceProp.multiProcessorCount,
           _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor),
           _ConvertSMVer2Cores(deviceProp.major, deviceProp.minor) * deviceProp.multiProcessorCount);

    printf("> scale_factor = %1.4f\n", 1.0f/scale_factor);
    printf("> array_size   = %d\n\n", n);

    // enable use of blocking sync, to reduce CPU usage
    printf("> Using CPU/GPU Device Synchronization method (%s)\n", sDeviceSyncMethod[device_sync_method]);
    cudaSetDeviceFlags(device_sync_method | (bPinGenericMemory ? cudaDeviceMapHost : 0));

    // allocate host memory
    int c = 5;                      // value to which the array will be initialized
    int *h_a = 0;                   // pointer to the array data in host memory
    int *hAligned_a = 0;           // pointer to the array data in host memory (aligned to MEMORY_ALIGNMENT)

    // Allocate Host memory (could be using cudaMallocHost or VirtualAlloc/mmap if using the new CUDA 4.0 features
    {
        NVTX_SCOPED_RANGE(L"Init: Host Malloc");
        AllocateHostMemory(bPinGenericMemory, &h_a, &hAligned_a, nbytes);
    }
    

    // allocate device memory
    int *d_a = 0, *d_c = 0;             // pointers to data and init value in the device memory
    {
        NVTX_SCOPED_RANGE(L"Init: Device Malloc");
        checkCudaErrors(cudaMalloc((void **)&d_a, nbytes));
        checkCudaErrors(cudaMalloc((void **)&d_c, sizeof(int)));
        checkCudaErrors(cudaMemcpy(d_c, &c, sizeof(int), cudaMemcpyHostToDevice));
    }

    printf("\nStarting Test\n");

    // allocate and initialize an array of stream handles
    cudaStream_t *streams = (cudaStream_t *) malloc(nstreams * sizeof(cudaStream_t));

    for (int i = 0; i < nstreams; i++)
    {
        checkCudaErrors(cudaStreamCreate(&(streams[i])));
    }

    // create CUDA event handles
    // use blocking sync
    cudaEvent_t start_event, stop_event;
    int eventflags = ((device_sync_method == cudaDeviceBlockingSync) ? cudaEventBlockingSync: cudaEventDefault);

    checkCudaErrors(cudaEventCreateWithFlags(&start_event, eventflags));
    checkCudaErrors(cudaEventCreateWithFlags(&stop_event, eventflags));

    // time memcopy from device
    {
        NVTX_SCOPED_RANGE(L"Time Memcpy DtoH");

        cudaEventRecord(start_event, 0);     // record in stream-0, to ensure that all previous CUDA calls have completed
        cudaMemcpyAsync(hAligned_a, d_a, nbytes, cudaMemcpyDeviceToHost, streams[0]);
        cudaEventRecord(stop_event, 0);
        cudaEventSynchronize(stop_event);   // block until the event is actually recorded
    }

    checkCudaErrors(cudaEventElapsedTime(&time_memcpy, start_event, stop_event));
    printf("memcopy:\t%.2f\n", time_memcpy);
    
    // time kernel
    threads=dim3(512, 1);
    blocks=dim3(n / threads.x, 1);

    {
        NVTX_SCOPED_RANGE(L"Time Single Kernel");

        cudaEventRecord(start_event, 0);

        init_array<<<blocks, threads, 0, streams[0]>>>(d_a, d_c, niterations);

        cudaEventRecord(stop_event, 0);
        cudaEventSynchronize(stop_event);
    }

    checkCudaErrors(cudaEventElapsedTime(&time_kernel, start_event, stop_event));
    printf("kernel:\t\t%.2f\n", time_kernel);

    //////////////////////////////////////////////////////////////////////
    // time non-streamed execution for reference
    threads=dim3(512, 1);
    blocks=dim3(n / threads.x, 1);

    {
        NVTX_SCOPED_RANGE(L"Time Non-Streamed Execution");

        cudaEventRecord(start_event, 0);

        for (int k = 0; k < nreps; k++)
        {
            init_array<<<blocks, threads>>>(d_a, d_c, niterations);

            cudaMemcpy(hAligned_a, d_a, nbytes, cudaMemcpyDeviceToHost);
        }
        
        cudaEventRecord(stop_event, 0);
        cudaEventSynchronize(stop_event);
    }

    checkCudaErrors(cudaEventElapsedTime(&elapsed_time, start_event, stop_event));
    printf("non-streamed:\t%.2f (%.2f expected)\n", elapsed_time / nreps, time_kernel + time_memcpy);

    //////////////////////////////////////////////////////////////////////
    // time execution with nstreams streams
    threads=dim3(512,1);
    blocks=dim3(n/(nstreams*threads.x),1);
    memset(hAligned_a, 255, nbytes);     // set host memory bits to all 1s, for testing correctness
    cudaMemset(d_a, 0, nbytes); // set device memory to all 0s, for testing correctness
    
    {
        NVTX_SCOPED_RANGE(L"Time Streamed Execution");

        cudaEventRecord(start_event, 0);

        for (int k = 0; k < nreps; k++)
        {
            // asynchronously launch nstreams kernels, each operating on its own portion of data
            for (int i = 0; i < nstreams; i++)
            {
                init_array<<<blocks, threads, 0, streams[i]>>>(d_a + i * n / nstreams, d_c, niterations);
            }

            // asynchronously launch nstreams memcopies.  Note that memcopy in stream x will only
            //   commence executing when all previous CUDA calls in stream x have completed
            for (int i = 0; i < nstreams; i++)
            {
                cudaMemcpyAsync(hAligned_a + i * n / nstreams, d_a + i * n / nstreams, nbytes / nstreams, cudaMemcpyDeviceToHost, streams[i]);
            }
        }

        cudaEventRecord(stop_event, 0);
        cudaEventSynchronize(stop_event);
    }
    checkCudaErrors(cudaEventElapsedTime(&elapsed_time, start_event, stop_event));
    printf("%d streams:\t%.2f (%.2f expected with compute capability 1.1 or later)\n", nstreams, elapsed_time / nreps, time_kernel + time_memcpy / nstreams);

    // check whether the output is correct
    printf("-------------------------------\n");
    bool bResults = 0 != correct_data(hAligned_a, n, c*nreps*niterations);

    // release resources
    for (int i = 0; i < nstreams; i++)
    {
        cudaStreamDestroy(streams[i]);
    }
    cudaEventDestroy(start_event);
    cudaEventDestroy(stop_event);

    // Free cudaMallocHost or Generic Host allocated memory (from CUDA 4.0)
    FreeHostMemory(bPinGenericMemory, &h_a, &hAligned_a, nbytes);

    cudaFree(d_a);
    cudaFree(d_c);

    cudaDeviceReset();

    return bResults ? EXIT_SUCCESS : EXIT_FAILURE;
}
