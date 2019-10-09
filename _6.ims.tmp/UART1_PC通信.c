UART1 與PC通信

使用:

//-------------------------------------------------------------------------------------------
// main.c


void main_loop()
{
	char c[1]  = {0};
	while (1)
	{
		c[0] = XUartPs_RecvByte(XPAR_PS7_UART_1_BASEADDR);	//0xE0001000
		xil_printf("%c",c[0]);
	}
}


u8 XUartPs_RecvByte(u32 BaseAddress)
{
	u32 RecievedByte;
	/* Wait until there is data */
	while (!XUartPs_IsReceiveData(BaseAddress)) {
		;
	}
	RecievedByte = XUartPs_ReadReg(BaseAddress, XUARTPS_FIFO_OFFSET);
	/* Return the byte received */
	return (u8)RecievedByte;
}



