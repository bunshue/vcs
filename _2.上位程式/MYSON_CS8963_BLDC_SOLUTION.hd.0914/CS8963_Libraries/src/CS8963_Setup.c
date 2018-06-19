#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "CS8963_Setup.h"
#include "CS8963_Function.h"
#include "CS8963_ADC.h"
#include "CS8963_Clock.h"
#include "CS8963_Config.h"
#include "CS8963_Initial.h"
#include "CS8963_UART.h"
#include "CS8963_Timer.h"
#include "CS8963_PWM.h"
#include "CS8963_PCA.h"
#include "CS8963_WatchDog.h"
#include "Setup.h"
#include "Setup_function.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function
 * Filename: CS8963_Setup.C
 * Author  :
 * Date    : 2015/01/13
 **********************************************************/

void Show_SETUP_Info(void)
{
	ULONG voltage = 0;
	#ifdef LESS_CODE
	printString("\n\nBLDC start\n");
	#else
	printString("\n");printString("\n");
	printString(RELEASE_INFO);
	printString("Compiled time: ");printString(__DATE__);printS(' ');printString(__TIME__);printString("\n");
	printString(__FILE__);printS('(');printd(__LINE__);printS(')');printString("\n");
	#ifdef CM2209B	
	printString("CM2209B LV_DEMO_BOARD use CS7211\t");
	#elif defined CM2209D
	printString("CM2209D LV_DEMO_BOARD use IR2101\t");
	#elif defined CM2209C
	printString("CM2209C HV_DEMO_BOARD\t");
	#elif defined CM2209A
	printString("CM2209A LV_DEMO_BOARD use level shift\t");
	#elif defined CM2209_K1
	printString("CM2209 K1 customer board 1\t");
	#else
	printString("BOARD_VERSION unknown\t");
	#endif

	#ifdef USE_NNMOS
	printString("USE_NNMOS\n");
	#elif defined USE_PNMOS
	printString("USE_PNMOS\n");
	#else
	printString("MOS Type Unknown\n");
	#endif

	printString("UART_BD_OFFSET = ");
	printd(UART_BD_OFFSET);

	#ifdef NO_PRINT_WHEN_RUNNING
	printString("\tNO_PRINT_WHEN_RUNNING");
	#endif
	printString("\n");

	#ifdef USE_MYSONLINK
	printString("USE_MYSONLINK\n");
	#endif

	#ifdef STAR
	printString("STAR version\n");
	#endif

	#ifdef STAR_V17
	printString("STAR_V17 version\n");
	#endif

	printString("ENABLE PWM mode, \t");
	if(flag_sensor_type == HALL_SENSOR_MODE)
		printString("Hall Sensor Mode\n");
	else if(flag_sensor_type == SENSORLESS_MODE)
		printString("Sensorless Mode\n");
	else if(flag_sensor_type == PCA_MODE)
	{
		printString("PCA Mode");
		#ifdef USE_PCA_AUTO_RUN
		printString("\tEnable PCA_AUTO_RUN\n");
		printString("PCA_START_DUTY:  ");printd(PCA_START_DUTY);
		printString("\tPCA_DUTY_MAX:  ");printd(PCA_DUTY_MAX);printString("\n");
		#endif
	}
	else
		printString("Unknown Sensor Mode\n");

	#if ENABLE_PHASE_COMPENSATION == 1
	if(flag_phase_compensation_mode)
	{
		printString("Phase Compensation Mode, PHASE_ANGLE_CW = ");printd(PHASE_ANGLE_CW);printString(", PHASE_ANGLE_CCW = ");printd(PHASE_ANGLE_CCW);
		if(flag_run_dir == CW)
			phase_angle = PHASE_ANGLE_CW;
		else
			phase_angle = PHASE_ANGLE_CCW;
		printString(", phase_angle = ");printd(phase_angle);printString("\n");
		PCA_EN = 1;											//use PWM interrupt
	}
	#endif

	if(flag_mode_type == CLOSE_LOOP)
	{
		printString("CLOSE ");
	}
	else if(flag_mode_type == OPEN_LOOP)
	{
		printString("OPEN ");
	}
	printString("LOOP\t");
	if(flag_run_dir == CW)
		printString("CW");
	else
		printString("CCW");
	printString("\n");
	printString("Motor setup:\t");

	#ifdef MOTOR_M0
	printString("MOTOR_M0\n");
	#elif defined MOTOR_M1
	printString("MOTOR_M1\n");
	#elif defined MOTOR_M2
	printString("MOTOR_M2\n");
	#elif defined MOTOR_M3
	printString("MOTOR_M3\n");
	#elif defined MOTOR_M4
	printString("MOTOR_M4\n");
	#elif defined MOTOR_HD
	printString("MOTOR_HD\n");
	#elif defined MOTOR_STAR
	printString("MOTOR_STAR\n");
	#else
	printString("MOTOR others\n");
	#endif
	printString("MOTOR_POLE_PAIR: ");printd(MOTOR_POLE_PAIR);printString("\n");
	printString("PWM_START_DUTY:  ");printd(PWM_START_DUTY);printString("\n");
	printString("PWM_PERIOD:\t0x");printx(PWM_period);printString(" = ");printd(PWM_period);printString(" (points)\n");
	PWM_freq = iSYSCLK/2/PWM_period;	//PWM_freq = 1/((1/16M)*point*2)
	printString("PWM_FREQ:\t");printd(PWM_freq);printString(" Hz\n");
	printString("TARGET_SPEED: ");printd(TARGET_SPEED);
	printString(", MAX: ");printd(MAXSPEED);
	printString(", MIN: ");printd(MINSPEED);
	printString(", STEP_SIZE: ");printd(number_rpm_step_size);
	printString(", TOLERANCE: ");printd(rpm_tolerance);
	printString("\n");
	printString("VR:\t");
	#ifdef USE_VR_RESUME
		printString("USE_VR_RESUME\t");
	#else
		printString("NO_USE_VR_RESUME\t");
	#endif
	#ifdef USE_VR_TOLERANCE
	{
		printString("USE_VR_TOLERANCE, tolerance: ");printd(VR_TOLERANCE);printString(" ADC\n");
	}
	#else
		printString("NO_USE_VR_TOLERANCE\n");
	#endif
	printString("\tVR_MAX: ");printd(VR_MAX);
	printString("mV\tVR_MIN: ");printd(VR_MIN);
	printString("mV\n\tDUTY_MAX: ");printd(VR_SPEED_DUTY_MAX);
	printString("%\tDUTY_MIN: ");printd(VR_SPEED_DUTY_MIN);
	printString("%\n\tRPM_MAX: ");printd(VR_SPEED_RPM_MAX);
	printString("\tRPM_MIN: ");printd(VR_SPEED_RPM_MIN);printString("\n");

	#ifdef PWM_TRIGGER_ADC
	printString("PWM_TRIGGER_ADC\n");
	#endif

	printString("slow modify speed = ");printd(slow_modify_speed);printString("\n");

	if(flag_speed_control_mode == VR_MODE)
	{
		printString("Enable VR speed control mode\n");
		//Initial_ADC(PIN_VRin);									//Initial ADC for pin PIN_VRin
	}
	else
	{
		printString("Enable NORMAL speed control mode\n");
	}

	#if ENABLE_PHASE_COMPENSATION == 1
	if( flag_phase_compensation_mode )
	{
		//PIN_CONFIG_setup_gpio(PIN1);		//CM2209B can not use this
		#ifndef STAR_V17
		PIN_CONFIG_setup_gpio(PIN2);		//STAR_V17 can not use this
		#endif
		PIN_CONFIG_setup_gpio(PIN3);
		PIN_CONFIG_setup_gpio(PIN4);
		PIN_CONFIG_setup_gpio(PIN17);
		PIN_CONFIG_setup_gpio(PIN25);
	}
	#endif
	
	//IFB_Read_256Byte();						//Print Information Block (IFB) data.
	#ifdef ENABLE_FG_OUT
	printString("ENABLE_FG_OUT, use pin ");printd(PIN_FG_OUT);printString("\n");
	#endif

	if(flag_enable_watchdog)
		printString("Watchdog      PROTECTION enabled.\n");
	else
		printString("Watchdog      PROTECTION disabled.\n");

	if(flag_hall_protection == 1)
		printString("Hall sequence PROTECTION enabled\n");
	else
		printString("Hall sequence PROTECTION disabled.\n");

	if(flag_vdc_protection == 1)
	{
		#if defined(CM2209B) || defined(CM2209C)
		printString("VDC           PROTECTION enabled\n");
		#endif
	}
	else
		printString("VDC           PROTECTION disabled.\n");

	if(flag_lock_rotor_protection)
		printString("LOCK ROTOR    PROTECTION enabled.\n");
	else
		printString("LOCK ROTOR    PROTECTION disabled.\n");
	if((flag_over_current_protection&0x01) == 1)
	{
		printString("OVER CURRENT  PROTECTION A enabled.");
		printString("\tADC value: 0x");
		printx(Over_Current_ADC);
		printString("\tADC limit: ");
		voltage=((unsigned long)Over_Current_ADC*5000)/4095;
		printv(voltage);
		printString(" V\n");
	}
	else
		printString("OVER CURRENT  PROTECTION A disabled.\n");

	if((flag_over_current_protection&0x02) == 2)
	{
		printString("OVER CURRENT  PROTECTION C enabled.");
		printString("\tCMP value: 0x");
		printx(CMPVTH_VALUE);
		printString("\t\tCMP limit: ");
		voltage=(unsigned long)CMPVTH_VALUE*9*1000/5/255;
		printv(voltage);
		printString(" V\n");
	}
	else
		printString("OVER CURRENT  PROTECTION C disabled.\n");

	if((flag_over_current_protection&0x04) == 4)
		printString("OVER CURRENT  PROTECTION X enabled.\n");
	else
		printString("OVER CURRENT  PROTECTION X disabled.\n");

	printString("OVER_CURRENT_VALUE: 0x");printx(OVER_CURRENT_VALUE);printS('=');printd(OVER_CURRENT_VALUE);printString("\n");
	printString("VAC_HIGH_OFF: ");printd(adc2vac(VAC_HIGH_OFF_ADC));printString(" VAC,\t");printString("VAC_LOW_OFF: ");printd(adc2vac(VAC_LOW_OFF_ADC));printString(" VAC\n");
	printString("VAC_HIGH_ON:  ");printd(adc2vac(VAC_HIGH_ON_ADC));printString(" VAC,\t");printString("VAC_LOW_ON:  ");printd(adc2vac(VAC_LOW_ON_ADC));printString(" VAC\n");

	#ifdef MOTOR_HD
	#ifndef USE_HD_CONTROL
	printString("\nUse MOTOR_HD\t");
	#ifdef USE_AC_220
	printString("USE_AC_220\t");
	#else
	printString("USE_AC_110\t");
	#endif
	printString("MAX_RPM: ");printd(HD_RPM_MAX);printString(",\tMIN_RPM: ");printd(HD_RPM_MIN);printString("\n\n");
	#endif
	#endif
	#ifdef USE_HD_CONTROL
	printString("\nUSE_HD_CONTROL, setup:\t");
	printd(P2_1);printS(' ');
	printd(P2_2);printS(' ');
	printd(P2_3);printS(' ');
	printd(P2_4);printS(' ');
	printd(P2_5);printS(' ');
	printd(P2_6);printString("\n");
	if(P2_3 == 1)
		SETUP_vr_max_speed(HD_RPM_MAX_3600);
	else
		SETUP_vr_max_speed(HD_RPM_MAX_1800);
	SETUP_vr_min_speed(HD_RPM_MIN);
	printString("MAX_RPM:\t");printd(vr_max_speed);printString(",\tMIN_RPM: ");printd(vr_min_speed);
	printString(",\tTOLERANCE: ");printd(rpm_tolerance);printString("\n");
	printString("MAX_POWER:\t");printd(max_power);printString(" W\n");
	printString("AC_VOLTAGE:\t");printd(ac_voltage);printString(" V\n");

	if(flag_enable_speed_up_fast == 1)
		printString("Speed up:\tfast\n");
	else
		printString("Speed up:\tslow\n");
	if(flag_enable_speed_down_fast == 1)
		printString("Speed down:\tfast\n");
	else
		printString("Speed down:\tslow\n");
	if(flag_enable_brake == 1)
		printString("Brake:\tON\n");
	else
		printString("Brake:\tOFF\n");
	#endif
	#endif
}

