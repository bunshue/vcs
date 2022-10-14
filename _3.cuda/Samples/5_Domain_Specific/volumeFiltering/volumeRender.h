#ifndef _VOLUMERENDER__H_
#define _VOLUMERENDER__H_

#include <cuda_runtime.h>
#include "volume.h"

extern "C" {
    void VolumeRender_init();
    void VolumeRender_deinit();

    void VolumeRender_setPreIntegrated(int state);
    void VolumeRender_setTextureFilterMode(bool bLinearFilter, Volume* volume);
    void VolumeRender_render(dim3 gridSize, dim3 blockSize, uint* d_output,
        uint imageW, uint imageH, float density,
        float brightness, float transferOffset,
        float transferScale, cudaTextureObject_t tex);
    void VolumeRender_copyInvViewMatrix(float* invViewMatrix, size_t sizeofMatrix);
};

#endif
