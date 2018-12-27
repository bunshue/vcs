
// *****************************************************
// Dependencies
// *****************************************************
#include "vid_io_intf.h"
#include "video_resolution.h"
#include "zc702_i2c_utils.h"
#include "main.h"

// *****************************************************
// Constants
// *****************************************************
#define FMC_IMAGEON_INPUT_TIMING_DET_TIMEOUT 100

// *****************************************************
// Globals
// *****************************************************
static const uint8_t fmc_imageon_hdmii_edid_content[256] =
{
		0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00,
		0x06, 0xD4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
		0x00, 0x16, 0x01, 0x03, 0x81, 0x46, 0x27, 0x78,
		0x0A, 0x32, 0x30, 0xA1, 0x54, 0x52, 0x9E, 0x26,
		0x0A, 0x49, 0x4B, 0xA3, 0x08, 0x00, 0x81, 0xC0,
		0x81, 0x00, 0x81, 0x0F, 0x81, 0x40, 0x81, 0x80,
		0x95, 0x00, 0xB3, 0x00, 0x01, 0x01, 0x02, 0x3A,
		0x80, 0x18, 0x71, 0x38, 0x2D, 0x40, 0x58, 0x2C,
		0x45, 0x00, 0xC4, 0x8E, 0x21, 0x00, 0x00, 0x1E,
		0xA9, 0x1A, 0x00, 0xA0, 0x50, 0x00, 0x16, 0x30,
		0x30, 0x20, 0x37, 0x00, 0xC4, 0x8E, 0x21, 0x00,
		0x00, 0x1A, 0x00, 0x00, 0x00, 0xFC, 0x00, 0x46,
		0x4D, 0x43, 0x2D, 0x49, 0x4D, 0x41, 0x47, 0x45,
		0x4F, 0x4E, 0x0A, 0x20, 0x00, 0x00, 0x00, 0xFD,
		0x00, 0x38, 0x4B, 0x20, 0x44, 0x11, 0x00, 0x0A,
		0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x01, 0x54,
		0x02, 0x03, 0x1F, 0x71, 0x4B, 0x90, 0x03, 0x04,
		0x05, 0x12, 0x13, 0x14, 0x1F, 0x20, 0x07, 0x16,
		0x26, 0x15, 0x07, 0x50, 0x09, 0x07, 0x01, 0x67,
		0x03, 0x0C, 0x00, 0x10, 0x00, 0x00, 0x1E, 0x01,
		0x1D, 0x00, 0x72, 0x51, 0xD0, 0x1E, 0x20, 0x6E,
		0x28, 0x55, 0x00, 0xC4, 0x8E, 0x21, 0x00, 0x00,
		0x1E, 0x01, 0x1D, 0x80, 0x18, 0x71, 0x1C, 0x16,
		0x20, 0x58, 0x2C, 0x25, 0x00, 0xC4, 0x8E, 0x21,
		0x00, 0x00, 0x9E, 0x8C, 0x0A, 0xD0, 0x8A, 0x20,
		0xE0, 0x2D, 0x10, 0x10, 0x3E, 0x96, 0x00, 0xC4,
		0x8E, 0x21, 0x00, 0x00, 0x18, 0x01, 0x1D, 0x80,
		0x3E, 0x73, 0x38, 0x2D, 0x40, 0x7E, 0x2C, 0x45,
		0x80, 0xC4, 0x8E, 0x21, 0x00, 0x00, 0x1E, 0x1A,
		0x36, 0x80, 0xA0, 0x70, 0x38, 0x1F, 0x40, 0x30,
		0x20, 0x25, 0x00, 0xC4, 0x8E, 0x21, 0x00, 0x00,
		0x1A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01
};

// *****************************************************
// Private data
// *****************************************************

// Subcore instantiations
//static fmc_imageon_t              fmc_imageon_inst;
//static fmc_iic_t                  fmc_imageon_iic_inst;
//static si570_t                    si570_inst;
static video_timing_t camera_input_timing_inst;
static video_timing_t camera_output_timing_inst;
static video_timing_t camera_freeze_input_timing_inst;
static video_timing_t camera_freeze_output_timing_inst;
static video_timing_t GUI_input_timing_inst;
static video_timing_t GUI_output_timing_inst;

// *****************************************************
// Private functions
// *****************************************************


