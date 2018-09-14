
// *****************************************************
// Dependencies
// *****************************************************
#include "psuart0.h"
#include "periphs.h"
#include "sleep.h"

volatile int TotalReceivedCount = 0;
volatile int TotalSentCount = 0;
int TotalErrorCount = 0;

static u8 SendBuffer[PSUART0_BUFFER_SIZE];	/* Buffer for Transmitting Data */
static u8 RecvBuffer[PSUART0_BUFFER_SIZE];	/* Buffer for Receiving Data */

// *****************************************************
// Private functions
// *****************************************************

/****************************************************************************
psuart0 interrupt handler
******************************************************************************/
void psuart0_IntrHandler(void *CallBackRef, u32 Event, unsigned int EventData)
{
	XUartPs *psuart0 = (XUartPs *)CallBackRef;

	/* All of the data has been sent */
	if (Event == XUARTPS_EVENT_SENT_DATA) {
		TotalSentCount = EventData;
	}

	/* All of the data has been received */
	if (Event == XUARTPS_EVENT_RECV_DATA) {
		TotalReceivedCount = EventData;
	}

	/*
	 * Data was received, but not the expected number of bytes, a
	 * timeout just indicates the data stopped for 8 character times
	 */
	if (Event == XUARTPS_EVENT_RECV_TOUT) {
		TotalReceivedCount = EventData;
	}

	/*
	 * Data was received with an error, keep the data but determine
	 * what kind of errors occurred
	 */
	if (Event == XUARTPS_EVENT_RECV_ERROR) {
		TotalReceivedCount = EventData;
		TotalErrorCount++;
	}

	/*
	 * Data was received with an parity or frame or break error, keep the data
	 * but determine what kind of errors occurred. Specific to Zynq Ultrascale+
	 * MP.
	 */
	if (Event == XUARTPS_EVENT_PARE_FRAME_BRKE) {
		TotalReceivedCount = EventData;
		TotalErrorCount++;
	}

	/*
	 * Data was received with an overrun error, keep the data but determine
	 * what kind of errors occurred. Specific to Zynq Ultrascale+ MP.
	 */
	if (Event == XUARTPS_EVENT_RECV_ORERR) {
		TotalReceivedCount = EventData;
		TotalErrorCount++;
	}

}

unsigned int psuart0_dongle_ping(void)
{
	uint32_t Index;

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */
	for (Index = 0; Index < PSUART0_BUFFER_SIZE; Index++) {

		//SendBuffer[Index] = (Index % 26) + 'A';
		SendBuffer[Index] = 0;

		RecvBuffer[Index] = 0;
	}

	// Init SendBuffer with data
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x05;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[5] = 0x30;	//					data3, write address 0x300A, only move pointer
	SendBuffer[6] = 0x0A;	//					data4


	SendBuffer[7] = 0xFF;	//sync
	SendBuffer[8] = 0xAA;	//sync
	SendBuffer[9] = 0x04;	//len					data0
	SendBuffer[10] = 0x57;	//op code	I2C_READ	data1
	SendBuffer[11] = 0x79;	//						data2	, sensor address
	SendBuffer[12] = 0xCC;	//						data3	, dummy variable

	SendBuffer[13] = 0xFF;	//sync
	SendBuffer[14] = 0xAA;	//sync
	SendBuffer[15] = 0x03;	//len				data0
	SendBuffer[16] = 0xA3;	//op code			data1  0xA_:CMD_READ 0x3 addr for I2C
	SendBuffer[17] = 0x01;	//					data2

	/*
	 * Wait for the entire buffer to be received, letting the interrupt
	 * processing work in the background, this function may get locked
	 * up in this loop if the interrupts are not working correctly.
	 */
	while (1) {

		TotalSentCount = 0;
		TotalReceivedCount = 0;

		// Set up send buffer

		/*
		 * Start receiving data before sending it since there is a loopback,
		 * ignoring the number of bytes received as the return value since we
		 * know it will be zero
		 */
		XUartPs_Recv(periphs_inst.p_psuart0_inst, RecvBuffer, PSUART0_BUFFER_SIZE);

		/*
		 * Send the buffer using the UART and ignore the number of bytes sent
		 * as the return value since we are using it in interrupt mode.
		 */
		XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 18);

		//xil_printf("detecting dongle\r\n");
		usleep(200000); // Sleep for a bit to wait for response

		//xil_printf("sent: %d, rec: %d\r\n", TotalSentCount, TotalReceivedCount);

		if (TotalSentCount+1 == TotalReceivedCount)
		{
			// Found Camera
			if(RecvBuffer[18] == 0x76)//xil_printf("dongle+camera\r\n");
				return 0; // All plugged in
		}
		else if (TotalSentCount == TotalReceivedCount)
		{
			//xil_printf("dongle only\r\n");
			return 1; // Found dongle but no camera
		}
		else if (TotalSentCount == 18 && TotalReceivedCount == 0)
		{
			//xil_printf("no dongle\r\n");
			return 2; // No dongle or camera
		}
	}

	//	/* Verify the entire receive buffer was successfully received */
	//	for (Index = 0; Index < TEST_BUFFER_SIZE; Index++) {
	//		if (RecvBuffer[Index] != SendBuffer[Index]) {
	//			BadByteCount++;
	//		}
	//	}
}

