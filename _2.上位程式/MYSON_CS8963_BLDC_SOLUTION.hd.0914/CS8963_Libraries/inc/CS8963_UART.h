#ifndef __CS8963_UART_H__
#define __CS8963_UART_H__
void Initial_EUART2(unsigned long BR, unsigned long XTAL);
void UART0_Send_1byte(unsigned char c);
BYTE UART0_Receive_1byte(void);
void UART1_Send_1byte(BYTE send_byte);
void EUART2_Send_4byte();
BYTE UART1_Receive_1byte(void);
#endif


