
#ifndef _VID_IO_INTF_H_
#define _VID_IO_INTF_H_

// *****************************************************
// Notes
// *****************************************************
//   - The purpose of this driver is to abstract the
//     input/output video interface. The implementation
//     for this example is the IMAGEON FMC card and also
//     the on-board ADV7511

// *****************************************************
// Dependencies
// *****************************************************
//#include "fmc_imageon.h"
#include "video.h"
//#include "si570.h"

// *****************************************************
// Function status return values
// *****************************************************
#define VID_IO_INTF_SUCCESS                   0
#define VID_IO_INTF_ERROR_UNKNOWN            -1
#define VID_IO_INTF_INPUT_NOT_LOCKED         -2
#define VID_IO_INTF_INPUT_INVALID_RESOLUTION -3
#define VID_IO_INTF_NO_FMC_CARD              -4

// *****************************************************
// Object
// *****************************************************
typedef struct vid_io_intf
{
	// Video I/O interface drivers (user should allocate
	// and attach pointers before doing anything else)
	//fmc_imageon_t*  p_fmc_imageon_inst;
	//fmc_iic_t*      p_fmc_imageon_iic_inst;
	//si570_t*        p_si570_inst;
	
	// Input and output frame sizes (allocated locally)
	video_timing_t* p_input_timing_inst;
	video_timing_t* p_output_timing_inst;
	
	// Flag indicating whether or not IMAGEON FMC card
	// is connected
	unsigned int fmc_imageon_is_present;
} vid_io_intf_t;

// *****************************************************
// Public functions
// *****************************************************

// vid_io_intf_init() - Initialize drivers for all peripherals
//                      and set them to a known power-on state.
//                      This function must be called on the
//                      object before any other driver functions
//                      can be called. This function also querys
//                      the hardware to see if the IMAGEON FMC
//                      card is present and sets the
//                      fmc_imageon_is_present member variable
//                      appropriately.
//   - p_vid_io_intf_inst         - Pointer to object to work on
//   - fmc_imageon_iic_base_addr  - Base address for I2C device that controls the IMAGEON FMC card
//   - si570_iic_device_id        - Device ID for the I2C device that controls the SI570 clock generator
//   - return                     - Function status return value (see above)
int vid_io_intf_init
(
	vid_io_intf_t* p_vid_io_camera_inst,
	vid_io_intf_t* p_vid_io_camera_freeze_inst,
	vid_io_intf_t* p_vid_io_GUI_inst
	//unsigned int   fmc_imageon_iic_base_addr,
	//unsigned int   si570_iic_device_id
);

// vid_io_intf_get_fmc_status() - Check if the IMAGEON FMC card was detected by
//                                querying the state of the fmc_imageon_is_present
//                                member variable.
//   - p_vid_io_intf_inst        - Pointer to object to work on
//   - return                    - 1 if FMC card is present, 0 if not.

int vid_io_intf_get_fmc_status
(
	vid_io_intf_t* p_vid_io_intf_inst
);

// vid_io_intf_detect_input_fsize() - Detect the input frame size from the IMAGEON FMC
//                                    card (if connected). If the FMC card is detected,
//                                    this function blocks until lock is achieved (or
//                                    times out).
//   - p_vid_io_intf_inst - Pointer to object to work on
//   - return             - Function status return value (see above)
int vid_io_intf_detect_input_fsize
(
	vid_io_intf_t* p_vid_io_intf_inst
);

// vid_io_intf_update_output_fsize() - Change the output frame size
//   - p_vid_io_intf_inst - Pointer to object to work on
//   - new_output_timing  - New output timing option to use from video_resolution.h
//   - return             - Function status return value (see above)
int vid_io_intf_update_output_fsize
(
	vid_io_intf_t* p_vid_io_intf_inst,
	unsigned int   new_output_timing
);


#endif // _VID_IO_INTF_H_

