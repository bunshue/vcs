/**********************************************************
 * Chips   : CS8963
 * Purpose : BLDC initial
 * Filename: CS8963_Initial.C
 * Author  :
 * Date    : 2015/01/07
 **********************************************************/

#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_Function.h"
#include "CS8963_Initial.h"
#include "CS8963_Config.h"
#include "CS8963_DAC.h"
#include "CS8963_MysonLink.h"

#define PARSE_IFB

#ifdef PARSE_IFB
BYTE IFB_DATA[256] = 0;
#endif
bit flag_check_vdc = 0;
bit flag_check_vr = 0;
bit flag_check_speed = 0;
bit flag_check_lock_rotor = 0;
bit flag_check_over_current = 0;
bit flag_check_test_start = 0;
bit flag_check_debug_message = 0;
bit flag_check_status = 0;
bit flag_send_hall_status = 0;
bit flag_print_message = 0;
bit flag_PWM16_Modify = 0;
bit flag_int0_ser = 0;
BYTE check_speed = 0;
UINT  PWM_period = PWM_PERIOD;
unsigned char PWM_start_duty = PWM_START_DUTY;
unsigned char PWM_duty = PWM_START_DUTY;
unsigned char PWM_duty_target = 0;
unsigned char PWM_duty_old = PWM_START_DUTY;
unsigned char PWM_duty_new = 0;
unsigned char PWM_dead_time = 0;
unsigned char pwm_input_duty = 0;
unsigned char pwm_input_duty_old = 0;
unsigned char PCA_duty = PCA_START_DUTY;
unsigned char PCA_duty_old = PWM_START_DUTY;
unsigned char PCA_use_real_hall = PCA_USE_REAL_HALL;
UINT real_speed = 0;
UINT real_speed_tmp = 0;
BYTE data int0_cnt = 0;
UINT data pwm16_int_cnt = 0;
UINT data pwm16_int_cnt_tmp = 50000;
UINT max_speed = MAXSPEED;
UINT min_speed = MINSPEED;
BYTE rpm_tolerance = RPM_TOLERANCE;
BYTE acceleration = ACCELERATION;
unsigned char motor_uvw_sequence;
UINT Over_Current_ADC = OVER_CURRENT_VALUE;
UINT ADC_A_result = 0;
UINT ADC_B_result = 0;
UINT ADC_C_result = 0;
UINT ADC_D_result = 0;
unsigned char Hal_sta = 0;
unsigned char Hal_sta_next = 0;
unsigned char Hal_sta_next2 = 0;
unsigned char t0_cnt = 0;
unsigned char t1_cnt = 0;
unsigned char count_mode_type = 0;
UINT over_current_cnt = 0;
unsigned char cnt_CurPro = 0;
unsigned char flag_run_dir = 0;		//0:CW, 1:CCW
unsigned char flag_enable_vr_speed = 0;	//0:off, 1:on
unsigned char slow_modify_speed = SLOW_MODIFY_SPEED;
unsigned char flag_debug_mode = 0;	//0:off, 1:on
unsigned char flag_test_hall_sequence_mode = 0;		//0:off, 1:on
unsigned char flag_phase_compensation_mode = 0;	//0:off, 1:on
unsigned char flag_mode_type = 0;			//0:open loop, 1:close loop, 2:current loop, 3:pwm loop
unsigned char flag_sensor_type = 0;			//0:hall sensor, 1: sensorless, 2: pca mode
unsigned char flag_speed_control_mode = 0;		//0:normal mode, 1:vr mode, 2:pwm input mode
unsigned char flag_enable_watchdog = 0;
unsigned char flag_over_current_protection = 0;	//0:off, 1:on
unsigned char flag_lock_rotor_protection = 0;	//0:off, 1:on
unsigned char flag_vdc_protection = 0;	//0:off, 1:on
unsigned char flag_hall_protection = 0;	//0:off, 1:on
unsigned char flag_update_status = 0;	//0:off, 1:on
unsigned char flag_hall_sequence = HALL_SEQ_000;
unsigned char PowerState = POWER_NORMAL;
BYTE VDC_result = 0;
UINT VDC_result_ADC = 0;
UINT Voltage_High_Off = 0;
UINT Voltage_High_On = 0;
UINT Voltage_Low_On = 0;
UINT Voltage_Low_Off = 0;
UINT Voltage_High_Off_ADC = 0;
UINT Voltage_High_On_ADC = 0;
UINT Voltage_Low_On_ADC = 0;
UINT Voltage_Low_Off_ADC = 0;
BYTE power_warning_count = ENABLE_POWER_WARNING_FAST;
unsigned char delay_time = 2;
unsigned char number_motor_pole_pair = 1;
UINT number_rpm_step_size = 0;
ULONG PWM16INT_cnt = 0;
ULONG pwm_cnt_start = 0;
ULONG pwm_cnt_diff = 0;
ULONG pwm_cnt_start2 = 0;
ULONG pwm_cnt_diff2 = 0;
unsigned char MtState = stop;
unsigned char MtState_temp = 0;
ULONG T4_count = 0;
ULONG T5_count = 0;
BYTE T3H_pwm_output = 0;
BYTE T3L_pwm_output = 0;
ULONG time_diff_hall = 0;
BYTE phase_angle = 60;
BYTE flag_enable_brake = 0;
BYTE flag_enable_speed_up_fast = 0;
BYTE flag_enable_speed_down_fast = 0;
UINT vr_max_speed = 0;
UINT vr_min_speed = 0;
UINT max_power = 0;
UINT ac_voltage = 0;
UINT data target_speed = TARGET_SPEED;
UINT data PWM_freq = PWM_PERIOD;
UINT data Hal_cnt = 0;
ULONG PWM_high_sum = 0;
ULONG PWM_low_sum = 0;
UINT tx2_buf[4] = 0;
ULONG StartTime = 0;
BYTE StartTimeT5T = 0;
BYTE StartTimeT5H = 0;
BYTE StartTimeT5L = 0;
ULONG StopTime = 0;
BYTE StopTimeT5T = 0;
BYTE StopTimeT5H = 0;
BYTE StopTimeT5L = 0;
ULONG ReachTime = 0;
BYTE ReachTimeT5T = 0;
BYTE ReachTimeT5H = 0;
BYTE ReachTimeT5L = 0;
UINT ERROR_number = 0;
BYTE motor_restart = 0;
BYTE vr_duty_start = 0;

