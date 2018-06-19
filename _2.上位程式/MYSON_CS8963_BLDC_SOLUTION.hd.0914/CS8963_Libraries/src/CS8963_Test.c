#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_Function.h"
#include "CS8963_Config.h"
#include "CS8963_ADC.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_I2C.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : Test Function
 * Filename: CS8963_Test.C
 * Author  :
 * Date    : 2016/6/24
 **********************************************************/

void CS8963_Test(void)
{
	#ifdef TEST_UART
	int i;
	#endif

	#ifdef USE_I2C_Slave
	int i;
	#endif

	#ifdef TEST_VR
	unsigned long voltage = 0;
	unsigned long cnt1 = 0;
	unsigned char vr_duty=0;
	#endif

	#ifdef TEST_I2C
	#ifdef USE_I2C_Master
	printString("USE I2C_Master\n");
	mIIC_P21P20_Initial();
	while(1)
	{
		I2C_buffer[0] = 'M';
		I2C_buffer[1] = 'Y';
		I2C_buffer[2] = 'S';
		I2C_buffer[3] = 'O';
		I2C_buffer[4] = 'N';
		I2C_buffer_length = 5;
		send_I2C_data(I2C_buffer_length);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);

		I2C_buffer[0] = 'S';
		I2C_buffer[1] = 'T';
		I2C_buffer[2] = 'A';
		I2C_buffer[3] = 'R';
		I2C_buffer_length = 4;
		send_I2C_data(I2C_buffer_length);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	#endif

	#ifdef USE_I2C_Slave
	printString("USE I2C_Slave\n");
	sIIC_P21P20_Initial(IICS1_Addr3,IICS1_Addr1);					//Initial Slave1(P21P20)

	while(1)
	{
		get_I2C_data();
		if(I2C_buffer_length > 0)
		{
			printString("\n");
			printString("len = ");printd(I2C_buffer_length);
			printString(", data : ");
			for(i = 0 ;i<I2C_buffer_length;i++)
			{
				if(I2C_buffer[i] != 0)
					printS(I2C_buffer[i]);
				else
					printS('-');
			}
		}
		DelayXms(200);
	}
	#endif
	#endif

	#ifdef TEST_UART
	while(1)
	{
		for(i=0;i<26;i++)
		{
			printS(0x41+i);
			DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		}
	}
	#endif

	#ifdef TEST_VR
	printString("\n");
	printString("Test VR in CB2209B........,  Press RESET to EXIT.\n");
	printString("ADC, pin ");printd(SAMPLE_CURRENT_ADC);printString(";    VR, pin ");printd(PIN_VRin);printString("\n");
	while(1)		//CM2209B test ADC and test VR
	{
		cnt1++;
		if((cnt1%(VR_PROBE_SPEED*10))==0)
		{
			printString("ADC=");
			Initial_ADC(SAMPLE_CURRENT_ADC);						//Initial ADC A channel for sample current, pin18
			Get_ADC_Result(SAMPLE_CURRENT_ADC);
			Disable_ADC(SAMPLE_CURRENT_ADC);
			voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;	//mV
			printd(voltage);printS(';');

			printString("       VR=");
			Initial_ADC(PIN_VRin);						//Initial ADC A channel for sample current, pin18
			Get_ADC_Result(PIN_VRin);
			Disable_ADC(PIN_VRin);
			voltage=((unsigned long)ADC_B_result*ADC_FULL*1000)/4096;	//mV
			printd(voltage);
			if(voltage>=VR_MAX)
				vr_duty = VR_SPEED_DUTY_MAX;
			else if(voltage<=VR_MIN)
				vr_duty = 0;
			else
				vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
			printString("; duty=");printd(vr_duty);printString(";\n");
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		}
	}
	#endif

	#ifdef TEST_UVW
	printString("TEST_UVW, Test Gate Driver........,  Press RESET to EXIT.\n");
	while(1)
	{
		printS('6');printS(' ');MT_drive(6);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		printS('4');printS(' ');MT_drive(4);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		printS('5');printS(' ');MT_drive(5);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		printS('1');printS(' ');MT_drive(1);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		printS('3');printS(' ');MT_drive(3);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		printS('2');printS(' ');MT_drive(2);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	#endif

	#ifdef TEST_KEY
	#ifdef CM2209B
	printString("TEST_KEY, Test Key........ P3_3 P2_0,  Press RESET to EXIT.\n");
	while(1)
	{
		printd(P3_3);printd(P2_0);printS(' ');

		DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
	}
	#endif
	#endif

	#ifdef TEST_START
	printString("\n\n\n\nTEST_START........\n\n\n\n");
	#endif

	#ifdef TEST_ADC2VAC
	int i = 0;
	UINT ADC_result = 0;
	UINT dc_bus_voltage = 0;

	printString("\n");printString("\n");printString("\n");

	printString("TEST_ADC2VAC 220V\n");

	for(ADC_result = 0; ADC_result < 4200 ; ADC_result += 100)
	{
		dc_bus_voltage = (UINT)(((unsigned long)ADC_result*ADC_FULL*1000)/4096);	//mV
		//printString("DC_BUS_ADC = ");printd(ADC_result);printString("\t");
		//printString("DC_BUS = ");printd(dc_bus_voltage);printString(" mV\t\t");
		//printString("VM = ");printd(dc_bus_voltage/20*111/50);printString(" V\t");
		//printString("VAC = ");printd(ADC_result*2/23);printString(" V\n");

		//printString("VM  = ");printd((ADC_result/16)*185/256*3);printString(" V\t");
		//printString("VAC = ");printd((ADC_result/16)*185/256*3*5/7);printString(" V\n");
		i++;
		printString("ADC(");printd(i);printString(")=");printd(ADC_result);
		printString(";DC_BUS(");printd(i);printString(")=");printd(dc_bus_voltage);
		printString(";VM(");printd(i);printString(")=");printd((ADC_result/16)*185/256*3);
		printString(";VAC(");printd(i);printString(")=");printd((ADC_result/16)*185/256*3*5/7);
		printString(";\n");
	}
	printString("\n");printString("\n");printString("\n");
	#endif
}
