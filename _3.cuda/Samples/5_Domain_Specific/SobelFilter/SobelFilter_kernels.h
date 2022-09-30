#ifndef __SOBELFILTER_KERNELS_H_
#define __SOBELFILTER_KERNELS_H_

typedef unsigned char Pixel;

// global determines which filter to invoke
enum SobelDisplayMode {
	SOBELDISPLAY_IMAGE = 0,
	SOBELDISPLAY_SOBELTEX,
	SOBELDISPLAY_SOBELSHARED
};

extern enum SobelDisplayMode g_SobelDisplayMode;

extern "C" void sobelFilter(Pixel * odata, int iw, int ih, enum SobelDisplayMode mode, float fScale);
extern "C" void setupTexture(int iw, int ih, Pixel * data, int Bpp);
extern "C" void deleteTexture(void);
extern "C" void initFilter(void);

#endif
