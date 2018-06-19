#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"

#ifdef USE_COMPACT
#include "CS8963_BLDC.h"
#include "CS8963_MysonLink.h"
#include "CS8963_Compact_Function.h"

extern unsigned int real_speed;
extern unsigned char PWM_duty;
extern unsigned char PWM_start_duty;
extern unsigned char flag_speed_control_mode;
extern char MtState;
extern unsigned char Hal_sta;
extern int PWM_period;
extern unsigned char number_motor_pole_pair;
enum _Direction
{
	CW,
	CCW,
};

BYTE check_speed = 0;
BYTE phase_angle = PHASE_ANGLE_CW;
BYTE ERROR_number = 0;
unsigned char flag_phase_compensation_mode = 0;	//0:off, 1:on
unsigned char flag_enable_vr_speed;	//0:off, 1:on
unsigned char flag_run_dir = 0;		//0:clockwise, CW 1:counterclockwise, CCW
unsigned char flag_mode_type = 0;			//0:open loop, 1:close loop, 2:current loop, 3:pwm loop
unsigned int xdata target_speed = TARGET_SPEED;
unsigned int xdata PWM_freq = PWM_PERIOD;
unsigned int max_speed = MAXSPEED;
unsigned int min_speed = MINSPEED;
BYTE rpm_tolerance = RPM_TOLERANCE;
BYTE acceleration = ACCELERATION;
BYTE PWM_duty_old = 0;
#else
#include "CS8963_Function.h"
#include "CS8963_Motor_Function.h"
#include "CS8963_MysonLink.h"
#include "CS8963_UART.h"
#include "CS8963_Config.h"
#include "CS8963_ADC.h"
#include "CS8963_PWM.h"
#include "CS8963_PCA.h"
#include "CS8963_Setup.h"
#include "CS8963_Timer.h"
#include "CS8963_Initial.h"
#include "CS8963_Sensorless.h"
#endif

#define CHECK_SEND_GOT_CMD_LENGTH 10
BYTE send_got_command_number = 0;
BYTE send_got_command_buffer[3][CHECK_SEND_GOT_CMD_LENGTH];

extern unsigned char motor_start;
extern unsigned int data mt_drive_cnt;

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function MysonLink
 * Filename: CS8963_MysonLink.C
 * Author  :
 * Date    : 2015/10/14
 **********************************************************/

#ifdef USE_MYSONLINK

BYTE gui_cmd[UART_BUF_LENGTH] = 0;
BYTE gui_cmd_index = 0;
BYTE timer3_check_cnt = 0;
BYTE cnt1 = 0;
BYTE hall = 0;
BYTE flag_getting_data = 0;

#ifdef USE_COMPACT
//for sensorless
#define START_DUTY			10
#define DELAY				200	//250
#define ROUND				20
BYTE Hal_sta_my = 0;
#endif

void Timer345_ISR(void) interrupt 14
{
	unsigned char T3CON_tmp;
	if((T34CON & 0x08)==0x08)
	{
		//printString("T3 ");
		//T34CON &= 0xf7; 					//time3 (16bit timer mode)
		T3CON_tmp = T34CON;
		T3CON_tmp &= 0xf7;
		T34CON = T3CON_tmp;

		timer3_check_cnt++;		//  1/16e6 *65536 = 4.12ms
		if((timer3_check_cnt % 50) == 0)	//every 4.12*50 = 0.2s
		{
			if(send_got_command_number >= 1)
				Check_Send_Got_Cmd();
			else if(cnt1 == 0)
			{
				Send_Motor_Parameter_Cmd(_ALIVE, flag_speed_control_mode, 1 - MtState);
			}
			else if(cnt1 == 1)
			{
				Send_Motor_Parameter_Cmd(_REAL_SPEED, (real_speed_tmp>>8)&0xff, real_speed_tmp&0xff);
			}
			else if(cnt1 == 2)
			{
				if(MtState == stop)
				{
					if(flag_sensor_type == PCA_MODE)
						Send_Motor_Parameter_Cmd(_PCA_DUTY, _NONE, 0);
					else
						Send_Motor_Parameter_Cmd(_DUTY, _NONE, 0);
				}
				else
				{
					if(flag_sensor_type == PCA_MODE)
						Send_Motor_Parameter_Cmd(_PCA_DUTY, _NONE, PCA_duty);
					else
						Send_Motor_Parameter_Cmd(_DUTY, _NONE, PWM_duty);
				}
			}
			#ifndef USE_COMPACT
			else if(cnt1 == 3)
			{
				if(flag_send_hall_status ==1)
				{
					hall = get_current_hall_status();
					Send_Motor_Parameter_Cmd(_HALL, _NONE, hall);
				}
			}
			else if(cnt1 == 4)
			{
				Initial_ADC(PIN_VRin);								//Initial ADC A channel for sample current, pin13
				Get_ADC_Result(PIN_VRin);
				Disable_ADC(PIN_VRin);
				Send_Motor_Parameter_Cmd(_VR, ADCAH, ADCAL);
			}
			else if(cnt1 == 5)
			{
				Initial_ADC(SAMPLE_CURRENT_ADC);					//Initial ADC A channel for sample current, pin18
				Get_ADC_Result(SAMPLE_CURRENT_ADC);
				Disable_ADC(SAMPLE_CURRENT_ADC);
				Send_Motor_Parameter_Cmd(_IS, ADCAH, ADCAL);
			}
			#endif
			else if(cnt1 == 6)
			{
				Send_System_Control_Cmd();
			}
			cnt1++;
			if(cnt1 > 6)
				cnt1 = 0;
		}
		T3H = 0x00;							//Timer 3 count start point
		T3L = 0x00;	
	}
}

