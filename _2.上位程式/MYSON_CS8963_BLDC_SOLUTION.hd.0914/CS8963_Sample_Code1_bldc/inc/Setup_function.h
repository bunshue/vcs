#ifndef __SETUP_FUNCTION_H__
#define __SETUP_FUNCTION_H__

/************************************************************************/
/*                        Function Setup                                */
/************************************************************************/

#define SVPWM_M_VALUE 		10

#define SLOW_MODIFY_SPEED	2				//0 ~ 10: quick ~ slow

#define CS7211_VREF_VOLTAGE	4500			//CM2209B Setup pin1_P1.7 as CS7211_VREF_VOLTAGE mV

/*  VR  */
//#define USE_VR_RESUME
#define USE_VR_TOLERANCE
#define VR_TOLERANCE			21			//in ADC, 21ADC = 25mV
#define PIN_VRin				PIN13		//CM2209A, CM2209B, CM2209C use pin13 as VRin, ADC A
#define VR_SPEED_DUTY_MAX		100
#define VR_SPEED_DUTY_MIN		PWM_START_DUTY
#ifdef MOTOR_HD
#define VR_SPEED_RPM_MAX		HD_RPM_MAX
#define VR_SPEED_RPM_MIN		HD_RPM_MIN
#else
#define VR_SPEED_RPM_MAX		MAXSPEED
#define VR_SPEED_RPM_MIN		MINSPEED
#endif
#define VR_MAX					4500		//mV
#define VR_MIN					500			//mV
#define VR_PROBE_SPEED			500			//typical 500	//for TEST_VR

//#define USE_LOW_SPEED_WARNING				//enable low speed warning

//#define NO_PRINT_WHEN_RUNNING

/*  Phase Compensation  */
#define ENABLE_PHASE_COMPENSATION		0	//Phase compensation enable  0:off 1:on
#define PHASE_ANGLE_CW					45
#define PHASE_ANGLE_CCW					75

#define ENABLE_POWER_WARNING		//use for POWER warning if power is on
#define ENABLE_POWER_WARNING_FAST	2
#define ENABLE_POWER_WARNING_MEDIUM	10
#define ENABLE_POWER_WARNING_SLOW	20

#define USE_FLASH_DATA			//reserved for mysonlink

#define DC_VOLTAGE		12		//DC Voltage, reserved
#define AC_VOLTAGE		220		//AC Voltage, reserved

#define CALCULATE_SPEED_BY_PWM

#define CHECK_SPEED_BY_PWM
//#define CHECK_SPEED_BY_PID
//#define CHECK_SPEED_BY_LINEAR

#define KP 	4
#define KI 	4
#define KD 	0

/*  UVW  */
#define UVW_TYPE_A
//#define UVW_TYPE_B

/*  MysonLink  */

#define RPM_TOLERANCE		15

/*	reserved
#define RPM_TOLERANCE_P		3			//percent

7%
4%	1/
3%   1/32
2%	 1/64
1%   1/128
*/

#define ACCELERATION		100
#define MYSONLINK_UPDATE_MESSAGE	1	//MysonLink Update Message enable  0:off 1:on

#ifdef USE_MYSONLINK
#undef NO_PRINT_WHEN_RUNNING
#endif

#define USE_FULL
//#define USE_COMPACT

//#define LESS_CODE

/*  PWM frequency  */
//#define PWM_PERIOD	0x200		//PWM period, 15.625kHz
#define PWM_PERIOD		400			//PWM period, 20kHz
//#define PWM_PERIOD	320			//PWM period, 25kHz
//#define PWM_PERIOD	4000		//PWM period, 2kHz
//#define PWM_PERIOD	8000		//PWM period, 1kHz
//#define PWM_PERIOD	16000		//PWM period, 500Hz
//#define PWM_PERIOD	32000		//PWM period, 250Hz
//#define PWM_PERIOD	32767		//PWM period, 244Hz(minimum)

#ifdef CM2209D
#undef SPEED_CONTROL_MODE
#define SPEED_CONTROL_MODE	NORMAL_MODE
#endif