void SETUP_System(void)
{
	#ifdef CM2209C		//CM2209C needs boost time
	int i;
	#endif

 	Initial_REGTRM(IFB_Read_1Byte(0x20));					//Initial IOSC:
	Initial_IOSC(IFB_Read_1Byte(0x21), IFB_Read_1Byte(0x22) + UART_BD_OFFSET);	//Default IOSC: 16MHz

	#ifdef USE_XOSC
	DelayXms(200);
	Initial_XOSC();
	Initial_EUART2(BAUD_RATE, xSYSCLK);						//Initial EUART2
	#else
	Initial_EUART2(BAUD_RATE, iSYSCLK);						//Initial EUART2
	#endif

	//Wait for system stable
	DelayXms(200);DelayXms(200 );DelayXms(200);DelayXms(200);

	//Initial PWM setting for NNMOS
	#ifdef USE_NNMOS
	#ifdef STAR
	P1_1=1;
	P1_5=1;
	P3_0=1;
	#elif defined STAR_V17
	P1_1=1;
	P1_7=1;
	P3_0=1;
	#else
	P1_1=0;
	P1_5=0;
	P3_0=0;
	#endif
	P1_0=0;
	#ifdef STAR_V17
	P1_6=0;
	#else
	P1_4=0;
	#endif
	P3_1=0;

	MFCFGP1_0=0x01;IOCFGP1_0=PinC_InOutCMOS;  		//PWMAP
	MFCFGP1_1=0x01;IOCFGP1_1=PinC_InOutCMOS;  		//PWMAN
	#ifdef STAR_V17
	MFCFGP1_6=0x01;IOCFGP1_6=PinC_InOutCMOS;  		//PWMBP
	MFCFGP1_7=0x01;IOCFGP1_7=PinC_InOutCMOS;  		//PWMBN
	#else
	MFCFGP1_4=0x01;IOCFGP1_4=PinC_InOutCMOS;  		//PWMBP
	MFCFGP1_5=0x01;IOCFGP1_5=PinC_InOutCMOS;  		//PWMBN
	#endif
	MFCFGP3_1=0x01;IOCFGP3_1=PinC_InOutCMOS;  		//PWMCP
	MFCFGP3_0=0x01;IOCFGP3_0=PinC_InOutCMOS;  		//PWMCN
	#endif

	#ifdef CM2209C		//CM2209C needs boost time
	for(i=0; i<20; i++)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	#endif
}