unsigned int test_dongle_read_write(void)
{
	uint32_t i;

	xil_printf("test_dongle_read_write ST\n\r");

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */

	//						64
	for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
	{
		//SendBuffer[i] = (Index % 26) + 'A';
		SendBuffer[i] = 0;
		RecvBuffer[i] = 0;
	}

	// Init SendBuffer with data
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x05;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[5] = 0x30;	//					data3, write address 0x300A, only move pointer
	SendBuffer[6] = 0x0A;	//					data4


	SendBuffer[7] = 0xFF;	//sync
	SendBuffer[8] = 0xAA;	//sync
	SendBuffer[9] = 0x04;	//len					data0
	SendBuffer[10] = 0x57;	//op code	I2C_READ	data1
	SendBuffer[11] = 0x79;	//						data2	, sensor address
	SendBuffer[12] = 0xCC;	//						data3	, dummy variable

	SendBuffer[13] = 0xFF;	//sync
	SendBuffer[14] = 0xAA;	//sync
	SendBuffer[15] = 0x03;	//len				data0
	SendBuffer[16] = 0xA3;	//op code			data1  0xA_:CMD_READ 0x3 addr for I2C
	SendBuffer[17] = 0x01;	//					data2

	/*
	 * Wait for the entire buffer to be received, letting the interrupt
	 * processing work in the background, this function may get locked
	 * up in this loop if the interrupts are not working correctly.
	 */
	while (1)
	{
		TotalSentCount = 0;
		TotalReceivedCount = 0;

		// Set up send buffer

		/*
		 * Start receiving data before sending it since there is a loopback,
		 * ignoring the number of bytes received as the return value since we
		 * know it will be zero
		 */
		//														64
		XUartPs_Recv(periphs_inst.p_psuart0_inst, RecvBuffer, PSUART0_BUFFER_SIZE);

		xil_printf("RecvBuffer : 0x \n\r");
		for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
		{
			xil_printf("%x ", RecvBuffer[i]);
			if((i%16) == 15)
				xil_printf("\n\r");
		}
		xil_printf("\n\r");
		xil_printf("TotalReceivedCount = %d\n\r",TotalReceivedCount);

		/*
		 * Send the buffer using the UART and ignore the number of bytes sent
		 * as the return value since we are using it in interrupt mode.
		 */
		XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 18);

		xil_printf("RecvBuffer : 0x \n\r");
		for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
		{
			xil_printf("%x ", RecvBuffer[i]);
			if((i%16) == 15)
				xil_printf("\n\r");
		}
		xil_printf("\n\r");
		xil_printf("TotalReceivedCount = %d\n\r",TotalReceivedCount);

		//xil_printf("detecting dongle\r\n");
		usleep(200000); // Sleep for a bit to wait for response

		//										18				19, 18, 0
		xil_printf("sent: %d, rec: %d\r\n", TotalSentCount, TotalReceivedCount);

		//		18 + 1				19
		if (TotalSentCount+1 == TotalReceivedCount)
		{
			// Found Camera
			xil_printf("psuart0_dongle_ping SP 0 dongle + camera\n\r");
			if(RecvBuffer[18] == 0x76)//xil_printf("dongle+camera\r\n");
				return 0; // All plugged in
		}
		//			18					18
		else if (TotalSentCount == TotalReceivedCount)
		{
			//xil_printf("dongle only\r\n");
			xil_printf("psuart0_dongle_ping SP 1 dongle only\n\r");
			return 1; // Found dongle but no camera
		}
		//			18							0
		else if (TotalSentCount == 18 && TotalReceivedCount == 0)
		{
			//xil_printf("no dongle\r\n");
			xil_printf("psuart0_dongle_ping SP 2 no dongle\n\r");
			return 2; // No dongle or camera
		}
	}

	//	/* Verify the entire receive buffer was successfully received */
	//	for (Index = 0; Index < TEST_BUFFER_SIZE; Index++) {
	//		if (RecvBuffer[Index] != SendBuffer[Index]) {
	//			BadByteCount++;
	//		}
	//	}
}


