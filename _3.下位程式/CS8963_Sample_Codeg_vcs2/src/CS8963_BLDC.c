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

void DelayXms(unsigned char delay )
{
	unsigned char i,j;
	for(i=0;i<delay;i++)
		for(j=0;j<100;j++)
			;
}

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

void printd(unsigned long value)
{
	if(value>=100000000)
		printS('X');
	if(value>=10000000)
		printS(((value/10000000)%10)+0x30);
	if(value>=1000000)
		printS(((value/1000000)%10)+0x30);
	if(value>=100000)
		printS(((value/100000)%10)+0x30);
	if(value>=10000)
		printS(((value/10000)%10)+0x30);
	if(value>=1000)
		printS(((value/1000)%10)+0x30);
	if(value>=100)
		printS(((value/100)%10)+0x30);
	if(value>=10)
		printS(((value/10)%10)+0x30);
	printS(((value)%10)+0x30);
}

void printx(unsigned int value)
{
        unsigned int quotient;
        char hexadecimalNumber[100];
        int i=1,j,temp;
        quotient = value;

	if(value<16)
		printS('0');

        while(quotient!=0){
        temp = quotient % 16;

        //To convert integer into character
        if( temp < 10)
                temp =temp + 48;
        else
                temp = temp + 55;

        hexadecimalNumber[i++]= temp;
        quotient = quotient / 16;
        }

        for(j = i -1 ;j> 0;j--)
			printS(hexadecimalNumber[j]);
	if(value==0)
		printS('0');
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

void PIN_CONFIG_setup_dac(unsigned char pin)
{
	if(pin == _P1_7)
	{
		IOCFGP1_7 = PinC_Analog;
		MFCFGP1_7 = b10000000;
	}
	else if(pin == _P2_2)
	{
		IOCFGP2_2 = PinC_Analog;
		MFCFGP2_2 = b10000000;
	}
	else if(pin == _P3_2)
	{
		IOCFGP3_2 = PinC_Analog;
		MFCFGP3_2 = b10000000;
	}
	else
	{
		printString("Illegal DAC port: ");printd(pin);printString("\n");
	}
}

void PIN_CONFIG_disable_dac(unsigned char pin)
{
	pin = 0;

}

void Setup_DAC_Data(unsigned char DH, unsigned char DL)
{
	DACH = DH;		// just update bit [1:0] for DAC bit[9-8]
	DACL = DL;		// IDAC[7:0], bit 0~7 of 10 bit DAC date
					// low byte data should update later
	DACH |= 0x80;	// Enable DAC
}

void Setup_DAC_Voltage(unsigned int minivolt)
{
	ULONG dac;
	dac = 1023*(ULONG)minivolt/5000;

	DACH = (dac>>8)&0xff;	// just update bit [1:0] for DAC bit[9-8]
	DACL = dac&0xff;			// IDAC[7:0], bit 0~7 of 10 bit DAC date
							// low byte data should update later
	DACH |= 0x80;			// Enable DAC
}

void Setup_DAC_Demo_Mode(unsigned char on_off)
{
	int i;
	unsigned int DAC_data = 0;
	if(on_off)
	{
		printString("[CS8963]: DAC Demo Mode........,  Use P1.7_pin1, P2.2_pin29, P3.2_pin23, Press RESET to EXIT.\n");
		IOCFGP1_7 = PinC_Analog;
		MFCFGP1_7 = b10000000;
		IOCFGP2_2 = PinC_Analog;
		MFCFGP2_2 = b10000000;
		IOCFGP3_2 = PinC_Analog;
		MFCFGP3_2 = b10000000;
		while(1)
		{
			for(i=0;i<20;i++)
			{
				DAC_data=i*51;printd(DAC_data);printS(' ');Setup_DAC_Data(DAC_data>>8,DAC_data&0xff);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
			for(i=0;i<51;i++)
			{
				printd(i*100);printS(' ');Setup_DAC_Voltage(i*100);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
		}
	}
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
	unsigned int mV;

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
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x02) && (gui_cmd[3] == 0x00))
			{
				printString("[CS8963]: Got command: Initial DAC cmd, use ");
				if(gui_cmd[4] == 0)
				{
					printString("pin 1_P1.7\n");
					PIN_CONFIG_setup_dac(_P1_7);
				}
				else if(gui_cmd[4] == 1)
				{
					printString("pin 23_P3.2\n");
					PIN_CONFIG_setup_dac(_P3_2);
				}
				else if(gui_cmd[4] == 2)
				{
					printString("pin 29_P2.2\n");
					PIN_CONFIG_setup_dac(_P2_2);
				}
				else
					printString("Illegal DAC port.");
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x02) && (gui_cmd[3] == 0x01))
			{
				printString("[CS8963]: Got command: Disable DAC cmd, disable ");
				if(gui_cmd[4] == 0)
				{
					printString("pin 1_P1.7\n");
					PIN_CONFIG_disable_dac(_P1_7);
				}
				else if(gui_cmd[4] == 1)
				{
					printString("pin 23_P3.2\n");
					PIN_CONFIG_disable_dac(_P3_2);
				}
				else if(gui_cmd[4] == 2)
				{
					printString("pin 29_P2.2\n");
					PIN_CONFIG_disable_dac(_P2_2);
				}
				else
					printString("Illegal DAC port.");
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x02) && (gui_cmd[3] == 0x02))
			{
				printString("[CS8963]: Got command: Set DAC Data cmd, data: 0x ");
				printx(gui_cmd[5]);printS(' ');printx(gui_cmd[6]);printString("\n");
				Setup_DAC_Data(gui_cmd[5],gui_cmd[6]);
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x02) && (gui_cmd[3] == 0x03))
			{
				mV = gui_cmd[5] << 8 | gui_cmd[6];
				printString("[CS8963]: Got command: Set DAC Voltage cmd, voltage: ");printd(mV);printString(" mV\n");
				Setup_DAC_Voltage(mV);
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x02) && (gui_cmd[3] == 0x04))
			{
				printString("[CS8963]: Got command: Set DAC Demo Mode cmd\n");
				Setup_DAC_Demo_Mode(gui_cmd[4]);
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

