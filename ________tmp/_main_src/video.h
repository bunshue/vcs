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
//                     Copyright(c) 2011 Avnet, Inc.
//                             All rights reserved.
//
//----------------------------------------------------------------
//
// Create Date:         Sep 01, 2011
// Design Name:         FMC-IMAGEON
// Module Name:         fmc_imageon.h
// Project Name:        FMC-IMAGEON
// Target Devices:      Spartan-6, Virtex-6
//                      Artix-7, Kintex-7, Virtex-7, Zynq
// Avnet Boards:        FMC-IMAGEON
//
// Tool versions:       Vivado 2013.3
//
// Description:         FMC-IMAGEON Software Library.
//                      Includes functions for:
//                      - I2C Multiplexer
//                      - I2C I/O Expander
//                      - HDMI Input Configuration
//                      - HDMI Output Configuration
//
// Dependencies:        
//
// Revision:            Sep 01, 2011: 1.01 Initial version
//                      Nov 14, 2011: 1.02 Add HDMI I2C config sequences
//                                         Add multiple I2C mux selections
//                      Dec 10, 2011: 1.03 Add HDMI functions
//                                         - fmc_imageon_hdmii_get_lock
//                                         - fmc_imageon_hdmii_get_timing
//                                         - fmc_imageon_hdmio_set_timing
//                      Feb 16, 2012: 1.04 Modify HDMI functions
//                                         - HDMI input
//                                            - I2C config for SPDIF
//                                         - HDMI output
//                                            - I2C config for SPDIF
//                                            - implement WaitForHPD
//                      Feb 21, 2012: 1.05 Modify HDMI output function
//                                         - set HDMI/DVI mode according
//                                           to pTiming argument
//                      Apr 13, 2012: 1.06 Fix typo in verbose
//                      Aug 15, 2012: 1.07 Set ADV7511 clock delay to 101 (+0.8ns)
//                      Nov 28, 2012: 2.01 Configure ADV7611 LLC for inverse polarity
//                                         for FMC-IMAGEON Rev.B hardware
//                                         
//----------------------------------------------------------------

#ifndef __FMC_IMAGEON_H__
#define __FMC_IMAGEON_H__

#include <stdio.h>

// Located in: microblaze_0/include/
#include "xparameters.h"
#include "xstatus.h"

//#include "fmc_iic.h"

// Detailed ADV7611 I2C addresses
#define IIC_ADV7611_BASE_ADDR        0x98
#define IIC_ADV7611_CEC_ADDR         0x80
//#define IIC_ADV7611_INFOFRAME_ADDR   0x7C  => I2C Address conflict with ADV7511 (Fixed I2C Address at 0x7C)
#define IIC_ADV7611_INFOFRAME_ADDR   0x6A
#define IIC_ADV7611_DPLL_ADDR        0x4C
#define IIC_ADV7611_KSV_ADDR         0x64
#define IIC_ADV7611_EDID_ADDR        0x6C
#define IIC_ADV7611_HDMI_ADDR        0x68
#define IIC_ADV7611_CP_ADDR          0x44

// Detailed ADV7511 I2C addresses
#define IIC_ADV7511_BASE_ADDR        0x72


// FMC-IMAGEON I2C addresses
#define FMC_IMAGEON_I2C_MUX_ADDR  0x70 // 0xE0/0xE1 (PCA9546A)
#define FMC_IMAGEON_IO_EXP_ADDR   0x20 // 0x40/0x41 (PCA9534)
#define FMC_IMAGEON_VID_CLK_ADDR  0x65 // 0xCA/0xCB (CDCE913)
#define FMC_IMAGEON_HDMI_IN_ADDR  (IIC_ADV7611_BASE_ADDR>>1) // 0x98/0x99 (ADV7611)
#define FMC_IMAGEON_HDMI_OUT_ADDR (IIC_ADV7511_BASE_ADDR>>1) // 0x72/0x73 (ADV7511)
#define FMC_IMAGEON_DDCEDID_ADDR  0x50 // 0xA0/0xA1


//struct struct_fmc_imageon_t
//{
//   // software library version
//   uint32_t uVersion;
//
//   // instantiation-specific name
//   char szName[32];
//
//   // pointer to FMC-IIC instance
//   fmc_iic_t *pIIC;
//
//   // GPIO value
//   uint32_t GpioData;
//
//   // Verblse
//   uint32_t bVerbose;
//};
//typedef struct struct_fmc_imageon_t fmc_imageon_t;

struct struct_video_timing_t
{
   //char *pName;
   
   // General info
   uint32_t IsHDMI;
   uint32_t IsEncrypted;
   uint32_t IsInterlaced;
   uint32_t ColorDepth;

