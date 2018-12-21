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
BYTE TH1_tmp = 0;
BYTE TL1_tmp = 0;
BYTE TH3_tmp = 0;
BYTE TL3_tmp = 0;
BYTE TH4_tmp = 0;
BYTE TL4_tmp = 0;
BYTE TT5_tmp = 0;
BYTE TH5_tmp = 0;
BYTE TL5_tmp = 0;

#define PWM_CLOCK_SCALE	0

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
	WDCON = 0x01;         // reset watchdog timer 
	TA=0x00;
	WDCON = 0x02;        // - - - - WDIF WTRF EWT RWT
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
	DACL = dac&0xff;		// IDAC[7:0], bit 0~7 of 10 bit DAC date
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

void Setup_PWM_Initial(void)
{
	P1_0=1;					//CM2209A close AP
	P1_1=0;					//CM2209A close AN
	P1_4=1;					//CM2209A close BP
	P1_5=0;					//CM2209A Close BN
	P3_1=1;					//CM2209A close CP
	P3_0=0;					//CM2209A close CN
	MFCFGP1_0=0x01;IOCFGP1_0=PinC_InOutCMOS;	//Setup AP
	MFCFGP1_1=0x01;IOCFGP1_1=PinC_InOutCMOS;	//Setup AN
	MFCFGP1_4=0x01;IOCFGP1_4=PinC_InOutCMOS;	//Setup BP
	MFCFGP1_5=0x01;IOCFGP1_5=PinC_InOutCMOS;	//Setup BN
	IOCFGP3_1=PinC_InOutCMOS;  MFCFGP3_1=0x01;	//Setup CP
	IOCFGP3_0=PinC_InOutCMOS;  MFCFGP3_0=0x01;	//Setup CN
}

void Setup_PWM_Disable(void)
{
	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0

	P1_0=1;					//CM2209A close AP
	P1_1=0;					//CM2209A close AN
	P1_4=1;					//CM2209A close BP
	P1_5=0;					//CM2209A Close BN
	P3_1=1;					//CM2209A close CP
	P3_0=0;					//CM2209A close CN
}

