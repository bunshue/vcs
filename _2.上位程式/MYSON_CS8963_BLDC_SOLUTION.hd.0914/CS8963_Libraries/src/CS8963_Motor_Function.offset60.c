#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_Function.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_Setup.h"
#include "CS8963_PWM.h"
#include "CS8963_Timer.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function
 * Filename: CS8963_Motor_Function.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/

char MtState_changed()
{
	if(MtState==MtState_temp)
	{
		return 0;
	}
	else
	{
		MtState_temp = MtState;
		return 1;
	}
}

void MT_drive(unsigned char Hal_sta_tmp)	//UNIPOLAR PWM
{
#ifdef CM2209B
	IOCFGP1_1 = PinC_InOutCMOS; MFCFGP1_1 = 0x01;	//PWMAN
	IOCFGP1_5 = PinC_InOutCMOS; MFCFGP1_5 = 0x01;	//PWMBN
	IOCFGP3_0 = PinC_InOutCMOS; MFCFGP3_0 = 0x01;	//PWMCN
#endif
		switch(Hal_sta_tmp)
		{
#ifdef USE_NNMOS
			case 3:	MFCFGP1_0 = Hopen;	 P1_1=0;	//A+
					MFCFGP1_4 = Close;	 P1_5=1;	//B-
					MFCFGP3_1 = Close;	 P3_0=0;	//C0
					break;
			case 2:	MFCFGP1_0 = Close;	 P1_1=0;	//A0
					MFCFGP1_4 = Close;	 P1_5=1;	//B-
					MFCFGP3_1 = Hopen;	 P3_0=0;	//C+
					break;
			case 6:	MFCFGP1_0 = Close;	 P1_1=1;	//A-
					MFCFGP1_4 = Close;	 P1_5=0;	//B0
					MFCFGP3_1 = Hopen;	 P3_0=0;	//C+
					break;
			case 4:	MFCFGP1_0 = Close;	 P1_1=1;	//A-
					MFCFGP1_4 = Hopen;	 P1_5=0;	//B+
					MFCFGP3_1 = Close;	 P3_0=0;	//C0
					break;
			case 5:	MFCFGP1_0 = Close;	 P1_1=0;	//A0
					MFCFGP1_4 = Hopen;	 P1_5=0;	//B+
					MFCFGP3_1 = Close;	 P3_0=1;	//C-
					break;
			case 1:	MFCFGP1_0 = Hopen;	 P1_1=0;	//A+
					MFCFGP1_4 = Close;	 P1_5=0;	//B0
					MFCFGP3_1 = Close;	 P3_0=1;	//C-
					break;						
#elif defined USE_PNMOS
			case 2:			//HALL_DEGREE_270
					PWMAL=PWMDUTY_L;PWMAH=PWMDUTY_H;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
					PWMBL=PWM_PERIOD;PWMBH=PWM_PERIOD;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Lopen;	//B-
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 6:			//HALL_DEGREE_210
					MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					PWMBL=PWM_PERIOD;PWMBH=PWM_PERIOD;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Lopen;	//B-
					PWMCL=PWMDUTY_L;PWMCH=PWMDUTY_H;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
					break;
			case 4:			//HALL_DEGREE_150
					PWMAL=PWM_PERIOD;PWMAH=PWM_PERIOD;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Lopen;	//A-
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					PWMCL=PWMDUTY_L;PWMCH=PWMDUTY_H;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
					break;
			case 5:			//HALL_DEGREE_90
					PWMAL=PWM_PERIOD;PWMAH=PWM_PERIOD;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Lopen;	//A-
					PWMBL=PWMDUTY_L;PWMBH=PWMDUTY_H;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 1:			//HALL_DEGREE_30
					MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					PWMBL=PWMDUTY_L;PWMBH=PWMDUTY_H;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
					PWMCL=PWM_PERIOD;PWMCH=PWM_PERIOD;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Lopen;	//C-
					break;
			case 3:			//HALL_DEGREE_330
					PWMAL=PWMDUTY_L;PWMAH=PWMDUTY_H;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					PWMCL=PWM_PERIOD;PWMCH=PWM_PERIOD;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Lopen;	//C-
					break;
#else
			case 2:			//HALL_DEGREE_270
					PWMAL=PWMDUTY_L;PWMAH=PWMDUTY_H;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
					PWMBL=0;PWMBH=0;
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	//B-
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 6:			//HALL_DEGREE_210
					MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					PWMBL=0;PWMBH=0;
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	//B-
					PWMCL=PWMDUTY_L;PWMCH=PWMDUTY_H;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
					break;
			case 4:			//HALL_DEGREE_150
					PWMAL=0;PWMAH=0;
					MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	//A-
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					PWMCL=PWMDUTY_L;PWMCH=PWMDUTY_H;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
					break;
			case 5:			//HALL_DEGREE_90
					PWMAL=0;PWMAH=0;
					MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	//A-
					PWMBL=PWMDUTY_L;PWMBH=PWMDUTY_H;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 1:			//HALL_DEGREE_30
					MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					PWMBL=PWMDUTY_L;PWMBH=PWMDUTY_H;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
					PWMCL=0;PWMCH=0;
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	//C-
					break;
			case 3:			//HALL_DEGREE_330
					PWMAL=PWMDUTY_L;PWMAH=PWMDUTY_H;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					PWMCL=0;PWMCH=0;
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	//C-
					break;
#endif
			default:
					printS('F');printS('A');printS('I');printS('L');printS(':');printS(Hal_sta+0x30);
					break;
		}
}

