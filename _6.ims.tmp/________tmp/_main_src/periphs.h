
#ifndef _PERIPHS_H_
#define _PERIPHS_H_

// *****************************************************
// Notes
// *****************************************************
// - The purpose of this software layer is to
//   encapsulate all the peripherals in this system and
//   provide functions needed for the application to:
//     - Detect or set input video frame size
//     - Set output video frame size
//     - Switch between the old scaler datapath and the
//       VPSS-based scaler datapath
//     - Switch between live input video from the IMAGEON
//       FMC card and internal TPG
// - The new and old scaler TPGs are differentiated via
//   the color of the bouncing box. It is blue for the
//   old scaler and red for the new VPSS-based scaler
// - The design has two parallel data paths that are 
//   muxed together on the ouput. The paths are
//   differentiated in the software with the following
//   naming conventions:
//     - *_old_* - Indicates IPs used in the same data
//                 path with the old Scaler v8.1.
//     - *_new_* - Indicates IPs used in the same data
//                 path with the new VPSS-based Scaler.
//   Note that the only IP version that is different
//   between the two data paths is the Scaler/VPSS. For
//   example, AXI VDMA v6.2 is used in both data paths.
//   p_vdma_old_inst only indicates that this instance
//   of the IP is used in the same data path with the
//   old scaler (not that this is some other old version
//   of the VDMA)

// *****************************************************
// Dependencies
// *****************************************************
#include "framebuffer.h"
#include "gpio.h"
#include "vid_io_intf.h"
#include "test_pattern_gen.h"
#include "scaler_new.h"
#include "vtiming_det.h"
#include "vtiming_gen.h"
#include "mixer.h"
#include "video_resolution.h"
#include "xscutimer.h"
//#include "main.h"
#include "psuart0.h"
#include "psusb0.h"


// *****************************************************
// Function status return values
// *****************************************************
#define PERIPHS_SUCCESS            0
#define PERIPHS_ERROR_UNKNOWN     -1
#define PERIPHS_ERROR_NO_FMC_CARD -2



// *****************************************************
// Enumerations
// *****************************************************
typedef enum
{
	PERIPHS_SEL_OLD_SCALER = 0,
	PERIPHS_SEL_NEW_SCALER = 1
} scaler_option_t;

typedef enum
{
	PERIPHS_SEL_ENABLE_TPG = 0,
	PERIPHS_SEL_BYPASS_TPG = 1
} tpg_option_t;

typedef enum
{
	PERIPHS_SEL_DISABLE_PARK = 0,
	PERIPHS_SEL_ENABLE_PARK = 1
} park_option_t;


static XUartPs_Config *g_psuart1_config;

uint32_t g_procedure_started;

// *****************************************************
// Object
// *****************************************************
typedef struct periphs
{
	// Datapath peripheral drivers (user should allocate and attach pointers before doing anything else)
	//XGpio*          p_vid_mux_sel_gpio_inst;
	XGpioPs*		p_ps_gpio_inst;
	XGpio* 		    p_lock_monitor_inst;
	XScuGic*		p_scugic_inst;
	XScuTimer*		p_scutimer_inst;
	XUartPs*		p_psuart0_inst;
	vid_io_intf_t*  p_vid_io_camera_inst;
	vid_io_intf_t*  p_vid_io_camera_freeze_inst;
	vid_io_intf_t*  p_vid_io_GUI_inst;
	//XVtc*           p_vtd_inst;
	//XV_tpg*         p_tpg_old_inst;
	XV_tpg*         p_tpg_GUI_inst;
	XVprocSs*       p_scaler_camera_inst;
	XVprocSs*       p_scaler_camera_freeze_inst;
	XAxiVdma*       p_vdma_camera_inst;
	XAxiVdma*       p_vdma_camera_freeze_inst;
	XAxiVdma*       p_vdma_GUI_inst;
	XV_Mix_l2*		p_vid_output_mixer_l2_inst;
	XVtc*           p_vtg_inst_0;
	XVtc*           p_vtg_inst_1;
	XUsbPs*			p_psusb0_inst;
	
	// Frame buffer addresses
	unsigned int    fb_camera_start_addr;
	unsigned int    fb_camera_freeze_start_addr;
	unsigned int    fb_GUI_start_addr;
	// Current scaler to use
	scaler_option_t which_scaler;
	
	// Whether or not to bypass the TPG
	tpg_option_t    bypass_GUI_tpg;

	park_option_t	enable_camera_freeze_vdma;

} periphs_t;

// *****************************************************
// Public functions
// *****************************************************

