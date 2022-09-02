/*
* Copyright 1993-2010 NVIDIA Corporation.  All rights reserved.
*
* NOTICE TO USER:
*
* This source code is subject to NVIDIA ownership rights under U.S. and
* international Copyright laws.  Users and possessors of this source code
* are hereby granted a nonexclusive, royalty-free license to use this code
* in individual and commercial software.
*
* NVIDIA MAKES NO REPRESENTATION ABOUT THE SUITABILITY OF THIS SOURCE
* CODE FOR ANY PURPOSE.  IT IS PROVIDED "AS IS" WITHOUT EXPRESS OR
* IMPLIED WARRANTY OF ANY KIND.  NVIDIA DISCLAIMS ALL WARRANTIES WITH
* REGARD TO THIS SOURCE CODE, INCLUDING ALL IMPLIED WARRANTIES OF
* MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
* IN NO EVENT SHALL NVIDIA BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL,
* OR CONSEQUENTIAL DAMAGES, OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
* OF USE, DATA OR PROFITS,  WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
* OR OTHER TORTIOUS ACTION,  ARISING OUT OF OR IN CONNECTION WITH THE USE
* OR PERFORMANCE OF THIS SOURCE CODE.
*
* U.S. Government End Users.   This source code is a "commercial item" as
* that term is defined at  48 C.F.R. 2.101 (OCT 1995), consisting  of
* "commercial computer  software"  and "commercial computer software
* documentation" as such terms are  used in 48 C.F.R. 12.212 (SEPT 1995)
* and is provided to the U.S. Government only as a commercial end item.
* Consistent with 48 C.F.R.12.212 and 48 C.F.R. 227.7202-1 through
* 227.7202-4 (JUNE 1995), all U.S. Government End Users acquire the
* source code with only those rights set forth herein.
*
* Any use of this source code in individual and commercial software must
* include, in the user documentation and internal comments to the code,
* the above Disclaimer and U.S. Government End Users Notice.
*/

#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#include <limits.h>
#include <float.h>
#include <xutility>
#include <intrin.h>

#include "nvToolsExt.h"

// ============================================================================
// PREPROCESSOR
// ============================================================================

#define NVTX_ENABLE

#ifdef NVTX_ENABLE
#define DELAY_RANGE() Sleep(100);     // sleep 100 ms
#define DELAY()       Sleep(10);      // sleep 10 ms
#else
#define DELAY_RANGE()
#define DELAY()
#endif

// C Preprocessor macros to conditionally enable NvToolsExt functions.

#ifdef NVTX_ENABLE

#define NVTX_MarkEx nvtxMarkEx
#define NVTX_MarkA nvtxMarkA
#define NVTX_MarkW nvtxMarkW

#define NVTX_RangeStartEx nvtxRangeStartEx
#define NVTX_RangeStartA nvtxRangeStartA
#define NVTX_RangeStartW nvtxRangeStartW

#define NVTX_RangeEnd nvtxRangeEnd

#define NVTX_RangePushEx nvtxRangePushEx
#define NVTX_RangePushA nvtxRangePushA
#define NVTX_RangePushW nvtxRangePushW

#define NVTX_RangePop nvtxRangePop

#define NVTX_NameOsThreadA nvtxNameOsThreadA
#define NVTX_NameOsThreadW nvtxNameOsThreadW

#else

#define NVTX_MarkEx __noop
#define NVTX_MarkA __noop
#define NVTX_MarkW __noop

#define NVTX_RangeStartEx __noop
#define NVTX_RangeStartA __noop
#define NVTX_RangeStartW __noop

#define NVTX_RangeEnd __noop

#define NVTX_RangePushEx __noop
#define NVTX_RangePushA __noop
#define NVTX_RangePushW __noop

#define NVTX_RangePop __noop

#define NVTX_NameOsThreadA __noop
#define NVTX_NameOsThreadW __noop

#endif

// C++ function templates to enable NvToolsExt functions
namespace nvtx
{
#ifdef NVTX_ENABLE
    class Attributes
    {
    public:
        inline Attributes()
        {
            clear();
        }

        inline Attributes& category(uint32_t category)
        {
            m_event.category = category;
            return *this;
        }

