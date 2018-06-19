#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_Function.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_Setup.h"
#include "CS8963_PWM.h"
#include "CS8963_Timer.h"
#include "CS8963_Config.h"
#include "CS8963_ADC.h"
#include "CS8963_MysonLink.h"
#include "CS8963_Initial.h"
#include "CS8963_Sensorless.h"
#include "CS8963_ISR.h"
#include "CS8963_PCA.h"

#ifdef MT_DRIVE_DEBUG
#define MT_DRIVE_LENGTH 200
UINT mt_drive_index = 0;
BYTE mt_drive_value[MT_DRIVE_LENGTH] = 0;
UINT mt_drive_time_index = 0;
UINT mt_drive_time[MT_DRIVE_LENGTH] = 0;
#endif

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function
 * Filename: CS8963_Motor_Function.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/

BYTE vr_duty = 0;
#ifdef USE_VR_RESUME
BYTE vr_duty_old = 0;
UINT target_speed_old = 0;
#else
BYTE vr_duty_old = VR_SPEED_DUTY_MIN;
UINT target_speed_old = VR_SPEED_RPM_MIN;
#endif
#ifdef USE_VR_TOLERANCE
UINT voltage_apply = 0;
#endif

BYTE flag_reach_target_speed = 0;

char MtState_changed()
{
	if(MtState == MtState_temp)
	{
		return 0;
	}
	else
	{
		MtState_temp = MtState;
		return 1;
	}
}

void Start_Motor()
{
	if(MtState == stop)
	{
		if(ERROR_number == _ERROR_NONE)		//if no error
		{
			SETUP_PWM_duty(PWM_start_duty);
			SETUP_PWM_duty_target(PWM_start_duty);
			SETUP_PWM_duty_new(PWM_start_duty);
			#ifdef MT_DRIVE_DEBUG
			reset_mt_drive_value();
			#endif
			flag_reach_target_speed = 0;
			motor_restart = 0;
			int0_cnt = 0;
			pwm16_int_cnt = 0;
			t1_cnt = 0;
			power_warning_count = ENABLE_POWER_WARNING_SLOW;
			RESET_time();
			SETUP_start_time();

			MtState = start;
			if(flag_sensor_type == SENSORLESS_MODE)
			{
				Start_Motor_Sensorless();
			}
			else if(flag_sensor_type == HALL_SENSOR_MODE)
			{
				if((Hal_sta<1)||(Hal_sta>6))
				{
					printString("\n");printString("Invalid Hall Sensor status. Please check the Hall sensor.  Hal_sta = ");printd(Hal_sta);printString("\n");
					MtState = stop;
				}
				else
				{
					printString("Start Motor, Hall: ");get_current_hall_state();
					printString(", Duty:");printd(PWM_duty);
					if(flag_mode_type == OPEN_LOOP)
					{
							printString(", OPEN LOOP, target_duty: ");printd(PWM_duty);
					}
					else if(flag_mode_type == CLOSE_LOOP)
					{
							printString(", CLOSE LOOP, target_speed: ");printd(target_speed);
							printString(", TOLERANCE: ");printd(rpm_tolerance);
					}
					if(flag_run_dir == CW)
						printString(", CW\n");
					else
						printString(", CCW\n");
					RESET_time();
					SETUP_start_time();
					Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
					PINT0EN = 1;
					if(flag_run_dir == CW)
						MT_drive(Hal_sta);
					else
						MT_drive(7 - Hal_sta);
				}
			}
			else if(flag_sensor_type == PCA_MODE)
			{

				if(PCA_use_real_hall == 1)	//use real hall
					PINT0EN = 1;
				else if(PCA_use_real_hall == 0)	//use sensorless hall
				{
					printString("PCA sensorless start\n");
					PCA_duty = PCA_START_DUTY;
					PCA8_Modify(PCA_duty);
					PINT0EN = 0;
					Disable_Comparator();
					Initial_Comparator_Sensorless();
					if(flag_run_dir == CW)
						P1_2 = 1;	//CW
					else
						P1_2 = 0;	//CCW
					P1_3 = 0;	//start UVW
					Hal_sta_my = 5;
					P2_7=1;P3_2=0;P3_3=1;
					CMPCFGAB = B01101111;CMPCFGCD = B11111111;
				}
			}
		}
		else
		{
			printString("[CS8963]: Error Status = ");printd(ERROR_number);printString(", Abort...\n");
			print_error_message(ERROR_number);
		}
	}
}

void Stop_Motor()
{
	MtState = stop;
	real_speed = 0;
	real_speed_tmp = 0;
	if(flag_sensor_type == PCA_MODE)
	{
		P1_3 = 1;	//stop UVW
		PCA_duty = PCA_START_DUTY;
		if(PCA_use_real_hall == 1)
			PINT0EN = 0;
		else	//use sensorless hall
			Disable_Comparator();
	}
	else
		PWM16_disable();
	SETUP_stop_time();
	if(flag_sensor_type == SENSORLESS_MODE)
	{
		Disable_Comparator();
		motor_start = 1;
		SETUP_PWM_duty(PWM_start_duty);
		printString("\n[CS8963]: SENSORLESS SP\n\n");printString(PROMPT);
	}
	else if(flag_sensor_type == HALL_SENSOR_MODE)
	{
		PINT0EN = 0;
		PWM_duty = 0;
		printString("\nStop Hall: ");get_current_hall_state();printString("\n\n");printString(PROMPT);
	}
	PWM16_disable();
}

