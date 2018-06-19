#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_WatchDog.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function
 * Filename: CS8963_WatchDog.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/

void Initial_WDT(void)
{
	WDCON |= 0X02;
	CKCON &= ~0XC7;
	CKCON |= 0X40;
}

void Kick_WDT(void)
{
	TA=0xAA;
	TA=0x55;
	WDCON |= 0X01;
}

void WatchDOG_Initial(unsigned char DATA1)
{
	TA=0xAA;
	TA=0x55;
	WDCON = 0x01;         // reset watchdog timer 
	TA=0x00;

	WDCON = DATA1;        // - - - - WDIF WTRF EWT RWT
} 

void WatchDOG_Enable(void)
{
	WatchDOG_Initial(0x02);        //Watchdog reset enable
	CKCON &= ~0xC7;
}



