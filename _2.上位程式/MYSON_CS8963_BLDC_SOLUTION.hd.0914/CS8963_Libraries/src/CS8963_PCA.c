#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_Function.h"
#include "CS8963_PCA.h"
#include "CS8963_Config.h"
#include "CS8963_Initial.h"

void PCA_Mode_Setup(void)
{
	PIN_CONFIG_setup_gpio(_P1_3);	//pin3
	PIN_CONFIG_setup_gpio(_P1_2);	//pin4
	P1_3 = 1;		//stop UVW
	if(flag_run_dir == CW)
		P1_2 = 1;	//CW
	else
		P1_2 = 0;	//CCW
	PIN_CONFIG_setup_gpio(_P3_3);	//pin22
	PIN_CONFIG_setup_gpio(_P3_2);	//pin23
	PIN_CONFIG_setup_gpio(_P2_7);	//pin24
	P3_3 = P0_4;
	P3_2 = P0_3;
	P2_7 = P0_2;

	Init_PCA_IO();
	PCA_duty = PCA_START_DUTY;
	PCA8_Modify(PCA_duty);

	if(PCA_use_real_hall == 0)	//use sensorless hall
	{
		Disable_Comparator();
		Initial_Comparator_Sensorless();
		PINT0EN = 0;
		printString("\nPCA Mode\tSensorless Hall\tPCA duty = ");
		printd(PCA_duty);printString(", max=255\n");
	}
}

void Init_PCA_IO(void)
{
	/*
	IOCFGP1_0 = b00000110;	 									//P1_0		CEX0
	MFCFGP1_0 = b00010000;
	P1_0 = 1;
	*/

	/*
	IOCFGP3_1 = b00000110;	 									//P1_3		CEX3
	MFCFGP3_1 = b00010000;
	P3_1 = 1;
	*/

	IOCFGP2_1 = b00000110;	 									//P2_1		CEX5
	MFCFGP2_1 = b00010000;
	P2_1 = 1;

	/*
	IOCFGP0_0 = b00000110;	 									//P0_0		CEX0
	MFCFGP0_0 = b00010000;

	IOCFGP0_1 = b00000110;	 									//P0_1		CEX1		
	MFCFGP0_1 = b00010000;
		
	IOCFGP0_2 = b00000110;	 									//P0_2		CEX2
	MFCFGP0_2 = b00010000;
														
	IOCFGP0_3 = b00000110;	 									//P0_3		CEX3
	MFCFGP0_3 = b00010000;
	
	IOCFGP1_1 = b00000110;	 									//P1_1		CEX5
	MFCFGP1_1 = b00010000;
	*/
}

void PCA_disable(void)
{	
	/*
	P1_0 = 1;
	MFCFGP1_0 = 0x01;	// GPIO
	IOCFGP1_0 = 0x06;	// CMOS output

	P3_1 = 1;
	MFCFGP3_1 = 0x01;	// GPIO
	IOCFGP3_1 = 0x06;	// CMOS output
	*/
	P2_1 = 1;
	MFCFGP2_1 = 0x01;	// GPIO
	IOCFGP2_1 = 0x06;	// CMOS output

}

void PCA8_Modify(unsigned char Duty)				// bit16 = 1, 16bit PWM mode;  bit16 = 0, 8bit PWM mode
{	
	unsigned char temp;

	PCACPS = 0x02; 		//62.5k / (PCACPS + 1)		// clock input to PCA: system/(pcapcs[7:0]+1)

	/* PCA frequency
	PCA frequency = 16e6/(PCACPS+1)/(256-CHRLD)
	PCACPS = 1, CHRLD = 0, PCA frequency = 31.3kHz
	PCACPS = 2, CHRLD = 0, PCA frequency = 20.8kHz
	PCACPS = 3, CHRLD = 0, PCA frequency = 15.6kHz
	PCACPS = 4, CHRLD = 0, PCA frequency = 12.5kHz
	*/

    PCACON = b00000000;								// 16 bit PWM
    PCAMOD = b00000000;								// 16 bit PWM

	//CCAPM0 = b01000010;							//CEX0
	//CCAPM3 = b01000010;							//CEX3
   	CCAPM5 = b01000010;								//CEX5

	/*
	CCAP0L = 0x00;	CCAP0H = 0x20;					//DutyCycle: 87.5%
	CCAP1L = 0x00;	CCAP1H = 0xE0;					//DutyCycle: 12.5%	
	CCAP2L = 0x00;	CCAP2H = 0x40;					//DutyCycle: 75%
	CCAP3L = 0x00;	CCAP3H = 0xC0;					//DutyCycle: 25%
	CCAP4L = 0x00;	CCAP4H = 0x60;					//DutyCycle: 62.5%
	CCAP5L = 0x00;	CCAP5H = 0xA0;					//DutyCycle: 37.5%
	*/

    //temp = 255 - Duty;
	temp = Duty;

	//CCAP0L = temp;								//DutyCycle: 87.5%
	//CCAP1L = 0x40;								//DutyCycle: 75%
	//CCAP2L = 0x60;								//DutyCycle: 62.5%
	//CCAP3L = temp;								//DutyCycle: 50%
	//CCAP4L = 0xA0;								//DutyCycle: 37.5%
	CCAP5L = temp;									//DutyCycle: 25%

	PCAMOD |= b00001000;							//turn on main counter
}