#if defined(STAR) || defined(STAR_V17)
	#undef MOTOR_M0
	#undef MOTOR_M1
	#undef MOTOR_M2
	#undef MOTOR_M3
	#undef MOTOR_M4
	#undef MOTOR_HD
	#undef MOTOR_VAR1
	#undef MOTOR_VAR2
	#define MOTOR_STAR
	//#define NO_PRINT_WHEN_RUNNING
#endif

#ifdef HD
	#undef MOTOR_M0
	#undef MOTOR_M1
	#undef MOTOR_M2
	#undef MOTOR_M3
	#undef MOTOR_M4
	#undef MOTOR_VAR1
	#undef MOTOR_VAR2
	#undef MOTOR_STAR
	#define MOTOR_HD
	
	#undef CM2209A		//LV_DEMO_BOARD use PNMOS
	#undef CM2209B		//LV_DEMO_BOARD use CS7211
	#undef CM2209C		//HV_DEMO_BOARD use IR2101
	#undef CM2209D		//LV_DEMO_BOARD use IR2101
	#define CM2209C		//HV_DEMO_BOARD use IR2101
	
	#define USE_HD_CONTROL
	#define HD_RPM_MAX		3600	//1800, 3600
	#define HD_RPM_MAX_3600		3600
	#define HD_RPM_MAX_1800		1800
	#define HD_RPM_MIN		300
	
	#undef USE_VR_RESUME
	#define USE_VR_RESUME
	
	#undef MODE_TYPE
	#define MODE_TYPE			CLOSE_LOOP
#endif


#ifdef CM2209C
#define CHECK_VDC_VOLTAGE
#endif

#define UART_BUF_LENGTH		5

/*  UART  */
#define BAUD_RATE			115200		//UART baud rate

#ifdef CM2209A
	#define UART_BD_OFFSET	+0
#elif defined CM2209B
	#ifdef STAR
	#define UART_BD_OFFSET	-15
	#elif defined STAR_V17
	#define UART_BD_OFFSET	-15
	#else
	#define UART_BD_OFFSET	+10
	#endif
#elif defined CM2209C
	#ifdef HD
	#define UART_BD_OFFSET	-30
	#else
	#define UART_BD_OFFSET	0
	#endif
#elif defined CM2209D
	#define UART_BD_OFFSET	+10
#else
	#define UART_BD_OFFSET	+10
#endif

#ifndef USE_XOSC
#define ENABLE_FG_OUT						//enable FG output
#endif

#ifdef MOTOR_HD
#define PIN_FG_OUT				PIN2		//use pin2_P1.6 as FG-out for HD
#else
#define PIN_FG_OUT				PIN31		//use pin31_P2.0 as FG-out
#endif

/*  I2C  */
//#define USE_I2C_Master
//#define USE_I2C_Slave

#define IIC_Slave_Addr	0x90		//Master to slave
#define IICS1_Addr1		0x90		//P2_1 P2_0(bit6-bit0)
#define IICS1_Addr3		0x4E		//P2_1 P2_0(bit6-bit0)

/*  Test  */
//#define TEST_I2C
//#define TEST_UART
//#define TEST_VR
//#define TEST_UVW
//#define TEST_GPIO
//#define TEST_KEY
//#define TEST_START
//#define TEST_ADC2VAC

/*  Debug  */
#define DEBUG_MODE			0		//debug mode, 0:off, 1:on
//#define DUMP_PWM_SETUP
//#define PWM_TRIGGER_ADC
//#define SAVE_FACTORY_DATA
#define SAVE_FACTORY_DATA_PERIOD 	11111		//seconds
//#define MT_DRIVE_DEBUG
//#define HALL_DEBUG
//#define RECORD_PID_DATA

/************************************************************************/
/*                       Protection Setup                               */
/************************************************************************/

#define OVER_CURRENT_TIME					5	//over current protection time
#define LOCK_ROTOR_TIME						5	//lock rotor time
#define LOCK_ROTOR_UPPER_LIMIT				100	//lock rotor upper limit

