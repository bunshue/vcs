/**********************************************************
 * Chips   : CS8963
 * Purpose : BLDC ISR
 * Filename: CS8963_ISR.C
 * Author  :
 * Date    : 2015/01/07
 **********************************************************/

#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "CS8963_Setup.h"
#include "CS8963_Function.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_PWM.h"
#include "CS8963_WatchDog.h"
#include "CS8963_ISR.h"
#include "CS8963_ADC.h"
#include "CS8963_I2C.h"
#include "CS8963_Timer.h"
#include "CS8963_Initial.h"
#include "CS8963_Config.h"
#include "CS8963_DAC.h"
#include "CS8963_UART.h"
#include "CS8963_MysonLink.h"
#include "CS8963_Sensorless.h"
#include "CS8963_PCA.h"
#include "Setup.h"
#include "Setup_function.h"

#define EUART2_TIF									(SINT2 & 0x01)
#define EUART2_TIF_CLR								(SINT2 &= (~0x01))
#define EUART2_RIF									(SINT2 & 0x20)
#define EUART2_RIF_CLR								(SINT2 &= (~0x20))

BYTE over_current_count = 0;
BYTE over_current_retry = 0;
BYTE fg_out_count = 0;
bit flag_get_pwm_cnt = 0;
BYTE get_hall_ticks = 0;
BYTE Hal_sta_old = 0;
BYTE Hal_sta_tmp;
BYTE static_pwm_mode = 0;
BYTE PID_change_cnt = 0;
BYTE timer0_check_cnt = 0;
bit lock_on_off = 0;
UINT data Hal_cnt_old = 0;
BYTE no_move_count = 0;

//for sensorless
BYTE CMPST_tmp = 0;
BYTE CMPST_old = 0;
BYTE lock_rotor_cnt = 0;

#if ENABLE_PHASE_COMPENSATION == 1
BYTE even = 0;
ULONG PWM16INT_cnt_start = 0;
ULONG PWM16INT_cnt_old = 0;
ULONG PWM16INT_cnt_tmp = 0;
ULONG PWM16INT_cnt_diff = 0;
ULONG PWM16INT_cnt_number = 0;
BYTE get_next_hall_status(BYTE hall_status_now);
#endif

BYTE buffer[10];
BYTE ptr = 0;
BYTE length = 0;

int hall_fail_cnt = 0;
BYTE hall_ok_cnt = 0;

#ifdef DUMP_PWM_SETUP
UINT real_speed_tmp = 0;
UINT PWM_period_tmp = 0;
BYTE PWM_duty_tmp = 0;
BYTE Hal_sta_tmp = 0;
BYTE PWMAL_tmp = 0;
BYTE PWMAH_tmp = 0;
BYTE PWMBL_tmp = 0;
BYTE PWMBH_tmp = 0;
BYTE PWMCL_tmp = 0;
BYTE PWMCH_tmp = 0;
BYTE PWMTRG0L_tmp = 0;
BYTE PWMTRG0H_tmp = 0;
BYTE PWMTRG1L_tmp = 0;
BYTE PWMTRG1H_tmp = 0;
BYTE PWMCNTL_tmp = 0;
BYTE PWMCNTH_tmp = 0;
BYTE PWMPRDL_tmp = 0;
BYTE PWMPRDH_tmp = 0;
BYTE PWM16CFG_tmp = 0;
BYTE PWM16INT_tmp = 0;
#endif

#ifdef HALL_DEBUG
#define DEBUG_LENGTH2 500
BYTE HALL_RESULT[DEBUG_LENGTH2] = 0;
UINT hall_array_index = 0;
#endif

#ifdef RECORD_PID_DATA
#define DEBUG_LENGTH4 45
UINT real_speed_array[DEBUG_LENGTH4] = 0;
SINT pp_array[DEBUG_LENGTH4] = 0;
SLONG ii_array[DEBUG_LENGTH4] = 0;
SLONG dd_array[DEBUG_LENGTH4] = 0;
SLONG pid_array[DEBUG_LENGTH4] = 0;
UINT pid_array_index = 0;
#endif

#ifdef TEST_START
#define DEBUG_LENGTH5 200
UINT rpm_array[DEBUG_LENGTH5] = 0;
BYTE PWM_AH_array[DEBUG_LENGTH5] = 0;
BYTE PWM_AL_array[DEBUG_LENGTH5] = 0;
BYTE ADC_result8[DEBUG_LENGTH5] = 0;
UINT timer0_cnt = 0;
UINT reach_cnt = 0;
UINT rpm_array_index = 0;
UINT pwm16_int_record_rpm_data_cnt = 0;
#endif

#ifndef USE_MYSONLINK
void Timer345_ISR(void) interrupt 14
{
	BYTE T3CON_tmp;
	BYTE T4CON_tmp;

	if((T34CON & 0x08)==0x08)
	{
		//printString("T3 ");
		T3H = 0x00;							//Timer 3 count start point
		T3L = 0x00;	
		//T34CON &= 0xf7; 					//time3 (16bit timer mode)
		T3CON_tmp = T34CON;
		T3CON_tmp &= 0xf7;
		T34CON = T3CON_tmp;
	}

	if((T34CON & 0x80)==0x80)
	{
		//printString("T4 ");
		T4L = 0x00;							//Timer 4 count start point
		T4H = 0x00;
		//T34CON &= 0x7f; 					//time3 (16bit timer mode)
		T4CON_tmp = T34CON;
		T4CON_tmp &= 0x7f;
		T34CON = T4CON_tmp;
	}		 

	if((T5CON & 0x80) == 0x80)
	{
		//printString("T5 ");
		//RTCCMD = 0x00;
		T5_count++;
		if((T5_count % 10) == 0)
		{
			//printString("rpm=");printd(real_speed);printString("\n");
		}
		EXIF = 0x00;
		//one second
		T5L = 0x00;		//Low
		T5H = 0xDC;		//Medium
		T5T = 0x0B;		//High
		T5CON = 0x19;	//time5 (24bit timer mode)	0x19 iosc	0x39 XOSC	0x59 RTC	0x79 siosc

		#ifdef SAVE_FACTORY_DATA
		if((T5_count%SAVE_FACTORY_DATA_PERIOD)==0)
			save_factory_data_time();
		#endif
	}
}
#endif

