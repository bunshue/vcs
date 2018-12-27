//
// This design is the property of Avnet.  Publication of this
// design is not authorized without written consent from Avnet.
// 
// Please direct any questions to:  technical.support@avnet.com
//
// Disclaimer:
//    Avnet, Inc. makes no warranty for the use of this code or design.
//    This code is provided  "As Is". Avnet, Inc assumes no responsibility for
//    any errors, which may appear in this code, nor does it make a commitment
//    to update the information contained herein. Avnet, Inc specifically
//    disclaims any implied warranties of fitness for a particular purpose.
//                     Copyright(c) 2010 Avnet, Inc.
//                             All rights reserved.
//
//----------------------------------------------------------------
//
// Create Date:         Mar 05, 2010
// Design Name:         Video Resolution utility
// Module Name:         video_resolution.h
// Project Name:        FMC-IMAGEON
// Target Devices:      Zynq-7000 SoC
// Avnet Boards:        FMC-IMAGEON
//
// Tool versions:       ISE 14.3
//
// Description:         IVK Video Resolution
//                      - video timing definitions
//                      - video resolution detection
//
// Dependencies:        
//
// Revision:            Mar 05, 2010: 1.00 Initial version for S6-IVK
//                      Dec 03, 2011: 1.01 Reuse for FMC-IMAGEON
//                      Nov 01, 2012: 1.02 Add 576P resolution
//
//----------------------------------------------------------------

#ifndef __VIDEO_RESOLUTION_H__
#define __VIDEO_RESOLUTION_H__

#include "xil_types.h"

// Video Pattern Generator - Video Resolution values
#define VIDEO_RESOLUTION_VGA       0
#define VIDEO_RESOLUTION_480P      1
#define VIDEO_RESOLUTION_576P      2
#define VIDEO_RESOLUTION_SVGA      3
#define VIDEO_RESOLUTION_XGA       4
#define VIDEO_RESOLUTION_720P      5
#define VIDEO_RESOLUTION_SXGA      6
#define VIDEO_RESOLUTION_1080P     7
#define VIDEO_RESOLUTION_UXGA      8
#define NUM_VIDEO_RESOLUTIONS      9

struct struct_vres_timing_t
{
	char *pName;
	uint32_t VActiveVideo;
	uint32_t VFrontPorch;
	uint32_t VSyncWidth;
	uint32_t VBackPorch;
	uint32_t VSyncPolarity;
	uint32_t HActiveVideo;
	uint32_t HFrontPorch;
	uint32_t HSyncWidth;
	uint32_t HBackPorch;
	uint32_t HSyncPolarity;
};
typedef struct struct_vres_timing_t vres_timing_t;

char *  vres_get_name(uint32_t resolutionId);
uint32_t vres_get_width(uint32_t resolutionId);
uint32_t vres_get_height(uint32_t resolutionId);
uint32_t vres_get_timing(uint32_t resolutionId, vres_timing_t *pTiming );

int32_t vres_detect( uint32_t width, uint32_t height );


#endif // __VIDEO_RESOLUTION_H__
