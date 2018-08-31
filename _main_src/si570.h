
#ifndef _SI570_H_
#define _SI570_H_

// *****************************************************
// Notes
// *****************************************************
// - The purpose of this driver is to provide utilities
//   for setting the ZC702 on-board clock oscillator
//   (SI570) to various common video pixel clock rates.
//   The driver uses a look-up table whose values were
//   calculated using SiLabs utility software for
//   determining register values. This driver does NOT
//   calculate those values on the fly, so only the
//   frequencies listed in si570_freq_id_t enumeration
//   are supported.
// - Most of this code is adapted from:
//   http://www.xilinx.com/support/documentation/boards_and_kits/zc702_zvik/2014_4/xtp181-zc702-si570-prog-c-2014-4.pdf

// *****************************************************
// Dependencies
// *****************************************************
#include "xiicps.h"

// *****************************************************
// Constants
// *****************************************************
#define I2C_MUX_CHIP_ADDR    0x74
#define SI570_I2C_CHIP_ADDR  0x5D

// *****************************************************
// Function status return values
// *****************************************************
#define SI570_SUCCESS        0
#define SI570_ERR_UNKNOWN   -1

// *****************************************************
// Enumerations
// *****************************************************
typedef enum
{
	SI570_FREQ_25_175_000  = 0,
	SI570_FREQ_27_000_000  = 1,
	SI570_FREQ_40_000_000  = 2,
	SI570_FREQ_65_000_000  = 3,
	SI570_FREQ_74_250_000  = 4,
	SI570_FREQ_110_000_000 = 5,
	SI570_FREQ_148_500_000 = 6,
	SI570_FREQ_162_000_000 = 7,
	SI570_NUM_FREQS        = 8
} si570_freq_id_t;

// *****************************************************
// Object
// *****************************************************
typedef struct si570
{
	XIicPs* p_si570_iic_inst;
	
} si570_t;

// *****************************************************
// Public functions
// *****************************************************

// si570_init() - Initialize drivers for all peripherals
//                and set them to a known power-on state.
//   - p_si570_inst        - Pointer to object to work on
//   - si570_iic_device_id - Device ID for the I2C instance that controls the SI570 clock generator
//   - return              - Function status return value (see above)
int si570_init
(
	si570_t*     p_si570_inst,
	unsigned int si570_iic_device_id
);

// si570_set_freq() - Set the output frequency of the Si570 to
//                    the desired rate.
//   - p_si570_inst - Pointer to object to work on
//   - freq_id      - Which output frequency to use
//   - return       - None
void si570_set_freq
(
	si570_t*        p_si570_inst,
	si570_freq_id_t freq_id
);

// si5750_print_regs() - Print the current state of the relevant
//                       Si570 registers for debugging purposes.
//   - p_si570_inst - Pointer to object to work on
//   - return       - None
void si5750_print_regs
(
	si570_t* p_si570_inst
);

#endif // _SI570_H_

