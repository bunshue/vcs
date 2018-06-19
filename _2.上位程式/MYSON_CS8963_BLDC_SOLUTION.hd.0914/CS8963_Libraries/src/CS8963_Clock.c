#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_Function.h"
#include "CS8963_Clock.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function clock
 * Filename: CS8963_Clock.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/

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

void Initial_XOSC(void)			//Initial XOSC
{
	IOCFGP2_0=b00000000;		//P2.0 xosc in
	IOCFGP2_1=b00000000;		//P2.1 xosc out
	MFCFGP2_0=b00000010;
	MFCFGP2_1=b00000010;

	TB = 0xAA;
	TB = 0x55;
	XOSCCFG = 0x07;				//7 : >16MHz, 3 : 12MHz, 1 : 8MHz
	TB = 0x00;

	DelayXms(200);

	TB = 0xAA;
	TB = 0x55;
	CKSEL = 0x01;				//select xosc
	TB = 0x00;
}

void Initial_RTC(void)			//Initial RTC
{
	IOCFGP1_4 = 0x08; 	  // analog switch enable 
	IOCFGP1_5 = 0x08; 	  // analog switch enable
	MFCFGP1_4 = 0x00;
	MFCFGP1_5 = 0x00;

	TB = 0xAA;
	TB = 0x55;
	XOSCCFG = 0x80;	 // RTC enable
	TB = 0x00;

	TB = 0xAA;
	TB = 0x55;
	CKSEL = 0x02;	 //select RTC as source clock 
	TB = 0x00;

}

void Initial_SIOSC(unsigned char ITRM, unsigned char VTRM)	//Initial SIOSC
{
  	TB = 0xAA;
  	TB = 0x55;
  	IOSCITRM = ITRM;
  	TB = 0x00;

  	DelayXms(10);

  	TB = 0xAA;
  	TB = 0x55;
  	IOSCVTRM = VTRM;
	CKSEL = 0x03;	 		//select siosc
  	TB = 0x00;
}