        inline Attributes& color(uint32_t argb)
        {
            m_event.colorType = NVTX_COLOR_ARGB;
            m_event.color = argb;
            return *this;
        }

        inline Attributes& payload(uint64_t value)
        {
            m_event.payloadType = NVTX_PAYLOAD_TYPE_UNSIGNED_INT64;
            m_event.payload.ullValue = value;
            return *this;
        }

        inline Attributes& payload(int64_t value)
        {
            m_event.payloadType = NVTX_PAYLOAD_TYPE_INT64;
            m_event.payload.llValue = value;
            return *this;
        }

        inline Attributes& payload(double value)
        {
            m_event.payloadType = NVTX_PAYLOAD_TYPE_DOUBLE;
            m_event.payload.dValue = value;
            return *this;
        }

        inline Attributes& message(const char* message)
        {
            m_event.messageType = NVTX_MESSAGE_TYPE_ASCII;
            m_event.message.ascii = message;
            return *this;
        }

        inline Attributes& message(const wchar_t* message)
        {
            m_event.messageType = NVTX_MESSAGE_TYPE_UNICODE;
            m_event.message.unicode = message;
            return *this;
        }

        inline Attributes& clear()
        {
            memset(&m_event, 0, NVTX_EVENT_ATTRIB_STRUCT_SIZE);
            m_event.version = NVTX_VERSION;
            m_event.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
            return *this;
        }

        inline const nvtxEventAttributes_t* out() const
        {
            return &m_event;
        }

    private:
        nvtxEventAttributes_t m_event;
    };


    class ScopedRange
    {
    public:
        inline ScopedRange(const char* message)
        {
            nvtxRangePushA(message);
        }

        inline ScopedRange(const wchar_t* message)
        {
            nvtxRangePushW(message);
        }

        inline ScopedRange(const nvtxEventAttributes_t* attributes)
        {
            nvtxRangePushEx(attributes);
        }

        inline ScopedRange(const nvtx::Attributes& attributes)
        {
            nvtxRangePushEx(attributes.out());
        }

        inline ~ScopedRange()
        {
            nvtxRangePop();
        }
    };

    inline void Mark(const nvtx::Attributes& attrib) { nvtxMarkEx(attrib.out()); }
    inline void Mark(const nvtxEventAttributes_t* eventAttrib) { nvtxMarkEx(eventAttrib); }
    inline void Mark(const char* message) { nvtxMarkA(message); }
    inline void Mark(const wchar_t* message) { nvtxMarkW(message); }

    inline nvtxRangeId_t RangeStart(const nvtx::Attributes& attrib) { return nvtxRangeStartEx(attrib.out()); }
    inline nvtxRangeId_t RangeStart(const nvtxEventAttributes_t* eventAttrib) { return nvtxRangeStartEx(eventAttrib); }
    inline nvtxRangeId_t RangeStart(const char* message) { return nvtxRangeStartA(message); }
    inline nvtxRangeId_t RangeStart(const wchar_t* message) { return nvtxRangeStartW(message); }

    inline void RangeEnd(nvtxRangeId_t id) { nvtxRangeEnd(id); }

    inline int RangePush(const nvtx::Attributes& attrib) { return nvtxRangePushEx(attrib.out()); }
    inline int RangePush(const nvtxEventAttributes_t* eventAttrib) { return nvtxRangePushEx(eventAttrib); }
    inline int RangePush(const char* message) { return nvtxRangePushA(message); }
    inline int RangePush(const wchar_t* message) { return nvtxRangePushW(message); }

    inline void RangePop() { nvtxRangePop(); }

    inline void NameCategory(uint32_t category, const char* name) { nvtxNameCategoryA(category, name); }
    inline void NameCategory(uint32_t category, const wchar_t* name) { nvtxNameCategoryW(category, name); }

    inline void NameOsThread(uint32_t threadId, const char* name) { nvtxNameOsThreadA(threadId, name); }
    inline void NameOsThread(uint32_t threadId, const wchar_t* name) { nvtxNameOsThreadW(threadId, name); }
    inline void NameCurrentThread(const char* name) { nvtxNameOsThreadA(::GetCurrentThreadId(), name); }
    inline void NameCurrentThread(const wchar_t* name) { nvtxNameOsThreadW(::GetCurrentThreadId(), name); }

#else