   // Horizontal Timing
   uint32_t HActiveVideo;
   uint32_t HFrontPorch;
   uint32_t HSyncWidth;
   uint32_t HBackPorch;
   uint32_t HSyncPolarity;

   // Vertical Timing   
   uint32_t VActiveVideo;
   uint32_t VFrontPorch;
   uint32_t VSyncWidth;
   uint32_t VBackPorch;
   uint32_t VSyncPolarity;
};
typedef struct struct_video_timing_t video_timing_t;


//int fmc_imageon_init( fmc_imageon_t *pContext, char szName[], fmc_iic_t *pIIC );

// I2C MUX Functions
//void fmc_imageon_iic_mux_reset( fmc_imageon_t *pContext );
//void fmc_imageon_iic_mux( fmc_imageon_t *pContext, uint32_t MuxSelect );
// Single Mux Selections
#define FMC_IMAGEON_I2C_MIN               0
#define FMC_IMAGEON_I2C_MAX               3
#define FMC_IMAGEON_I2C_SELECT_DDCEDID    0
#define FMC_IMAGEON_I2C_SELECT_HDMI_OUT   1
#define FMC_IMAGEON_I2C_SELECT_HDMI_IN    2
#define FMC_IMAGEON_I2C_SELECT_IO_EXP     3
#define FMC_IMAGEON_I2C_SELECT_VID_CLK    3
// Multiple Mux Selections
#define FMC_IMAGEON_I2C_SELECT_HDMI       4 // select both HDMI_IN and HDMI_OUT

// General I2C Configuration Functions
//void fmc_imageon_iic_config2( fmc_imageon_t *pContext, uint8_t ChipAddress,
//                              uint8_t ConfigData[][2], uint32_t ConfigLength );
//void fmc_imageon_iic_config3( fmc_imageon_t *pContext,
//                              uint8_t ConfigData[][3], uint32_t ConfigLength );

// Video Clock Synthesizer Functions
//void fmc_imageon_vclk_init( fmc_imageon_t *pContext );
//void fmc_imageon_vclk_config( fmc_imageon_t *pContext, uint32_t FreqId );
#define FMC_IMAGEON_VCLK_FREQ_25_175_000       0
#define FMC_IMAGEON_VCLK_FREQ_27_000_000       1
#define FMC_IMAGEON_VCLK_FREQ_40_000_000       2
#define FMC_IMAGEON_VCLK_FREQ_65_000_000       3
#define FMC_IMAGEON_VCLK_FREQ_74_250_000       4
#define FMC_IMAGEON_VCLK_FREQ_110_000_000      5
#define FMC_IMAGEON_VCLK_FREQ_148_500_000      6
#define FMC_IMAGEON_VCLK_FREQ_162_000_000      7

// HDMI Input Functions
//int fmc_imageon_hdmii_init( fmc_imageon_t *pContext, uint32_t Enable, uint32_t edidInit, uint8_t pEdid[256] );
//int fmc_imageon_hdmii_init2( fmc_imageon_t *pContext, uint32_t Enable, uint32_t edidInit, uint8_t pEdid[256], uint32_t llc_polarity, uint32_t llc_delay );
//int fmc_imageon_hdmii_set_hpd( fmc_imageon_t *pContext, uint32_t HotPlugStatus );
//int fmc_imageon_hdmii_set_rst( fmc_imageon_t *pContext, uint32_t Reset );
//int fmc_imageon_hdmii_get_int( fmc_imageon_t *pContext, uint32_t *pIntStatus );
//int fmc_imageon_hdmii_get_lock( fmc_imageon_t *pContext );
//int fmc_imageon_hdmii_get_timing( fmc_imageon_t *pContext, fmc_imageon_video_timing_t *pTiming );

// HDMI Output Functions
//int fmc_imageon_hdmio_init( fmc_imageon_t *pContext, uint32_t Enable, fmc_imageon_video_timing_t *pTiming, uint32_t WaitForHPD );
//int fmc_imageon_hdmio_set_pd( fmc_imageon_t *pContext, uint32_t PowerDown );
//int fmc_imageon_hdmio_get_hpd( fmc_imageon_t *pContext, uint32_t *pHotPlugDetect );

// DDC/EDID Functions
//int fmc_imageon_hdmii_read_edid( fmc_imageon_t *pContext, uint8_t data[256] );
//int fmc_imageon_hdmii_write_edid( fmc_imageon_t *pContext, uint8_t data[256] );
//int fmc_imageon_hdmio_read_edid( fmc_imageon_t *pContext, uint8_t data[256] );

// Delay Functions
void fmc_imageon_wait_usec(unsigned int delay);

#endif // __FMC_IMAGEON_H__
