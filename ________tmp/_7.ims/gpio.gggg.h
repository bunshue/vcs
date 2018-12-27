
#ifndef _GPIO_H_
#define _GPIO_H_

// *****************************************************
// Dependencies
// *****************************************************

#include "xgpio.h"
#include "xgpiops.h"
#include "xscugic.h"
//#include "main.h"
#include "periphs.h"

// *****************************************************
// Function status return values
// *****************************************************
#define GPIO_SUCCESS        0
#define GPIO_ERROR_UNKNOWN -1

// *****************************************************
// Pin Placing

#define GPIO_LED_CEN 	54
#define GPIO_LED_AVG 	55
#define GPIO_LED_AUTO	56
#define GPIO_LED_1		57
#define GPIO_LED_2	 	58
#define GPIO_LED_3 		59
#define GPIO_LED_4		60
#define GPIO_LED_5		61
#define GPIO_LED_RED	62
#define GPIO_FAN_EN		63		//not used yet
#define GPIO_CAM_LED	64		//not used yet


// Outputs
#define LED_CEN 	0x00000001
#define LED_AVG 	0x00000002
#define LED_AUTO	0x00000004
#define LED_1		0x00000008
#define LED_2	 	0x00000010
#define LED_3 		0x00000020
#define LED_4		0x00000040
#define LED_5		0x00000080
#define LED_RED		0x00000100	//not used yet
#define FAN_EN		0x00000200	//not used yet
#define CAM_LED		0x00000400	//not used yet
#define IO_CD		0x00010000	//not used yet
#define IO_KEY		0x00020000	//not used yet
// Inputs
#define SW_SMART	0x00000800
#define SW_START	0x00001000
#define SW_METER	0x00002000
#define SW_DARKEN	0x00004000
#define SW_BRIGHT	0x00008000
// Unused
#define IO_UNUSED	0xFFFC0000

#define INPUT_INTERRUPT_ALL (SW_SMART|SW_START|SW_METER|SW_DARKEN|SW_BRIGHT)

// Pin direction
// Outputs
#define LED_CEN_DIR 	0x00000001
#define LED_AVG_DIR 	0x00000002
#define LED_AUTO_DIR	0x00000004
#define LED_1_DIR		0x00000008
#define LED_2_DIR	 	0x00000010
#define LED_3_DIR 		0x00000020
#define LED_4_DIR		0x00000040
#define LED_5_DIR		0x00000080
#define LED_RED_DIR		0x00000100
#define FAN_EN_DIR		0x00000200
#define CAM_LED_DIR		0x00000400
#define IO_CD_DIR		0x00010000
#define IO_KEY_DIR		0x00020000
// Inputs
#define SW_SMART_DIR	0x00000000
#define SW_START_DIR	0x00000000
#define SW_METER_DIR	0x00000000
#define SW_DARKEN_DIR	0x00000000
#define SW_BRIGHT_DIR	0x00000000
// Untied
#define IO_UNUSED_DIR	0xFFFC0000

#define PIN_DIR_DEFAULT (LED_CEN_DIR | LED_AVG_DIR | LED_AUTO_DIR | LED_1_DIR | LED_2_DIR | LED_3_DIR | LED_4_DIR | LED_5_DIR | LED_RED_DIR | FAN_EN_DIR | CAM_LED_DIR | IO_CD_DIR | IO_KEY_DIR |IO_UNUSED_DIR)

// Pin output default
// Outputs
#define LED_CEN_DEF 	0x00000000
#define LED_AVG_DEF 	0x00000000
#define LED_AUTO_DEF	0x00000004
#define LED_1_DEF		0x00000000
#define LED_2_DEF	 	0x00000000
#define LED_3_DEF 		0x00000020
#define LED_4_DEF		0x00000000
#define LED_5_DEF		0x00000000
#define LED_RED_DEF		0x00000000
#define FAN_EN_DEF		0x00000200
#define CAM_LED_DEF		0x00000400
#define IO_CD_DEF		0x00000000
#define IO_KEY_DEF		0x00000000
// Inputs
#define SW_SMART_DEF	0x00000000
#define SW_START_DEF	0x00000000
#define SW_METER_DEF	0x00000000
#define SW_DARKEN_DEF	0x00000000
#define SW_BRIGHT_DEF	0x00000000

// Untied
#define IO_UNUSED_DEF	0x00000000

#define PIN_DEF_DEFAULT (LED_CEN_DEF | LED_AVG_DEF | LED_AUTO_DEF | LED_1_DEF | LED_2_DEF | LED_3_DEF | LED_4_DEF | LED_5_DEF | LED_RED_DEF | FAN_EN_DEF | CAM_LED_DEF | IO_CD_DEF | IO_KEY_DEF |IO_UNUSED_DEF)

#define XGPIO_CHANNEL1		1

uint32_t g_metering_mode; // Auto = 0, Center = 1, Average = 2;
uint32_t g_exposure; // 1 ~ 5, 3 is AUTO/Middle
volatile uint32_t g_updated;


void ps_gpio_IntrHandler(void *CallBackRef, u32 Bank, u32 Status);
void lock_monitor_IntrHandler(void *CallBackRef);

#endif // _GPIO_H_

