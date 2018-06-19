#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_Function.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_Sensorless.h"
#include "CS8963_PWM.h"
#include "CS8963_Initial.h"

BYTE sensorless_start = 6;

void Start_Motor_Sensorless()
{
	Disable_Comparator();
	Initial_Comparator_Sensorless();
	
	Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
	mt_drive_time_new = 0;
	mt_drive_time_old = 0;
	mt_drive_time_diff_new = 0;
	mt_drive_time_diff_old = 0;
	too_fast = 0;
	too_slow = 0;
	abnormal = 0;
	MtState = start;
	motor_start = 1;

	sensorless_start = get_next_sensorless_start_status(sensorless_start);
	Hal_sta_my = sensorless_start;

	printString("Hall:");get_current_hall_state();
	printString("\tH:");printd(Hal_sta_my);printString("\tD:");printd(PWM_duty);printString("\n");

	if(flag_run_dir == CW)
		MT_drive(Hal_sta_my);
	else
		MT_drive(7 - Hal_sta_my);
	mt_drive_cnt = 0;
}

BYTE get_next_sensorless_start_status(BYTE sensorless_start_status_now)
{
	BYTE sensorless_start_status_next;
	if(flag_run_dir == CW)	//6 4 5 1 3 2
	{
		switch(sensorless_start_status_now)
		{
			case 6:	sensorless_start_status_next = 5;	break;
			case 4:	sensorless_start_status_next = 1;	break;
			case 5:	sensorless_start_status_next = 3;	break;
			case 1:	sensorless_start_status_next = 2;	break;
			case 3:	sensorless_start_status_next = 6;	break;
			case 2:	sensorless_start_status_next = 4;	break;
			default:
					sensorless_start_status_next = 1;	break;
		}
	}
	else	//CCW 5 4 6 2 3 1
	{
		switch(sensorless_start_status_now)
		{
			case 5:	sensorless_start_status_next = 6;	break;
			case 4:	sensorless_start_status_next = 2;	break;
			case 6:	sensorless_start_status_next = 3;	break;
			case 2:	sensorless_start_status_next = 1;	break;
			case 3:	sensorless_start_status_next = 5;	break;
			case 1:	sensorless_start_status_next = 4;	break;
			default:
					sensorless_start_status_next = 1;	break;
		}
	}
	return sensorless_start_status_next;
}
