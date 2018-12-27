
// *****************************************************
// Dependencies
// *****************************************************
#include "gpio.h"
#include "psuart0.h"
#include "main.h"

uint32_t g_metering_mode = 0; // Auto = 0, Center = 1, Average = 2;
uint32_t g_exposure = 3; // 1 ~ 5, 3 is AUTO/Middle
volatile uint32_t g_updated = 0;

// *****************************************************
// Private functions
// *****************************************************

/****************************************************************************/
/**
* This function is the user layer callback function for the bank 2 interrupts of
* the GPIO device. It checks if all the switches have been pressed to stop the
* interrupt processing and exit from the example.
*
* @param	CallBackRef is a pointer to the upper layer callback reference.
* @param	Status is the Interrupt status of the GPIO bank.
*
* @return	None.
*
* @note		None.
*
******************************************************************************/
void ps_gpio_IntrHandler(void *CallBackRef, u32 Bank, u32 Status)
{
	XGpioPs *Gpio = (XGpioPs *)CallBackRef;
	u32 DataRead;
	// Clear interrupt
	//xil_printf("Bank: %x\r\n", Bank);

	// Block Bank0 and Bank1 interrupts, this might be a SDK bug, do not take away until verified
	if(Bank != XGPIOPS_BANK2) {
		return;
	}

	DataRead = XGpioPs_Read(Gpio, XGPIOPS_BANK2);

	xil_printf("Bank: %d Status = 0x%x DataRead = 0x%x\t", Bank, Status, DataRead);

	if(Status & SW_SMART)
	{
		xil_printf("SMART\r\n");
	}
	else if (Status & SW_START)
	{
		xil_printf("START\r\n");
	}
	else if (Status & SW_METER)
	{
		xil_printf("METER\r\n");
	}
	else if (Status & SW_DARKEN)
	{
		xil_printf("DARKEN\r\n");
	}
	else if (Status & SW_BRIGHT)
	{
		xil_printf("BRIGHTEN\r\n");
	}
	XGpioPs_IntrClear(Gpio, XGPIOPS_BANK2, 0xffffffff);
}

/******************************************************************************/
/**
*
* This is the interrupt handler routine for the video lock monitor
*
* @param	CallbackRef is the Callback reference for the handler.
*
* @return	None.
*
* @note		None.
*
******************************************************************************/
void lock_monitor_IntrHandler(void *CallbackRef)
{
	XGpio *lock_mon_Ptr = (XGpio *)CallbackRef;
	unsigned int status;

	status = XGpio_DiscreteRead(lock_mon_Ptr,  XGPIO_CHANNEL1);

	// Got Interrupt, Check which interrupt was signaled
	xil_printf("david0906: %s:%s(%d) ST\r\n",__FILE__,__func__,__LINE__);
	xil_printf("lock interrupt!: %x\r\n", status);

	// Clear the Interrupt on XGPIO Channel 1
	XGpio_InterruptClear(lock_mon_Ptr, XGPIO_CHANNEL1);

}
