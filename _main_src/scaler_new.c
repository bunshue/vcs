
// *****************************************************
// Dependencies
// *****************************************************
#include "scaler_new.h"

// *****************************************************
// Private functions
// *****************************************************

// scaler_new_set_stream() - Configure VPSS stream parameters. Taken from 
//                           VPSS driver example software.
//   - p_vpss_inst   - Pointer to object to work on
//   - direction     - When 0, configure input stream. Otherwise, configure output stream
//   - width         - Horizontal active size to use
//   - height        - Vertical active size to use
//   - color_format  - Color format to use
//   - is_interlaced - When 0, configure for progressive. When 1, configure for interlaced
//   - return        - None
void scaler_new_set_stream
(
	XVprocSs*         p_vpss_inst,
	unsigned short    direction,
	unsigned short    width,
	unsigned short    height,
	XVidC_ColorFormat color_format,
	XVidC_FrameRate	  frame_rate,
	unsigned short    is_interlaced
)
{
	// Local variables
	XVidC_VideoMode resId;
	XVidC_VideoStream Stream;

	// Get resolution ID from frame size
	resId = XVidC_GetVideoModeId(width, height, frame_rate, FALSE);

	// Setup Video Processing Subsystem
	Stream.VmId           = resId;
	Stream.Timing.HActive = width;
	Stream.Timing.VActive = height;
	Stream.ColorFormatId  = color_format;
	Stream.ColorDepth     = p_vpss_inst->Config.ColorDepth;
	Stream.PixPerClk      = p_vpss_inst->Config.PixPerClock;
	Stream.FrameRate      = frame_rate;
	Stream.IsInterlaced   = is_interlaced;

	if(direction == 0)
	{
		XVprocSs_SetVidStreamIn(p_vpss_inst, &Stream);
	}
	else
	{
		XVprocSs_SetVidStreamOut(p_vpss_inst, &Stream);
	}
}

// *****************************************************
// Public functions
// *****************************************************
unsigned int scaler_new_set_size
(
	XVprocSs*    p_scaler_new_inst,
	unsigned int in_hsize,
	unsigned int in_vsize,
	unsigned int in_color_format,
	unsigned int out_hsize,
	unsigned int out_vsize,
	unsigned int out_color_format,
	unsigned int print_config
)
{
	// Local variables
	int        status        = 0;
//	static int is_first_time = 1;
	
	// The VPSS needs a valid config for both input and output the first time
	// XVprocSs_SetSubsystemConfig() is called, otherwise error
//	if (is_first_time)
	{
		scaler_new_set_stream
		(
			p_scaler_new_inst,
			1, // Output stream
			out_hsize,
			out_vsize,
			out_color_format,
			//XVIDC_CSF_YCRCB_422,
			//XVIDC_CSF_RGB,
			XVIDC_FR_60HZ,
			0 // Interlaced
		);
//		is_first_time = 0;
	}
	
	scaler_new_set_stream
	(
		p_scaler_new_inst,
		0, // Input stream
		in_hsize,
		in_vsize,
		in_color_format,
		//XVIDC_CSF_YCRCB_422,
		//XVIDC_CSF_RGB,
		XVIDC_FR_60HZ,
		0 // Interlaced
	);
	
	status = XVprocSs_SetSubsystemConfig(p_scaler_new_inst);
	if (status != 0)
	{
		xil_printf("ERROR! Failed to set VPSS-based scaler.\n\r");
		return SCALER_NEW_ERROR_UNKNOWN;
	}
	
	if (print_config)
	{
		XVprocSs_ReportSubsystemConfig(p_scaler_new_inst);
	}
	
	return SCALER_NEW_SUCCESS;
}

