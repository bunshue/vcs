#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_Setup.h"
#include "CS8963_Function.h"
#include "CS8963_Config.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : Pin Config Function
 * Filename: CS8963_Config.C
 * Author  :
 * Date    : 2015/01/15
 **********************************************************/

void PIN_CONFIG_setup_pwmap(unsigned char pin)
{
	if(pin == _P1_0)
	{
		IOCFGP1_0=PinC_InOutCMOS;  MFCFGP1_0=0x01;		//PWMAP
		P1_0=0;				   //PWMAP close H
	}
	else if(pin == _P1_2)
	{
		IOCFGP1_2=PinC_InOutCMOS;  MFCFGP1_2=0x01;		//PWMAP
		P1_2=0;				   //PWMAP close H
	}
	else
	{
		printString("WRONG01\n");
	}
}

void PIN_CONFIG_setup_pwman(unsigned char pin)
{
	if(pin == _P1_1)
	{
		IOCFGP1_1 = PinC_InOutCMOS;  MFCFGP1_1=0x01;		//PWMAN
		IOCFGP1_1 = b00000110;	 	//PWMAN   output,open L,charge
		MFCFGP1_1 = b00100000;	 	//enable PWM16 Channel A negative output
	}
	else if(pin == _P1_3)
	{
		IOCFGP1_3 = PinC_InOutCMOS;  MFCFGP1_3=0x01;		//PWMAN
		IOCFGP1_3 = b00000110;	 	//PWMAN   output,open L,charge
		MFCFGP1_3 = b00100000;	 	//enable PWM16 Channel A negative output
	}
	else
	{
		printString("WRONG02\n");
	}
}

void PIN_CONFIG_setup_pwmbp(unsigned char pin)
{
	if(pin == _P1_4)
	{
		IOCFGP1_4=PinC_InOutCMOS;  MFCFGP1_4=0x01;		//PWMBP
		P1_4=0;				//PWMBP close H
	}
	else if(pin == _P1_6)
	{
		IOCFGP1_6=PinC_InOutCMOS;  MFCFGP1_6=0x01;		//PWMBP
		P1_6=0;				//PWMBP close H
	}
	else
	{
		printString("WRONG03\n");
	}
}

void PIN_CONFIG_setup_pwmbn(unsigned char pin)
{
	if(pin == _P1_5)
	{
		IOCFGP1_5=PinC_InOutCMOS;  MFCFGP1_5=0x01;		//PWMBN
		IOCFGP1_5 = b00000110;	 	//PWMBN   output
		MFCFGP1_5 = b00100000;	 	//enable PWM16 Channel B negative output
	
	}
	else if(pin == _P1_7)
	{
		IOCFGP1_7=PinC_InOutCMOS;  MFCFGP1_7=0x01;		//PWMBN
		IOCFGP1_7 = b00000110;	 	//PWMBN   output
		MFCFGP1_7 = b00100000;	 	//enable PWM16 Channel B negative output
	}
	else
	{
		printString("WRONG04\n");
	}
}

void PIN_CONFIG_setup_pwmcp(unsigned char pin)
{
	if(pin == _P3_1)
	{
		IOCFGP3_1=PinC_InOutCMOS;  MFCFGP3_1=0x01;		//PWMCP
		P3_1=0; 			 //PWMCP close H
	}
	else if(pin == _P2_4)
	{
		IOCFGP2_4=PinC_InOutCMOS;  MFCFGP2_4=0x01;		//PWMCP
		P2_4=0; 			 //PWMCP close H
	}
	else
	{
		printString("WRONG05\n");
	}
}

void PIN_CONFIG_setup_pwmcn(unsigned char pin)
{
	if(pin == _P3_0)
	{
		IOCFGP3_0=PinC_InOutCMOS;  MFCFGP3_0=0x01;		//PWMCN
		IOCFGP3_0 = b00000110;	 	//PWMCN   output
		MFCFGP3_0 = b00100000;	 	//enable PWM16 Channel C negative output
	}
	else if(pin == _P2_5)
	{
		IOCFGP2_5=PinC_InOutCMOS;  MFCFGP2_5=0x01;		//PWMCN
		IOCFGP2_5 = b00000110;	 	//PWMCN   output
		MFCFGP2_5 = b00100000;	 	//enable PWM16 Channel C negative output
	}
	else
	{
		printString("WRONG06\n");
	}
}

