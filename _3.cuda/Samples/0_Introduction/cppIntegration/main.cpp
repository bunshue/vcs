// includes, system
#include <stdlib.h>
#include <iostream>

// Required to include CUDA vector types
#include <cuda_runtime.h>
#include <vector_types.h>
#include <helper_cuda.h>

////////////////////////////////////////////////////////////////////////////////
// declaration, forward
extern "C" bool runTest(const int argc, const char** argv, char* data, int2 * data_int2, unsigned int len);

////////////////////////////////////////////////////////////////////////////////
// Program main
////////////////////////////////////////////////////////////////////////////////
int main(int argc, char** argv)
{
    // input data
    int len = 16;
    // the data has some zero padding at the end so that the size is a multiple of
    // four, this simplifies the processing as each thread can process four
    // elements (which is necessary to avoid bank conflicts) but no branching is
    // necessary to avoid out of bounds reads
    //              H     e   l    l     o       W   o   r    l    d   .
    char str[] = { 82,  111, 118, 118, 121, 42, 97, 121,124, 118, 110, 56,  10,  10, 10, 10 };

    // Use int2 showing that CUDA vector types can be used in cpp code
    int2 i2[16];

    for (int i = 0; i < len; i++)
    {
        i2[i].x = str[i];
        i2[i].y = 10;
    }

    bool bTestResult;

    // run the device part of the program
    bTestResult = runTest(argc, (const char**)argv, str, i2, len);

    std::cout << str << std::endl;

    char str_device[16];

    for (int i = 0; i < len; i++)
    {
        str_device[i] = (char)(i2[i].x);
    }

    std::cout << str_device << std::endl;

    exit(bTestResult ? EXIT_SUCCESS : EXIT_FAILURE);
}


