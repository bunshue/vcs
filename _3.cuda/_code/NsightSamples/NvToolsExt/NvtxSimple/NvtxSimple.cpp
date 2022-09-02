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

#include "nvToolsExt.h"

#define WIN32_LEAN_AND_MEAN
#include <Windows.h>
#include <limits.h>
#include <float.h>

#include <xutility>

#define DELAY_RANGE() Sleep(100);     // sleep 100 ms
#define DELAY()       Sleep(10);      // sleep 10 ms

static const uint32_t COLOR_RED     = 0xFFFF0000;
static const uint32_t COLOR_GREEN   = 0xFF00FF00;
static const uint32_t COLOR_BLUE    = 0xFF0000FF;
static const uint32_t COLOR_YELLOW  = 0xFFFFFF00;
static const uint32_t COLOR_MAGENTA = 0xFFFF00FF;
static const uint32_t COLOR_CYAN    = 0xFF00FFFF;

static void simple_nvtxMarker()
{
    // nvtxMark{A,W}

    nvtxMarkA(__FUNCTION__ ":nvtxMarkA");

    DELAY();

    nvtxMarkW(__FUNCTIONW__ L":nvtxMarkW");

    DELAY();

    // nvtxMarkEx

    // zero the structure
    nvtxEventAttributes_t eventAttrib = {0};

    // set the version and the size information
    eventAttrib.version = NVTX_VERSION;
    eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

    // configure the attributes.  0 is the default for all attributes.
    eventAttrib.colorType = NVTX_COLOR_ARGB;
    eventAttrib.color = COLOR_RED;
    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__ ":nvtxMarkEx";
    nvtxMarkEx(&eventAttrib);

    DELAY();
}

static void simple_nvtxRangePushPop()
{
    // nvtxRangePush{A,W}

    nvtxRangePushA(__FUNCTION__ ":nvtxRangePushA");
    DELAY_RANGE();
    nvtxRangePop();

    nvtxRangePushW(__FUNCTIONW__ L":nvtxRangePushW");
    DELAY_RANGE();
    nvtxRangePop();

    // nvtxRangePushEx

    // zero the structure
    nvtxEventAttributes_t eventAttrib = {0};

    // set the version and the size information
    eventAttrib.version = NVTX_VERSION;
    eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

    // configure the attributes.  0 is the default for all attributes.
    eventAttrib.colorType = NVTX_COLOR_ARGB;
    eventAttrib.color = COLOR_GREEN;
    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__ ":nvtxRangePushEx";

    nvtxRangePushEx(&eventAttrib);
    DELAY_RANGE()
    nvtxRangePop();

    DELAY();

    // show nested ranges

    // re-use eventAttrib
    eventAttrib.message.ascii = __FUNCTION__ ":Level 0";
    nvtxRangePushEx(&eventAttrib);
    DELAY();
    eventAttrib.message.ascii = __FUNCTION__ ":Level 1";
    nvtxRangePushEx(&eventAttrib);
    DELAY_RANGE();
    nvtxRangePop(); // Level 1
    DELAY();
    nvtxRangePop(); // Level 0
}


static void simple_nvtxRangeStartEnd()
{
    // nvtxRangeStart{A,W}

    nvtxRangeId_t id1 = nvtxRangeStartA(__FUNCTION__ ":nvtxRangeStartA");
    DELAY_RANGE();
    nvtxRangeEnd(id1);

    nvtxRangeId_t id2 = nvtxRangeStartW(__FUNCTIONW__ L":nvtxRangeStartW");
    DELAY_RANGE();
    nvtxRangeEnd(id2);

    // zero the structure
    nvtxEventAttributes_t eventAttrib = {0};

    // set the version and the size information
    eventAttrib.version = NVTX_VERSION;
    eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

    // configure the attributes.  0 is the default for all attributes.
    eventAttrib.colorType = NVTX_COLOR_ARGB;
    eventAttrib.color = COLOR_BLUE;
    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__ ":nvtxRangeStartEx";

    nvtxRangeId_t id3 = nvtxRangeStartEx(&eventAttrib);
    DELAY_RANGE();
    nvtxRangeEnd(id3);

    // overlapping events

    // re-use eventAttrib
    eventAttrib.message.ascii = __FUNCTION__ ":Range 1";
    nvtxRangeId_t r1 = nvtxRangeStartEx(&eventAttrib);
    DELAY();
    eventAttrib.message.ascii = __FUNCTION__ ":Range 2";
    nvtxRangeId_t r2 = nvtxRangeStartEx(&eventAttrib);
    DELAY_RANGE();
    nvtxRangeEnd(r1);
    DELAY();
    nvtxRangeEnd(r2);

    DELAY();
}