unsigned char dongle_read_data(unsigned int addr)
{
	uint32_t i;

	//xil_printf("dongle_read_data ST addr = 0x%x\n\r", addr);

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */

	//						64
	for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
	{
		//SendBuffer[i] = (Index % 26) + 'A';
		SendBuffer[i] = 0;
		RecvBuffer[i] = 0;
	}

	// Init SendBuffer with data
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x05;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[5] = (addr >> 8)&0xff;	//		data3, write address 0x300A, only move pointer
	SendBuffer[6] = addr & 0xff;		//		data4

	SendBuffer[7] = 0xFF;	//sync
	SendBuffer[8] = 0xAA;	//sync
	SendBuffer[9] = 0x04;	//len					data0
	SendBuffer[10] = 0x57;	//op code	I2C_READ	data1
	SendBuffer[11] = 0x79;	//						data2	, sensor address
	SendBuffer[12] = 0xCC;	//						data3	, dummy variable

	SendBuffer[13] = 0xFF;	//sync
	SendBuffer[14] = 0xAA;	//sync
	SendBuffer[15] = 0x03;	//len				data0
	SendBuffer[16] = 0xA3;	//op code			data1  0xA_:CMD_READ 0x3 addr for I2C
	SendBuffer[17] = 0x01;	//					data2

	/*
	 * Wait for the entire buffer to be received, letting the interrupt
	 * processing work in the background, this function may get locked
	 * up in this loop if the interrupts are not working correctly.
	 */
	//while (1)
	{
		TotalSentCount = 0;
		TotalReceivedCount = 0;

		// Set up send buffer

		/*
		 * Start receiving data before sending it since there is a loopback,
		 * ignoring the number of bytes received as the return value since we
		 * know it will be zero
		 */
		//														64
		XUartPs_Recv(periphs_inst.p_psuart0_inst, RecvBuffer, PSUART0_BUFFER_SIZE);

		/*
		 * Send the buffer using the UART and ignore the number of bytes sent
		 * as the return value since we are using it in interrupt mode.
		 */
		XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 18);

		/*
		xil_printf("RecvBuffer : 0x \n\r");
		for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
		{
			xil_printf("%x ", RecvBuffer[i]);
			if((i%16) == 15)
				xil_printf("\n\r");
		}
		xil_printf("\n\r");
		xil_printf("TotalReceivedCount = %d\n\r",TotalReceivedCount);
		*/

		//xil_printf("detecting dongle\r\n");
		usleep(200000); // Sleep for a bit to wait for response

		if(TotalReceivedCount == 19)
		{
			//xil_printf("data : 0x%x\n\r", RecvBuffer[18]);
			return RecvBuffer[18];
		}
		else
			return 0;

	}
}

unsigned char dongle_write_data(unsigned int addr, unsigned char data)
{
	uint32_t i;

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */

	//						64
	for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
	{
		//SendBuffer[i] = (Index % 26) + 'A';
		SendBuffer[i] = 0;
		RecvBuffer[i] = 0;
	}

	// Init SendBuffer with data
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x06;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[5] = (addr >> 8)&0xff;	//		data3, write address 0x300A, only move pointer
	SendBuffer[6] = addr & 0xff;		//		data4
	SendBuffer[7] = (data&0xff);		//		data5

	XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 8);

	return 0;
}