//#include "xiic.h"
// fmc_iic_write_w_timeout() - Perform a I2C register write. Time out
//                             if the bus hangs.
//   - fmc_imageon_iic_base_addr - Base address for I2C device that controls the IMAGEON FMC card
//   - chip_addr                 - Chip address of the device to access
//   - reg_addr                  - Register address to write
//   - reg_data                  - Register data to write
//   - return                    - 0 if success. -1 if bus timeout
//int fmc_iic_write_w_timeout
//(
//	unsigned int   fmc_imageon_iic_base_addr,
//	unsigned char  chip_addr,
//	unsigned char  reg_addr,
//	unsigned char  reg_data
//)
//{
//	// Local variables
//	unsigned char wr_buf[2];
//	unsigned char sr             = 0;
//	unsigned char num_bytes_sent = 0;
//	int           timeout        = 10000;
//
//	// Make sure all the Fifo's are cleared and Bus is Not busy
//	do
//	{
//		sr = Xil_In8(fmc_imageon_iic_base_addr + XIIC_SR_REG_OFFSET);
//		sr = sr & (XIIC_SR_RX_FIFO_EMPTY_MASK | XIIC_SR_TX_FIFO_EMPTY_MASK | XIIC_SR_BUS_BUSY_MASK);
//	} while (sr != (XIIC_SR_RX_FIFO_EMPTY_MASK | XIIC_SR_TX_FIFO_EMPTY_MASK) && timeout-- > 0);
//	if (timeout < 0)
//	{
//		return -1;
//	}
//
//	wr_buf[0] = reg_addr;
//	wr_buf[1] = reg_data;
//	num_bytes_sent = XIic_DynSend(fmc_imageon_iic_base_addr, chip_addr, wr_buf, 2, XIIC_STOP);
//	if (num_bytes_sent < 1)
//	{
//		num_bytes_sent = 1;
//	}
//
//	return num_bytes_sent - 1; // Return the number of bytes written.
//}

// detect_fmc_imageon() - Query the hardware to see if the FMC IMAGEON card
//                        is connected to the board. This happens by doing a
//                        dummy I2C access and determining whether or not it
//                        times out.
//   - fmc_imageon_iic_base_addr - Base address for I2C device that controls the IMAGEON FMC card
//   - return                    - 1 if FMC card was detected, 0 if not
static unsigned int detect_fmc_imageon
(
	unsigned int fmc_imageon_iic_base_addr
)
{
	// Local variables
	unsigned int ret = 0;

	// Set up I2C mux first
	//ret = fmc_iic_write_w_timeout(fmc_imageon_iic_base_addr, FMC_IMAGEON_I2C_MUX_ADDR, 0x08, 0x08);

	// Perform a dummy write to ADV7511 (this is used by figuring out the first write that the fmc imageon driver does via I2C)
	//ret = fmc_iic_write_w_timeout(fmc_imageon_iic_base_addr, 0x20, 0x03, 0xEA);

	//
	if (ret == -1)
	{
		xil_printf("FMC IMAGEON not detected.\n\r");
		return 0;
	}
	else
	{
		xil_printf("FMC IMAGEON detected.\n\r");
		return 1;
	}
}