void SETUP_Parameter(void)
{
	UINT dc_bus_voltage = 0;
	SETUP_target_speed(TARGET_SPEED);
	SETUP_PWM_period(PWM_PERIOD);
	SETUP_PWM_start_duty(PWM_START_DUTY);
	SETUP_PWM_duty(PWM_START_DUTY);
	SETUP_PWM_dead_time(PWM_DEAD_TIME);
	SETUP_direction(DIRECTION);
	SETUP_slow_modify_speed(SLOW_MODIFY_SPEED);
	SETUP_speed_control_mode(SPEED_CONTROL_MODE);
	SETUP_mode_type(MODE_TYPE);
	SETUP_sensor_mode(SENSOR_MODE);
	SETUP_debug_mode(DEBUG_MODE);
	SETUP_phase_compensation_mode(ENABLE_PHASE_COMPENSATION);
	SETUP_enable_watchdog(ENABLE_WATCHDOG);
	SETUP_enable_over_current_protection(ENABLE_OVER_CURRENT_PROTECTION_A|(ENABLE_OVER_CURRENT_PROTECTION_C<<1)|(ENABLE_OVER_CURRENT_PROTECTION_X<<2));
	SETUP_enable_lock_rotor_protection(ENABLE_LOCK_ROTOR_PROTECTION);
	SETUP_enable_vdc_protection(ENABLE_VDC_PROTECTION);
	SETUP_enable_hall_protection(ENABLE_HALL_PROTECTION);
	SETUP_motor_pole_pair(MOTOR_POLE_PAIR);
	//SETUP_motor_uvw_sequence(MOTOR_UVW_SEQUENCE_TYPE);
	SETUP_rpm_step_size((MAXSPEED-MINSPEED)/(100-PWM_START_DUTY));
	max_speed = MAXSPEED;
	min_speed = MINSPEED;
	rpm_tolerance = RPM_TOLERANCE;
	acceleration = ACCELERATION;
	if((flag_over_current_protection&0x01) == 1)
		SETUP_Over_Current_ADC(Over_Current_ADC);
	if((flag_over_current_protection&0x02) == 2)
		Initial_Comparator_VTH1(CMPVTH_VALUE);					//Initial Comparator

	if(flag_sensor_type == PCA_MODE)
		PCA_Mode_Setup();

	if(flag_enable_watchdog)
		Initial_WDT();										//Enable WDT
	else
		EWT = 0; 											//Disable WDT

	if(flag_vdc_protection == 1)
	{
		#if defined(CM2209B) || defined(CM2209C)
		Initial_ADC(SAMPLE_DCBUS_ADC);						//Initial ADC B channel for DC_BUS, pin17, CM2209B
		Get_ADC_Result(SAMPLE_DCBUS_ADC);
		Disable_ADC(SAMPLE_DCBUS_ADC);
		dc_bus_voltage = (UINT)(((unsigned long)ADC_B_result*ADC_FULL*1000)/4096);	//mV
		//printString("DC_BUS = ");printd(dc_bus_voltage);printString("mV\n");
		#endif
	}

	#ifdef ENABLE_FG_OUT
	PIN_CONFIG_setup_gpio(PIN_FG_OUT);
	#endif

	#ifdef USE_HD_CONTROL
	if(P2_6 == 1)
		SETUP_enable_speed_down_fast(1);
	else
		SETUP_enable_speed_down_fast(0);
	if(P2_5 == 1)
		SETUP_enable_speed_up_fast(1);
	else
		SETUP_enable_speed_up_fast(0);
	if(P2_4 == 1)
		SETUP_enable_brake(1);
	else
		SETUP_enable_brake(0);
	if(P2_3 == 1)
	{
		SETUP_vr_max_speed(HD_RPM_MAX_3600);
		rpm_tolerance = 15;
	}
	else
	{
		SETUP_vr_max_speed(HD_RPM_MAX_1800);
		rpm_tolerance = 7;
	}
	if(P2_2 == 1)
		SETUP_max_power(400);
	else
		SETUP_max_power(200);
	if(P2_1 == 1)
	{
		SETUP_AC_voltage(220);
		if(flag_vdc_protection == 1)
		{
			SETUP_VDC_protection_adc(VAC_HIGH_OFF_ADC_220, VAC_HIGH_ON_ADC, VAC_LOW_ON_ADC, VAC_LOW_OFF_ADC_220);
		}
	}
	else
	{
		SETUP_AC_voltage(110);
		if(flag_vdc_protection == 1)
		{
			SETUP_VDC_protection_adc(VAC_HIGH_OFF_ADC_110, VAC_HIGH_ON_ADC, VAC_LOW_ON_ADC, VAC_LOW_OFF_ADC_110);
		}
	}
	#else
	SETUP_enable_speed_down_fast(0);
	SETUP_enable_speed_up_fast(0);
	SETUP_enable_brake(1);
	SETUP_vr_max_speed(VR_SPEED_RPM_MAX);
	SETUP_vr_min_speed(VR_SPEED_RPM_MIN);
	SETUP_max_power(400);
	SETUP_AC_voltage(220);
	if(flag_vdc_protection == 1)
	{
		SETUP_VDC_protection_value(275, 260, 180, 165);
		SETUP_VDC_protection_adc(VAC_HIGH_OFF_ADC, VAC_HIGH_ON_ADC, VAC_LOW_ON_ADC, VAC_LOW_OFF_ADC);
	}
	#endif
}

