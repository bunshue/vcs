#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function DAC (Digital to Analog Converter)
 * Filename: CS8963_DAC.C
 * Author  :
 * Date    : 2016/03/22
 **********************************************************/

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





