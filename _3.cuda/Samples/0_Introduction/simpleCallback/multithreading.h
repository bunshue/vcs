#ifndef MULTITHREADING_H
#define MULTITHREADING_H

// Simple portable thread library.

#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
// Windows threads.
#include <windows.h>

typedef HANDLE CUTThread;
typedef unsigned(WINAPI* CUT_THREADROUTINE)(void*);

struct CUTBarrier
{
	CRITICAL_SECTION criticalSection;
	HANDLE barrierEvent;
	int releaseCount;
	int count;
};

#define CUT_THREADPROC unsigned WINAPI
#define CUT_THREADEND return 0

#else
// POSIX threads.
#include <pthread.h>

typedef pthread_t CUTThread;
typedef void* (*CUT_THREADROUTINE)(void*);

#define CUT_THREADPROC void *
#define CUT_THREADEND return 0

struct CUTBarrier {
	pthread_mutex_t mutex;
	pthread_cond_t conditionVariable;
	int releaseCount;
	int count;
};

#endif

#ifdef __cplusplus
extern "C" {
#endif

	// Create thread.
	CUTThread cutStartThread(CUT_THREADROUTINE, void* data);

	// Wait for thread to finish.
	void cutEndThread(CUTThread thread);

	// Wait for multiple threads.
	void cutWaitForThreads(const CUTThread* threads, int num);

	// Create barrier.
	CUTBarrier cutCreateBarrier(int releaseCount);

	// Increment barrier. (execution continues)
	void cutIncrementBarrier(CUTBarrier* barrier);

	// Wait for barrier release.
	void cutWaitForBarrier(CUTBarrier* barrier);

	// Destroy barrier
	void cutDestroyBarrier(CUTBarrier* barrier);

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // MULTITHREADING_H