void SETUP_HallSensor(void)
{
	IOCFGP0_2 = PinC_InHoldPu;  MFCFGP0_2 = B00000011;	//PINT0  only input
	IOCFGP0_3 = PinC_InHoldPu;  MFCFGP0_3 = B00000011;	//PINT0  only input
	IOCFGP0_4 = PinC_InHoldPu;  MFCFGP0_4 = B00000011;	//PINT0  only input

	PIOEDGR0 &= ~0x1C;
	PIOEDGF0 &= ~0x1C;
	PIOEDGR0 = 0x1C;
	PIOEDGF0 = 0x1C;

	PINT0EN = 0;									//enable PINT0EN.1
	PX0 = 1;										//Pin Interrupt INT0 Priority bit.
}

void SETUP_PWM(void)
{
	//TBD
}

void SETUP_Key(void)
{
	/*Initial key*/
	#ifndef USE_PCA	
	#ifdef CM2209B
	PIN_CONFIG_setup_key(_P3_3);	//setup push button K1
	//PIN_CONFIG_setup_key(_P2_0);	//setup push button K2
	PIN_CONFIG_setup_key(_P3_2);	//receive fault signal from CS7211
	#endif

	#ifdef CM2209C
	PIN_CONFIG_setup_key(_P3_2);	//setup push button K3
	PIN_CONFIG_setup_key(_P3_3);	//setup push button K2
	#endif

	#ifdef CM2209D
	//PIN_CONFIG_setup_key(_P2_2);	//setup push button K4	KEY3	move to sensorless debug pin 1
	//PIN_CONFIG_setup_key(_P2_1);	//setup push button K3	KEY2	move to sensorless debug pin 2
	//PIN_CONFIG_setup_key(_P2_0);	//setup push button K2	KEY1	move to FG out
	PIN_CONFIG_setup_key(_P3_2);	//setup push button K5	KEY4
	#endif
	#endif
}

