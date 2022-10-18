#ifndef _FDTD3DREFERENCE_H_
#define _FDTD3DREFERENCE_H_

void generateRandomData(float* data, const int dimx, const int dimy,
    const int dimz, const float lowerBound,
    const float upperBound);
void generatePatternData(float* data, const int dimx, const int dimy,
    const int dimz, const float lowerBound,
    const float upperBound);
bool fdtdReference(float* output, const float* input, const float* coeff,
    const int dimx, const int dimy, const int dimz,
    const int radius, const int timesteps);
bool compareData(const float* output, const float* reference, const int dimx,
    const int dimy, const int dimz, const int radius,
    const float tolerance = 0.0001f);

#endif
