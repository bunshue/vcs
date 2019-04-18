#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"

#define UART_BUF_LENGTH 10
BYTE gui_cmd[UART_BUF_LENGTH] = 0;
BYTE gui_cmd_index = 0;
BYTE tcount = 0;
UINT ADC_A_InstanceCurrent = 0;
UINT ADC_A_InstanceCurrent_result = 0;
UINT CalcCheckSum(UINT *pData, UINT len);
void Send_ADC_Result_Cmd();

void Initial_Timer0(void)
{
	TL0 = 0x00;
	TH0 = 0x00;
	CKCON &= ~0x08;		//T0CKDCTL, Timer 0 Clock Source Division Factor, 0:CPU/12, 1:CPU/4
	//TMOD = (TMOD|0x01); //time0 mode1(16bit timer mode)
	//TMOD=0x21;
	TMOD=0x11;

	TCON &=0xcf;					//	TF1	TR1	TF0	TR0	:	IE1	IT1	IE0	IT0
	ET0 = 1;						//Timer 0 Interrupt Enable bit
	TR0=1;						//Timer 0 Run Control bit. Set to enable Timer 0
	PT0 = 0;					//Timer 0 Priority bit, 0: low, 1: high
}

void Timer0_Close(void)
{
	TCON = (TCON &0xEf);   // this is timer 0 && timer 1	 stop
}

void printS(unsigned char p)
{
	ES0 = 0;
	SBUF0 = p;
	while (!TI0);
	TI0 = 0;
	ES0 = 1;
}

void printString(unsigned char* p)
{
	int len=0;
	while(1)
	{
		if(p[len]=='\0')
			break;
		if(p[len]=='\n')
		{
			printS(0x0a);
		}
		else
		{
			printS(p[len]);
		}
		len++;
	}
}

void Reset_system(void)
{
	//printString("[CS8963]: RESET\n");
	TA=0xAA;
	TA=0x55;
	WDCON = 0x01;			//reset watchdog timer
	TA=0x00;
	WDCON = 0x02;			//WDIF WTRF EWT RWT
	CKCON &= ~0xC7;
}

void Initial_ADC_A(void)
{
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;

	IOCFGP0_5 = _ANEN_;				//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;			//ADC A2 for instantaneous current
	ADCCFG = b10000001;				//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);					//wait until ADC is stable

	ADCAVG = 0;						//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_A_EN;		//select A channel
	ADCCHSL =ADCCHSL_tmp;
}

void Disable_ADC_A()
{
	ADCCHSL &= ~ADC_A_EN;
	IOCFGP0_5 = B00000000;			//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;			//ADC A3 for instantaneous current
}

unsigned int Get_ADC_A_Result(void)
{
	unsigned int ah = 0;
	unsigned int al = 0;
	ADCCFG = b10110001;				//Start convertion
	while(ADCCFG&0x10);				//Waiting for conversion finish

	ADC_A_InstanceCurrent = 0;

	if(ADCCHSL&ADC_A_IF)
	{
		ADC_A_InstanceCurrent = (ADCAH*256 + ADCAL);
	}
	return ADC_A_InstanceCurrent;
}

void DelayXms(unsigned char delay )
{
	unsigned char i,j;
 	for(i=0;i<delay;i++)
		for(j=0;j<100;j++)
			;
}

void Initial_REGTRM(unsigned char regtrm)						//Initial REGTRM
{
	TB = 0xAA;
	TB = 0x55;
	REGTRM = regtrm;
   	TB = 0x00;
}

unsigned char IFB_Read_1Byte(unsigned char ADD)					//IFB Read byte
{
	unsigned char IFB_DAT;

	TB = 0xAA;
	TB = 0x55;
	FLSHADH = 0x00;
	FLSHADL = ADD;
	FLSHCMD = IFB_ByteRead;					//IFB read enable
	TB = 0x00;

	TB = 0xAA;
	TB = 0x55;
	IFB_DAT = FLSHDAT;
	TB = 0x00;

	return IFB_DAT;
}

void Initial_IOSC(unsigned char ITRM, unsigned char VTRM)	 	//Initial IOSC
{
  	TB = 0xAA;
  	TB = 0x55;
  	IOSCITRM = ITRM;
  	TB = 0x00;

  	DelayXms(10);

  	TB = 0xAA;
  	TB = 0x55;
  	IOSCVTRM = VTRM;
	CKSEL = 0xf0;	 		//select iosc, set Wakeup Delay Timer = 0xf, 196 IOSC cycle
  	TB = 0x00;
}

