typedef    unsigned char		BYTE;		//8bit
typedef    unsigned int			UINT;		//16bit
typedef    unsigned long int		ULONG;		//32bit

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

extern unsigned int  PWM_period;
extern unsigned int target_current;
extern unsigned int target_speed;
extern unsigned int real_speed;
extern unsigned int real_speed1;
extern unsigned char PWM_duty;
extern unsigned char PWM_duty_old;
extern unsigned char PWM_dead_time;
extern UINT dutyA;
extern UINT dutyB;
extern UINT dutyC;
extern unsigned char pwm_input_duty;
extern unsigned char pwm_input_duty_old;
extern unsigned char motor_uvw_sequence;
extern char MtState_temp;
extern unsigned int ADC_A_InstanceCurrent;
extern unsigned int ADC_B_InstanceCurrent;
extern unsigned int ADC_C_InstanceCurrent;
extern unsigned int ADC_D_InstanceCurrent;
extern unsigned char Hal_sta;
extern unsigned char Hal_sta_next;
extern unsigned char Hal_sta_next2;
extern unsigned char tcount;
extern unsigned char t1count;
extern unsigned char count_mode_type;
extern unsigned int over_current_cnt;
extern unsigned char cnt_CurPro;
extern unsigned char flag_run_dir;
extern unsigned char flag_auto_start;
extern unsigned char flag_slow_modify_duty;
extern unsigned char flag_debug_mode;
extern unsigned char flag_test_hall_sequence_mode;
extern unsigned char flag_engineering_mode;
extern unsigned char flag_phase_compensation_mode;
extern unsigned char flag_mode_type;
extern unsigned char flag_speed_control_mode;
extern unsigned char flag_enable_watchdog;
extern unsigned char flag_fix_current_function;
extern unsigned char flag_over_current_proction;
extern unsigned char flag_lock_rotor_proction;
extern unsigned char flag_svpwm_mode;
extern UINT svpwm_leading_angle;
extern UINT angle_tmp;
extern unsigned int index_angle;
extern BYTE svpwm_step;
extern unsigned char delay_time;
extern unsigned char number_motor_pole_pair;
extern ULONG PWM16INT_cnt;
extern ULONG pwm_cnt_start;
extern ULONG pwm_cnt_diff;
extern ULONG pwm_cnt_start2;
extern ULONG pwm_cnt_diff2;
extern unsigned char MtState; 
extern unsigned char MtState_vr;
extern ULONG T4_count;
extern ULONG T5_count;
extern BYTE T3H_pwm_output;
extern BYTE T3L_pwm_output;
extern BYTE PWMDUTY_L;
extern BYTE PWMDUTY_H;
extern ULONG time_diff_hall;
extern BYTE phase_angle;
extern ULONG pwm_cnt_start_gui;
extern unsigned int xdata targ_speed;
extern unsigned int xdata PWM_freq;
extern unsigned int xdata Hal_cnt;
extern ULONG PWM_high_sum;
extern ULONG PWM_low_sum;
extern UINT svpwm_change_pwm_array[60];

//USE_MYSON_GUI ST
//extern unsigned char xdata flag_uart0_rec;
//extern unsigned char xdata buffer_uart0_rec[3];
//extern unsigned char xdata uart0_rec[3];
//extern unsigned char xdata Flag_update_PCtoBLDC;
//extern unsigned char xdata PCtoBLDC_UART0_REC[24];
extern unsigned char xdata send_message_flag;	
extern unsigned char xdata SEND_MESSAGE_NUM;
extern unsigned char xdata Flag_Alarm_L;
extern unsigned char xdata Hal_sta_final;
extern unsigned int xdata AverageCurrent;

enum _MtState
{
	start,
	stop,
	brake,
	run,
	error
};

enum _ModeType
{
	OPEN_LOOP,
	CLOSE_LOOP,
	CURRENT_LOOP,
	PWM_LOOP,
};

enum _SpeedControlMode
{
	NORMAL_MODE,
	VR_MODE,
	PWM_INPUT_MODE,
};

#define iSYSCLK				16000000
#define xSYSCLK				22118400
#define SYSCLK				iSYSCLK

#define Hopen				b00100000
#define Lopen				b00100000
#define Close				b00000001


