
// *****************************************************
// Dependencies
// *****************************************************
#include "framebuffer.h"

// *****************************************************
// Private functions
// *****************************************************

// set_vdma_write() - Set up and the write side of the VDMA instance.
//                    The function uses the number of frames that the
//                    hardware is configured for.
//   - p_vdma_inst    - Pointer to object to work on
//   - bits_per_pixel - Number of bits per pixel
//   - hsize          - Horizontal frame size (pixels per line)
//   - vsize          - Vertical frame size (lines per frame)
//   - buf_base_addr  - Base address where frame buffers will be stored
//   - return         - Function status return value (see above)
static int set_vdma_write
(
	XAxiVdma*    p_vdma_inst,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr,
	unsigned int stride
)
{
	// Local variables
	int               status      = 0;
	XAxiVdma_DmaSetup write_setup_inst;
	int               cur_fb_addr = 0;
	int               ii          = 0;

	// Set VDMA register values
	write_setup_inst.VertSizeInput       = vsize;
	write_setup_inst.HoriSizeInput       = hsize * bits_per_pixel / 8;
	write_setup_inst.Stride              = stride;
	write_setup_inst.FrameDelay          = 0;
	write_setup_inst.EnableCircularBuf   = 1;
	write_setup_inst.EnableSync          = 1; // Enable genlock
	write_setup_inst.PointNum            = 0; // Write side is master
	write_setup_inst.EnableFrameCounter  = 0;
	write_setup_inst.FixedFrameStoreAddr = 0; // Not parking

	status = XAxiVdma_DmaConfig(p_vdma_inst, XAXIVDMA_WRITE, &write_setup_inst);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the VDMA write channel.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Compute buffer addresses
	cur_fb_addr = buf_base_addr;
	for (ii = 0; ii < p_vdma_inst->MaxNumFrames; ii++)
	{
		write_setup_inst.FrameStoreStartAddr[ii] = cur_fb_addr;
		cur_fb_addr += write_setup_inst.Stride * write_setup_inst.VertSizeInput;
	}

	// Set buffer addresses
	status = XAxiVdma_DmaSetBufferAddr(p_vdma_inst, XAXIVDMA_WRITE, write_setup_inst.FrameStoreStartAddr);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the VDMA write frame addresses.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Clear frame buffer data
	memset((void*)buf_base_addr, 0, write_setup_inst.Stride * write_setup_inst.VertSizeInput * 3);

	return FRAMEBUFFER_SUCCESS;
}

// set_vdma_read() - Set up and the read side of the VDMA instance.
//                   The function uses the number of frames that the
//                   hardware is configured for.
//   - p_vdma_inst    - Pointer to object to work on
//   - bits_per_pixel - Number of bits per pixel
//   - hsize          - Horizontal frame size (pixels per line)
//   - vsize          - Vertical frame size (lines per frame)
//   - buf_base_addr  - Base address where frame buffers will be stored
//   - return         - Function status return value (see above)
static int set_vdma_read
(
	XAxiVdma*    p_vdma_inst,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr,
	unsigned int stride
)
{
	// Local variables
	int               status            = 0;
	XAxiVdma_DmaSetup read_setup_inst;
	int               cur_fb_addr       = 0;
	int               ii                = 0;

	// Set VDMA register values
	read_setup_inst.VertSizeInput       = vsize;
	read_setup_inst.HoriSizeInput       = hsize * bits_per_pixel / 8;
	read_setup_inst.Stride              = stride;
	read_setup_inst.FrameDelay          = 1;
	read_setup_inst.EnableCircularBuf   = 1;
	read_setup_inst.EnableSync          = 1; // Enable genlock
	//read_setup_inst.EnableSync          = 0; // Disable genlock
	read_setup_inst.PointNum            = 1;
	read_setup_inst.EnableFrameCounter  = 0;
	read_setup_inst.FixedFrameStoreAddr = 0; // Not parking

	status = XAxiVdma_DmaConfig(p_vdma_inst, XAXIVDMA_READ, &read_setup_inst);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the VDMA read channel.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	// Compute buffer addresses
	cur_fb_addr = buf_base_addr;
	for (ii = 0; ii < p_vdma_inst->MaxNumFrames; ii++)
	{
		read_setup_inst.FrameStoreStartAddr[ii] = cur_fb_addr;
		cur_fb_addr += read_setup_inst.Stride * read_setup_inst.VertSizeInput;
	}

	// Set buffer addresses
	status = XAxiVdma_DmaSetBufferAddr(p_vdma_inst, XAXIVDMA_READ, read_setup_inst.FrameStoreStartAddr);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to configure the VDMA read frame addresses.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	return FRAMEBUFFER_SUCCESS;
}

