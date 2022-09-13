// Required header to support CUDA vector types
#include <vector_types.h>

////////////////////////////////////////////////////////////////////////////////
// export C interface
extern "C" void computeGold(char *reference, char *idata,const unsigned int len);
extern "C" void computeGold2(int2 *reference, int2 *idata,const unsigned int len);

////////////////////////////////////////////////////////////////////////////////
//! Compute reference data set
//! Each element is multiplied with the number of threads / array length
//! @param reference  reference data, computed but preallocated
//! @param idata      input data as provided to device
//! @param len        number of elements in reference / idata
////////////////////////////////////////////////////////////////////////////////
void computeGold(char* reference, char* idata, const unsigned int len)
{
    for (unsigned int i = 0; i < len; ++i)
    {
        reference[i] = idata[i] - 10;
    }
}

////////////////////////////////////////////////////////////////////////////////
//! Compute reference data set for int2 version
//! Each element is multiplied with the number of threads / array length
//! @param reference  reference data, computed but preallocated
//! @param idata      input data as provided to device
//! @param len        number of elements in reference / idata
////////////////////////////////////////////////////////////////////////////////
void computeGold2(int2* reference, int2* idata, const unsigned int len)
{
    for (unsigned int i = 0; i < len; ++i)
    {
        reference[i].x = idata[i].x - idata[i].y;
        reference[i].y = idata[i].y;
    }
}

