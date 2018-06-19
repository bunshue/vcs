#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_Timer.h"
#include "CS8963_Function.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function Timer
 * Filename: CS8963_Timer.c
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/
void Timer0_Running(void)
{
	TCON = (TCON|0x50);	   // this is timer 0 && timer 1 runing at the same time
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

void Initial_Timer1(void)
{
	//TMOD = (TMOD|0x10); //time0 mode1(16bit timer mode)
	TMOD=0x11;
	TCON &= 0x3f;
	CKCON &= ~0x10;		//T1CKDCTL, Timer 1 Clock Source Division Factor, 0:CPU/12, 1:CPU/4
	TH1 =0x00;		//50ms@11.0592mhz
	TL1 =0x00;

	ET1 = 1;
	EA = 1;

	TR1 = 1; //run
}

void Initial_Timer2(void)
{
	//CKCON &= ~0x20;		//T2CKDCTL, Timer 2 Clock Source Division Factor, 0:CPU/12, 1:CPU/4
	T2CON = 0x00;		//time0 mode1(16bit timer mode)
	RLDH = 0xaf;
	RLDL = 0x3C;
	TH2 = 0xaf;
	TL2 = 0x3c;

	ET2 = 1;
	EA = 1;

	TR2 = 1;
}

void Initial_Timer3(void)	   	 //after timer initial the counter will up count to overflow 		and to interrupt 14
{
	EXIE = EXIE | 0x80;
	EA = 1;			             //Global Interrupt Enable bit.

	//TH4 : T4[15-8] TL4 :T4[7-0]
	T3L = 0x00;
	T3H = 0x00;

	//T34CON = TF4 TM4 TR4 T4IEN TF3 TM3  TR3 T3IEN
	T34CON |= 0x07;               //time4 (16bit timer mode)
}

void Initial_Timer4(void)	 	 //after timer initial the counter will up count to overflow 		and to interrupt 14
{
	unsigned char T4CON_tmp;
	EXIE = EXIE | 0x80;
	EA = 1;			             //Global Interrupt Enable bit.
	//TH4 : T4[15-8] TL4 :T4[7-0]
	T4L = 0x00;
	T4H = 0x00;

	//T34CON = TF4 TM4 TR4 T4IEN TF3 TM3  TR3 T3IEN
	//T34CON |= 0x70;               //time4 (16bit timer mode)
	T4CON_tmp = T34CON;
	T4CON_tmp |= 0x70;
	T34CON = T4CON_tmp;
}

void Initial_Timer5(void)	//after timer initial the counter will up count to overflow 		and to interrupt 14
{
	EXIE = EXIE | 0x80;
	EA = 1;					//Global Interrupt Enable bit.
	RTCCMD = 0x00;
	PMR = 0x40;				//CD1=0 CD0=1 => full speed operation
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

void Timer0_Close(void)
{
	TCON = (TCON &0xEf);	// this is timer 0 && timer 1	 stop
}

void Timer1_Close(void)
{
	TCON = (TCON &0xbf);	//TR1 = 0
}

void Timer2222_Close(void)
{
	T2CON = (T2CON &0xfb);	//TR2 = 0
}

void RESET_time(void)
{
	//printString("RESET_time\n");
	StartTime = 0;
	StartTimeT5T = 0;
	StartTimeT5H = 0;
	StartTimeT5L = 0;
	StopTime = 0;
	StopTimeT5T = 0;
	StopTimeT5H = 0;
	StopTimeT5L = 0;
	ReachTime = 0;
	ReachTimeT5T = 0;
	ReachTimeT5H = 0;
	ReachTimeT5L = 0;
}

void SETUP_start_time(void)
{
	StartTime = T5_count;
	StartTimeT5T = T5T;
	StartTimeT5H = T5H;
	StartTimeT5L = T5L;
	//printString("SETUP_start_time:\t");printd(StartTime);printString(" sec ");
	//printx(StartTimeT5T);printx(StartTimeT5H);printx(StartTimeT5L);
}

void SETUP_stop_time(void)
{
	StopTime = T5_count;
	StopTimeT5T = T5T;
	StopTimeT5H = T5H;
	StopTimeT5L = T5L;
	//printString("SETUP_stop_time:\t");printd(StopTime);printString(" sec ");
	//printx(StopTimeT5T);printx(StopTimeT5H);printx(StopTimeT5L);printString("\n\n");
}

void SETUP_reach_time(void)
{
	//printString("SETUP_reach_time\n");
	ReachTime = T5_count;
	ReachTimeT5T = T5T;
	ReachTimeT5H = T5H;
	ReachTimeT5L = T5L;
}

#ifdef TEST_START													
#define diff(a,b)	(((a) > (b)) ? (a-b) : (a+0x1000000-b))

void GET_run_time(void)
{
	ULONG seconds = 0;
	ULONG t5_count = 0;
	ULONG start_time_t5 = 0;
	ULONG stop_time_t5 = 0;

	start_time_t5 = (ULONG)StartTimeT5T<<16 | (ULONG)StartTimeT5H<<8 | StartTimeT5L;
	if(StartTime == 0)
	{
		printString("Run   Time:\tNo run time\n");
		return;
	}

	stop_time_t5 = (ULONG)StopTimeT5T<<16 | (ULONG)StopTimeT5H<<8 | StopTimeT5L;
	//printString("start time t5\t0x");printx(start_time_t5);printS('=');printd(start_time_t5);
	//printString("\nstop time t5\t0x");printx(stop_time_t5);printS('=');printd(stop_time_t5);printString("\n");
	
	seconds = StopTime - StartTime;
	t5_count = diff(stop_time_t5, start_time_t5);
	if(start_time_t5 > stop_time_t5)
		seconds -= 1;

	//printString("Run   Time :\t");printd(seconds);printString("sec ");
	//printx(t5_count);printString("\n");
	printString("Run   Time:\t");printd(seconds);printS('.');
	printd(t5_count/16000);printString(" sec\n");
}

void GET_reach_time(void)
{
	ULONG seconds = 0;
	ULONG t5_count = 0;
	ULONG start_time_t5 = 0;
	ULONG reach_time_t5 = 0;

	if(ReachTime == 0)
	{
		printString("Reach Time:\tNo reach time\n");
		return;
	}

	start_time_t5 = (ULONG)StartTimeT5T<<16 | (ULONG)StartTimeT5H<<8 | StartTimeT5L;
	reach_time_t5 = (ULONG)ReachTimeT5T<<16 | (ULONG)ReachTimeT5H<<8 | ReachTimeT5L;
	
	seconds = ReachTime - StartTime;
	t5_count = diff(reach_time_t5, start_time_t5);
	if(start_time_t5 > reach_time_t5)
		seconds -= 1;

	//printString("Reach  Time :\t");printd(seconds);printString("sec ");
	//printx(t5_count);printString("\n");
	printString("Reach Time:\t");printd(seconds);printS('.');
	printd(t5_count/16000);printString(" sec\n");
}
#endif