static void attributes_unversioned()
{
    // The version and size field are used by the Tools Extension implementation
    // to handle multiple versions of the attributes structures.  This example
    // shows how to initialize the structure for forwards compatibility.

    // 1. Initialize all fields to 0.  0 is the default value for all fields.
    // This should be done using
    //   a. = {0} or
    //   b. memset(&eventAttrib, 0, NVTX_EVENT_ATTRIB_STRUCT_SIZE);
    // Do not use ordered structure initialization as future version may
    // change the order of fields but maintain source level compatibility.
    //
    // 2. Configure the version field to NVTX_VERSION which is defined in
    // nvToolsExt.h.  The value of this macro will be increased whenever
    // a change is made that break binary compatibility.
    //
    // 3. Configure the size field to NVTX_EVENT_ATTRIB_STRUCT_SIZE.  The value
    // of this macro will be increased whenever the struct tag is changed.

    nvtxEventAttributes_t eventAttrib = {0};
    eventAttrib.version = NVTX_VERSION;
    eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

    eventAttrib.colorType = NVTX_COLOR_ARGB;
    eventAttrib.color = ::COLOR_YELLOW;
    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__;

    nvtxMarkEx(&eventAttrib);

    DELAY();

    // This can be done using C99 designated initializers.
#ifdef SUPPORTS_C99_DESIGNATED_INITIALIZERS
    nvtxEventAttributes_t eventAttrib2 =
    {
        .version = NVTX_VERSION,                // version
        .size = NVTX_EVENT_ATTRIB_STRUCT_SIZE,  // size
        .colorType = NVTX_COLOR_ARGB,           // colorType
        .color = COLOR_YELLOW,                  // color
        .messageType = NVTX_MESSAGE_TYPE_ASCII, // messageType
        .message = __FUNCTION__ ":Designated Initializer"
    };

    nvtxMarkEx(eventAttrib2);

    DELAY();
#endif // SUPPORTS_C99_DESIGNATED_INITIALIZERS
}

static void attributes_versioned()
{
    // The version and size field are used by the Tools Extension implementation
    // to handle multiple versions of the attributes structures.  This example
    // shows how to initialize the structure to a specific version of the library.

    // 1. Initialize all fields to 0.  0 is the default value for all fields.
    // This should be done using
    //   a. = {0} or
    //   b. memset(&eventAttrib, 0, sizeof(nvtxEventAttributes_v1);
    // If you hardcode to a specific version of the structure then ordered
    // structure initialization can be used.
    //
    // 2. Configure the version field to a numeric value that matches version
    // number in the struct tag (nvtxEventAttributes_v#).
    //
    // 3. Configure the size field to sizeof(nvtxEventAttributes_v#).
    //
    // Do not use NVTX_VERSION or NVTX_EVENT_ATTRIB_STRUCT_SIZE.

    nvtxEventAttributes_v1 eventAttrib = {0};
    eventAttrib.version = 1;
    eventAttrib.size = (uint16_t)(sizeof(nvtxEventAttributes_v1));

    eventAttrib.colorType = NVTX_COLOR_ARGB;
    eventAttrib.color = COLOR_MAGENTA;

    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__;

    nvtxMarkEx(&eventAttrib);

    DELAY();

    // This can be done using ordered initialization.  C89/99 only supports
    // initialization of the first member of a union.  This limits payload to
    // ullValue and message to ascii.  See attributes_unversioned() above
    // for an example of C99 designated initializer for alternative syntax
    // option.  Do not use the typedef nvtxEventAttributes_t with ordered
    // initialization, because the typedef is only guaranteed to preserve
    // the named members across versions, not necessarily the order or number
    // of members.

    nvtxEventAttributes_v1 eventAttrib2 =
        {
            1,                                          // version
            (uint16_t)(sizeof(nvtxEventAttributes_v1)), // size
            0,                                          // category    - no limitations
            NVTX_COLOR_ARGB,                            // colorType   - no limitations
            COLOR_CYAN,                                 // color       - no limitations
            NVTX_PAYLOAD_TYPE_UNSIGNED_INT64,           // payloadType - REQUIRED, can only initialize payload.ullValue
            0,                                          // reserved
            1ULL,                                       // payload     - type must be assignable to uint64_t
            NVTX_MESSAGE_TYPE_ASCII,                    // messageType - REQUIRED, can only initialize message.ascii
            __FUNCTION__ ":Ordered Initialization"      // message     - type must be assignable to char*
        };
    nvtxMarkEx(&eventAttrib2);

    DELAY();
}

