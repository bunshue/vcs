#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "CS8963_Initial.h"
#include "CS8963_Function.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_PWM.h"
#include "CS8963_Setup.h"
#include "Setup.h"
#include "Setup_function.h"
#include "Pin_Config.h"
#include "CS8963_WatchDog.h"
#include "CS8963_MysonLink.h"
#include "CS8963_Test.h"
#include "CS8963_Timer.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive BLDC
 * Filename: CS8963_BLDC.C
 * Author  :
 * Date    : 2015/01/07
 **********************************************************/

void main(void)
{
	EWT = 0; 													//Disable WDT
	WTST = 0;													//Wait state cycle = 1
	EXIP=0x08;													//Setup PWM16 int as the highest priority

	SETUP_System();		//Setup IOSC, UART
	Initial_IO();												//Initila IO
	SETUP_Parameter();	//Setup software parameters
	SETUP_HallSensor();	//Setup Hall sensor
	//SETUP_PWM();		TBD
	SETUP_Key();
	SETUP_LED();
	//PIN_CONFIG_setup_adc(PIN_VRin);							//Initial ADC A channel, pin 13
	//Initial_ADC(PIN13);										//Initial ADC A channel, pin 13

	Show_SETUP_Info();

	#ifdef SAVE_FACTORY_DATA
	Initial_Timer5();											//Initial Timer5
	#endif
	#ifdef TEST_START
	Initial_Timer5();											//Initial Timer5
	#endif

	CS8963_Test();
	SETUP_Timer();

	DelayXms(2);												//boost cap charge delay
	EA = 1;														//Enable interrupt
	//Initial_IO();												//Initila IO	??
	DelayXms(4);
	Hal_sta=((P0&0x1C)>>2);										//check Hall position

	#ifdef CHECK_VDC_VOLTAGE
	do_check_vdc_voltage();
	#endif

	//Initial_PWM16(PWM_period,PWM_duty);		reserved
	power_warning_count = ENABLE_POWER_WARNING_SLOW;

	if(flag_vdc_protection == 1)
		do_VDC_protection();

	if(flag_enable_watchdog)
		Kick_WDT();

	#ifdef TEST_START
	flag_speed_control_mode = NORMAL_MODE;
	#else
	if(flag_speed_control_mode == VR_MODE)
	{
		if(flag_mode_type == OPEN_LOOP)
			do_check_VR_open_loop();
		else
			do_check_VR_close_loop();
	}
	#endif

	#ifdef USE_PCA_AUTO_RUN
	printString("\nPCA_AUTO_RUN\n\n");
	Start_Motor();
	#endif

	while(1)
	{
		if(flag_enable_watchdog)
			Kick_WDT();

		do_check_key();

		if(MtState_changed())
		{
			switch(MtState)
			{
				case start:	
					//printString("Start Hall: ");get_current_hall_state();printString("\n");
					if(MtState == stop)
						Start_Motor();
					break;
				case stop:
					Stop_Motor();
					break;
				default:
					break;
			}
		}

		if((flag_vdc_protection == 1) && (flag_check_vdc == 1))
		{
			flag_check_vdc = 0;
			do_VDC_protection();
		}

		if((flag_speed_control_mode == VR_MODE) && (flag_check_vr == 1))
		{
			flag_check_vr = 0;
			if(flag_mode_type == OPEN_LOOP)
				do_check_VR_open_loop();
			else
				do_check_VR_close_loop();
		}

		if((flag_mode_type == OPEN_LOOP) && (flag_check_speed == 1) && (motor_start == 0))
		{
			calculate_real_speed();
		}
		else if((flag_mode_type == CLOSE_LOOP) && (flag_check_speed == 1) && (motor_start == 1))
		{
			calculate_real_speed();
		}
		else if((flag_mode_type == CLOSE_LOOP) && (flag_check_speed == 1) && (motor_start == 0))
		{
			calculate_real_speed();
			flag_check_speed = 0;
			do_check_speed();
		}

		if(flag_check_over_current == 1)	//do OCA
		{
			flag_check_over_current = 0;
			if((flag_over_current_protection&0x01)==1)
				do_over_current_protection_adc();
		}

		if(flag_lock_rotor_protection == 1)
		{
			if(flag_check_lock_rotor == 1)
			{
				flag_check_lock_rotor = 0;
				do_check_lock_rotor_protection();
			}
		}

		#ifdef TEST_START
		if(flag_check_test_start == 1)	//every 50ms * 16 = 0.8 sec
		{
			flag_check_test_start = 0;
			do_check_test_start();
		}
		#endif

		if(flag_debug_mode == 1)
		{
			if(flag_check_debug_message == 1)
			{
				flag_check_debug_message = 0;
				print_debug_message();
			}
		}
		if(flag_print_message == 1)
		{
			flag_print_message = 0;
			print_message();
		}
		//DelayXms(100);
	}
}