void MT_drive(unsigned char Hal_sta_tmp)	//UNIPOLAR PWM
{
	if(flag_sensor_type == PCA_MODE)
	{		//use real/sensorless hall, all use this in PCA mode.
		if(flag_run_dir == CW)
		{
			switch(Hal_sta_tmp)
			{
				case 3:
					P2_7=0;P3_2=1;P3_3=1;
					CHECK_FALLING_EDGE;
					break;
				case 4:
					P2_7=1;P3_2=0;P3_3=0;
					CHECK_RISING_EDGE;
					break;
				case 5:
					P2_7=1;P3_2=0;P3_3=1;
					CHECK_FALLING_EDGE;
					break;
				case 2:
					P2_7=0;P3_2=1;P3_3=0;
					CHECK_RISING_EDGE;
					break;
				case 1:
					P2_7=0;P3_2=0;P3_3=1;
					CHECK_RISING_EDGE;
					break;
				case 6:
					P2_7=1;P3_2=1;P3_3=0;
					CHECK_FALLING_EDGE;
					break;
				default:
					printString("FAIL:");printS(Hal_sta_tmp+0x30);printString("\n");
					break;
			}
		}
		else	//CCW
		{
			switch(Hal_sta_tmp)
			{
				case 4:
					P2_7=0;P3_2=1;P3_3=1;
					CHECK_FALLING_EDGE;
					break;
				case 3:
					P2_7=1;P3_2=0;P3_3=0;
					CHECK_RISING_EDGE;
					break;
				case 2:
					P2_7=1;P3_2=0;P3_3=1;
					CHECK_FALLING_EDGE;
					break;
				case 5:
					P2_7=0;P3_2=1;P3_3=0;
					CHECK_RISING_EDGE;
					break;
				case 6:
					P2_7=0;P3_2=0;P3_3=1;
					CHECK_RISING_EDGE;
					break;
				case 1:
					P2_7=1;P3_2=1;P3_3=0;
					CHECK_FALLING_EDGE;
					break;
				default:
					printString("FAIL:");printS(Hal_sta_tmp+0x30);printString("\n");
					break;
			}
		}
		return;
	}

		switch(Hal_sta_tmp)
		{
#ifdef USE_NNMOS
#ifdef UVW_TYPE_A
			#ifdef STAR
			case 2:	MFCFGP1_0 = Hopen;	 P1_1=1;	//A+
					MFCFGP1_4 = Close;	 P1_5=0;	//B-
					MFCFGP3_1 = Close;	 P3_0=1;	//C0
					break;
			case 6:	MFCFGP1_0 = Close;	 P1_1=1;	//A0
					MFCFGP1_4 = Close;	 P1_5=0;	//B-
					MFCFGP3_1 = Hopen;	 P3_0=1;	//C+
					break;
			case 4:	MFCFGP1_0 = Close;	 P1_1=0;	//A-
					MFCFGP1_4 = Close;	 P1_5=1;	//B0
					MFCFGP3_1 = Hopen;	 P3_0=1;	//C+
					break;
			case 5:	MFCFGP1_0 = Close;	 P1_1=0;	//A-
					MFCFGP1_4 = Hopen;	 P1_5=1;	//B+
					MFCFGP3_1 = Close;	 P3_0=1;	//C0
					break;
			case 1:	MFCFGP1_0 = Close;	 P1_1=1;	//A0
					MFCFGP1_4 = Hopen;	 P1_5=1;	//B+
					MFCFGP3_1 = Close;	 P3_0=0;	//C-
					break;
			case 3:	MFCFGP1_0 = Hopen;	 P1_1=1;	//A+
					MFCFGP1_4 = Close;	 P1_5=1;	//B0
					MFCFGP3_1 = Close;	 P3_0=0;	//C-
					break;
			#elif defined STAR_V17
			case 2:	MFCFGP1_0 = Hopen;	 P1_1=1;	//A+
					MFCFGP1_6 = Close;	 P1_7=0;	//B-
					MFCFGP3_1 = Close;	 P3_0=1;	//C0
					break;
			case 6:	MFCFGP1_0 = Close;	 P1_1=1;	//A0
					MFCFGP1_6 = Close;	 P1_7=0;	//B-
					MFCFGP3_1 = Hopen;	 P3_0=1;	//C+
					break;
			case 4:	MFCFGP1_0 = Close;	 P1_1=0;	//A-
					MFCFGP1_6 = Close;	 P1_7=1;	//B0
					MFCFGP3_1 = Hopen;	 P3_0=1;	//C+
					break;
			case 5:	MFCFGP1_0 = Close;	 P1_1=0;	//A-
					MFCFGP1_6 = Hopen;	 P1_7=1;	//B+
					MFCFGP3_1 = Close;	 P3_0=1;	//C0
					break;
			case 1:	MFCFGP1_0 = Close;	 P1_1=1;	//A0
					MFCFGP1_6 = Hopen;	 P1_7=1;	//B+
					MFCFGP3_1 = Close;	 P3_0=0;	//C-
					break;
			case 3:	MFCFGP1_0 = Hopen;	 P1_1=1;	//A+
					MFCFGP1_6 = Close;	 P1_7=1;	//B0
					MFCFGP3_1 = Close;	 P3_0=0;	//C-
					break;
			#else	//NNMOS normal use
			case 2:
					MFCFGP3_1 = Close;	 P3_0=0;	//C0
					MFCFGP1_4 = Close;	 P1_5=1;	//B-
					MFCFGP1_0 = Hopen;	 P1_1=0;	//A+
					break;
			case 6:
					MFCFGP1_0 = Close;	 P1_1=0;	//A0
					MFCFGP1_4 = Close;	 P1_5=1;	//B-
					MFCFGP3_1 = Hopen;	 P3_0=0;	//C+
					break;
			case 4:
					MFCFGP1_4 = Close;	 P1_5=0;	//B0
					MFCFGP1_0 = Close;	 P1_1=1;	//A-
					MFCFGP3_1 = Hopen;	 P3_0=0;	//C+
					break;
			case 5:
					MFCFGP3_1 = Close;	 P3_0=0;	//C0
					MFCFGP1_0 = Close;	 P1_1=1;	//A-
					MFCFGP1_4 = Hopen;	 P1_5=0;	//B+
					break;
			case 1:
					MFCFGP1_0 = Close;	 P1_1=0;	//A0
					MFCFGP3_1 = Close;	 P3_0=1;	//C-
					MFCFGP1_4 = Hopen;	 P1_5=0;	//B+
					break;
			case 3:
					MFCFGP1_4 = Close;	 P1_5=0;	//B0
					MFCFGP3_1 = Close;	 P3_0=1;	//C-
					MFCFGP1_0 = Hopen;	 P1_1=0;	//A+
					break;
			#endif
#else	//UVW_TYPE_B
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
#endif
#elif defined USE_PNMOS
			case 6:	MFCFGP1_1 = Close;	P1_0 = 1;	//U0
					MFCFGP3_0 = Close;	P3_1 = 0;	//W-a
					MFCFGP1_5 = Hopen;	P1_4 = 1;	//V+a
					break;
			case 2:	MFCFGP1_1 = Close;	P1_0 = 0;	//U-
					MFCFGP3_0 = Close;	P3_1 = 1;	//W0a
					MFCFGP1_5 = Hopen;	P1_4 = 1;	//V+a
					break;
			case 3:	MFCFGP1_1 = Close;	P1_0 = 0;	//U-
					MFCFGP3_0 = Hopen;	P3_1 = 1;	//W+a
					MFCFGP1_5 = Close;	P1_4 = 1;	//V0a
					break;
			case 1:	MFCFGP1_1 = Close;	P1_0 = 1;	//U0
					MFCFGP3_0 = Hopen;	P3_1 = 1;	//W+a
					MFCFGP1_5 = Close;	P1_4 = 0;	//V-a
					break;
			case 5:	MFCFGP1_1 = Hopen;	P1_0 = 1;	//U+
					MFCFGP3_0 = Close;	P3_1 = 1;	//W0
					MFCFGP1_5 = Close;	P1_4 = 0;	//V-
					break;
			case 4:	MFCFGP1_1 = Hopen;	P1_0 = 1;	//U+
					MFCFGP3_0 = Close;	P3_1 = 0;	//W-
					MFCFGP1_5 = Close;	P1_4 = 1;	//V0
					break;
#else
			printString("MOS Type Unknown\n");
#endif
			default:
					printString("FAIL:");printS(Hal_sta_tmp+0x30);printString("\n");
					break;
		}
	#ifdef MT_DRIVE_DEBUG
	if(mt_drive_index < (MT_DRIVE_LENGTH - 10))
	{
		mt_drive_value[mt_drive_index] = Hal_sta_tmp;
		mt_drive_index++;
	}
	#endif

	if(flag_sensor_type == SENSORLESS_MODE)
	{
		check_comparator_edge();
		mt_drive_cnt++;

		//for calculate sensorless abnormal case, 33.3us
		mt_drive_time_new = TH0<<8 | TL0;
		if(mt_drive_time_new < 100)
			too_fast++;
		else if(mt_drive_time_new > 20000)
			too_slow++;
		mt_drive_time_diff_new = diff(mt_drive_time_new, mt_drive_time_old);
		if((mt_drive_time_diff_new / mt_drive_time_diff_old) > 10)	//suddenly slow down
			abnormal++;
		#ifdef MT_DRIVE_DEBUG
		if(mt_drive_time_index < (MT_DRIVE_LENGTH - 10))
		{
			mt_drive_time[mt_drive_time_index] = mt_drive_time_diff_new;
			mt_drive_time_index++;
		}
		#endif
		mt_drive_time_old = mt_drive_time_new;
		mt_drive_time_diff_old = mt_drive_time_diff_new;
	
		if(abnormal == 20)
		{
			abnormal = 0;
			Stop_Motor();
			printString("Abnormal2, sensorless restart\n");
			#ifdef MT_DRIVE_DEBUG
			reset_mt_drive_value();
			#endif
			motor_start = 1;
			RESET_time();
			SETUP_start_time();
			Start_Motor_Sensorless();
			return;
		}
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

void do_over_current_protection_adc(void)
{
	#ifdef USE_MYSONLINK
	int i;
	#endif

	/*
	Initial_ADC(SAMPLE_CURRENT_ADC);						//Initial ADC A channel for sample current, pin18, P0_0
	Get_ADC_Result(SAMPLE_CURRENT_ADC);
	Disable_ADC(SAMPLE_CURRENT_ADC);
	*/
	//Initial ADC A for P0_0, pin18
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	IOCFGP0_0 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_0 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_A_EN;	//select A channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC A result for P0_0
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_A_result = 0;
	if(ADCCHSL&ADC_A_IF)		//select A channel
		ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;

	//Disable ADC A for P0_0
	ADCCHSL &= ~ADC_A_EN;		//select A channel
	IOCFGP0_0 = B00000000;		//Enable Anolog MUX
	MFCFGP0_0 = PinC_In;		//ADC A3 for instantaneous current
	
	if(ADC_A_result > Over_Current_ADC)
	{
		over_current_cnt++;
		printString("\nOCA: 0x");printx(ADC_A_result);printS('=');printd(ADC_A_result);printS(' ');printd(over_current_cnt);
		if(over_current_cnt == OVER_CURRENT_TIME)
		{
			Stop_Motor();
			printString("\nOver Current Protection STOP\n\n");
			over_current_cnt = 0;
			power_warning_count = ENABLE_POWER_WARNING_FAST;
			ERROR_number = _ERROR_OCA;
			#ifdef USE_MYSONLINK
			for(i=0;i<10;i++)
			{
				Send_Motor_Error_Cmd(ERROR_number);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
			}
			#endif
		}
	}
	else
		over_current_cnt = 0;
}

void MT_Brake(void)
{
	if(flag_enable_brake == 1)
	{
		//close upper arms
		#ifdef USE_NNMOS	//NNMOS, STAR
		P1_0=0;									//close AP
		#ifdef STAR_V17
		P1_6=0;									//close BP
		#else
		P1_4=0;									//close BP
		#endif
		P3_1=0;									//close CP
		#else	//PNMPS
		P1_0=1;									//close AP
		P1_4=1;									//close BP
		P3_1=1;									//close CP
		#endif
	
		//open lower arms
		#ifdef STAR
		MFCFGP1_0 = Close;	 P1_1 = 0;			//A-
		MFCFGP1_4 = Close;	 P1_5 = 0;			//B-
		MFCFGP3_1 = Close;	 P3_0 = 0;			//C-
		#elif defined STAR_V17
		MFCFGP1_0 = Close;	 P1_1 = 0;			//A-
		MFCFGP1_6 = Close;	 P1_7 = 0;			//B-
		MFCFGP3_1 = Close;	 P3_0 = 0;			//C-
		#else	//NNMOS, PNMOS
		MFCFGP1_0 = Close;	 P1_1 = 1;			//A-
		MFCFGP1_4 = Close;	 P1_5 = 1;			//B-
		MFCFGP3_1 = Close;	 P3_0 = 1;			//C-
		#endif
		
		//delay some time
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
		
		//close lower arms
		#ifdef STAR
		P1_1 = 1;								//close AN
		P1_5 = 1;								//close BN
		P3_0 = 1;								//close CN
		MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
		MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	//B0
		MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
		#elif defined STAR_V17
		P1_1 = 1;								//close AN
		P1_7 = 1;								//close BN
		P3_0 = 1;								//close CN
		MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
		MFCFGP1_6 = Close;  MFCFGP1_7 = Close;	//B0
		MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
		#else	//NNMOS, PNMOS
		P1_1=0;									//close AN
		P1_5=0;									//close BN
		P3_0=0;									//close CN
		MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
		MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	//B0
		MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
		#endif
	}
	else
		printString("NO BRAKE\n");
}

void MT_Lock(bit on_off)
{
	if(on_off == 1)
	{
		//close upper arms
		#ifdef USE_NNMOS	//NNMOS, STAR
		P1_0=0;									//close AP
		#ifdef STAR_V17
		P1_6=0;									//close BP
		#else
		P1_4=0;									//close BP
		#endif
		P3_1=0;									//close CP
		#else	//PNMPS
		P1_0=1;									//close AP
		P1_4=1;									//close BP
		P3_1=1;									//close CP
		#endif
	
		//open lower arms
		#ifdef STAR
		MFCFGP1_0 = Close;	 P1_1 = 0;			//A-
		MFCFGP1_4 = Close;	 P1_5 = 0;			//B-
		MFCFGP3_1 = Close;	 P3_0 = 0;			//C-
		#elif defined STAR_V17
		MFCFGP1_0 = Close;	 P1_1 = 0;			//A-
		MFCFGP1_6 = Close;	 P1_7 = 0;			//B-
		MFCFGP3_1 = Close;	 P3_0 = 0;			//C-
		#else	//NNMOS, PNMOS
		MFCFGP1_0 = Close;	 P1_1 = 1;			//A-
		MFCFGP1_4 = Close;	 P1_5 = 1;			//B-
		MFCFGP3_1 = Close;	 P3_0 = 1;			//C-
		#endif
	}
	else	//lock off
	{
		//close lower arms
		#ifdef STAR
		P1_1 = 1;								//close AN
		P1_5 = 1;								//close BN
		P3_0 = 1;								//close CN
		MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
		MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	//B0
		MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
		#elif defined STAR_V17
		P1_1 = 1;								//close AN
		P1_7 = 1;								//close BN
		P3_0 = 1;								//close CN
		MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
		MFCFGP1_6 = Close;  MFCFGP1_7 = Close;	//B0
		MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
		#else	//NNMOS, PNMOS
		P1_1=0;									//close AN
		P1_5=0;									//close BN
		P3_0=0;									//close CN
		MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
		MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	//B0
		MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
		#endif
	}
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
	#ifdef STAR_V17
	MFCFGP1_6 = Hopen;  MFCFGP1_7 = Close;	//B+
	#else
	MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
	#endif
}

void MT_drive_B_off()
{
	#ifdef STAR_V17
	MFCFGP1_6 = Close;  MFCFGP1_7 = Close;		//B0
	#else
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;		//B0
	#endif
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
	#ifdef STAR_V17
	MFCFGP1_6 = Close;  MFCFGP1_7 = Close;		//B0
	#else
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;		//B0
	#endif
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;		//C0
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

BYTE get_current_hall_status()
{
	BYTE hall_status;
	hall_status=((P0&0x1C)>>2);
	//printS(Hal_sta+0x30);
	PIOEDGR0 &= ~0x1C;
	PIOEDGF0 &= ~0x1C;
	PIOEDGR0 = 0x1C;
	PIOEDGF0 = 0x1C;
	return hall_status;
}

void do_check_VR_open_loop()
{
	UINT voltage = 0;
	
	/*
	Initial_ADC(PIN_VRin);						//Initial ADC A channel for VR, pin13
	Get_ADC_Result(PIN_VRin);
	Disable_ADC(PIN_VRin);
	*/
	//Initial ADC A for P0_5
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	IOCFGP0_5 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_A_EN;	//select A channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC A result for P0_5
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_A_result = 0;
	if(ADCCHSL&ADC_A_IF)		//select A channel
		ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;

	//Disable ADC A for P0_5
	ADCCHSL &= ~ADC_A_EN;		//select A channel
	IOCFGP0_5 = B00000000;		//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	
	voltage = (UINT)(((unsigned long)ADC_A_result*ADC_FULL*1000)/4096);	//mV
	//printString("VR ");printd(voltage);//printS(' ');
	//printString("\n");
	
	if(voltage >= VR_MAX)
		vr_duty = VR_SPEED_DUTY_MAX;
	else if(voltage <= VR_MIN)
		vr_duty = 0;
	else
	{
		#ifdef USE_VR_TOLERANCE
		//printString("\n");printS('A');printd(voltage);printS(' ');printS('B');printd(voltage_apply);printS(' ');
		if((voltage > voltage_apply) && (voltage - voltage_apply) > VR_TOLERANCE)
		{
			//printS('d');printd(voltage - voltage_apply);printS(' ');printS('+');printS(' ');
			voltage_apply = voltage;
			vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
		}
		else if((voltage_apply > voltage) && (voltage_apply - voltage) > VR_TOLERANCE)
		{
			//printS('d');printd(voltage_apply - voltage);printS(' ');printS('-');printS(' ');
			voltage_apply = voltage;
			vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
		}
		/*	debug message
		else
		{
			if(voltage > voltage_apply)
			{
				printS('D');printd(voltage - voltage_apply);
			}
			else
			{
				printS('d');printd(voltage_apply - voltage);
			}
			printS(' ');printS('|');printS(' ');
		}
		*/
		#else
		vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
		#endif
	}
	
	//printS('_');printd(vr_duty);printS('_');
	
	if(vr_duty != vr_duty_old)
	{
		if(vr_duty == 0)
		{
			Stop_Motor();
			SETUP_PWM_duty_target(0);	//slow
			SETUP_PWM_duty_new(0);		//fast
			printString("VR Stop\n");
		}
		else if(vr_duty_old == 0)
		{
			if(ERROR_number == _ERROR_NONE)		//no error
			{
				SETUP_PWM_duty(PWM_START_DUTY);
				PWM_duty_old = PWM_START_DUTY;
				vr_duty_old = PWM_START_DUTY;
				SETUP_PWM_duty_target(vr_duty);	//slow
				SETUP_PWM_duty_new(vr_duty);	//fast
				printString("VR Start\tstart_duty = ");printd(PWM_duty);
				printString(", target_duty = ");printd(PWM_duty_target);printString("\n");
				precharge_lower_arms();
				Start_Motor();
			}
			else
			{
				printString("[CS8963]: Error Status = ");printd(ERROR_number);printString(", Abort...\n");
				print_error_message(ERROR_number);
			}
		}
		else
		{
			//printS('d');
			//printString("duty= ");printd(vr_duty);printString("\n");
			//PWM_duty_target = vr_duty;
			PWM16_Modify(PWM_period, vr_duty);
			//printd(vr_duty);printS('d');printS(' ');
			//printS('_');printd(vr_duty);printS('_');
		}
		vr_duty_old = vr_duty;
	}
	//printS(' ');
	
	/*
	//debug message
	printString("ADC:0x");printx(ADC_D_result);printS('=');printd(ADC_D_result);printString("  ");
	printString("ADC_D_instance  = 0x");printx(ADC_D_result);printString(" = ");printd(ADC_D_result);printString(" ");
	printString("v_out = ");printv(voltage);printString(" V   ");printString("   duty = ");printd(vr_duty);printString("\n");
	
	printString("debug\n");printString("\n");printString("\n");printString("\n");printString("\n");
	for(voltage=0; voltage <= 5300; voltage += 33)
	{
		if(voltage >= VR_MAX)
			vr_duty = VR_SPEED_DUTY_MAX;
		else if(voltage <= VR_MIN)
			vr_duty = 0;
		else
			vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
		
		printString("v_out = ");printv(voltage);printString(" V   ");printString("   duty = ");printd(vr_duty);printString("\n");
	}
	while(1)
	{
		DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
	}
	*/
}

void do_check_VR_close_loop()
{
	UINT voltage = 0;
	
	/*
	Initial_ADC(PIN_VRin);						//Initial ADC A channel for VR, pin13
	Get_ADC_Result(PIN_VRin);
	Disable_ADC(PIN_VRin);
	*/
	//Initial ADC A for P0_5
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	IOCFGP0_5 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_A_EN;	//select A channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC A result for P0_5
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_A_result = 0;
	if(ADCCHSL&ADC_A_IF)		//select A channel
		ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;

	//Disable ADC A for P0_5
	ADCCHSL &= ~ADC_A_EN;		//select A channel
	IOCFGP0_5 = B00000000;		//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	
	voltage = (UINT)(((unsigned long)ADC_A_result*ADC_FULL*1000)/4096);	//mV
	//printString("VR ");printd(voltage);printS(' ');

	if(voltage >= VR_MAX)
		SETUP_target_speed(vr_max_speed);
	else if(voltage <= VR_MIN)
		SETUP_target_speed(0);
	else
	{
		#ifdef USE_VR_TOLERANCE
		//printString("\n");printS('A');printd(voltage);printS(' ');printS('B');printd(voltage_apply);printS(' ');
		if((voltage > voltage_apply) && (voltage - voltage_apply) > VR_TOLERANCE)
		{
			//printS('d');printd(voltage - voltage_apply);printS(' ');printS('+');printS(' ');
			voltage_apply = voltage;
			//SETUP_target_speed((UINT)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(vr_max_speed-vr_min_speed))) + vr_min_speed);
			SETUP_target_speed((UINT)((ULONG)(voltage-VR_MIN)*(vr_max_speed-vr_min_speed)/(VR_MAX-VR_MIN))+vr_min_speed);
		}
		else if((voltage_apply > voltage) && (voltage_apply - voltage) > VR_TOLERANCE)
		{
			//printS('d');printd(voltage_apply - voltage);printS(' ');printS('-');printS(' ');
			voltage_apply = voltage;
			//SETUP_target_speed((UINT)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(vr_max_speed-vr_min_speed))) + vr_min_speed);
			SETUP_target_speed((UINT)((ULONG)(voltage-VR_MIN)*(vr_max_speed-vr_min_speed)/(VR_MAX-VR_MIN))+vr_min_speed);
		}
		/*	debug message
		else
		{
			if(voltage > voltage_apply)
			{
				printS('D');printd(voltage - voltage_apply);
			}
			else
			{
				printS('d');printd(voltage_apply - voltage);
			}
			printS(' ');printS('|');printS(' ');
		}
		*/
		#else
		//SETUP_target_speed((UINT)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(vr_max_speed-vr_min_speed))) + vr_min_speed);
		SETUP_target_speed((UINT)((ULONG)(voltage-VR_MIN)*(vr_max_speed-vr_min_speed)/(VR_MAX-VR_MIN))+vr_min_speed);
		#endif
	}
	
	//printS('_');printd(target_speed);printS('_');
	
	if(target_speed != target_speed_old)
	{
		if(target_speed == 0)
		{
			Stop_Motor();
			printString("VR Stop\n");
		}
		else if(target_speed_old == 0)
		{
			if(ERROR_number == _ERROR_NONE)		//no error
			{
				if(voltage > 2000)
				{
					printString("VR too large, check it again\t");
					printS('A');printd(ADC_A_result);printS(';');
					printS('H');printd(ADCAH);printS('L');printd(ADCAL);
					printS('v');printd(voltage);printS(';');
					printS('T');printd(target_speed);printString("\tread adc again\n");
	
					//Initial ADC A for P0_5
					//unsigned char temp = 30;
					//unsigned char ADCCHSL_tmp;
					IOCFGP0_5 = _ANEN_;			//Enable Anolog MUX
					MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
					ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
					temp = 30;
					while(temp--);				//wait until ADC is stable
					ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
					ADCCHSL_tmp = ADCCHSL;
					ADCCHSL_tmp |= ADC_A_EN;	//select A channel
					ADCCHSL =ADCCHSL_tmp;
					DelayXms(5);
	
					//Get ADC A result for P0_5
					ADCCFG = b10110001;			//Start convertion
					while(ADCCFG&0x10);			//Waiting for conversion finish
					ADC_A_result = 0;
					if(ADCCHSL&ADC_A_IF)		//select A channel
						ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;
	
					//Disable ADC A for P0_5
					ADCCHSL &= ~ADC_A_EN;		//select A channel
					IOCFGP0_5 = B00000000;		//Enable Anolog MUX
					MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
					
					voltage = (UINT)(((unsigned long)ADC_A_result*ADC_FULL*1000)/4096);	//mV
					printString("VR ");printd(voltage);printString("\n");
					if(voltage > 2000)
					{
						printString("VR Start\t");
						printS('v');printd(voltage);printS(';');
						printS('T');printd(target_speed);printString("\n");
						precharge_lower_arms();
						Start_Motor();
					}
					else
					{
						printString("arort.....\n");
						return;
					}
				}
				else
				{
					printString("VR Start\t");
					printS('v');printd(voltage);printS(';');
					printS('T');printd(target_speed);printString("\n");
	
					/*	debug
					printString("voltage=");printd(voltage);
					printString(";VR_MAX=");printd(VR_MAX);
					printString(";VR_MIN=");printd(VR_MIN);
					printString(";vr_max_speed=");printd(vr_max_speed);
					printString(";vr_min_speed=");printd(vr_min_speed);
					printString(";target_speed=");printd(target_speed);printString("\n");
					*/
	
					precharge_lower_arms();
					Start_Motor();
				}
			}
			else
			{
				printString("[CS8963]: Error Status = ");printd(ERROR_number);printString(", Abort...\n");
				print_error_message(ERROR_number);
			}
		}
		else
		{
			//printS('t');printd(target_speed);printS(' ');
		}
		target_speed_old = target_speed;
	}
	//printS(' ');
	
	/*
	//debug message
	printString("ADC:0x");printx(ADC_D_result);printS('=');printd(ADC_D_result);printString("  ");
	printString("ADC_D_instance  = 0x");printx(ADC_D_result);printString(" = ");printd(ADC_D_result);printString(" ");
	printString("v_out = ");printv(voltage);printString(" V   ");printString("   duty = ");printd(vr_duty);printString("\n");
	
	printString("debug\n");printString("\n");printString("\n");printString("\n");printString("\n");
	for(voltage=0; voltage <= 5300; voltage += 33)
	{
		if(voltage >= VR_MAX)
			vr_duty = VR_SPEED_DUTY_MAX;
		else if(voltage <= VR_MIN)
			vr_duty = 0;
		else
			vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
		
		printString("v_out = ");printv(voltage);printString(" V   ");printString("   duty = ");printd(vr_duty);printString("\n");
	}
	while(1)
	{
		DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
	}
	*/
}


void do_check_VR_open_loop_test()
{
	UINT voltage = 0;
	
	/*
	Initial_ADC(PIN_VRin);						//Initial ADC A channel for VR, pin13
	Get_ADC_Result(PIN_VRin);
	Disable_ADC(PIN_VRin);
	*/
	//Initial ADC A for P0_5
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	IOCFGP0_5 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_A_EN;	//select A channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC A result for P0_5
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_A_result = 0;
	if(ADCCHSL&ADC_A_IF)		//select A channel
		ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;

	//Disable ADC A for P0_5
	ADCCHSL &= ~ADC_A_EN;		//select A channel
	IOCFGP0_5 = B00000000;		//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	
	voltage = (UINT)(((unsigned long)ADC_A_result*ADC_FULL*1000)/4096);	//mV
	printString("Open VR = ");printd(voltage);

	//printString("\n");
	
	if(voltage >= VR_MAX)
		vr_duty = VR_SPEED_DUTY_MAX;
	else if(voltage <= VR_MIN)
		vr_duty = 0;
	else
	{
		vr_duty = (unsigned char)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
	}
	printString(" mV, duty = ");;printd(vr_duty);printString("\t\t");
}

void do_check_VR_close_loop_test()
{
	UINT voltage;
	
	/*
	Initial_ADC(PIN_VRin);						//Initial ADC A channel for VR, pin13
	Get_ADC_Result(PIN_VRin);
	Disable_ADC(PIN_VRin);
	*/
	//Initial ADC A for P0_5
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	IOCFGP0_5 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_A_EN;	//select A channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC A result for P0_5
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_A_result = 0;
	if(ADCCHSL&ADC_A_IF)		//select A channel
		ADC_A_result = ((UINT)ADCAH<<8)+ (UINT)ADCAL;

	//Disable ADC A for P0_5
	ADCCHSL &= ~ADC_A_EN;		//select A channel
	IOCFGP0_5 = B00000000;		//Enable Anolog MUX
	MFCFGP0_5 = PinC_In;		//ADC A3 for instantaneous current
	
	voltage = (UINT)(((unsigned long)ADC_A_result*ADC_FULL*1000)/4096);	//mV
	printString("Close VR = ");printd(voltage);

	if(voltage >= VR_MAX)
		SETUP_target_speed(vr_max_speed);
	else if(voltage <= VR_MIN)
		SETUP_target_speed(0);
	else
	{
		SETUP_target_speed((UINT)((voltage-VR_MIN)/((VR_MAX-VR_MIN)/(vr_max_speed-vr_min_speed))) + vr_min_speed);
	}
	printString(" mV, target_speed = ");;printd(target_speed);printString("\n");
}

void do_check_lock_rotor_protection()
{
	/*
	int i;
	if(MtState == start)
	{
		if((!motor_start)&&(real_speed<10))
		{
			lock_rotor_cnt++;
			//if(lock_rotor_cnt >= 5)
			{
				PINT0EN = 0;
				PWM16_disable();
				MtState = stop;
				motor_start = 1;
				timer0_cnt = 0;
				SETUP_target_speed(0);
				real_speed = 0;
				hall_fail_cnt = 0;
				printString("\n");printString("\n");
				printString("B real_speed = ");printd(real_speed);printString("\n");
				for(i=0;i<5;i++)
				{
					printString("LOCK ROTOR PROTECTION, STOP, RESET to restart....\n");
				}
				//ERROR_number = _ERROR_LOCK_ROTOR;
				for(i=0;i<10;i++)
				{
					//Send_Error_Speed_Cmd(ERROR_number);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
				if(flag_enable_vr_speed==1)
				{
					while(1)
						DelayXms(200);
				}
			}
		}
		else
			lock_rotor_cnt = 0;
	}
	*/
}

#ifdef MT_DRIVE_DEBUG
void pirnt_mt_drive_value(void)
{
	int i;
	int pair = 0;
	printString("mt_drive_value_array:\n");
	for(i = 0; i< MT_DRIVE_LENGTH; i++)
	{
		printd(mt_drive_value[i]);
		if(mt_drive_value[i] == 2)
		{
			printS(' ');
			pair++;
		}
		if(pair == 10)
		{
			printString("\n");
			pair = 0;
		}
	}
	printString("\n\n");
	printString("mt_drive_time_array:\n");
	for(i = 0; i< MT_DRIVE_LENGTH; i++)
	{
		printString("Time(");printd(i+1);printString(")=");printd(mt_drive_time[i]);
		if((i % 6) == 5)
			printString(";\n");
		else
			printS(';');
	}
	printString("\n\n");

	printString("too_fast = ");printd(too_fast);printString(";\n");
	printString("too_slow = ");printd(too_slow);printString(";\n");
	printString("abnormal = ");printd(abnormal);printString(";\n");
}

void reset_mt_drive_value(void)
{
	int i;
	mt_drive_index = 0;
	for(i = 0; i< MT_DRIVE_LENGTH; i++)
		mt_drive_value[i] = 0;

	mt_drive_time_index = 0;
	for(i = 0; i< MT_DRIVE_LENGTH; i++)
		mt_drive_time[i] = 0;
	mt_drive_time_new = 0;
	mt_drive_time_old = 0;
	mt_drive_time_diff_new = 0;
	mt_drive_time_diff_old = 0;

	too_fast = 0;
	too_slow = 0;
	abnormal = 0;
}
#endif

#ifdef CHECK_VDC_VOLTAGE
UINT check_vdc_voltage()
{
	#if defined(CM2209B) || defined(CM2209C)
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	UINT dc_bus_voltage = 0;
	ADC_B_result = 0;

	/*
	Initial_ADC(SAMPLE_DCBUS_ADC);						//Initial ADC B channel for DC_BUS, pin17, CM2209B
	Get_ADC_Result(SAMPLE_DCBUS_ADC);
	Disable_ADC(SAMPLE_DCBUS_ADC);
	*/
	//Initial ADC B for P0_1, pin17
	IOCFGP0_1 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_B_EN;	//select B channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC B result for P0_1
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_B_result = 0;
	if(ADCCHSL&ADC_B_IF)		//select A channel
		ADC_B_result = ((UINT)ADCBH<<8)+ (UINT)ADCBL;

	//Disable ADC B for P0_1
	ADCCHSL &= ~ADC_B_EN;		//select B channel
	IOCFGP0_1 = B00000000;		//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current

	dc_bus_voltage = (UINT)(((unsigned long)ADC_B_result*ADC_FULL*1000)/4096);	//mV
	//printString("DC_BUS = ");printd(dc_bus_voltage);printString(" mV\t");

	#ifdef CM2209B
	//printString("VM = ");printd(dc_bus_voltage/10*110/1000);printString(" V\n");
	//printString("VM = ");printd(dc_bus_voltage*11);printString(" mV\n");
	return (dc_bus_voltage*11/1000);
	#elif defined CM2209C
	//printString("VM = ");printd(dc_bus_voltage/20*111/50);printString(" V\n");
	return (dc_bus_voltage/20*111/50);
	#else
	return 0;
	#endif
	#else
	return 0;
	#endif

}

void do_check_vdc_voltage()
{
	int check_vdc_cnt = 0;
	UINT vdc_voltage = 0;

	printString("\nCHECK_VDC_VOLTAGE:\t");
	while(check_vdc_cnt < 3)
	{
		vdc_voltage = check_vdc_voltage();
		if((ac_voltage == 220) && (vdc_voltage > 248))	//310 * 0.8
		{
			printS('H');
			check_vdc_cnt++;
		}
		else if((ac_voltage == 110) && (vdc_voltage > 124))	//155 * 0.8
		{
			printS('L');
			check_vdc_cnt++;
		}
		else
			printS('U');
		DelayXms(100);
	}
	printString("\n");
	//printString("VDC voltage : ");printd(vdc_voltage);printString(" V\n");
}
#endif

void get_vdc_voltage()
{
	#if defined(CM2209B) || defined(CM2209C)
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	UINT dc_bus_voltage = 0;
	ADC_B_result = 0;

	/*
	Initial_ADC(SAMPLE_DCBUS_ADC);						//Initial ADC B channel for DC_BUS, pin17, CM2209B
	Get_ADC_Result(SAMPLE_DCBUS_ADC);
	Disable_ADC(SAMPLE_DCBUS_ADC);
	*/
	//Initial ADC B for P0_1, pin17
	IOCFGP0_1 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_B_EN;	//select B channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC B result for P0_1
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_B_result = 0;
	if(ADCCHSL&ADC_B_IF)		//select A channel
		ADC_B_result = ((UINT)ADCBH<<8)+ (UINT)ADCBL;

	//Disable ADC B for P0_1
	ADCCHSL &= ~ADC_B_EN;		//select B channel
	IOCFGP0_1 = B00000000;		//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current

	printString("DC_BUS_ADC = ");printd(ADC_B_result);printString("\t");

	dc_bus_voltage = (UINT)(((unsigned long)ADC_B_result*ADC_FULL*1000)/4096);	//mV

	printString("DC_BUS = ");printd(dc_bus_voltage);printString(" mV\t\t");

	#ifdef CM2209B
	//printString("VM = ");printd(dc_bus_voltage/10*110/1000);printString(" V\n");
	printString("VM = ");printd(dc_bus_voltage*11);printString(" mV\n");
	#elif defined CM2209C
	printString("VM = ");printd(dc_bus_voltage/20*111/50);printString(" V\t");
	printString("VAC = ");printd(ADC_B_result*2/23);printString(" V\n");
	#else
	printString("\n");
	#endif
	#endif
}

#if defined(STAR) || defined(STAR_V17)
void do_VDC_protection()
{
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	UINT dc_bus_voltage = 0;
	ADC_B_result = 0;

	/*
	Initial_ADC(SAMPLE_DCBUS_ADC);						//Initial ADC B channel for DC_BUS, pin17, CM2209B
	Get_ADC_Result(SAMPLE_DCBUS_ADC);
	Disable_ADC(SAMPLE_DCBUS_ADC);
	*/
	//Initial ADC B for P0_1, pin17
	IOCFGP0_1 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_B_EN;	//select B channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC B result for P0_1
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_B_result = 0;
	if(ADCCHSL&ADC_B_IF)		//select A channel
		ADC_B_result = ((UINT)ADCBH<<8)+ (UINT)ADCBL;

	//Disable ADC B for P0_1
	ADCCHSL &= ~ADC_B_EN;		//select B channel
	IOCFGP0_1 = B00000000;		//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current

	#if 0
	dc_bus_voltage = (UINT)(((unsigned long)ADC_B_result*ADC_FULL*1000)/4096);	//mV
	printString("DC_BUS = ");printd(dc_bus_voltage);printString(" mV\t");

	//printString("VM = ");printd(dc_bus_voltage/10*110/1000);printString(" V\n");
	printString("VM = ");printd(dc_bus_voltage*11);printString(" mV\n");
	#else
	VDC_result_ADC = ADC_B_result;

	if(VDC_result_ADC < VDC24_LOW_OFF_ADC)	// < VDC24*80%
	{
		if(VDC_result_ADC > 5)
		{
		if(PowerState != POWER_LOW)
		{
			PINT0EN = 0;
			PWM16_disable();
			MtState = stop;
			SETUP_target_speed(0);
			power_warning_count = ENABLE_POWER_WARNING_FAST;
			dc_bus_voltage = (UINT)(((unsigned long)VDC_result_ADC*ADC_FULL*1000)/4096);	//mV
			printString("Too Low Voltage: ADC = ");printd(VDC_result_ADC);printString(", VDC = ");printd(dc_bus_voltage);printString("V   STOP\n");
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			PowerState = POWER_LOW;
			ERROR_number = _ERROR_UV;
			//Send_Error_Speed_Cmd(ERROR_number);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		}
		PowerState = POWER_LOW;
		//ERROR_number = _ERROR_UV;
		}
	}
	else if(VDC_result_ADC > VDC24_HIGH_OFF_ADC)	  // > VDC24*120%
	{
		if(PowerState != POWER_HIGH)
		{
			PINT0EN = 0;
			PWM16_disable();
			MtState = stop;
			SETUP_target_speed(0);
			power_warning_count = ENABLE_POWER_WARNING_FAST;
			dc_bus_voltage = (UINT)(((unsigned long)VDC_result_ADC*ADC_FULL*1000)/4096);	//mV
			printString("Too High Voltage: ADC = ");printd(VDC_result_ADC);printString(", VDC = ");printd(dc_bus_voltage);printString("V   STOP\n");
			PowerState = POWER_HIGH;
			ERROR_number = _ERROR_OV;
			//Send_Error_Speed_Cmd(ERROR_number);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		}
		PowerState = POWER_HIGH;
		//ERROR_number = _ERROR_OV;
	}
	#endif
}
#else
void do_VDC_protection()
{
	#if 0
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	UINT dc_bus_voltage = 0;
	ADC_B_result = 0;

	/*
	Initial_ADC(SAMPLE_DCBUS_ADC);						//Initial ADC B channel for DC_BUS, pin17, CM2209B
	Get_ADC_Result(SAMPLE_DCBUS_ADC);
	Disable_ADC(SAMPLE_DCBUS_ADC);
	*/
	//Initial ADC B for P0_1, pin17
	IOCFGP0_1 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_B_EN;	//select B channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC B result for P0_1
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_B_result = 0;
	if(ADCCHSL&ADC_B_IF)		//select A channel
		ADC_B_result = ((UINT)ADCBH<<8)+ (UINT)ADCBL;

	//Disable ADC B for P0_1
	ADCCHSL &= ~ADC_B_EN;		//select B channel
	IOCFGP0_1 = B00000000;		//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current

	dc_bus_voltage = (UINT)(((unsigned long)ADC_B_result*ADC_FULL*1000)/4096);	//mV
	printString("DC_BUS = ");printd(dc_bus_voltage);printString(" mV\t");

	#ifdef CM2209B
	//printString("VM = ");printd(dc_bus_voltage/10*110/1000);printString(" V\n");
	printString("VM = ");printd(dc_bus_voltage*11);printString(" mV\n");
	#elif defined CM2209C
	printString("VM = ");printd(dc_bus_voltage/20*111/50);printString(" V\n");
	#else
	printString("\n");
	#endif
	#else
	unsigned char temp = 30;
	unsigned char ADCCHSL_tmp;
	ADC_B_result = 0;

	/*
	Initial_ADC(SAMPLE_DCBUS_ADC);						//Initial ADC B channel for DC_BUS, pin17, CM2209B
	Get_ADC_Result(SAMPLE_DCBUS_ADC);
	Disable_ADC(SAMPLE_DCBUS_ADC);
	*/
	//Initial ADC B for P0_1, pin17
	IOCFGP0_1 = _ANEN_;			//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current
	ADCCFG = b10000001;			//adcen  -  adcINT cstart  adcfm  -  pre1 pre0(00:/2; 01:/4; 10:/8; 11:/16)	16MHZ/4 = 4MHZ
	temp = 30;
	while(temp--);				//wait until ADC is stable
	ADCAVG = ADC_AVG_TIMES;  	//1 times average (1/2/4/8/16/32/64/test mode)
	ADCCHSL_tmp = ADCCHSL;
	ADCCHSL_tmp |= ADC_B_EN;	//select B channel
	ADCCHSL =ADCCHSL_tmp;
	DelayXms(5);

	//Get ADC B result for P0_1
	ADCCFG = b10110001;			//Start convertion
	while(ADCCFG&0x10);			//Waiting for conversion finish
	ADC_B_result = 0;
	if(ADCCHSL&ADC_B_IF)		//select A channel
		ADC_B_result = ((UINT)ADCBH<<8)+ (UINT)ADCBL;

	//Disable ADC B for P0_1
	ADCCHSL &= ~ADC_B_EN;		//select B channel
	IOCFGP0_1 = B00000000;		//Enable Anolog MUX
	MFCFGP0_1 = PinC_In;		//ADC A3 for instantaneous current

	VDC_result_ADC = ADC_B_result;
	VDC_result = (BYTE)((VDC_result_ADC>>4)&0xff);

	if(VDC_result_ADC < Voltage_Low_Off_ADC)	// < VAC*80%
	{
		if(VDC_result_ADC > 10)
		{
		if(PowerState != POWER_LOW)
		{
			PINT0EN = 0;
			PWM16_disable();
			MtState = stop;
			SETUP_target_speed(0);
			power_warning_count = ENABLE_POWER_WARNING_FAST;
			printString("Too Low Voltage: ADC = ");printd(VDC_result_ADC);printString(", VAC = ");printd(VDC_result_ADC*2/23);printString("V   STOP\n");
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			PowerState = POWER_LOW;
			ERROR_number = _ERROR_UV;
			//Send_Error_Speed_Cmd(ERROR_number);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		}
		PowerState = POWER_LOW;
		//ERROR_number = _ERROR_UV;
		}
	}
	else if(VDC_result_ADC > Voltage_High_Off_ADC)	  // > VAC*120%
	{
		if(PowerState != POWER_HIGH)
		{
			PINT0EN = 0;
			PWM16_disable();
			MtState = stop;
			SETUP_target_speed(0);
			power_warning_count = ENABLE_POWER_WARNING_FAST;
			printString("Too High Voltage: ADC = ");printd(VDC_result_ADC);printString(", VAC = ");printd(VDC_result_ADC*2/23);printString("V   STOP\n");
			PowerState = POWER_HIGH;
			ERROR_number = _ERROR_OV;
			//Send_Error_Speed_Cmd(ERROR_number);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		}
		PowerState = POWER_HIGH;
		//ERROR_number = _ERROR_OV;
	}
	#ifndef MOTOR_HD
	else
	{
		if((VDC_result_ADC > Voltage_Low_On_ADC)&&(PowerState == POWER_LOW))
		{
			printString("[CS8963]: ADC = ");printd(VDC_result_ADC);printString(", VAC = ");printd(VDC_result_ADC*2/23);printString("V\n");
			printString("[CS8963]: Power recovered 1, Reset system.\n");
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			ERROR_number = _ERROR_RECOVER;
			//Send_Error_Speed_Cmd(ERROR_number);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			Reset_system();
		}
		if((VDC_result_ADC < Voltage_High_On_ADC)&&(PowerState == POWER_HIGH))
		{
			printString("[CS8963]: ADC = ");printd(VDC_result_ADC);printString(", VAC = ");printd(VDC_result_ADC*2/23);printString("V\n");
			printString("[CS8963]: Power recovered 2, Reset system.\n");
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			ERROR_number = _ERROR_RECOVER;
			//Send_Error_Speed_Cmd(ERROR_number);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			Reset_system();
		}
		if(PowerState == POWER_NORMAL)
		{
			//ERROR_number = _ERROR_RECOVER;
			//ERROR_number = _ERROR_NONE;
		}
	}
	#endif
	#endif
}
#endif

void precharge_lower_arms()
{
	#ifndef STAR_V17
	#ifdef USE_NNMOS
	P1_0=0;									//close AP
	P1_4=0;									//close BP
	P3_1=0;									//close CP
	
	MFCFGP1_0 = Close;	 P1_1=1;			//A-
	MFCFGP1_4 = Close;	 P1_5=1;			//B-
	MFCFGP3_1 = Close;	 P3_0=1;			//C-
	
	DelayXms(200);DelayXms(200);DelayXms(200);
	DelayXms(200);DelayXms(200);DelayXms(200);
	
	P1_1=0;									//close AN
	P1_5=0;									//close BN
	P3_0=0;									//close CN
	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	//A0
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	//B0
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	//C0
	#endif
	#endif
}

int pp_old = 0;
SLONG ii_old = 0;

void do_check_speed()
{
#ifdef CHECK_SPEED_BY_PID
	SINT error = 0;
	SINT pp = 0;
	SLONG ii = 0;
	SLONG dd = 0;
	SLONG pid = 0;

	error = target_speed - real_speed;
	pp = error;
	ii = pp + ii_old;
	dd = pp - pp_old;
	pid = pp*KP/10 + ii*KI/10 + dd*KD/10;

	if (pid > 0)
	{
		PWM_duty++;
		if(PWM_duty >= 100)
			PWM_duty = 100;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	else if (pid < 0)
	{
		PWM_duty--;
		if(PWM_duty <= 0)
			PWM_duty = 0;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	ii_old = ii;
	pp_old = pp;
#elif defined CHECK_SPEED_BY_LINEAR
	if(real_speed < (target_speed - (RPM_TOLERANCE*3)))
	{
		PWM_duty += 3;
		if(PWM_duty >= 100)
			PWM_duty = 100;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	else if(real_speed > (target_speed + (RPM_TOLERANCE*3)))
	{
		PWM_duty -= 3;
		if(PWM_duty <= 0)
			PWM_duty = 0;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	else if(real_speed < (target_speed - (RPM_TOLERANCE*2)))
	{
		PWM_duty += 2;
		if(PWM_duty >= 100)
			PWM_duty = 100;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	else if(real_speed > (target_speed + (RPM_TOLERANCE*2)))
	{
		PWM_duty -= 2;
		if(PWM_duty <= 0)
			PWM_duty = 0;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	else if(real_speed < (target_speed - RPM_TOLERANCE))
	{
		PWM_duty +=1;
		if(PWM_duty >= 100)
			PWM_duty = 100;
		PWM16_Modify(PWM_period, PWM_duty);
	}
	else if(real_speed > (target_speed + RPM_TOLERANCE))
	{
		PWM_duty -=1;
		if(PWM_duty <= 0)
			PWM_duty = 0;
		PWM16_Modify(PWM_period, PWM_duty);
	}
#else		//CHECK_SPEED_BY_PWM

	if(flag_enable_speed_up_fast == 1)
	{
		if((target_speed > (RPM_TOLERANCE*8)) && (real_speed < (target_speed - (RPM_TOLERANCE*8))))
		{
			check_speed_by_pwm(1, 12);
		}
		else if((target_speed > (RPM_TOLERANCE*4)) && (real_speed < (target_speed - (RPM_TOLERANCE*4))))
		{
			check_speed_by_pwm(1, 6);
		}
		else if(real_speed < (target_speed - RPM_TOLERANCE))
		{
			check_speed_by_pwm(1, 1);
		}
	}
	else
	{
		if((target_speed > (RPM_TOLERANCE*8)) && (real_speed < (target_speed - (RPM_TOLERANCE*8))))
		{
			check_speed_by_pwm(1, 8);
		}
		else if((target_speed > (RPM_TOLERANCE*4)) && (real_speed < (target_speed - (RPM_TOLERANCE*4))))
		{
			check_speed_by_pwm(1, 4);
		}
		else if(real_speed < (target_speed - RPM_TOLERANCE))
		{
			check_speed_by_pwm(1, 1);
		}
	}


	if(flag_enable_speed_down_fast == 1)
	{
		if(real_speed > (target_speed + (RPM_TOLERANCE*8)))
		{
			check_speed_by_pwm(0, 12);
		}
		else if(real_speed > (target_speed + (RPM_TOLERANCE*4)))
		{
			check_speed_by_pwm(0, 6);
		}
		else if(real_speed > (target_speed + RPM_TOLERANCE))
		{
			check_speed_by_pwm(0, 1);
		}
	}
	else
	{
		if(real_speed > (target_speed + (RPM_TOLERANCE*8)))
		{
			check_speed_by_pwm(0, 8);
		}
		else if(real_speed > (target_speed + (RPM_TOLERANCE*4)))
		{
			check_speed_by_pwm(0, 4);
		}
		else if(real_speed > (target_speed + RPM_TOLERANCE))
		{
			check_speed_by_pwm(0, 1);
		}
	}

	/*	testing
	if(flag_reach_target_speed == 0)
	{
		flag_reach_target_speed = 1;
		SETUP_reach_time();
	}
	*/
#endif
}

#ifdef TEST_START
UINT check_test_start = 0;
UINT round = 0;
void do_check_test_start()	//every 50ms * 16 = 0.8 sec
{
	check_test_start++;
	if(flag_mode_type == OPEN_LOOP)
	{
		if(check_test_start == 10)
		{
			clear_rpm_data();
			round++;
			printString("\n\nTest Start, OPEN_LOOP, round ");printd(round);printString("\n");
			Start_Motor();
		}
		else if((check_test_start > 12) && (check_test_start < 590))
		{
			if((check_test_start % 3) == 0)
				check_speed_by_pwm(1, 2);
			else if((check_test_start % 3) == 2)
				record_open_loop_rpm_data();
		}
		else if(check_test_start == 595)
		{
			Stop_Motor();
		}
		else if(check_test_start == 600)
		{
			show_rpm_time_data(round);
			check_test_start = 0;
		}
	}
	else if(flag_mode_type == CLOSE_LOOP)
	{
		if(check_test_start == 10)
		{
			clear_rpm_data();
			round++;
			printString("\n\nTest Start, CLOSE_LOOP, round ");printd(round);printString("\n");
			Start_Motor();
		}
		else if(check_test_start == 45)
		{
			Stop_Motor();
		}
		else if(check_test_start == 50)
		{
			show_rpm_time_data(round);
			check_test_start = 0;
		}
	}
}
#endif

#ifdef CM2209B
BYTE P3_3_old = 1;
#endif
#ifdef USE_HD_CONTROL
BYTE P2_0_old = 0;
BYTE P1_7_old = 0;
#endif

void do_check_key()
{
	#ifndef USE_PCA
	#ifdef CM2209B
	#ifndef STAR
	#ifndef STAR_V17
	if(P3_3 == 1)
	{
		if(P3_3_old == 0)
		{
			if(MtState == stop)
			{
				if(flag_run_dir == CW)
				{
					printString("CCW\n");
					flag_run_dir = CCW;
				}
				else
				{
					printString("CW\n");
					flag_run_dir = CW;
				}
				P3_3_old = 1;
			}
		}
	}
	else
		P3_3_old = 0;
	#endif
	#endif
	#endif

	#ifdef CM2209C
	if(P3_3==0)
	{
	 	DelayXms(1);
		if(P3_3==1)
		{
			if(MtState == stop)
			{
				if(flag_run_dir == CW)
				{
					printString("CCW\n");
					flag_run_dir = CCW;
					#ifndef USE_HD_CONTROL
					P1_7 = 1;
					#endif
				}
				else
				{
					printString("CW\n");
					flag_run_dir = CW;
					#ifndef USE_HD_CONTROL
					P1_7 = 0;
					#endif
				}
			}
		}
	}
	else if(P3_2==0)
	{
	 	DelayXms(1);
		if(P3_2==1)
		{
			if(MtState == stop)
			{
				if(flag_run_dir == CW)
				{
					printString("CCW\n");
					flag_run_dir = CCW;
				}
				else
				{
					printString("CW\n");
					flag_run_dir = CW;
				}
			}
		}
	}
	#endif
	#ifdef USE_HD_CONTROL
	if(P2_0 == 1)
	{
		if(P2_0_old == 0)
		{
			if(MtState == stop)
			{
				if(flag_run_dir == CW)
				{
					printString("CCW\n");
					flag_run_dir = CCW;
				}
				else
				{
					printString("CW\n");
					flag_run_dir = CW;
				}
				P2_0_old = 1;
			}
		}
	}
	else
		P2_0_old = 0;

	if(P1_7 == 1)
	{
		if(P1_7_old == 0)
		{
			MtState = stop;
			real_speed = 0;
			PINT0EN = 0;
			PWM16_disable();
			MT_Brake();
			P1_7_old = 1;
			printString("BRAKE, Hall: ");get_current_hall_state();printString("\n");
		}
	}
	else
		P1_7_old = 0;
	#endif
	#endif
}

void calculate_real_speed()
{
	#if defined(STAR) || defined(STAR_V17)
	real_speed = 600000/pwm16_int_cnt_tmp;	//star uses 7 pairs, 0.5 round
	#elif defined HD
	real_speed = 2400000/pwm16_int_cnt_tmp;	//hd uses 4 pairs, 2 rounds
	#else	//normal case
	//real_speed = 12000000/pwm16_int_cnt;	//2 pair
	//real_speed = 6000000/pwm16_int_cnt;	//4 pair
	//real_speed = (UINT)((24000000/(ULONG)number_motor_pole_pair)/((ULONG)pwm16_int_cnt));
	real_speed = (24000000/number_motor_pole_pair)/pwm16_int_cnt_tmp;
	#endif
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
}