void PIN_CONFIG_setup_xemg(unsigned char pin, unsigned char select)
{
	if(pin == _P0_5)
	{
		//------------------XEMG use pin13_P0.5-----------------
		MFCFGP0_5 = b00100000;			//enable XEMG
		if(select == 0)
			IOCFGP0_5 = b10010000;		//input pull up	(FLTA)  IPOL = 0
		else
			IOCFGP0_5 = b10010001;		//input pull up	(FLTA)  IPOL = 1
		//PDEN(pull down enable, bit 4) = 1, pull down
	}
	else if(pin == _P2_2)
	{
		//------------------XEMG use pin29_P2.2-----------------
		MFCFGP2_2 = b00100000;			//enable XEMG
		if(select == 0)
			IOCFGP2_2 = b10010000;		//input pull up	(FLTA)  IPOL = 0
		else
			IOCFGP2_2 = b10010001;		//input pull up	(FLTA)  IPOL = 1
		//PDEN(pull down enable, bit 4) = 1, pull down
	}
	else if(pin == _P2_3)
	{
		//------------------XEMG use pin28_P2.3-----------------
		MFCFGP2_3 = b00100000;			//enable XEMG
		if(select == 0)
			IOCFGP2_3 = b10010000;		//input pull up	(FLTA)  IPOL = 0
		else
			IOCFGP2_3 = b10010001;		//input pull up	(FLTA)  IPOL = 1
		//PDEN(pull down enable, bit 4) = 1, pull down
	}
	else if(pin == _P2_7)
	{
		//------------------XEMG use pin24_P2.7-----------------
		MFCFGP2_7 = b00100000;			//enable XEMG
		if(select == 0)
			IOCFGP2_7 = b10010000;		//input pull up	(FLTA)  IPOL = 0
		else
			IOCFGP2_7 = b10010001;		//input pull up	(FLTA)  IPOL = 1
		//PDEN(pull down enable, bit 4) = 1, pull down
	}
	else
	{
		printString("XEMG WRONG pin = ");printd(pin);printString("\n");
		return;
	}

	PWM16EMG = b10010000;
	//1. if PWM count (PWMPRDH bit 7=0) disable this register will be clear (PWM16EMG = 0)
	//2. if do'nt use interrupt only set MFCFGPx_y bit 5
	//3. bit 7 :interrupt enable bit 
}

void PIN_CONFIG_setup_hallsensor_a(unsigned char pin)
{
	pin=0;
	//TBD
}

void PIN_CONFIG_setup_hallsensor_b(unsigned char pin)
{
	pin=0;
	//TBD
}

void PIN_CONFIG_setup_hallsensor_c(unsigned char pin)
{
	pin=0;
	//TBD
}

void PIN_CONFIG_setup_i2c_scl(unsigned char pin)
{
	pin=0;
	//TBD
}

void PIN_CONFIG_setup_i2c_sda(unsigned char pin)
{
	pin=0;
	//TBD
}

void PIN_CONFIG_setup_uart_rxd(unsigned char pin)
{
	if(pin == _P0_7)
	{
		IOCFGP0_7 = b10100000;  			//input only(RXD0)
		MFCFGP0_7 = b00010000;  			//UART0 RXD0	ENABLE
	}
	else
	{
		printString("WRONG07\n");
	}
}

void PIN_CONFIG_setup_uart_txd(unsigned char pin)
{
	if(pin == _P0_6)
	{
		IOCFGP0_6 = b00000110;  			//CMOS output(TXD0)
		MFCFGP0_6 = b00010000;  			//UART0 TXD0	ENABLE
	}
	else
	{
		printString("WRONG08\n");
	}
}

