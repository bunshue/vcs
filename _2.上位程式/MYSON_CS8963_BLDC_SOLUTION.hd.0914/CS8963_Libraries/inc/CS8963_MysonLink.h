#ifndef __CS8963_MYSONLINK_H__
#define __CS8963_MYSONLINK_H__

#define _ALL			63
#define	_CONTROL		0
#define	_DIRECTION		1
#define	_REAL_SPEED		2
#define	_TARGET_SPEED	3
#define	_MAX_SPEED		4
#define	_MIN_SPEED		5
#define	_DUTY			6
#define	_SVPWM_M		7
#define	_PWM_FREQUENCY	8
#define	_POLE_PAIR		9
#define	_TOLERANCE		10
#define	_ACCELERATION	11
#define	_HALL			12
#define	_PROTECTION		13
#define	_ERROR			14
#define	_RUN_STATUS		15
#define	_PHASE_COMP		16
#define	_START_DUTY		17
#define	_PCA_DUTY		18
#define	_GPIO			19
#define	_TIMER0			20
#define	_TIMER1			21
#define	_TIMER2			22
#define	_TIMER3			23
#define	_TIMER4			24
#define	_TIMER5			25
#define	_ADC1			26
#define	_ADC2			27
#define	_ADC3			28
#define	_ADC4			29
#define	_CMP1			30
#define	_CMP2			31
#define	_CMP3			32
#define	_CMP4			33
#define	_CMPVTH0		34
#define	_CMPVTH1		35
#define	_VDC			40
#define	_IS				41
#define	_VR				42
#define	_DEADTIME		43

#define	_ALIVE			63

#define	_PROTECTION_OCA		0
#define	_PROTECTION_OCC		1
#define	_PROTECTION_OCX		2
#define	_PROTECTION_LOCK	3
#define	_PROTECTION_HALL	4
#define	_PROTECTION_VDC		5
#define	_PROTECTION_WD		6

#define _NONE			0
#define _STOP			0
#define _ONCE			1
#define _CONTINUOUS		2
#define _START			1
#define _TEST			2
#define _DELAY			0
#define _TIMER			1
#define _TEST_NONE		0
#define _TEST_PWM		1
#define _TEST_SVPWM		2
#define _TEST_SENSORLESS	3
#define _TEST_UART		4
#define _TEST_UVW		5

UINT CalcCheckSum(UINT *pData, UINT len);
void Send_Got_Speed_Cmd(BYTE cmd1, BYTE cmd2);
void Send_Motor_Speed_Cmd(UINT real_speed);
void Send_Motor_Duty_Cmd(BYTE duty);
void Check_Send_Got_Cmd();
void Send_Got_Cmd0(BYTE cmd1, BYTE cmd2, BYTE cmd3);
void Send_Got_Cmd(BYTE cmd1, BYTE cmd2, BYTE cmd3);
void Send_Motor_Error_Cmd(UINT error_number);
void Send_Motor_Parameter_Cmd(BYTE XX, BYTE YY, BYTE ZZ);
void Send_System_Status_Cmd(BYTE XX);
void Send_System_Control_Cmd();
#endif
