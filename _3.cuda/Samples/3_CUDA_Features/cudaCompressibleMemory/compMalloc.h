#ifndef COMP_MALLOC_H
#define COMP_MALLOC_H

cudaError_t allocateCompressible(void** adr, size_t size, bool UseCompressibleMemory);
cudaError_t freeCompressible(void* ptr, size_t size, bool UseCompressibleMemory);

#endif
