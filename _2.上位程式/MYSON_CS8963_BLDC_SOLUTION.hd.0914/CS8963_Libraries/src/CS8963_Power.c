#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_Power.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function Power Mode
 * Filename: CS8963_Power.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/
void PowerMode_Pmm(void)
{
	PMR = 0xc0;	// CD1 CD0 SWB - - - - -	// CD1 = CD0 = 1 PMM mode                                                  // CD1=0, CD0=1 normal mode
}

void PowerMode_Idle(void)
{
	PCON = 0x01;	//SMOD0 - - - - Sleep Stop Idle
}

void PowerMode_Stop(void)
{
	PCON |= 0x02;   //SMOD0 - - - - Sleep Stop Idle
}
void PowerMode_Sleep(void)
{
	PCON = 0x06;	//SMOD0 - - - - Sleep Stop Idle	0x06
}