// *****************************************************
// Public functions
// *****************************************************
int vid_io_intf_init
(
	vid_io_intf_t* p_vid_io_camera_inst,
	vid_io_intf_t* p_vid_io_camera_freeze_inst,
	vid_io_intf_t* p_vid_io_GUI_inst
//	unsigned int   fmc_imageon_iic_base_addr,
//	unsigned int   si570_iic_device_id
)
{
	// Local variables
	int status                    = 0;
	int detected_input_resolution = 0;
	int tries                     = 0;
	
	// Attach subcore instances to object
	//p_vid_io_intf_inst->p_fmc_imageon_inst     = &fmc_imageon_inst;
	//p_vid_io_intf_inst->p_fmc_imageon_iic_inst = &fmc_imageon_iic_inst;
	//p_vid_io_intf_inst->p_si570_inst           = &si570_inst;
	p_vid_io_camera_inst->p_input_timing_inst    = &camera_input_timing_inst;
	p_vid_io_camera_inst->p_output_timing_inst   = &camera_output_timing_inst;
	p_vid_io_camera_freeze_inst->p_input_timing_inst    = &camera_freeze_input_timing_inst;
	p_vid_io_camera_freeze_inst->p_output_timing_inst   = &camera_freeze_output_timing_inst;
	p_vid_io_GUI_inst->p_input_timing_inst    = &GUI_input_timing_inst;
	p_vid_io_GUI_inst->p_output_timing_inst   = &GUI_output_timing_inst;
	
	// Initialize object data
	p_vid_io_camera_inst->fmc_imageon_is_present = 0;
	p_vid_io_camera_freeze_inst->fmc_imageon_is_present = 0;
	p_vid_io_GUI_inst->fmc_imageon_is_present = 0;

	p_vid_io_camera_inst->p_input_timing_inst->HActiveVideo  = CAMERA_X; // This needs to be non-zero by upper layer drivers
	p_vid_io_camera_inst->p_input_timing_inst->VActiveVideo  = CAMERA_Y;  // This needs to be non-zero by upper layer drivers
	p_vid_io_camera_inst->p_output_timing_inst->HActiveVideo = LAYER2_WIDTH; // This needs to be non-zero by upper layer drivers
	p_vid_io_camera_inst->p_output_timing_inst->VActiveVideo = LAYER2_HEIGHT;  // This needs to be non-zero by upper layer drivers

	p_vid_io_camera_freeze_inst->p_input_timing_inst->HActiveVideo  = CAMERA_X; // This needs to be non-zero by upper layer drivers
	p_vid_io_camera_freeze_inst->p_input_timing_inst->VActiveVideo  = CAMERA_Y;  // This needs to be non-zero by upper layer drivers
	p_vid_io_camera_freeze_inst->p_output_timing_inst->HActiveVideo = LAYER1_WIDTH; // This needs to be non-zero by upper layer drivers
	p_vid_io_camera_freeze_inst->p_output_timing_inst->VActiveVideo = LAYER1_HEIGHT;  // This needs to be non-zero by upper layer drivers

	p_vid_io_GUI_inst->p_input_timing_inst->HActiveVideo  = LAYER3_WIDTH; // This needs to be non-zero by upper layer drivers
	p_vid_io_GUI_inst->p_input_timing_inst->VActiveVideo  = LAYER3_HEIGHT;  // This needs to be non-zero by upper layer drivers
	p_vid_io_GUI_inst->p_output_timing_inst->HActiveVideo = LAYER3_WIDTH; // This needs to be non-zero by upper layer drivers
	p_vid_io_GUI_inst->p_output_timing_inst->VActiveVideo = LAYER3_HEIGHT;  // This needs to be non-zero by upper layer drivers
	
	// SI570 oscillator initialization
	//si570_init(p_vid_io_intf_inst->p_si570_inst, si570_iic_device_id);
	
//	// Initialize I2C for FMC IMAGEON (need to do this first because VTC driver hangs if no input clock)
//	xil_printf("Initializing IIC for FMC IMAGEON.\n\r");
//	status = fmc_iic_xps_init(p_vid_io_intf_inst->p_fmc_imageon_iic_inst,"FMC-IMAGEON I2C Controller", fmc_imageon_iic_base_addr);
//	if (!status)
//	{
//	  xil_printf("ERROR! Failed to open IIC driver for the FMC IMAGEON card.\n\r" );
//	  return VID_IO_INTF_ERROR_UNKNOWN;
//	}
	
	// Initialize FMC IMAGEON if it is connected
	xil_printf("Checking for FMC IMAGEON card.\n\r");
	//p_vid_io_intf_inst->fmc_imageon_is_present = detect_fmc_imageon(fmc_imageon_iic_base_addr);
	//p_vid_io_intf_inst->fmc_imageon_is_present = 1;
	if (vid_io_intf_get_fmc_status(p_vid_io_camera_inst))
	{
		xil_printf("Initializing FMC IMAGEON.\n\r");
//		fmc_imageon_init(p_vid_io_intf_inst->p_fmc_imageon_inst, "FMC-IMAGEON", p_vid_io_intf_inst->p_fmc_imageon_iic_inst); // Do we need this?
//		p_vid_io_intf_inst->p_fmc_imageon_inst->bVerbose = 0;
//
//		// Initialize IMAGEON FMC card input
////		xil_printf("HDMI input initialization.\n\r");
////		status = fmc_imageon_hdmii_init2
////		(
////				p_vid_io_intf_inst->p_fmc_imageon_inst,
////				1, // hdmiiEnable = 1
////				1, // editInit = 1
////				fmc_imageon_hdmii_edid_content,
////				0,
////				0
////		);
////		if (!status)
////		{
////			xil_printf("ERROR! Failed to initialize HDMI Input Interface.\n\r");
////			return VID_IO_INTF_ERROR_UNKNOWN;
////		}
//
		// Detect incoming video (need to do this here because VTC init hangs if there's no input clock)
		xil_printf("Detecting HDMI input resolution.\n\r");
		detected_input_resolution = vid_io_intf_detect_input_fsize(p_vid_io_camera_inst);
		while ((detected_input_resolution < 0)&&(tries < 3))
		{
			xil_printf("ERROR! ADV7611 detect error. Trying again\n\r");
			detected_input_resolution = vid_io_intf_detect_input_fsize(p_vid_io_camera_inst);
			tries++;
		}
		if (detected_input_resolution < 0)
		{
			xil_printf("ERROR! Failed to detect input resolution. Aborting.\n\r");
			return VID_IO_INTF_INPUT_INVALID_RESOLUTION;
		}
//
//		// Initialize clock synthesizer
//		//fmc_imageon_vclk_init(p_vid_io_intf_inst->p_fmc_imageon_inst);
	}
	
	//si570_set_freq(p_vid_io_intf_inst->p_si570_inst, SI570_FREQ_74_250_000);
	
	// Set up On-board (ZC702) HDMI
	//zc702_hdmi_init(p_vid_io_intf_inst->p_si570_inst->p_si570_iic_inst);

	return VID_IO_INTF_SUCCESS;
}