#define SAMPLE_DCBUS_ADC		PIN17	//ADCB
#define SAMPLE_CURRENT_ADC		PIN18	//ADCA
#define SAMPLE_CURRENT_CMP		PIN24	//CMPA

#define RESISTANCE		0.5			//resistor in sampling circuit
#define VOLTAGE_GAIN	6			//voltage gain of sampling circuit
#define I510mA_Average	0x00F0
#define I459mA_Average	0x00D0
#define I420mA_Average	0x00A0
#define I384mA_Average	0x008F

#define I100mA 0x0F5
#define I200mA 0x1EB
#define I300mA 0x2E1
#define I400mA 0x3D7
#define I500mA 0x4CC
#define I600mA 0x5C2
#define I700mA 0x6B8
#define I800mA 0x7AE
#define I900mA 0x8A3
#define I1000mA 0x8A3
#define I1100mA 0x999
#define I1200mA 0xA8F
#define I1300mA 0xC7A

/* matlab code for ADC
clear,clc
RESISTANCE = 0.5;
VOLTAGE_GAIN = 6;
ADC_FULL = 5;
current= 100:100:1300;
voltage_in = current * RESISTANCE;
voltage_out = voltage_in * OLTAGE_GAIN;
ADC = voltage_out*4096/ADC_FULL/1000;
plotyy(current,voltage_out/1000,current,ADC);
xlabel('sample current (mA)');ylabel('vout (V)');text(1450,2.5,'ADC');grid on;
dec2hex(floor(ADC))
=> result : 0F5 1EB 2E1 3D7 4CC 5C2 6B8 7AE 8A3 999 A8F B85 C7A
*/

//#define CMPVTH_VALUE	42	//Comparator Threshold 0.300V Value, 0.300/1.8*256=42	100mA
//#define CMPVTH_VALUE	85	//Comparator Threshold 0.600V Value, 0.600/1.8*256=85	200mA
//#define CMPVTH_VALUE	128	//Comparator Threshold 0.900V Value, 0.900/1.8*256=128	300mA
//#define CMPVTH_VALUE	170	//Comparator Threshold 1.200V Value, 1.200/1.8*256=170	400mA
//#define CMPVTH_VALUE	213	//Comparator Threshold 1.500V Value, 1.500/1.8*256=213	500mA
//#define CMPVTH_VALUE	241
//#define CMPVTH_VALUE	256	//Comparator Threshold 1.800V Value, 1.800/1.8*256=256	600mA

//#define CMPVTH_VALUE	240	//Comparator Threshold 1.690V Value, 1.690/1.8*256=240	1130mA 0.25Ohm for CM2209D

/* matlab code for CMP
clear,clc
RESISTANCE = 0.5;
VOLTAGE_GAIN = 6;
CMP_FULL = 1.8;
current= 0:100:600;
voltage_in = current * RESISTANCE;
voltage_out = voltage_in * VOLTAGE_GAIN;
CMPVTH_VALUE = voltage_out*256/CMP_FULL/1000;
plotyy(current,voltage_out/1000,current,CMPVTH_VALUE);
xlabel('sample current (mA)');ylabel('vout (V)');text(600,0.5,'CMPVTH_VALUE');grid on;
floor(CMPVTH_VALUE)=> result : 0 42 85 128 170 213 256
*/

#define VAC_HIGH_OFF_ADC_220	2755	//220*120% = 264VAC
#define VAC_LOW_OFF_ADC_220		1840	//220*80%  = 176VAC
#define VAC_HIGH_OFF_ADC_110	1380	//110*120% = 132VAC
#define VAC_LOW_OFF_ADC_110		 920	//110*80%  =  88VAC