void SETUP_LED(void)
{
	#ifdef CM2209A
	PIN_CONFIG_setup_gpio(_P1_6);	//setup gpio for LED D19, PORT1
	//PIN_CONFIG_setup_gpio(_P2_0);	//setup gpio for LED D21, PORT2	P2_0 move to FG out
	#elif defined CM2209B
	PIN_CONFIG_setup_gpio(_P1_3);	//setup gpio for LED D3, PORT1
	PIN_CONFIG_setup_gpio(_P1_2);	//setup gpio for LED D4, PORT2
	//PIN_CONFIG_setup_gpio(_P2_0);	//setup gpio for LED D5, PORT3
	#ifndef STAR_V17
	PIN_CONFIG_setup_gpio(_P1_6);	//setup gpio for LED D6, PORT4
	#endif
	#elif defined CM2209C
	#ifndef USE_HD_CONTROL
	PIN_CONFIG_setup_gpio(_P1_7);	//setup gpio for LED D44, PORT1
	P1_7 = 0;	//ON
	#endif
	PIN_CONFIG_setup_gpio(_P1_3);	//setup gpio for LED D46, PORT3
	//PIN_CONFIG_setup_gpio(_P2_0);	//setup gpio for LED D47, PORT4		move to FG out
	//PIN_CONFIG_setup_gpio(_P2_1);	//setup gpio for LED D48, PORT5		move to sensorless debug pin 2
	//PIN_CONFIG_setup_gpio(_P2_2);	//setup gpio for LED D49, PORT6		move to sensorless debug pin 1
	//P2_0 = 0;	//ON
	//P2_1 = 0;	//ON
	//P2_2 = 0;	//ON
	#elif defined CM2209D
	PIN_CONFIG_setup_gpio(_P1_7);	//setup gpio for LED D11, PORT1
	PIN_CONFIG_setup_gpio(_P1_6);	//setup gpio for LED D12, PORT2
	PIN_CONFIG_setup_gpio(_P0_5);	//setup gpio for LED D13, PORT3
	PIN_CONFIG_setup_gpio(_P0_1);	//setup gpio for LED D15, BRAKE
	P1_7 = 0;	//ON
	P1_6 = 0;	//ON
	P0_5 = 0;	//ON
	P0_1 = 0;	//ON
	#endif
}