UINT CalcCheckSum(UINT *pData, UINT len)
{
    unsigned char i = 0,sum = 0;
    for (; i < len; i++)
    {
        sum += (unsigned char) pData[i];
    }
    sum = (sum^0xFF) + 1;
    return (sum&0xFF);
}

void Check_Send_Got_Cmd()
{
	BYTE tmp1 = 0;
	BYTE tmp2 = 0;
	BYTE tmp3 = 0;
	if(send_got_command_number >= 1)
	{
		tmp1 = send_got_command_buffer[0][send_got_command_number];
		tmp2 = send_got_command_buffer[1][send_got_command_number];
		tmp3 = send_got_command_buffer[2][send_got_command_number];
		send_got_command_number--;
		Send_Got_Cmd0(tmp1, tmp2, tmp3);
	}
}

void Send_Got_Cmd(BYTE cmd1, BYTE cmd2, BYTE cmd3)
{
	send_got_command_buffer[0][send_got_command_number] = cmd1;
	send_got_command_buffer[1][send_got_command_number] = cmd2;
	send_got_command_buffer[2][send_got_command_number] = cmd3;
	send_got_command_number++;
	if(send_got_command_number >= CHECK_SEND_GOT_CMD_LENGTH)
		send_got_command_number = 1;
}

void Send_Got_Cmd0(BYTE cmd1, BYTE cmd2, BYTE cmd3)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	UartTxBuf[0] = 0xDD;
	UartTxBuf[1] = cmd1;
	UartTxBuf[2] = cmd2;
	UartTxBuf[3] = cmd3;
	UartTxBuf[4] = CalcCheckSum(UartTxBuf, 4);

	for(i=0;i<UART_BUF_LENGTH;i++) SBUF2 = UartTxBuf[i];
}

/*
void Send_Got_Cmd(BYTE cmd1, BYTE cmd2, BYTE cmd3)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	UartTxBuf[0] = 0xDD;
	UartTxBuf[1] = cmd1;
	UartTxBuf[2] = cmd2;
	UartTxBuf[3] = cmd3;
	UartTxBuf[4] = CalcCheckSum(UartTxBuf, 4);

	for(i=0;i<UART_BUF_LENGTH;i++) SBUF2 = UartTxBuf[i];
}
*/

void Send_Motor_Error_Cmd(UINT error_number)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	UartTxBuf[0] = 0xEE;
	UartTxBuf[1] = 0;
	UartTxBuf[2] = (error_number>>8)&0xff;
	UartTxBuf[3] = error_number&0xff;
	UartTxBuf[4] = CalcCheckSum(UartTxBuf, 4);

	for(i=0;i<UART_BUF_LENGTH;i++) SBUF2 = UartTxBuf[i];
}

void Send_Motor_Parameter_Cmd(BYTE XX, BYTE YY, BYTE ZZ)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	UartTxBuf[0] = 0xC1;
	UartTxBuf[1] = XX;
	UartTxBuf[2] = YY;
	UartTxBuf[3] = ZZ;
	UartTxBuf[4] = CalcCheckSum(UartTxBuf, 4);

	for(i=0;i<UART_BUF_LENGTH;i++) SBUF2 = UartTxBuf[i];
}

void Send_System_Status_Cmd(BYTE XX)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	UartTxBuf[0] = 0xC2;
	UartTxBuf[1] = XX;
	UartTxBuf[2] = 0;
	UartTxBuf[3] = 0;
	UartTxBuf[4] = CalcCheckSum(UartTxBuf, 4);

	for(i=0;i<UART_BUF_LENGTH;i++) SBUF2 = UartTxBuf[i];
}

void Send_System_Control_Cmd()
{
	BYTE yy = 0;
	BYTE zz = 0;
	yy |= flag_run_dir<<7;
	yy |= flag_mode_type<<6;
	yy |= flag_sensor_type<<4;
	yy |= PCA_use_real_hall<<0;
	#ifdef CM2209A
	zz = 1;
	#elif defined CM2209B
	zz = 2;
	#elif defined CM2209C
	zz = 3;
	#elif defined CM2209D
	zz = 4;
	#else
	zz = 0;
	#endif
	Send_Motor_Parameter_Cmd(_CONTROL, yy, zz);
}