void PIN_CONFIG_setup_euart2_rxd(unsigned char pin)
{
	if(pin == _P0_7)
	{
		IOCFGP0_7 = b10100000;  			//input only(RXD2)
		MFCFGP0_7 = b00010000;  			//EUART2 RXD2	ENABLE
	}
	else if(pin == _P2_3)
	{
		IOCFGP2_3 = b10100000;  			//input only(RXD2)
		MFCFGP2_3 = b00010000;  			//EUART2 RXD2	ENABLE
	}
	else if(pin == _P3_3)
	{
		IOCFGP3_3 = b10100000;  			//input only(RXD2)
		MFCFGP3_3 = b00010000;  			//EUART2 RXD2	ENABLE
	}
	else
	{
		printString("WRONG09\n");
	}
}

void PIN_CONFIG_setup_euart2_txd(unsigned char pin)
{
	if(pin == _P0_6)
	{
		IOCFGP0_6 = b00000110;  			//CMOS output(TXD2)
		MFCFGP0_6 = b00010000;  			//EUART2 TXD2	ENABLE
	}
	else if(pin == _P2_2)
	{
		IOCFGP2_2 = b00000110;  			//CMOS output(TXD2)
		MFCFGP2_2 = b00010000;  			//EUART2 TXD2	ENABLE
	}
	else if(pin == _P3_2)
	{
		IOCFGP3_2 = b00000110;  			//CMOS output(TXD2)
		MFCFGP3_2 = b00010000;  			//EUART2 TXD2	ENABLE
	}
	else
	{
		printString("WRONG10\n");
	}
}

void PIN_CONFIG_setup_adc(unsigned char pin)
{
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;

	if(pin == _P0_0)					//ADA2
	{
		IOCFGP0_0 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_0 = PinC_In;			//ADC A2 for instantaneous current
	}
	else if(pin == _P0_2)				//ADA1
	{
		IOCFGP0_2 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_2 = PinC_In;			//ADC A1 for instantaneous current
	}
	else if(pin == _P0_5)				//ADA3
	{
		IOCFGP0_5 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_5 = PinC_In;			//ADC A3 for instantaneous current
	}
	else if(pin == _P0_1)				//ADB2
	{
		IOCFGP0_1 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_1 = PinC_In;			//ADC B2 for instantaneous current
	}
	else if(pin == _P0_3)				//ADB1
	{
		IOCFGP0_3 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_3 = PinC_In;			//ADC B1 for instantaneous current
	}
	else if(pin == _P0_4)				//ADB3
	{
		IOCFGP0_4 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_4 = PinC_In;			//ADC B1 for instantaneous current
	}
	else if(pin == _P0_6)				//ADC2
	{
		IOCFGP0_6 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_6 = PinC_In;			//ADC C2 for instantaneous current
	}
	else if(pin == _P0_7)				//ADD2
	{
		IOCFGP0_7 = _ANEN_;			//Enable Anolog MUX
		MFCFGP0_7 = PinC_In;			//ADC D2 for instantaneous current
	}
	else if(pin == _P1_0)				//ADD3
	{
		IOCFGP1_0 = _ANEN_;			//Enable Anolog MUX
		MFCFGP1_0 = PinC_In;			//ADC D3 for instantaneous current
	}
	else if(pin == _P1_1)				//ADD4
	{
		IOCFGP1_1 = _ANEN_;			//Enable Anolog MUX
		MFCFGP1_1 = PinC_In;			//ADC D4 for instantaneous current
	}
	else if(pin == _P1_2)				//ADD7
	{
		IOCFGP1_2 = _ANEN_;			//Enable Anolog MUX
		MFCFGP1_2 = PinC_In;			//ADC D7 for instantaneous current
	}
	else if(pin == _P1_3)				//ADD8
	{
		IOCFGP1_3 = _ANEN_;			//Enable Anolog MUX
		MFCFGP1_3 = PinC_In;			//ADC D8 for instantaneous current
	}
	else if(pin == _P1_6)				//ADD9
	{
		IOCFGP1_6 = _ANEN_;			//Enable Anolog MUX
		MFCFGP1_6 = PinC_In;			//ADC D9 for instantaneous current
	}
	else if(pin == _P3_0)				//ADD5
	{
		IOCFGP3_0 = _ANEN_;			//Enable Anolog MUX
		MFCFGP3_0 = PinC_In;			//ADC D5 for instantaneous current
	}
	else if(pin == _P3_1)				//ADD6
	{
		IOCFGP3_1 = _ANEN_;			//Enable Anolog MUX
		MFCFGP3_1 = PinC_In;			//ADC D6 for instantaneous current
	}
	else
	{
		printString("Illegal ADC port: ");printd(pin);printString("\n");
		return;
	}

	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);					//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  				//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	if((pin == _P0_0)||(pin == _P0_2)||(pin == _P0_5))	//select A channel
		ADCCHSL_tmp |= ADC_A_EN;
	else if((pin == _P0_1)||(pin == _P0_3)||(pin == _P0_4))	//select B channel
		ADCCHSL_tmp |= ADC_B_EN;
	else if(pin == _P0_6)									//select C channel
		ADCCHSL_tmp |= ADC_C_EN;
	else if((pin == _P0_7)||(pin == _P1_0)||(pin == _P1_1)||(pin == _P1_2)||(pin == _P1_3)||(pin == _P1_6)||(pin == _P3_0)||(pin == _P3_1))	//select D channel
		ADCCHSL_tmp |= ADC_D_EN;
	else
	{
		printString("Illegal ADC port: ");printd(pin);printString("\n");
		return;
	}
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);
}

