
#ifndef _TEST_PATTERN_GEN_H_
#define _TEST_PATTERN_GEN_H_

// *****************************************************
// Dependencies
// *****************************************************
#include "xv_tpg.h"

// *****************************************************
// Function status return values
// *****************************************************
#define TEST_PATTERN_GEN_SUCCESS        0
#define TEST_PATTERN_GEN_ERROR_UNKNOWN -1

// *****************************************************
// Public functions
// *****************************************************

// test_pattern_gen_config() - Set up and start TPG registers and enable.
//   - p_tpg_inst  - Pointer to object to work on
//   - hsize       - Active horizontal frame size
//   - vsize       - Active vertical frame size
//   - bypass      - Whether or not to bypass the TPG
//   - box_is_blue - 1 sets the overlay box to blue, 0 sets it to red (for differentiating between TPG on the new and old scaler datapaths)
//   - print_regs  - Whether or not to dump registers (for debugging purposes)
//   - return      - None
void test_pattern_gen_config
(
	XV_tpg*       p_tpg_inst,
	unsigned int  hsize,
	unsigned int  vsize,
	unsigned int  bypass,
	unsigned int  box_is_blue,
	unsigned int  cfmt,
	unsigned int  background,
	unsigned char print_regs
);

#endif // _TEST_PATTERN_GEN_H_