// read_vdma_regs() - Helper function for framebuffer_dump_vdma_regs()
//                    which dumps the actual register values.
//   - p_vdma_inst - Pointer to object to work on
static void read_vdma_regs
(
	XAxiVdma* p_vdma_inst
)
// Helper function for dump_vdma_regs()
{
	// Local variables
	int offset = 0;

	xil_printf("\n\rRead side (MM2S)\n\r");
	offset = XAXIVDMA_TX_OFFSET+XAXIVDMA_CR_OFFSET;
	xil_printf("MM2S_VDMACR         (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_TX_OFFSET+XAXIVDMA_SR_OFFSET;
	xil_printf("MM2S_VDMASR         (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_MM2S_ADDR_OFFSET+XAXIVDMA_VSIZE_OFFSET;
	xil_printf("MM2S_VSIZE          (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_MM2S_ADDR_OFFSET+XAXIVDMA_HSIZE_OFFSET;
	xil_printf("MM2S_HSIZE          (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_MM2S_ADDR_OFFSET+XAXIVDMA_STRD_FRMDLY_OFFSET;
	xil_printf("MM2S_FRMDLY_STRIDE  (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_MM2S_ADDR_OFFSET+XAXIVDMA_START_ADDR_OFFSET+0x0;
	xil_printf("MM2S_START_ADDRESS0 (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_MM2S_ADDR_OFFSET+XAXIVDMA_START_ADDR_OFFSET+0x4;
	xil_printf("MM2S_START_ADDRESS1 (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_MM2S_ADDR_OFFSET+XAXIVDMA_START_ADDR_OFFSET+0x8;
	xil_printf("MM2S_START_ADDRESS2 (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));

	xil_printf("\n\rWrite side (S2MM)\n\r");
	offset = XAXIVDMA_RX_OFFSET+XAXIVDMA_CR_OFFSET;
	xil_printf("S2MM_VDMACR         (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_RX_OFFSET+XAXIVDMA_SR_OFFSET;
	xil_printf("S2MM_VDMASR         (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_S2MM_ADDR_OFFSET+XAXIVDMA_VSIZE_OFFSET;
	xil_printf("S2MM_VSIZE          (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_S2MM_ADDR_OFFSET+XAXIVDMA_HSIZE_OFFSET;
	xil_printf("S2MM_HSIZE          (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_S2MM_ADDR_OFFSET+XAXIVDMA_STRD_FRMDLY_OFFSET;
	xil_printf("S2MM_FRMDLY_STRIDE  (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_S2MM_ADDR_OFFSET+XAXIVDMA_START_ADDR_OFFSET+0x0;
	xil_printf("S2MM_START_ADDRESS0 (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_S2MM_ADDR_OFFSET+XAXIVDMA_START_ADDR_OFFSET+0x4;
	xil_printf("S2MM_START_ADDRESS1 (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_S2MM_ADDR_OFFSET+XAXIVDMA_START_ADDR_OFFSET+0x8;
	xil_printf("S2MM_START_ADDRESS2 (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));

	xil_printf("\n\rMiscellaneous\n\r");
	offset = XAXIVDMA_PARKPTR_OFFSET;
	xil_printf("PARKPTR     (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
	offset = XAXIVDMA_VERSION_OFFSET;
	xil_printf("VERSION     (0x%02X) = 0x%08X\n\r", offset, XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, offset));
}

// *****************************************************
// Public functions
// *****************************************************
//int framebuffer_run
//(
//	XAxiVdma*    p_vdma_inst_write,
//	XAxiVdma*    p_vdma_inst_read,
//	unsigned int bits_per_pixel,
//	unsigned int hsize,
//	unsigned int vsize,
//	unsigned int buf_base_addr
//)
//{
//	// Local variables
//	int status = 0;
//
//	// Setup read channel
//	if(p_vdma_inst_read != NULL) {
//		status = framebuffer_read(p_vdma_inst_read, bits_per_pixel, hsize, vsize, buf_base_addr);
//		if (status != XST_SUCCESS)
//		{
//			xil_printf("ERROR! Failed to start the read side of the VDMA.\n\r");
//			return FRAMEBUFFER_ERROR_UNKNOWN;
//		}
//	}
//
//	// Setup write channel
//	if(p_vdma_inst_write != NULL) {
//		status = framebuffer_write(p_vdma_inst_write, bits_per_pixel, hsize, vsize, buf_base_addr);
//		if (status != XST_SUCCESS)
//		{
//			xil_printf("ERROR! Failed to start the write side of the VDMA.\n\r");
//			return FRAMEBUFFER_ERROR_UNKNOWN;
//		}
//	}
//
//	// Start write side
//	if(p_vdma_inst_write != NULL) {
//		status = XAxiVdma_DmaStart(p_vdma_inst_write, XAXIVDMA_WRITE);
//		if (status != XST_SUCCESS)
//		{
//			xil_printf("ERROR! Failed to start the write side of the VDMA.\n\r");
//			return FRAMEBUFFER_ERROR_UNKNOWN;
//		}
//	}
//
//	// Start read side
//	if(p_vdma_inst_read != NULL) {
//		status = XAxiVdma_DmaStart(p_vdma_inst_read, XAXIVDMA_READ);
//		if (status != XST_SUCCESS)
//		{
//			xil_printf("ERROR! Failed to start the read side of the VDMA.\n\r");
//			return FRAMEBUFFER_ERROR_UNKNOWN;
//		}
//	}
//
//	framebuffer_dump_vdma_regs(p_vdma_inst_read);
//
//
//	return FRAMEBUFFER_SUCCESS;
//}

int framebuffer_write
(
	XAxiVdma*    p_vdma_inst,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr,
	unsigned int stride
)
{
	// Local variables
	int status = 0;

	// Setup write channel
	status = set_vdma_write(p_vdma_inst, bits_per_pixel, hsize, vsize, buf_base_addr, stride);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to set up the write side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	return FRAMEBUFFER_SUCCESS;
}

int framebuffer_read
(
	XAxiVdma*    p_vdma_inst,
	unsigned int bits_per_pixel,
	unsigned int hsize,
	unsigned int vsize,
	unsigned int buf_base_addr,
	unsigned int stride
)
{
	// Local variables
	int status = 0;

	// Setup read channel
	status = set_vdma_read(p_vdma_inst, bits_per_pixel, hsize, vsize, buf_base_addr, stride);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to set up the read side of the VDMA.\n\r");
		return FRAMEBUFFER_ERROR_UNKNOWN;
	}

	return FRAMEBUFFER_SUCCESS;
}

void framebuffer_dump_vdma_regs(XAxiVdma* p_vdma_inst)
{
	xil_printf("-----------------------------------------------------\n\r");
	xil_printf("AXI VDMA is at address 0x%08X              \n\r", p_vdma_inst->BaseAddr);
	xil_printf("-----------------------------------------------------\n\r");
	read_vdma_regs(p_vdma_inst);
	xil_printf("-----------------------------------------------------\n\r");

	if ((XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, XAXIVDMA_TX_OFFSET+XAXIVDMA_SR_OFFSET) & XAXIVDMA_IXR_ERROR_MASK) ||
	    (XAxiVdma_ReadReg(p_vdma_inst->BaseAddr, XAXIVDMA_RX_OFFSET+XAXIVDMA_SR_OFFSET) & XAXIVDMA_IXR_ERROR_MASK))
	{
		xil_printf("Clearing VDMA errors...\n\r");
		XAxiVdma_WriteReg(p_vdma_inst->BaseAddr, XAXIVDMA_TX_OFFSET+XAXIVDMA_SR_OFFSET, 0xFFFFFFFF);
		XAxiVdma_WriteReg(p_vdma_inst->BaseAddr, XAXIVDMA_RX_OFFSET+XAXIVDMA_SR_OFFSET, 0xFFFFFFFF);
		read_vdma_regs(p_vdma_inst);
		xil_printf("-----------------------------------------------------\n\r");
	}
}


uint32_t vdma_reset(XAxiVdma *VDMAPtr, uint32_t direction)
{
	uint32_t Polls;

	xil_printf("Resetting VDMA ...\r\n");

	XAxiVdma_Reset(VDMAPtr, direction);
	Polls = 1000000;

	while (Polls && XAxiVdma_ResetNotDone(VDMAPtr, direction)) {
		Polls--;
	}

	if (Polls == 0) {
		xil_printf( "ERROR: VDMA %s channel reset failed %x\n\r", (direction==XAXIVDMA_READ)?"Read":"Write", 0);
		return XST_FAILURE;
	}
	return 0;
}