unsigned char* dongle_read_n_data(unsigned int addr, unsigned int len)
{
	uint32_t i;

	xil_printf("fail to read 2 bytes by one command\n\r");

	xil_printf("dongle_read_data ST addr = 0x%x\n\r", addr);

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */

	//						64
	for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
	{
		//SendBuffer[i] = (Index % 26) + 'A';
		SendBuffer[i] = 0;
		RecvBuffer[i] = 0;
	}

	// Init SendBuffer with data
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x05;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[5] = (addr >> 8)&0xff;	//		data3, write address 0x300A, only move pointer
	SendBuffer[6] = addr & 0xff;		//		data4

	SendBuffer[7] = 0xFF;	//sync
	SendBuffer[8] = 0xAA;	//sync
	SendBuffer[9] = 0x05;	//len					data0
	SendBuffer[10] = 0x57;	//op code	I2C_READ	data1
	SendBuffer[11] = 0x79;	//						data2	, sensor address
	SendBuffer[12] = 0xCC;	//						data3	, dummy variable
	SendBuffer[13] = 0xDD;	//						data4	, dummy variable

	SendBuffer[14] = 0xFF;	//sync
	SendBuffer[15] = 0xAA;	//sync
	SendBuffer[16] = 0x04;	//len				data0
	SendBuffer[17] = 0xA4;	//op code			data1  0xA_:CMD_READ 0x3 addr for I2C
	SendBuffer[18] = 0x01;	//					data2
	SendBuffer[19] = 0x01;	//					data3

	/*
	 * Wait for the entire buffer to be received, letting the interrupt
	 * processing work in the background, this function may get locked
	 * up in this loop if the interrupts are not working correctly.
	 */
	//while (1)
	{
		TotalSentCount = 0;
		TotalReceivedCount = 0;

		// Set up send buffer

		/*
		 * Start receiving data before sending it since there is a loopback,
		 * ignoring the number of bytes received as the return value since we
		 * know it will be zero
		 */
		//														64
		XUartPs_Recv(periphs_inst.p_psuart0_inst, RecvBuffer, PSUART0_BUFFER_SIZE);

		/*
		 * Send the buffer using the UART and ignore the number of bytes sent
		 * as the return value since we are using it in interrupt mode.
		 */
		XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 20);

		/*
		xil_printf("RecvBuffer : 0x \n\r");
		for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
		{
			xil_printf("%x ", RecvBuffer[i]);
			if((i%16) == 15)
				xil_printf("\n\r");
		}
		xil_printf("\n\r");
		xil_printf("TotalReceivedCount = %d\n\r",TotalReceivedCount);
		*/

		//xil_printf("detecting dongle\r\n");
		usleep(200000); // Sleep for a bit to wait for response

		xil_printf("TotalReceivedCount = %d\n\r",TotalReceivedCount);

		if(TotalReceivedCount == 20)
		{
			xil_printf("data : 0x%x\n\r", RecvBuffer[18]);
			xil_printf("data : 0x%x\n\r", RecvBuffer[19]);
			return 0;
		}
		else
			return 0;

	}
}

