
#ifndef _PSUSB0_H_
#define _PSUSB0_H_

// *****************************************************
// Dependencies
// *****************************************************

#include "xscugic.h"
#include "xusbps.h"
//#include "main.h"
#include "periphs.h"

// *****************************************************
// Function status return values
// *****************************************************
#define PSUSB0_SUCCESS        0
#define PSUSB0_ERROR_UNKNOWN -1

#define PSUSB0_BUFFER_SIZE	64

#define XUSBPS_ULPIVIEW_DATWR_SHIFT	(0) /**< ULPI Data Write */
#define XUSBPS_ULPIVIEW_DATRD_SHIFT	(8) /**< ULPI Data Read */
#define XUSBPS_ULPIVIEW_ADDR_SHIFT	(16) /**< ULPI Data Address */
#define XUSBPS_ULPIVIEW_PORT_SHIFT	(24) /**< ULPI Port Number */
#define XUSBPS_ULPIVIEW_SS_SHIFT	(27) /**< ULPI Synchronous State */
#define XUSBPS_ULPIVIEW_RW_SHIFT	(29) /**< ULPI Read/Write Control */
#define XUSBPS_ULPIVIEW_RUN_SHIFT	(30) /**< ULPI Run */
#define XUSBPS_ULPIVIEW_WU_SHIFT	(31) /**< ULPI Wakeup */

//static u8 SendBuffer[PSUSB0_BUFFER_SIZE];	/* Buffer for Transmitting Data */
//static u8 RecvBuffer[PSUSB0_BUFFER_SIZE];	/* Buffer for Receiving Data */

void psusb0_IntrHandler(void *CallBackRef);
void psusb0_hal_interrupt_enable(uint8_t coreid);
void psusb0_hal_interrupt_disable(uint8_t coreid);
int psusb0_hal_controller_reset(uint8_t coreid);
int32_t ulpi_init(void);
int32_t ulpi_check_integrity(void);
int32_t ulpi_set_flags(void);
int32_t ulpi_set_otg_flags(void);
int32_t ulpi_set_ic_flags(void);
int32_t ulpi_set_fc_flags(void);
int32_t ulpi_set_vbus(int32_t on);
uint8_t ulpi_ReadReg(uint8_t reg);
int32_t ulpi_WriteReg(uint8_t flags, uint8_t reg);






#endif // _PSUSB0_H_