//for MysonLink
bit flag_mysonlink_update_message = MYSONLINK_UPDATE_MESSAGE;
unsigned char svpwm_m = SVPWM_M_VALUE;	//SVPWM m value, 1~100
unsigned char flag_svpwm_mode = 0;		//0:off, 1:on
BYTE cmp_vth1 = 0;
BYTE cmp_vth2 = 0;
unsigned char sReceive_Tab[20] = 0;		//Slave IIC1(P21P20) Receive Tab
unsigned char sTransmit_Tab[20] = 0;
unsigned char I2C_buffer[20] = 0;
unsigned char I2C_buffer_length = 0;

//for sensorless
unsigned char Hal_sta_my = 5;
unsigned char motor_start = 1;
UINT data mt_drive_cnt = 0;
UINT mt_drive_free_cnt = 0;

//for calculate sensorless abnormal case
UINT mt_drive_time_new = 0;
UINT mt_drive_time_old = 0;
UINT mt_drive_time_diff_new = 0;
UINT mt_drive_time_diff_old = 0;
UINT too_fast = 0;
UINT too_slow = 0;
UINT abnormal = 0;

void Initial_IO(void)
{
	#ifdef CM2209B
	#ifndef STAR
	#ifndef STAR_V17
	//Setup CM2209B ITRIP signal from CS7211, use P0.0(PIN18)
	IOCFGP0_0=PinC_In;			MFCFGP0_0=_GPIOEN_;
	PIN_CONFIG_setup_dac(_P1_7);			//CM2209B Setup VREF signal to CS7211, use P1.7(PIN1)
	Setup_DAC_Voltage(CS7211_VREF_VOLTAGE);	//CM2209B Setup pin1_P1.7 as CS7211_VREF_VOLTAGE mV
	#endif
	#endif
	#endif
	#ifdef USE_HD_CONTROL
	PIN_CONFIG_setup_key(_P2_6);	//pin25, OPT_DEC
	PIN_CONFIG_setup_key(_P2_5);	//pin26, OPT_INC
	PIN_CONFIG_setup_key(_P2_4);	//pin27, OPT_BRAKE
	PIN_CONFIG_setup_key(_P2_3);	//pin28, OPT_RPM
	PIN_CONFIG_setup_key(_P2_2);	//pin29, OPT_POWER
	PIN_CONFIG_setup_key(_P2_1);	//pin30, OPT_AC
	PIN_CONFIG_setup_key(_P2_0);	//pin31, CW/CCW
	PIN_CONFIG_setup_key(_P1_7);	//pin1,  BRAKE
	#endif
}

