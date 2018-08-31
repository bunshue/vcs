
#ifndef _MIXER_H_
#define _MIXER_H_

// *****************************************************
// Notes
// *****************************************************
//   - The purpose of this driver is to provide a layer
//     of abstraction over the AXI VDMA drivers. It
//     assumes the caller has allocated and initialized
//     the XAxiVdma instance to be used.

// *****************************************************
// Dependencies
// *****************************************************
#include "xv_mix_l2.h"

// *****************************************************
// Function status return values
// *****************************************************
#define MIXER_SUCCESS        0
#define MIXER_ERROR_UNKNOWN -1

#define CAMERA_STRIDE 	2048
//#define GUI_STRIDE 		8192
#define GUI_STRIDE 		1920*4

void ConfigMixer(XV_Mix_l2 *mix, XVidC_VideoStream *StreamPtr, unsigned int MemAddr);
void RunMixer(XV_Mix_l2 *mix);

#endif // _MIXER_H_