void Initial_UART0(unsigned long BR, unsigned long XTAL)
{
    IOCFGP0_6=b00000110;	//output CMOS push-pull	(TXD0)
	IOCFGP0_7=b10100000;	//input pull up			(RXD0)
	MFCFGP0_6=b00010000;	//UART0 TXD0
	MFCFGP0_7=b00010000;	//UART0 RXD0

	SCON0 = 0x52;
	TMOD |= 0x20;			//time1 mode2(8bit auto reload mode)
	PCON = PCON|0x80;		//smod0 = 1

	T2CON = 0x34;
	TL2 = RLDL = 65536-(XTAL/32/BR);      	// init value
	TH2 = RLDH =(65536-(XTAL/32/BR))>>8;    // init value

	ES0 = 1; 				//UART0 interrupt enable
	ET2=1;
}

void main(void)
{
	EWT = 0;
	WTST = 0;													//Wait state cycle = 1
	EA = 1;														//Enable interrupt

 	Initial_REGTRM(IFB_Read_1Byte(0x20));						//Initial IOSC:
	Initial_IOSC(IFB_Read_1Byte(0x21), IFB_Read_1Byte(0x22));	//Default IOSC: 16MHz	
	Initial_UART0(9600,iSYSCLK);								//Initial UART0

	printString("\n");
	printString("[CS8963]: Reset\n");

	while(1)
	{
		DelayXms(100);
	}
}

void UART0_SP(void) interrupt 4
{
	unsigned char SBUF0_temp;
	if(RI0 == 1)
	{
		RI0 = 0;
		SBUF0_temp = SBUF0;

		if(SBUF0_temp == 0xAA)
			gui_cmd_index = 0;

		gui_cmd[gui_cmd_index] = SBUF0_temp;

		if(gui_cmd_index == 0)
		{
			if(SBUF0_temp == 0xAA)	//Check Header
				gui_cmd_index++;
			else
				gui_cmd_index = 0;
		}
		else
			gui_cmd_index++;

		if (gui_cmd_index == UART_BUF_LENGTH)
		{
			gui_cmd_index = 0;
			if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x00) && (gui_cmd[3] == 0x00))
			{
				printString("[CS8963]: Got command: Reset\n");
				Reset_system();					//Reset Demo Board
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x01) && (gui_cmd[3] == 0x00))
			{
				printString("[CS8963]: Got command: Initial\n");
				Initial_ADC_A();				//Initial ADC A channel for VR control
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x01) && (gui_cmd[3] == 0x01))
			{
				printString("[CS8963]: Got command: Disable\n");
				Disable_ADC_A();
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x01) && (gui_cmd[3] == 0x02))
			{
				printString("[CS8963]: Got command: Read\n");
				Initial_Timer0();				//Initial Timer0
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x01) && (gui_cmd[3] == 0x03))
			{
				printString("[CS8963]: Got command: Stop reading ADC\n");
				Timer0_Close();					//Disable Timer0
			}
		}
	}
	else  if(TI0==1)	//Transmit Interrupt Flag bit, CS8963 to computer
	{
		TI0=0;
	}
}

///**************************************************************************
// * 函數名：CalcCheSun()
// * 功  能：計算數據校驗和
// * 輸  入：數組，計算數據長度
// * 輸  出：返回校驗和的低8位
// *************************************************************************/
UINT CalcCheckSum(UINT *pData, UINT len)
{
    unsigned char i = 0,sum = 0;
    for (; i < len; i++)
    {
        sum += (unsigned char) pData[i];
    }
    sum = (sum^0xFF) + 1;
    return (sum&0xFF);
}

void Timer0(void) interrupt 1	    // 50ms
{
	if(++tcount==2)
	{
		tcount=0;
		Send_ADC_Result_Cmd();
	}	
 	TH0 = 0x00;						//Timer 0 count start point
	TL0 = 0x00;	
}

void Send_ADC_Result_Cmd()
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	Get_ADC_A_Result();

	UartTxBuf[0] = 0x55;
	UartTxBuf[1] = 0x20;
	UartTxBuf[2] = 0x01;
	UartTxBuf[3] = ADCAH;
	UartTxBuf[4] = ADCAL;
	UartTxBuf[5] = 0;
	UartTxBuf[6] = 0;
	UartTxBuf[7] = 0;
	UartTxBuf[8] = 0;
	UartTxBuf[9] = CalcCheckSum(UartTxBuf, 9);
	for(i=0;i<UART_BUF_LENGTH;i++)
		printS(UartTxBuf[i]);
}

