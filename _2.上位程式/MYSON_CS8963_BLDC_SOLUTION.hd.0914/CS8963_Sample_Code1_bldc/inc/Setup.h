#ifndef __SETUP_H__
#define __SETUP_H__

/*  MOS  */
#define USE_NNMOS
//#define USE_PNMOS

/*  Board  */
//#define CM2209A		//LV_DEMO_BOARD use PNMOS
//#define CM2209B			//LV_DEMO_BOARD use CS7211
#define CM2209C		//HV_DEMO_BOARD use IR2101
//#define CM2209D		//LV_DEMO_BOARD use IR2101
//#define CM2209_K1		//customer board 1
//#define TW
//#define STAR
//#define STAR_V17
#define HD
//#define USE_XOSC

//#define USE_PCA
//#define USE_PCA_AUTO_RUN
#define PCA_START_DUTY		140
#define PCA_DUTY_MAX		255
#define PCA_USE_REAL_HALL	0		//0: sensorless, 1: hall sensor

/*  MysonLink  */
//#define USE_MYSONLINK

/*  Control  */
#define SPEED_CONTROL_MODE	VR_MODE
/*
0	NORMAL_MODE
1	VR_MODE
*/

#define MODE_TYPE			OPEN_LOOP
/*
0	OPEN_LOOP
1	CLOSE_LOOP
*/

#define SENSOR_MODE			HALL_SENSOR_MODE
/*
0	HALL_SENSOR_MODE
1	SENSORLESS_MODE
2	PCA_MODE
*/

#define ENABLE_WATCHDOG						0	//watchdog enable
#define ENABLE_HALL_PROTECTION				1	//hall sequence check
#ifdef CM2209C
#define ENABLE_VDC_PROTECTION				1	//VDC protection enable
#else
#define ENABLE_VDC_PROTECTION				0	//VDC protection enable
#endif
#if defined(CM2209B) || defined(CM2209C)
#define ENABLE_OVER_CURRENT_PROTECTION_A	1	//over current protection enable by ADC
#define ENABLE_OVER_CURRENT_PROTECTION_C	1	//over current protection enable by CMP
#define ENABLE_OVER_CURRENT_PROTECTION_X	1	//over current protection enable by XEMG
#define ENABLE_LOCK_ROTOR_PROTECTION		1	//lock rotor protection enable
#else
#define ENABLE_OVER_CURRENT_PROTECTION_A	0	//over current protection enable by ADC
#define ENABLE_OVER_CURRENT_PROTECTION_C	0	//over current protection enable by CMP
#define ENABLE_OVER_CURRENT_PROTECTION_X	0	//over current protection enable by XEMG
#define ENABLE_LOCK_ROTOR_PROTECTION		0	//lock rotor protection enable
#endif

#define MOTOR_M0
/* Motor number
0: M0
1: M1
2: M2
3: M3
4: M4
5: HD
6: STAR
7: VAR1
8: VAR2
8: CL
9: CM
10: CS
*/

#define USE_AC_220
//#define USE_AC_110
#endif