void EUART2(void) interrupt 6
{
	unsigned char SBUF2_temp;
	UINT UartRxBuf[UART_BUF_LENGTH];
	UINT checksum;
	BYTE gui_value = 0;
	BYTE control_data1 = 0;
	BYTE control_data2 = 0;
	BYTE control_data3 = 0;
	BYTE board_number = 0;
	UINT pwmsetup = 0;
	BYTE ask_cmd = 0;
	BYTE continus = 0;
	BYTE hall_status = 0;
	BYTE xx = 0;
	BYTE yy = 0;
	BYTE zz = 0;

	if(EUART2_TIF)							//transmit interrupt
	{
		EUART2_TIF_CLR;
	}

	if(EUART2_RIF)							//receive interrupt
	{
		EUART2_RIF_CLR;
		SBUF2_temp = SBUF2;					//EUART Receive Data

		if((SBUF2_temp >= 0xD1)&&(SBUF2_temp <= 0xDB))
		{
			if((gui_cmd_index != 1) && (flag_getting_data = 0))
			{
				gui_cmd_index = 0;
				flag_getting_data = 1;
			}
		}

		gui_cmd[gui_cmd_index] = SBUF2_temp;

		/*
		if(gui_cmd_index == 0)
		{
			if((SBUF2_temp >= 0xD1)&&(SBUF2_temp <= 0xD9))	//Check Header
				gui_cmd_index++;
			else
				gui_cmd_index = 0;
		}
		else
			gui_cmd_index++;
		*/
		gui_cmd_index++;

		if (gui_cmd_index == UART_BUF_LENGTH)
		{
			gui_cmd_index = 0;
			UartRxBuf[0] = gui_cmd[0];
			UartRxBuf[1] = gui_cmd[1];
			UartRxBuf[2] = gui_cmd[2];
			UartRxBuf[3] = gui_cmd[3];
			checksum = CalcCheckSum(UartRxBuf, 4);
			xx = gui_cmd[1];
			yy = gui_cmd[2];
			zz = gui_cmd[3];
			flag_getting_data = 0;
			if(gui_cmd[4] != checksum)
			{
				printString("[CS8963]: UART Receive data NG, data: 0x ");
				printx(gui_cmd[0]);printS(' ');
				printx(gui_cmd[1]);printS(' ');
				printx(gui_cmd[2]);printS(' ');
				printx(gui_cmd[3]);printS(' ');
				printx(gui_cmd[4]);
				printString(", checksum = 0x ");
				printx(checksum);
				printString(", Abort...\n");
				return;
			}
			else
				Send_Got_Cmd0(gui_cmd[1], gui_cmd[2], gui_cmd[3]);

			if(gui_cmd[0] == 0xD1)
			{
				if(MtState == stop)		//only available when stop
				{
					control_data1 = gui_cmd[1];
					control_data2 = gui_cmd[2];
					control_data3 = gui_cmd[3];
					board_number = control_data3;
					//printString("[CS8963]: Control data : 0x ");printx(control_data1);printS(' ');
					//printx(control_data2);printS(' ');printx(control_data3);printString("\n");

					if(control_data1 == 0xff)
					{
						PINT0EN = 0;
						PWM16_disable();
						MtState = stop;
						//motor_start = 1;
						//timer0_cnt = 0;
						//target_speed = 0;
						real_speed = 0;
						//hall_fail_cnt = 0;
						check_speed = 0;
						//svpwm_m = SVPWM_M_VALUE;
						//PWM_duty = svpwm_m;
						//svpwm_m_temp = SVPWM_M_VALUE;
						printString("[CS8963]: Got command: Reset\n");
						Reset_system();
						return;
					}
					if(((control_data2>>7)&0x01) == 0)
					{
						SETUP_direction(CW);
					}
					else
					{
						SETUP_direction(CCW);
					}
					if(((control_data2>>6)&0x01) == 0)
					{
						SETUP_mode_type(OPEN_LOOP);
					}
					else
					{
						SETUP_mode_type(CLOSE_LOOP);
					}
					if(((control_data2>>4)&0x03) == 0)
					{
						SETUP_sensor_mode(HALL_SENSOR_MODE);
					}
					else if(((control_data2>>4)&0x03) == 0x01)
					{
						SETUP_sensor_mode(SENSORLESS_MODE);
					}
					else if(((control_data2>>4)&0x03) == 0x02)
					{
						SETUP_sensor_mode(PCA_MODE);
						PCA_Mode_Setup();
					}
					else if(((control_data2>>4)&0x03) == 0x03)
					{
						//reserved
						//Timer1_Close();
					}
					/*
					if(((control_data2>>2)&0x03) == 0)
					{
						printString("PWM\n");
					}
					else if(((control_data2>>2)&0x03) == 1)
					{
						printString("KPWM\n");
					}
					else if(((control_data2>>2)&0x03) == 2)
					{
						printString("SVPWM\n");
					}
					else
					{
						printString("Unknown PWM mode\n");
					}
					if(((control_data2>>1)&0x01) == 0)
					{
						printString("NNMOS\n");
					}
					else
					{
						printString("PNMOS\n");
					}
					switch(board_number)
					{
						case 1:		printString("CM2209A\n");	break;
						case 2:		printString("CM2209B\n");	break;
						case 3:		printString("CM2209C\n");	break;
						case 4:		printString("CM2209D\n");	break;
						default:	printString("Unknown\n");	break;
					}
					*/
					if(((control_data2>>0)&0x01) == 1)	//use real hall
					{
						SETUP_sensor_mode(PCA_MODE);
						PCA_Mode_Setup();
						PCA_use_real_hall = 1;
						PINT0EN = 1;
						//Timer1_Close();
						printString("Use Real Hall\n");
					}
					else
					{
						SETUP_sensor_mode(PCA_MODE);
						PCA_Mode_Setup();
						PCA_use_real_hall = 0;
						//TH1 = ac_motor_TH1;
						//TL1 = ac_motor_TL1;
						//Initial_Timer1();		// PCA_MODE w/ sensorless hall
						PINT0EN = 0;
						//Timer1_Close();
						printString("Use Sensorless Hall\n");

						Disable_Comparator();
						Initial_Comparator_Sensorless();
					}
					Send_System_Control_Cmd();
				}
				else
				{
					//printString("[CS8963]: Not acceptable when running.\n");
				}
			}
			else if(gui_cmd[0] == 0xD2)
			{
				if(gui_cmd[1] == _TARGET_SPEED)	//target speed
				{
					target_speed = gui_cmd[2]<<8 | gui_cmd[3];
					printString("[CS8963]: got target speed = ");printd(target_speed);printString("\n");
				}
				else if(gui_cmd[1] == _MAX_SPEED)	//max speed
				{
					max_speed = gui_cmd[2]<<8 | gui_cmd[3];
					//printString("[CS8963]: got max speed = ");printd(max_speed);printString("\n");
				}
				else if(gui_cmd[1] == _MIN_SPEED)	//min speed
				{
					min_speed = gui_cmd[2]<<8 | gui_cmd[3];
					//printString("[CS8963]: got min speed = ");printd(min_speed);printString("\n");
				}
				else if(gui_cmd[1] == _DUTY)	//duty
				{
					PWM_duty = gui_cmd[3];
					//printString("[CS8963]: got duty = ");printd(PWM_duty);printString("\n");
					PWM16_Modify(PWM_period, PWM_duty);
				}
				else if(gui_cmd[1] == _TOLERANCE)	//tolerance
				{
					rpm_tolerance = gui_cmd[3];
					printString("[CS8963]: got rpm_tolerance = ");printd(rpm_tolerance);printString("\n");
				}
				else if(gui_cmd[1] == _ACCELERATION)	//acceleration
				{
					acceleration = gui_cmd[3];
					printString("[CS8963]: got acceleration = ");printd(acceleration);printString("\n");
				}
				else if(gui_cmd[1] == _POLE_PAIR)	//number_motor_pole_pair
				{
					number_motor_pole_pair = gui_cmd[3];
					//printString("[CS8963]: got number_motor_pole_pair = ");printd(number_motor_pole_pair);printString("\n");
				}
				else if(gui_cmd[1] == _PWM_FREQUENCY)	//PWM frequency in kHz
				{
					pwmsetup = gui_cmd[2]<<8 | gui_cmd[3];
					//pwmfreq = 8000 / pwmsetup;
					//printString("[CS8963]: got pwm_frequency = ");printd(pwmfreq);printString(" kHz\n");
					PWM_period = pwmsetup;
					//PWM16_Modify(PWM_period, PWM_duty);
					Initial_PWM16(PWM_period, PWM_duty);
				}
				else if(gui_cmd[1] == _PROTECTION)	//protection
				{
					/* old
					#ifndef USE_COMPACT
					printString("[CS8963]: Get Protection Command = ");printx(zz);printString("\n");
					if(((zz>>0)&0x01)==1)
					{
						SETUP_enable_over_current_protection(1);
						//printString("[CS8963]: Enable over current protection. VTH1 = ");printd(cmp_vth1);printString("\n");
						//Initial_Comparator_VTH(cmp_vth1);						//Initial Comparator with large VTH when start
						printString("[CS8963]: Enable Over Current Protection A.\n");
					}
					else
					{
						SETUP_enable_over_current_protection(0);
						printString("[CS8963]: Disable Over Current Protection A.\n");

						//Disable_Comparator();
					}
					if(((zz>>1)&0x01)==1)
					{
						printString("[CS8963]: Enable Over Current Protection C.\n");
					}
					else
					{
						printString("[CS8963]: Disable Over Current Protection C.\n");
					}
	
					if(((zz>>2)&0x01)==1)
					{
						printString("[CS8963]: Enable Over Current Protection X.\n");
					}
					else
					{
						printString("[CS8963]: Disable Over Current Protection X.\n");
					}

					if(((zz>>3)&0x01)==1)
					{
						SETUP_enable_lock_rotor_protection(1);
						printString("[CS8963]: Enable Lock-Rotor Protection.\n");
					}
					else
					{
						SETUP_enable_lock_rotor_protection(0);
						printString("[CS8963]: Disable Lock-Rotor Protection.\n");
					}

					if(((zz>>4)&0x01)==1)
					{
						SETUP_enable_hall_protection(1);
						printString("[CS8963]: Enable Hall sequence protection.\n");
					}
					else
					{
						SETUP_enable_hall_protection(0);
						printString("[CS8963]: Disable Hall sequence protection.\n");
					}

					if(((zz>>5)&0x01)==1)
					{
						SETUP_enable_vdc_protection(1);
						printString("[CS8963]: Enable VDC protection.\n");
					}
					else
					{
						SETUP_enable_vdc_protection(0);
						printString("[CS8963]: Disable VDC protection.\n");
					}

					if(((zz>>6)&0x01)==1)
					{
						printString("[CS8963]: Enable WatchDog.\n");
					}
					else
					{
						printString("[CS8963]: Disable WatchDog.\n");
					}
					#endif
					*/
				}
				else if(gui_cmd[1] == _DIRECTION)	//direction
				{
					#ifndef USE_COMPACT
					if(MtState == stop)
						SETUP_direction(zz);
					#endif
					/*
					if(zz == 0)
						printString("CW\n");
					else
						printString("CCW\n");
					*/
				}
				else if(gui_cmd[1] == _PHASE_COMP)	//phase compensation
				{
					if(yy == _START)
					{
						phase_angle = zz;
						printString("Phase Compensation mode ON, phase_angle = ");printd(phase_angle);printString("\n");
						flag_phase_compensation_mode = 1;
					}
					else
					{
						printString("Phase Compensation mode OFF\n");
						flag_phase_compensation_mode = 0;
					}
				}
				else if(gui_cmd[1] == _START_DUTY)	//start duty
				{
					PWM_start_duty = gui_cmd[3];
					//printString("[CS8963]: got pwm_start_duty = ");printd(PWM_start_duty);printString("\n");
				}
				else if(gui_cmd[1] == _PCA_DUTY)	//PCA duty
				{
					PCA_duty = gui_cmd[3];
					//printString("[CS8963]: got PCA duty = ");printd(PCA_duty);printString("\n");
					PCA8_Modify(PCA_duty);
				}
				else if(gui_cmd[1] == _GPIO)		//GPIO
				{
					if(gui_cmd[2] == _P1_3)
						P1_3 = gui_cmd[3];
					else if(gui_cmd[2] == _P1_2)
						P1_2 = gui_cmd[3];
				}
				else if(gui_cmd[1] == _TIMER1)	//timer 1 start point
				{
					//ac_motor_TH1 = gui_cmd[2];
					//ac_motor_TL1 = gui_cmd[3];
					//printString(", T: 0x");printx(gui_cmd[2]);printS(' ');printx(gui_cmd[3]);printS('=');printd(gui_cmd[2] << 8 | gui_cmd[3]);
					//printString("\n");
				}
			}
			else if(gui_cmd[0] == 0xD3)
			{
				if(gui_cmd[3] == 0xAA)	//speed up
				{
					if(flag_sensor_type == PCA_MODE)
					{
						PCA_duty_old  = PCA_duty;
						if(PCA_duty >= 255)
							PCA_duty = 255;
						else
							PCA_duty += 1;
						//printString("PCA Duty +1, Duty:");printd(PCA_duty);printString("\n");
						PCA8_Modify(PCA_duty);
					}
					else
					{
						PWM_duty_old  = PWM_duty;
						PWM_duty += 1;
						if(PWM_duty > 100)
							PWM_duty = 100;
						//printString("Duty +1, Duty:");printd(PWM_duty);printString("\n");
						PWM16_Modify(PWM_period, PWM_duty);
					}
				}
				else if(gui_cmd[3] == 0x55)	//speed down
				{
					if(flag_sensor_type == PCA_MODE)
					{
						PCA_duty_old  = PCA_duty;
						if(PCA_duty <= 0)
							PCA_duty = 0;
						else
							PCA_duty -= 1;
						//printString("PCA Duty -1, Duty:");printd(PCA_duty);printString("\n");
						PCA8_Modify(PCA_duty);
					}
					else
					{
						PWM_duty_old  = PWM_duty;
						if(PWM_duty == 0)
							PWM_duty = 0;
						else
							PWM_duty -= 1;
						//printString("Duty -1, Duty:");printd(PWM_duty);printString("\n");
						PWM16_Modify(PWM_period, PWM_duty);
					}
				}
				else if((gui_cmd[1]&0x01) == 0)
					Stop_Motor();
				else if((gui_cmd[1]&0x01) == 1)
				{
					if(((gui_cmd[2])==0)&&((gui_cmd[3])==0))
					{
						if(ERROR_number == _ERROR_NONE)		//no error
						{
							flag_enable_vr_speed = 0;
							if(MtState == stop)
							{
								printString("MysonLink Start\n");
								SETUP_PWM_duty(PWM_start_duty);
								SETUP_PWM_duty_target(PWM_start_duty);
								SETUP_PWM_duty_new(PWM_start_duty);
								Start_Motor();
							}
						}
						else
						{
							printString("[CS8963]: Error Status = ");printd(ERROR_number);printString(", Abort...\n");
							print_error_message(ERROR_number);
						}
					}
					else if(((gui_cmd[2])==1)&&((gui_cmd[3])==0))	//speed up
					{
						PWM_duty_old  = PWM_duty;
						PWM_duty += 1;
						if(PWM_duty > 100)
							PWM_duty = 100;
						printString("Duty +1, Duty:");printd(PWM_duty);printString("\n");
						PWM16_Modify(PWM_period, PWM_duty);
					}
					else if(((gui_cmd[2])==0)&&((gui_cmd[3])==1))	//speed down
					{
						PWM_duty_old  = PWM_duty;
						if(PWM_duty == 0)
							PWM_duty = 0;
						else
							PWM_duty -= 1;
						printString("Duty -1, Duty:");printd(PWM_duty);printString("\n");
						PWM16_Modify(PWM_period, PWM_duty);
					}
				}
			}
			else if(gui_cmd[0] == 0xD4)
			{

				ask_cmd = gui_cmd[1]&0x3f;
				continus = (gui_cmd[1]>>6)&0x3;
				/*
				printString("[CS8963]: Got ask command, data: 0x ");printx(gui_cmd[1]);
				printString(", cmd = ");printd(ask_cmd);
				if(continus == 0)
					printString(", STOP\n");
				else if(continus == 1)
					printString(", Once\n");
				else if(continus == 2)
					printString(", Continous\n");
				else
					printString("Unknown\n");
					*/
				
				if(ask_cmd == _CONTROL)
				{
					yy = 0;
					zz = 0;
					yy |= flag_run_dir<<7;
					yy |= flag_mode_type<<6;
					yy |= flag_sensor_type<<4;
					#ifdef CM2209A
					zz = 1;
					#elif defined CM2209B
					zz = 2;
					#elif defined CM2209C
					zz = 3;
					#elif defined CM2209D
					zz = 4;
					#else
					zz = 0;
					#endif
					Send_Motor_Parameter_Cmd(_CONTROL, yy, zz);
				}
				else if(ask_cmd == _DIRECTION)
				{
					Send_Motor_Parameter_Cmd(_DIRECTION, _NONE, flag_run_dir);
				}
				else if(ask_cmd == _REAL_SPEED)
				{
					//printString("real speed\n");
					Send_Motor_Parameter_Cmd(_REAL_SPEED, (real_speed>>8)&0xff, real_speed&0xff);
				}
				else if(ask_cmd == _TARGET_SPEED)
				{
					//printString("target speed\n");
					Send_Motor_Parameter_Cmd(_TARGET_SPEED, (target_speed>>8)&0xff, target_speed&0xff);
				}
				else if(ask_cmd == _MAX_SPEED)
				{
					//printString("max speed\n");
					Send_Motor_Parameter_Cmd(_MAX_SPEED, (max_speed>>8)&0xff, max_speed&0xff);
				}
				else if(ask_cmd == _MIN_SPEED)
				{
					//printString("min speed\n");
					Send_Motor_Parameter_Cmd(_MIN_SPEED, (min_speed>>8)&0xff, min_speed&0xff);
				}
				else if(ask_cmd == _DUTY)
				{
					Send_Motor_Parameter_Cmd(_DUTY, 0, PWM_duty);
				}
				else if(ask_cmd == _CONTROL)
				{
					printString("control data\n");
				}
				else if(ask_cmd == _TOLERANCE)
				{
					//printString("tolerance\n");
					Send_Motor_Parameter_Cmd(_TOLERANCE, 0, rpm_tolerance);
				}
				else if(ask_cmd == _ACCELERATION)
				{
					//printString("acceleration\n");
					Send_Motor_Parameter_Cmd(_ACCELERATION, 0, acceleration);
				}
				else if(ask_cmd == _HALL)	//hall status
				{
					#ifndef USE_COMPACT
					if(continus == _STOP)	//stop
					{
						flag_send_hall_status = 0;
					}
					else if(continus == _ONCE)	//once
					{
						hall_status = get_current_hall_status();
						Send_Motor_Parameter_Cmd(_HALL, 0, hall_status);
					}
					else if(continus == _CONTINUOUS)	//continous
					{
						flag_send_hall_status = 1;
					}
					#endif
				}
				else if(ask_cmd == _PROTECTION)
				{
					printString("protection\n");
				}
				else if(ask_cmd == _RUN_STATUS)
				{
					printString("run status\n");
				}
				else if(ask_cmd == _ERROR)
				{
					printString("error status\n");
				}
				else if(ask_cmd == _PWM_FREQUENCY)
				{
					//printString("pwm frequency\n");
					//printString("pwm frequency period = ");printd(PWM_period);printString("\n");
					Send_Motor_Parameter_Cmd(_PWM_FREQUENCY, (PWM_period>>8)&0xff, PWM_period&0xff);
				}
				else if(ask_cmd == _POLE_PAIR)
				{
					//printString("pole pair\n");
					Send_Motor_Parameter_Cmd(_POLE_PAIR, 0, number_motor_pole_pair);
				}
				else if(ask_cmd == _START_DUTY)
				{
					//printString("start duty \n");
					Send_Motor_Parameter_Cmd(_START_DUTY, 0, PWM_start_duty);
				}
				else if(ask_cmd == 21)
				{
					printString("ADC1 VR\n");
				}
				else if(ask_cmd == 22)
				{
					printString("ADC2 VDC\n");
				}
				else if(ask_cmd == 23)
				{
					printString("ADC3\n");
				}
				else if(ask_cmd == 24)
				{
					printString("ADC4\n");
				}
				else if(ask_cmd == 25)
				{
					printString("CMPVTH0\n");
				}
				else if(ask_cmd == 26)
				{
					printString("CMPVTH1\n");
				}
				else
				{
					printString("unknown item = ");printd(ask_cmd);printString("\n");
				}
			}
			/*
			else if(gui_cmd[0] == 0xD4)
			{
				//printString("Got value = ");printd(gui_cmd[1]);printString("\n");
				if(gui_cmd[1]==0xff)
				{
					printString("[CS8963]: SVPWM TEST MODE, AUTO Mode.\n");
					svpwm_m = SVPWM_M_VALUE;
					PWM_duty = svpwm_m;
					for(index_angle=0;index_angle<360;index_angle+=10)
					{
						printString("m:");printd(svpwm_m);printString(", A:");printd(index_angle);printS(' ');

						SVPWM_Setup_Duty(index_angle);

						MFCFGP1_0 = Hopen;  MFCFGP1_1 = Lopen;	//A+
						MFCFGP1_4 = Hopen;  MFCFGP1_5 = Lopen;	//B+
						MFCFGP3_1 = Hopen;  MFCFGP3_0 = Lopen;	//C+
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						PWM16_disable();
						printString(" H:");get_current_hall_state();printString("\n");
						DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					}
				}
				else if(((gui_cmd[1]>>6)&0x01)==1)
				{
					svpwm_m = SVPWM_M_VALUE;
					PWM_duty = svpwm_m;
					printString("[CS8963]: SVPWM TEST MODE SVPWM m:");printd(svpwm_m);printString(", A:");printd((gui_cmd[1]&0x3f)*10);
					printString("   START\n");
					index_angle = gui_cmd[1]&0x3f;
					SVPWM_Setup_Duty(index_angle*10);
					MFCFGP1_0 = Hopen;  MFCFGP1_1 = Lopen;	//A+
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Lopen;	//B+
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Lopen;	//C+
				}
				else
				{
					svpwm_m = SVPWM_M_VALUE;
					PWM_duty = svpwm_m;
					printString("[CS8963]: SVPWM TEST MODE SVPWM m:");printd(svpwm_m);printString(", A:");printd((gui_cmd[1]&0x3f)*10);
					printString("   STOP\n");
					PWM16_disable();
				}
			}
			*/
			else if(gui_cmd[0] == 0xD5)
			{
				if(gui_cmd[1] == 0xFF)
				{
					printString("[CS8963]: Got command: Reset, abort....\n");
					return;
					PINT0EN = 0;
					PWM16_disable();
					MtState = stop;
					//motor_start = 1;
					//timer0_cnt = 0;
					//target_speed = 0;
					real_speed = 0;
					//hall_fail_cnt = 0;
					check_speed = 0;
					//svpwm_m = SVPWM_M_VALUE;
					//PWM_duty = svpwm_m;
					//svpwm_m_temp = SVPWM_M_VALUE;
					printString("[CS8963]: Got command: Reset\n");
					Reset_system();
				}
				else if(gui_cmd[1] == 0xFC)
				{
					printString("[CS8963]: Print Message.......\n");
					Show_SETUP_Info();
					printString("Now: \n");
					printString("Duty:");printd(PWM_duty);printS(' ');
					printString("Period: 0x");printx(PWM_period);
					printString(" Target:");printd(target_speed);
					printString(" RPM:");printd(real_speed);printString("\n");
					printString("Hall status: ");get_current_hall_state();printString("\n");

					printString("USE_UART, UART_BD_OFFSET = ");
					//printd_sign(UART_BD_OFFSET);

					if(UART_BD_OFFSET<0)
					{
						printS('-');
						//printd(-UART_BD_OFFSET);
					}
					else
					{
						printS('+');
						printd(UART_BD_OFFSET);
					}

					printString("\n");
					#ifndef USE_COMPACT
					if(flag_over_current_protection == 1)
					{
						//printString("[CS8963]: Enable over current protection. Use pin22 P3.3, VTH1=");printd(CMPVTH_VALUE1);
						//printString(", VTH2=");printd(CMPVTH_VALUE2);printString("\n");
					}
					#endif
					//printString("H:");get_current_hall_state();printString(", m:");printd(svpwm_m);
					//printString(", A:");printd(index_angle);
					printString("\n");

					#ifdef ENABLE_USE_POWER_LIMIT_DEBUG
					flag_print_power_data = 1;
					#endif

					#ifdef ENABLE_ZW_DEBUG
					flag_print_debug_data = 1;
					#endif
				}
				else if(gui_cmd[1] == 0xFA)
				{
					printString("[CS8963]: Got command: Update System Status\n");
					Initial_Timer3();											//Initial Timer3
					flag_mysonlink_update_message = 1;
				}
				else if(gui_cmd[1] == 0xF5)
				{
					printString("[CS8963]: Got command: Do Not Update System Status\n");
					Timer3_Close();
					flag_mysonlink_update_message = 0;
				}
				else if(gui_cmd[1] == 0xFD)
				{
					printString("[CS8963]: PWM mode\n");
					//SETUP_enable_svpwm_mode(0);
				}
				else if(gui_cmd[1] == 0xFE)
				{
					printString("[CS8963]: SVPWM mode\n");
					//SETUP_enable_svpwm_mode(1);
				}
				else
				{
					printString("[CS8963]: Unknown\n");
				}
			}
			else if(gui_cmd[0] == 0xD6)
			{
				//TBD
			}
			else if(gui_cmd[0] == 0xD7)
			{
				if(xx == _TEST_PWM)		//PWM test
				{
					if(yy == _STOP)
					{
						printString("[CS8963]: Disable PWM\n");
						PWM16_disable();
					}
					else if(yy == 0x55)		//auto one step
					{
						printString("[CS8963]: auto one step\n");
						get_current_hall_state();
						if(flag_run_dir == CW)
							MT_drive(Hal_sta);
						else
							MT_drive(7 - Hal_sta);
						DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
						PWM16_disable();
					}
					else if((yy >= 1)&&(yy <= 6))
					{
						printString("[CS8963]: Got Mt_drive(");
						printd(yy);printString("), pulse mode\n");
						if(flag_run_dir == CW)
							MT_drive(yy);
						else
							MT_drive(7 - yy);
						DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
						PWM16_disable();
					}
					else if((yy >= 11)&&(yy <= 16))
					{
						yy -= 10;
						PWM16_disable();
						printString("[CS8963]: Got Mt_drive(");
						printd(yy);printString("), continous mode\n");
						if(flag_run_dir == CW)
							MT_drive(yy);
						else
							MT_drive(7 - yy);
					}
					else
					{
						printString("[CS8963]: Illegal Mt_drive, step = ");
						printd(yy);printString(", abort...\n");
					}
				}
				else if(xx == _TEST_UART)		//UART test
				{
					if(yy == _STOP)
					{
						printString("[CS8963]: UART test SP\n");
						//Timer4_Close();
					}
					else
					{
						printString("[CS8963]: UART test ST\n");
						//Initial_Timer4();
					}
				}
				else if(xx == _TEST_UVW)		//UVW test
				{
					if(yy == _STOP)
					{
						printString("[CS8963]: UVW test SP\n");
						//Timer4_Close();		TBD
					}
					else
					{
						printString("[CS8963]: UVW test ST\n");
						printString("TEST Gate Driver........,  Press RESET to EXIT.\n");
						//Initial_PWM16_Test_Gate_Driver(PWM_period, 10, 3, 20);
						while(1)
						{
							printS('6');printS(' ');MT_drive(6);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
							printS('4');printS(' ');MT_drive(4);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
							printS('5');printS(' ');MT_drive(5);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
							printS('1');printS(' ');MT_drive(1);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
							printS('3');printS(' ');MT_drive(3);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
							printS('2');printS(' ');MT_drive(2);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
						}
						//Initial_Timer4();		TBD
					}
				}
			}
			else if(gui_cmd[0] == 0xD8)	//AC Motor parameters
			{
				PWM_duty = xx;
				//ac_motor_TH1 = yy;
				//ac_motor_TL1 = zz;
			}
			else if(gui_cmd[0] == 0xD9)	//setup comparator
			{
				if(((xx)>>6&0x03)==3)
				{
					if(zz != 0)
					{
						printString("[CS8963]: Enable Comparator, VTH1 = ");printd(zz);printString("\n");
						Initial_Comparator_VTH1(zz);						//Initial Comparator with small VTH when running
					}
					//else
						//printString("[CS8963]: No VTH1 setup, abort...\n");
				}
				else if(((xx)>>6&0x03)==0)
				{
					printString("[CS8963]: Disable Comparator\n");
					Disable_Comparator();
				}
			}
			else if(gui_cmd[0] == 0xDA)	//setup DAC
			{
				//TBD
			}
			else if(gui_cmd[0] == 0xDB)	//setup protection
			{
				#ifndef USE_COMPACT
				if(xx == 0xff)
				{
					printString("[CS8963]: Get Protection Command = ");printx(zz);printString("\n");
					SETUP_enable_over_current_protection(zz&0x07);
					if(((zz>>0)&0x01)==1)
					{
						//SETUP_enable_over_current_protection(1);
						printString("[CS8963]: Enable Over Current Protection A.\n");
					}
					else
					{
						//SETUP_enable_over_current_protection(0);
						printString("[CS8963]: Disable Over Current Protection A.\n");
						Disable_ADC(SAMPLE_CURRENT_ADC);
					}
					if(((zz>>1)&0x01)==1)
					{
						printString("[CS8963]: Enable Over Current Protection C.\n");
					}
					else
					{
						printString("[CS8963]: Disable Over Current Protection C.\n");
					}
	
					if(((zz>>2)&0x01)==1)
					{
						printString("[CS8963]: Enable Over Current Protection X.\n");
					}
					else
					{
						printString("[CS8963]: Disable Over Current Protection X.\n");
					}

					if(((zz>>3)&0x01)==1)
					{
						SETUP_enable_lock_rotor_protection(1);
						printString("[CS8963]: Enable Lock-Rotor Protection.\n");
					}
					else
					{
						SETUP_enable_lock_rotor_protection(0);
						printString("[CS8963]: Disable Lock-Rotor Protection.\n");
					}

					if(((zz>>4)&0x01)==1)
					{
						SETUP_enable_hall_protection(1);
						printString("[CS8963]: Enable Hall sequence protection.\n");
					}
					else
					{
						SETUP_enable_hall_protection(0);
						printString("[CS8963]: Disable Hall sequence protection.\n");
					}

					if(((zz>>5)&0x01)==1)
					{
						SETUP_enable_vdc_protection(1);
						printString("[CS8963]: Enable VDC protection.\n");
					}
					else
					{
						SETUP_enable_vdc_protection(0);
						printString("[CS8963]: Disable VDC protection.\n");
					}

					if(((zz>>6)&0x01)==1)
					{
						SETUP_enable_watchdog(1);
						printString("[CS8963]: Enable WatchDog.\n");
					}
					else
					{
						SETUP_enable_watchdog(0);
						printString("[CS8963]: Disable WatchDog.\n");
					}
				}
				else if(((xx>>4)&0x0f) == 0)	//OCA
				{
					if(((xx>>0)&0x0f) == 0x0f)
					{
						SETUP_Over_Current_ADC(yy<<8|zz);
						//printString("Enable ADC, value = ");printx(yy<<8|zz);printString("\n");
					}
					else if(((xx>>0)&0x0f) == 0x00)
					{
						//Disable OCA
						Disable_ADC(SAMPLE_CURRENT_ADC);
					}
				}
				else if(((xx>>4)&0x0f) == 2)	//OCX
				{
					if(((xx>>0)&0x0f) == 0x0f)	//Enable
					{
						printString("Enable Over-Current Protection X\n");
					}
					else if(((xx>>0)&0x0f) == 0x00)
					{
						printString("Disable Over-Current Protection X\n");
					}
				}
				else if(((xx>>4)&0x0f) == 3)	//Lock-Rotor
				{
					if(((xx>>0)&0x0f) == 0x0f)	//Enable
					{
						printString("Enable Lock-Rotor Protection\n");
						SETUP_enable_lock_rotor_protection(1);
					}
					else if(((xx>>0)&0x0f) == 0x00)
					{
						printString("Disable Lock-Rotor Protection\n");
						SETUP_enable_lock_rotor_protection(0);
					}
				}
				else if(((xx>>4)&0x0f) == 4)	//Hall
				{
					if(((xx>>0)&0x0f) == 0x0f)	//Enable
					{
						printString("Enable Hall Protection\n");
						SETUP_enable_hall_protection(1);
					}
					else if(((xx>>0)&0x0f) == 0x00)
					{
						printString("Disable Hall Protection\n");
						SETUP_enable_hall_protection(0);
					}
				}
				else if(((xx>>4)&0x0f) == 5)	//VDC
				{
					if(((xx>>0)&0x0f) == 0x0f)
					{
						SETUP_enable_vdc_protection(1);
						if(((yy>>4)&0x0f) == 1)
							Voltage_High_Off = ((yy&0x0f)<<8) | zz;
						else if(((yy>>4)&0x0f) == 2)
							Voltage_High_On = ((yy&0x0f)<<8) | zz;
						else if(((yy>>4)&0x0f) == 3)
							Voltage_Low_On = ((yy&0x0f)<<8) | zz;
						else if(((yy>>4)&0x0f) == 4)
							Voltage_Low_Off = ((yy&0x0f)<<8) | zz;
					}
					else if(((xx>>0)&0x0f) == 0x00)
					{
						//Disable VDC protection
						SETUP_enable_vdc_protection(0);
					}
				}
				else if(((xx>>4)&0x0f) == 6)	//Watchdog
				{
					if(((xx>>0)&0x0f) == 0x0f)	//Enable
					{
						printString("Enable Watchdog\n");
						SETUP_enable_watchdog(1);
					}
					else if(((xx>>0)&0x0f) == 0x00)
					{
						printString("Disable Watchdog\n");
						SETUP_enable_watchdog(0);
					}
				}


				#endif

			}
			/*	useless?
			else if(gui_cmd[0] == 0xDD)
			{
				gui_value = gui_cmd[1];
				if((gui_value >=0 )&&(gui_value <=100 ))
				{
					printString("[CS8963]: Got Setup Duty Command, duty = ");
					printd(gui_value);printString("\n");
					PWM_duty = gui_value;
					Initial_PWM16(PWM_period, PWM_duty);				//Initial PWM16
				}
				else
				{
					printString("[CS8963]: Illegal PWM duty, duty = ");
					printd(gui_value);printString(", abort...\n");
				}
			}
			*/
		}
	}
	SINT2 = 0xa0;	//only EUART2 need use it!!!,other UARTs needn't.
	EA = 1;
}
#endif	//end of #ifdef USE_MYSONLINK
