#ifndef IMAGE_DENOISING_H
#define IMAGE_DENOISING_H

typedef unsigned int TColor;

// Isolated definition
typedef struct { unsigned char x, y, z, w; } uchar4;

// functions to load images
extern "C" void LoadBMPFile(uchar4 * *dst, int* width, int* height, const char* name);

#endif
