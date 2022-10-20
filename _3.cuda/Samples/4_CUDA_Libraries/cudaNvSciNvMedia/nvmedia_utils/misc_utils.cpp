#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#if defined (__QNX__)
#include <sys/time.h>
#endif
#include "misc_utils.h"

uint32_t
u32(const uint8_t* ptr)
{
    return ptr[0] | (ptr[1]<<8) | (ptr[2]<<16) | (ptr[3]<<24);
}

NvMediaStatus
GetTimeMicroSec(
    uint64_t *uTime)
{
    struct timespec t;
#if !(defined(CLOCK_MONOTONIC) && defined(_POSIX_MONOTONIC_CLOCK) && _POSIX_MONOTONIC_CLOCK >= 0 && _POSIX_TIMERS > 0)
    struct timeval tv;
#endif

    if(!uTime)
        return NVMEDIA_STATUS_BAD_PARAMETER;

#if !(defined(CLOCK_MONOTONIC) && defined(_POSIX_MONOTONIC_CLOCK) && _POSIX_MONOTONIC_CLOCK >= 0 && _POSIX_TIMERS > 0)
    gettimeofday(&tv, NULL);
    t.tv_sec = tv.tv_sec;
    t.tv_nsec = tv.tv_usec*1000L;
#else
    clock_gettime(CLOCK_MONOTONIC, &t);
#endif

    *uTime = (uint64_t)t.tv_sec * 1000000LL + (uint64_t)t.tv_nsec / 1000LL;
    return NVMEDIA_STATUS_OK;
}