void Comparator() interrupt 9
{
	int i;

	CMPST_tmp = CMPST;
	if(CMPST_tmp != CMPST_old)
	{
		if(flag_run_dir == CW)
		{
			if ((CMPST & 0x20) == 0x20) 		//U-ComparatorB
			{
				if(Hal_sta_my == 1)
				{
					Hal_sta_my = 3;
					MT_drive(Hal_sta_my);
				}
				else if(Hal_sta_my == 6)
				{
					Hal_sta_my = 4;
					MT_drive(Hal_sta_my);
				}
			}
			if ((CMPST & 0x40) == 0x40) 		//V-ComparatorC
			{
				if(Hal_sta_my == 4)
				{
					Hal_sta_my = 5;
					MT_drive(Hal_sta_my);
				}
				else if(Hal_sta_my == 3)
				{
					Hal_sta_my = 2;
					MT_drive(Hal_sta_my);
				}
			}
			if ((CMPST & 0x80) == 0x80) 		//W-ComparatorD
			{
				if(Hal_sta_my == 5)
				{
					Hal_sta_my = 1;
					MT_drive(Hal_sta_my);
				}
				else if(Hal_sta_my == 2)
				{
					Hal_sta_my = 6;
					MT_drive(Hal_sta_my);
				}
			}
		}
		else	//CCW
		{
			if ((CMPST & 0x20) == 0x20) 		//U-ComparatorB
			{
				if(Hal_sta_my == 1)
				{
					Hal_sta_my = 5;
					MT_drive(Hal_sta_my);
				}
				else if(Hal_sta_my == 6)
				{
					Hal_sta_my = 2;
					MT_drive(Hal_sta_my);
				}
			}
			if ((CMPST & 0x40) == 0x40) 		//V-ComparatorC
			{
				if(Hal_sta_my == 4)
				{
					Hal_sta_my = 6;
					MT_drive(Hal_sta_my);
				}
				else if(Hal_sta_my == 3)
				{
					Hal_sta_my = 1;
					MT_drive(Hal_sta_my);
				}
			}
			if ((CMPST & 0x80) == 0x80) 		//W-ComparatorD
			{
				if(Hal_sta_my == 5)
				{
					Hal_sta_my = 4;
					MT_drive(Hal_sta_my);
				}
				else if(Hal_sta_my == 2)
				{
					Hal_sta_my = 3;
					MT_drive(Hal_sta_my);
				}
			}
		}
		flag_int0_ser = 1;
		CMPST_old = CMPST_tmp;
	}

	if(PWM16EMG & 0x08)
	{
		PINT0EN = 0;
		PWM16_disable();
		MtState = stop;
		SETUP_target_speed(0);
		//real_speed = 0;
		//printS('X');
	}

	if((CMPST & INTflg_CMPA) == 0x10)
	{
		CMPST &= ~INTflg_CMPA;				//clear ComparatorA flag
		PINT0EN = 0;
		PWM16_disable();
		MtState = stop;
		SETUP_target_speed(0);
		//real_speed = 0;
		power_warning_count = ENABLE_POWER_WARNING_FAST;
		if(PWM16EMG & 0x08)
		{
			//printString("XEMG by CMP A interrupt\n");
			ERROR_number = _ERROR_OCX;
			#ifdef USE_MYSONLINK
			for(i=0;i<5;i++)
			{
				Send_Motor_Error_Cmd(ERROR_number);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
			#endif
		}
		/*
		printString("CMP A interrupt ");printString("  STOP, CMPVTH_VALUE = ");printd(CMPVTH1);printString("\n");
		for(i=0;i<5;i++)
		{
			printString("OVER CURRENT PROTECTION, STOP, RESET to restart....\n");
			ERROR_number = _ERROR_OCC;
			#ifdef USE_MYSONLINK
			Send_Motor_Error_Cmd(ERROR_number);
			#endif
		}
		for(i=0;i<10;i++)
		{
			DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		}
		*/
		over_current_count++;
		if((real_speed < 200) && (over_current_count <= 5) && (MtState == start))	//when start-up, allow 5 chances.
		{
			MtState = start;
			power_warning_count = ENABLE_POWER_WARNING_SLOW;
			printS('R');
		}
		else
		{
			printString("CMP A interrupt ");printString("  STOP, CMPVTH_VALUE = ");printd(CMPVTH1);printString("\n");
			for(i=0;i<5;i++)
			{
				printString("OVER CURRENT PROTECTION, STOP, RESET to restart....\n");
				ERROR_number = _ERROR_OCC;
				#ifdef USE_MYSONLINK
				Send_Motor_Error_Cmd(ERROR_number);
				#endif
			}
		}
		/*
		if(flag_enable_vr_speed==1)
		{
			while(1)
				DelayXms(200);
		}
		*/
	}
	CMPST = 0;
}

void PWM16_INT(void) interrupt 12
{
	pwm16_int_cnt++;
	PWM16INT &= ~0x04;						//clear Zero Interrupt Flag
	if((flag_PWM16_Modify == 1) && (flag_int0_ser == 1))
	{
		flag_PWM16_Modify = 0;
		flag_int0_ser = 0;
		do_PWM16_Modify();
	}
	else if (flag_int0_ser == 1)
		flag_int0_ser = 0;
/*		TBD
#ifdef PWM_TRIGGER_ADC		//use PWM interrupt
	if(MtState == start)
	{
		if((flag_over_current_protection&0x01)==1)
		{
			Initial_ADC(SAMPLE_CURRENT_ADC);					//Initial ADC A channel for sample current, pin18
			Get_ADC_Result(SAMPLE_CURRENT_ADC);
			Disable_ADC(SAMPLE_CURRENT_ADC);
			Get_ADC_Result(SAMPLE_CURRENT_ADC);
			Over_Current_Protection();
		}
	}	
#endif
*/
	if(flag_get_pwm_cnt == 1)
	{
		flag_get_pwm_cnt = 0;
		pwm16_int_cnt = 0;
	}

	#ifdef TEST_START
	if(MtState == start)
	{
		pwm16_int_record_rpm_data_cnt++;
		if((flag_mode_type == CLOSE_LOOP) && (pwm16_int_record_rpm_data_cnt == 1000))
		{
			pwm16_int_record_rpm_data_cnt = 0;
			if(rpm_array_index < DEBUG_LENGTH5)
			{
				timer0_cnt++;
				rpm_array[rpm_array_index] = real_speed;
				PWM_AH_array[rpm_array_index] = PWMAH;
				PWM_AL_array[rpm_array_index] = PWMAL;
				if((real_speed > (target_speed - RPM_TOLERANCE))&&(reach_cnt == 0))
				{
					reach_cnt = timer0_cnt;
				}
				Initial_ADC(SAMPLE_CURRENT_ADC);					//Initial ADC A channel for sample current, pin18
				Get_ADC_Result(SAMPLE_CURRENT_ADC);
				Disable_ADC(SAMPLE_CURRENT_ADC);
				ADC_result8[rpm_array_index] = (ADC_A_result>>4)&0xff;
			}
			if(rpm_array_index < (DEBUG_LENGTH5 + 50))
				rpm_array_index++;

			//if(rpm_array_index == (DEBUG_LENGTH5 + 40))
			//	printString("OK\n");
		}
	}
	#endif
}

void Timer1(void) interrupt 3				// 50ms, for open-loop speed up/down
{
	if(flag_sensor_type == PCA_MODE)
	{
		if(MtState == start)
		{
			if(PCA_duty<(PCA_DUTY_MAX*2/4))
			{
				PCA_duty+=10;
				PCA8_Modify(PCA_duty);
				//printS('1');
			}
			else if(PCA_duty<(PCA_DUTY_MAX*3/4))
			{
				PCA_duty+=5;
				PCA8_Modify(PCA_duty);
				//printS('2');
			}
			else if(PCA_duty<PCA_DUTY_MAX)
			{
				PCA_duty++;
				PCA8_Modify(PCA_duty);
				//printS('3');
			}
		}
		TH1 = 0xa0;			//Timer 1 count start point
		TL1 = 0x00;
	}
	else	//Hall sensor mode, sensorless mode
	{
		t1_cnt++;
		if(t1_cnt == slow_modify_speed)
		{
			t1_cnt = 0;
			if((MtState == start) && (motor_start == 0) && (slow_modify_speed > 0))
			{
				if(PWM_duty < PWM_duty_target)
				{
					//printS('+');
					PWM_duty++;
					SETUP_PWM_duty_new(PWM_duty);
					flag_PWM16_Modify = 1;
				}
				else if(PWM_duty > PWM_duty_target)
				{
					//printS('-');
					PWM_duty--;
					SETUP_PWM_duty_new(PWM_duty);
					flag_PWM16_Modify = 1;
				}
			}
		}
		//P0_5 = ~P0_5;		//for debug, P0_5 should be configured as GPIO
		TH1 = 0x00;			//Timer 1 count start point
		TL1 = 0x00;
	}
}

void Int0_ser(void) interrupt 0
{
	PINT0EN=0;							//disable all PINT0 external interrupt
	
	if(PINT0F==1)
	{
		Hal_cnt++;
		get_hall_ticks++;

		Hal_sta = ((P0&0x1C)>>2);

		if(flag_sensor_type == PCA_MODE)
		{
			if(PCA_use_real_hall == 1)	//use real hall
			{
				P3_3 = P0_4;
				P3_2 = P0_3;
				P2_7 = P0_2;
			}
		}

		#ifdef HALL_DEBUG
		HALL_RESULT[hall_array_index] = Hal_sta;
		hall_array_index++;
		if(hall_array_index >= DEBUG_LENGTH2)
			hall_array_index = 0;
		#endif

#if ENABLE_PHASE_COMPENSATION == 1
		if((flag_phase_compensation_mode) && (MtState == start))
		{
			PWM16INT_cnt_tmp = PWM16INT_cnt;
			PWM16INT_cnt_start = PWM16INT_cnt_tmp;
			PWM16INT_cnt_diff = PWM16INT_cnt_tmp - PWM16INT_cnt_old;
			PWM16INT_cnt_old = PWM16INT_cnt_tmp;
		}
#endif

		if(Hal_sta_old == Hal_sta)		//skip continuous the same hall interrupt
		{
			PIOEDGR0 &= ~0x1C;
			PIOEDGF0 &= ~0x1C;
			PIOEDGR0 = 0x1C;
			PIOEDGF0 = 0x1C;
			//DelayYms();
			PINT0EN = 1;						//for PINT0.0	 PINT0.1
			return;
		}

		if(Hal_sta == 4)
		{
			if(Hal_sta_old == 5)
				flag_hall_sequence = HALL_SEQ_546;
			else
				flag_hall_sequence = HALL_SEQ_645;
		}

		if(flag_hall_protection == 1)
			check_hall_sequence();
		
		if(flag_test_hall_sequence_mode)
		{
			Hal_sta_tmp++;
			printd(Hal_sta);printS(' ');
			if(Hal_sta == 2)
			{
				if(Hal_sta_old == 3)
				{
					printS(' ');printS(' ');
				}
			}
			else if(Hal_sta == 1)
			{
				if(Hal_sta_old == 3)
				{
					printS(' ');printS(' ');
				}
			}
		}
		else if(flag_sensor_type != PCA_MODE)
		{
			if(flag_run_dir == CW)
			{
				if(flag_phase_compensation_mode)		//Phase Compensation Mode, CW
				{
					#if ENABLE_PHASE_COMPENSATION == 1
					if(phase_angle ==60)
						MT_drive(Hal_sta);					//PWM Mode, CW
					/*
					else if(phase_angle > 60)
					{
						PWM16INT_cnt_number = PWM16INT_cnt_diff * (phase_angle-60) / 60;
						if(PWM16INT_cnt_number ==0)
							MT_drive(Hal_sta);					//PWM Mode, CW
						else
						{
							Hal_sta_next = Hal_sta;
							SETUP_PWMCNT_diff(PWM16INT_cnt_start, PWM16INT_cnt_number);
						}
					}
					*/
					else
					{
						PWM16INT_cnt_number = PWM16INT_cnt_diff * phase_angle / 60;
						if(even)
						{
							even = 0;
							Hal_sta_next = get_next_hall_status(Hal_sta);
							SETUP_PWMCNT_diff(PWM16INT_cnt_start, PWM16INT_cnt_number);
						}
						else
						{
							even = 1;
							Hal_sta_next2 = get_next_hall_status(Hal_sta);
							SETUP_PWMCNT_diff2(PWM16INT_cnt_start, PWM16INT_cnt_number);
						}
					}
					#endif	//end of #if ENABLE_PHASE_COMPENSATION == 1
				}
				else
					MT_drive(Hal_sta);					//PWM Mode, CW
			}
			else
			{
				if(flag_phase_compensation_mode)		//Phase Compensation Mode, CCW
				{
					#if ENABLE_PHASE_COMPENSATION == 1
					if(phase_angle ==60)
						MT_drive(7 - Hal_sta);			//PWM Mode, CCW
					/*
					else if(phase_angle > 60)
					{
						PWM16INT_cnt_number = PWM16INT_cnt_diff * (phase_angle-60) / 60;
						Hal_sta_next = Hal_sta;
						SETUP_PWMCNT_diff(PWM16INT_cnt_start, PWM16INT_cnt_number);
					}
					*/
					else
					{
						PWM16INT_cnt_number = PWM16INT_cnt_diff * phase_angle / 60;
						if(even)
						{
							even = 0;
							Hal_sta_next = get_next_hall_status(Hal_sta);
							SETUP_PWMCNT_diff(PWM16INT_cnt_start, PWM16INT_cnt_number);
						}
						else
						{
							even = 1;
							Hal_sta_next2 = get_next_hall_status(Hal_sta);
							SETUP_PWMCNT_diff2(PWM16INT_cnt_start, PWM16INT_cnt_number);
						}
					}
					#endif	//end of #if ENABLE_PHASE_COMPENSATION == 1
				}
				else
					MT_drive(7 - Hal_sta);			//PWM Mode, CCW
			}
			#ifdef CALCULATE_SPEED_BY_PWM
			int0_cnt++;

			#if defined(STAR) || defined(STAR_V17)	//star uses 7 pairs, 0.5 round
			if(int0_cnt == 21)
			#elif defined HD	//hd uses 4 pairs, 2 round
			if(int0_cnt == 48)
			#else
			if(int0_cnt == 120)	//normal case, 120 steps
			#endif
			{
				pwm16_int_cnt_tmp = pwm16_int_cnt;

				int0_cnt = 0;
				if(motor_start == 1)
				{
					if(real_speed > MINSPEED)
						motor_start = 0;
				}
				else
				{
					if(real_speed < MINSPEED)
						motor_start = 1;
				}

				flag_get_pwm_cnt = 1;
			}
			#endif

			flag_int0_ser = 1;
#ifdef ENABLE_FG_OUT
			fg_out_count++;
			if(fg_out_count == (3 * number_motor_pole_pair))
			{
				fg_out_count = 0;
				#ifdef MOTOR_HD
				P1_6 = ~P1_6;	//P1_6(pin2) should be configured as GPIO for HD
				#else
				P2_0 = ~P2_0;	//P2_0(pin31) should be configured as GPIO
				#endif
			}
#endif
		}
		Hal_sta_old = Hal_sta;
		//DelayYms();
	}
	PIOEDGR0 &= ~0x1C;
	PIOEDGF0 &= ~0x1C;
	PIOEDGR0 = 0x1C;
	PIOEDGF0 = 0x1C;
	PINT0EN = 1;						//for PINT0.0	 PINT0.1
}

void Timer0(void) interrupt 1			//50ms
{
	int i;
	//P0_5 = ~P0_5;		//for debug, P0_5 should be configured as GPIO

	if(++t0_cnt == 2)						//2 times = 0.1 sec
	{
		t0_cnt=0;

		if((MtState == start) && (flag_sensor_type != PCA_MODE))
		{
			//Calculate real speed
			if(flag_sensor_type == HALL_SENSOR_MODE)
			{
				//real_speed = (Hal_cnt*10*60)/(6*number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				//real_speed = (Hal_cnt*10*10)/(number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				#ifdef CALCULATE_SPEED_BY_PWM
				if(Hal_cnt == Hal_cnt_old)
				{
					no_move_count++;
					if(no_move_count == 5)
					{
						no_move_count = 0;
						real_speed = 0;
					}
				}
				else
				{
					Hal_cnt_old = Hal_cnt;
					no_move_count = 0;
				}
				#else
				real_speed = (Hal_cnt*101)/(number_motor_pole_pair);		//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				Hal_cnt = 0;
				if(motor_start == 1)
				{
					if(real_speed > MINSPEED)
						motor_start = 0;
				}
				else
				{
					if(real_speed < MINSPEED)
						motor_start = 1;
				}
				#endif
			}
			else if(flag_sensor_type == SENSORLESS_MODE)
			{
				//real_speed = (Hal_cnt*10*60)/(6*number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				//real_speed = (Hal_cnt*10*10)/(number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				real_speed = (mt_drive_cnt*101)/(number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm

				if(real_speed > MAXSPEED)	//too many steps, abnormal
				{
						Stop_Motor();
						printString("Abnormal1, sensorless restart, mt_drive_cnt = ");printd(mt_drive_cnt);printString("\n");
						real_speed = (mt_drive_cnt*101)/(number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
						printString("real_speed = ");printd(real_speed);printString("\n");
						mt_drive_cnt = 0;
						real_speed = 0;
						printString("MAXSPEED = ");printd(MAXSPEED);printString("\n");
						//printString("\n[CS8963]: SENSORLESS ST\n");
						motor_start = 1;
						RESET_time();
						SETUP_start_time();
						Start_Motor_Sensorless();
						return;
				}
				mt_drive_cnt = 0;

				if(motor_start == 1)
				{
					if(real_speed > MINSPEED)
						motor_start = 0;
				}
				//printS('r');printd(real_speed);printS('d');printd(PWM_duty);printS(' ');
			}
			else if(flag_sensor_type == PCA_MODE)
			{
				//TBD
			}
			else
				printString("Unknown Sensor Mode\n");


			#ifdef USE_LOW_SPEED_WARNING
			if(real_speed < MINSPEED)
				P0_1 = 0;
			else
				P0_1 = 1;
			#endif

			//Consider lock rotor protection
			if(real_speed < MINSPEED)
				check_speed++;
			else
				check_speed = 0;

			#if defined(STAR) || defined(STAR_V17) || defined(HD)
			if((real_speed < MINSPEED) && (check_speed == 20) && (MtState == start))	// 0.1*20 = 2.0 sec
			#else
			if((real_speed < MINSPEED) && (check_speed == 10) && (MtState == start))	// 0.1*10 = 1.0 sec
			#endif
			{
				check_speed = 0;
				PINT0EN = 0;
				PWM16_disable();
				//printString("r:");printd(real_speed);printS(' ');
				//printString("m:");printd(MINSPEED);printS(' ');
				DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);

				if(flag_sensor_type == HALL_SENSOR_MODE)
				{
					get_current_hall_state();
					if((Hal_sta<1)||(Hal_sta>6))
					{
						Stop_Motor();
						printString("\n");printString("Invalid Hall Sensor status. Please check the Hall sensor.  Hal_sta = ");printd(Hal_sta);printString("\n");
						return;
					}
				}

				if((flag_sensor_type == HALL_SENSOR_MODE)&&(over_current_count>0)&&(over_current_count<5)&&(over_current_retry<5))
				{	//For HD cold-motor start issue
					PINT0EN = 0;
					over_current_retry++;
					printString("No Move, over_current_retry = ");printd(over_current_retry);printString("\n");

					power_warning_count = ENABLE_POWER_WARNING_SLOW;
					Initial_PWM16(PWM_period, PWM_duty);					//Initial PWM16
					get_current_hall_state();
					if(flag_run_dir == CW)
						MT_drive(Hal_sta);
					else
						MT_drive(7 - Hal_sta);
					PINT0EN = 1;
				}
				else
				{
					PWM_duty += PWM_START_DUTY_INC;
					SETUP_PWM_duty_target(PWM_duty);
					if(PWM_duty > PWM_START_DUTY_END)
					{
						PWM_duty = PWM_start_duty;
						PINT0EN = 0;
						PWM16_disable();
						MtState = stop;
						SETUP_target_speed(0);
						real_speed = 0;
						hall_fail_cnt = 0;
						power_warning_count = ENABLE_POWER_WARNING_FAST;
						printString("\n");printString("\n");
						printString("A real_speed = ");printd(real_speed);printString("\n");
						for(i=0;i<5;i++)
						{
							printString("LOCK ROTOR PROTECTION, STOP, RESET to restart....\n");
						}
						#ifdef USE_MYSONLINK
						ERROR_number = _ERROR_LOCK_ROTOR;
						for(i=0;i<10;i++)
						{
							Send_Motor_Error_Cmd(ERROR_number);
							DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						}
						#endif
					}
					else
					{
						motor_restart++;
						printString("No move, start PWM again, PWM Duty:");printd(PWM_duty);printString(",\trestart_cnt = ");printd(motor_restart);printString("\n");
	
						if(flag_sensor_type == HALL_SENSOR_MODE)
						{
							PINT0EN = 0;
							PWM16_disable();
							Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
							get_current_hall_state();
							if(flag_run_dir == CW)
								MT_drive(Hal_sta);
							else
								MT_drive(7 - Hal_sta);
							PINT0EN = 1;
						}
						else if(flag_sensor_type == SENSORLESS_MODE)
						{
							//printString("\n[CS8963]: SENSORLESS ST\n");
							motor_start = 1;
							RESET_time();
							SETUP_start_time();
							Start_Motor_Sensorless();
						}
					}
				}
			}
			if(flag_mode_type == CLOSE_LOOP)
			{
				count_mode_type++;
				#ifdef CALCULATE_SPEED_BY_PWM
				#ifdef HD
				if(count_mode_type == 4)
				#else
				if(count_mode_type == 2)
				#endif
				#else
				if(count_mode_type == 5)
				#endif
				{
					flag_check_speed = 1;
					count_mode_type=0;
				}
			}
		}		//end of if(MtState == start)
		else if((MtState == start) && (flag_sensor_type == PCA_MODE))
		{
			real_speed = (Hal_cnt*101)/(number_motor_pole_pair);		//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
			real_speed_tmp = real_speed;
			if(real_speed_tmp > 30000)
				printString("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxx\n");
			Hal_cnt = 0;
		}
	}		//end of if(++t0_cnt == 2)

	timer0_check_cnt++;

	if((timer0_check_cnt%16) == 0)	//50*16 = 0.8s
		flag_check_vdc = 1;
	else if((timer0_check_cnt%16) == 3)
		flag_check_vr = 1;
	else if((timer0_check_cnt%16) == 6)
		flag_check_over_current = 1;
	#ifdef TEST_START
	else if((timer0_check_cnt%16) == 9)
		flag_check_test_start = 1;
	#endif
	else if((timer0_check_cnt%32) == 13)	//50ms*32 = 1.6s
		flag_check_debug_message = 1;

	if(MtState == start)
	{
		if((timer0_check_cnt % 16) == 12)
			flag_check_lock_rotor = 1;
	}

	/*
	if(MtState == start)
	{
	*/
		/*
		#ifdef M_MODIFY_SPEED_3
		if(++PID_change_cnt >= 150)		//5ms*150 = 750ms
		#elif defined M_MODIFY_SPEED_2
		if(++PID_change_cnt >= 100)		//5ms*100 = 500ms
		#elif defined M_MODIFY_SPEED_1
		if(++PID_change_cnt >= 50)		//5ms* 50 = 250ms
		#endif
		*/
		/*
		//if(++PID_change_cnt >= m_modify_count)
		if(++PID_change_cnt >= 20)
		{
			flag_check_speed = 1;
			PID_change_cnt = 0;
		}
	}
	*/

#ifdef ENABLE_POWER_WARNING
	if((timer0_check_cnt % power_warning_count) == 0)
		do_power_warning();
#endif

	TH0 = 0x00;				//Timer 0 count start point
	TL0 = 0x00;	
}

#ifndef USE_MYSONLINK
void EUART2(void) interrupt 6
{
	BYTE SBUF2_temp;
	if(EUART2_TIF)							//transmit interrupt
	{
		EUART2_TIF_CLR;
	}

	if(EUART2_RIF)							//receive interrupt
	{
		EUART2_RIF_CLR;
		SBUF2_temp = SBUF2;					//EUART Receive Data

		/*
		if(SBUF2_temp == 0x0d)
		{
			printString("\n");
		}
		else
		{
			printS(SBUF2_temp);
		}
		*/
		buffer[ptr] = SBUF2_temp;
		ptr++;

		if(SBUF2_temp == 0x0d)
		{
			/*
			for(i=0;i<ptr;i++)
			{
				printS(buffer[i]);
			}
			printString("\n");
			*/
			length = ptr;
			ptr = 0;
			#ifndef LESS_CODE
			parse_euart2_command();
			#endif
		}
		if(MtState == stop)
		{
			if(SBUF2_temp == 0x0d)
			{
				printString("\n");
				printString(PROMPT);
			}
			else
			{
				printS(SBUF2_temp);
			}
		}
	}	
	SINT2 = 0xa0;	//only EUART2 need use it!!!,other UARTs needn't.
	EA = 1;
}

#ifndef LESS_CODE
void parse_euart2_command()
{
	int i;
	BYTE Hal_sta_new;
	BYTE vr_duty = 0;
	UINT DAC_data = 0;
	ULONG voltage;
	ULONG cnt1 = 0;
	SINT error_speed = 0;
	UINT target_speed_tmp = 0;
	#ifdef TEST_START
	ULONG time_t5 = 0;
	#endif

	if(length == 8)
	{
		if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x35) || (buffer[3] < 0x30) || (buffer[3] > 0x39) 
			|| (buffer[4] < 0x30) || (buffer[4] > 0x39) || (buffer[5] < 0x30) || (buffer[5] > 0x39)
			|| (buffer[6] < 0x30) || (buffer[6] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			target_speed_tmp = (buffer[2] - 0x30) * 10000 + (buffer[3] - 0x30) * 1000 + (buffer[4] - 0x30) * 100 + (buffer[5] - 0x30) * 10 + (buffer[6] - 0x30);
			SETUP_target_speed(target_speed_tmp);
			printString("\nTarget_speed: ");printd(target_speed);printString("\n");
		}
	}
	else if(length == 7)
	{
		if((buffer[0] == 'u')&&(buffer[1] == 'p')&&(buffer[2] == 't')&&(buffer[3] == 'i')&&(buffer[4] == 'm')&&(buffer[5] == 'e'))
		{
			printString("\n");
			//Get System Up time
			get_system_up_time();
		}
		else if((buffer[0] == 's')&&(buffer[1] == 'e')&&(buffer[2] == 'n')&&(buffer[3] == 's')&&(buffer[4] == 'o')&&(buffer[5] == 'r'))
		{
			if(MtState == stop)
			{
				if(flag_sensor_type == SENSORLESS_MODE)
				{
					SETUP_sensor_mode(HALL_SENSOR_MODE);
					printString("\nHall Sensor Mode\n");
				}
				else if(flag_sensor_type == HALL_SENSOR_MODE)
				{
					SETUP_sensor_mode(SENSORLESS_MODE);
					printString("\nSensorless Mode\n");
				}
				else
				{
					SETUP_sensor_mode(HALL_SENSOR_MODE);
					printString("\nHall Sensor Mode\n");
				}
			}
		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39) 
			|| (buffer[4] < 0x30) || (buffer[4] > 0x39) || (buffer[5] < 0x30) || (buffer[5] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			target_speed_tmp = (buffer[2] - 0x30) * 1000 + (buffer[3] - 0x30) * 100 + (buffer[4] - 0x30) * 10 + (buffer[5] - 0x30);
			SETUP_target_speed(target_speed_tmp);
			printString("\nTarget_speed: ");printd(target_speed);printString("\n");
		}
	}
	else if(length == 6)
	{
		if((buffer[0] == 'c')&&(buffer[1] == 'l')&&(buffer[2] == 'o')&&(buffer[3] == 'c')&&(buffer[4] == 'k'))
		{
			printString("\n");
			printString("Clock Mode, enable T5\n");
			Initial_Timer5();											//Initial Timer5
		}
		else if((buffer[0] == 'p')&&(buffer[1] == 'r')&&(buffer[2] == 'i')&&(buffer[3] == 'n')&&(buffer[4] == 't'))
		{
			printString("\n");
			printString("print test........,  Press RESET to EXIT.\n");
			while(1)
			{
				for(i=0;i<26;i++)
				{
					printS(0x41+i);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
			}
		}
		else if((buffer[0] == 'b')&&(buffer[1] == 'r')&&(buffer[2] == 'a')&&(buffer[3] == 'k')&&(buffer[4] == 'e'))
		{
			if(flag_enable_brake == 0)
			{
				SETUP_enable_brake(1);
				printString("\nEnable BRAKE\n");
			}
			else
			{
				SETUP_enable_brake(0);
				printString("\nDisable BRAKE\n");
			}
		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39) 
			|| (buffer[4] < 0x30) || (buffer[4] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			target_speed_tmp = (buffer[2] - 0x30) * 100 + (buffer[3] - 0x30) * 10 + (buffer[4] - 0x30);
			SETUP_target_speed(target_speed_tmp);
			printString("\nTarget_speed: ");printd(target_speed);printString("\n");
		}
	}
	else if(length == 5)
	{
		if((buffer[0] == 'h')&&(buffer[1] == 'e')&&(buffer[2] == 'l')&&(buffer[3] == 'p'))
		{
			printString("\n");
			printString("BLDC command prompt, ");
			printString(RELEASE_INFO);
			printString("\n");
			printString("help: help menu\n");
			printString("s: start/stop\n");
			printString("r: reset\n");
			printString("m: message\n");
			printString("w: CW/CCW\n");
			printString("k: brake\n");
			printString("0: restore to default value\n");
			printString("u: current protection on/off\n");
			printString("o: lock rotor protection on/off\n");
			printString("x: open/close loop\n");
			printString("+: duty+1 / speed+step\n");
			printString("-: duty-1 / speed-step\n");
			printString("1: dty=10, 2:dty=20, 3:dty=30, 4:dty=40, 5:dty=50, 6:dty=60, 7:dty=70, 8:dty=80, 9:dty=90\n");
			printString("1: 1000rpm,2:2000rpm,3:3000rpm,4:4000rpm,5:5000rpm,6:6000rpm,7:7000rpm,8:8000rpm,9:9000rpm\n");
			printString("A: prd=0x100,B:prd=0x140,C:prd=0x180,D:prd=0x1c0,E:prd=0x200,F:prd=0x240,...,I:prd=0x300\n");
			printString("l: list current setting\n");
			printString("n: test hall status\n");
			printString("h: show hall status\n");
			printString("d: show current status\n");
			printString("p: print test result\n");
			printString("M: test gate driver\n");
			printString("v: test read ADC\n");
			printString("=: get system up time\n");
			printString("\\: switch motor UVW sequence\n");
			printString("`: motor auto one step\n");
			printString("^1: motor step 1\n");
			printString("^2: motor step 2\n");
			printString("^3: motor step 3\n");
			printString("^4: motor step 4\n");
			printString("^5: motor step 5\n");
			printString("^6: motor step 6\n");
			printString("vr:  VR  test\n");
			printString("adc: ADC test\n");
			printString("dac: DAC test\n");
			printString("slow: slow modify duty\n");
			printString("fast: fast modify duty\n");
			printString("hall: test hall sequence\n");
			printString("lock: lock/unlock rotor\n");
			printString("print: UART test\n");
			printString("sensor: Hall sensor / Sensorless switch\n");
			printString("p n: setup motor pole-pair (n=1~9)\n");
			printString("s n: setup start_duty (n=0~99)\n");
			printString("d n: setup duty (n=0~99)\n");
			printString("t n: setup target_speed (n=10~59999)\n");
			printString("{}: decrease/increase phase compensation angle\n");
			printString("[]: decrease/increase PWM period\n");
			printString("<>: decrease/increase PWM deadtime\n");
		}
		else if((buffer[0] == 'h')&&(buffer[1] == 'a')&&(buffer[2] == 'l')&&(buffer[3] == 'l'))
		{
			printString("\n");
			printString("TEST HALL Sensor sequence ST\n");
			if(flag_test_hall_sequence_mode == 1)
			{
				printString("TEST HALL SEQUENCE MODE : OFF\n");
				flag_test_hall_sequence_mode = 0;
				PINT0EN = 0;
			}
			else
			{
				printString("TEST HALL SEQUENCE MODE : ON, manual hall sequence check\n");
				flag_test_hall_sequence_mode = 1;
				Hal_sta_tmp=0;
				PINT0EN = 1;
			}
		}
		else if((buffer[0] == 's')&&(buffer[1] == 'l')&&(buffer[2] == 'o')&&(buffer[3] == 'w'))
		{
			if(MtState == stop)
			{
				if(slow_modify_speed < 100)
					slow_modify_speed++;
				printString("slow modify speed = ");printd(slow_modify_speed);printString("\n");
			}
		}
		else if((buffer[0] == 'f')&&(buffer[1] == 'a')&&(buffer[2] == 's')&&(buffer[3] == 't'))
		{
			if(MtState == stop)
			{
				if(slow_modify_speed >= 1)
					slow_modify_speed--;
				printString("slow modify speed = ");printd(slow_modify_speed);printString("\n");
			}
		}
		else if((buffer[0] == 's')&&(buffer[1] == 'a')&&(buffer[2] == 'v')&&(buffer[3] == 'e'))
		{
			printString("\n");
			printString("Save parameters to flash\tTBD\n");
		}
		else if((buffer[0] == 'l')&&(buffer[1] == 'o')&&(buffer[2] == 'a')&&(buffer[3] == 'd'))
		{
			printString("\n");
			printString("Load parameters from flash\tTBD\n");
		}
		else if((buffer[0] == 'l')&&(buffer[1] == 'o')&&(buffer[2] == 'c')&&(buffer[3] == 'k'))
		{
			if(lock_on_off == 0)
			{
				lock_on_off = 1;
				printString("\nLock ON\n");
				MT_Lock(lock_on_off);
			}
			else
			{
				lock_on_off = 0;
				printString("\nLock OFF\n");
				MT_Lock(lock_on_off);
			}
		}
		else if((buffer[0] == 'r')&&(buffer[1] == 'e')&&(buffer[2] == 'a')&&(buffer[3] == 'l'))
		{
			if(PCA_use_real_hall == 0)
			{
				PCA_use_real_hall = 1;
				printString("\nPCA Use Real Hall\n");
			}
			else
			{
				PCA_use_real_hall = 0;
				printString("\nPCA Use Sensorless Hall\n");
			}
		}
		else if((buffer[0] == 's')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			PWM_start_duty = (buffer[2] - 0x30) * 10 + (buffer[3] - 0x30);
			printString("\nPWM_start_duty: ");printd(PWM_start_duty);printString("\n");
		}
		else if((buffer[0] == 'd')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			PWM_duty = (buffer[2] - 0x30) * 10 + (buffer[3] - 0x30);
			printString("\nPWM_duty: ");printd(PWM_duty);printString("\n");
		}
		else if((buffer[0] == 't')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x30) || (buffer[2] > 0x39) || (buffer[3] < 0x30) || (buffer[3] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			target_speed_tmp = (buffer[2] - 0x30) * 10 + (buffer[3] - 0x30);
			SETUP_target_speed(target_speed_tmp);
			printString("\nTarget_speed: ");printd(target_speed);printString("\n");
		}
	}
	else if(length == 4)
	{
		if((buffer[0] == 'd')&&(buffer[1] == 'a')&&(buffer[2] == 'c'))
		{
			printString("\n");
			printString("DAC Mode........,  Use P1.7_pin1, P2.2_pin29, P3.2_pin23, Press RESET to EXIT.\n");
			
			PIN_CONFIG_setup_dac(_P1_7);
			PIN_CONFIG_setup_dac(_P2_2);
			PIN_CONFIG_setup_dac(_P3_2);

			while(1)
			{
				for(i=0;i<20;i++)
				{
					DAC_data=i*51;printd(DAC_data);printS(' ');Setup_DAC_Data(DAC_data>>8,DAC_data&0xff);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
				for(i=0;i<51;i++)
				{
					printd(i*100);printS(' ');Setup_DAC_Voltage(i*100);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
			}
		}
		else if((buffer[0] == 'v')&&(buffer[1] == 'd')&&(buffer[2] == 'c'))
		{
			printString("\n");
			printString("VDC Mode........,  Press RESET to EXIT.\n");
			printString("ADC, pin ");printd(SAMPLE_DCBUS_ADC);printString("\n");
			while(1)
			{
				get_vdc_voltage();
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
		}
		else if((buffer[0] == 'a')&&(buffer[1] == 'd')&&(buffer[2] == 'c'))
		{
			printString("\n");
			printString("Test ADC in CB2209A/B/C/D........,  Press RESET to EXIT.\n");
			printString("ADC, pin ");printd(SAMPLE_CURRENT_ADC);printString("\n");
			while(1)		//CM2209A/B/C/D test ADC
			{
				cnt1++;
				if((cnt1%(VR_PROBE_SPEED*20))==0)
				{
					Initial_ADC(SAMPLE_CURRENT_ADC);						//Initial ADC A channel for sample current, pin18
					Get_ADC_Result(SAMPLE_CURRENT_ADC);
					Disable_ADC(SAMPLE_CURRENT_ADC);
					printString("ADC=");printd(ADC_A_result);
					voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;	//mV
					printString(", V=");printd(voltage);printString(" mV;\n");
				}
			}
		}
		else if((buffer[0] == 'i')&&(buffer[1] == 'f')&&(buffer[2] == 'b'))
		{
			IFB_Read_256Byte();					//Print Information Block (IFB) data.
		}
		else if((buffer[0] == 'p')&&(buffer[1] == 'c')&&(buffer[2] == 'a'))
		{
			if(MtState == stop)
			{
				SETUP_sensor_mode(PCA_MODE);
				PCA_Mode_Setup();
			}
		}
		else if((buffer[0] == 'p')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x31) || (buffer[2] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			number_motor_pole_pair = buffer[2] - 0x30;
			printString("\npole-pair: ");printd(number_motor_pole_pair);printString("\n");
		}
		else if((buffer[0] == 's')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x31) || (buffer[2] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			PWM_start_duty = buffer[2] - 0x30;
			printString("\nPWM_start_duty: ");printd(PWM_start_duty);printString("\n");
		}
		else if((buffer[0] == 'd')&&(buffer[1] == ' '))
		{
			if((buffer[2] < 0x31) || (buffer[2] > 0x39))
			{
				printString("\nIllegal parameters.\n");
				return;
			}
			PWM_duty = buffer[2] - 0x30;
			printString("\nPWM_duty: ");printd(PWM_duty);printString("\n");
		}
	}
	else if(length == 3)
	{
		if(((buffer[0] == 'l')&&(buffer[1] == 's'))||(buffer[0] == 'l')&&(buffer[1] == 'l'))
		{
			printString("\n");
			printString("Type `help' to see help list.\n");
		}
		else if((buffer[0] == 'v')&&(buffer[1] == 'r'))
		{
			printString("\n");
			printString("Test VR in CB2209A/B/C........,  Press RESET to EXIT.\n");
			printString("VR, pin ");printd(PIN_VRin);printString("\n");
			while(1)		//CM2209A/B/C test VR
			{
				cnt1++;
				if((cnt1%(VR_PROBE_SPEED*10))==0)
				{
					do_check_VR_open_loop_test();
					DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
					DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
					do_check_VR_close_loop_test();
					DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
					DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
				}
			}
		}
	}
	else if(length == 2)
	{
		printString("\n");
		if(buffer[0] == '0')
		{
			printString("DEFAULT\n");
			SETUP_target_speed(TARGET_SPEED);
			SETUP_PWM_period(PWM_PERIOD);
			SETUP_PWM_duty(PWM_START_DUTY);
			SETUP_direction(DIRECTION);
			SETUP_slow_modify_speed(SLOW_MODIFY_SPEED);
			SETUP_speed_control_mode(SPEED_CONTROL_MODE);
			SETUP_mode_type(MODE_TYPE);
			SETUP_debug_mode(DEBUG_MODE);
			SETUP_phase_compensation_mode(ENABLE_PHASE_COMPENSATION);
			SETUP_enable_watchdog(ENABLE_WATCHDOG);
			SETUP_enable_over_current_protection(ENABLE_OVER_CURRENT_PROTECTION_A|(ENABLE_OVER_CURRENT_PROTECTION_C<<1)|(ENABLE_OVER_CURRENT_PROTECTION_X<<2));
			SETUP_enable_lock_rotor_protection(ENABLE_LOCK_ROTOR_PROTECTION);
			SETUP_motor_pole_pair(MOTOR_POLE_PAIR);
			//SETUP_motor_uvw_sequence(MOTOR_UVW_SEQUENCE_TYPE);
			Initial_PWM16(PWM_period,PWM_duty);
		}
		else if(buffer[0] == '1')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 10;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(1000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '2')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 20;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(2000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}		
		else if(buffer[0] == '3')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 30;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(3000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '4')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 40;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(4000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '5')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 50;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(5000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '6')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 60;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(6000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '7')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 70;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(7000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '8')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 80;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(8000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '9')
		{
			if(flag_mode_type == OPEN_LOOP)
			{
				PWM_duty_old  = PWM_duty;
				PWM_duty = 90;
				if(MtState == stop)
				{
					printString("Duty:");printd(PWM_duty);printString("\n");
				}
				PWM16_Modify(PWM_period, PWM_duty);
			}
			else if(flag_mode_type == CLOSE_LOOP)
			{
				SETUP_target_speed(9000);
				if(MtState == stop)
				{
					printString("Target:");printd(target_speed);printString("\n");
				}
			}
		}
		else if(buffer[0] == '+')
		{
			if(flag_sensor_type == PCA_MODE)
			{
				if(PCA_duty > 245)
					PCA_duty = 255;
				else
					PCA_duty += 10;
				printString("PCA Duty +10, Duty:");printd(PCA_duty);printString("\n");
				PCA8_Modify(PCA_duty);
			}
			else
			{
				if(flag_mode_type == OPEN_LOOP)
				{
					//Modify duty
					PWM_duty_old  = PWM_duty;
					PWM_duty += 1;
					if(PWM_duty > 100)
						PWM_duty = 100;
					if(MtState == stop)
					{
						printString("Duty +1, Duty:");printd(PWM_duty);printString("\n");
					}
					PWM16_Modify(PWM_period, PWM_duty);
	
					//Modify period
					//PWM_period *= 2;
					//printString("period * 2, Period: ");printd(PWM_period);printString("\n");
					//Initial_PWM16(PWM_period, PWM_duty);
				}
				else if(flag_mode_type == CLOSE_LOOP)
				{
					/*
					target_speed += 200;
					if(target_speed > MAXSPEED)
						target_speed = MAXSPEED;
					printString("Target + 200, Target: ");printd(target_speed);printString("\n");
					*/
					target_speed_tmp = target_speed + number_rpm_step_size;
					SETUP_target_speed(target_speed_tmp);
					if(target_speed > MAXSPEED)
						target_speed = MAXSPEED;
					if(MtState == stop)
					{
						printString("Target + "); printd(number_rpm_step_size);printString(", Target: ");printd(target_speed);printString("\n");
					}
				}
			}
		}		
		else if(buffer[0] == '-')
		{
			if(flag_sensor_type == PCA_MODE)
			{
				if(PCA_duty <= 10)
					PCA_duty = 0;
				else
					PCA_duty -= 10;
				printString("PCA Duty -10, Duty:");printd(PCA_duty);printString("\n");
				PCA8_Modify(PCA_duty);
			}
			else
			{
				if(flag_mode_type == OPEN_LOOP)
				{
					//Modify duty
					PWM_duty_old  = PWM_duty;
					if(PWM_duty == 0)
						PWM_duty = 0;
					else
						PWM_duty -= 1;
					if(MtState == stop)
					{
						printString("Duty -1, Duty:");printd(PWM_duty);printString("\n");
					}
					PWM16_Modify(PWM_period, PWM_duty);
	
					//Modify period
					//PWM_period /= 2;
					//printString("period / 2, Period: ");printd(PWM_period);printString("\n");
					//Initial_PWM16(PWM_period, PWM_duty);
				}
				else if(flag_mode_type == CLOSE_LOOP)
				{
					/*
					target_speed -= 200;
					if(target_speed < MINSPEED)
						target_speed = MINSPEED;
					printString("Target - 200, Target:");printd(target_speed);printString("\n");
					*/
					target_speed_tmp = target_speed - number_rpm_step_size;
					SETUP_target_speed(target_speed_tmp);
					if(target_speed < MINSPEED)
						target_speed = MINSPEED;
					if(MtState == stop)
					{
						printString("Target - "); printd(number_rpm_step_size);printString(", Target: ");printd(target_speed);printString("\n");
					}
				}
			}
		}		
		else if(buffer[0] == '{')
		{
			//Modify phase angle, decrease
			if(flag_phase_compensation_mode)
			{
				if(phase_angle <= 0)
					phase_angle = 0;
				else
					phase_angle -= 1;
				printString("phase_angle -1, phase_angle:");printd(phase_angle);printString("\n");
			}
			else
				printString("Invalid command for non-phase-compensation mode\n");
		}		
		else if(buffer[0] == '}')
		{
			//Modify phase angle, increase
			if(flag_phase_compensation_mode)
			{
				if(phase_angle >= 120)
					phase_angle = 120;
				else
					phase_angle += 1;
				printString("phase_angle +1, phase_angle:");printd(phase_angle);printString("\n");
			}
			else
				printString("Invalid command for non-phase-compensation mode\n");
		}
		#ifndef STAR_V17
		else if(buffer[0] == '[')
		{
			//Modify period
			if(PWM_period <= 0x10)
				PWM_period = 0x10;
			else
				PWM_period -= 0x10;
			printString("Period -16, Period:0x");printx(PWM_period);printS('=');printd(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}		
		else if(buffer[0] == ']')
		{
			//Modify period
			if(PWM_period >= 0x7fef)
				PWM_period = 0x7fff;
			else
				PWM_period += 0x10;
			printString("Period +16, Period:0x");printx(PWM_period);printS('=');printd(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		#endif
		else if(buffer[0] == '<')
		{
			//Modify PWM dead time
			PWM_dead_time = PWM16CFG & 0x1f;
			if(PWM_dead_time <= 0)
				PWM_dead_time = 0;
			else
				PWM_dead_time--;
			printString("PWM_dead_time -1, PWM_dead_time:0x");printx(PWM_dead_time);printS('=');printd(PWM_dead_time);printString(" (transitions)\n");
			PWM16CFG = (PWM16CFG&0xE0)|PWM_dead_time;
		}		
		else if(buffer[0] == '>')
		{
			//Modify PWM dead time
			PWM_dead_time = PWM16CFG & 0x1f;
			if(PWM_dead_time >= 31)
				PWM_dead_time = 31;
			else
				PWM_dead_time++;
			printString("PWM_dead_time +1, PWM_dead_time:0x");printx(PWM_dead_time);printS('=');printd(PWM_dead_time);printString(" (transitions)\n");
			PWM16CFG = (PWM16CFG&0xE0)|PWM_dead_time;
		}
		#ifndef STAR_V17
		else if(buffer[0] == 'A')
		{
			PWM_period = 0x100;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'B')
		{
			PWM_period = 0x140;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'C')
		{
			PWM_period = 0x180;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'D')
		{
			PWM_period = 0x1c0;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'E')
		{
			PWM_period = 0x200;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'F')
		{
			PWM_period = 0x240;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'G')
		{
			PWM_period = 0x280;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'H')
		{
			PWM_period = 0x2c0;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		else if(buffer[0] == 'I')
		{
			PWM_period = 0x300;
			printString("Freq:0x");printx(PWM_period);printString("\n");
			Initial_PWM16(PWM_period, PWM_duty);
		}
		#endif
		else if(buffer[0] == 'P')
		{
			/*
			if(flag_phase_compensation_mode == 1)
			{
				printString("Phase Compensation mode OFF\n");
				SETUP_phase_compensation_mode(0);
			}
			else
			{
				printString("Phase Compensation mode ON, phase_angle = ");printd(phase_angle);printString("\n");
				SETUP_phase_compensation_mode(1);
			}
			*/
			if(flag_hall_protection == 1)
			{
				SETUP_enable_hall_protection(0);
			}
			else
			{
				SETUP_enable_hall_protection(1);
			}
		}
		else if(buffer[0] == 'g')
		{
			#ifdef DUMP_PWM_SETUP
			real_speed_tmp = real_speed;
			PWM_period_tmp = PWM_period;
			PWM_duty_tmp = PWM_duty;
			Hal_sta_tmp = Hal_sta;
			PWMAL_tmp = PWMAL;
			PWMAH_tmp = PWMAH;
			PWMBL_tmp = PWMBL;
			PWMBH_tmp = PWMBH;
			PWMCL_tmp = PWMCL;
			PWMCH_tmp = PWMCH;
			PWMTRG0L_tmp = PWMTRG0L;
			PWMTRG0H_tmp = PWMTRG0H;
			PWMTRG1L_tmp = PWMTRG1L;
			PWMTRG1H_tmp = PWMTRG1H;
			PWMCNTL_tmp = PWMCNTL;
			PWMCNTH_tmp = PWMCNTH;
			PWMPRDL_tmp = PWMPRDL;
			PWMPRDH_tmp = PWMPRDH;
			PWM16CFG_tmp = PWM16CFG;
			PWM16INT_tmp = PWM16INT;
			#endif
		}
		else if(buffer[0] == 'X')		//static PWM single step
		{
			if(static_pwm_mode == 1)
			{
				printString("Static PWM mode OFF\n");
				static_pwm_mode = 0;
			}
			else
			{
				printString("Static PWM mode ON\n");
				static_pwm_mode = 1;
			}
		}
		else if(buffer[0] == '`')	//auto one step
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printd(Hal_sta);Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(Hal_sta);
			else
				MT_drive(7 - Hal_sta);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == 'w')
		{
			if(MtState == stop)
			{
				if(flag_run_dir == CW)
				{
					SETUP_direction(CCW);
					printString("CCW\n");
					if(flag_sensor_type == PCA_MODE)
						P1_2 = 0;
				}
				else
				{
					SETUP_direction(CW);
					printString("CW\n");
					if(flag_sensor_type == PCA_MODE)
						P1_2 = 1;
				}
				if(flag_phase_compensation_mode)
				{
					if(flag_run_dir == CW)
						phase_angle = PHASE_ANGLE_CW;
					else
						phase_angle = PHASE_ANGLE_CCW;
					printString("phase_angle:");printd(phase_angle);printString("\n");
				}
			}
		}
		else if(buffer[0] == 'm')
		{
			if(flag_debug_mode == 1)
			{
				printString("DEBUG:OFF\n");
				flag_debug_mode = 0;
			}
			else
			{
				printString("DEBUG:ON\n");
				flag_debug_mode = 1;
			}
		}
		else if(buffer[0] == 'x')
		{
			if(MtState == stop)
			{
				if(flag_mode_type == OPEN_LOOP)
				{
					printString("CLOSE LOOP, target_speed: ");printd(target_speed);printString("\n");
					SETUP_mode_type(CLOSE_LOOP);
				}
				else if(flag_mode_type == CLOSE_LOOP)
				{
					printString("OPEN LOOP, Duty = ");printd(PWM_duty);printString("\n");
					SETUP_mode_type(OPEN_LOOP);
				}
			}
		}
		else if(buffer[0] == 'y')
		{
			printString("TEST HALL Sensor sequence ST\n");
			if(flag_test_hall_sequence_mode == 1)
			{
				printString("TEST HALL SEQUENCE MODE : OFF\n");
				flag_test_hall_sequence_mode = 0;
				PINT0EN = 0;
			}
			else
			{
				printString("TEST HALL SEQUENCE MODE : ON, manual hall sequence check\n");
				flag_test_hall_sequence_mode = 1;
				Hal_sta_tmp=0;
				PINT0EN = 1;
			}
		}
		else if(buffer[0] == 'M')
		{
			printString("TEST Gate Driver........,  Press RESET to EXIT,\t");
			if(flag_run_dir == CW)
				printString("CW\n");
			else
				printString("CCW\n");
			Initial_PWM16_Test_Gate_Driver(PWM_period, 20, 20, 20);
			while(1)
			{
				if(flag_run_dir == CW)
				{
					printS('6');printS(' ');MT_drive(6);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('4');printS(' ');MT_drive(4);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('5');printS(' ');MT_drive(5);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('1');printS(' ');MT_drive(1);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('3');printS(' ');MT_drive(3);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('2');printS(' ');MT_drive(2);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
				else	//CCW
				{
					printS('5');printS(' ');MT_drive(5);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('4');printS(' ');MT_drive(4);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('6');printS(' ');MT_drive(6);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('2');printS(' ');MT_drive(2);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('3');printS(' ');MT_drive(3);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					printS('1');printS(' ');MT_drive(1);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
			}
		}
		else if(buffer[0] == 'v')
		{
			printString("TEST READ ADC RESULT ST\n");
			while(1)
			{
				printString("\n");
				Get_ADC_Result(SAMPLE_CURRENT_ADC);
				printString("ADC_A_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
				printString("v_out = ");printv(voltage);printString(" V ");
				printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
				printString("sample_current = ");printd(voltage/VOLTAGE_GAIN/RESISTANCE);printString(" mA\n");
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
		}
		#if defined(STAR) || defined(STAR_V17)
		else if(buffer[0] == 's')
		{
			if(MtState == stop)
				Start_Motor();
		}
		else if(buffer[0] == 'S')
		{
			Stop_Motor();
		}
		#else	//normal use
		else if(buffer[0] == 's')
		{
			if(MtState == stop)
				Start_Motor();
			else
				Stop_Motor();
		}
		#endif
		else if(buffer[0] == 'k')
		{
			MtState = stop;
			real_speed = 0;
			PINT0EN = 0;
			PWM16_disable();
			MT_Brake();
			printString("BRAKE, Hall: ");get_current_hall_state();printString("\n");
		}
		else if(buffer[0] == 'r')
		{
			PINT0EN = 0;
			PWM16_disable();
			printString("\n");
			printString("Stop & RESET\n");
			WatchDOG_Enable();
		}
		else if((buffer[0] == '=') || (buffer[0] == 't'))
		{
			//Get System Up time
			get_system_up_time();
		}
		else if(buffer[0] == 'p')
		{
			printString("print test result\n");

			#ifdef MT_DRIVE_DEBUG
				pirnt_mt_drive_value();
			#endif

			#ifdef HALL_DEBUG
			printString("HALL_array:\n");
			for(i=0; i<DEBUG_LENGTH2; i++)
			{
				printd(HALL_RESULT[i]);
				if(HALL_RESULT[i] == 1)
					printString("\n");
				else
					printS(' ');
			}
			printString("\n");
			#endif

			#ifdef RECORD_PID_DATA
			printString("pid data_array:\n");
			printString("kp = ");printd(KP);printS('\t');
			printString("ki = ");printd(KI);printS('\t');
			printString("kd = ");printd(KD);printString("\n");
			printString("step\ttgt\treal\terr\tpp\tii\tdd\tpid\n");
			for(i=0; i<DEBUG_LENGTH4; i++)
			{
				//printString("real_speed(");printd(i+1);printString(")=");printd(real_speed_array[i]);
				//printString(";PP(");printd(i+1);printString(")=");printd(pp_array[i]);
				//printString(";II(");printd(i+1);printString(")=");printd(ii_array[i]);
				//printString(";DD(");printd(i+1);printString(")=");printd(dd_array[i]);
				//printString(";PID(");printd(i+1);printString(")=");printd(pid_array[i]);printString(";\n");

				printd(i);printS('\t');
				printd(target_speed);printS('\t');
				printd(real_speed_array[i]);printS('\t');
				error_speed = target_speed - real_speed_array[i];
				printd(error_speed);printS('\t');
				printd(pp_array[i]);printS('\t');
				printd(ii_array[i]);printS('\t');
				printd(dd_array[i]);printS('\t');
				printd(pid_array[i]);printString("\n");
			}
			printString("\n");
			#endif
		}
		else if(buffer[0] == 'u')
		{
			if(flag_over_current_protection > 0)
			{
				printString("Disable over current protection\n");
				flag_over_current_protection = 0;
				Disable_Comparator();
			}
			else
			{
				printString("Enable over current protection\n");
				flag_over_current_protection = 7;
				Initial_Comparator_VTH1(CMPVTH_VALUE);					//Initial Comparator
			}
		}
		else if(buffer[0] == 'o')
		{
			if(flag_lock_rotor_protection == 1)
			{
				printString("Disable lock rotor protection\n");
				flag_lock_rotor_protection = 0;
			}
			else
			{
				printString("Enable lock rotor protection\n");
				flag_lock_rotor_protection = 1;
			}
		}
		else if(buffer[0] == 'h')	//read current hall state
		{
			printString("h:");get_current_hall_state();printString("\n");
		}
		else if(buffer[0] == 'd')	//read current duty and speed
		{
			flag_print_message = 1;
		}
		else if(buffer[0] == '!')	//shift 1, MT_drive(1)
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printS('1');Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(1);
			else
				MT_drive(6);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == '@')	//shift 2, MT_drive(2)
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printS('2');Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(2);
			else
				MT_drive(5);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == '#')	//shift 3, MT_drive(3)
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printS('3');Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(3);
			else
				MT_drive(4);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == '$')	//shift 4, MT_drive(4)
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printS('4');Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(4);
			else
				MT_drive(3);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == '%')	//shift 5, MT_drive(5)
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printS('5');Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(5);
			else
				MT_drive(2);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == '^')	//shift 6, MT_drive(6)
		{
			if(static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();printS('6');Hal_sta_old = Hal_sta;
			if(flag_run_dir == CW)
				MT_drive(6);
			else
				MT_drive(1);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			if(!static_pwm_mode)
				PWM16_disable();
			DelayXms(100);get_current_hall_state();Hal_sta_new=Hal_sta;
			if(Hal_sta_new != Hal_sta_old)
				printString("     Moved\n");
			else
				printString("\n");
		}
		else if(buffer[0] == 'L')
		{
			printString("List factory data.\n");
#ifdef SAVE_FACTORY_DATA
			//Get System Up time
			get_system_up_time();
#endif
		}
		else if(buffer[0] == 'l')
		{
			printString("List current settings.");
			Show_SETUP_Info();
			printString("Now: \n");
			printString("Duty:");printd(PWM_duty);printS(' ');
			printString("Period: 0x");printx(PWM_period);
			printString(" Target:");printd(target_speed);
			printString(" RPM:");printd(real_speed);printString("\n");
			printString("Hall status: ");get_current_hall_state();printString("\n");
			printString("Hall sequence: ");
			if(flag_hall_sequence == HALL_SEQ_546)
				printString("5 4 6 2 3 1\n");
			else if(flag_hall_sequence == HALL_SEQ_645)
				printString("6 4 5 1 3 2\n");
			else
				printString("Unknown\n");
			//Get System Up time
			get_system_up_time();
/*
			printString("READ ADC RESULT:\n");
			for(i=1;i<10;i++)
			{
				Get_ADC_Result(SAMPLE_CURRENT_ADC);
				printString("ADC_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
				//voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
				printString("v_out = ");printv(voltage);printString(" V ");
				printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
				printString("sample_current = ");printd(voltage/VOLTAGE_GAIN/RESISTANCE);printString(" mA\n");
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
*/
/*
			printString("Dump SYSTEM data.\n");
			printString("IOCFGP0_0=0x");printx(IOCFGP0_0);printS(';');
			printString("IOCFGP0_1=0x");printx(IOCFGP0_1);printS(';');
			printString("IOCFGP0_2=0x");printx(IOCFGP0_2);printS(';');
			printString("IOCFGP0_3=0x");printx(IOCFGP0_3);printS(';');
			printString("IOCFGP0_4=0x");printx(IOCFGP0_4);printS(';');
			printString("IOCFGP0_5=0x");printx(IOCFGP0_5);printS(';');
			printString("IOCFGP0_6=0x");printx(IOCFGP0_6);printS(';');
			printString("IOCFGP0_7=0x");printx(IOCFGP0_7);printString(";\n");
			printString("IOCFGP1_0=0x");printx(IOCFGP1_0);printS(';');
			printString("IOCFGP1_1=0x");printx(IOCFGP1_1);printS(';');
			printString("IOCFGP1_2=0x");printx(IOCFGP1_2);printS(';');
			printString("IOCFGP1_3=0x");printx(IOCFGP1_3);printS(';');
			printString("IOCFGP1_4=0x");printx(IOCFGP1_4);printS(';');
			printString("IOCFGP1_5=0x");printx(IOCFGP1_5);printS(';');
			printString("IOCFGP1_6=0x");printx(IOCFGP1_6);printS(';');
			printString("IOCFGP1_7=0x");printx(IOCFGP1_7);printString(";\n");
			printString("IOCFGP2_0=0x");printx(IOCFGP2_0);printS(';');
			printString("IOCFGP2_1=0x");printx(IOCFGP2_1);printS(';');
			printString("IOCFGP2_2=0x");printx(IOCFGP2_2);printS(';');
			printString("IOCFGP2_3=0x");printx(IOCFGP2_3);printS(';');
			printString("IOCFGP2_4=0x");printx(IOCFGP2_4);printS(';');
			printString("IOCFGP2_5=0x");printx(IOCFGP2_5);printS(';');
			printString("IOCFGP2_6=0x");printx(IOCFGP2_6);printS(';');
			printString("IOCFGP2_7=0x");printx(IOCFGP2_7);printString(";\n");
			printString("IOCFGP3_0=0x");printx(IOCFGP3_0);printS(';');
			printString("IOCFGP3_1=0x");printx(IOCFGP3_1);printS(';');
			printString("IOCFGP3_2=0x");printx(IOCFGP3_2);printS(';');
			printString("IOCFGP3_3=0x");printx(IOCFGP3_3);printString(";\n");
			printString("MFCFGP0_0=0x");printx(MFCFGP0_0);printS(';');
			printString("MFCFGP0_1=0x");printx(MFCFGP0_1);printS(';');
			printString("MFCFGP0_2=0x");printx(MFCFGP0_2);printS(';');
			printString("MFCFGP0_3=0x");printx(MFCFGP0_3);printS(';');
			printString("MFCFGP0_4=0x");printx(MFCFGP0_4);printS(';');
			printString("MFCFGP0_5=0x");printx(MFCFGP0_5);printS(';');
			printString("MFCFGP0_6=0x");printx(MFCFGP0_6);printS(';');
			printString("MFCFGP0_7=0x");printx(MFCFGP0_7);printString(";\n");
			printString("MFCFGP1_0=0x");printx(MFCFGP1_0);printS(';');
			printString("MFCFGP1_1=0x");printx(MFCFGP1_1);printS(';');
			printString("MFCFGP1_2=0x");printx(MFCFGP1_2);printS(';');
			printString("MFCFGP1_3=0x");printx(MFCFGP1_3);printS(';');
			printString("MFCFGP1_4=0x");printx(MFCFGP1_4);printS(';');
			printString("MFCFGP1_5=0x");printx(MFCFGP1_5);printS(';');
			printString("MFCFGP1_6=0x");printx(MFCFGP1_6);printS(';');
			printString("MFCFGP1_7=0x");printx(MFCFGP1_7);printString(";\n");
			printString("MFCFGP2_0=0x");printx(MFCFGP2_0);printS(';');
			printString("MFCFGP2_1=0x");printx(MFCFGP2_1);printS(';');
			printString("MFCFGP2_2=0x");printx(MFCFGP2_2);printS(';');
			printString("MFCFGP2_3=0x");printx(MFCFGP2_3);printS(';');
			printString("MFCFGP2_4=0x");printx(MFCFGP2_4);printS(';');
			printString("MFCFGP2_5=0x");printx(MFCFGP2_5);printS(';');
			printString("MFCFGP2_6=0x");printx(MFCFGP2_6);printS(';');
			printString("MFCFGP2_7=0x");printx(MFCFGP2_7);printString(";\n");
			printString("MFCFGP3_0=0x");printx(MFCFGP3_0);printS(';');
			printString("MFCFGP3_1=0x");printx(MFCFGP3_1);printS(';');
			printString("MFCFGP3_2=0x");printx(MFCFGP3_2);printS(';');
			printString("MFCFGP3_3=0x");printx(MFCFGP3_3);printString(";\n");
			printString("P0_0=0x");printx(P0_0);printS(';');
			printString("P0_1=0x");printx(P0_1);printS(';');
			printString("P0_2=0x");printx(P0_2);printS(';');
			printString("P0_3=0x");printx(P0_3);printS(';');
			printString("P0_4=0x");printx(P0_4);printS(';');
			printString("P0_5=0x");printx(P0_5);printS(';');
			printString("P0_6=0x");printx(P0_6);printS(';');
			printString("P0_7=0x");printx(P0_7);printString(";\n");
			printString("P1_0=0x");printx(P1_0);printS(';');
			printString("P1_1=0x");printx(P1_1);printS(';');
			printString("P1_2=0x");printx(P1_2);printS(';');
			printString("P1_3=0x");printx(P1_3);printS(';');
			printString("P1_4=0x");printx(P1_4);printS(';');
			printString("P1_5=0x");printx(P1_5);printS(';');
			printString("P1_6=0x");printx(P1_6);printS(';');
			printString("P1_7=0x");printx(P1_7);printString(";\n");
			printString("P2_0=0x");printx(P2_0);printS(';');
			printString("P2_1=0x");printx(P2_1);printS(';');
			printString("P2_2=0x");printx(P2_2);printS(';');
			printString("P2_3=0x");printx(P2_3);printS(';');
			printString("P2_4=0x");printx(P2_4);printS(';');
			printString("P2_5=0x");printx(P2_5);printS(';');
			printString("P2_6=0x");printx(P2_6);printS(';');
			printString("P2_7=0x");printx(P2_7);printString(";\n");
			printString("P3_0=0x");printx(P3_0);printS(';');
			printString("P3_1=0x");printx(P3_1);printS(';');
			printString("P3_2=0x");printx(P3_2);printS(';');
			printString("P3_3=0x");printx(P3_3);printString(";\n");
*/
			#ifdef DUMP_PWM_SETUP
			printString("\n");
			printString("Dump PWM data\n");
			printString("Duty = ");printd(PWM_duty_tmp);
			printString(" ;Period = 0x");printx(PWM_period_tmp);
			printString(" ;RPM = ");printd(real_speed_tmp);
			printString(" ;Hall = ");printd(Hal_sta_tmp);printString(";\n");
			printString("PWMAL = 0x");printx(PWMAL_tmp);printString(";\n");
			printString("PWMAH = 0x");printx(PWMAH_tmp);printString(";\n");
			printString("PWMBL = 0x");printx(PWMBL_tmp);printString(";\n");
			printString("PWMBH = 0x");printx(PWMBH_tmp);printString(";\n");
			printString("PWMCL = 0x");printx(PWMCL_tmp);printString(";\n");
			printString("PWMCH = 0x");printx(PWMCH_tmp);printString(";\n");
			printString("PWMTRG0L = 0x");printx(PWMTRG0L_tmp);printString(";\n");
			printString("PWMTRG0H = 0x");printx(PWMTRG0H_tmp);printString(";\n");
			printString("PWMTRG1L = 0x");printx(PWMTRG1L_tmp);printString(";\n");
			printString("PWMTRG1H = 0x");printx(PWMTRG1H_tmp);printString(";\n");
			printString("PWMCNTL = 0x");printx(PWMCNTL_tmp);printString(";\n");
			printString("PWMCNTH = 0x");printx(PWMCNTH_tmp);printString(";\n");
			printString("PWMPRDL = 0x");printx(PWMPRDL_tmp);printString(";\n");
			printString("PWMPRDH = 0x");printx(PWMPRDH_tmp);printString(";\n");
			printString("PWM16CFG = 0x");printx(PWM16CFG_tmp);printString(";\n");
			printString("PWM16INT = 0x");printx(PWM16INT_tmp);printString(";\n");
			#endif
		}
		else if(buffer[0] == '\\')
			SETUP_motor_uvw_sequence((motor_uvw_sequence%6)+1);
		else
		{
			if(MtState == stop)
			{
				printString("Invalid command : ");printS(buffer[0]);printString("\n");
			}
		}
	}
	length = 0;
}
#endif
#endif

void check_hall_sequence()
{
	int i;
	int hall_fail = 0;
	Hal_sta_tmp = Hal_sta;

	if(Hal_sta_tmp==3)
	{
		if((Hal_sta_old != 2)&&(Hal_sta_old != 1))
		{
			hall_fail = 1;
			//printS('X');printS('a');
		}
	}
	else if(Hal_sta_tmp==1)
	{
		if((Hal_sta_old != 3)&&(Hal_sta_old != 5))
		{
			hall_fail = 1;
			//printS('X');printS('b');
		}
	}
	else if(Hal_sta_tmp==5)
	{
		if((Hal_sta_old != 1)&&(Hal_sta_old != 4))
		{
			hall_fail = 1;
			//printS('X');printS('c');
		}
	}
	else if(Hal_sta_tmp==4)
	{
		if((Hal_sta_old != 5)&&(Hal_sta_old != 6))
		{
			hall_fail = 1;
			//printS('X');printS('d');
		}
	}
	else if(Hal_sta_tmp==6)
	{
		if((Hal_sta_old != 4)&&(Hal_sta_old != 2))
		{
			hall_fail = 1;
			//printS('X');printS('e');
		}
	}
	else if(Hal_sta_tmp==2)
	{
		if((Hal_sta_old != 6)&&(Hal_sta_old != 3))
		{
			hall_fail = 1;
			//printS('X');printS('f');
		}
	}
	else
	{
		hall_fail = 1;
		printString("Impossible");
	}

	if(hall_fail)
		hall_fail_cnt++;
	else
		hall_ok_cnt++;
	
	if(hall_ok_cnt == 255)
	{
		if(hall_fail_cnt>1)
			hall_fail_cnt-=1;
	}

	if(hall_fail_cnt == 6)
	{
		MtState = stop;
		real_speed = 0;
		PINT0EN = 0;
		PWM16_disable();
		printString("\n");printString("\n");
		for(i=0;i<10;i++)
		{
			printString("HALL SENSOR ABNORMAL, STOP, RESET to restart....\n");
		}
		while(1)
			DelayXms(200);
	}
}

#if ENABLE_PHASE_COMPENSATION == 1
BYTE get_next_hall_status(BYTE hall_status_now)
{
	BYTE hall_status_next;
	if(flag_run_dir == CW)
	{
		switch(hall_status_now)
		{
			case 5:	hall_status_next = 1;	break;
			case 1:	hall_status_next = 3;	break;
			case 3:	hall_status_next = 2;	break;
			case 2:	hall_status_next = 6;	break;
			case 6:	hall_status_next = 4;	break;
			case 4:	hall_status_next = 5;	break;
			default:
					hall_status_next = 1;	break;
		}
	}
	else
	{
		switch(hall_status_now)
		{
			case 5:	hall_status_next = 4;	break;
			case 1:	hall_status_next = 5;	break;
			case 3:	hall_status_next = 1;	break;
			case 2:	hall_status_next = 3;	break;
			case 6:	hall_status_next = 2;	break;
			case 4:	hall_status_next = 6;	break;
			default:
					hall_status_next = 1;	break;
		}
	}
	return hall_status_next;
}
#endif

#ifdef TEST_START
void clear_rpm_data()
{
	int i;
	for(i = 0; i < DEBUG_LENGTH5; i++)
	{
		rpm_array[i] = 0;
		PWM_AH_array[i] = 0;
		PWM_AL_array[i] = 0;
		ADC_result8[i] = 0;
	}
	rpm_array_index = 0;
	reach_cnt = 0;
	timer0_cnt = 0;
}

void show_rpm_time_data(UINT round)
{
	ULONG time_t5 = 0;
	int i = 0;
	printString("rpm_data_array:\n\n");
	for(i=0; i< DEBUG_LENGTH5; i++)
	{
		printString("rpm_array");printd(round);printS('(');printd(i+1);printString(")=");printd(rpm_array[i]);
		printString(";pwm_array");printd(round);printS('(');printd(i+1);printString(")=");printd((PWM_AH_array[i] <<8) + PWM_AL_array[i]);
		printString(";adc8_array");printd(round);printS('(');printd(i+1);printString(")=");printd(ADC_result8[i]);
		printString(";\n");
	}
	if(flag_mode_type == CLOSE_LOOP)
	{
		printString("reach_cnt(");printd(round);printString(")=");printd(reach_cnt);printString(";\n");
	}

	//printString("Start Time:\t");printd(StartTime);printString(" sec ");
	//printx(StartTimeT5T);printx(StartTimeT5H);printx(StartTimeT5L);

	/*
	time_t5 = (ULONG)StartTimeT5T<<16 | (ULONG)StartTimeT5H<<8 | StartTimeT5L;
	printString("Start Time:\t");printd(StartTime);printS('.');
	printd(time_t5/16000);printString(" sec");

	if(ReachTime == 0)
		printString("\nReach Time:\tNo reach time");
	else
	{
		//printString("\nReach Time:\t");printd(ReachTime);printString(" sec ");
		//printx(ReachTimeT5T);printx(ReachTimeT5H);printx(ReachTimeT5L);
		time_t5 = (ULONG)ReachTimeT5T<<16 | (ULONG)ReachTimeT5H<<8 | ReachTimeT5L;
		printString("\nReach Time:\t");printd(StartTime);printS('.');
		printd(time_t5/16000);printString(" sec");
	}
	//printString("\nStop  Time:\t");printd(StopTime);printString(" sec ");
	//printx(StopTimeT5T);printx(StopTimeT5H);printx(StopTimeT5L);printString("\n\n");
	time_t5 = (ULONG)StopTimeT5T<<16 | (ULONG)StopTimeT5H<<8 | StopTimeT5L;
	printString("\nStop Time:\t");printd(StopTime);printS('.');
	printd(time_t5/16000);printString(" sec\n\n");
	*/

	if(flag_mode_type == CLOSE_LOOP)
	{
		GET_run_time();
		GET_reach_time();
	}
	printString("\n");
}

void record_open_loop_rpm_data()
{
	if(rpm_array_index < DEBUG_LENGTH5)
	{
		rpm_array[rpm_array_index] = real_speed;
		PWM_AH_array[rpm_array_index] = PWMAH;
		PWM_AL_array[rpm_array_index] = PWMAL;
		Initial_ADC(SAMPLE_CURRENT_ADC);					//Initial ADC A channel for sample current, pin18
		Get_ADC_Result(SAMPLE_CURRENT_ADC);
		Disable_ADC(SAMPLE_CURRENT_ADC);
		ADC_result8[rpm_array_index] = (ADC_A_result>>4)&0xff;
	}
	if(rpm_array_index < DEBUG_LENGTH5)
		rpm_array_index++;
}
#endif

#ifdef ENABLE_POWER_WARNING
void do_power_warning(void)
{
	#ifdef CM2209A
	P1_6 = ~P1_6;
	//P2_0 = ~P2_0;			P2_0 move to FG out
	#elif defined CM2209B
	if(flag_sensor_type != PCA_MODE)
	{
		P1_3 = ~P1_3;
		P1_2 = ~P1_2;
	}
	#ifndef STAR_V17
	P1_6 = ~P1_6;
	#endif
	#elif defined CM2209C
	P1_3 = ~P1_3;
	#elif defined CM2209D
	P1_7 = ~P1_7;
	P1_6 = ~P1_6;
	P0_5 = ~P0_5;
	P0_1 = ~P0_1;
	#endif
}
#endif