    class Attributes
    {
    public:
        Attributes() {}
        Attributes& category(uint32_t category) { return *this; }
        Attributes& color(uint32_t argb) { return *this; }
        Attributes& payload(uint64_t value) { return *this; }
        Attributes& payload(int64_t value) { return *this; }
        Attributes& payload(double value) { return *this; }
        Attributes& message(const char* message) { return *this; }
        Attributes& message(const wchar_t* message) { return *this; }
        Attributes& clear() { return *this; }
        const nvtxEventAttributes_t* out() { return 0; }
    };

    class ScopedRange
    {
    public:
        ScopedRange(const char* message) { (void)message; }
        ScopedRange(const wchar_t* message) { (void)message; }
        ScopedRange(const nvtxEventAttributes_t* attributes) { (void)attributes; }
        ScopedRange(const Attributes& attributes) { (void)attributes; }
        ~ScopedRange() {}
    };

    inline void Mark(const nvtx::Attributes& attrib) { (void)attrib; }
    inline void Mark(const nvtxEventAttributes_t* eventAttrib) { (void)eventAttrib; }
    inline void Mark(const char* message) { (void)message; }
    inline void Mark(const wchar_t* message) { (void)message; }

    inline nvtxRangeId_t RangeStart(const nvtx::Attributes& attrib) { (void)attrib; return 0; }
    inline nvtxRangeId_t RangeStart(const nvtxEventAttributes_t* eventAttrib) { (void)eventAttrib; return 0; }
    inline nvtxRangeId_t RangeStart(const char* message) { (void)message; return 0; }
    inline nvtxRangeId_t RangeStart(const wchar_t* message) { (void)message; return 0; }

    inline void RangeEnd(nvtxRangeId_t id) { (void)id; }


    inline int RangePush(const nvtx::Attributes& attrib) { (void)attrib; return -1; }
    inline int RangePush(const nvtxEventAttributes_t* eventAttrib) { (void)eventAttrib; return -1; }
    inline int RangePush(const char* message) { (void)message; return -1;}
    inline int RangePush(const wchar_t* message) { (void)message; return -1; }

    inline int RangePop() { return -1; }

    inline void NameCategory(uint32_t category, const char* name) { (void)category; (void)name; }
    inline void NameCategory(uint32_t category, const wchar_t* name) { (void)category; (void)name; }

    inline void NameOsThread(uint32_t threadId, const char* name) { (void)threadId; (void)name; }
    inline void NameOsThread(uint32_t threadId, const wchar_t* name) { (void)threadId; (void)name; }
    inline void NameCurrentThread(const char* name) { (void)name; }
    inline void NameCurrentThread(const wchar_t* name) { (void)name; }

#endif
}