// periphs_init() - Initialize drivers for all peripherals
//   - p_periphs_inst             - Pointer to Peripheral object
//   - vid_mux_sel_gpio_device_id - Device ID for GPIO controlling the output video mux
//   - fmc_imageon_iic_base_addr  - Base address for IIC device that controls the IMAGEON FMC card
//   - vtd_device_id              - Device ID for Video Timing Detector
//   - tpg_old_device_id          - Device ID for Test Pattern Generator that drives the old Scaler
//   - tpg_new_device_id          - Device ID for Test Pattern Generator that drives the new VPSS-based Scaler
//   - scaler_old_device_id       - Device ID for Scaler v8.1 instance
//   - scaler_new_device_id       - Device ID for VPSS v1.0 Scaler instance
//   - vdma_old_device_id         - Device ID for VDMA for old scaler datapath
//   - vdma_new_device_id         - Device ID for VDMA for new scaler datapath
//   - vtg_device_id #0           - Device ID for Video Timing Generator
//   - vtg_device_id #1           - Device ID for Video Timing Generator
//   - fb_old_start_addr          - Frame buffer start address for old scaler datapath
//   - fb_new_start_addr          - Frame buffer start address for new scaler datapath
//   - return                     - Function status return value (see above)
int periphs_init
(
	periphs_t*   p_periphs_inst,
	unsigned int ps_gpio_device_id,
	unsigned int video_lock_device_id,
	unsigned int scugic_device_id,
	unsigned int scutimer_device_id,
	unsigned int psuart0_device_id,
	//unsigned int vid_mux_sel_gpio_device_id,
	//unsigned int fmc_imageon_iic_base_addr,
	//unsigned int si570_iic_device_id,
	//unsigned int vtd_device_id,
	//unsigned int tpg_old_device_id,
	unsigned int tpg_GUI_device_id,
	//unsigned int scaler_camera_device_id,
	unsigned int scaler_camera_freeze_device_id,
	unsigned int vdma_camera_device_id,
	unsigned int vdma_camera_freeze_device_id,
	//unsigned int vdma_GUI_device_id,
	unsigned int vid_output_mixer,
	unsigned int vtg_device_id_0,
	unsigned int vtg_device_id_1,
	unsigned int psusb0_device_id,
	unsigned int fb_camera_start_addr,
	unsigned int fb_camera_freeze_start_addr,
	unsigned int fb_GUI_start_addr
);

// periphs_get_fmc_status() - Check if the IMAGEON FMC card was detected by
//                            querying the vid_io_intf driver.
//   - p_periphs_inst - Pointer to object to work on
//   - return         - 1 if FMC card is present, 0 if not.
int periphs_get_fmc_status
(
	periphs_t* p_periphs_inst
);

// periphs_detect_input_fsize() - Detect the input frame size from the IMAGEON
//                                FMC card. This function blocks until lock is
//                                achieved (or times out)
//   - p_periphs_inst - Pointer to object to work on
//   - return         - Function status return value (see above)
int periphs_detect_input_fsize
(
	periphs_t* p_periphs_inst
);

// periphs_set_fsize() - Set frame size (intended to be used
//                             when no FMC card is present)
//   - p_periphs_inst - Pointer to object to work on
//   - return         - Function status return value (see above)
int periphs_set_fsize
(
	XVprocSs*   p_scaler_inst,
	vid_io_intf_t*  p_vid_io_inst
);

// periphs_update_output_fsize() - Change the input frame size
//   - p_periphs_inst    - Pointer to object to work on
//   - new_output_timing - New output timing option to use from video_resolution.h
int periphs_update_output_fsize
(
	periphs_t*   p_periphs_inst,
	unsigned int new_output_timing
);

// periphs_select_scaler() - Select which scaler to use
//   - p_periphs_inst - Pointer to object to work on
//   - which_scaler   - Which scaler datapath to use
void periphs_select_scaler
(
	periphs_t*      p_periphs_inst,
	scaler_option_t which_scaler
);

// periphs_toggle_tpg() - Enable/bypass TPG
//   - p_periphs_inst - Pointer to object to work on
//   - return         - Function status return value (see above)
int periphs_toggle_GUI_tpg
(
	periphs_t* p_periphs_inst
);

int periphs_toggle_camera_freeze_vdma
(
	periphs_t* p_periphs_inst
);

int periphs_configure_gpio_pins
(
	periphs_t*	p_periphs_inst
);

int SetupInterruptSystem
(
	periphs_t*	p_periphs_inst
);

int periphs_bring_up_input_pipeline
(
	periphs_t*   p_periphs_inst
);

int periphs_bring_up_input_dma
(
	periphs_t*   p_periphs_inst
);

int periphs_bring_up_output_pipeline
(
	periphs_t*   p_periphs_inst,
	unsigned int new_output_timing,
	unsigned int fb_GUI_start_addr
);

int periphs_bring_up_output_dma
(
	periphs_t*   p_periphs_inst
);

periphs_t periphs_inst;

void scutimer_IntrHandler(void *CallBackRef);





#endif // _PERIPHS_H_

