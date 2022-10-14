#ifndef _VOLUMEFILTER_KERNEL_H_
#define _VOLUMEFILTER_KERNEL_H_

#define VOLUMEFILTER_MAXWEIGHTS 125

#include <cuda_runtime.h>
#include "volume.h"

extern "C" {
	Volume* VolumeFilter_runFilter(Volume* input, Volume* output0, Volume* output1, int iterations, int numWeights, float4* weights, float postWeightOffset);
};

#endif