void MT_drive_reverse(unsigned char Hal_sta_tmp)	//UNIPOLAR PWM
{
#ifdef CM2209B
	IOCFGP1_1 = PinC_InOutCMOS; MFCFGP1_1 = 0x01;		//PWMAN
	IOCFGP1_5 = PinC_InOutCMOS; MFCFGP1_5 = 0x01;		//PWMBN
	IOCFGP3_0 = PinC_InOutCMOS; MFCFGP3_0 = 0x01;		//PWMCN
#endif
	switch(Hal_sta_tmp)
	{
#ifdef USE_NNMOS
			case 4:	MFCFGP1_0 = Hopen;	 P1_1=0;	//A+
					MFCFGP1_4 = Close;	 P1_5=1;	//B-
					MFCFGP3_1 = Close;	 P3_0=0;	//C0
					break;
			case 5:	MFCFGP1_0 = Close;	 P1_1=0;	//A0
					MFCFGP1_4 = Close;	 P1_5=1;	//B-
					MFCFGP3_1 = Hopen;	 P3_0=0;	//C+
					break;
			case 1:	MFCFGP1_0 = Close;	 P1_1=1;	//A-
					MFCFGP1_4 = Close;	 P1_5=0;	//B0
					MFCFGP3_1 = Hopen;	 P3_0=0;	//C+
					break;
			case 3:	MFCFGP1_0 = Close;	 P1_1=1;	//A-
					MFCFGP1_4 = Hopen;	 P1_5=0;	//B+
					MFCFGP3_1 = Close;	 P3_0=0;	//C0
					break;
			case 2:	MFCFGP1_0 = Close;	 P1_1=0;	//A0
					MFCFGP1_4 = Hopen;	 P1_5=0;	//B+
					MFCFGP3_1 = Close;	 P3_0=1;	//C-
					break;
			case 6:	MFCFGP1_0 = Hopen;	 P1_1=0;	//A+
					MFCFGP1_4 = Close;	 P1_5=0;	//B0
					MFCFGP3_1 = Close;	 P3_0=1;	//C-
					break;						
#else
			case 5:	
					PWMAL=PWMDUTY_L;PWMAH=PWMDUTY_H;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	 //A+
					PWMBL=0;PWMBH=0;
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	 //B-
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 1:	
					MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					PWMBL=0;PWMBH=0;
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	 //B-
					PWMCL=PWMDUTY_L;PWMCH=PWMDUTY_H;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	 //C+
					break;
			case 3:	
					PWMAL=0;PWMAH=0;
					MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	 //A-
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					PWMCL=PWMDUTY_L;PWMCH=PWMDUTY_H;
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	 //C+
					break;
			case 2:	
					PWMAL=0;PWMAH=0;
					MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	 //A-
					PWMBL=PWMDUTY_L;PWMBH=PWMDUTY_H;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	 //B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 6:	
					MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					PWMBL=PWMDUTY_L;PWMBH=PWMDUTY_H;
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	 //B+
					PWMCL=0;PWMCH=0;
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	 //C-
					break;
			case 4:	
					PWMAL=PWMDUTY_L;PWMAH=PWMDUTY_H;
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	 //A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;		 //B0
					PWMCL=0;PWMCH=0;
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	 //C-
					break;
#endif
			default:
					printS('F');printS('A');printS('I');printS('L');printS(':');printS(Hal_sta+0x30);
					break;
	}
}

