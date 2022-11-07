extern "C" {
    void cudaInit(int argc, char** argv);

    void allocateArray(void** devPtr, int size);
    void freeArray(void* devPtr);

    void threadSync();

    void copyArrayFromDevice(void* host, const void* device, struct cudaGraphicsResource** cuda_vbo_resource, int size);
    void copyArrayToDevice(void* device, const void* host, int offset, int size);
    void registerGLBufferObject(uint vbo, struct cudaGraphicsResource** cuda_vbo_resource);
    void unregisterGLBufferObject(struct cudaGraphicsResource* cuda_vbo_resource);
    void* mapGLBufferObject(struct cudaGraphicsResource** cuda_vbo_resource);
    void unmapGLBufferObject(struct cudaGraphicsResource* cuda_vbo_resource);

    void setParameters(SimParams* hostParams);

    void integrateSystem(float* pos, float* vel, float deltaTime, uint numParticles);

    void calcHash(uint* gridParticleHash, uint* gridParticleIndex, float* pos, int numParticles);

    void reorderDataAndFindCellStart(uint* cellStart, uint* cellEnd, float* sortedPos, float* sortedVel,
        uint* gridParticleHash, uint* gridParticleIndex, float* oldPos, float* oldVel, uint numParticles, uint numCells);

    void collide(float* newVel, float* sortedPos, float* sortedVel, uint* gridParticleIndex, uint* cellStart, uint* cellEnd, uint numParticles, uint numCells);

    void sortParticles(uint* dGridParticleHash, uint* dGridParticleIndex, uint numParticles);
}
