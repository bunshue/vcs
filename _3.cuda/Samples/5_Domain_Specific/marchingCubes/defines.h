#ifndef _DEFINES_H_
#define _DEFINES_H_

typedef unsigned int uint;
typedef unsigned char uchar;

// if SAMPLE_VOLUME is 0, an implicit dataset is generated. If 1, a voxelized dataset is loaded from file
#define SAMPLE_VOLUME 1

// Using shared to store computed vertices and normals during triangle generation improves performance
#define USE_SHARED 1

// The number of threads to use for triangle generation (limited by shared memory size)
#define NTHREADS 32

#define SKIP_EMPTY_VOXELS 1

#endif
