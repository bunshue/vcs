#ifndef MONTECARLO_COMMON_H
#define MONTECARLO_COMMON_H
#include "realtype.h"
#include "curand_kernel.h"

////////////////////////////////////////////////////////////////////////////////
// Global types
////////////////////////////////////////////////////////////////////////////////
typedef struct
{
    float S;
    float X;
    float T;
    float R;
    float V;
} TOptionData;

typedef struct
//#ifdef __CUDACC__
//__align__(8)
//#endif
{
    float Expected;
    float Confidence;
} TOptionValue;

// GPU outputs before CPU postprocessing
typedef struct
{
    real Expected;
    real Confidence;
} __TOptionValue;

typedef struct
{
    // Device ID for multi-GPU version
    int device;
    // Option count for this plan
    int optionCount;

    // Host-side data source and result destination
    TOptionData* optionData;
    TOptionValue* callValue;

    // Temporary Host-side pinned memory for async + faster data transfers
    __TOptionValue* h_CallValue;

    // Device- and host-side option data
    void* d_OptionData;
    void* h_OptionData;

    // Device-side option values
    void* d_CallValue;

    // Intermediate device-side buffers
    void* d_Buffer;

    // random number generator states
    curandState* rngStates;

    // Pseudorandom samples count
    int pathN;

    // Time stamp
    float time;

    int gridSize;
} TOptionPlan;

extern "C" void initMonteCarloGPU(TOptionPlan * plan);
extern "C" void MonteCarloGPU(TOptionPlan * plan, cudaStream_t stream = 0);
extern "C" void closeMonteCarloGPU(TOptionPlan * plan);

#endif
