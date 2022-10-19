#if !defined(__COMMON_GPU_HEADER_H)
#define __COMMON_GPU_HEADER_H

////////////////////////////////////////////////////////////////////////////////
// Internal GPU-side constants and data structures
////////////////////////////////////////////////////////////////////////////////

#define  TIME_STEPS 16

#define CACHE_DELTA (2 * TIME_STEPS)

#define  CACHE_SIZE (256)

#define  CACHE_STEP (CACHE_SIZE - CACHE_DELTA)

#if NUM_STEPS % CACHE_DELTA
#error Bad constants
#endif

#endif