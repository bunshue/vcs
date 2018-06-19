typedef    unsigned char		BYTE;		//8bit
typedef    signed int			SINT;		//16bit
typedef    unsigned int			UINT;		//16bit
typedef    unsigned long int	ULONG;		//32bit
typedef    signed long int		SLONG;		//32bit

#define IFB_ByteRead 	0x02

#define INTflg_CMPA		0x10
#define Output_CMPSTA	0x01
#define ADC_A_EN		0x80	//ADC A conversion enable
#define ADC_B_EN		0x40	//ADC B conversion enable
#define ADC_C_EN		0x20	//ADC C conversion enable
#define ADC_D_EN		0x10	//ADC D conversion enable

#define ADC_A_IF		0x08	//ADC A conversion completion interrupt flag
#define ADC_B_IF		0x04	//ADC B conversion completion interrupt flag
#define ADC_C_IF		0x02	//ADC C conversion completion interrupt flag
#define ADC_D_IF		0x01	//ADC D conversion completion interrupt flag

extern bit flag_check_vdc;
extern bit flag_check_vr;
extern bit flag_check_speed;
extern bit flag_check_lock_rotor;
extern bit flag_check_over_current;
extern bit flag_check_test_start;
extern bit flag_check_status;
extern bit flag_check_debug_message;
extern bit flag_send_hall_status;
extern bit flag_print_message;
extern bit flag_PWM16_Modify;
extern bit flag_int0_ser;
extern BYTE check_speed;
extern unsigned int PWM_period;
extern unsigned int real_speed;
extern unsigned int real_speed_tmp;
extern BYTE data int0_cnt;
extern UINT data pwm16_int_cnt;
extern UINT data pwm16_int_cnt_tmp;
extern unsigned int max_speed;
extern unsigned int min_speed;
extern BYTE rpm_tolerance;
extern BYTE acceleration;
extern unsigned char PWM_start_duty;
extern unsigned char PWM_duty;
extern unsigned char PWM_duty_target;
extern unsigned char PWM_duty_old;
extern unsigned char PWM_duty_new;
extern unsigned char PWM_dead_time;
extern unsigned char pwm_input_duty;
extern unsigned char pwm_input_duty_old;
extern unsigned char PCA_duty;
extern unsigned char PCA_duty_old;
extern unsigned char PCA_use_real_hall;
extern unsigned char motor_uvw_sequence;
extern unsigned int Over_Current_ADC;
extern unsigned int ADC_A_result;
extern unsigned int ADC_B_result;
extern unsigned int ADC_C_result;
extern unsigned int ADC_D_result;
extern unsigned char Hal_sta;
extern unsigned char Hal_sta_next;
extern unsigned char Hal_sta_next2;
extern unsigned char t0_cnt;
extern unsigned char t1_cnt;
extern unsigned char count_mode_type;
extern unsigned int over_current_cnt;
extern unsigned char cnt_CurPro;
extern unsigned char flag_run_dir;
extern unsigned char flag_enable_vr_speed;
extern unsigned char slow_modify_speed;
extern unsigned char flag_debug_mode;
extern unsigned char flag_test_hall_sequence_mode;
extern unsigned char flag_phase_compensation_mode;
extern unsigned char flag_mode_type;
extern unsigned char flag_sensor_type;
extern unsigned char flag_speed_control_mode;
extern unsigned char flag_enable_watchdog;
extern unsigned char flag_over_current_protection;
extern unsigned char flag_lock_rotor_protection;
extern unsigned char flag_vdc_protection;
extern unsigned char flag_hall_protection;
extern unsigned char flag_update_status;
extern unsigned char flag_hall_sequence;
extern unsigned char PowerState;
extern BYTE VDC_result;
extern UINT VDC_result_ADC;
extern UINT Voltage_High_Off;
extern UINT Voltage_High_On;
extern UINT Voltage_Low_On;
extern UINT Voltage_Low_Off;
extern UINT Voltage_High_Off_ADC;
extern UINT Voltage_High_On_ADC;
extern UINT Voltage_Low_On_ADC;
extern UINT Voltage_Low_Off_ADC;
extern BYTE power_warning_count;
extern unsigned char delay_time;
extern unsigned char number_motor_pole_pair;
extern UINT number_rpm_step_size;
extern ULONG PWM16INT_cnt;
extern ULONG pwm_cnt_start;
extern ULONG pwm_cnt_diff;
extern ULONG pwm_cnt_start2;
extern ULONG pwm_cnt_diff2;
extern unsigned char MtState; 
extern unsigned char MtState_temp;
extern ULONG T4_count;
extern ULONG T5_count;
extern BYTE T3H_pwm_output;
extern BYTE T3L_pwm_output;
extern ULONG time_diff_hall;
extern BYTE phase_angle;
extern BYTE flag_enable_brake;
extern BYTE flag_enable_speed_up_fast;
extern BYTE flag_enable_speed_down_fast;
extern UINT vr_max_speed;
extern UINT vr_min_speed;
extern UINT max_power;
extern UINT ac_voltage;
extern unsigned int data target_speed;
extern unsigned int data PWM_freq;
extern unsigned int data Hal_cnt;
extern ULONG PWM_high_sum;
extern ULONG PWM_low_sum;
extern UINT tx2_buf[4];
extern ULONG StartTime;
extern BYTE StartTimeT5T;
extern BYTE StartTimeT5H;
extern BYTE StartTimeT5L;
extern ULONG StopTime;
extern BYTE StopTimeT5T;
extern BYTE StopTimeT5H;
extern BYTE StopTimeT5L;
extern ULONG ReachTime;
extern BYTE ReachTimeT5T;
extern BYTE ReachTimeT5H;
extern BYTE ReachTimeT5L;
extern UINT ERROR_number;
extern BYTE motor_restart;
extern BYTE vr_duty_start;