void Initial_Comparator_VTH1(BYTE vth1)
{
	BYTE cmpcfgab_tmp = 0;
	//printString("Initial_Comparator by CMPVTH_VALUE, CMPVTH_VALUE = ");printd(vth1);printString("\n");
	CMP_EN = 0;

	#ifdef CM2209A
	IOCFGP2_7 = _ANEN_;						//Comparator A: ANEN
	MFCFGP2_7 = 0x80;						//enable Comparator A Input
	#elif defined CM2209B
	IOCFGP2_7 = _ANEN_;						//Comparator A: ANEN
	MFCFGP2_7 = 0x80;						//enable Comparator A Input
	#elif defined CM2209C
	IOCFGP2_7 = _ANEN_;						//Comparator A: ANEN
	MFCFGP2_7 = 0x80;						//enable Comparator A Input
	#elif defined CM2209D
	IOCFGP3_3 = _ANEN_;						//Comparator A: ANEN
	MFCFGP3_3 = 0x80;						//enable Comparator A Input
	#endif

	CMPST = 0x00;							//disable Comparator A/B/C/D Hysteresis
	DelayXms(4);							//delay

	cmpcfgab_tmp = CMPCFGAB;
	cmpcfgab_tmp &= 0x0F;	//get 0000BBBB
	cmpcfgab_tmp |= 0xE0;	//get 1110BBBB

	CMPVTH1 = vth1;
	CMPCFGAB = cmpcfgab_tmp;				//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
//	CMPCFGCD = B01100110;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
											//THSELx is 0, use internal(TH0) threshold; is 1 use external(TH1) threshold
											//POLx is 0,set default polarity; is 1,reverse the output polarity of the comparator

	CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
	DelayXms(1);							//delay as least 20us for the stabilization of comparator block, 258us
}

void Disable_Comparator(void)
{
	if((flag_over_current_protection&0x02)==2)
	{
		CMP_EN = 0;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
		//Disable comparator B/C/D
		CMPCFGAB = B11100110;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		CMPCFGCD = B01100110;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
		                 						//THSELx is 0, use internal(TH0) threshold; is 1 use external(TH1) threshold
												//POLx is 0,set default polarity; is 1,reverse the output polarity of the comparator
		CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
	}
	else
	{
		//Disable comparator A/B/C/D
		CMPCFGAB = B01100110;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		CMPCFGCD = B01100110;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
		                 						//THSELx is 0, use internal(TH0) threshold; is 1 use external(TH1) threshold
												//POLx is 0,set default polarity; is 1,reverse the output polarity of the comparator
		CMP_EN = 0;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
	}
}