void Limit_MinMaxSpeed(void)
{
	if (target_speed < MINSPEED)
	{
  		target_speed = MINSPEED;
	}
	if (target_speed > MAXSPEED)
	{
  		target_speed = MAXSPEED;
	}
}

#ifdef OVER_CURRENT_PROTECTION_METHOD_1
void OverCurrentProtection(void)
{
	cnt_CurPro++;
	printString("Over Current Protection ");printd(cnt_CurPro);printString(" \n");

	if(cnt_CurPro == OVER_CURRENT_TIME)
	{
		cnt_CurPro = 0;
		printString("Over Current Protection 1    STOP\n");
		PWM_duty = PWM_DUTY;
		target_speed=TARGET_SPEED;
		SETUP_PWM_duty(PWM_duty);
		Initial_PWM16(PWM_period,PWM_duty);
		MtState = stop;
		real_speed = 0;
		PINT0EN = 0;
		PWM16_disable();
	}
}
#elif OVER_CURRENT_PROTECTION_METHOD_2
void OverCurrentProtection(void)
{
		printString("Over Current Protection 2    STOP\n");		
		PINT0EN = 0;
		PWM_duty = PWM_DUTY;
		target_speed=TARGET_SPEED;
		SETUP_PWM_duty(PWM_duty);
		Initial_PWM16(PWM_period,PWM_duty);

		PWM16_disable();
		MtState = stop;
		real_speed = 0;
		PINT0EN = 0;
		over_current_cnt = 0;
		ADC_A_result = 0;
}
#endif

void Lock_Rotor_Protection(void)
{
	if(real_speed < LOCK_ROTOR_UPPER_LIMIT)
	{
		printString("Too slow\n");
	}

	if(ADC_A_result > OVER_CURRENT_VALUE)
	{
		printString("Lock Rotor Protection: Over Current: 0x");
		printx(ADC_A_result>>8);
		printx(ADC_A_result);
		printS(' ');
		over_current_cnt++;
		printd(over_current_cnt);
		printS(0x0a);printS(0x0d);
		if(over_current_cnt == LOCK_ROTOR_TIME)
		{
			//OverCurrentProtection();
			printString("STOP\n");
			over_current_cnt = 0;
			PWM_duty = PWM_DUTY;
			target_speed=TARGET_SPEED;
			SETUP_PWM_duty(PWM_duty);
			Initial_PWM16(PWM_period,PWM_duty);
			MtState = stop;
			real_speed = 0;
			PINT0EN = 0;
			PWM16_disable();
		}
	}
	else
	{
		over_current_cnt = 0;
	}
}

void MT_Brake(void)
{
	MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;
	MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;
	MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;

	P1_1 = 1;
	P1_5 = 1;
	P3_0 = 1;
}

void MT_drive_A_on()
{
	MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
}

void MT_drive_A_off()
{
	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;		//A0
}

void MT_drive_B_on()
{
	MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
}

void MT_drive_B_off()
{
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;		//B0
}

void MT_drive_C_on()
{
	MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
}

void MT_drive_C_off()
{
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;		//C0
}

void MT_drive_ABC_off()
{
	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;		//A0
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;		//B0
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;		//C0
}
