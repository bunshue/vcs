#ifndef _VOLUME_H_
#define _VOLUME_H_

#include <cuda_runtime.h>

typedef unsigned char VolumeType;

extern "C" {

    struct Volume {
        cudaArray* content;
        cudaExtent size;
        cudaChannelFormatDesc channelDesc;
        cudaTextureObject_t volumeTex;
        cudaSurfaceObject_t volumeSurf;
    };

    void Volume_init(Volume* vol, cudaExtent size, void* data, int allowStore);
    void Volume_deinit(Volume* vol);
};

//////////////////////////////////////////////////////////////////////////

#ifdef __CUDACC__

/* Helper class to do popular integer storage to float conversions if required
 */

template <typename T>
struct VolumeTypeInfo {};

template <>
struct VolumeTypeInfo<unsigned char> {
    static const cudaTextureReadMode readMode = cudaReadModeNormalizedFloat;
    static __inline__ __device__ unsigned char convert(float sampled) {
        return (unsigned char)(saturate(sampled) * 255.0);
    }
};

template <>
struct VolumeTypeInfo<unsigned short> {
    static const cudaTextureReadMode readMode = cudaReadModeNormalizedFloat;
    static __inline__ __device__ unsigned short convert(float sampled) {
        return (unsigned short)(saturate(sampled) * 65535.0);
    }
};

template <>
struct VolumeTypeInfo<float> {
    static const cudaTextureReadMode readMode = cudaReadModeElementType;
    static __inline__ __device__ float convert(float sampled) { return sampled; }
};

#endif

#endif
