#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_BLDC.h"
#include "CS8963_MysonLink.h"
#include "CS8963_Compact_Function.h"

extern unsigned char Hal_sta;

void Initial_Timer3(void)		//after timer initial the counter will up count to overflow		and to interrupt 14
{
	EXIE = EXIE | 0x80;
	EA = 1;						//Global Interrupt Enable bit.

	//TH4 : T4[15-8] TL4 :T4[7-0]
	T3L = 0x00;
	T3H = 0x00;

	//T34CON = TF4 TM4 TR4 T4IEN TF3 TM3  TR3 T3IEN
	T34CON |= 0x07;				//time4 (16bit timer mode)
}

void Initial_Timer4(void)		//after timer initial the counter will up count to overflow		and to interrupt 14
{
	unsigned char T4CON_tmp;
	EXIE = EXIE | 0x80;
	EA = 1;						//Global Interrupt Enable bit.
	//TH4 : T4[15-8] TL4 :T4[7-0]
	T4L = 0x00;
	T4H = 0x00;

	//T34CON = TF4 TM4 TR4 T4IEN TF3 TM3  TR3 T3IEN
	//T34CON |= 0x70;			//time4 (16bit timer mode)
	T4CON_tmp = T34CON;
	T4CON_tmp |= 0x70;
	T34CON = T4CON_tmp;
}

void Initial_Timer5(void)		//after timer initial the counter will up count to overflow		and to interrupt 14
{
	EXIE = EXIE | 0x80;
	EA = 1;						//Global Interrupt Enable bit.
	RTCCMD = 0x00;
	PMR = 0x40;					//CD1=0 CD0=1 => full speed operation
	//TT5 : T5[23-16] TH5 : T5[15-8] TL5 :T5[7-0]		24bit counter value
	T5L = 0x00;
	T5H = 0x00;
	T5T = 0x00;

	// T5CON : TF5 T5SEL[1] T5SEL[0] TM5 TR5  - -  T5IEN
	T5CON = 0x19;	//time5 (24bit timer mode)	0x19 iosc	0x39 XOSC	0x59 RTC	0x79 siosc
}

void Timer3_Close(void)
{
	T34CON = (T34CON & 0xf0);
}

void Timer4_Close(void)
{
	T34CON = (T34CON & 0x0f);
}

void Timer5_Close(void)
{
	T5CON = 0;
}

void get_current_hall_state()
{
	Hal_sta=((P0&0x1C)>>2);
	printS(Hal_sta+0x30);
	PIOEDGR0 &= ~0x1C;
	PIOEDGF0 &= ~0x1C;
	PIOEDGR0 = 0x1C;
	PIOEDGF0 = 0x1C;
}

void Initial_Comparator_VTH1(BYTE vth1)
{
	//printString("Initial_Comparator by CMPVTH_VALUE, CMPVTH_VALUE = ");printd(vth1);printString("\n");
	CMP_EN = 0;

	#ifdef CM2209A
	IOCFGP2_7 = _ANEN_;						//Comparator A: ANEN
	MFCFGP2_7 = 0x80;						//enable Comparator A Input
	#elif defined CM2209B
	IOCFGP2_7 = _ANEN_;						//Comparator A: ANEN
	MFCFGP2_7 = 0x80;						//enable Comparator A Input
	#elif defined CM2209C
	IOCFGP2_7 = _ANEN_;						//Comparator A: ANEN
	MFCFGP2_7 = 0x80;						//enable Comparator A Input
	#elif defined CM2209D
	IOCFGP3_3 = _ANEN_;						//Comparator A: ANEN
	MFCFGP3_3 = 0x80;						//enable Comparator A Input
	#endif

	CMPST = 0x00;							//disable Comparator A/B/C/D Hysteresis
	DelayXms(4);							//delay

	CMPVTH1 = vth1;
	CMPCFGAB = B11100000;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
//	CMPCFGCD = B10101010;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
											//THSELx is 0, use internal(TH0) threshold; is 1 use external(TH1) threshold
											//POLx is 0,set default polarity; is 1,reverse the output polarity of the comparator

	CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
	DelayXms(1);							//delay as least 20us for the stabilization of comparator block, 258us
}

void Disable_Comparator(void)
{
	CMP_EN = 0;
	CMPCFGAB = B01100000;					//Disable comparator A by setting bit7 = 0
}

void printhex(BYTE value)
{
	BYTE nibble = 0;
	nibble = (value>>4)&0xf;
	if(nibble > 9)
		printS(nibble+0x41-10);
	else
		printS(nibble+0x30);
	nibble = (value)&0xf;
	if(nibble > 9)
		printS(nibble+0x41-10);
	else
		printS(nibble+0x30);
}

void printx(ULONG value)
{
	BYTE value3 = 0;
	BYTE value2 = 0;
	BYTE value1 = 0;
	BYTE value0 = 0;
	BYTE need_to_print_zero = 0;

	value3 = (value>>24)&0xff;
	value2 = (value>>16)&0xff;
	value1 = (value>>8)&0xff;
	value0 = (value)&0xff;

	if(value3 > 0)
	{
		need_to_print_zero = 1;
		printhex(value3);
	}
	if((value2 > 0) || (need_to_print_zero == 1))
	{
		need_to_print_zero = 1;
		printhex(value2);
	}
	if((value1 > 0) || (need_to_print_zero == 1))
	{
		need_to_print_zero = 1;
		printhex(value1);
	}
	printhex(value0);
}