void psuart0_exposure(unsigned int exposure)
{
	uint32_t Index;

	if(exposure < 1 || exposure > 5)
		return;



	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */
	for (Index = 0; Index < PSUART0_BUFFER_SIZE; Index++) {

		//SendBuffer[Index] = (Index % 26) + 'A';
		SendBuffer[Index] = 0;

		RecvBuffer[Index] = 0;
	}

	TotalSentCount = 0;
	TotalReceivedCount = 0;

	// Init SendBuffer, white point
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x06;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[5] = 0x3a;	//					data3
	SendBuffer[6] = 0x03;	//					data4
							//SendBuffer[7]		data5
	switch(exposure)
	{
		case 1:
			SendBuffer[7] = 0x2A;
			break;
		case 2:
			SendBuffer[7] = 0x36;
			break;
		case 3:
			SendBuffer[7] = 0x42;
			break;
		case 4:
			SendBuffer[7] = 0x4E;
			break;
		case 5:
			SendBuffer[7] = 0x5A;
			break;
		default:
			break;
	}

	SendBuffer[8] = 0xFF;	//sync
	SendBuffer[9] = 0xAA;	//sync
	SendBuffer[10] = 0x06;	//len				data0
	SendBuffer[11] = 0x67;	//op code 	I2C_WR	data1
	SendBuffer[12] = 0x78;	//					data2, sensor address 0x78
	SendBuffer[13] = 0x3a;	//					data3
	SendBuffer[14] = 0x04;	//					data4
							//SendBuffer[7]		data5
	switch(exposure)
	{
		case 1:
			SendBuffer[15] = 0x20;
			break;
		case 2:
			SendBuffer[15] = 0x2C;
			break;
		case 3:
			SendBuffer[15] = 0x38;
			break;
		case 4:
			SendBuffer[15] = 0x44;
			break;
		case 5:
			SendBuffer[15] = 0x50;
			break;
		default:
			break;
	}

	XUartPs_Recv(periphs_inst.p_psuart0_inst, RecvBuffer, PSUART0_BUFFER_SIZE);

	/*
	 * Send the buffer using the UART and ignore the number of bytes sent
	 * as the return value since we are using it in interrupt mode.
	 */
	XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 16);

	//xil_printf("detecting dongle\r\n");
	usleep(100000); // Sleep for a bit to wait for response

//	xil_printf("sent: %d, rec: %d\r\n", TotalSentCount, TotalReceivedCount);
//
//	for(Index=0; Index < TotalReceivedCount; Index++){
//		xil_printf("%x\r\n", RecvBuffer[Index]);
//	}
	return;
}

void psuart0_exposure_data(u8 exposure)
{
	uint32_t Index;

	if(exposure < 0 || exposure > 255)
	{
		xil_printf("david0703: %s:%s(%d) ST xxxxxxxxxxxxxxxxx\r\n",__FILE__,__func__,__LINE__);
		return;
	}

	xil_printf("david0703: %s:%s(%d) ST exposure = %d\r\n",__FILE__,__func__,__LINE__,exposure);

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */
	//						64
	for (Index = 0; Index < PSUART0_BUFFER_SIZE; Index++)
	{
		//SendBuffer[Index] = (Index % 26) + 'A';
		SendBuffer[Index] = 0;

		RecvBuffer[Index] = 0;
	}

	TotalSentCount = 0;
	TotalReceivedCount = 0;

	// Init SendBuffer, white point
	SendBuffer[0] = 0xFF;		//sync
	SendBuffer[1] = 0xAA;		//sync
	SendBuffer[2] = 0x06;		//len				data0
	SendBuffer[3] = 0x67;		//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;		//					data2, sensor address 0x78
	SendBuffer[5] = 0x3a;		//					data3
	SendBuffer[6] = 0x03;		//					data4
	SendBuffer[7] = exposure;	//SendBuffer[7]		data5

	SendBuffer[8] = 0xFF;		//sync
	SendBuffer[9] = 0xAA;		//sync
	SendBuffer[10] = 0x06;		//len				data0
	SendBuffer[11] = 0x67;		//op code 	I2C_WR	data1
	SendBuffer[12] = 0x78;		//					data2, sensor address 0x78
	SendBuffer[13] = 0x3a;		//					data3
	SendBuffer[14] = 0x04;		//					data4
	SendBuffer[15] = exposure;	//SendBuffer[7]		data5

	//														64
	XUartPs_Recv(periphs_inst.p_psuart0_inst, RecvBuffer, PSUART0_BUFFER_SIZE);

	/*
	 * Send the buffer using the UART and ignore the number of bytes sent
	 * as the return value since we are using it in interrupt mode.
	 */
	XUartPs_Send(periphs_inst.p_psuart0_inst, SendBuffer, 16);

	//xil_printf("detecting dongle\r\n");
	usleep(100000); // Sleep for a bit to wait for response

	/*
	xil_printf("sent: %d, rec: %d\r\n", TotalSentCount, TotalReceivedCount);

	for(Index=0; Index < TotalReceivedCount; Index++)
	{
		xil_printf("%x\r\n", RecvBuffer[Index]);
	}
	*/
	return;
}


