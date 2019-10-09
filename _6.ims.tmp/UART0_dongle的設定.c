
UART0傳送dongle資料


C:\iMS_Video\iMS_Video.sdk\aries_bsp\ps7_cortexa9_0\include\xuartps.h	機器造出來的
C:\iMS_Video\iMS_Video.sdk\aries_bsp\ps7_cortexa9_0\libsrc\uartps_v3_5\src\xuartps.h	可修改



//-------------------------------------------------------------------------------------------
// main.c
int main()
{
    status = periphs_init
    (
    	&periphs_inst,			//Global變數
	XPAR_PS7_UART_0_DEVICE_ID	//0
    );

}

//-------------------------------------------------------------------------------------------
// periphs.h
typedef struct periphs
{
	XUartPs*	p_psuart0_inst;
} periphs_t;


periphs_t periphs_inst;		//Global變數


//-------------------------------------------------------------------------------------------
// xuartps.h

aries_bsp\ps7_cortexa9_0\libsrc\uartps_v3_5\src\xuartps.h
/**
 * The XUartPs driver instance data structure. A pointer to an instance data
 * structure is passed around by functions to refer to a specific driver
 * instance.
 */
typedef struct {
	XUartPs_Config Config;	/* Configuration data structure */
	u32 InputClockHz;	/* Input clock frequency */
	u32 IsReady;		/* Device is initialized and ready */
	u32 BaudRate;		/* Current baud rate */

	XUartPsBuffer SendBuffer;
	XUartPsBuffer ReceiveBuffer;

	XUartPs_Handler Handler;
	void *CallBackRef;	/* Callback reference for event handler */
	u32 Platform;
	u8 is_rxbs_error;
} XUartPs;

/**
 * This typedef contains configuration information for the device.
 */
typedef struct {
	u16 DeviceId;	 /**< Unique ID  of device */
	u32 BaseAddress; /**< Base address of device (IPIF) */
	u32 InputClockHz;/**< Input clock frequency */
	s32 ModemPinsConnected; /** Specifies whether modem pins are connected
				 *  to MIO or FMIO */
} XUartPs_Config;


//-------------------------------------------------------------------------------------------
// periphs.c
static XUartPs		 psuart0_inst;
static XUartPs_Config *g_psuart1_config = 0;

static int init_drivers
(
	periphs_t*   p_periphs_inst,
	unsigned int psuart0_device_id
)
{
	XUartPs_Config*	 p_psuart0_cfg;
	
	xil_printf("\n\r---UART driver 0xE0000000 for dongle UART 0-----------------------------------------\n\r");

	// Initialize the UART driver so that it's ready to use

	xil_printf("david0712: %s:%s(%d) call XUartPs_LookupConfig with device = %d\r\n",__FILE__,__func__,__LINE__,psuart0_device_id);
	p_psuart0_cfg = XUartPs_LookupConfig(psuart0_device_id);
	
	/*
	XUartPs_LookupConfig(0或1)
	回傳XUartPs_Config結構的指標

	XUartPs_Config XUartPs_ConfigTable[XPAR_XUARTPS_NUM_INSTANCES] =
	{
		{
			XPAR_PS7_UART_0_DEVICE_ID,
			XPAR_PS7_UART_0_BASEADDR,
			XPAR_PS7_UART_0_UART_CLK_FREQ_HZ,
			XPAR_PS7_UART_0_HAS_MODEM
		},
		{
			XPAR_PS7_UART_1_DEVICE_ID,
			XPAR_PS7_UART_1_BASEADDR,
			XPAR_PS7_UART_1_UART_CLK_FREQ_HZ,
			XPAR_PS7_UART_1_HAS_MODEM
		}
	};
	由deviceID決定XUartPs_Config結構內的4個變數
	*/

	
	if (NULL == p_psuart0_cfg)
	{
		xil_printf("ERROR! Failed to find psuart0.\n\r");
		return XST_FAILURE;
	}

	status = XUartPs_CfgInitialize(p_periphs_inst->p_psuart0_inst, p_psuart0_cfg, p_psuart0_cfg->BaseAddress);
	if (status != XST_SUCCESS)
	{
		xil_printf("ERROR! Failed to initialize psuart0.\n\r");
		return XST_FAILURE;
	}
	xil_printf("david0704: %s:%s(%d) XUartPs base address = 0x%x\r\n",__FILE__,__func__,__LINE__, p_psuart0_cfg->BaseAddress);

	xil_printf("\n\r---????? UART 1 for PC comm -----------------------------------------\n\r");


	xil_printf("david0712: %s:%s(%d) call XUartPs_LookupConfig with device = %d\r\n",__FILE__,__func__,__LINE__,XPAR_PS7_UART_1_DEVICE_ID);
	// Get psuart1 config							1
	g_psuart1_config = XUartPs_LookupConfig(XPAR_PS7_UART_1_DEVICE_ID);

	if (NULL == g_psuart1_config)
	{
		xil_printf("ERROR! Failed to find psuart0.\n\r");
		return XST_FAILURE;
	}

	//david: lack a XUartPs_CfgInitialize  ???
	return PERIPHS_SUCCESS;
}

