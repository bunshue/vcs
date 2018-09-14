

// *****************************************************
// Dependencies
// *****************************************************
#include <stdio.h>
#include <stdlib.h>
#include "xil_cache.h"
#include "platform.h"
#include "main.h"
#include "xuartps_hw.h"
#include "periphs.h"
#include "mixer.h"
#include "gpio.h"
#include "ulpi.h"
#include "xiicps.h"
#include "sleep.h"

#include "xparameters.h"
#include "xiicps.h"
#include "xil_printf.h"

#define IIC_DEVICE_ID		XPAR_XIICPS_0_DEVICE_ID

//#define IIC_SLAVE_ADDR		0xE0		//TCA9546A
#define IIC_SLAVE_ADDR		0x68	//RTC
#define IIC_SCLK_RATE		100000

#define TEST_BUFFER_SIZE	2
#define TX_BUFFER_SIZE	2
#define RX_BUFFER_SIZE	8

int IicPsMasterPolledExample(u16 DeviceId);
XIicPs Iic;		/**< Instance of the IIC Device */
u8 SendBuffer[TX_BUFFER_SIZE];    /**< Buffer for Transmitting Data */
u8 RecvBuffer[RX_BUFFER_SIZE];    /**< Buffer for Receiving Data */


//int IicPsSelfTestExample(u16 DeviceId);

//XIicPs Iic;			/* Instance of the IIC Device */


//----------------------------------------------------
// MAIN FUNCTION
//----------------------------------------------------

int main()
{

    usleep(200000);usleep(200000);usleep(200000);usleep(200000);

    xil_printf("\n\n\n\nTest\n\r");
    xil_printf("Compiled time: %s %s\n\r", __DATE__, __TIME__);
    xil_printf("%s:%s(%d)\n\r\n\r",__FILE__,__func__,__LINE__);

    /*
	int Status;
	int deviceid;


	 //Run the Iic Self Test example, specify the Device ID that is
	 //generated in xparameters.h
	deviceid = 0;
	xil_printf("IIC Self Test Example, device id = %d\r\n", deviceid);
	Status = IicPsSelfTestExample(deviceid);
	if (Status != XST_SUCCESS) {
		xil_printf("IIC Self Test Failed\r\n");
		return XST_FAILURE;
	}

	xil_printf("Successfully ran IIC Self Test Example Test\r\n");

    usleep(200000);usleep(200000);usleep(200000);usleep(200000);

    xil_printf("\n\n\n\n");

	deviceid = 1;
	xil_printf("IIC Self Test Example, device id = %d\r\n", deviceid);
	Status = IicPsSelfTestExample(deviceid);
	if (Status != XST_SUCCESS) {
		xil_printf("IIC Self Test Failed\r\n");
		return XST_FAILURE;
	}

	xil_printf("Successfully ran IIC Self Test Example Test\r\n");



	return XST_SUCCESS;
	*/

    int Status;

	while(1)
	{
		xil_printf("IIC Master Polled Example Test \r\n");

		/*
		 * Run the Iic polled example in master mode, specify the Device
		 * ID that is specified in xparameters.h.
		 */
		//Status = IicPsMasterPolledExample(IIC_DEVICE_ID);
		Status = IicPsMasterPolledExample(1);
		if (Status != XST_SUCCESS) {
			xil_printf("IIC Master Polled Example Test Failed\r\n");
			//return XST_FAILURE;
		}

		xil_printf("Successfully ran IIC Master Polled Example Test\r\n");
		usleep(200000);usleep(200000);usleep(200000);usleep(200000);
		usleep(200000);usleep(200000);usleep(200000);usleep(200000);
		usleep(200000);usleep(200000);usleep(200000);usleep(200000);
	}
	return XST_SUCCESS;

}