int vid_io_intf_get_fmc_status
(
	vid_io_intf_t* p_vid_io_intf_inst
)
{
	return p_vid_io_intf_inst->fmc_imageon_is_present;
}

int vid_io_intf_detect_input_fsize
(
	vid_io_intf_t* p_vid_io_intf_inst
)
{
	// Local variables
	unsigned int hdmii_locked     = 0;
	unsigned int timeout          = FMC_IMAGEON_INPUT_TIMING_DET_TIMEOUT;
	int          hdmii_resolution = -1;
	
	if (!vid_io_intf_get_fmc_status(p_vid_io_intf_inst))
	{
		xil_printf("FMC Card is not present. Cannot detect an incoming image.\n\r");
		return VID_IO_INTF_NO_FMC_CARD;
	}

//	xil_printf("Waiting for ADV7611 to locked on incoming video...\n\r");
//	while (!hdmii_locked && timeout--)
//	{
//		usleep(100000); // wait 100msec ...
//		hdmii_locked = fmc_imageon_hdmii_get_lock(p_vid_io_intf_inst->p_fmc_imageon_inst);
//	}
	if (!hdmii_locked)
	{
		return VID_IO_INTF_INPUT_NOT_LOCKED;
	}
	usleep(100000); // wait 100msec for timing to stabilize
	xil_printf("ADV7611 is locked!\n\r");
	
	// Get Video Input information
//	fmc_imageon_hdmii_get_timing(p_vid_io_intf_inst->p_fmc_imageon_inst, p_vid_io_intf_inst->p_input_timing_inst);
//	hdmii_resolution = vres_detect(p_vid_io_intf_inst->p_input_timing_inst->HActiveVideo, p_vid_io_intf_inst->p_input_timing_inst->VActiveVideo);
//
//	xil_printf("ADV7611 Video Input Information\n\r");
//	xil_printf("Video Input      = %s", p_vid_io_intf_inst->p_input_timing_inst->IsHDMI       ? "HDMI"             : "DVI");
//	xil_printf("%s",                    p_vid_io_intf_inst->p_input_timing_inst->IsEncrypted  ? ", HDCP Encrypted" : "");
//	xil_printf(", %s\n\r",              p_vid_io_intf_inst->p_input_timing_inst->IsInterlaced ? "Interlaced"       : "Progressive");
//	xil_printf("Color Depth      = %d bits per channel\n\r", p_vid_io_intf_inst->p_input_timing_inst->ColorDepth);
//	xil_printf("HSYNC Timing     = hav=%04d, hfp=%02d, hsw=%02d(hsp=%d), hbp=%03d\n\r",
//		p_vid_io_intf_inst->p_input_timing_inst->HActiveVideo,
//		p_vid_io_intf_inst->p_input_timing_inst->HFrontPorch,
//		p_vid_io_intf_inst->p_input_timing_inst->HSyncWidth, p_vid_io_intf_inst->p_input_timing_inst->HSyncPolarity,
//		p_vid_io_intf_inst->p_input_timing_inst->HBackPorch
//	);
//	xil_printf("VSYNC Timing     = vav=%04d, vfp=%02d, vsw=%02d(vsp=%d), vbp=%03d\n\r",
//		p_vid_io_intf_inst->p_input_timing_inst->VActiveVideo,
//		p_vid_io_intf_inst->p_input_timing_inst->VFrontPorch,
//		p_vid_io_intf_inst->p_input_timing_inst->VSyncWidth, p_vid_io_intf_inst->p_input_timing_inst->VSyncPolarity,
//		p_vid_io_intf_inst->p_input_timing_inst->VBackPorch
//	);
//	xil_printf("Video Dimensions = %d x %d\n\r", p_vid_io_intf_inst->p_input_timing_inst->HActiveVideo, p_vid_io_intf_inst->p_input_timing_inst->VActiveVideo);
//
//	if (hdmii_resolution == -1)
//	{
//		xil_printf("ERROR! Invalid resolution.\n\r");
//		return VID_IO_INTF_INPUT_INVALID_RESOLUTION;
//	}
	
	return VID_IO_INTF_SUCCESS;
}

