#ifndef _MANDELBROT_KERNEL_h_
#define _MANDELBROT_KERNEL_h_

#include <vector_types.h>

extern "C" void RunMandelbrot0(uchar4 * dst, const int imageW, const int imageH,
    const int crunch, const double xOff,
    const double yOff, const double xjp,
    const double yjp, const double scale,
    const uchar4 colors, const int frame,
    const int animationFrame, const int mode,
    const int numSMs, const bool isJ,
    int version = 13);
extern "C" void RunMandelbrot1(uchar4 * dst, const int imageW, const int imageH,
    const int crunch, const double xOff,
    const double yOff, const double xjp,
    const double yjp, const double scale,
    const uchar4 colors, const int frame,
    const int animationFrame, const int mode,
    const int numSMs, const bool isJ,
    int version = 13);

#endif
