
#ifndef _MAIN_H_
#define _MAIN_H_

// *****************************************************
// Function status return values
// *****************************************************
#define MAIN_SUCCESS        0
#define MAIN_ERROR_UNKNOWN -1

#include "xtime_l.h"
#include "gfx.h"
#include "tusb.h"
#include "mouse_host_app.h"
#include "keyboard_host_app.h"

// *****************************************************
// Constants
// *****************************************************
#define FRAMEBUFFER_GUI_START_ADDR XPAR_PS7_DDR_0_S_AXI_BASEADDR + 0x30000000
#define FRAMEBUFFER_CAMERA_START_ADDR XPAR_PS7_DDR_0_S_AXI_BASEADDR + 0x32000000 // shift by 32MB
#define FRAMEBUFFER_CAMERA_FREEZE_START_ADDR XPAR_PS7_DDR_0_S_AXI_BASEADDR + 0x32400000 // Shift by 4MB

#define COUNTS_PER_MILLI_SECOND (COUNTS_PER_SECOND/1000)

#define LAYER0_WIDTH    1920
#define LAYER0_HEIGHT   1080
#define LAYER1_WIDTH 1216
#define LAYER1_HEIGHT 912
#define LAYER2_WIDTH 640
#define LAYER2_HEIGHT 480
#define LAYER3_WIDTH    1920
#define LAYER3_HEIGHT   1080

#define CAMERA_X 640
#define CAMERA_Y 480
#define BORDER_X 16
#define BORDER_Y 16

// *****************************************************
// Globals
// *****************************************************
//uint32_t g_metering_mode = 0; // Auto = 0, Center = 1, Average = 2;
//uint32_t g_exposure = 3; // 1 ~ 5, 3 is AUTO/Middle
volatile uint32_t g_ms_uptime;
volatile uint32_t g_ms_tick;
uint32_t g_nn;
uint32_t g_dongle_plugged;
uint32_t g_camera_plugged;

uint32_t update_dongle_status;
uint32_t update_usb_status;
uint32_t update_usb_descriptor_status;
uint16_t vendor_id_tmp;
uint16_t product_id_tmp;

// *****************************************************
// Function prototypes
// *****************************************************
void main_menu();
void TIMERinit(uint32_t Reload);

#endif // _MAIN_H_