void test_wrapper()
{
    nvtx::Attributes attrib;

    // PREPROCESSOR TESTS
    {
        DELAY();    NVTX_MarkEx(attrib.message("NVTX_MarkEx Ascii").out());
        DELAY();    NVTX_MarkEx(attrib.message(L"NVTX_MarkEx Unicode").out());
        DELAY();    NVTX_MarkA("NVTX_MarkA");
        DELAY();    NVTX_MarkW(L"NVTX_MarkW");

        DELAY();    nvtxRangeId_t r1 = NVTX_RangeStartEx(attrib.message("NVTX_RangeStartEx").out());
        DELAY();    nvtxRangeId_t r2 = NVTX_RangeStartEx(attrib.message(L"NVTX_RangeStartEx").out());
        DELAY();    NVTX_RangeEnd(r2);
        DELAY();    nvtxRangeId_t r3 = NVTX_RangeStartA("NVTX_RangeStartA");
        DELAY();    nvtxRangeId_t r4 = NVTX_RangeStartW(L"NVTX_RangeStartW");
        DELAY();    NVTX_RangeEnd(r3);
        DELAY();    NVTX_RangeEnd(r1);
        DELAY();    NVTX_RangeEnd(r4);

        DELAY();    NVTX_RangePushEx(attrib.message("NVTX_RangePushEx").out());
        DELAY();    NVTX_RangePushEx(attrib.message(L"NVTX_RangePushEx").out());
        DELAY();    NVTX_RangePop();
        DELAY();    NVTX_RangePushA("NVTX_RangePushA");
        DELAY();    NVTX_RangePushW(L"NVTX_RangePushW");
        DELAY();    NVTX_RangePop();
        DELAY();    NVTX_RangePop();
        DELAY();    NVTX_RangePop();
    }

    // C++ WRAPPER TESTS
    {
        DELAY();    nvtx::Mark(attrib.message("ascii").out());
        DELAY();    nvtx::Mark(attrib.message(L"unicode").out());
        DELAY();    nvtx::Mark(attrib.message("ascii"));
        DELAY();    nvtx::Mark(attrib.message(L"unicode"));
        DELAY();    nvtx::Mark("nvtx::Mark");
        DELAY();    nvtx::Mark(L"nvtx::Mark");

        DELAY();    nvtxRangeId_t r1 = nvtx::RangeStart(attrib.message("nvtx::RangeStartEx").out());
        DELAY();    nvtxRangeId_t r2 = nvtx::RangeStart(attrib.message(L"nvtx::RangeStartEx"));
        DELAY();    nvtx::RangeEnd(r2);
        DELAY();    nvtxRangeId_t r3 = nvtx::RangeStart("nvtx::RangeStartA");
        DELAY();    nvtxRangeId_t r4 = nvtx::RangeStart(L"nvtx::RangeStartW");
        DELAY();    nvtx::RangeEnd(r3);
        DELAY();    nvtx::RangeEnd(r1);
        DELAY();    nvtx::RangeEnd(r4);

        DELAY();    nvtx::RangePush(attrib.message("nvtx::RangePushEx").out());
        DELAY();    nvtx::RangePush(attrib.message(L"nvtx::RangePushEx"));
        DELAY();    nvtx::RangePop();
        DELAY();    nvtx::RangePush("nvtx::RangePushA");
        DELAY();    nvtx::RangePush(L"nvtx::RangePushW");
        DELAY();    nvtx::RangePop();
        DELAY();    nvtx::RangePop();
        DELAY();    nvtx::RangePop();
    }

    // C++ ScopedRange
    {
        {
            DELAY();    nvtx::ScopedRange sr1(attrib.message("sr1").out());
            DELAY();    nvtx::ScopedRange sr2(attrib.message(L"sr2"));
            {
                DELAY();
                {
                    nvtx::ScopedRange sr3("sr3");
                    DELAY();
                }
            }
            DELAY();
        }
        {
            DELAY();    nvtx::ScopedRange sr4(L"sr4");
            DELAY();
        }
    }

    // Attributes
    {
        nvtx::Attributes a1;
        DELAY();    nvtx::Mark(a1);
        DELAY();    nvtx::Mark(a1.clear().category(1));
        DELAY();    nvtx::Mark(a1.clear());

        DELAY();    nvtx::Mark(nvtx::Attributes().color(0xFFFF0000));

        DELAY();    nvtx::Mark(nvtx::Attributes().payload(ULLONG_MAX));
        DELAY();    nvtx::Mark(nvtx::Attributes().payload(LLONG_MIN));
        DELAY();    nvtx::Mark(nvtx::Attributes().payload(LLONG_MAX));
        DELAY();    nvtx::Mark(nvtx::Attributes().payload(DBL_MIN));
        DELAY();    nvtx::Mark(nvtx::Attributes().payload(DBL_MAX));

        DELAY();    nvtx::Mark(nvtx::Attributes().message("ascii"));
        DELAY();    nvtx::Mark(nvtx::Attributes().message(L"unicode"));
        DELAY();    nvtx::Mark(nvtx::Attributes().message(L"\u2603"));
    }
}

// Struct containing arguments passed to each thread
struct ThreadArgs_st
{
    const char* message;
    uint32_t delay;
    uint32_t duration;
    uint32_t category;
    uint32_t threadIdx;
    uint32_t eventIdx;
    uint32_t color;

    LONG crossCount;
    volatile LONG* crossLock;
    nvtxRangeId_t* crossIds;
};