#ifdef MOTOR_HD
#ifdef USE_AC_220
#define VAC_HIGH_OFF_ADC	2400	//220*105% = 231VAC => 2400*5000/4096/1000*(220+2)/2/sqrt(2)=230
#define VAC_LOW_OFF_ADC		1878	//220*82%  = 180VAC => 1878*5000/4096/1000*(220+2)/2/sqrt(2)=180
#else	//USE_AC_110
#define VAC_HIGH_OFF_ADC	1380	//110*120% = 132VAC => 1380*5000/4096/1000*(220+2)/2/sqrt(2)=132
#define VAC_LOW_OFF_ADC		 920	//110*80%  = 88VAC  =>  920*5000/4096/1000*(220+2)/2/sqrt(2)=88
#endif
#else
#define VAC_HIGH_OFF_ADC	2870	//275VAC => 2870*5000/4096/1000*(220+2)/2/sqrt(2)=275
#define VAC_LOW_OFF_ADC		1725	//165VAC => 1725*5000/4096/1000*(220+2)/2/sqrt(2)=165
#endif

#define VAC_HIGH_ON_ADC		2720	//260VAC => 2720*5000/4096/1000*(220+2)/2/sqrt(2)=260
#define VAC_LOW_ON_ADC		1880	//180VAC => 1880*5000/4096/1000*(220+2)/2/sqrt(2)=180

#define VDC24_HIGH_OFF_ADC	2145	//24*120% = 28.8V => VDC=24*1.2;VDC*4096/11/5=2145
#define VDC24_LOW_OFF_ADC	1430	//24*80%  = 19.2V => VDC=24*0.8;VDC*4096/11/5=1430

/************************************************************************/
/*                           Motor Setup                                */
/************************************************************************/

#define MINDUTY					3			//minimum pwm duty

#ifdef MOTOR_M0
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			2			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			2000		//target speed
#define MAXSPEED				20000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_M1
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			1			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			10000		//target speed
#define MAXSPEED				20000
#define MINSPEED				1000
#define OVER_CURRENT_VALUE		1234		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_M2
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			4			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			1000		//target speed
#define MAXSPEED				4500
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1234		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_M3
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			2			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			1000		//target speed
#define MAXSPEED				4000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1234		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_M4
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			6			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			1000		//target speed
#define MAXSPEED				3000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1234		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_HD
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			4			//motor magnetic pole pair
#define PWM_START_DUTY			3			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			1000		//target speed
#define MAXSPEED				3600
#define MINSPEED				100
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_STAR
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			7			//motor magnetic pole pair
#define PWM_START_DUTY			25			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+20	//PWM duty cycle increment end when start
#define TARGET_SPEED			50			//target speed
#define MAXSPEED				3000
#define MINSPEED				20
#define OVER_CURRENT_VALUE		700			//over current criterion 	2A
#define CMPVTH_VALUE			120			//Comparator Threshold		2A
#elif defined MOTOR_VAR1
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			6			//motor magnetic pole pair
#define PWM_START_DUTY			30			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			2000		//target speed
#define MAXSPEED				5000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_VAR2
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			6			//motor magnetic pole pair
#define PWM_START_DUTY			30			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			2000		//target speed
#define MAXSPEED				25000
#define MINSPEED				1000
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_CL
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			2			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle	20@12V
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			2000		//target speed
#define MAXSPEED				10000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_CM
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			1			//motor magnetic pole pair
#define PWM_START_DUTY			30			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			2000		//target speed
#define MAXSPEED				20000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#elif defined MOTOR_CS
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			1			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			2000		//target speed
#define MAXSPEED				20000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1445		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#else
//#define MOTOR_UVW_SEQUENCE_TYPE	1		//motor UVW sequence
#define UVW_TYPE_A							//motor UVW sequence
#define DIRECTION				0			//0:clockwise, 1:counterclockwise
#define MOTOR_POLE_PAIR			3			//motor magnetic pole pair
#define PWM_START_DUTY			20			//PWM duty cycle
#define PWM_START_DUTY_INC		2			//PWM duty cycle increment when start
#define PWM_START_DUTY_END		PWM_START_DUTY+10	//PWM duty cycle increment end when start
#define TARGET_SPEED			1000		//target speed
#define MAXSPEED				3000
#define MINSPEED				500
#define OVER_CURRENT_VALUE		1234		//over current criterion
#define CMPVTH_VALUE			250			//Comparator Threshold 250/255*1.8 = 1.76V
#endif

/************************************************************************/
/*                       Sensorless Setup                               */
/************************************************************************/

//Sensorless setup

#endif