unsigned int scaler_new_set_input_color_format
(
	XVprocSs*    p_scaler_new_inst,
	unsigned int color_format,
	unsigned int print_config
)
{
	// Local variables
	int        status        = 0;
	uint32_t   value;

//	XVprocSs_SetPictureBrightness(p_scaler_new_inst, 50);
//	XVprocSs_SetPictureContrast(p_scaler_new_inst, 50);
//	XVprocSs_SetPictureSaturation(p_scaler_new_inst, 50);
//	//XVprocSs_SetPictureGain(XVprocSs *Instance, XVprocSs_ColorChannel ChId, s32 NewValue);
	XVprocSs_SetPictureColorStdIn(p_scaler_new_inst, XVIDC_BT_709);
	XVprocSs_SetPictureColorStdOut(p_scaler_new_inst, XVIDC_BT_709);
	XVprocSs_SetPictureColorRange(p_scaler_new_inst, XVIDC_CR_0_255);



	value = XVprocSs_GetPictureBrightness(p_scaler_new_inst);
	xil_printf("Brightness: %d\r\n", value);
	value = XVprocSs_GetPictureContrast(p_scaler_new_inst);
	xil_printf("Contrast: %d\r\n", value);
	value = XVprocSs_GetPictureSaturation(p_scaler_new_inst);
	xil_printf("Saturation: %d\r\n", value);
	value = XVprocSs_GetPictureGain(p_scaler_new_inst, XVPROCSS_COLOR_CH_Y_RED);
	xil_printf("Red/Y Gain: %d\r\n", value);
	value = XVprocSs_GetPictureGain(p_scaler_new_inst, XVPROCSS_COLOR_CH_CB_GREEN);
	xil_printf("Green/Cb Gain: %d\r\n", value);
	value = XVprocSs_GetPictureGain(p_scaler_new_inst, XVPROCSS_COLOR_CH_CR_BLUE);
	xil_printf("Blue/Cr Gain: %d\r\n", value);
	value = XVprocSs_GetPictureColorStdIn(p_scaler_new_inst);
	xil_printf("Input Color: %d\r\n", value);
	value = XVprocSs_GetPictureColorStdOut(p_scaler_new_inst);
	xil_printf("Output Color: %d\r\n", value);
	value = XVprocSs_GetPictureColorRange(p_scaler_new_inst);
	xil_printf("Color Range: %d\r\n", value);

	status = XVprocSs_SetSubsystemConfig(p_scaler_new_inst);
	if (status != 0)
	{
		xil_printf("ERROR! Failed to set VPSS-based scaler.\n\r");
		return SCALER_NEW_ERROR_UNKNOWN;
	}

	if (print_config)
	{
		XVprocSs_ReportSubsystemConfig(p_scaler_new_inst);
	}

	return SCALER_NEW_SUCCESS;
}

//unsigned int scaler_new_set_output_size
//(
//	XVprocSs*    p_scaler_new_inst,
//	unsigned int hsize,
//	unsigned int vsize,
//	unsigned int print_config
//)
//{
//	// Local variables
//	int        status        = 0;
//	static int is_first_time = 1;
//
//	// The VPSS needs a valid config for both input and output the first time
//	// XVprocSs_SetSubsystemConfig() is called, otherwise error
//	if (is_first_time)
//	{
//		scaler_new_set_stream
//		(
//			p_scaler_new_inst,
//			0, // Input stream
//			640,
//			480,
//			//hsize,
//			//vsize,
//			XVIDC_CSF_YCRCB_422,
//			//XVIDC_CSF_YCRCB_444,
//			//XVIDC_CSF_RGB,
//			XVIDC_FR_60HZ,
//			0 // Interlaced
//		);
//		is_first_time = 0;
//	}
//
//	scaler_new_set_stream
//	(
//		p_scaler_new_inst,
//		1,
//		hsize,
//		vsize,
//		XVIDC_CSF_YCRCB_422,
//		//XVIDC_CSF_RGB,
//		XVIDC_FR_60HZ,
//		0
//	);
//
//	status = XVprocSs_SetSubsystemConfig(p_scaler_new_inst);
//	if (status != 0)
//	{
//		xil_printf("ERROR! Failed to set VPSS-based scaler.\n\r");
//		return SCALER_NEW_ERROR_UNKNOWN;
//	}
//
//	if (print_config)
//	{
//		XVprocSs_ReportSubsystemConfig(p_scaler_new_inst);
//	}
//
//	return SCALER_NEW_SUCCESS;
//}