int periphs_init
(
	periphs_t*   p_periphs_inst,
	unsigned int psuart0_device_id,
)
{
	int status = 0;
	u32 IntrMask = 0;
	u32 Index = 0;

	xil_printf("\tpsuart0_device_id = %u\r\n", psuart0_device_id);		//0

	p_periphs_inst->p_psuart0_inst			= &psuart0_inst;
	
	status = init_drivers
	(
		p_periphs_inst,
		psuart0_device_id,
	);

	// psuart0 - Connect the device driver handler that will be called when an interrupt for the device occurs
	// Print UART settings
	status = XScuGic_Connect(p_periphs_inst->p_scugic_inst, XPAR_XUARTPS_0_INTR,
				(Xil_ExceptionHandler)XUartPs_InterruptHandler, p_periphs_inst->p_psuart0_inst);
	if (status != XST_SUCCESS) {
		xil_printf("failed to connect psuart0\r\n");
		return status;
	}

	// Setup the handler for PSUART0
	XUartPs_SetHandler(p_periphs_inst->p_psuart0_inst, (XUartPs_Handler)psuart0_IntrHandler, p_periphs_inst->p_psuart0_inst);

	/*
	 * Enable the interrupt of the UART so interrupts will occur
	 */
	IntrMask =
		XUARTPS_IXR_TOUT | XUARTPS_IXR_PARITY | XUARTPS_IXR_FRAMING |
		XUARTPS_IXR_OVER | XUARTPS_IXR_TXEMPTY | XUARTPS_IXR_RXFULL |
		XUARTPS_IXR_RXOVR;

	if (p_periphs_inst->p_psuart0_inst->Platform == XPLAT_ZYNQ_ULTRA_MP) {
		IntrMask |= XUARTPS_IXR_RBRK;
	}
	XUartPs_SetInterruptMask(p_periphs_inst->p_psuart0_inst, IntrMask);

	xil_printf("\n\rdavid0709: %s:%s(%d) ST BaudRate =%d call XUartPs_SetBaudRate 333\r\n",__FILE__,__func__,__LINE__, XUARTPS_DFT_BAUDRATE);
	//maybe the same
	XUartPs_SetBaudRate(p_periphs_inst->p_psuart0_inst, XUARTPS_DFT_BAUDRATE);
	xil_printf("\r\n");

	/*
	 * Set the receiver timeout. If it is not set, and the last few bytes
	 * of data do not trigger the over-water or full interrupt, the bytes
	 * will not be received. By default it is disabled.
	 *
	 * The setting of 8 will timeout after 8 x 4 = 32 character times.
	 * Increase the time out value if baud rate is high, decrease it if
	 * baud rate is low.
	 */
	XUartPs_SetRecvTimeout(p_periphs_inst->p_psuart0_inst, 8);

	xil_printf("psuart0 baudrate: %d\r\n", p_periphs_inst->p_psuart0_inst->BaudRate);
	xil_printf("psuart0 callback: 0x%x\r\n", p_periphs_inst->p_psuart0_inst->CallBackRef);
	xil_printf("psuart0 clock: %d\r\n", p_periphs_inst->p_psuart0_inst->InputClockHz);
	xil_printf("psuart0 ready: %d\r\n", p_periphs_inst->p_psuart0_inst->IsReady);
	xil_printf("psuart0 platform: %d\r\n", p_periphs_inst->p_psuart0_inst->Platform);
	xil_printf("psuart0 rxbs_errot: %d\r\n", p_periphs_inst->p_psuart0_inst->is_rxbs_error);

	/* Enable the interrupt for the device */
	XScuGic_Enable(p_periphs_inst->p_scugic_inst, XPAR_XUARTPS_0_INTR);

	//XUartPs_SetOperMode(p_periphs_inst->p_psuart0_inst, XUARTPS_OPER_MODE_LOCAL_LOOP);
	//XUartPs_SetOperMode(p_periphs_inst->p_psuart0_inst, XUARTPS_OPER_MODE_NORMAL);

	/* Set the UART in Normal Mode */
	XUartPs_SetOperMode(p_periphs_inst->p_psuart0_inst, XUARTPS_OPER_MODE_NORMAL);

	return PERIPHS_SUCCESS;
}

