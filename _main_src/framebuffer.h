
#ifndef _FRAMEBUFFER_H_
#define _FRAMEBUFFER_H_

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
#include "xaxivdma.h"

// *****************************************************
// Function status return values
// *****************************************************
#define FRAMEBUFFER_SUCCESS        0
#define FRAMEBUFFER_ERROR_UNKNOWN -1

// *****************************************************
// Public functions
// *****************************************************

// framebuffer_run() - Set up and start VDMA instance to run.
//                     The function uses the number of frames
//                     that the hardware is configured for.
//   - p_vdma_inst_write  - Pointer to write object to work on
//   - p_vdma_inst_read   - Pointer to read object to work on
//   - bits_per_pixel - Number of bits per pixel
//   - hsize          - Horizontal frame size (pixels per line)
//   - vsize          - Vertical frame size (lines per frame)
//   - buf_base_addr  - Base address where frame buffers will be stored
//   - return         - Function status return value (see above)
int framebuffer_run
(
	XAxiVdma*    p_vdma_inst_write,
	XAxiVdma*    p_vdma_inst_read,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr
);

// framebuffer_write() - Set up and start VDMA instance to run.
//                     The function uses the number of frames
//                     that the hardware is configured for.
//   - p_vdma_inst  - Pointer to write object to work on
//   - bits_per_pixel - Number of bits per pixel
//   - hsize          - Horizontal frame size (pixels per line)
//   - vsize          - Vertical frame size (lines per frame)
//   - buf_base_addr  - Base address where frame buffers will be stored
//   - return         - Function status return value (see above)
int framebuffer_write
(
	XAxiVdma*    p_vdma_inst,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr,
	unsigned int stride
);

// framebuffer_read() - Set up and start VDMA instance to run.
//                     The function uses the number of frames
//                     that the hardware is configured for.
//   - p_vdma_inst  - Pointer to read object to work on
//   - bits_per_pixel - Number of bits per pixel
//   - hsize          - Horizontal frame size (pixels per line)
//   - vsize          - Vertical frame size (lines per frame)
//   - buf_base_addr  - Base address where frame buffers will be stored
//   - return         - Function status return value (see above)
int framebuffer_read
(
	XAxiVdma*    p_vdma_inst,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr,
	unsigned int stride
);

// framebuffer_dump_vdma_regs() - Print the current state of the relevant
//                                VDMA registers for debugging purposes.
//   - p_vdma_inst - Pointer to object to work on
//   - return      - None
void framebuffer_dump_vdma_regs
(
	XAxiVdma* p_vdma_inst
);


uint32_t vdma_reset(XAxiVdma *VDMAPtr, uint32_t direction);







#endif // _FRAMEBUFFER_H_