int IicPsMasterPolledExample(u16 DeviceId)
{
	int Status;
	XIicPs_Config *Config;
	int Index;

	/*
	 * Initialize the IIC driver so that it's ready to use
	 * Look up the configuration in the config table,
	 * then initialize it.
	 */
	Config = XIicPs_LookupConfig(DeviceId);
	if (NULL == Config) {
		return XST_FAILURE;
	}

	Status = XIicPs_CfgInitialize(&Iic, Config, Config->BaseAddress);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	xil_printf("device id = %d, base_addr = 0x%x\r\n", DeviceId, Config->BaseAddress);
	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));

	/*
	 * Perform a self-test to ensure that the hardware was built correctly.
	 */
	Status = XIicPs_SelfTest(&Iic);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	/*
	 * Set the IIC serial clock rate.
	 */
	XIicPs_SetSClk(&Iic, IIC_SCLK_RATE);

	/*
	 * Initialize the send buffer bytes with a pattern to send and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified.
	 */
	SendBuffer[0] = 0;

	for (Index = 0; Index < RX_BUFFER_SIZE; Index++) {
		RecvBuffer[Index] = 0;
	}

	/*
	 * Send the buffer using the IIC and ignore the number of bytes sent
	 * as the return value since we are using it in interrupt mode.
	 */

	xil_printf("aaaa\n\r");
	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");

	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));

	Status = XIicPs_MasterSendPolled(&Iic, SendBuffer,
			 TEST_BUFFER_SIZE, IIC_SLAVE_ADDR);

	xil_printf("bbbb\n\r");
	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");

	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));


	if (Status != XST_SUCCESS) {
		xil_printf("david0719: %s:%s(%d) ffff b\r\n",__FILE__,__func__,__LINE__);
		return XST_FAILURE;
	}


	/*
	 * Wait until bus is idle to start another transfer.
	 */
	while (XIicPs_BusIsBusy(&Iic)) {
		/* NOP */
	}

	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");

	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));

	Status = XIicPs_MasterRecvPolled(&Iic, RecvBuffer,
			  RX_BUFFER_SIZE, IIC_SLAVE_ADDR);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");

	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));

	xil_printf("\n\rdata: \t");
	for (Index = 0; Index < RX_BUFFER_SIZE; Index++) {
		xil_printf("data: %X\t",RecvBuffer[Index]);
	}
	xil_printf("\n\r");

	return XST_SUCCESS;
}

int IicPsSelfTestExample(u16 DeviceId)
{
	int Status;
	XIicPs_Config *Config;

	/*
	 * Initialize the IIC driver so that it's ready to use
	 * Look up the configuration in the config table, then initialize it.
	 */
	Config = XIicPs_LookupConfig(DeviceId);
	if (NULL == Config) {
		return XST_FAILURE;
	}

	Status = XIicPs_CfgInitialize(&Iic, Config, Config->BaseAddress);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	xil_printf("device id = %d, base_addr = 0x%x\r\n", DeviceId, Config->BaseAddress);
	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");

	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));

	/*
	 * Perform a self-test.
	 */
	Status = XIicPs_SelfTest(&Iic);
	if (Status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	xil_printf("%s\t%s\t%s\t%s\t", "CR", "SR", "ADDR", "DATA");
	xil_printf("%s\t%s\t%s\t%s\t", "ISR", "TRAN", "SLV", "TIME");
	xil_printf("%s\t%s\t%s\n\r", "IMR", "IER", "IDR");


	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x00), XIicPs_ReadReg(Config->BaseAddress, 0x04), XIicPs_ReadReg(Config->BaseAddress, 0x08), XIicPs_ReadReg(Config->BaseAddress, 0x0c));
	xil_printf("%X\t%X\t%X\t%X\t", XIicPs_ReadReg(Config->BaseAddress, 0x10), XIicPs_ReadReg(Config->BaseAddress, 0x14), XIicPs_ReadReg(Config->BaseAddress, 0x18), XIicPs_ReadReg(Config->BaseAddress, 0x1c));
	xil_printf("%X\t%X\t%X\n\r", XIicPs_ReadReg(Config->BaseAddress, 0x20), XIicPs_ReadReg(Config->BaseAddress, 0x24), XIicPs_ReadReg(Config->BaseAddress, 0x28));


	return XST_SUCCESS;
}



systemticks_t gfxSystemTicks(void)
{
	return g_ms_tick;
}

systemticks_t gfxMillisecondsToTicks(delaytime_t ms)
{
	return ms;
}
/////////////////////////////////////

uint32_t tusb_tick_get(void)
{
  //return system_ticks;
  return g_ms_tick;
}