void SETUP_Timer(void)
{
	Initial_Timer0();					//Initial Timer0
	Initial_Timer1();					//Initial Timer1	for speed up/down
	//Initial_Timer3();					//Initial Timer3
	//Initial_Timer4();					//Initial Timer4
	Initial_Timer5();					//Initial Timer5, for clock mode
	#ifdef USE_MYSONLINK
	if(flag_mysonlink_update_message == 1)
		Initial_Timer3();				//Initial Timer3
	#endif
}

void SETUP_enable_brake(unsigned char enable_brake)
{
	flag_enable_brake = enable_brake;
}

void SETUP_enable_speed_up_fast(unsigned char enable_speed_up_fast)
{
	flag_enable_speed_up_fast = enable_speed_up_fast;
}

void SETUP_enable_speed_down_fast(unsigned char enable_speed_down_fast)
{
	flag_enable_speed_down_fast = enable_speed_down_fast;
}

void SETUP_vr_max_speed(unsigned int speed)
{
	vr_max_speed = speed;
}

void SETUP_vr_min_speed(unsigned int speed)
{
	vr_min_speed = speed;
}

void SETUP_max_power(unsigned int power)
{
	max_power = power;
}

void SETUP_AC_voltage(unsigned int voltage)
{
	ac_voltage = voltage;
}