// Thread main body
DWORD WINAPI threadEvent(LPVOID arg)
{
    ThreadArgs_st* threadArgs = (ThreadArgs_st*) arg;

    // Create event message
    char* eventName[64] = { 0 };
    sprintf_s((char*)eventName, 64, "Thread %d [%d]: %s %d",
        threadArgs->threadIdx, GetCurrentThreadId(), threadArgs->message, threadArgs->eventIdx);

    // Create attribute
    nvtx::Attributes attrib;
    attrib.message((char*)eventName);
    attrib.color(threadArgs->color);
    attrib.category(threadArgs->category);

    nvtx::Mark("Delay Event");
    Sleep(threadArgs->delay);

    nvtx::Mark("Begin Event");
    nvtxRangeId_t rangeId = nvtx::RangeStart(attrib);

    Sleep(threadArgs->duration);

    nvtx::Mark("End Event");
    nvtx::RangeEnd(rangeId);

    return 0;
}

// Create a row of markers with increasing payload
DWORD WINAPI threadMarkerEvent(LPVOID arg)
{
    ThreadArgs_st* threadArgs = (ThreadArgs_st*) arg;

    nvtx::Attributes attrib;
    attrib.message(threadArgs->message);
    attrib.color(threadArgs->color);
    attrib.category(threadArgs->category);

    for (uint64_t p = 1 ; p <= 10; ++p)
    {
        attrib.payload(p);
        DELAY()
        nvtx::Mark(attrib);
    }

    return 0;
}

// Thread main body for cross thread events
DWORD WINAPI threadEventCross(LPVOID arg)
{
    ThreadArgs_st* threadArgs = (ThreadArgs_st*) arg;

    int threadIdx = threadArgs->threadIdx;
    int startIdx = threadArgs->eventIdx;
    int endIdx = (startIdx + 1) % threadArgs->crossCount; // TODO

    // Create event message
    char* eventName[64] = { 0 };
    sprintf_s((char*)eventName, 64, "Thread %d [%d]: %s From %d to %d",
        threadArgs->threadIdx, GetCurrentThreadId(), threadArgs->message, threadIdx, threadIdx-startIdx+endIdx);

    // Create attribute
    nvtx::Attributes attrib;
    attrib.message((char*)eventName);
    attrib.color(threadArgs->color);
    attrib.category(threadArgs->category);

    // Start a start/stop range on the current thread
    nvtxRangeId_t rangeId = nvtx::RangeStart(attrib);

    // Store rangeId in global data structure with startIdx
    threadArgs->crossIds[startIdx] = rangeId;
    InterlockedIncrement(threadArgs->crossLock);

    // Sleep for some time
    Sleep(threadArgs->duration);

    // Assure all global data was already written
    while (*threadArgs->crossLock < threadArgs->crossCount)
    {
        SwitchToThread();
    }

    // Read rangeId from global data structure with endIdx
    rangeId = threadArgs->crossIds[endIdx];

    // End a start/stop range from a different thread on the current one
    nvtx::RangeEnd(rangeId);

    return 0;
}