void Initial_PAC_IO(void)
{
	#ifdef USE_NNMOS
	P1_0=0;					//close AP
	#ifdef STAR_V17
	P1_6=0;					//close BP
	#else
	P1_4=0;					//close BP
	#endif
	P3_1=0;					//close CP
	#elif defined USE_PNMOS
	P1_0=1;					//close AP
	P1_4=1;					//close BP
	P3_1=1;					//close CP
	#else
	printString("MOS Type Unknown\n");
	#endif

	#ifdef STAR
	P1_1=1;					//close AN
	P1_5=1;					//close BN
	P3_0=1;					//close CN
	#elif defined STAR_V17
	P1_1=1;					//close AN
	P1_7=1;					//close BN
	P3_0=1;					//close CN
	#else
	P1_1=0;					//close AN
	P1_5=0;					//close BN
	P3_0=0;					//close CN
	#endif

	MFCFGP1_0=0x01;IOCFGP1_0=PinC_InOutCMOS;	//Setup AP
	MFCFGP1_1=0x01;IOCFGP1_1=PinC_InOutCMOS;	//Setup AN
	#ifdef STAR_V17
	MFCFGP1_6=0x01;IOCFGP1_6=PinC_InOutCMOS;	//Setup BP
	MFCFGP1_7=0x01;IOCFGP1_7=PinC_InOutCMOS;	//Setup BN
	#else
	MFCFGP1_4=0x01;IOCFGP1_4=PinC_InOutCMOS;	//Setup BP
	MFCFGP1_5=0x01;IOCFGP1_5=PinC_InOutCMOS;	//Setup BN
	#endif
	MFCFGP3_1=0x01;IOCFGP3_1=PinC_InOutCMOS;	//Setup CP
	MFCFGP3_0=0x01;IOCFGP3_0=PinC_InOutCMOS;	//Setup CN
	/*
	IOCFGP1_1 = b00000110;										//PWMAN   output,open L,charge
	MFCFGP1_1 = b00100000;										//enable PWM16 Channel A negative output

	IOCFGP1_5 = b00000110;										//PWMBN   output
	MFCFGP1_5 = b00100000;										//enable PWM16 Channel B negative output

	IOCFGP3_0 = b00000110;										//PWMCN   output
	MFCFGP3_0 = b00100000;										//enable PWM16 Channel C negative output
	*/
}

void Initial_REGTRM(unsigned char regtrm)						//Initial REGTRM
{
	TB = 0xAA;
	TB = 0x55;
	REGTRM = regtrm;
   	TB = 0x00;
}

BYTE IFB_Read_1Byte(unsigned char ADD)	//IFB Read byte
{
	BYTE IFB_DAT;

	TB = 0xAA;
	TB = 0x55;
	FLSHADH = 0x00;
	FLSHADL = ADD;
	FLSHCMD = IFB_ByteRead;					//IFB read enable
	TB = 0x00;

	TB = 0xAA;
	TB = 0x55;
	IFB_DAT = FLSHDAT;
	TB = 0x00;

	return IFB_DAT;
}

void IFB_Read_256Byte(void)
{
	int i;
	unsigned char result;
	printString("\n");printString("Information Block (IFB) data:\n");
	for(i=0;i<128;i++)
	{
		result = IFB_Read_1Byte(i);
		#ifdef PARSE_IFB
		IFB_DATA[i] = result;
		#endif
		printx(result);
		if((i%16)==15)
			printString("\n");
		else if((i%16)==7)
		{
			printS(' ');printS(' ');
		}
		else
			printS(' ');
	}

	#ifdef PARSE_IFB
	printString("Device Name:        ");printS(IFB_DATA[2]);printS(IFB_DATA[3]);printS(IFB_DATA[4]);printS(IFB_DATA[5]);printS(IFB_DATA[6]);printS(IFB_DATA[7]);printS(IFB_DATA[8]);printString("\n");
	printString("Device Version:     ");printS(IFB_DATA[14]);printS(IFB_DATA[15]);printString("\n");
	printString("Die Record:         ");printS(IFB_DATA[0xa]);printS(IFB_DATA[0xb]);printS(IFB_DATA[0xc]);printS(IFB_DATA[0xd]);printS(IFB_DATA[0xe]);printS(IFB_DATA[0xf]);printString("\n");
	printString("Lot Number:         0x");printx(IFB_DATA[0x10]);printx(IFB_DATA[0x11]);printx(IFB_DATA[0x12]);printx(IFB_DATA[0x13]);printx(IFB_DATA[0x14]);printx(IFB_DATA[0x15]);printx(IFB_DATA[0x16]);printx(IFB_DATA[0x17]);printString("\n");
	printString("FT Date Code:       0x");printx(IFB_DATA[0x18]);printx(IFB_DATA[0x19]);printx(IFB_DATA[0x1a]);printx(IFB_DATA[0x1b]);printx(IFB_DATA[0x1c]);printx(IFB_DATA[0x1d]);printx(IFB_DATA[0x1e]);printx(IFB_DATA[0x1f]);printString("\n");
	printString("REGTRM value:       0x");printx(IFB_DATA[0x20]);printString("\n");
	printString("IOSC ITRM value:    0x");printx(IFB_DATA[0x21]);printString("\n");
	printString("IOSC VTRM value:    0x");printx(IFB_DATA[0x22]);printString("\n");
	printString("LVDTHD 4.0V value:  0x");printx(IFB_DATA[0x23]);printString("\n");
	printString("LVDTHD 3.0V value:  0x");printx(IFB_DATA[0x24]);printString("\n");
	printString("BootCode Wait Time: 0x");printx(IFB_DATA[0x40]);printString("\n");
	#endif
}

