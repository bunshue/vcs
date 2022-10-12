#include <assert.h>
#include "histogram_common.h"

extern "C" void histogram64CPU(uint *h_Histogram, void *h_Data,
                               uint byteCount) {
  for (uint i = 0; i < HISTOGRAM64_BIN_COUNT; i++) h_Histogram[i] = 0;

  assert(sizeof(uint) == 4 && (byteCount % 4) == 0);

  for (uint i = 0; i < (byteCount / 4); i++) {
    uint data = ((uint *)h_Data)[i];
    h_Histogram[(data >> 2) & 0x3FU]++;
    h_Histogram[(data >> 10) & 0x3FU]++;
    h_Histogram[(data >> 18) & 0x3FU]++;
    h_Histogram[(data >> 26) & 0x3FU]++;
  }
}

extern "C" void histogram256CPU(uint *h_Histogram, void *h_Data,
                                uint byteCount) {
  for (uint i = 0; i < HISTOGRAM256_BIN_COUNT; i++) h_Histogram[i] = 0;

  assert(sizeof(uint) == 4 && (byteCount % 4) == 0);

  for (uint i = 0; i < (byteCount / 4); i++) {
    uint data = ((uint *)h_Data)[i];
    h_Histogram[(data >> 0) & 0xFFU]++;
    h_Histogram[(data >> 8) & 0xFFU]++;
    h_Histogram[(data >> 16) & 0xFFU]++;
    h_Histogram[(data >> 24) & 0xFFU]++;
  }
}
