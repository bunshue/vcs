#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_UART.h"
#include "CS8963_Initial.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function UART
 * Filename: CS8963_UART.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/
void Initial_EUART2(ULONG BR, ULONG XTAL)
{
	ULONG ii;
	//ii= XTAL / BR;

	BR = 115200;
	XTAL = 16000000;
	ii = 139;

	IOCFGP0_6=b10000110;
	IOCFGP0_7=b10100000;
	MFCFGP0_6=b00100010;			//set p0.6 pin as TXD1
	MFCFGP0_7=b00100010;			//set P0.7 pin as RXD1
	
	SCON2=0xB0;						//enable EUART2 transmit and receive;The number of bits of a data byte is 8.
	LINSBRH = (ii >> 8)& 0xff;		//BUAD RATE = SYSCLK/BR[15-0]  SYSCLK:16Mhz	 BUAD RATE = 9600
	LINSBRL = ii & 0xff;			//BUAD RATE = SYSCLK/BR[15-0]  SYSCLK:16Mhz	 BUAD RATE = 9600
	LINCNTRH = (ii << 8)& 0xff;		//set timer limit for LCNTR[15-0]
	LINCNTRL = ii & 0xff;			//set timer limit for LCNTR[15-0]
	SFIFO2 = 0x01;					//RX FIFO trigger level=2;TX FIFO trigger level=3; 
	SFIFO2 = 0x68;
	SINT2 = 0xA0;					//enable UART2 interrupt; enable Transmit FIFO; enable Receive FIFO
	LINCTRL = 0x00;					//LIN Enable;Enable master LIN;Send Break;set Break Length
	LININT = 0X00;					//Set Break Completion Interrupt;set Receive Sync Completion Interrupt;set LIN Counter Overflow Interrupt
	LININTEN = 0x00;				//Disable all LIN INTERRUPT
	IE = IE |0x40;					//EUART interrupt enable	  
	EA = 1;							//global interrupt enable
}

void UART0_Send_1byte(unsigned char c)
{
	TI0 = 0;
	SBUF0 = c;
	while(!TI0)
	{
		;
	}
	TI0 = 0;
}

BYTE UART0_Receive_1byte(void)
{
	BYTE temp;

	RI0 = 0;
	while(!RI0)	;  //if RI=0, waiting
	temp = SBUF0 ;
	return temp;
}

void UART1_Send_1byte(BYTE send_byte)  // EUART function
{
	//SINT2 &= 0xfe;
	SINT2 = 0xa0;
	SBUF2 = send_byte;
	while(!(SINT2&0x01));
}

void EUART2_Send_4byte()
{
	unsigned char i;
	//tx2_request = 0;
	//tx2_not_finish = 1;
	for(i=0;i<=3;i++) SBUF2 = tx2_buf[i];
}

BYTE UART1_Receive_1byte(void)		   // EUART function
{
	BYTE temp;

	//SINT2 &= 0xdf;
	SINT2 = 0xc0;
	while(!(SINT2&0x20));  //if RI=0, waiting
	temp = SBUF2;
	return temp;
}
