#ifndef __H_UTIL_
#define __H_UTIL_

extern "C"
void dumpBGR(float* d_srcBGR, int pitch, int width, int height, int batchSize, char* folder, char* tag);
extern "C"
void dumpYUV(unsigned char* d_nv12, int size, char* folder, char* tag);
#endif