//-------------------------------------------------------------------------------------------





使用:

設定dongle的攝影機的光圈大小:

psuart0_exposure(1~5);


void psuart0_exposure(unsigned int exposure)
{
	uint32_t Index;

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */
	//				64
	for (Index = 0; Index < PSUART0_BUFFER_SIZE; Index++)
	{
		SendBuffer[Index] = 0;
		RecvBuffer[Index] = 0;
	}

	TotalSentCount = 0;
	TotalReceivedCount = 0;

	// Init SendBuffer, white point
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x06;	//len		data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR	data1
	SendBuffer[4] = 0x78;	//		data2, sensor address 0x78
	SendBuffer[5] = 0x3a;	//		data3
	SendBuffer[6] = 0x03;	//		data4
				//SendBuffer[7]	data5
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
	SendBuffer[10] = 0x06;	//len		data0
	SendBuffer[11] = 0x67;	//op code 	I2C_WR	data1
	SendBuffer[12] = 0x78;	//		data2, sensor address 0x78
	SendBuffer[13] = 0x3a;	//		data3
	SendBuffer[14] = 0x04;	//		data4
				//SendBuffer[7]	data5
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

	//								64
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



uint32_t g_conn_status = 2;

void main_loop()
{
	while (1)
	{
		g_conn_status = psuart0_dongle_ping();
		if(g_conn_status == 2) // Nothing is plugged in
		{
			xil_printf("no dongle or camera\n\r");
		}
		else if(g_conn_status == 1)	// Only dongle is plugged in
		{
			xil_printf("dongle plugged only dongle\n\r");
		}
		else	// Everything is plugged in
		{
			xil_printf("all plugged, dongle + camera\n\r");
		}
	}
}




unsigned int psuart0_dongle_ping(void)
{
	uint32_t i;

	/*
	 * Initialize the send buffer bytes with a pattern and the
	 * the receive buffer bytes to zero to allow the receive data to be
	 * verified
	 */

	//			64
	for (i = 0; i < PSUART0_BUFFER_SIZE; i++)
	{
		SendBuffer[i] = 0;
		RecvBuffer[i] = 0;
	}

	// Init SendBuffer with data
	SendBuffer[0] = 0xFF;	//sync
	SendBuffer[1] = 0xAA;	//sync
	SendBuffer[2] = 0x05;	//len				data0
	SendBuffer[3] = 0x67;	//op code	I2C_WR		data1
	SendBuffer[4] = 0x78;	//				data2, sensor address 0x78
	SendBuffer[5] = 0x30;	//				data3, write address 0x300A, only move pointer
	SendBuffer[6] = 0x0A;	//				data4


	SendBuffer[7] = 0xFF;	//sync
	SendBuffer[8] = 0xAA;	//sync
	SendBuffer[9] = 0x04;	//len				data0
	SendBuffer[10] = 0x57;	//op code	I2C_READ	data1
	SendBuffer[11] = 0x79;	//				data2, sensor address
	SendBuffer[12] = 0xCC;	//				data3, dummy variable

	SendBuffer[13] = 0xFF;	//sync
	SendBuffer[14] = 0xAA;	//sync
	SendBuffer[15] = 0x03;	//len				data0
	SendBuffer[16] = 0xA3;	//op code			data1  0xA_:CMD_READ 0x3 addr for I2C
	SendBuffer[17] = 0x01;	//				data2

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

		//										18				19, 18, 0
		//xil_printf("sent: %d, rec: %d\r\n", TotalSentCount, TotalReceivedCount);

		//		18 + 1				19
		if (TotalSentCount+1 == TotalReceivedCount)
		{
			// Found Camera
			//xil_printf("psuart0_dongle_ping SP 0 dongle + camera\n\r");
			if(RecvBuffer[18] == 0x76)//xil_printf("dongle+camera\r\n");
				return 0; // All plugged in
		}
		//			18					18
		else if (TotalSentCount == TotalReceivedCount)
		{
			//xil_printf("dongle only\r\n");
			//xil_printf("psuart0_dongle_ping SP 1 dongle only\n\r");
			return 1; // Found dongle but no camera
		}
		//			18							0
		else if (TotalSentCount == 18 && TotalReceivedCount == 0)
		{
			//xil_printf("no dongle\r\n");
			//xil_printf("psuart0_dongle_ping SP 2 no dongle\n\r");
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