int main(int argc, char* argv[])
{
    // Output events using the wrapper functions
    test_wrapper();

    // Output events on multiple threads
    nvtx::ScopedRange srEventsGeneration("Generate Events on Multiple Threads");

    const int k_numMarkerThreads = 1;
    const int k_numSerialThreads = 2;
    const int k_numOverlapThreads = 4;
    const int k_numNestedThreads = 3;
    const LONG k_numCrossThreads = 4;
    const int k_numThreads = k_numMarkerThreads + k_numSerialThreads + k_numOverlapThreads + k_numNestedThreads + k_numCrossThreads;

    const DWORD k_sleepTimeMs = 50;
    const DWORD k_sleepTimeMsTiny = 50;
    const DWORD k_sleepTimeMsSmall = 100;
    const DWORD k_sleepTimeMsMedium = 200;
    const DWORD k_sleepTimeMsLarge = 300;

    HANDLE threads[k_numThreads];
    ThreadArgs_st threadArgs[k_numThreads] = { 0 };

    int idx = 0;
    int category = 0;

    //////////////////////////////////////////////////////////////////////
    // Marker events
    //////////////////////////////////////////////////////////////////////
    nvtx::Mark("Setting up Marker Events");
    int markerThreadIdx = idx;

    // Give the category a name which will be labelled on the y-axis
    ++category;
    nvtxNameCategoryA(category, "Markers");

    // Create a row of markers with increasing payload
    threadArgs[idx].message = "Payload Marker";
    threadArgs[idx].category = category;
    threadArgs[idx].color = 0xFFED1C24;
    threadArgs[idx].threadIdx = idx;
    threads[idx] = CreateThread( 0, 0, threadMarkerEvent, &threadArgs[idx], CREATE_SUSPENDED, 0 );
    ++idx;

    //////////////////////////////////////////////////////////////////////
    // Serial events
    //////////////////////////////////////////////////////////////////////
    nvtx::Mark("Setting up Serial Events");
    int firstSerialThreadIdx = idx;

    // Give the category a name which will be labelled on the y-axis
    ++category;
    nvtxNameCategoryA(category, "Serial Ranges");

    int serialEventIdx = 1;
    DWORD startTimeSerial = 0;

    for (int i = 0; i < k_numSerialThreads; ++i)
    {
        threadArgs[idx].category = category;
        threadArgs[idx].color = 0xFF00A2E8;
        threadArgs[idx].threadIdx = idx;
        threadArgs[idx].message = "Serial Ranges";
        threadArgs[idx].delay = startTimeSerial;
        threadArgs[idx].duration = k_sleepTimeMsSmall;
        threadArgs[idx].eventIdx = serialEventIdx;

        threads[idx] = CreateThread( 0, 0, threadEvent, &threadArgs[idx], CREATE_SUSPENDED, 0 );

        startTimeSerial += threadArgs[idx].duration;    // Start the next serial event after this one.
        startTimeSerial += k_sleepTimeMsTiny;           // Put a gap between each serial event.

        ++idx;
        ++serialEventIdx;
    }

    //////////////////////////////////////////////////////////////////////
    // Overlapping events
    //////////////////////////////////////////////////////////////////////
    nvtx::Mark("Setting up Overlapping Events");
    int firstOverlapThreadIdx = idx;

    // Give the category a name which will be labelled on the y-axis
    ++category;
    nvtxNameCategoryA(category, "Overlapping Ranges");

    int overlapEventIdx = 1;
    DWORD startTimeOverlap = 0;
    int half = k_numOverlapThreads / 2;
    int otherHalf = k_numOverlapThreads - half;

    for (int i = 0; i < half; ++i)
    {
        threadArgs[idx].category = category;
        threadArgs[idx].color = 0xFF22B14C;
        threadArgs[idx].threadIdx = idx;
        threadArgs[idx].message = "Overlapping Ranges";
        threadArgs[idx].delay = startTimeOverlap;
        threadArgs[idx].duration = k_sleepTimeMsMedium;
        threadArgs[idx].eventIdx = overlapEventIdx;
        threads[idx] = CreateThread( 0, 0, threadEvent, &threadArgs[idx], CREATE_SUSPENDED, 0 );

        // Start the next nested event shortly after this one
        startTimeOverlap += k_sleepTimeMsMedium;

        ++idx;
        ++overlapEventIdx;
    }

    // Remember the event on the first row (event begins earlier than other events below it)
    ThreadArgs_st* leadingOverlapEvent = &threadArgs[idx];

    // Reset the start time to shortly after the first overlapped event
    startTimeOverlap = leadingOverlapEvent->delay + leadingOverlapEvent->duration + k_sleepTimeMsTiny / 2;

    for (int i = 0; i < otherHalf; ++i)
    {
        threadArgs[idx].category = category;
        threadArgs[idx].color = 0xFF22B14C;
        threadArgs[idx].threadIdx = idx;
        threadArgs[idx].message = "Overlapping Ranges";
        threadArgs[idx].delay = startTimeOverlap;
        threadArgs[idx].duration = k_sleepTimeMsMedium;
        threadArgs[idx].eventIdx = overlapEventIdx;
        threads[idx] = CreateThread( 0, 0, threadEvent, &threadArgs[idx], CREATE_SUSPENDED, 0 );

        // Start the next event shortly after this one
        startTimeOverlap += k_sleepTimeMsTiny;

        ++idx;
        ++overlapEventIdx;
    }

    //////////////////////////////////////////////////////////////////////
    // Nested events
    //////////////////////////////////////////////////////////////////////
    nvtx::Mark("Setting up Nested Events");
    int firstNestedThreadIdx = idx;

    // Give the category a name which will be labelled on the y-axis
    ++category;
    nvtxNameCategoryA(category, "Nested Ranges");

    int nestedEventIdx = 1;
    DWORD startTimeNested = 0;
    int numTriplets = k_numNestedThreads / 3;
    int remainder = k_numNestedThreads - (numTriplets * 3);

    DWORD delays[3] =
    {
        k_sleepTimeMsLarge,
        k_sleepTimeMsMedium,
        k_sleepTimeMsSmall
    };

    // Remember the event on the first row (event begins earlier than other events below it)
    ThreadArgs_st* leadingNestedEvent = 0;

    for (int i = 0; i < numTriplets + 1; ++i)
    {
        leadingNestedEvent = &threadArgs[idx];

        for (int j = 0; j < 3; ++j)
        {
            if ( !(i < numTriplets || j < remainder) )
            {
                break;
            }

            threadArgs[idx].category = category;        // Set category to 3
            threadArgs[idx].color = 0xFFFF7F27;
            threadArgs[idx].threadIdx = idx;
            threadArgs[idx].message = "Nested Ranges";
            threadArgs[idx].delay = startTimeNested;
            threadArgs[idx].duration = delays[j];
            threadArgs[idx].eventIdx = nestedEventIdx;
            threads[idx] = CreateThread( 0, 0, threadEvent, &threadArgs[idx], CREATE_SUSPENDED, 0 );

            // Start the next nested event shortly after this one
            startTimeNested += k_sleepTimeMsTiny;

            ++idx;
            ++nestedEventIdx;
        }

        startTimeNested = leadingNestedEvent->delay + leadingNestedEvent->duration + k_sleepTimeMsTiny;
    }

    //////////////////////////////////////////////////////////////////////
    // Cross thread events
    //////////////////////////////////////////////////////////////////////
    nvtx::Mark("Setting up Cross-Thread Events");
    int firstCrossThreadIdx = idx;

    // Give the category a name which will be labelled on the y-axis
    ++category;
    nvtxNameCategoryA(category, "Cross Thread Ranges");

    int crossEventIdx = 0;
    nvtxRangeId_t crossThreadRangeIds[k_numCrossThreads] = {0};
    volatile LONG crossThreadLock = 0;

    for (int i = 0; i < k_numCrossThreads; ++i)
    {
        threadArgs[idx].category = category;             // Set category to 3
        threadArgs[idx].color = 0xFFDCDF00;
        threadArgs[idx].threadIdx = idx;
        threadArgs[idx].message = "Cross Ranges";
        threadArgs[idx].delay = 0;
        threadArgs[idx].duration = k_sleepTimeMsMedium;
        threadArgs[idx].eventIdx = crossEventIdx;
        threadArgs[idx].crossCount = k_numCrossThreads;
        threadArgs[idx].crossLock = &crossThreadLock;
        threadArgs[idx].crossIds = crossThreadRangeIds;
        threads[idx] = CreateThread( 0, 0, threadEventCross, &threadArgs[idx], CREATE_SUSPENDED, 0 );

        ++idx;
        ++crossEventIdx;
    }

    //////////////////////////////////////////////////////////////////////
    // Run threads
    //////////////////////////////////////////////////////////////////////

    // Check the threads
    for (int i = 0; i < k_numThreads; ++i)
    {
        if (!threads[i])
        {
            fprintf(stderr, "Error: CreateThread failed.");
            return -1;
        }
    }

    // Wake up threads
    for (int i = 0; i < k_numThreads; ++i)
    {
        ResumeThread(threads[i]);
    }

    // Name the first thread of each type
    nvtxNameOsThreadA(GetThreadId(threads[markerThreadIdx]), "First thread generating marker events");
    nvtxNameOsThreadA(GetThreadId(threads[firstSerialThreadIdx]), "First thread in serial events");
    nvtxNameOsThreadA(GetThreadId(threads[firstOverlapThreadIdx]), "First thread in overlapping events");
    nvtxNameOsThreadA(GetThreadId(threads[firstNestedThreadIdx]), "First thread in nested events");
    nvtxNameOsThreadA(GetThreadId(threads[firstCrossThreadIdx]), "First thread in cross-thread events");

    // Wait for threads to exit
    WaitForMultipleObjects(k_numThreads, threads, 1, INFINITE);

    return 0;
};