static void attributes_category()
{
    // The category field is used to group events.  The default category is 0.
    // The caller is responsible for managing categories numbers.

    nvtxEventAttributes_t eventAttrib = {0};
    eventAttrib.version = NVTX_VERSION;
    eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    eventAttrib.category = 1;
    // specifying message to help identify this event in the tool.
    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__;

    nvtxMarkEx(&eventAttrib);

    // Categories can be named using nvtxNameCategory{A,W}().
    nvtxNameCategoryA(1, __FUNCTION__);

    DELAY();
}

static void attributes_color()
{
    // The color field is used to help visually identify events in the tool.
    // The caller must specify valid values for both colorType and color.

    // valid specification of color

    nvtxEventAttributes_t eventAttrib1 = {0};
    eventAttrib1.version = NVTX_VERSION;
    eventAttrib1.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    eventAttrib1.colorType = NVTX_COLOR_ARGB;
    eventAttrib1.color = COLOR_RED;
    // specifying message to help identify this event in the tool.
    eventAttrib1.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib1.message.ascii = __FUNCTION__ ":valid color";
    nvtxMarkEx(&eventAttrib1);

    DELAY();

    // default color

    nvtxEventAttributes_t eventAttrib2 = {0};
    eventAttrib2.version = NVTX_VERSION;
    eventAttrib2.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    // specifying message to help identify this event in the tool.
    eventAttrib2.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib2.message.ascii = __FUNCTION__ ":default color";
    nvtxMarkEx(&eventAttrib2);

    DELAY();

    // invalid specification of color -- missing colorType

    nvtxEventAttributes_t eventAttrib3 = {0};
    eventAttrib3.version = NVTX_VERSION;
    eventAttrib3.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    eventAttrib3.color = COLOR_GREEN;
    // specifying message to help identify this event in the tool.
    eventAttrib3.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib3.message.ascii = __FUNCTION__ ":colorType undefined";
    nvtxMarkEx(&eventAttrib3);

    DELAY();
}