//for MysonLink
extern bit flag_mysonlink_update_message;
extern unsigned char svpwm_m;
extern unsigned char flag_svpwm_mode;
extern BYTE cmp_vth1;
extern BYTE cmp_vth2;
extern unsigned char sReceive_Tab[20];
extern unsigned char sTransmit_Tab[20];
extern unsigned char I2C_buffer[20];
extern unsigned char I2C_buffer_length;

//for sensorless
extern unsigned char Hal_sta_my;
extern unsigned char motor_start;
extern unsigned int data mt_drive_cnt;
extern UINT mt_drive_free_cnt;

//for calculate sensorless abnormal case
extern UINT mt_drive_time_new;
extern UINT mt_drive_time_old;
extern UINT mt_drive_time_diff_new;
extern UINT mt_drive_time_diff_old;
extern UINT too_fast;
extern UINT too_slow;
extern UINT abnormal;
#define diff(a,b)	(((a) > (b)) ? (a-b) : (a+0x10000-b))

enum _PowerState
{
	POWER_NORMAL,
	POWER_LOW,
	POWER_HIGH
};

enum _MtState
{
	start,
	stop
};

enum _ModeType
{
	OPEN_LOOP,
	CLOSE_LOOP,
};

enum _SpeedControlMode
{
	NORMAL_MODE,
	VR_MODE,
};

enum _SensorMode
{
	HALL_SENSOR_MODE,
	SENSORLESS_MODE,
	PCA_MODE,
};

enum _Direction
{
	CW,
	CCW,
};

enum _Hall_Sequence
{
	HALL_SEQ_000,
	HALL_SEQ_546,
	HALL_SEQ_645,
};

#define iSYSCLK				16000000
#define xSYSCLK				16000000
#define SYSCLK				iSYSCLK

#define Hopen				b00100000
#define Lopen				b00100000
#define Close				b00000001

#define CHECK_RISING_EDGE	CMPCFGAB = B01101110;CMPCFGCD = B11101110;
#define CHECK_FALLING_EDGE	CMPCFGAB = B01101111;CMPCFGCD = B11111111;

#define CHECK_RISING_EDGE_CD	CMPCFGCD = B11101110;
#define CHECK_FALLING_EDGE_CD	CMPCFGCD = B11111111;