int vid_io_intf_update_output_fsize
(
	vid_io_intf_t* p_vid_io_intf_inst,
	unsigned int new_output_timing
)
{
	// Local variables
	int                        status     = 0;
	int                        vid_clk_id = 0;
	vres_timing_t              vres_timing;
	
	// Lookup timing parameters
	vres_get_timing(new_output_timing, &vres_timing);
	
	// Copy timing over to FMC card struct
	p_vid_io_intf_inst->p_output_timing_inst->IsHDMI        = 0;
	p_vid_io_intf_inst->p_output_timing_inst->IsEncrypted   = 0;
	p_vid_io_intf_inst->p_output_timing_inst->IsInterlaced  = 0;
	p_vid_io_intf_inst->p_output_timing_inst->ColorDepth    = 8;
	p_vid_io_intf_inst->p_output_timing_inst->HActiveVideo  = vres_timing.HActiveVideo;
	p_vid_io_intf_inst->p_output_timing_inst->HFrontPorch   = vres_timing.HFrontPorch;
	p_vid_io_intf_inst->p_output_timing_inst->HSyncWidth    = vres_timing.HSyncWidth;
	p_vid_io_intf_inst->p_output_timing_inst->HBackPorch    = vres_timing.HBackPorch;
	p_vid_io_intf_inst->p_output_timing_inst->HSyncPolarity = vres_timing.HSyncPolarity;
	p_vid_io_intf_inst->p_output_timing_inst->VActiveVideo  = vres_timing.VActiveVideo;
	p_vid_io_intf_inst->p_output_timing_inst->VFrontPorch   = vres_timing.VFrontPorch;
	p_vid_io_intf_inst->p_output_timing_inst->VSyncWidth    = vres_timing.VSyncWidth;
	p_vid_io_intf_inst->p_output_timing_inst->VBackPorch    = vres_timing.VBackPorch;
	p_vid_io_intf_inst->p_output_timing_inst->VSyncPolarity = vres_timing.VSyncPolarity;
	
	// Set FMC IMAGEON output timing
//	if (vid_io_intf_get_fmc_status(p_vid_io_intf_inst))
//	{
//		xil_printf("Setting ADV7511 output video to %s\n\r", vres_get_name(new_output_timing));
//		status = fmc_imageon_hdmio_init
//		(
//			p_vid_io_intf_inst->p_fmc_imageon_inst, // FMC IMAGEON instance
//			1,                                      // HDMI Output enable
//			p_vid_io_intf_inst->p_output_timing_inst,    // Video timing information
//			0                                       // No wait for Hot Plug Detect (HPD)
//		);
//		if (!status)
//		{
//		  xil_printf("ERROR! Failed to set HDMI Output Interface.\n\r");
//		  return VID_IO_INTF_ERROR_UNKNOWN;
//		}
//	}
	
//	// Set FMC IMAGEON clock synthesizer
//	switch (new_output_timing)
//	{
//		case 0:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_25_175_000;  break; // VGA
//		case 1:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_27_000_000;  break; // 480p
//		case 2:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_27_000_000;  break; // 576p
//		case 3:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_40_000_000;  break; // SVGA
//		case 4:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_65_000_000;  break; // XGA
//		case 5:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_74_250_000;  break; // 720p
//		case 6:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_110_000_000; break; // SXGA
//		case 7:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_148_500_000; break; // 1080p
//		case 8:  vid_clk_id = FMC_IMAGEON_VCLK_FREQ_162_000_000; break; // UXGA
//		default: vid_clk_id = FMC_IMAGEON_VCLK_FREQ_74_250_000;  break;
//	}
//
//	if (vid_io_intf_get_fmc_status(p_vid_io_intf_inst))
//	{
//		fmc_imageon_vclk_config(p_vid_io_intf_inst->p_fmc_imageon_inst, vid_clk_id);
//	}
//	si570_set_freq(p_vid_io_intf_inst->p_si570_inst, vid_clk_id);
	
	return VID_IO_INTF_SUCCESS;
}

