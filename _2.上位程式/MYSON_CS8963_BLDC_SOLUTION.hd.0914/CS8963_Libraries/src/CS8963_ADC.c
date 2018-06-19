#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "CS8963_Function.h"
#include "CS8963_Config.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function ADC
 * Filename: CS8963_ADC.C
 * Author  :
 * Date    : 2015/01/13
 **********************************************************/

void Initial_ADC(unsigned char pin)
{
	PIN_CONFIG_setup_adc(pin);
}

void Disable_ADC(unsigned char pin)
{
	if((pin == _P0_0)||(pin == _P0_2)||(pin == _P0_5))		//select A channel
		ADCCHSL &= ~ADC_A_EN;
	else if((pin == _P0_1)||(pin == _P0_3)||(pin == _P0_4))	//select B channel
		ADCCHSL &= ~ADC_B_EN;
	else if(pin == _P0_6)									//select C channel
		ADCCHSL &= ~ADC_C_EN;
	else if((pin == _P0_7)||(pin == _P1_0)||(pin == _P1_1)||(pin == _P1_2)||(pin == _P1_3)||(pin == _P1_6)||(pin == _P3_0)||(pin == _P3_1))	//select D channel
		ADCCHSL &= ~ADC_D_EN;
	else
	{
		printString("Illegal ADC port: ");printd(pin);printString("\n");
	}
	if(pin == _P0_0)					//ADA2
	{
		IOCFGP0_0 = B00000000;			//Enable Anolog MUX
		MFCFGP0_0 = PinC_In;			//ADC A2 for instantaneous current
	}
	else if(pin == _P0_2)				//ADA1
	{
		IOCFGP0_2 = B00000000;			//Enable Anolog MUX
		MFCFGP0_2 = PinC_In;			//ADC A1 for instantaneous current
	}
	else if(pin == _P0_5)				//ADA3
	{
		IOCFGP0_5 = B00000000;			//Enable Anolog MUX
		MFCFGP0_5 = PinC_In;			//ADC A3 for instantaneous current
	}
	else if(pin == _P0_1)				//ADB2
	{
		IOCFGP0_1 = B00000000;			//Enable Anolog MUX
		MFCFGP0_1 = PinC_In;			//ADC B2 for instantaneous current
	}
	else if(pin == _P0_3)				//ADB1
	{
		IOCFGP0_3 = B00000000;			//Enable Anolog MUX
		MFCFGP0_3 = PinC_In;			//ADC B1 for instantaneous current
	}
	else if(pin == _P0_4)				//ADB3
	{
		IOCFGP0_4 = B00000000;			//Enable Anolog MUX
		MFCFGP0_4 = PinC_In;			//ADC B1 for instantaneous current
	}
	else if(pin == _P0_6)				//ADC2
	{
		IOCFGP0_6 = B00000000;			//Enable Anolog MUX
		MFCFGP0_6 = PinC_In;			//ADC C2 for instantaneous current
	}
	else if(pin == _P0_7)				//ADD2
	{
		IOCFGP0_7 = B00000000;			//Enable Anolog MUX
		MFCFGP0_7 = PinC_In;			//ADC D2 for instantaneous current
	}
	else if(pin == _P1_0)				//ADD3
	{
		IOCFGP1_0 = B00000000;			//Enable Anolog MUX
		MFCFGP1_0 = PinC_In;			//ADC D3 for instantaneous current
	}
	else if(pin == _P1_1)				//ADD4
	{
		IOCFGP1_1 = B00000000;			//Enable Anolog MUX
		MFCFGP1_1 = PinC_In;			//ADC D4 for instantaneous current
	}
	else if(pin == _P1_2)				//ADD7
	{
		IOCFGP1_2 = B00000000;			//Enable Anolog MUX
		MFCFGP1_2 = PinC_In;			//ADC D7 for instantaneous current
	}
	else if(pin == _P1_3)				//ADD8
	{
		IOCFGP1_3 = B00000000;			//Enable Anolog MUX
		MFCFGP1_3 = PinC_In;			//ADC D8 for instantaneous current
	}
	else if(pin == _P1_6)				//ADD9
	{
		IOCFGP1_6 = B00000000;			//Enable Anolog MUX
		MFCFGP1_6 = PinC_In;			//ADC D9 for instantaneous current
	}
	else if(pin == _P3_0)				//ADD5
	{
		IOCFGP3_0 = B00000000;			//Enable Anolog MUX
		MFCFGP3_0 = PinC_In;			//ADC D5 for instantaneous current
	}
	else if(pin == _P3_1)				//ADD6
	{
		IOCFGP3_1 = B00000000;			//Enable Anolog MUX
		MFCFGP3_1 = PinC_In;			//ADC D6 for instantaneous current
	}
	else
	{
		printString("Illegal ADC port: ");printd(pin);printString("\n");
	}
}

void Get_ADC_Result(unsigned char pin)
{
	ADCCFG = b10110001;				//Start convertion
	while(ADCCFG&0x10);				//Waiting for conversion finish
	if((pin == _P0_0)||(pin == _P0_2)||(pin == _P0_5))		//select A channel
	{
		if(ADCCHSL&ADC_A_IF)
			ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;
	}
	else if((pin == _P0_1)||(pin == _P0_3)||(pin == _P0_4))	//select B channel
	{
		if(ADCCHSL&ADC_B_IF)
			ADC_B_result = ((UINT)ADCBH<<8)+ (UINT)ADCBL;
	}
	else if(pin == _P0_6)									//select C channel
	{
		if(ADCCHSL&ADC_C_IF)
			ADC_C_result = ((UINT)ADCCH<<8)+ (UINT)ADCCL;
	}
	else if((pin == _P0_7)||(pin == _P1_0)||(pin == _P1_1)||(pin == _P1_2)||(pin == _P1_3)||(pin == _P1_6)||(pin == _P3_0)||(pin == _P3_1))	//select D channel
	{
		if(ADCCHSL&ADC_D_IF)
			ADC_D_result = ((UINT)ADCDH<<8)+ (UINT)ADCDL;
	}
	else
	{
		printString("Illegal ADC port: ");printd(pin);printString("\n");
	}
}