#define RELEASE_INFO "MYSON CENTURY,INC., March-11-2017\n"
#define PROMPT "[bldc@myson cs8963]# "

#define ADC_AVG_TIMES					0	//ADC readout average times
/* ADC readout average times
0:  1 Time Average
1:  2 Time Average
2:  4 Time Average
3:  8 Time Average
4: 16 Time Average
5: 32 Time Average
6: 64 Time Average
7: Test Mode
*/
#define ADC_FULL		5			//ADC full scale reference
#define CMP_FULL		1.8			//CMP full scale reference

#define TOGGLE_01		P1_7 = 0;P1_7 = 1;P1_7 = 0;P1_7 = 1;P1_7 = 0;P1_7 = 1;P1_7 = 0;
#define TOGGLE_02		P1_6 = 0;P1_6 = 1;P1_6 = 0;P1_6 = 1;P1_6 = 0;P1_6 = 1;P1_6 = 0;
#define TOGGLE_03		P1_3 = 0;P1_3 = 1;P1_3 = 0;P1_3 = 1;P1_3 = 0;P1_3 = 1;P1_3 = 0;
#define TOGGLE_04		P1_2 = 0;P1_2 = 1;P1_2 = 0;P1_2 = 1;P1_2 = 0;P1_2 = 1;P1_2 = 0;
#define TOGGLE_13		P0_5 = 0;P0_5 = 1;P0_5 = 0;P0_5 = 1;P0_5 = 0;P0_5 = 1;P0_5 = 0;
#define TOGGLE_25		P2_6 = 0;P2_6 = 1;P2_6 = 0;P2_6 = 1;P2_6 = 0;P2_6 = 1;P2_6 = 0;

#define PIN_01_HIGH		P1_7 = 1;
#define PIN_01_LOW		P1_7 = 0;
#define PIN_02_HIGH		P1_6 = 1;
#define PIN_02_LOW		P1_6 = 0;
#define PIN_03_HIGH		P1_3 = 1;
#define PIN_03_LOW		P1_3 = 0;
#define PIN_04_HIGH		P1_2 = 1;
#define PIN_04_LOW		P1_2 = 0;
#define PIN_13_HIGH		P0_5 = 1;
#define PIN_13_LOW		P0_5 = 0;
#define PIN_17_HIGH		P0_1 = 1;
#define PIN_17_LOW		P0_1 = 0;
#define PIN_25_HIGH		P2_6 = 1;
#define PIN_25_LOW		P2_6 = 0;

#define HALL_DEGREE_210	6
#define HALL_DEGREE_150	4
#define HALL_DEGREE_90	5
#define HALL_DEGREE_30	1
#define HALL_DEGREE_330	3
#define HALL_DEGREE_270	2

#define DEG0	0
#define DEG60	60
#define DEG120	120
#define DEG180	180
#define DEG240	240
#define DEG300	300
#define DEG360	360

#define PWM_CLOCK_SCALE	0
	//PWM16CFG
	//CS[2:0] : PWM Clock Scaling Setting bits
	//PWMCLK = SYSCLK/(PWM_CLOCK_SCALE+1)
	//PWM_CLOCK_SCALE = 0 => PWM_CLOCK = SYSCLK

#define PWM_DEAD_TIME	8
	//PWM16CFG
	//DT[4:0] : PWM Output Rise Dead Time Delay
	//DT[4:0] = 01000 =>  8  => 1/16M*  8=0.5us
	//DT[4:0] = 11111 => 31 => 1/16M*31=1.94u

#define	_ERROR_NONE			0x0000
#define	_ERROR_PARAMETER	0x0001
#define	_ERROR_OV			0x0002
#define	_ERROR_UV			0x0004
#define	_ERROR_LOCK_ROTOR	0x0008
#define	_ERROR_HALL			0x0010
#define	_ERROR_OCA			0x0020
#define	_ERROR_OCC			0x0040
#define	_ERROR_OCX			0x0080
#define	_ERROR_UVW			0x0100
#define	_ERROR_SHORT		0x0200
#define	_ERROR_RECOVER		0x0400