void Setup_PWM_Parameter(BYTE PRDH, BYTE PRDL, BYTE pwmduty, BYTE deadtime, BYTE polarity)
{
	unsigned int pwm_a = 0;
	unsigned int pwm_b = 0;
	unsigned int pwm_c = 0;
	unsigned long pwmduty_tmp = 0;
	unsigned int pwmprd = (UINT)PRDH << 8 | (UINT)PRDL;
	unsigned char PWM_dead_time = deadtime;
	unsigned char PWM_polarity = polarity;

	if(pwmduty > 100)
		pwmduty = 100;

	printString("Setup_PWM_Parameter period = ");printd(pwmprd);printString(", duty = ");printd(pwmduty);printString("\n");
	printString("Setup_PWM_Parameter PWM_polarity = ");printd(PWM_polarity);printString("\n");

	pwmduty_tmp = (unsigned long)pwmprd*(100-pwmduty);
	pwmduty_tmp = pwmduty_tmp/100;

	pwm_a = pwmduty_tmp;
	pwm_b = pwmduty_tmp;
	pwm_c = pwmduty_tmp;

	PWMPRDH = 0x00;												//disable PWM16

	//DT[4:0] : PWM Output Rise Dead Time Delay
	//DT[4:0] = 01000 =>  8  => 1/16M*  8=0.5us
	//DT[4:0] = 11111 => 31 => 1/16M*31=1.94us

	PWM16CFG = PWM_CLOCK_SCALE<<5 | PWM_dead_time;				//PWMCLK = SYSCLK/(PWM_CLOCK_SCALE+1)

	PWMPRDL = (unsigned char)(pwmprd & 0x00ff);					//set PWMPRDH and PWMPRDL
	PWMPRDH = (unsigned char)((pwmprd & 0x7f00)>>8); 			//disable PWM16

	PWMAL = (unsigned char)(pwm_a & 0x00ff);					//the value of PWMA is less than PWMPRD
	PWMAH = ((unsigned char)((pwm_a & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMBL = (unsigned char)(pwm_b & 0x00ff);					//the value of PWMB is less than PWMPRD
	PWMBH = ((unsigned char)((pwm_b & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMCL = (unsigned char)(pwm_c & 0x00ff);					//the value of PWMc is less than PWMPRD
	PWMCH = ((unsigned char)((pwm_c & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWM16INT = 0x40;						  					//enable zero interrupt

	PWM16CHS = 0xF0 | PWM_polarity;
	//NEMG[1-0]	PEMG[1-0]	EMGF[1-0]	NPOL	PPOL
	//N outputs are forced to 1
	//P outputs are forced to 1

	PWMPRDH = ((unsigned char)((pwmprd & 0x7f00)>>8)) | 0x80;	//turn on PWM16
}

void Setup_PWM_ON_OFF(BYTE port_on)
{
	if((port_on>>5)&0x01)
	{
		printString("AP ON\n");
		MFCFGP1_0 = Hopen;	//AP
	}
	else
	{
		printString("AP OFF\n");
		MFCFGP1_0 = Close;	//AP
		P1_0=1;				//CM2209A close AP
	}

	if((port_on>>4)&0x01)
	{
		printString("AN ON\n");
		MFCFGP1_1 = Lopen;	//AN
	}
	else
	{
		printString("AN OFF\n");
		MFCFGP1_1 = Close;	//AN
		P1_1=0;				//CM2209A close AN
	}
	if((port_on>>3)&0x01)
	{
		printString("BP ON\n");
		MFCFGP1_4 = Hopen;	//BP
	}
	else
	{
		printString("BP OFF\n");
		MFCFGP1_4 = Close;	//BP
		P1_4=1;				//CM2209A close BP
	}
	if((port_on>>2)&0x01)
	{
		printString("BN ON\n");
		MFCFGP1_5 = Lopen;	//BN
	}
	else
	{
		printString("BN OFF\n");
		MFCFGP1_5 = Close;	//BN
		P1_5=0;				//CM2209A Close BN
	}
	if((port_on>>1)&0x01)
	{
		printString("CP ON\n");
		MFCFGP3_1 = Hopen;	//CP
	}
	else
	{
		printString("CP OFF\n");
		MFCFGP3_1 = Close;	//CP
		P3_1=1;				//CM2209A close CP
	}
	if((port_on>>0)&0x01)
	{
		printString("CN ON\n");
		MFCFGP3_0 = Lopen;	//CN
	}
	else
	{
		printString("CN OFF\n");
		MFCFGP3_0 = Close;	//CN
		P3_0=0;				//CM2209A close CN
	}
}

void Setup_PWM_Demo_Mode(unsigned char on_off)
{
	int i;
	if(on_off)
	{
		printString("[CS8963]: PWM Demo Mode........,  Use AP, AN, BP, BN, CP, CN, Press RESET to EXIT.\n");
		Setup_PWM_Initial();
		Setup_PWM_Parameter(0x01, 144, 10, 8, 0);

		Setup_PWM_ON_OFF(0x3f);	//Turn on all PWM channels

		while(1)
		{
			for(i=0;i<=100;i+=10)
			{
				Setup_PWM_Parameter(0x01, 144, i, 8, 0);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}

			Setup_PWM_Parameter(0x01, 144, 10, 8, 0);
			for(i=100;i<=1000;i+=100)
			{
				Setup_PWM_Parameter((i>>8)&0xff, i&0xff, 10, 8, 0);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
		}
	}
}

void Setup_CMP_Initial(BYTE pin, BYTE VTH)
{
	if(pin == 1)					//CMPA
	{
		IOCFGP2_7 = _ANEN_;				//Comparator A: ANEN
		MFCFGP2_7 = 0x80;				//enable Comparator A Input
	}
	else if(pin == 0)				//CMPA
	{
		IOCFGP3_3 = _ANEN_;	  			//Comparator A: ANEN
		MFCFGP3_3 = 0x80;				//enable Comparator A Input
	}
	else if(pin == 2)				//CMPB
	{
		IOCFGP2_6 = _ANEN_;				//Comparator B: ANEN
		MFCFGP2_6 = 0x80;				//enable Comparator B Input
	}
	else if(pin == 3)				//CMPC
	{
		IOCFGP2_5 = _ANEN_;				//Comparator C: ANEN
		MFCFGP2_5 = 0x80;				//enable Comparator C Input
	}
	else if(pin == 4)				//CMPD
	{
		IOCFGP2_4 = _ANEN_;				//Comparator D: ANEN
		MFCFGP2_4 = 0x80;				//enable Comparator D Input
	}
	else
	{
		printString("Illegal CMP port: ");printd(pin);printString("\n");
		return;
	}

	CMPST = 0x00;							//disable Comparator A/B/C/D Hysteresis
	DelayXms(4);							//delay
	CMPVTH1 = VTH;

	if((pin == 0) || (pin == 1))			//CMPA
	{
		CMPCFGAB |= B11100000;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
	}
	else if(pin == 2)						//CMPB
	{
		CMPCFGAB |= B00001110;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
	}
	else if(pin == 3)						//CMPC
	{
		CMPCFGCD |= B11100000;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
	}
	else if(pin == 4)						//CMPD
	{
		CMPCFGCD |= B00001110;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
	}
	CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
	DelayXms(1);							// delay as least 20us for the stabilization of comparator block, 258us
}

void Setup_CMP_Disable()
{
	CMP_EN = 0;
}

void PIN_CONFIG_setup_gpio(unsigned char pin)
{
	if(pin == _P0_1)
	{
		IOCFGP0_1=PinC_InOutCMOS;  	MFCFGP0_1=_GPIOEN_;
	}
	else if(pin == _P1_2)
	{
		IOCFGP1_2=PinC_InOutCMOS;  	MFCFGP1_2=_GPIOEN_;
	}
	else if(pin == _P1_3)
	{
		IOCFGP1_3=PinC_InOutCMOS;  	MFCFGP1_3=_GPIOEN_;
	}
	else if(pin == _P1_7)
	{
		IOCFGP1_7=PinC_InOutCMOS;  	MFCFGP1_7=_GPIOEN_;
	}
	else if(pin == _P3_3)
	{
		IOCFGP3_3=PinC_InOutCMOS;  	MFCFGP3_3=_GPIOEN_;
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}
}

void Setup_Timer_Initial(BYTE timer, BYTE TT, BYTE TH, BYTE TL)
{
	if((gui_cmd[4]>=0) && (gui_cmd[4]<=4))
	{
		printString("[CS8963]: TH = 0x");printx(TH);printString(", TL = 0x");printx(TL);printString("\n");
	}
	else if(gui_cmd[4]==5)
	{
		printString("[CS8963]: TT = 0x");printx(TT);printString(", TH = 0x");printx(TH);printString(", TL = 0x");printx(TL);printString("\n");
	}

	if(timer == 1)
	{
		//TMOD = (TMOD|0x10); //time0 mode1(16bit timer mode)
		TMOD=0x11;
		TCON &= 0x3f;
		CKCON &= ~0x10;		//T1CKDCTL, Timer 1 Clock Source Division Factor, 0:CPU/12, 1:CPU/4
		TH1 = TH;
		TL1 = TL;
		TH1_tmp = TH;
		TL1_tmp = TL;
	
		ET1 = 1;
		EA = 1;
	
		TR1 = 1; //run
	}
	else if(timer == 3)
	{
		EXIE = EXIE | 0x80;
		EA = 1;			             //Global Interrupt Enable bit.
	
		//TH4 : T4[15-8] TL4 :T4[7-0]
		T3L = TL;
		T3H = TH;
		TH3_tmp = TH;
		TL3_tmp = TL;
	
		//T34CON = TF4 TM4 TR4 T4IEN TF3 TM3  TR3 T3IEN
		T34CON |= 0x07;               //time4 (16bit timer mode)
	}
	else if(timer == 4)
	{
		unsigned char T4CON_tmp;
		EXIE = EXIE | 0x80;
		EA = 1;			             //Global Interrupt Enable bit.
		//TH4 : T4[15-8] TL4 :T4[7-0]
		T4L = TL;
		T4H = TH;
		TH4_tmp = TH;
		TL4_tmp = TL;
	
		//T34CON = TF4 TM4 TR4 T4IEN TF3 TM3  TR3 T3IEN
		//T34CON |= 0x70;               //time4 (16bit timer mode)
		T4CON_tmp = T34CON;
		T4CON_tmp |= 0x70;
		T34CON = T4CON_tmp;
	}
	else if(timer == 5)
	{
		EXIE = EXIE | 0x80;
		EA = 1;					//Global Interrupt Enable bit.
		RTCCMD = 0x00;
		PMR = 0x40;				//CD1=0 CD0=1 => full speed operation
		//TT5 : T5[23-16] TH5 : T5[15-8] TL5 :T5[7-0]		24bit counter value
		T5L = TL;
		T5H = TH;
		T5T = TT;
		TT5_tmp = TT;
		TH5_tmp = TH;
		TL5_tmp = TL;
	
		// T5CON : TF5 T5SEL[1] T5SEL[0] TM5 TR5  - -  T5IEN
		T5CON = 0x19;	//time5 (24bit timer mode)	0x19 iosc	0x39 XOSC	0x59 RTC	0x79 siosc
	}
	else
	{
		printString("[CS8963]: Unknown Timer : ");printd(timer);printString("\n");
	}
}

void Setup_Timer_Disable(BYTE timer)
{
	if(timer == 1)
	{
		TCON = (TCON &0xbf);		//TR1 = 0
	}
	else if(timer == 3)
	{
		T34CON = (T34CON & 0xf0);
	}
	else if(timer == 4)
	{
		T34CON = (T34CON & 0x0f);
	}
	else if(timer == 5)
	{
		T5CON = 0;
	}
	else
	{
		printString("[CS8963]: Unknown Timer : ");printd(timer);printString("\n");
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
	FLSHCMD = IFB_ByteRead;										//IFB read enable
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

	PIN_CONFIG_setup_gpio(_P1_3);		//For Timer1 P1.3 pin3
	PIN_CONFIG_setup_gpio(_P1_2);		//For Timer3 P1.2 pin4
	PIN_CONFIG_setup_gpio(_P0_1);		//For Timer4 P0.1 pin17
	PIN_CONFIG_setup_gpio(_P3_3);		//For Timer5 P3.3 pin22

	printString("\n");
	printString("[CS8963]: Reset\n");

	while(1)
	{
		DelayXms(100);
	}
}

void Comparator() interrupt 9
{
	/*
	CMPST &= ~INTflg_CMPA;				//clear ComparatorA flag
	if((CMPST & Output_CMPSTA) == 0x01)
	{
		printString("CMP A interrupt\n");
		CMPST =0x00;//clear all-INT flag
		if(flag_over_current_proction)
		 	OverCurrentProtection();
	}
	*/
      switch(CMPST & 0xF0)
      {
             case 0x10:
                   printS('A');
                   CMPST &= ~INTflg_CMPA;                                                                 //clear ComparatorA flag
                   //CMPCFGAB &= ~0x20;
                   break;
             case 0x20:
                   printS('B');
                   //CMPCFGAB &= ~0x02;
                   CMPST &= ~INTflg_CMPB;                                                                 //clear ComparatorB flag
                   break;
             case 0x40:
                   printS('C');
                   //CMPCFGCD &= ~0x20;
                   CMPST &= ~INTflg_CMPC;                                                                 //clear ComparatorC flag
                   break;
             case 0x80:
                   printS('D');
                   //CMPCFGCD &= ~0x02;
                   CMPST &= ~INTflg_CMPD;                                                                 //clear ComparatorD flag
                   break;
             default:
                   break;
     }  

	CMPST = 0x00;							//disable Comparator A/B/C/D Hysteresis
	//CMPCFGAB = B11100000;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
	// CMPST&= ~0xF0;
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
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x03))
			{
			 	if(gui_cmd[3] == 0x00)
				{
					printString("[CS8963]: Got command: Set PWM Initial cmd\n");
					Setup_PWM_Initial();
				}
				else if(gui_cmd[3] == 0x01)
				{
					printString("[CS8963]: Got command: Set PWM Disable cmd\n");
					Setup_PWM_Disable();
				}
				else if(gui_cmd[3] == 0x02)
				{
					printString("[CS8963]: Got command: Set PWM Parameter cmd\n");
					Setup_PWM_Parameter(gui_cmd[4], gui_cmd[5], gui_cmd[6], gui_cmd[7], gui_cmd[8]);
				}
				else if(gui_cmd[3] == 0x03)
				{
					printString("[CS8963]: Got command: Set PWM ON-OFF cmd\n");
					Setup_PWM_ON_OFF(gui_cmd[4]);
				}
				else if(gui_cmd[3] == 0x04)
				{
					printString("[CS8963]: Got command: Set PWM Demo Mode cmd\n");
					Setup_PWM_Demo_Mode(gui_cmd[4]);
				}
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x04))
			{
			 	if(gui_cmd[3] == 0x00)
				{
					printString("[CS8963]: Got command: Set CMP Initial cmd\n");
					Setup_CMP_Initial(gui_cmd[4], gui_cmd[5]);
				}
				else if(gui_cmd[3] == 0x01)
				{
					printString("[CS8963]: Got command: Set CMP Disable cmd\n");
					Setup_CMP_Disable();
				}
			}
			else if((gui_cmd[0] == 0xAA) && (gui_cmd[1] == 0x20) && (gui_cmd[2] == 0x05) && (gui_cmd[3] == 0x00))
			{
			 	if(gui_cmd[5] == 0x00)
				{
					if((gui_cmd[4]<0)||(gui_cmd[4]>5))
					{
						printString("[CS8963]: Stop Unknown Timer, ");printd(gui_cmd[4]);printString("\n");
					}
					else
					{
						printString("[CS8963]: Got command: Stop Timer cmd for Timer ");
						switch(gui_cmd[4])
						{
							case 1:
								printString("1, \n");
								Setup_Timer_Disable(gui_cmd[4]);
								break;
							case 3:
								printString("3, \n");
								Setup_Timer_Disable(gui_cmd[4]);
								break;
							case 4:
								printString("4, \n");
								Setup_Timer_Disable(gui_cmd[4]);
								break;
							case 5:
								printString("5, \n");
								Setup_Timer_Disable(gui_cmd[4]);
								break;
							default:
								printString("Unknown Timer\n");
								break;
					     }	
					 }
				}
				else if(gui_cmd[5] == 0x01)
				{
					if((gui_cmd[4]<0)||(gui_cmd[4]>5))
					{
						printString("[CS8963]: Start Unknown Timer, ");printd(gui_cmd[4]);printString("\n");
					}
					else
					{
						printString("[CS8963]: Got command: Start Timer cmd for Timer ");
						switch(gui_cmd[4])
						{
							case 1:
								printString("1, \n");
								Setup_Timer_Initial(gui_cmd[4],gui_cmd[6],gui_cmd[7],gui_cmd[8]);
								break;
							case 3:
								printString("3, \n");
								Setup_Timer_Initial(gui_cmd[4],gui_cmd[6],gui_cmd[7],gui_cmd[8]);
								break;
							case 4:
								printString("4, \n");
								Setup_Timer_Initial(gui_cmd[4],gui_cmd[6],gui_cmd[7],gui_cmd[8]);
								break;
							case 5:
								printString("5, \n");
								Setup_Timer_Initial(gui_cmd[4],gui_cmd[6],gui_cmd[7],gui_cmd[8]);
								break;
							default:
								printString("Unknown Timer\n");
								break;
					     }	
					 }
				}
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

void Timer0(void) interrupt 1					//50ms
{
	if(++tcount==2)
	{
		tcount=0;
		Send_ADC_Result_Cmd();
	}	
 	TH0 = 0x00;									//Timer 0 count start point
	TL0 = 0x00;	
}

void Timer1(void) interrupt 3
{
	P1_3 = ~P1_3;
	TH1 = TH1_tmp;								//Timer 1 count start point
	TL1 = TH1_tmp;
}

void Timer345_ISR(void) interrupt 14
{
	unsigned char T3CON_tmp;
	unsigned char T4CON_tmp;

	if((T34CON & 0x08)==0x08)
	{
		P1_2 = ~P1_2;
		T3H = TH3_tmp;							//Timer 3 count start point
		T3L = TL3_tmp;
		//T34CON &= 0xf7;						//time3 (16bit timer mode)
		T3CON_tmp = T34CON;
		T3CON_tmp &= 0xf7;
		T34CON = T3CON_tmp;
	}

	if((T34CON & 0x80)==0x80)
	{
		P0_1 = ~P0_1;
		T4L = TL4_tmp;							//Timer 4 count start point
		T4H = TH4_tmp;
		//T34CON &= 0x7f;						//time3 (16bit timer mode)
		T4CON_tmp = T34CON;
		T4CON_tmp &= 0x7f;
		T34CON = T4CON_tmp;
	}		 

	if((T5CON & 0x80)==0x80)
	{
		P3_3 = ~P3_3;
		//RTCCMD = 0x00;
		EXIF = 0x00;
		//one second
		T5L = TL5_tmp;		//Low
		T5H = TH5_tmp;		//Medium
		T5T = TT5_tmp;		//High
		T5CON = 0x19;		//time5 (24bit timer mode)	0x19 iosc	0x39 XOSC	0x59 RTC	0x79 siosc
	}
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