void PIN_CONFIG_setup_cmp(BYTE pin, BYTE VTH, BYTE enable)
{
	if(enable == 0)
	{
		CMP_EN = 0;
		if((pin == _P2_7) || (pin == _P3_3))	//CMPA
		{
			CMPCFGAB &= B00011111;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		else if(pin == _P2_6)					//CMPB
		{
			CMPCFGAB &= B11110001;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		else if(pin == _P2_5)					//CMPC
		{
			CMPCFGCD &= B00011111;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		else if(pin == _P2_4)					//CMPD
		{
			CMPCFGCD &= B11110001;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
	}
	else
	{
		if(pin == _P2_7)					//CMPA
		{
			IOCFGP2_7 = _ANEN_;				//Comparator A: ANEN
			MFCFGP2_7 = 0x80;				//enable Comparator A Input
		}
		else if(pin == _P3_3)				//CMPA
		{
			IOCFGP3_3 = _ANEN_;	  			//Comparator A: ANEN
			MFCFGP3_3 = 0x80;				//enable Comparator A Input
		}
		else if(pin == _P2_6)				//CMPB
		{
			IOCFGP2_6 = _ANEN_;				//Comparator B: ANEN
			MFCFGP2_6 = 0x80;				//enable Comparator B Input
		}
		else if(pin == _P2_5)				//CMPC
		{
			IOCFGP2_5 = _ANEN_;				//Comparator C: ANEN
			MFCFGP2_5 = 0x80;				//enable Comparator C Input
		}
		else if(pin == _P2_4)				//CMPD
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

		if((pin == _P2_7) || (pin == _P3_3))	//CMPA
		{
			CMPCFGAB |= B11100000;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		else if(pin == _P2_6)					//CMPB
		{
			CMPCFGAB |= B00001110;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		else if(pin == _P2_5)					//CMPC
		{
			CMPCFGCD |= B11100000;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		else if(pin == _P2_4)					//CMPD
		{
			CMPCFGCD |= B00001110;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		}
		CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
		DelayXms(1);							// delay as least 20us for the stabilization of comparator block, 258us
	}
}

void PIN_CONFIG_setup_gpio(unsigned char pin)
{
	if(pin == _P0_0)
	{
		IOCFGP0_0=PinC_InOutCMOS;  	MFCFGP0_0=_GPIOEN_;
	}
	else if(pin == _P0_1)
	{
		IOCFGP0_1=PinC_InOutCMOS;  	MFCFGP0_1=_GPIOEN_;
	}
	else if(pin == _P0_2)
	{
		IOCFGP0_2=PinC_InOutCMOS;  	MFCFGP0_2=_GPIOEN_;
	}
	else if(pin == _P0_3)
	{
		IOCFGP0_3=PinC_InOutCMOS;  	MFCFGP0_3=_GPIOEN_;
	}
	else if(pin == _P0_4)
	{
		IOCFGP0_4=PinC_InOutCMOS;  	MFCFGP0_4=_GPIOEN_;
	}
	else if(pin == _P0_5)
	{
		IOCFGP0_5=PinC_InOutCMOS;  	MFCFGP0_5=_GPIOEN_;
	}
	else if(pin == _P0_6)
	{
		IOCFGP0_6=PinC_InOutCMOS;  	MFCFGP0_6=_GPIOEN_;
	}
	else if(pin == _P0_7)
	{
		IOCFGP0_7=PinC_InOutCMOS;  	MFCFGP0_7=_GPIOEN_;
	}
	else if(pin == _P1_0)
	{
		IOCFGP1_0=PinC_InOutCMOS;  	MFCFGP1_0=_GPIOEN_;
	}
	else if(pin == _P1_1)
	{
		IOCFGP1_1=PinC_InOutCMOS;  	MFCFGP1_1=_GPIOEN_;
	}
	else if(pin == _P1_2)
	{
		IOCFGP1_2=PinC_InOutCMOS;  	MFCFGP1_2=_GPIOEN_;
	}
	else if(pin == _P1_3)
	{
		IOCFGP1_3=PinC_InOutCMOS;  	MFCFGP1_3=_GPIOEN_;
	}
	else if(pin == _P1_4)
	{
		IOCFGP1_4=PinC_InOutCMOS;  	MFCFGP1_4=_GPIOEN_;
	}
	else if(pin == _P1_5)
	{
		IOCFGP1_5=PinC_InOutCMOS;  	MFCFGP1_5=_GPIOEN_;
	}
	else if(pin == _P1_6)
	{
		IOCFGP1_6=PinC_InOutCMOS;  	MFCFGP1_6=_GPIOEN_;
	}
	else if(pin == _P1_7)
	{
		IOCFGP1_7=PinC_InOutCMOS;  	MFCFGP1_7=_GPIOEN_;
	}
	else if(pin == _P2_0)
	{
		IOCFGP2_0=PinC_InOutCMOS;  	MFCFGP2_0=_GPIOEN_;
	}
	else if(pin == _P2_1)
	{
		IOCFGP2_1=PinC_InOutCMOS;  	MFCFGP2_1=_GPIOEN_;
	}
	else if(pin == _P2_2)
	{
		IOCFGP2_2=PinC_InOutCMOS;  	MFCFGP2_2=_GPIOEN_;
	}
	else if(pin == _P2_3)
	{
		IOCFGP2_3=PinC_InOutCMOS;  	MFCFGP2_3=_GPIOEN_;
	}
	else if(pin == _P2_4)
	{
		IOCFGP2_4=PinC_InOutCMOS;  	MFCFGP2_4=_GPIOEN_;
	}
	else if(pin == _P2_5)
	{
		IOCFGP2_5=PinC_InOutCMOS;  	MFCFGP2_5=_GPIOEN_;
	}
	else if(pin == _P2_6)
	{
		IOCFGP2_6=PinC_InOutCMOS;  	MFCFGP2_6=_GPIOEN_;
	}
	else if(pin == _P2_7)
	{
		IOCFGP2_7=PinC_InOutCMOS;  	MFCFGP2_7=_GPIOEN_;
	}
	else if(pin == _P3_0)
	{
		IOCFGP3_0=PinC_InOutCMOS;  	MFCFGP3_0=_GPIOEN_;
	}
	else if(pin == _P3_1)
	{
		IOCFGP3_1=PinC_InOutCMOS;  	MFCFGP3_1=_GPIOEN_;
	}
	else if(pin == _P3_2)
	{
		IOCFGP3_2=PinC_InOutCMOS;  	MFCFGP3_2=_GPIOEN_;
	}
	else if(pin == _P3_3)
	{
		IOCFGP3_3=PinC_InOutCMOS;  	MFCFGP3_3=_GPIOEN_;
	}
	else
	{
		printString("WRONG11\n");
	}
}

void PIN_CONFIG_setup_key(unsigned char pin)
{
	if(pin == _P0_0)
	{
		IOCFGP0_0 = PinC_InPuDn;  	MFCFGP0_0=_GPIOEN_;
	}
	else if(pin == _P0_1)
	{
		IOCFGP0_1 = PinC_InPuDn;  	MFCFGP0_1=_GPIOEN_;
	}
	else if(pin == _P0_2)
	{
		IOCFGP0_2 = PinC_InPuDn;  	MFCFGP0_2=_GPIOEN_;
	}
	else if(pin == _P0_3)
	{
		IOCFGP0_3 = PinC_InPuDn;  	MFCFGP0_3=_GPIOEN_;
	}
	else if(pin == _P0_4)
	{
		IOCFGP0_4 = PinC_InPuDn;  	MFCFGP0_4=_GPIOEN_;
	}
	else if(pin == _P0_5)
	{
		IOCFGP0_5 = PinC_InPuDn;  	MFCFGP0_5=_GPIOEN_;
	}
	else if(pin == _P0_6)
	{
		IOCFGP0_6 = PinC_InPuDn;  	MFCFGP0_6=_GPIOEN_;
	}
	else if(pin == _P0_7)
	{
		IOCFGP0_7 = PinC_InPuDn;  	MFCFGP0_7=_GPIOEN_;
	}
	else if(pin == _P1_0)
	{
		IOCFGP1_0 = PinC_InPuDn;  	MFCFGP1_0=_GPIOEN_;
	}
	else if(pin == _P1_1)
	{
		IOCFGP1_1 = PinC_InPuDn;  	MFCFGP1_1=_GPIOEN_;
	}
	else if(pin == _P1_2)
	{
		IOCFGP1_2 = PinC_InPuDn;  	MFCFGP1_2=_GPIOEN_;
	}
	else if(pin == _P1_3)
	{
		IOCFGP1_3 = PinC_InPuDn;  	MFCFGP1_3=_GPIOEN_;
	}
	else if(pin == _P1_4)
	{
		IOCFGP1_4 = PinC_InPuDn;  	MFCFGP1_4=_GPIOEN_;
	}
	else if(pin == _P1_5)
	{
		IOCFGP1_5 = PinC_InPuDn;  	MFCFGP1_5=_GPIOEN_;
	}
	else if(pin == _P1_6)
	{
		IOCFGP1_6 = PinC_InPuDn;  	MFCFGP1_6=_GPIOEN_;
	}
	else if(pin == _P1_7)
	{
		IOCFGP1_7 = PinC_InPuDn;  	MFCFGP1_7=_GPIOEN_;
	}
	else if(pin == _P2_0)
	{
		IOCFGP2_0 = PinC_InPuDn;  	MFCFGP2_0=_GPIOEN_;
	}
	else if(pin == _P2_1)
	{
		IOCFGP2_1 = PinC_InPuDn;  	MFCFGP2_1=_GPIOEN_;
	}
	else if(pin == _P2_2)
	{
		IOCFGP2_2 = PinC_InPuDn;  	MFCFGP2_2=_GPIOEN_;
	}
	else if(pin == _P2_3)
	{
		IOCFGP2_3 = PinC_InPuDn;  	MFCFGP2_3=_GPIOEN_;
	}
	else if(pin == _P2_4)
	{
		IOCFGP2_4 = PinC_InPuDn;  	MFCFGP2_4=_GPIOEN_;
	}
	else if(pin == _P2_5)
	{
		IOCFGP2_5 = PinC_InPuDn;  	MFCFGP2_5=_GPIOEN_;
	}
	else if(pin == _P2_6)
	{
		IOCFGP2_6 = PinC_InPuDn;  	MFCFGP2_6=_GPIOEN_;
	}
	else if(pin == _P2_7)
	{
		IOCFGP2_7 = PinC_InPuDn;  	MFCFGP2_7=_GPIOEN_;
	}
	else if(pin == _P3_0)
	{
		IOCFGP3_0 = PinC_InPuDn;  	MFCFGP3_0=_GPIOEN_;
	}
	else if(pin == _P3_1)
	{
		IOCFGP3_1 = PinC_InPuDn;  	MFCFGP3_1=_GPIOEN_;
	}
	else if(pin == _P3_2)
	{
		IOCFGP3_2 = PinC_InPuDn;  	MFCFGP3_2=_GPIOEN_;
	}
	else if(pin == _P3_3)
	{
		IOCFGP3_3 = PinC_InPuDn;  	MFCFGP3_3=_GPIOEN_;
	}
	else
	{
		printString("WRONG12\n");
	}
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