static void attributes_payload()
{
    // The payload field can be used to provide additional data for markers
    // and ranges.  Range events can only specify values at the beginning of a
    // range.
    //
    // The caller must specify valid values for both payloadType and payload.

    // INVALID - payloadType must be defined to a type

    nvtxEventAttributes_t eventAttrib = {0};
    eventAttrib.version = NVTX_VERSION;
    eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    // fail to set eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_UNSIGNED_INT64;
    eventAttrib.payload.ullValue = 1;
    // specifying message to help identify this event in the tool.
    eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib.message.ascii = __FUNCTION__ ":Invalid payloadType";
    nvtxMarkEx(&eventAttrib);

    DELAY();

    // VALID NVTX_PAYLOAD_TYPE_UNSIGNED_INT64
    {
        // NOTE: eventAttrib can be re-used
        nvtxEventAttributes_t eventAttrib = {0};
        eventAttrib.version = NVTX_VERSION;
        eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_UNSIGNED_INT64;
        eventAttrib.payload.llValue = 0;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":UNSIGNED_INT64 = 0";
        nvtxMarkEx(&eventAttrib);

        DELAY();

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_UNSIGNED_INT64;
        eventAttrib.payload.llValue = ULLONG_MAX;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":UNSIGNED_INT64 = ULLONG_MAX =";
        nvtxMarkEx(&eventAttrib);

        DELAY();
    }

    // VALID NVTX_PAYLOAD_TYPE_INT64
    {
        nvtxEventAttributes_t eventAttrib = {0};
        eventAttrib.version = NVTX_VERSION;
        eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_INT64;
        eventAttrib.payload.llValue = 0LL;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":INT64 = 0";
        nvtxMarkEx(&eventAttrib);

        DELAY();

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_INT64;
        eventAttrib.payload.llValue = LLONG_MIN;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":INT64 = LLONG_MIN";
        nvtxMarkEx(&eventAttrib);

        DELAY();

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_INT64;
        eventAttrib.payload.llValue = LLONG_MAX;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":INT64 = LLONG_MAX";
        nvtxMarkEx(&eventAttrib);

        DELAY();
    }

    // VALID NVTX_PAYLOAD_TYPE_UNSIGNED_DOUBLE
    {
        nvtxEventAttributes_t eventAttrib = {0};
        eventAttrib.version = NVTX_VERSION;
        eventAttrib.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_DOUBLE;
        eventAttrib.payload.dValue = 0.0;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":DOUBLE = 0.0";
        nvtxMarkEx(&eventAttrib);

        DELAY();

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_DOUBLE;
        eventAttrib.payload.dValue = DBL_MIN;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":DOUBLE = DBL_MIN";
        nvtxMarkEx(&eventAttrib);

        DELAY();

        eventAttrib.payloadType = NVTX_PAYLOAD_TYPE_DOUBLE;
        eventAttrib.payload.dValue = DBL_MAX;
        eventAttrib.messageType = NVTX_MESSAGE_TYPE_ASCII;
        eventAttrib.message.ascii = __FUNCTION__ ":DOUBLE = DBL_MAX";
        nvtxMarkEx(&eventAttrib);

        DELAY();
    }
}

static void attributes_message()
{
    // The message field can be used to specify an optional string.
    // The caller must specify a messageType and a message.

    // VALID NVTX_MESSAGE_TYPE_ASCII

    nvtxEventAttributes_t eventAttrib1 = {0};
    eventAttrib1.version = NVTX_VERSION;
    eventAttrib1.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    eventAttrib1.messageType = NVTX_MESSAGE_TYPE_ASCII;
    eventAttrib1.message.ascii = __FUNCTION__ ":ascii";
    nvtxMarkEx(&eventAttrib1);

    DELAY();

    // VALID NVTX_MESSAGE_TYPE_UNICODE

    nvtxEventAttributes_t eventAttrib2 = {0};
    eventAttrib2.version = NVTX_VERSION;
    eventAttrib2.size = NVTX_EVENT_ATTRIB_STRUCT_SIZE;
    eventAttrib2.messageType = NVTX_MESSAGE_TYPE_UNICODE;
    eventAttrib2.message.unicode = __FUNCTIONW__ L":unicode \u2603 snowman";
    nvtxMarkEx(&eventAttrib2);

    DELAY();
}

static void name_thread()
{
    // The caller can name threads in the current process.
    nvtxNameOsThreadA(::GetCurrentThreadId(), "main");
};

int main(int argc, char* argv[])
{
    // Events

    simple_nvtxMarker();
    simple_nvtxRangeStartEnd();
    simple_nvtxRangePushPop();

    // Events with Attributes

    attributes_versioned();
    attributes_unversioned();

    attributes_category();
    attributes_color();
    attributes_payload();
    attributes_message();

    // Resource Naming

    name_thread();
    // see attributes_category for example of naming a category

    return 0;
}