void SETUP_target_speed(unsigned int speed)
{
	target_speed = speed;
	//rpm_tolerance = speed*RPM_TOLERANCE_P/100;	//reserved
}

void SETUP_PWM_period(unsigned int pwm_period)
{
	PWM_period = pwm_period;
}

void SETUP_PWM_start_duty(unsigned char pwm_start_duty)
{
	PWM_start_duty = pwm_start_duty;
}

void SETUP_PWM_duty(unsigned char pwm_duty)
{
	PWM_duty = pwm_duty;
}

void SETUP_PWM_duty_target(unsigned char pwm_duty_target)
{
	PWM_duty_target = pwm_duty_target;
}

void SETUP_PWM_duty_new(unsigned char pwm_duty_new)
{
	PWM_duty_new = pwm_duty_new;
}

void SETUP_PWM_dead_time(unsigned char pwm_dead_time)
{
	PWM_dead_time = pwm_dead_time;
}

void SETUP_motor_uvw_sequence(unsigned char uvw_sequence)
{
	motor_uvw_sequence = uvw_sequence;
	printString("SETUP motor UVW sequence, type: ");printd(motor_uvw_sequence);printString("\n");
}

void SETUP_direction(unsigned char direction)
{
	flag_run_dir = direction;
}

void SETUP_slow_modify_speed(unsigned char speed)
{
	slow_modify_speed = speed;
}

void SETUP_mode_type(unsigned char mode_type)
{
	flag_mode_type = mode_type;
}

void SETUP_sensor_mode(unsigned char sensor_type)
{
	flag_sensor_type = sensor_type;
}

void SETUP_speed_control_mode(unsigned char speed_control_mode)
{
	flag_speed_control_mode = speed_control_mode;
}

void SETUP_debug_mode(unsigned char debug_mode)
{
	flag_debug_mode = debug_mode;
}

void SETUP_phase_compensation_mode(unsigned char phase_compensation_mode)
{
	flag_phase_compensation_mode = phase_compensation_mode;
}

void SETUP_enable_watchdog(unsigned char enable_watchdog)
{
	flag_enable_watchdog = enable_watchdog;
}

void SETUP_enable_over_current_protection(unsigned char over_current_protection)
{
	flag_over_current_protection = over_current_protection;
}

void SETUP_enable_lock_rotor_protection(unsigned char lock_rotor_protection)
{
	flag_lock_rotor_protection = lock_rotor_protection;
}

void SETUP_enable_vdc_protection(unsigned char vdc_protection)
{
	flag_vdc_protection = vdc_protection;
}

void SETUP_enable_hall_protection(unsigned char hall_protection)
{
	flag_hall_protection = hall_protection;
}

void SETUP_motor_pole_pair(unsigned char motor_pole_pair)
{
	number_motor_pole_pair = motor_pole_pair;
}

void SETUP_rpm_step_size(UINT rpm_step_size)
{
	number_rpm_step_size = rpm_step_size;
}

void SETUP_PWMCNT_diff(ULONG PWM16INT_cnt_start, ULONG PWM16INT_cnt_diff)
{
	pwm_cnt_start = PWM16INT_cnt_start;
	pwm_cnt_diff = PWM16INT_cnt_diff;
}

void SETUP_PWMCNT_diff2(ULONG PWM16INT_cnt_start, ULONG PWM16INT_cnt_diff)
{
	pwm_cnt_start2 = PWM16INT_cnt_start;
	pwm_cnt_diff2 = PWM16INT_cnt_diff;
}

void SETUP_Over_Current_ADC(UINT adc)
{
	Over_Current_ADC = adc;
}

void SETUP_VDC_protection_value(UINT v1, UINT v2, UINT v3, UINT v4)
{
	Voltage_High_Off = v1;
	Voltage_High_On = v2;
	Voltage_Low_On = v3;
	Voltage_Low_Off = v4;
}

void SETUP_VDC_protection_adc(UINT adc_1, UINT adc_2, UINT adc_3, UINT adc_4)
{
	Voltage_High_Off_ADC = adc_1;
	Voltage_High_On_ADC = adc_2;
	Voltage_Low_On_ADC = adc_3;
	Voltage_Low_Off_ADC = adc_4;
}
