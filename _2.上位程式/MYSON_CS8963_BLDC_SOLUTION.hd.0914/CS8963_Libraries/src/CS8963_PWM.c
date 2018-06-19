#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_PWM.h"
#include "CS8963_Function.h"
#include "CS8963_Initial.h"
#include "CS8963_Timer.h"
#include "CS8963_Setup.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function
 * Filename: CS8963_PWM.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/

void Initial_PWM16(unsigned int pwmprd,unsigned char pwmduty)
{
	unsigned int pwm_a = 0;
	unsigned int pwm_b = 0;
	unsigned int pwm_c = 0;
	unsigned long pwmduty_tmp = 0;

	Initial_PAC_IO();

	if(pwmduty > 100)
		pwmduty = 100;

	//printString("Initial PWM_duty=");printd(pwmduty);printString("\n");

	#ifdef USE_NNMOS
	pwmduty_tmp = (unsigned long)pwmprd*(100-pwmduty);
	#elif defined USE_PNMOS
	pwmduty_tmp = pwmprd*pwmduty;
	#else
	printString("MOS Type Unknown\n");
	return;
	#endif

	pwmduty_tmp = pwmduty_tmp/100;

	pwm_a = pwmduty_tmp;
	pwm_b = pwmduty_tmp;
	pwm_c = pwmduty_tmp;

	PWMPRDH = 0x00;											//disable PWM16

	//DT[4:0] : PWM Output Rise Dead Time Delay
	//DT[4:0] = 01000 =>  8  => 1/16M*  8=0.5us
	//DT[4:0] = 11111 => 31 => 1/16M*31=1.94us

	PWM16CFG = PWM_CLOCK_SCALE<<5 | PWM_dead_time;		//PWMCLK = SYSCLK/(PWM_CLOCK_SCALE+1)

	PWMPRDL = (unsigned char)(pwmprd & 0x00ff);				//set PWMPRDH and PWMPRDL
	PWMPRDH = (unsigned char)((pwmprd & 0x7f00)>>8); 			//disable PWM16

	PWMAL = (unsigned char)(pwm_a & 0x00ff);					//the value of PWMA is less than PWMPRD
	PWMAH = ((unsigned char)((pwm_a & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMBL = (unsigned char)(pwm_b & 0x00ff);					//the value of PWMB is less than PWMPRD
	PWMBH = ((unsigned char)((pwm_b & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMCL = (unsigned char)(pwm_c & 0x00ff);					//the value of PWMc is less than PWMPRD
	PWMCH = ((unsigned char)((pwm_c & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWM16INT = 0x40;											//enable zero interrupt

#ifdef USE_PNMOS
	//printString("USE_PNMOS\n");
	PWM16CHS = 0xF1;										//for N outputs inversion
#else	//USE_NNMOS
	//printString("USE_NNMOS\n");

	#if defined(STAR) || defined(STAR_V17)
	PWM16CHS = 0xEC;										//NEMG[1-0]	PEMG[1-0]	EMGF[1-0]	NPOL	PPOL
															//N outputs are forced to 1
															//P outputs are forced to 0
	#else
	PWM16CHS = 0xAC;										//NEMG[1-0]	PEMG[1-0]	EMGF[1-0]	NPOL	PPOL
															//N outputs are forced to 0
															//P outputs are forced to 0
	#endif
#endif

	PWMPRDH = ((unsigned char)((pwmprd & 0x7f00)>>8)) | 0x80;	//turn on PWM16

	PWM16EMG = b11001000;	//EMGEN LATEN CMPAEN

	//#ifdef PWM_TRIGGER_ADC
	PCA_EN = 1;												//use PWM interrupt
	//#endif
}

void Initial_PWM16_Test_Gate_Driver(unsigned int pwmprd, unsigned char pwmdutya, unsigned char pwmdutyb, unsigned char pwmdutyc)
{
	unsigned int pwm_a = 0;
	unsigned int pwm_b = 0;
	unsigned int pwm_c = 0;
	unsigned long pwmduty_tmp = 0;

	Initial_PAC_IO();

	if(pwmdutya > 100)
		pwmdutya = 100;
	if(pwmdutyb > 100)
		pwmdutyb = 100;
	if(pwmdutyc > 100)
		pwmdutyc = 100;

	printString("Initial PWM_dutyA=");printd(pwmdutya);printString(" PWM_dutyB=");printd(pwmdutyb);printString(" PWM_dutyC=");printd(pwmdutyc);printString("\n");

	#ifdef USE_NNMOS
	pwmduty_tmp = (unsigned long)pwmprd*(100-pwmdutya);
	pwm_a = pwmduty_tmp/100;
	pwmduty_tmp = (unsigned long)pwmprd*(100-pwmdutyb);
	pwm_b = pwmduty_tmp/100;
	pwmduty_tmp = (unsigned long)pwmprd*(100-pwmdutyc);
	pwm_c = pwmduty_tmp/100;
	#elif defined USE_PNMOS
	pwmduty_tmp = pwmprd*pwmdutya;
	pwm_a = pwmduty_tmp/100;
	pwmduty_tmp = pwmprd*pwmdutyb;
	pwm_b = pwmduty_tmp/100;
	pwmduty_tmp = pwmprd*pwmdutyc;
	pwm_c = pwmduty_tmp/100;
	#else
	printString("MOS Type Unknown\n");
	return;
	#endif

	PWMPRDH = 0x00;											//disable PWM16

	//DT[4:0] : PWM Output Rise Dead Time Delay
	//DT[4:0] = 01000 =>  8  => 1/16M*  8=0.5us
	//DT[4:0] = 11111 => 31 => 1/16M*31=1.94us

	PWM16CFG = PWM_CLOCK_SCALE<<5 | PWM_dead_time;		//PWMCLK = SYSCLK/(PWM_CLOCK_SCALE+1)

	PWMPRDL = (unsigned char)(pwmprd & 0x00ff);				//set PWMPRDH and PWMPRDL
	PWMPRDH = (unsigned char)((pwmprd & 0x7f00)>>8); 			//disable PWM16

	PWMAL = (unsigned char)(pwm_a & 0x00ff);					//the value of PWMA is less than PWMPRD
	PWMAH = ((unsigned char)((pwm_a & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMBL = (unsigned char)(pwm_b & 0x00ff);					//the value of PWMB is less than PWMPRD
	PWMBH = ((unsigned char)((pwm_b & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMCL = (unsigned char)(pwm_c & 0x00ff);					//the value of PWMc is less than PWMPRD
	PWMCH = ((unsigned char)((pwm_c & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWM16INT = 0x40;											//enable zero interrupt

#ifdef USE_PNMOS
	//printString("USE_PNMOS\n");
	PWM16CHS = 0xF1;										//for N outputs inversion
#else	//USE_NNMOS
	//printString("USE_NNMOS\n");
	PWM16CHS = 0xA0;										//NEMG[1-0]	PEMG[1-0]	EMGF[1-0]	NPOL	PPOL
															//N outputs are forced to 1
															//P outputs are forced to 1
#endif

	PWMPRDH = ((unsigned char)((pwmprd & 0x7f00)>>8)) | 0x80;	//turn on PWM16

	#ifdef PWM_TRIGGER_ADC
	PCA_EN = 1;												//use PWM interrupt
	#endif
}

void PWM16_Modify0(unsigned int pwmprd,unsigned char pwmduty)
{
	unsigned int pwm_a = 0;
	unsigned int pwm_b = 0;
	unsigned int pwm_c = 0;
	unsigned long pwmduty_tmp = 0;

	if(pwmduty > 100)
		pwmduty = 100;
	
	//printString("Modify PWM_duty=");printd(pwmduty);printString("\n");

	#ifdef USE_NNMOS
	pwmduty_tmp = (unsigned long)pwmprd*(100-pwmduty);
	#elif defined USE_PNMOS
	pwmduty_tmp = pwmprd*pwmduty;
	#else
	printString("MOS Type Unknown\n");
	return;
	#endif

	pwmduty_tmp = pwmduty_tmp/100;

	pwm_a = pwmduty_tmp;
	pwm_b = pwmduty_tmp;
	pwm_c = pwmduty_tmp;

	PWMAL = (unsigned char)(pwm_a & 0x00ff);					//the value of PWMA is less than PWMPRD
	PWMAH = ((unsigned char)((pwm_a & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMBL = (unsigned char)(pwm_b & 0x00ff);					//the value of PWMB is less than PWMPRD
	PWMBH = ((unsigned char)((pwm_b & 0xff00)>>8)) & 0x7f;		//IMM = 0

	PWMCL = (unsigned char)(pwm_c & 0x00ff);					//the value of PWMc is less than PWMPRD
	PWMCH = ((unsigned char)((pwm_c & 0xff00)>>8)) & 0x7f;		//IMM = 0
}

void PWM16_Modify(unsigned int pwmprd,unsigned char pwmduty)
{
	unsigned int pwmprd_tmp = pwmprd;
	unsigned char pwmduty_tmp = pwmduty;

	if (slow_modify_speed > 0)
	{
		SETUP_PWM_duty_target(pwmduty_tmp);	//slow
	}
	else
	{
		SETUP_PWM_duty_new(pwmduty_tmp);	//fast
	}
	flag_PWM16_Modify = 1;
}

void PWM16_disable(void)
{
#ifdef USE_NNMOS
	P1_0=0;					//close AP
	#ifdef STAR_V17
	P1_6=0;					//close BP
	#else
	P1_4=0;					//close BP
	#endif
	P3_1=0;					//close CP
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
#elif defined USE_PNMOS
	P1_0=1;					//close AP
	P1_1=0;					//close AN
	P1_4=1;					//close BP
	P1_5=0;					//close BN
	P3_1=1;					//close CP
	P3_0=0;					//close CN
#else
	printString("MOS Type Unknown\n");
#endif
	IOCFGP1_0=PinC_InOutCMOS;  MFCFGP1_0=0x01;
	IOCFGP1_1=PinC_InOutCMOS;  MFCFGP1_1=0x01;
	#ifdef STAR_V17
	IOCFGP1_6=PinC_InOutCMOS;  MFCFGP1_6=0x01;
	IOCFGP1_7=PinC_InOutCMOS;  MFCFGP1_7=0x01;
	#else
	IOCFGP1_4=PinC_InOutCMOS;  MFCFGP1_4=0x01;
	IOCFGP1_5=PinC_InOutCMOS;  MFCFGP1_5=0x01;
	#endif
	IOCFGP3_1=PinC_InOutCMOS;  MFCFGP3_1=0x01;
	IOCFGP3_0=PinC_InOutCMOS;  MFCFGP3_0=0x01;
}

void do_PWM16_Modify(void)
{
	//printString("PWM_duty = ");printd(PWM_duty);
	//printString(" PWM_duty_new = ");printd(PWM_duty_new);
	//printString("\n");
	PWM16_Modify0(PWM_period, PWM_duty_new);
	SETUP_PWM_duty(PWM_duty_new);
}

void check_speed_by_pwm(BYTE type, BYTE amount)
{
	UINT pwmabc = 0;
	BYTE pwmabcl = 0;
	BYTE pwmabch = 0;
	pwmabc = (PWMAH <<8) + PWMAL;

	#ifdef USE_NNMOS

	#elif defined USE_PNMOS
	type = 1 - type;
	#else
	printString("MOS Type Unknown\n");
	return;
	#endif

	if(type == 1)
	{
		//NNMOS speed up, PNMOS speed down
		if(pwmabc > 0)
		{
			if(pwmabc >= amount)
				pwmabc -= amount;
			pwmabcl = (unsigned char)(pwmabc & 0x00ff);					//PWMABC_L
			pwmabch = ((unsigned char)((pwmabc & 0xff00)>>8)) & 0x7f;	//PWMABC_H, IMM = 0
			PWMAL = pwmabcl;
			PWMAH = pwmabch;
			PWMBL = pwmabcl;
			PWMBH = pwmabch;
			PWMCL = pwmabcl;
			PWMCH = pwmabch;
		}
	}
	else
	{
		//NNMOS speed down, PNMOS speed up
		if(pwmabc < (PWM_period+1))
		{
			pwmabc += amount;
			if(pwmabc >= (PWM_period + 1))
				pwmabc = PWM_period + 1;
			if(pwmabc > (400-MINDUTY*4))	//prevent too low duty
				pwmabc = 400-MINDUTY*4;
			pwmabcl = (unsigned char)(pwmabc & 0x00ff);					//PWMABC_L
			pwmabch = ((unsigned char)((pwmabc & 0xff00)>>8)) & 0x7f;	//PWMABC_H, IMM = 0
			PWMAL = pwmabcl;
			PWMAH = pwmabch;
			PWMBL = pwmabcl;
			PWMBH = pwmabch;
			PWMCL = pwmabcl;
			PWMCH = pwmabch;
		}
	}
}