void Initial_Comparator_Sensorless(void)
{
	CMP_EN = 0;								//Analog Comparator Interrupt and CAN Interrupt Enable bit

	IOCFGP2_3 = _ANEN_;	  					//Comparator TH:ANEN
	MFCFGP2_3 = 0x80;						//enable Comparator TH Input

	IOCFGP2_4 = _ANEN_; 					//Comparator D:ANEN
	MFCFGP2_4 = 0x80;						//enable Comparator D Input

	IOCFGP2_5 = _ANEN_; 					//Comparator C:ANEN
	MFCFGP2_5 = 0x80;						//enable Comparator C Input

	IOCFGP2_6 = _ANEN_; 					//Comparator B:ANEN
	MFCFGP2_6 = 0x80;						//enable Comparator B Input

	CMPST = 0x00;							//disable Comparator A/B/C/D Hysteresis
	DelayXms(4);							//delay

//	CMPVTH0 = 0x80;							//0.9V for Comparator B/C/D
//     CMPVTH1 = 0xff;							//1.8V   0.63A, 0Xb5 = 0.45A
//	CMPVTH1 = IOCFGP2_3;			             // rup


	if((flag_over_current_protection&0x02)==2)
	{
		CMPCFGAB = B11100000;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		CMPCFGCD = B00000000;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
		                 						//THSELx is 0, use internal(TH0) threshold; is 1 use external(TH1) threshold
												//POLx is 0,set default polarity; is 1,reverse the output polarity of the comparator
	}
	else
	{
		CMPCFGAB = B00000000;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
		CMPCFGCD = B00000000;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
		                 						//THSELx is 0, use internal(TH0) threshold; is 1 use external(TH1) threshold
												//POLx is 0,set default polarity; is 1,reverse the output polarity of the comparator
	}

	CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
	DelayXms(10);							// delay as least 20us for the stabilization of comparator block, 258us
}

void check_comparator_edge(void)	// 4.76us
{
	BYTE cmpcfgab_value_rising = 0;
	BYTE cmpcfgab_value_falling = 0;
	if((flag_over_current_protection&0x02) == 2)
	{
		cmpcfgab_value_rising  = B11101110;
		cmpcfgab_value_falling = B11101111;
	}
	else
	{
		cmpcfgab_value_rising  = B01101110;
		cmpcfgab_value_falling = B01101111;
	}

	if(flag_run_dir == CW)
	{
		if((Hal_sta_my == 1) || (Hal_sta_my == 2) || (Hal_sta_my == 4))
		{
			CMPCFGAB = cmpcfgab_value_rising;
			CHECK_RISING_EDGE_CD;
		}
		else
		{
			CMPCFGAB = B01101111;
			CHECK_FALLING_EDGE_CD;
		}
	}
	else		//CCW
	{
		if((Hal_sta_my == 1) || (Hal_sta_my == 2) || (Hal_sta_my == 4))
		{
			CMPCFGAB = B01101111;
			CHECK_FALLING_EDGE_CD;
		}
		else
		{
			CMPCFGAB = cmpcfgab_value_rising;
			CHECK_RISING_EDGE_CD;
		}
	}
}
