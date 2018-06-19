/**********************************************************
 * Chips   : CS8963
 * Purpose : backup code, do not need to compile
 * Filename: CS8963_Z.C
 * Author  :
 * Date    : 2016/01/22
 **********************************************************/

#define PWM_FREQ_14K	571
#define PWM_FREQ_15K	533
#define PWM_FREQ_16K	500
#define PWM_FREQ_17K	470
#define PWM_FREQ_18K	444
#define PWM_FREQ_19K	421
#define PWM_FREQ_20K	400
//#define PWM_FREQ_20K	512
#define PWM_FREQ_21K	380
#define PWM_FREQ_22K	363
#define PWM_FREQ_23K	347
#define PWM_FREQ_24K	333
#define PWM_FREQ_25K	320
#define PWM_FREQ_26K	307
#define PWM_FREQ_27K	296
#define PWM_FREQ_28K	285
#define PWM_FREQ_29K	275
#define PWM_FREQ_30K	266
/* matlab code for PWM freq
%FREQ=1/((1/16M)*PERIOD*2)
%=>PERIOD = 8M/FREQ

FREQ=14000:1000:30000
PERIOD=8000000./FREQ;
floor(PERIOD)
*/

CS8963_BLDC.c代刚code

//#define ENABLE_VR_SPEED_TOLERANCE
#define VR_TOLERANCE			10			//percent

	#ifdef ENABLE_VR_SPEED_TOLERANCE
	unsigned int ADC_D_upper = 0;
	unsigned int ADC_D_lower = 0;
	unsigned int ADC_tolerance = 0;
	#endif

					#ifdef ENABLE_VR_SPEED_TOLERANCE

					ADC_tolerance=(unsigned long)(VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)*4096/5/1000*VR_TOLERANCE/100;
					ADC_D_upper=( (unsigned long)(vr_duty_old-VR_SPEED_DUTY_MIN+1) * (VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)+VR_MIN ) *4096/5000 + ADC_tolerance;
					ADC_D_lower=( (unsigned long)(vr_duty_old-VR_SPEED_DUTY_MIN) * (VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)+VR_MIN ) * 4096/5000 - ADC_tolerance;

					/*
					//debug message
					printString("\n");
					printString("vr_duty_new=");printd(vr_duty);printString("  vr_duty_old=");printd(vr_duty_old);printString("\n");
					printString("ADC_tolerance=");printd(ADC_tolerance);printString("   ");
					printString("ADC:0x");printx(ADC_D_result);printS('=');printd(ADC_D_result);printString("\n");
					printString("ADC_upper:0x");printx(ADC_D_upper);printS('=');printd(ADC_D_upper);printString("\n");
					printString("ADC_lower:0x");printx(ADC_D_lower);printS('=');printd(ADC_D_lower);printString("  ");
					*/

					if(vr_duty > vr_duty_old)
					{
						if(ADC_D_result  > ADC_D_upper)
						{
							//printString("  Increase duty......");printd(vr_duty);printString("\n");
							PWM16_Modify(PWM_period, vr_duty);
							vr_duty_old = vr_duty;
						}
					}
					else if(vr_duty < vr_duty_old)
					{
						if(ADC_D_result  < ADC_D_lower)
						{
							//printString("  Decrease duty......");printd(vr_duty);printString("\n");
							PWM16_Modify(PWM_period, vr_duty);
							vr_duty_old = vr_duty;
						}
					}
					#else


	#ifdef SVPWM_DEBUG4
	UINT svpwm_hall_pwm_cnt;
	#endif

	#ifdef SVPWM_DEBUG4

	for(i=0;i<30;i++)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	svpwm_hall_pwm_cnt = 9;
	//printString("pwm_cnt = ");printd(PWM16INT_cnt);printString("  hall_diff = ");printd(svpwm_hall_pwm_cnt);printString("\n");
	Calculate_Change_SVPWM(svpwm_hall_pwm_cnt);
	SETUP_PWMCNT_diff(PWM16INT_cnt, svpwm_hall_pwm_cnt);
	Hal_sta = 6;MT_drive_SVPWM();//printString("\n");

	for(i=0;i<30;i++)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	svpwm_hall_pwm_cnt = 25;
	//printString("pwm_cnt = ");printd(PWM16INT_cnt);printString("  hall_diff = ");printd(svpwm_hall_pwm_cnt);printString("\n");
	Calculate_Change_SVPWM(svpwm_hall_pwm_cnt);
	SETUP_PWMCNT_diff(PWM16INT_cnt, svpwm_hall_pwm_cnt);
	Hal_sta = 4;MT_drive_SVPWM();//printString("\n");


	for(i=0;i<30;i++)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	svpwm_hall_pwm_cnt = 85;
	//printString("pwm_cnt = ");printd(PWM16INT_cnt);printString("  hall_diff = ");printd(svpwm_hall_pwm_cnt);printString("\n");
	Calculate_Change_SVPWM(svpwm_hall_pwm_cnt);
	SETUP_PWMCNT_diff(PWM16INT_cnt, svpwm_hall_pwm_cnt);
	Hal_sta = 5;MT_drive_SVPWM();//printString("\n");

	//Hal_sta = 6;MT_drive_SVPWM();printString("\n");
	//Hal_sta = 4;MT_drive_SVPWM();printString("\n");
	//Hal_sta = 5;MT_drive_SVPWM();printString("\n");
	//Hal_sta = 1;MT_drive_SVPWM();printString("\n");
	//Hal_sta = 3;MT_drive_SVPWM();printString("\n");
	//Hal_sta = 2;MT_drive_SVPWM();printString("\n");
	while(1)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}

	#endif //end of #ifdef SVPWM_DEBUG4

	#if ENABLE_SVPWM == 1

	#ifdef SVPWM_DEBUG
	printString("\n");
	Hal_sta = 2;MT_drive_SVPWM();printString("\n");
	Hal_sta = 6;MT_drive_SVPWM();printString("\n");
	Hal_sta = 4;MT_drive_SVPWM();printString("\n");
	Hal_sta = 5;MT_drive_SVPWM();printString("\n");
	Hal_sta = 1;MT_drive_SVPWM();printString("\n");
	Hal_sta = 3;MT_drive_SVPWM();printString("\n");
	while(1)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	for(m_value=10;m_value<=100;m_value+=10)
	{
		/*
		SETUP_PWM_duty(m_value);
		printString("M=");printd(PWM_duty);printString("\n");
		for(angle=0;angle<=360;angle++)
		{
			angle_tmp = angle;
			get_svpwm_duty(angle);
			PWM16_Setup_Duty(PWM_period, dutyA, dutyB, dutyC);
		}
		*/
		Calculate_SVPWM_Table(m_value);
	}
	while(1)
	{
		DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
	}
	#endif	//end of #ifdef SVPWM_DEBUG
	#endif	//end of #if ENABLE_SVPWM == 1




#define USE_HALL_04_03_02		//default
//#define USE_HALL_23_21_20

#define USE_PWMC_31_30			//default
//#define USE_PWMC_24_25

#define HALL_C_INVERT

	#if ((ENABLE_SVPWM == 1) || (ENABLE_PHASE_COMPENSATION == 1))

	printString("ZZZZZZZZZZZZZZZZZZZZZZZZZ\n");

	#endif


	#ifdef MSK
	PIN_CONFIG_setup_key(_P2_0);	//setup push button K1	SW303
	PIN_CONFIG_setup_key(_P2_1);	//setup push button K2	SW302
	PIN_CONFIG_setup_key(_P2_2);	//setup push button K3	SW301
	PIN_CONFIG_setup_key(_P3_2);	//setup push button K4	SW304
	#endif


	#ifdef MSK
	while(0)		//CM2209B MSK test push button function
	{
		if(P2_0==0)
		{
		 	DelayXms(1);
			if(P2_0==1)
			{
				printString("K1 is pressed. STSP\n");
			}
		}
		else if(P2_1==0)
		{
		 	DelayXms(1);
			if(P2_1==1)
			{
				printString("K2 is pressed. DIRN\n");
			}
		}
		else if(P2_2==0)
		{
		 	DelayXms(1);
			if(P2_2==1)
			{
				printString("K3 is pressed. UP\n");
			}
		}
		else if(P3_2==0)
		{
		 	DelayXms(1);
			if(P3_2==1)
			{
				printString("K4 is pressed. DOWN\n");
			}
		}
	}
	#endif

	while(0)		//CM2209B test push button function
	{
		if(P3_3==0)
		{
		 	DelayXms(1);
			if(P3_3==1)
			{
				printString("K1 is pressed.\n");
			}
		}
		else if(P2_0==0)
		{
		 	DelayXms(1);
			if(P2_0==1)
			{
				printString("K2 is pressed.\n");
			}
		}
	}




void get_current_hall_state()
{
#ifdef USE_HALL_04_03_02
		MFCFGP0_2 = B00000001;
		MFCFGP0_3 = B00000001;
		MFCFGP0_4 = B00000001;
		Hal_sta=((P0&0x1C)>>2);
#elif defined USE_HALL_23_21_20
		MFCFGP2_3 = B00000001;
		MFCFGP2_1 = B00000001;
		MFCFGP2_0 = B00000001;
		Hal_sta=((P2&0x8)>>1) | (P2&0x3);
#endif
		printS(Hal_sta+0x30);
#ifdef USE_HALL_04_03_02
		MFCFGP0_2 = B00000010;
		MFCFGP0_3 = B00000010;
		MFCFGP0_4 = B00000010;
		if(PIOEDGR0)
		{
			PIOEDGR0 &= ~0x1C;
		 	PIOEDGF0 = 0x1C;
		}
		else  if(PIOEDGF0)
		{
			PIOEDGF0 &= ~0x1C;
		 	PIOEDGR0 = 0x1C;
		}
#elif defined USE_HALL_23_21_20
		MFCFGP2_3 = B00000010;
		MFCFGP2_1 = B00000010;
		MFCFGP2_0 = B00000010;
		if(PIOEDGR2)
		{
			PIOEDGR2 &= ~0x0B;
		 	PIOEDGF2 = 0x0B;
		}
		else  if(PIOEDGF2)
		{
			PIOEDGF2 &= ~0x0B;
		 	PIOEDGR2 = 0x0B;
		}
#endif
}



void Initial_IO(void)
{
	//Setup CM2209B VREF signal to CS7211, use P1.7(PIN1)
	P1_7 = 1;
	IOCFGP1_7=PinC_InOutCMOS;  	MFCFGP1_7=0x01;

	//Setup CM2209B TEST signal to CS7211, use P2.7(PIN24)
	IOCFGP2_7=PinC_In;  			MFCFGP2_7=0x01;		//emg

	//Setup CM2209B ITRIP signal from CS7211, use P0.0(PIN18)
	IOCFGP0_0=PinC_In;     		MFCFGP0_0=0x01;

#ifdef USE_HALL_04_03_02
	IOCFGP0_2=PinC_In;			MFCFGP0_2=0x01;		//HALL sensor pin initialized as input IO
	IOCFGP0_3=PinC_In;			MFCFGP0_3=0x01;
	IOCFGP0_4=PinC_In;			MFCFGP0_4=0x01;
#elif defined USE_HALL_23_21_20
	IOCFGP2_3=PinC_In;			MFCFGP2_3=0x01;		//HALL sensor pin initialized as input IO
	IOCFGP2_1=PinC_In;			MFCFGP2_1=0x01;
	IOCFGP2_0=PinC_In;			MFCFGP2_0=0x01;
#endif
}




void Int0_ser(void) interrupt 0
{
	PINT0EN=0;							//disable all PINT0 external interrupt

	if(PINT0F==1)
	{
		Hal_cnt++;
		Hal_cnt_total ++;
		int0_counter++;
		get_hall_ticks++;

		//P1_3 = ~P1_3;		//for debug
		//P1_6 = ~P1_6;		//for debug

#ifdef USE_HALL_04_03_02
 		MFCFGP0_2 = B00000001;
		MFCFGP0_3 = B00000001;
		MFCFGP0_4 = B00000001;

		Hal_sta=((P0&0x1C)>>2);

#elif defined USE_HALL_23_21_20
 		MFCFGP2_3 = B00000001;
		MFCFGP2_1 = B00000001;
		MFCFGP2_0 = B00000001;

		Hal_sta=((P2&0x8)>>1) | (P2&0x3);

#endif
		}
#ifdef USE_HALL_04_03_02
		MFCFGP0_2 = B00000010;
		MFCFGP0_3 = B00000010;
		MFCFGP0_4 = B00000010;
#elif defined USE_HALL_23_21_20
		MFCFGP2_3 = B00000010;
		MFCFGP2_1 = B00000010;
		MFCFGP2_0 = B00000010;
#endif
	 	PINT0F=0;

#ifdef USE_HALL_04_03_02
	if(PIOEDGR0)
	{
		PIOEDGR0 &= ~0x1C;
	 	PIOEDGF0 = 0x1C;
	}
	else  if(PIOEDGF0)
	{
		PIOEDGF0 &= ~0x1C;
	 	PIOEDGR0 = 0x1C;
	}
#elif defined USE_HALL_23_21_20
	if(PIOEDGR2)
	{
		PIOEDGR2 &= ~0x0B;
	 	PIOEDGF2 = 0x0B;
	}
	else  if(PIOEDGF2)
	{
		PIOEDGF2 &= ~0x0B;
	 	PIOEDGR2 = 0x0B;
	}
#endif
	PINT0EN = 1; 						//for PINT0.0	 PINT0.1
}

void Initial_IO(void)
{
/*Initial Hall GPIO*/
#ifdef USE_HALL_04_03_02
#ifdef HALL_C_INVERT
	IOCFGP0_2=0x81;  		MFCFGP0_2=_GPIOEN_;
#else
	IOCFGP0_2=PinC_In;  		MFCFGP0_2=_GPIOEN_;
#endif
	IOCFGP0_3=PinC_In;  		MFCFGP0_3=_GPIOEN_;
	IOCFGP0_4=PinC_In; 		MFCFGP0_4=_GPIOEN_;
#elif defined USE_HALL_23_21_20
#ifdef HALL_C_INVERT
	IOCFGP2_0=0x81;  		MFCFGP2_0=_GPIOEN_;
#else
	IOCFGP2_0=PinC_In;  		MFCFGP2_0=_GPIOEN_;
#endif
	IOCFGP2_1=PinC_In;  		MFCFGP2_1=_GPIOEN_;
	IOCFGP2_3=PinC_In;  		MFCFGP2_3=_GPIOEN_;
#endif
}
#endif

void Initial_EXINT0(void)
{
#ifdef USE_HALL_04_03_02
#ifdef HALL_C_INVERT
	IOCFGP0_2 = 0x81;  MFCFGP0_2 = B00000010;//PINT0  only input
#else
	IOCFGP0_2 = B10000000;  MFCFGP0_2 = B00000010;//PINT0  only input
#endif
	IOCFGP0_3 = B10000000;  MFCFGP0_3 = B00000010;//PINT0  only input
	IOCFGP0_4 = B10000000;  MFCFGP0_4 = B00000010;//PINT0  only input

	PIOEDGR0 = 0x1C; 								// rising  edge at P0_1 bit measn GPIO P0.1
	PINT0EN = 0;  									// enable PINT0EN.1
	PX0 = 1;										// Pin Interrupt INT0 Priority bit.
#elif defined USE_HALL_23_21_20
#ifdef HALL_C_INVERT
	IOCFGP2_0 = 0x81;  MFCFGP2_0 = B00000010;//PINT0  only input
#else
	IOCFGP2_0 = B10000000;  MFCFGP2_0 = B00000010;//PINT0  only input
#endif
	IOCFGP2_3 = B10000000;  MFCFGP2_3 = B00000010;//PINT0  only input
	IOCFGP2_1 = B10000000;  MFCFGP2_1 = B00000010;//PINT0  only input

	PIOEDGR2 = 0x0B; 								// rising  edge at P0_1 bit measn GPIO P0.1
	PINT0EN = 0;  									// enable PINT0EN.1
	//PX0 = 1;										// Pin Interrupt INT0 Priority bit.
#endif
}



void Initial_PAC_IO(void)
{
	IOCFGP1_0=PinC_InOutCMOS;  MFCFGP1_0=0x01;		//PWMAP
	IOCFGP1_1=PinC_InOutCMOS;  MFCFGP1_1=0x01;		//PWMAN
	IOCFGP1_4=PinC_InOutCMOS;  MFCFGP1_4=0x01;		//PWMBP
	IOCFGP1_5=PinC_InOutCMOS;  MFCFGP1_5=0x01;		//PWMBN

#ifdef USE_PWMC_31_30
	IOCFGP3_1=PinC_InOutCMOS;  MFCFGP3_1=0x01;		//PWMCP
	IOCFGP3_0=PinC_InOutCMOS;  MFCFGP3_0=0x01;		//PWMCN
	P3_1=0; 				   //PWMCP close H
#elif defined USE_PWMC_24_25
	IOCFGP2_4=PinC_InOutCMOS;  MFCFGP2_4=0x01;		//PWMCP
	IOCFGP2_5=PinC_InOutCMOS;  MFCFGP2_5=0x01;		//PWMCN
	P2_4=0; 				   //PWMCP close H
#endif

	P1_0=0;				   //PWMAP close H
	P1_4=0;				   //PWMBP close H

	#ifdef CM2209Z2
	P1_1 = 0;				   //close L
	P1_5 = 0;				   //close L
	P3_0 = 0;				   //close L
	#endif

	#ifdef CM2209B
	P1_1 = 0;				   //close L
	P1_5 = 0;				   //close L
	P3_0 = 0;				   //close L
	#endif

	#ifdef CM2209A
	P1_1 = 0;				   //close L
	P1_5 = 0;				   //close L
	#ifdef USE_PWMC_31_30
	P3_0 = 0;				   //close L
	#elif defined USE_PWMC_24_25
	P2_5 = 0;				   //close L
	#endif
	#endif

	IOCFGP1_1 = b00000110;	 									//PWMAN   output,open L,charge
	MFCFGP1_1 = b00100000;	 									//enable PWM16 Channel A negative output

	IOCFGP1_5 = b00000110;	 									//PWMBN   output
	MFCFGP1_5 = b00100000;	 									//enable PWM16 Channel B negative output

	#ifdef USE_PWMC_31_30
	IOCFGP3_0 = b00000110;	 									//PWMCN   output
	MFCFGP3_0 = b00100000;	 									//enable PWM16 Channel C negative output
	#elif defined USE_PWMC_24_25
	IOCFGP2_5 = b00000110;	 									//PWMCN   output
	MFCFGP2_5 = b00100000;	 									//enable PWM16 Channel C negative output
	#endif
}

void MT_drive(unsigned char Hal_sta_tmp)	//UNIPOLAR PWM
{
					#ifdef USE_PWMC_31_30
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					#elif defined USE_PWMC_24_25
					MFCFGP2_4 = Close;  MFCFGP2_5 = Close;	 	//C0
					#endif
}

void MT_Brake(void)
{
	unsigned char i = 0;
	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;
	#ifdef USE_PWMC_31_30
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;
	#elif defined USE_PWMC_24_25
	MFCFGP2_4 = Close;  MFCFGP2_5 = Close;
	#endif

	for(i=0;i<100;i++)
	{
		MT_drive(5);Delay2us(50);
		MT_drive(1);Delay2us(50);
		MT_drive(3);Delay2us(50);
		MT_drive(2);Delay2us(50);
		MT_drive(6);Delay2us(50);
		MT_drive(4);Delay2us(50);
	}

	MFCFGP1_0 = Hopen; MFCFGP1_1 = Close;	 	//A+
	MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	//B-
	#ifdef USE_PWMC_31_30
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
	#elif defined USE_PWMC_24_25
	MFCFGP2_4 = Close;  MFCFGP2_5 = Close;	 	//C0
	#endif

	Delay1s();

	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;
	#ifdef USE_PWMC_31_30
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;
	#elif defined USE_PWMC_24_25
	MFCFGP2_4 = Close;  MFCFGP2_5 = Close;
	#endif
}

void PWM16_disable(void)
{
	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 //A0
	MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 //B0
	#ifdef USE_PWMC_31_30
	MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 //C0
	#elif defined USE_PWMC_24_25
	MFCFGP2_4 = Close;  MFCFGP2_5 = Close;	 //C0
	#endif
}

void Initial_IO(void)
{
	P1_1=0;
	P1_5=0;
	P3_0=0;
	IOCFGP1_1=PinC_InOutCMOS;  	MFCFGP1_1=0x01;
	IOCFGP1_5=PinC_InOutCMOS;  	MFCFGP1_5=0x01;
	IOCFGP3_0=PinC_InOutCMOS;  	MFCFGP3_0=0x01;

	P1_0=0;
	P1_4=0;
	P3_1=0;
	IOCFGP1_0=PinC_InOutCMOS;  	MFCFGP1_0=0x01;
	IOCFGP1_4=PinC_InOutCMOS;  	MFCFGP1_4=0x01;
	IOCFGP3_1=PinC_InOutCMOS;  	MFCFGP3_1=0x01;

/*Initial Hall GPIO*/
#ifdef HALL_C_INVERT
	IOCFGP0_2=0x81;  		MFCFGP0_2=_GPIOEN_;
#else
	IOCFGP0_2=PinC_In;  		MFCFGP0_2=_GPIOEN_;
#endif
	IOCFGP0_3=PinC_In;  		MFCFGP0_3=_GPIOEN_;
	IOCFGP0_4=PinC_In; 		MFCFGP0_4=_GPIOEN_;

	IOCFGP3_3=PinC_In;  	MFCFGP3_3=0x01;		//??key??
}

/*
void I2C_Master1() interrupt 7
{
	static unsigned char i = 0;

	EXIF = 0x00;
	P0_2 = ~P0_2;											    //for test
	if(I2CSST2&0x04)										    //RCBI has been set ?
	{
		sReceive_Tab[i] = I2CSDAT2;							    //receive the data sent by master1
		i++;
		if(i>9)
		{i=0;}
	}
}
*/

/*
const UINT sinetable10000[] = {
0, 175, 349, 523, 698, 872, 1045, 1219, 1392, 1564, 1736, 1908, 2079, 2250, 2419, 2588, 2756, 2924, 3090, 3256, 3420, 3584, 3746, 3907, 4067, 4226, 4384, 4540, 4695, 4848, 5000, 5150, 5299, 5446, 5592, 5736, 5878, 6018, 6157, 6293, 6428, 6561, 6691, 6820, 6947, 7071, 7193, 7314, 7431, 7547, 7660, 7771, 7880, 7986, 8090, 8192, 8290, 8387, 8480, 8572};
const UINT sinetable1000[] = {
0, 17, 35, 52, 70, 87, 105, 122, 139, 156, 174, 191, 208, 225, 242, 259, 276, 292, 309, 326, 342, 358, 375, 391, 407, 423, 438, 454, 469, 485, 500, 515, 530, 545, 559, 574, 588, 602, 616, 629, 643, 656, 669, 682, 695, 707, 719, 731, 743, 755, 766, 777, 788, 799, 809, 819, 829, 839, 848, 857};
*/

/*

U1		A+ B- C-
U2		A+ B+ C-
U3		A- B+ C-
U4		A- B+ C+
U5		A- B- C+
U6		A+ B- C+

U0		A- B- C-
U7		A+ B+ C+


Tpwm=T1+T2+T0=PWM秅戳

琿Α

sector1	uses		U1-U2
PWM_duty_a  T0/2 + T2 + T1		duty_a = (T0/2 + T2 + T1)/Tpwm	
PWM_duty_b  T0/2 + T2			duty_b = (T0/2 + T2 )/Tpwm	い
PWM_duty_c  T0/2			duty_c = (T0/2)/Tpwm		

sector2	uses		U2-U3
PWM_duty_a  T0/2 + T2			duty_a = (T0/2 + T2 )/Tpwm	い
PWM_duty_b  T0/2 + T2 + T1		duty_b = (T0/2 + T2 + T1)/Tpwm	
PWM_duty_c  T0/2			duty_c = (T0/2)/Tpwm		

sector3	uses		U3-U4
PWM_duty_a  T0/2			duty_a = (T0/2)/Tpwm		
PWM_duty_b  T0/2 + T2 + T1		duty_b = (T0/2 + T2 + T1)/Tpwm	
PWM_duty_c  T0/2 + T2			duty_c = (T0/2 + T2 )/Tpwm	い

sector4	uses		U4-U5
PWM_duty_a  T0/2			duty_a = (T0/2)/Tpwm		
PWM_duty_b  T0/2 + T2			duty_b = (T0/2 + T2 )/Tpwm	い
PWM_duty_c  T0/2 + T2 + T1		duty_c = (T0/2 + T2 + T1)/Tpwm	

sector5	uses		U5-U6
PWM_duty_a  T0/2 + T2			duty_a = (T0/2 + T2 )/Tpwm	い
PWM_duty_b  T0/2			duty_b = (T0/2)/Tpwm		
PWM_duty_c  T0/2 + T2 + T1		duty_c = (T0/2 + T2 + T1)/Tpwm	

sector6	uses		U6-U1
PWM_duty_a  T0/2 + T2 + T1		duty_a = (T0/2 + T2 + T1)/Tpwm	
PWM_duty_b  T0/2			duty_b = (T0/2)/Tpwm		
PWM_duty_c  T0/2 + T2			duty_c = (T0/2 + T2 )/Tpwm	い


き琿Α		猭Τ郎

sector1	uses		U1-U2
PWM_duty_a  T2+T1			duty_a = (T2 + T1)/Tpwm		
PWM_duty_b  T2			duty_b = (T2)/Tpwm		い
PWM_duty_c  0				duty_c = 0			

sector2	uses		U2-U3
PWM_duty_a  T2			duty_a = (T2)/Tpwm		い
PWM_duty_b  T2+T1			duty_b = (T2 + T1)/Tpwm		
PWM_duty_c  0				duty_c = 0			

sector3	uses		U3-U4
PWM_duty_a  0				duty_a = 0			
PWM_duty_b  T2+T1			duty_b = (T2 + T1)/Tpwm		
PWM_duty_c  T2			duty_c = (T2)/Tpwm		い

sector4	uses		U4-U5
PWM_duty_a  0				duty_a = 0			
PWM_duty_b  T2			duty_b = (T2)/Tpwm		い
PWM_duty_c  T2+T1			duty_c = (T2 + T1)/Tpwm		

sector5	uses		U5-U6
PWM_duty_a  T2			duty_a = (T2)/Tpwm		い
PWM_duty_b  0				duty_b = 0			
PWM_duty_c  T2+T1			duty_c = (T2 + T1)/Tpwm		

sector6	uses		U6-U1
PWM_duty_a  T2+T1			duty_a = (T2 + T1)/Tpwm		
PWM_duty_b  0				duty_b = 0			
PWM_duty_c  T2			duty_c = (T2)/Tpwm		い



き琿Α   	猭  礚郎	Tpwm=T0+T1+T2

sector1	uses		U1-U2
PWM_duty_a  T0 + T2 + T1		duty_a = (T0 + T2 + T1)/Tpwm = 1
PWM_duty_b  T0 + T2			duty_b = (T0 + T2)/Tpwm		い
PWM_duty_c  T0			duty_c = (T0)/Tpwm		

sector2	uses		U2-U3
PWM_duty_a  T0 + T2			duty_a = (T0 + T2)/Tpwm		い
PWM_duty_b  T0 + T2 + T1		duty_b = (T0 + T2 + T1)/Tpwm = 1
PWM_duty_c  T0			duty_c = (T0)/Tpwm		

sector3	uses		U3-U4
PWM_duty_a  T0			duty_a = (T0)/Tpwm		
PWM_duty_b  T0 + T2 + T1		duty_b = (T0 + T2 + T1)/Tpwm = 1
PWM_duty_c  T0 + T2			duty_c = (T0 + T2)/Tpwm		い

sector4	uses		U4-U5
PWM_duty_a  T0			duty_a = (T0)/Tpwm		
PWM_duty_b  T0 + T2			duty_b = (T0 + T2)/Tpwm		い
PWM_duty_c  T0 + T2 + T1		duty_c = (T0 + T2 + T1)/Tpwm = 1

sector5	uses		U5-U6
PWM_duty_a  T0 + T2			duty_a = (T0 + T2)/Tpwm		い
PWM_duty_b  T0			duty_b = (T0)/Tpwm		
PWM_duty_c  T0 + T2 + T1		duty_c = (T0 + T2 + T1)/Tpwm = 1

sector6	uses		U6-U1
PWM_duty_a  T0 + T2 + T1		duty_a = (T0 + T2 + T1)/Tpwm = 1
PWM_duty_b  T0			duty_b = (T0)/Tpwm		
PWM_duty_c  T0 + T2			duty_c = (T0 + T2)/Tpwm		い

*/

#define USE_UNIPOLAR_PWM
//#define USE_BIPOLAR_PWM


		#ifdef USE_UNIPOLAR_PWM
		printString("    USE_UNIPOLAR_PWM\n");
		#endif
		#ifdef USE_BIPOLAR_PWM
		printString("    USE_BIPOLAR_PWM\n");
		#endif




#ifdef USE_BIPOLAR_PWM
#ifdef CM2209C
void MT_drive(unsigned char Hal_sta_tmp)		//CM2209C BIPOLAR PWM
{
	IOCFGP1_1 = PinC_InOutCMOS; MFCFGP1_1 = 0x01;
	IOCFGP1_5 = PinC_InOutCMOS; MFCFGP1_5 = 0x01;
	IOCFGP3_0 = PinC_InOutCMOS; MFCFGP3_0 = 0x01;
	switch(Hal_sta_tmp)
	{
			case 2:	MFCFGP1_0 = Hopen;	 P1_1=0;
					MFCFGP1_4 = Close;	 P1_5=1;
					MFCFGP3_1 = Close;	 P3_0=0;
					break;
			case 6:	MFCFGP1_0 = Close;	 P1_1=0;
					MFCFGP1_4 = Close;	 P1_5=1;
					MFCFGP3_1 = Hopen;	 P3_0=0;
					break;
			case 4:	MFCFGP1_0 = Close;	 P1_1=1;
					MFCFGP1_4 = Close;	 P1_5=0;
					MFCFGP3_1 = Hopen;	 P3_0=0;
					break;
			case 5:	MFCFGP1_0 = Close;	 P1_1=1;
					MFCFGP1_4 = Hopen;	 P1_5=0;
					MFCFGP3_1 = Close;	 P3_0=0;
					break;
			case 1:	MFCFGP1_0 = Close;	 P1_1=0;
					MFCFGP1_4 = Hopen;	 P1_5=0;
					MFCFGP3_1 = Close;	 P3_0=1;
					break;
			case 3:	MFCFGP1_0 = Hopen;	 P1_1=0;
					MFCFGP1_4 = Close;	 P1_5=0;
					MFCFGP3_1 = Close;	 P3_0=1;
					break;
			default:
					break;
	}

}

void MT_drive_reverse(unsigned char Hal_sta_tmp)	//CM2209C BIPOLAR PWM
{
	IOCFGP1_1 = PinC_InOutCMOS; MFCFGP1_1 = 0x01;
	IOCFGP1_5 = PinC_InOutCMOS; MFCFGP1_5 = 0x01;
	IOCFGP3_0 = PinC_InOutCMOS; MFCFGP3_0 = 0x01;
	switch(Hal_sta_tmp)
	{
			case 5:	MFCFGP1_0 = Hopen;	 P1_1=0;
					MFCFGP1_4 = Close;	 P1_5=1;
					MFCFGP3_1 = Close;	 P3_0=0;
					break;
			case 1:	MFCFGP1_0 = Close;	 P1_1=0;
					MFCFGP1_4 = Close;	 P1_5=1;
					MFCFGP3_1 = Hopen;	 P3_0=0;
					break;
			case 3:	MFCFGP1_0 = Close;	 P1_1=1;
					MFCFGP1_4 = Close;	 P1_5=0;
					MFCFGP3_1 = Hopen;	 P3_0=0;
					break;
			case 2:	MFCFGP1_0 = Close;	 P1_1=1;
					MFCFGP1_4 = Hopen;	 P1_5=0;
					MFCFGP3_1 = Close;	 P3_0=0;
					break;
			case 6:	MFCFGP1_0 = Close;	 P1_1=0;
					MFCFGP1_4 = Hopen;	 P1_5=0;
					MFCFGP3_1 = Close;	 P3_0=1;
					break;
			case 4:	MFCFGP1_0 = Hopen;	 P1_1=0;
					MFCFGP1_4 = Close;	 P1_5=0;
					MFCFGP3_1 = Close;	 P3_0=1;
					break;
			default:
					break;
	}

}
#else
void MT_drive(unsigned char Hal_sta_tmp)	//CM2209ABZ BIPOLAR PWM
{
		switch(Hal_sta_tmp)
		{
			case 2:	MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	//B-
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 6:	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	//B-
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
					break;
			case 4:	MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	//A-
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	//C+
					break;
			case 5:	MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	//A-
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 1:	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	//B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	//C-
					break;
			case 3:	MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	//A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	//C-
					break;
			default:
					printS('F');printS('A');printS('I');printS('L');printS(':');printS(Hal_sta+0x30);
					break;
		}
}

void MT_drive_reverse(unsigned char Hal_sta_tmp)	//CM2209ABZ BIPOLAR PWM
{
	switch(Hal_sta_tmp)
	{
			case 5:	MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	 //A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	 //B-
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 1:	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					MFCFGP1_4 = Close;  MFCFGP1_5 = Lopen;	 //B-
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	 //C+
					break;
			case 3:	MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	 //A-
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;	 	//B0
					MFCFGP3_1 = Hopen;  MFCFGP3_0 = Close;	 //C+
					break;
			case 2:	MFCFGP1_0 = Close;  MFCFGP1_1 = Lopen;	 //A-
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	 //B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Close;	 	//C0
					break;
			case 6:	MFCFGP1_0 = Close;  MFCFGP1_1 = Close;	 	//A0
					MFCFGP1_4 = Hopen;  MFCFGP1_5 = Close;	 //B+
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	 //C-
					break;
			case 4:	MFCFGP1_0 = Hopen;  MFCFGP1_1 = Close;	 //A+
					MFCFGP1_4 = Close;  MFCFGP1_5 = Close;		 //B0
					MFCFGP3_1 = Close;  MFCFGP3_0 = Lopen;	 //C-
					break;
			default:
					printS('F');printS('A');printS('I');printS('L');printS(':');printS(Hal_sta+0x30);
					break;
	}
}
#endif
#endif


	#elif defined CM2209Z1
	IOCFGP2_1=PinC_In;  		MFCFGP2_1=_GPIOEN_;
	IOCFGP2_3=PinC_In;  		MFCFGP2_3=_GPIOEN_;
	#elif defined CM2209Z2
	IOCFGP2_1=PinC_In;  		MFCFGP2_1=_GPIOEN_;
	IOCFGP2_3=PinC_In;  		MFCFGP2_3=_GPIOEN_;


	//printString("CM2209Z2 LV_DEMO_BOARD version 2\n");
	PWM16CHS = 0xF2;										//for N outputs inversion


	#ifdef CM2209Z1
	PIN_CONFIG_setup_key(_P2_2);	//setup push button K4
	PIN_CONFIG_setup_key(_P2_1);	//setup push button K3
	#elif defined CM2209Z2
	PIN_CONFIG_setup_key(_P2_2);	//setup push button K4
	PIN_CONFIG_setup_key(_P2_1);	//setup push button K3


	#ifdef CM2209Z1
	PIN_CONFIG_setup_gpio(_P1_7);	//setup gpio for LED D11
	PIN_CONFIG_setup_gpio(_P1_6);	//setup gpio for LED D12
	PIN_CONFIG_setup_gpio(_P0_5);	//setup gpio for LED D13
	PIN_CONFIG_setup_gpio(_P0_1);	//setup gpio for LED D15
	P0_5 = 1;			 //inversin led
	P1_6 = 1; 			 //foreward led
	P1_7 = 0;			 //power led
	#elif defined CM2209Z2
	PIN_CONFIG_setup_gpio(_P1_7);	//setup gpio for LED D11
	PIN_CONFIG_setup_gpio(_P1_6);	//setup gpio for LED D12
	PIN_CONFIG_setup_gpio(_P0_5);	//setup gpio for LED D13
	PIN_CONFIG_setup_gpio(_P0_1);	//setup gpio for LED D15
	P0_5 = 1;			 //inversin led
	P1_6 = 1; 			 //foreward led
	P1_7 = 0;			 //power led


		if(MtState == stop)
		{
			#ifdef CM2209Z2
			if(P2_1==0)
			{
		 		DelayXms(1);
				if(P2_1==1)
				{
					if(flag_run_dir==0)
					{
						printString("CCW\n");
						flag_run_dir=1;
					}
					else
					{
						printString("CW\n");
						flag_run_dir=0;
					}
					if(flag_phase_compensation_mode)
					{
						if(flag_run_dir==0)
							phase_angle = PHASE_ANGLE_CW;
						else
							phase_angle = PHASE_ANGLE_CCW;
						printString("phase_angle:");printd(phase_angle);printString("\n");
					}
				}
			}
			#endif
		}


CS8963_BLDC.c

	unsigned int PWM_result_sum = 0;
	unsigned int PWM_result[GET_PWM_INPUT_NUMBER] = {0};
	unsigned int PWM_result_index = 0;
	unsigned int PWM_result_average = 0;


	if(flag_speed_control_mode == PWM_INPUT_MODE)
	{
	if(MtState == start)
	{
		cnt2++;
		if((cnt2%PWM_PROBE_SPEED)==0)
		{
			Get_PWM_Input_duty();

			printd(pwm_input_duty);printS(' ');

			PWM_result[PWM_result_index] = pwm_input_duty;
			PWM_result_index++;
			if(PWM_result_index==GET_PWM_INPUT_NUMBER)
				PWM_result_index = 0;

			for(i=0; i<GET_PWM_INPUT_NUMBER; i++)
			{
				PWM_result_sum += PWM_result[i];
			}
			PWM_result_average = PWM_result_sum/GET_PWM_INPUT_NUMBER;

			if(PWM_result_index==0)
			{
				printString("high=");printd(PWM_high_sum);printString(" low=");printd(PWM_low_sum);
				if((!PWM_high_sum)||!PWM_low_sum)
					pwm_input_duty = 0;
				else
					pwm_input_duty = PWM_high_sum*100/(PWM_high_sum+PWM_low_sum);

				PWM_high_sum = 0;
				PWM_low_sum = 0;

				printString(" => get ");
				printd(pwm_input_duty);printS(' ');printString("  => ");

				if(pwm_input_duty<10)
				{
					printString("VR Stop ");get_current_hall_state();printString("\n");
					//SETUP_PWM_duty(10);
					//MtState = stop;
					MtState_vr = stop;
					real_speed = 0;
					PINT0EN = 0;
					PWM16_disable();
				}
				else if(pwm_input_duty_old<10)
				{
					printString("VR Start ");get_current_hall_state();printString("\n");
					SETUP_PWM_duty(PWM_DUTY);
					Initial_PWM16(PWM_period, PWM_duty);					//Initial PWM16
					PWM_duty_old = PWM_DUTY;
					MtState_vr = start;
					PINT0EN = 1;
					if(flag_run_dir==0)
						MT_drive(Hal_sta);
					else
						MT_drive_reverse(Hal_sta);
					if(pwm_input_duty>=80)
						SETUP_PWM_duty(100);
					else
						SETUP_PWM_duty(pwm_input_duty+20);
					PWM16_Modify(PWM_period, PWM_duty);
					//PWM_duty_old  = PWM_duty;
				}
				else
				{
					//printString("duty= ");printd(pwm_input_duty);printString("\n");
					if(pwm_input_duty>=80)
						SETUP_PWM_duty(100);
					else if(pwm_input_duty<10)
						SETUP_PWM_duty(0);
					else
						SETUP_PWM_duty(pwm_input_duty+20);
					PWM16_Modify(PWM_period, PWM_duty);
					//PWM_duty_old  = PWM_duty;
				}
				pwm_input_duty_old = pwm_input_duty;
			}
		}
	}
	}


void Initial_Get_PWM_Input_duty(void)
{
	/*Initial get PWM input duty*/
#ifdef USE_PWM_INPUT_P1_2
	IOCFGP1_2=PinC_In;  	    MFCFGP1_2=_GPIOEN_;
#elif defined USE_PWM_INPUT_P2_4
	IOCFGP2_4=PinC_In;  	    MFCFGP2_4=_GPIOEN_;
#endif
}


void Get_PWM_Input_duty(void)
{
#ifdef ENABLE_PWM_INPUT_MODE
	int i;
	BYTE PWM_input[GET_PWM_INPUT_LENGTH];
	BYTE high = 0;
	BYTE low = 0;
	BYTE start_with_1 = 0;
	BYTE area = 0;

	for(i=0;i<GET_PWM_INPUT_LENGTH;i++)
	{
#ifdef USE_PWM_INPUT_P1_2
		PWM_input[i] = P1_2;
		Delay2us(1);	//for 1KHz
#elif defined USE_PWM_INPUT_P2_4
		PWM_input[i] = P2_4;
		Delay2us(5);	//for 1KHz
#endif
	}

	(PWM_input[0])?(start_with_1=1):(start_with_1=0);

	for(i=1;i<GET_PWM_INPUT_LENGTH;i++)
	{
		if(PWM_input[i]==start_with_1)
		{
			if(area==0)
				continue;
			else if(area==1)
			{
				area=2;
				(start_with_1)?(high++):(low++);
				high++;
			}
			else if(area==2)
			{
				(start_with_1)?(high++):(low++);
			}
		}
		else
		{
			if(area==0)
			{
				area =1;
				(start_with_1)?(low++):(high++);
			}
			if(area==1)
				(start_with_1)?(low++):(high++);
			if(area==2)
				break;
		}
	}
	//printString("high=");printd(high);printString(" low=");printd(low);printString("\n");
	PWM_high_sum += high;
	PWM_low_sum += low;
	if((!high)||(!low))
		pwm_input_duty = 0;
	else
		pwm_input_duty = high*100/(high+low);
#endif
}

#ifdef OUTPUT_SQUARE_WAVE
void PWM_Output_Frequency(unsigned int frequency)
{
	UINT T3H_count;
	if(frequency<200)
	{
		Timer3_Close();
	}
	else
	{
		Initial_Timer3();											//Initial Timer3
		T3H_count = 0xffff-(iSYSCLK/frequency/2);
		T3H_pwm_output = (T3H_count>>8)&0xff;							//Timer 3 count start point
		T3L_pwm_output = (T3H_count)&0xff;
		//printString("T3H_pwm_output=");printx(T3H_pwm_output);printString(" T3L_pwm_output=");printx(T3L_pwm_output);printString("\n");
	}
}
#endif

//#define ENABLE_ADC_WARNING		//use for ADC warning if current too large
#define ADC_WARNING_VALUE			I1300mA

#ifdef ENABLE_ADC_WARNING
	Initial_ADC(SAMPLE_CURRENT_ADC);						//Initial ADC A channel for sample current, pin18
	Get_ADC_Result(SAMPLE_CURRENT_ADC);
	Disable_ADC(SAMPLE_CURRENT_ADC);
	if(ADC_A_result > ADC_WARNING_VALUE)
	{
		printString("ADC WARNING: ADC_instance  = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
		voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;	//mV
		printString("v_out = ");printv(voltage);printString(" V ");
		printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
		printString("sample_current = ");printd(voltage/VOLTAGE_GAIN/RESISTANCE);printString(" mA\n");
	}
#endif

//#define ENABLE_VR_VOLTAGE_AVERAGE
#ifdef ENABLE_VR_VOLTAGE_AVERAGE
unsigned char voltage_index = 0;
unsigned long voltage_instant;
unsigned long voltage_array[10] = 0;
unsigned long voltage_sum = 0;
#endif

	#ifdef ENABLE_VR_VOLTAGE_AVERAGE
	voltage_instant = ((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;	//mV
	//printString("instant=");printd(voltage_instant);printS(' ');
	voltage_array[voltage_index] = voltage_instant;
	voltage_index++;
	if(voltage_index >= 10)
		voltage_index = 0;

	voltage_sum = 0;
	for(i=0; i<10; i++)
		voltage_sum += voltage_array[i];
	//printString("sum=");printd(voltage_sum);printS(' ');
	voltage = voltage_sum/10;
	//printString("average=");printd(voltage);printS(' ');
	#else
	voltage = (UINT)(((unsigned long)ADC_A_result*ADC_FULL*1000)/4096);	//mV
	//printString("VR ");printd(voltage);//printS(' ');
	#endif




//#define ENABLE_TEST_MOTOR_PARAMETERS	//use for test mode, test motor parameters, enable
#define TEST_MOTOR_PARAMETERS_TIMES	30	//use for test mode, measure times
#define MEASURE_SPEED_ST				MINSPEED	//use for test mode, speed start
#define MEASURE_SPEED_SP				MAXSPEED	//use for test mode, speed stop
#define MEASURE_PWM_DUTY_ST			60		//use for test mode, PWM duty start
#define MEASURE_PWM_DUTY_SP			70		//use for test mode, PWM duty stop
#define MEASURE_CURRENT_ST			I200mA	//use for test mode, current start
#define MEASURE_CURRENT_SP			I300mA	//use for test mode, current stop

//#define ENABLE_TEST_MOTOR_START					//use for test mode, test motor start, enable
#define TEST_MOTOR_START_PWM_DUTY	PWM_DUTY		//use for test mode, test motor start pwm_duty
#define TEST_MOTOR_START_SPEED		TARGET_SPEED	//use for test mode, test motor start speed
#endif

#ifdef ENABLE_TEST_MOTOR_START
#define TEST_MOTOR_PERIOD 2000
#define TEST_MOTOR_MEASURE 1800
#define TEST_LENGTH 1
unsigned long Hal_cnt_total_tmp = 0;
unsigned long Hal_cnt_total_old = 0;
ULONG test_motor_start_result[TEST_LENGTH];
#endif

#ifdef ENABLE_TEST_MOTOR_PARAMETERS	//Test Motor Parameters
	unsigned long voltage;
	unsigned int step;
#endif


#ifdef ENABLE_TEST_MOTOR_PARAMETERS	//Test Motor Parameters
		if(flag_mode_type == CLOSE_LOOP)
		{
			step=(MEASURE_SPEED_SP-MEASURE_SPEED_ST)/(TEST_MOTOR_PARAMETERS_TIMES-1);
			//printString("step = ");printd(step);printString("\n");

			timer_counter1++;

			Get_ADC_Result(SAMPLE_CURRENT_ADC);

			if(timer_counter1==TEST_MOTOR_PERIOD)			//1time = 4.1msec
			{
				if(timer_counter2 == (TEST_MOTOR_PARAMETERS_TIMES-2))
					target_speed = MEASURE_SPEED_SP;
				else
					target_speed += step;
				timer_counter1 = 0;
				timer_counter2++;
			}

			if(timer_counter1==TEST_MOTOR_MEASURE)
			{
				printString("\n");
				printString("Target(");printd(timer_counter2+1);printString(")=");printd(target_speed);printString(";");
				printString("Real(");printd(timer_counter2+1);printString(")=");printd(real_speed);printString(";");
				printString("PWM_duty(");printd(timer_counter2+1);printString(")=");printd(PWM_duty);printString(";");

				//instance current
				printString("ADC(");printd(timer_counter2+1);printString(")=");printd(ADC_A_result);printString(";");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;

				printString("v_out(");printd(timer_counter2+1);printString(")=");printv(voltage);printString(";");
				printString("v_in(");printd(timer_counter2+1);printString(")=");printv(voltage/VOLTAGE_GAIN);printString(";");
				printString("sample_current(");printd(timer_counter2+1);printString(")=");printv(voltage*1000/VOLTAGE_GAIN/RESISTANCE);printString(";");
			}

			if(timer_counter2 == TEST_MOTOR_PARAMETERS_TIMES)
			{
				target_speed = TARGET_SPEED;
				PWM_duty = PWM_DUTY;
				Timer3_Close();
				MtState = stop;
				real_speed = 0;
				PINT0EN = 0;
				PWM16_disable();
				printString("\n");
				printString("TEST MOTOR PARAMETERS SP\n");
			}
		}
		else if(flag_mode_type == OPEN_LOOP)
		{
			step=(MEASURE_PWM_DUTY_SP-MEASURE_PWM_DUTY_ST)/(TEST_MOTOR_PARAMETERS_TIMES-1);
			//printString("step = ");printd(step);printString("\n");

			timer_counter1++;

			Get_ADC_Result(SAMPLE_CURRENT_ADC);

			if(timer_counter1==TEST_MOTOR_PERIOD)				//1time = 4.1msec
			{
				if(timer_counter2 == (TEST_MOTOR_PARAMETERS_TIMES-2))
					PWM_duty = MEASURE_PWM_DUTY_SP;
				else
					PWM_duty += step;
				PWM16_Modify(PWM_period, PWM_duty);
				timer_counter1 = 0;
				timer_counter2++;
			}

			if(timer_counter1==TEST_MOTOR_MEASURE)
			{
				printString("\n");
				printString("PWM_duty(");printd(timer_counter2+1);printString(")=");printd(PWM_duty);printString(";");
				printString("Real(");printd(timer_counter2+1);printString(")=");printd(real_speed);printString(";");

				//instance current
				printString("ADC(");printd(timer_counter2+1);printString(")=");printd(ADC_A_result);printString(";");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;

				printString("v_out(");printd(timer_counter2+1);printString(")=");printv(voltage);printString(";");
				printString("v_in(");printd(timer_counter2+1);printString(")=");printv(voltage/VOLTAGE_GAIN);printString(";");
				printString("sample_current(");printd(timer_counter2+1);printString(")=");printv(voltage*1000/VOLTAGE_GAIN/RESISTANCE);printString(";");
			}

			if(timer_counter2 == TEST_MOTOR_PARAMETERS_TIMES)
			{
				target_speed = TARGET_SPEED;
				PWM_duty = PWM_DUTY;
				Timer3_Close();
				MtState = stop;
				real_speed = 0;
				PINT0EN = 0;
				PWM16_disable();
				printString("\n");
				printString("TEST MOTOR PARAMETERS SP\n");
			}
		}
	 	T3H = 0x00;				//Timer 3 count start point
		T3L = 0x00;

#elif defined ENABLE_TEST_MOTOR_START
			if((timer_counter1%5)==4)
				{
				Hal_cnt_total_tmp = Hal_cnt_total;
				test_motor_start_result[timer_counter1/5] = Hal_cnt_total_tmp - Hal_cnt_total_old;
				//printd(timer_counter1/10);printS(' ');printd(Hal_cnt_total);printString("\n");
				Hal_cnt_total_old = Hal_cnt_total_tmp;
				}
			timer_counter1++;
			if((timer_counter1/5) == TEST_LENGTH)
			{
				target_speed = TARGET_SPEED;
				PWM_duty = PWM_DUTY;
				Timer3_Close();
				MtState = stop;
				real_speed = 0;
				PINT0EN = 0;
				PWM16_disable();
				printString("\n");
				printString("TEST MOTOR START SP\n");
			}
	 	T3H = 0x00;				//Timer 3 count start point
		T3L = 0x00;

#elif defined OUTPUT_SQUARE_WAVE
		//printString("T3 ");
		P0_5 = ~P0_5;		//P0_5 should be configured as GPIO
		T3H = T3H_pwm_output;
		T3L = T3L_pwm_output;
#else


#endif
		else if(buffer[0] == 'T')
		{
#ifdef ENABLE_TEST_MOTOR_PARAMETERS	//Test Motor Parameters
			printString("TEST MOTOR PARAMETERS ST   ");

			if(flag_mode_type == CLOSE_LOOP)
			{
				printString("CLOSE LOOP, change target speed.\n");
				target_speed = MINSPEED;
			}
			else if(flag_mode_type == OPEN_LOOP)
			{
				printString("OPEN  LOOP, change PWM duty.\n");
			}
			Disable_Comparator();
			flag_debug_mode = 0;
			flag_over_current_protection = 0;
			flag_lock_rotor_protection = 0;
			SETUP_PWM_duty(PWM_DUTY);
			Initial_PWM16(PWM_period, PWM_DUTY);			//Initial PWM16
			MtState = start;
			PINT0EN = 1;
			if(flag_run_dir==0)
				MT_drive(Hal_sta);
			else
				MT_drive_reverse(Hal_sta);
			Initial_Timer3();										//Initial Timer3
#elif defined ENABLE_TEST_MOTOR_START
			printString("TEST MOTOR START ST   ");

			if(flag_mode_type == CLOSE_LOOP)
			{
				printString("CLOSE LOOP, test target speed.\n");
				target_speed = TEST_MOTOR_START_SPEED;
			}
			else if(flag_mode_type == OPEN_LOOP)
			{
				printString("OPEN  LOOP, test PWM duty.\n");
				PWM_duty = TEST_MOTOR_START_PWM_DUTY;
			}
			Disable_Comparator();
			flag_debug_mode = 0;
			flag_over_current_protection = 0;
			flag_lock_rotor_protection = 0;
			SETUP_PWM_duty(PWM_DUTY);
			Initial_PWM16(PWM_period, PWM_DUTY);			//Initial PWM16
			MtState = start;
			PINT0EN = 1;
			if(flag_run_dir==0)
				MT_drive(Hal_sta);
			else
				MT_drive_reverse(Hal_sta);
			Initial_Timer3();										//Initial Timer3
#else
			printString("Nothing to test.\n");
			printString("You should config test items in Setup.h first.\n");
#endif
		}


#ifdef ENABLE_TEST_MOTOR_START
			printString("Print test motor start result:\n");
			for(i=0;i<TEST_LENGTH;i++)
			{
				printString("total_hal_cnt_diff(");printd(i+1);printString(")=");printd(test_motor_start_result[i]);printString(";\n");
			}
#endif

#ifdef ENABLE_TEST_HALL_SENSOR
			for(i=0;i<TEST_HALL_SENSOR_LENGTH;i++)
			{
				printString("Direction(");printd(i+1);printString(")=");printd(dir[i]);printS(';');
				printString("Hall(");printd(i+1);printString(")=");printd(hall_sequence[i]);printS(';');
				printString("rpm(");printd(i+1);printString(")=");printd(real_speed_array[i]);printS(';');
				printString("One_Hall_Ticks(");printd(i+1);printString(")=");printd(hall_sector_time[i]);printString(";\n");
			}
#endif

#ifdef RECORD_ADC_DATA
			printString("Print ADC test result:\n");
			for(i=0;i<RECORD_ADC_DATA_LENGTH;i++)
			{
				printString("ADC_Result(");printd(i+1);printString(")=");printd(ADC_Result[i]);printString(";\n");
			}
#endif

//#define RECORD_ADC_DATA				//use for ADC recording data
#define RECORD_ADC_DATA_LENGTH	100		//use for ADC recording data length



#ifdef ENABLE_TEST_HALL_SENSOR
#define TEST_HALL_SENSOR_LENGTH 30
#define diff(a,b)	(((a) > (b)) ? (a-b) : (a+0x10000-b))
BYTE dir[TEST_HALL_SENSOR_LENGTH];
BYTE hall_sequence[TEST_HALL_SENSOR_LENGTH];
UINT hall_sector_time[TEST_HALL_SENSOR_LENGTH];
UINT real_speed_array[TEST_HALL_SENSOR_LENGTH];
BYTE hall_sequence_index = 0;
UINT hall_time_new = 0;
UINT hall_time_old = 0;
#endif

#ifdef RECORD_ADC_DATA
UINT ADC_Result_idx = 0;
UINT ADC_Result[RECORD_ADC_DATA_LENGTH];
#endif

#ifdef RECORD_ADC_DATA
	if(MtState == start)
	{
		Initial_ADC(PIN_VRin);
		Get_ADC_Result(PIN_VRin);
		Disable_ADC(PIN_VRin);
		ADC_Result[ADC_Result_idx] = ADC_A_result;
		ADC_Result_idx++;
		if(ADC_Result_idx>=RECORD_ADC_DATA_LENGTH)
			ADC_Result_idx = 0;
	}
#endif



#ifdef ENABLE_TEST_HALL_SENSOR
		dir[hall_sequence_index] = flag_run_dir;
		hall_sequence[hall_sequence_index] = Hal_sta;
		hall_time_new = TH0<<8 | TL0;
		hall_sector_time[hall_sequence_index] = diff(hall_time_new,hall_time_old);
		real_speed_array[hall_sequence_index] = real_speed;
		hall_time_old = hall_time_new;
		hall_sequence_index++;
		if(hall_sequence_index >= TEST_HALL_SENSOR_LENGTH)
			hall_sequence_index = 0;
#endif


#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "CS8963_Phase.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function Phase Compensation
 * Filename: CS8963_Phase.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/
union Wtemp
{
unsigned char tempB[2];			//[0]=0XAA [1]=0XBB
unsigned int tempW;				//0XAABB
};

union Wtemp w_Degree_Delay;

union Wtemp data wd_PWM_duty1;
union Wtemp	data wd_DebugADC1;
union Wtemp data wd_Degree30;
union Wtemp data wd_Degree60;

unsigned int data id_Speed_count=0;
unsigned int data id_Speed_Temp[4]={0,0,0,0};

bit b_motor_speed_stable_FG=0;
bit b_motor_current_stable_FG=0;
unsigned char data cd_phase_switch=1;
unsigned int data id_Motor_RPM=0;

void Phase_Compensation(void)
{
	int i;
	id_Speed_count=0;

	for(i=0;i<4;i++)
	{
		id_Speed_count=id_Speed_count+(id_Speed_Temp[i]>>2);
	}

	if(b_motor_speed_stable_FG==0)
		cd_phase_switch=1;
	else if(id_Motor_RPM<600)
		cd_phase_switch=2;
	else if((id_Motor_RPM>700)&&(id_Motor_RPM<900))
		cd_phase_switch=3;
	else if((id_Motor_RPM>1000)&&(id_Motor_RPM<1300))
		cd_phase_switch=4;
	else if((id_Motor_RPM>1400))
		cd_phase_switch=5;

		// 1=30(degree)  2=15  3=7	 4=3
		//     1+3+4=40
		// 1: 1+3=37
		// 2: 2+3=22
		// 3: 2+4=18

	switch(cd_phase_switch)
	{
		case 1:
			wd_Degree30.tempW=((id_Speed_count>>1)+(id_Speed_count>>3)/*+(id_Speed_count>>4)*/);	//instant closeloop 1+3 or 1+3+4=ok
			break;
		case 2:
			wd_Degree30.tempW=((id_Speed_count>>1)+(id_Speed_count>>3));
			break;
		case 3:
			wd_Degree30.tempW=(id_Speed_count>>1);
			break;
		case 4:
			wd_Degree30.tempW=((id_Speed_count>>2)+(id_Speed_count>>4));
			break;
		case 5:
			wd_Degree30.tempW=((id_Speed_count>>2));
			break;
		default:
			break;
	}

	//1. id_Speed_count=60 degree time
	//2. wd_Degree30=phase lag variable

}



void Initial_Phase_Compensation(void)
{
	int i;
	id_Speed_count=0;

	for(i=0;i<2;i++)
	{
		id_Speed_count=id_Speed_count+(id_Speed_Temp[i]>>1);
	}

	wd_Degree30.tempW=((id_Speed_count>>1)+(id_Speed_count>>3)+(id_Speed_count>>4));	//instant closeloop 1+3 or 1+3+4=ok

	// 1=30(degree)  2=15  3=7	 4=3
	//     1+3+4=40
	// 1: 1+3=37
	// 2: 2+3=22
	// 3: 2+4=18


}


		#ifdef ENABLE_PHASE_COMPENSATION_2
		Phase_Compensation();
		#endif

	#ifdef ENABLE_PHASE_COMPENSATION_2
	printString("Enable Phase Compensation 2\n");
	Initial_Phase_Compensation();
	#endif



//#define USE_MYSON_GUI_v1
//#define USE_MYSON_GUI_v2
//#define USE_ZW_UPPER_MCU_CONTROL

#if defined(USE_MYSON_GUI_v1) || defined(USE_MYSON_GUI_v2)
#define MODE_TYPE				CLOSE_LOOP
#else
#define MODE_TYPE				OPEN_LOOP
#endif



	#ifdef USE_MYSON_GUI_v1
	printString("USE_MYSON_GUI v1\n");
	#elif defined USE_MYSON_GUI_v2
	printString("USE_MYSON_GUI v2\n");
	#endif



#if defined(USE_MYSON_GUI_v1) || defined(USE_MYSON_GUI_v2)
#define BUFFER_LENGTH 600
#define UART_BUF_LENGTH 10
unsigned char gui_cmd_buffer[BUFFER_LENGTH] = 0;
unsigned char gui_cmd_buffer_index = 0;
unsigned char gui_cmd[UART_BUF_LENGTH] = 0;
unsigned char gui_cmd_index = 0;
ULONG PWM16INT_cnt_ST = 0;
unsigned char xdata flag_zero_one = 0x1B;
void CS8963_Send_Sync_To_PC();
UINT CalcCheckSum(UINT *pData, UINT len);
void CS8963_Get_Cmd_Write_Eflash_Data();		// PC祇癳糶戈Eflash
void CS8963_Get_Cmd_Read_Eflash_Data();			// PC祇癳眖Eflash弄戈
void CS8963_Get_Cmd_Update_MotoPara();			// PC祇癳穝皑笷笲锣把计
void CS8963_Get_Cmd_Update_StateMachinePara();	// PC祇癳穝放北呸胯把计
void CS8963_Get_Cmd_Read_Para();				// PC祇癳眖MCU弄把计
void CS8963_Get_Cmd_Write_Para();				// PC祇癳穝把计MCU
#endif
#ifdef USE_MYSON_GUI_v1
#define UART_BUF_LENGTH_1 16
void CS8963_Send_Data_To_PC_v1();
#elif defined USE_MYSON_GUI_v2
#define UART_BUF_LENGTH_2 10
void CS8963_Send_Data_To_PC_v2(BYTE cmd);
#endif



#ifdef USE_MYSON_GUI_v1
void CS8963_Send_Data_To_PC_v1()
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH_1];
	ULONG pwm_duty;
	UINT IAC = 2;

	pwm_duty= (MtState)?0:(PWM_duty * 32768 / 100);

	UartTxBuf[0] = 0x56;
	UartTxBuf[1] = 4;													// System State
	UartTxBuf[2] = (MtState)?0:2;										// MOTORSTATE
	UartTxBuf[3] = 0;													// FAULT_CODE
	UartTxBuf[4] = 0;													// CompProtect
	UartTxBuf[5] = MOTOR_POLE_PAIR;									// MOTOR_POLE_PAIR
	UartTxBuf[6] = ((ULONG)target_speed*MOTOR_POLE_PAIR*10/6) >> 8;	// SET_SPEED_HI
	UartTxBuf[7] = ((ULONG)target_speed*MOTOR_POLE_PAIR*10/6) & 0xFF;	// SET_SPEED_LO
	UartTxBuf[8] = ((ULONG)real_speed*MOTOR_POLE_PAIR*10/6) >> 8;		// REAL_SPEED_HI
	UartTxBuf[9] = ((ULONG)real_speed*MOTOR_POLE_PAIR*10/6) & 0xFF;	// REAL_SPEED_LO
	UartTxBuf[10] = DC_VOLTAGE/2;									// DC_VOLTAGE
	UartTxBuf[11] = AC_VOLTAGE/2;										// AC_VOLTAGE
	UartTxBuf[12] = (MtState)?0:IAC*15;									// IAC	AC_CURRENT
	UartTxBuf[13] = (pwm_duty>>8)&0xff;									// Iq	IQ_CURRENT_H
	UartTxBuf[14] = (pwm_duty>>0)&0xff;									// Iq	IQ_CURRENT_L

	UartTxBuf[15] = CalcCheckSum(UartTxBuf, 15);
	for(i=0;i<UART_BUF_LENGTH_1;i++)
		printS(UartTxBuf[i]);
}
#elif defined USE_MYSON_GUI_v2
void CS8963_Send_Data_To_PC_v2(BYTE cmd)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH_2];

	UartTxBuf[0] = 0x55;
	UartTxBuf[1] = cmd;

	switch(cmd)
	{
	case 0x00:
		UartTxBuf[2] = 123;	//ver
		UartTxBuf[3] = 234;	//serial number
		UartTxBuf[4] = 0;
		UartTxBuf[5] = 0;
		UartTxBuf[6] = 2;	//Magnetic pole pair
		UartTxBuf[7] = 0;	//Control mode 0:auto, 1: manual
		UartTxBuf[8] = 0;
		break;
	case 0x09:
		UartTxBuf[2] = 12/2;
		UartTxBuf[3] = 0;
		UartTxBuf[4] = 0;
		UartTxBuf[5] = 0;
		UartTxBuf[6] = 0;
		UartTxBuf[7] = 0;
		UartTxBuf[8] = 00;
		break;
	case 0x0A:
		UartTxBuf[2] = target_speed/60;
		UartTxBuf[3] = real_speed/60;
		UartTxBuf[4] = 0x00;
		UartTxBuf[5] = 0x01;
		UartTxBuf[6] = 0x01;
		UartTxBuf[7] = 0x00;
		UartTxBuf[8] = 0x01;
		break;
	case 0x0B:
		//UartTxBuf[2] = 1-MtState;	//useless
		UartTxBuf[2] = 0;	//useless
		UartTxBuf[3] = 0;
		UartTxBuf[4] = 0;
		UartTxBuf[5] = 0;
		UartTxBuf[6] = 0;
		UartTxBuf[7] = 0;
		UartTxBuf[8] = 85;	//IPM temperature
		break;
	default:
		break;
	}
	UartTxBuf[9] = CalcCheckSum(UartTxBuf, 9);
	for(i=0;i<UART_BUF_LENGTH_2;i++)
		printS(UartTxBuf[i]);
}
#endif

#if defined(USE_MYSON_GUI_v1) || defined(USE_MYSON_GUI_v2)
void CS8963_Send_Sync_To_PC()
{
	int i;
	UINT UartTxBuf[4];
	UartTxBuf[0] = 0xAB;
	UartTxBuf[1] = 0x01;
	UartTxBuf[2] = 0xcc;
	UartTxBuf[3] = CalcCheckSum(UartTxBuf, 3);

	for(i=0;i<4;i++)
		printS(UartTxBuf[i]);

}

///**************************************************************************
// * ㄧ计CalcCheSun()
// *   璸衡计沮喷㎝
// * 块  计舱璸衡计沮
// * 块  喷㎝8
// *************************************************************************/
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
void CS8963_Get_Cmd_Write_Eflash_Data()			// PC祇癳糶戈Eflash
{
	printString("CS8963_Get_Cmd_Write_Eflash_Data\n");
}
void CS8963_Get_Cmd_Read_Eflash_Data()			// PC祇癳眖Eflash弄戈
{
	printString("CS8963_Get_Cmd_Read_Eflash_Data\n");
}
void CS8963_Get_Cmd_Update_MotoPara()			// PC祇癳穝皑笷笲锣把计
{
	printString("CS8963_Get_Cmd_Update_MotoPara\n");
}
void CS8963_Get_Cmd_Update_StateMachinePara()	// PC祇癳穝放北呸胯把计
{
	printString("CS8963_Get_Cmd_Update_StateMachinePara\n");
}
void CS8963_Get_Cmd_Read_Para()					// PC祇癳眖MCU弄把计
{
	printString("CS8963_Get_Cmd_Read_Para\n");
}
void CS8963_Get_Cmd_Write_Para()				// PC祇癳穝把计MCU
{
	printString("CS8963_Get_Cmd_Write_Para\n");
}
#endif



void UART0_SP(void) interrupt 4
{
#if defined(USE_MYSON_GUI_v1) || defined(USE_MYSON_GUI_v2)
	unsigned char SBUF0_temp;
	int i;
	if(RI0 == 1)
	{
		RI0 = 0;
		//printS('R');
		SBUF0_temp = SBUF0;

		if(SBUF0_temp == 'p')
		{
			printString("Print GUI command:\n");
			for(i=0;i<BUFFER_LENGTH;i++)
			{
				if((gui_cmd_buffer[i] == 0xAA)||(gui_cmd_buffer[i] == 0xAB))
					printString("\n");
				if(gui_cmd_buffer[i] == '_')
					printS('_');
				else
					printx(gui_cmd_buffer[i]);
				printS(' ');
				//if((i%UART_BUF_LENGTH)==(UART_BUF_LENGTH-1))
					//printString("\n");
			}
			printString("\n");
			for(i=0;i<BUFFER_LENGTH;i++)
			{
				gui_cmd_buffer[i] = '_';
			}
			printString("\n");
		}
		else
		{
			if((SBUF0_temp==0xAA)||(SBUF0_temp==0xAB))
				gui_cmd_index = 0;

			gui_cmd_buffer[gui_cmd_buffer_index] = SBUF0_temp;
			gui_cmd[gui_cmd_index] = SBUF0_temp;

			if(gui_cmd_index==0)
			{
				if((SBUF0_temp==0xAA)||(SBUF0_temp==0xAB))		//HEADER OK
				{
					SETUP_PWMCNT_GUI(PWM16INT_cnt);
					gui_cmd_index++;
				}
				else
					gui_cmd_index = 0;
			}
			else
				gui_cmd_index++;

			gui_cmd_buffer_index++;

			if (gui_cmd_index == UART_BUF_LENGTH)
			{
				gui_cmd_index = 0;
				if((gui_cmd[0]==0xAA)&&(gui_cmd[1]==0x20)&&(gui_cmd[2]==0x01)&&(gui_cmd[6]==0x01)&&(gui_cmd[7]==0x00))
				{
					printString("Start Hall: ");get_current_hall_state();printString("\n");
					SETUP_PWM_duty(PWM_DUTY);
					Initial_PWM16(PWM_period, PWM_DUTY);			//Initial PWM16
					MtState = start;
					MtState_vr = start;
					PINT0EN = 1;
					if(flag_run_dir==0)
					{
						MT_drive(Hal_sta);
					}
					else
					{
						MT_drive_reverse(Hal_sta);
					}
				}
				else if((gui_cmd[0]==0xAA)&&(gui_cmd[1]==0x20)&&(gui_cmd[2]==0x01)&&(gui_cmd[6]==0x00)&&(gui_cmd[7]==0x00))
				{
					MtState = stop;
					MtState_vr = stop;
					real_speed = 0;
					PINT0EN = 0;
					PWM16_disable();
					P0_5 = 1;
					P1_6 = 1;
					printString("Stop Hall: ");get_current_hall_state();printString("\n");
					SETUP_target_speed(0);
				}
				else if((gui_cmd[0]==0xAA)&&(gui_cmd[1]==0x20)&&(gui_cmd[2]==0x02))
				{
					if(flag_mode_type == CLOSE_LOOP)
					{
						#ifdef USE_MYSON_GUI_v1
						target_speed = (gui_cmd[5] << 8 | gui_cmd[6]);
						#elif defined USE_MYSON_GUI_v2
						target_speed = (gui_cmd[5] << 8 | gui_cmd[6])*60;
						#endif
						//printString("Target:");printd(target_speed);;printString("\n");
					}
				}
				else if((gui_cmd[0]==0xAB)&&(gui_cmd[1]==0x01)&&(gui_cmd[2]==0xcc))
				{
					CS8963_Send_Sync_To_PC();
				}
				else if((gui_cmd[0]==0xAA)&&(gui_cmd[1]==0x10))
				{
					if((gui_cmd[2]==0x00)||(gui_cmd[2]==0x09)||(gui_cmd[2]==0x0A)||(gui_cmd[2]==0x0B))
						#ifdef USE_MYSON_GUI_v1
						CS8963_Send_Data_To_PC_v1();
						#elif defined USE_MYSON_GUI_v2
						CS8963_Send_Data_To_PC_v2(gui_cmd[2]);
						#endif
				}
				else if((gui_cmd[0]==0xAA)&&(gui_cmd[1]==0xF0))
				{
					if(gui_cmd[2]==0x07)
						CS8963_Get_Cmd_Read_Para();					// PC祇癳眖MCU弄把计
					else if(gui_cmd[2]==0x02)
						CS8963_Get_Cmd_Write_Para();				// PC祇癳穝把计MCU
					else if(gui_cmd[2]==0x03)
						CS8963_Get_Cmd_Write_Eflash_Data();			// PC祇癳糶戈Eflash
					else if(gui_cmd[2]==0x04)
						CS8963_Get_Cmd_Read_Eflash_Data();			// PC祇癳眖Eflash弄戈
					else if(gui_cmd[2]==0x05)
						CS8963_Get_Cmd_Update_MotoPara();			// PC祇癳穝皑笷笲锣把计
					else if(gui_cmd[2]==0x06)
						CS8963_Get_Cmd_Update_StateMachinePara();	// PC祇癳穝放北呸胯把计
				}
			}
		}
	}	 //end if(RI0 == 1)
	else  if(TI0==1)	//Transmit Interrupt Flag bit, CS8963 to computer
	{
		TI0=0;
	}
#else
	unsigned char SBUF0_temp;
	unsigned char Hal_sta_old;
	unsigned char Hal_sta_new;
	unsigned long voltage;
	unsigned long sample_current_0 = 0;



void Send_Motor_Parameter_Test_Cmd();
void Send_Motor_Error_Test_Cmd();
void Send_System_Status_Test_Cmd();




UINT cnt = 0;
UINT speed = 0;
UINT hall_status = 0;
UINT adc_vdc = 0;
UINT adc_is = 0;
UINT adc_vr = 0;

void Send_Motor_Parameter_Test_Cmd()
{
	if(cnt == 0)	//real speed
	{
		speed += 123;
		if(speed >= 3000)
			speed -= 3000;
		speed = 1234;
		Send_Motor_Parameter_Cmd(_REAL_SPEED, (speed>>8)&0xff, speed&0xff);
	}
	else if(cnt == 1)	//target speed
	{
		target_speed += 123;
		if(target_speed >= 3000)
			target_speed -= 3000;
		target_speed = 5678;
		Send_Motor_Parameter_Cmd(_TARGET_SPEED, (target_speed>>8)&0xff, target_speed&0xff);
	}
	else if(cnt == 2)	//max speed
	{
		max_speed += 123;
		if(max_speed >= MAXSPEED)
			max_speed -= MAXSPEED;
		max_speed = 6789;
		Send_Motor_Parameter_Cmd(_MAX_SPEED, (max_speed>>8)&0xff, max_speed&0xff);
	}
	else if(cnt == 3)	//min speed
	{
		min_speed += 123;
		if(min_speed >= MINSPEED)
			min_speed -= MINSPEED;
		min_speed = 1111;
		Send_Motor_Parameter_Cmd(_MIN_SPEED, (min_speed>>8)&0xff, min_speed&0xff);
	}
	else if(cnt == 4)	//pwm svpwm_m
	{
		PWM_duty += 6;
		if(PWM_duty >= 100)
			PWM_duty -= 100;
		PWM_duty = 33;
		Send_Motor_Parameter_Cmd(_DUTY, 0, PWM_duty);
	}
	else if(cnt == 5)	//rpm tolerance
	{
		rpm_tolerance += 7;
		if(rpm_tolerance >= 256)
			rpm_tolerance -= 256;
		rpm_tolerance = 123;
		Send_Motor_Parameter_Cmd(_TOLERANCE, 0, rpm_tolerance);
	}
	else if(cnt == 6)	//acceleration
	{
		acceleration += 9;
		if(acceleration >= 256)
			acceleration -= 256;
		acceleration = 234;
		Send_Motor_Parameter_Cmd(_ACCELERATION, 0, acceleration);
	}
	else if(cnt == 7)	//timer1 TH TL
	{
		Send_Motor_Parameter_Cmd(_TIMER1, 0x12, 0x34);
	}
	else if(cnt == 8)	//ADC VDC
	{
		adc_vdc += 234;
		if(adc_vdc >= 4000)
			adc_vdc -= 4000;
		adc_vdc = 0x123;
		Send_Motor_Parameter_Cmd(_VDC, (adc_vdc>>8)&0xff, adc_vdc&0xff);
	}
	else if(cnt == 9)	//ADC IS
	{
		adc_is += 234;
		if(adc_is >= 4000)
			adc_is -= 4000;
		adc_is = 0x456;
		Send_Motor_Parameter_Cmd(_IS, (adc_is>>8)&0xff, adc_is&0xff);
	}
	else if(cnt == 10)	//ADC VR
	{
		adc_vr += 347;
		if(adc_vr >= 4000)
			adc_vr -= 4000;
		adc_vr = 0x789;
		Send_Motor_Parameter_Cmd(_VR, (adc_vr>>8)&0xff, adc_vr&0xff);
	}
	else if(cnt == 11)	//ADC Hall status
	{
		hall_status++;
		if(hall_status > 6)
			hall_status -= 6;
		Send_Motor_Parameter_Cmd(_HALL, 0, hall_status);
	}
	cnt++;
	if(cnt > 11)
		cnt = 0;
}

UINT eee = 1;
void Send_Motor_Error_Test_Cmd()
{
	Send_Motor_Error_Cmd(eee);
	eee *= 2;
	if(eee > 256)
	{
		Send_Motor_Error_Cmd(0);
		eee = 1;
	}
}

BYTE system_status = 0;
void Send_System_Status_Test_Cmd()
{
	Send_System_Status_Cmd(system_status);
	system_status++;
	if(system_status > 128)
		system_status = 0;
}

//#define ENABLE_PWM_XEMG
#define XEMG_PIN			PIN28
#define XEMG_SELECT			1
//XEMG_SELECT = 0, LOW:  normal, HIGH: xemg
//XEMG_SELECT = 1, HIGH: normal, LOW:  xemg

	#ifdef ENABLE_PWM_XEMG
	PIN_CONFIG_setup_xemg(XEMG_PIN, XEMG_SELECT);				//Initial PWM emergency stop
	#endif

void OverCurrentProtection(void);
#ifdef OVER_CURRENT_PROTECTION_METHOD_1
void OverCurrentProtection(void)
{
	cnt_CurPro++;
	printString("Over Current Protection ");printd(cnt_CurPro);printString(" \n");

	if(cnt_CurPro == OVER_CURRENT_TIME)
	{
		cnt_CurPro = 0;
		printString("Over Current Protection 1    STOP\n");
		PWM_duty = PWM_DUTY;
		target_speed=TARGET_SPEED;
		SETUP_PWM_duty(PWM_duty);
		Initial_PWM16(PWM_period,PWM_duty);
		MtState = stop;
		real_speed = 0;
		PINT0EN = 0;
		PWM16_disable();
	}
}
#elif OVER_CURRENT_PROTECTION_METHOD_2
void OverCurrentProtection(void)
{
		printString("Over Current Protection 2    STOP\n");
		PINT0EN = 0;
		PWM_duty = PWM_DUTY;
		target_speed=TARGET_SPEED;
		SETUP_PWM_duty(PWM_duty);
		Initial_PWM16(PWM_period,PWM_duty);

		PWM16_disable();
		MtState = stop;
		real_speed = 0;
		PINT0EN = 0;
		over_current_cnt = 0;
		ADC_A_result = 0;
}
#endif



#define OVER_CURRENT_PROTECTION_METHOD_1	//over current protection method1
//#define OVER_CURRENT_PROTECTION_METHOD_2	//over current protection method2
//#define OVER_CURRENT_PROTECTION_METHOD_3	//over current protection method3


#define LOCK_ROTOR_PROTECTION_METHOD_1		//lock rotor protection method1



	#ifdef CM2209C
	Initial_ACMP();
	#endif

void Initial_ACMP(void);


void Initial_ACMP(void)
{
	IOCFGP2_7=b00001000;
	MFCFGP2_7=b10000000;

	CMPCFGAB = b00100000;

	CMPVTH0 = 0xe0;
	CMPST =0x00;//clear all-INT flag
}



int step = 0;
int pp_old = 0;
SLONG ii_old = 0;

void do_check_pid()
{
	#ifdef RECORD_PID_DATA
	if(step < DEBUG_LENGTH4)
	#endif
	{
		SINT error = 0;
		SINT pp = 0;
		SLONG ii = 0;
		SLONG dd = 0;
		SLONG pid = 0;

		error = target_speed - real_speed;
		pp = error;
		ii = pp + ii_old;
		dd = pp - pp_old;
		pid = pp*KP/10 + ii*KI/10 + dd*KD/10;

		#ifdef RECORD_PID_DATA
		if(pid_array_index < DEBUG_LENGTH4)
		{
			real_speed_array[pid_array_index] = real_speed;
			pp_array[pid_array_index] = pp;
			ii_array[pid_array_index] = ii;
			dd_array[pid_array_index] = dd;
			pid_array[pid_array_index] = pid;
			pid_array_index++;
		}
		#endif
		if (pid > 0)
			real_speed += number_rpm_step_size;
		else if (pid < 0)
			real_speed -= number_rpm_step_size;

		ii_old = ii;
		pp_old = pp;
		step++;
	}
}


		else if(buffer[0] == 'U')
		{
			printString("TEST MOTOR UVW connections\n");

			if(MtState == start)
			{
					printString("Stop Motor\n");
					MtState = stop;
					real_speed = 0;
					PINT0EN = 0;
					PWM16_disable();
			}

			printString("PWM_duty = 0\n");

			PWM_duty = 0;
			Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
			MT_drive(2);

			for(i=0; i<10; i++)
			{
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				Get_ADC_Result(SAMPLE_CURRENT_ADC);

				printString("ADC_A_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
				printString("v_out = ");printv(voltage);printString(" V ");
				printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
				sample_current_0 = voltage/VOLTAGE_GAIN/RESISTANCE;
				printString("sample_current = ");printd(sample_current_0);printString(" mA\n");
				sample_current_0_avg += sample_current_0;
			}
			sample_current_0_avg /= 10;
			printString("sample_current_0_avg = ");printd(sample_current_0_avg);printString(" mA\n");
			PWM16_disable();


			printString("PWM_duty = 10 MT_drive(1) A0 B+ C-\n");
			PWM_duty = 10;
			Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
			MT_drive(1);

			for(i=0; i<10; i++)
			{
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				Get_ADC_Result(SAMPLE_CURRENT_ADC);

				printString("ADC_A_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
				printString("v_out = ");printv(voltage);printString(" V ");
				printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
				sample_current_1 = voltage/VOLTAGE_GAIN/RESISTANCE;
				printString("sample_current = ");printd(sample_current_1);printString(" mA\n");
				sample_current_1_avg += sample_current_1;
			}
			sample_current_1_avg /= 10;
			printString("sample_current_1_avg = ");printd(sample_current_1_avg);printString(" mA\n");
			PWM16_disable();

			printString("PWM_duty = 10 MT_drive(2) A+ B- C0\n");
			PWM_duty = 10;
			Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
			MT_drive(2);

			for(i=0; i<10; i++)
			{
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				Get_ADC_Result(SAMPLE_CURRENT_ADC);

				printString("ADC_A_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
				printString("v_out = ");printv(voltage);printString(" V ");
				printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
				sample_current_2 = voltage/VOLTAGE_GAIN/RESISTANCE;
				printString("sample_current = ");printd(sample_current_2);printString(" mA\n");
				sample_current_2_avg += sample_current_2;
			}
			sample_current_2_avg /= 10;
			printString("sample_current_2_avg = ");printd(sample_current_2_avg);printString(" mA\n");
			PWM16_disable();

			printString("PWM_duty = 10 MT_drive(3) A+ B0 C-\n");
			PWM_duty = 10;
			Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
			MT_drive(3);

			for(i=0; i<10; i++)
			{
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				Get_ADC_Result(SAMPLE_CURRENT_ADC);

				printString("ADC_A_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
				voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
				printString("v_out = ");printv(voltage);printString(" V ");
				printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
				sample_current_3 = voltage/VOLTAGE_GAIN/RESISTANCE;
				printString("sample_current = ");printd(sample_current_3);printString(" mA\n");
				sample_current_3_avg += sample_current_3;
			}
			sample_current_3_avg /= 10;
			printString("sample_current_3_avg = ");printd(sample_current_3_avg);printString(" mA\n");
			PWM16_disable();

			if(sample_current_1_avg > (sample_current_0_avg*110/100))
			{
				printString("VW connection is OK\n");
				VW_connection_ok = 1;
			}
			else
			{
				printString("VW connection is NG\n");
				VW_connection_ok = 0;
			}
			if(sample_current_2_avg > (sample_current_0_avg*110/100))
			{
				printString("UV connection is OK\n");
				UV_connection_ok = 1;
			}
			else
			{
				printString("UV connection is NG\n");
				UV_connection_ok = 0;
			}
			if(sample_current_3_avg > (sample_current_0_avg*110/100))
			{
				printString("UW connection is OK\n");
				UW_connection_ok = 1;
			}
			else
			{
				printString("UW connection is NG\n");
				UW_connection_ok = 0;
			}

			printString("\n");

			if(VW_connection_ok && UV_connection_ok && UW_connection_ok)
			{
				printString("Connection: U OK, V OK, W OK\n");
			}
			else if(!VW_connection_ok && !UV_connection_ok && !UW_connection_ok)
			{
				printString("Connection: U NG, V NG, W NG\n");
			}
			else if(VW_connection_ok && !UV_connection_ok && !UW_connection_ok)
			{
				printString("Connection: U NG, V OK, W OK\n");
			}
			else if(!VW_connection_ok && UV_connection_ok && !UW_connection_ok)
			{
				printString("Connection: U OK, V OK, W NG\n");
			}
			else if(!VW_connection_ok && !UV_connection_ok && UW_connection_ok)
			{
				printString("Connection: U OK, V NG, W OK\n");
			}
			else
			{
				printString("Connection: U OK, V OK, W OK impossible case.\n");
			}
		}



		if(P3_3==0)
		{
		 	DelayXms(1);
			if(P3_3==1)
			{
				printString("[BLDC]: Key State Change......\n");
				(MtState == start)?(MtState = stop):(MtState = start);
			}
		}

		/*	P2_2, P2_1 move to sensorless debug pin 1,2
			P2.0 move to FG out
		if(P2_0==0)
		{
		 	DelayXms(1);
			if(P2_0==1)
			{
				printString("[BLDC]: Key State Change......\n");
				(MtState == start)?(MtState = stop):(MtState = start);
			}
		}
		else if(P2_1==0)
		{
		 	DelayXms(1);
			if(P2_1==1)
			{
				if(MtState == stop)
				{
					if(flag_run_dir == CW)
					{
						printString("CCW\n");
						flag_run_dir = CCW;
					}
					else
					{
						printString("CW\n");
						flag_run_dir = CW;
					}
				}
			}
		}
		else if(P2_2==0)
		{
		 	DelayXms(1);
			if(P2_2==1)
			{
				if(flag_mode_type == OPEN_LOOP)
				{
					PWM_duty_old  = PWM_duty;
					PWM_duty += 1;
					if(PWM_duty > 100)
						PWM_duty = 100;
					printString("Duty +1, Duty:");printd(PWM_duty);printString("\n");
					PWM16_Modify(PWM_period, PWM_duty);
				}
				else if(flag_mode_type == CLOSE_LOOP)
				{
					target_speed += number_rpm_step_size;
					if(target_speed > MAXSPEED)
						target_speed = MAXSPEED;
					printString("Target + "); printd(number_rpm_step_size);printString(", Target: ");printd(target_speed);printString("\n");
				}
			}
		}
		*/

		else if(P3_2==0)	//MSK
		{
		 	DelayXms(1);
			if(P3_2==1)
			{
				if(flag_mode_type == OPEN_LOOP)
				{
					PWM_duty_old  = PWM_duty;
					if(PWM_duty == 0)
						PWM_duty = 0;
					else
						PWM_duty -= 1;
					printString("Duty -1, Duty:");printd(PWM_duty);printString("\n");
					PWM16_Modify(PWM_period, PWM_duty);
				}
				else if(flag_mode_type == CLOSE_LOOP)
				{
					target_speed -= number_rpm_step_size;
					if(target_speed < MINSPEED)
						target_speed = MINSPEED;
					printString("Target - "); printd(number_rpm_step_size);printString(", Target: ");printd(target_speed);printString("\n");
				}
			}
		}
		#elif defined CM2209D
		/*	P2_2, P2_1 move to sensorless debug pin 1,2
		if(P2_2==0)
		{
		 	DelayXms(1);
			if(P2_2==1)
			{
				(MtState == start)?(MtState = stop):(MtState = start);
			}
		}
		else if(P2_1==0)
		{
		 	DelayXms(1);
			if(P2_1==1)
			{
				if(MtState == stop)
				{
					if(flag_run_dir == CW)
					{
						printString("CCW\n");
						flag_run_dir = CCW;
					}
					else
					{
						printString("CW\n");
						flag_run_dir = CW;
					}
				}
			}
		}
		*/


#ifdef USE_MD5523
#define UART_BUF_LENGTH		4
#else
#define UART_BUF_LENGTH		5
#endif

	  		#ifdef USE_MD5523
		if(flag_check_status == 1)
		{
			flag_check_status = 0;
			if(flag_update_status == 1)
				Send_Motor_Duty_Cmd(PWM_duty);
			else if(flag_update_status == 2)
				Send_Motor_Speed_Cmd(real_speed);
		}
		#endif


#ifdef USE_MD5523
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

void Send_Got_Speed_Cmd(BYTE cmd1, BYTE cmd2)
{
	int i;
	UINT UartTxBuf[UART_BUF_LENGTH];

	UartTxBuf[0] = 0xDD;
	UartTxBuf[1] = cmd1;
	UartTxBuf[2] = cmd2;
	UartTxBuf[3] = CalcCheckSum(UartTxBuf, 3);

	for(i=0;i<UART_BUF_LENGTH;i++)
		printS(UartTxBuf[i]);
}

void Send_Motor_Speed_Cmd(UINT real_speed)
{
	tx2_buf[0] = 0xC1;
	tx2_buf[1] = (real_speed>>8)&0xff;
	tx2_buf[2] = real_speed&0xff;
	tx2_buf[3] = CalcCheckSum(tx2_buf, 3);

	EUART2_Send_4byte();
}

void Send_Motor_Duty_Cmd(BYTE duty)
{
	tx2_buf[0] = 0xC2;
	tx2_buf[1] = 0;
	tx2_buf[2] = duty;
	tx2_buf[3] = CalcCheckSum(tx2_buf, 3);

	EUART2_Send_4byte();
}
#endif

	#ifdef USE_MD5523
	if(flag_update_status > 0)
	{
		if((timer0_check_cnt%16) == 0)
			flag_check_status = 1;
	}
	#endif

#ifdef USE_MD5523
BYTE gui_cmd[UART_BUF_LENGTH] = 0;
BYTE gui_cmd_index = 0;

void EUART2(void) interrupt 6
{
	BYTE SBUF2_temp;
	UINT UartRxBuf[UART_BUF_LENGTH];
	UINT checksum;

	if(EUART2_TIF)							//transmit interrupt
	{
		EUART2_TIF_CLR;
	}

	if(EUART2_RIF)							//receive interrupt
	{
		EUART2_RIF_CLR;
		SBUF2_temp = SBUF2;					//EUART Receive Data

		if(SBUF2_temp == 0xD1)
		{
			if(gui_cmd_index != 0)
				gui_cmd_index = 0;
		}

		gui_cmd[gui_cmd_index] = SBUF2_temp;

		gui_cmd_index++;

		if (gui_cmd_index == UART_BUF_LENGTH)
		{
			gui_cmd_index = 0;
			UartRxBuf[0] = gui_cmd[0];
			UartRxBuf[1] = gui_cmd[1];
			UartRxBuf[2] = gui_cmd[2];
			checksum = CalcCheckSum(UartRxBuf, 3);
			if(gui_cmd[3] != checksum)
			{
				printString("[MD8963]: UART Receive data NG, data: 0x ");
				printx(gui_cmd[0]);printS(' ');
				printx(gui_cmd[1]);printS(' ');
				printx(gui_cmd[2]);printS(' ');
				printx(gui_cmd[3]);
				printString(", checksum = 0x ");
				printx(checksum);
				printString(", Abort...\n");
				return;
			}
			else if(gui_cmd[0] == 0xD1)
			{
				if(gui_cmd[2] == 0)		//STOP
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					if(MtState == start)
					{
						Stop_Motor();
						if(flag_update_status == 1)
							Send_Motor_Duty_Cmd(PWM_duty);
						else if(flag_update_status == 2)
							Send_Motor_Speed_Cmd(real_speed);
						check_speed = 0;
						printString("[MD8963]: Got command: STOP\n");
					}
				}
				else if(gui_cmd[2] == 1)	//START
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					if(MtState == stop)
					{
						printString("[MD8963]: Got command: START\n");
						Start_Motor();
					}
				}
				else if(gui_cmd[2] == 2)	//CW
				{
					if(MtState == stop)
					{
						Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
						printString("[MD8963]: CW\n");
						flag_run_dir = CW;
					}
				}
				else if(gui_cmd[2] == 3)	//CCW
				{
					if(MtState == stop)
					{
						Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
						printString("[MD8963]: CCW\n");
						flag_run_dir = CCW;
					}
				}
				else if(gui_cmd[2] == 4)	//Acceleration
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					if(flag_mode_type == OPEN_LOOP)
					{
						PWM_duty_old  = PWM_duty;
						PWM_duty += 1;
						if(PWM_duty > 100)
							PWM_duty = 100;
						printString("Duty +1, Duty:");printd(PWM_duty);printString("\n");
						PWM16_Modify(PWM_period, PWM_duty);
					}
					else if(flag_mode_type == CLOSE_LOOP)
					{
						target_speed += number_rpm_step_size;
						if(target_speed > MAXSPEED)
							target_speed = MAXSPEED;
						printString("Target + "); printd(number_rpm_step_size);printString(", Target: ");printd(target_speed);printString("\n");
					}
				}
				else if(gui_cmd[2] == 5)	//Deceleration
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					if(flag_mode_type == OPEN_LOOP)
					{
						PWM_duty_old  = PWM_duty;
						if(PWM_duty == 0)
							PWM_duty = 0;
						else
							PWM_duty -= 1;
						printString("Duty -1, Duty:");printd(PWM_duty);printString("\n");
						PWM16_Modify(PWM_period, PWM_duty);
					}
					else if(flag_mode_type == CLOSE_LOOP)
					{
						target_speed -= number_rpm_step_size;
						if(target_speed < MINSPEED)
							target_speed = MINSPEED;
						printString("Target - "); printd(number_rpm_step_size);printString(", Target: ");printd(target_speed);printString("\n");
					}
				}
				else if(gui_cmd[2] == 6)	//Do not update status
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					printString("[MD8963]: Got command: Do Not Update System Status\n");
					flag_update_status = 0;
				}
				else if(gui_cmd[2] == 7)	//Update rpm status
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					printString("[MD8963]: Got command: Update RPM System Status\n");
					flag_update_status = 2;
				}
				else if(gui_cmd[2] == 8)	//Update duty status
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					printString("[MD8963]: Got command: Update Duty System Status\n");
					flag_update_status = 1;
				}
				else if(gui_cmd[2] == 9)	//Reset
				{
					Send_Got_Speed_Cmd(gui_cmd[1], gui_cmd[2]);
					PINT0EN = 0;
					PWM16_disable();
					MtState = stop;
					//target_speed = 0;
					real_speed = 0;
					check_speed = 0;
					printString("[MD8963]: Got command: Reset\n");
					Reset_system();
				}
				else
				{
					printString("[MD8963]: Unknown Command\n");
				}
			}
		}
	}
	SINT2 = 0xa0;	//only EUART2 need use it!!!,other UARTs needn't.
	EA = 1;
}
#else		//USE_MYSONLINK

#endif


flash control code:

#ifdef  FLASH_CONTROL
#define DATA_LENGTH 19
//data from user
BYTE user_header[5]={'N','O','S','Y','M'};
char user_magmetic_pole_pair = -1;
int user_rpm_max = -1;
int user_rpm_min = -1;
int user_rpm = -1;
char user_duty = -1;
int user_current_limit = -1;
int user_current_protection_enable = -1;
int user_current_protection_time = -1;
int user_lock_rotor_protection_enable = -1;
int user_lock_rotor_protection_time = -1;
//data from flash
BYTE para_header[5];
BYTE para_pole_pair;
BYTE para_speed_max[2];
BYTE para_speed_min[2];
BYTE para_speed_normal[2];
BYTE para_duty;
BYTE para_current_limit[2];
BYTE para_current_protection_enable;
BYTE para_current_protection_time;
BYTE para_lock_rotor_protection_enable;
BYTE para_lock_rotor_protection_time;
BYTE total_data[DATA_LENGTH];
void apply_parameters();
void read_data_from_flash();
void write_data_to_flash();
void erase_flash_page63();
#endif	//end of #ifdef  FLASH_CONTROL


			if(buffer[0] == 'w')
			{
				#ifdef  FLASH_CONTROL
				if(buffer[1] == ' ')
				{
					if(buffer[2] == 'h')			//header
					{
						if(length==10)
						{
							user_header[4]=buffer[4];
							user_header[3]=buffer[5];
							user_header[2]=buffer[6];
							user_header[1]=buffer[7];
							user_header[0]=buffer[8];
						}
						else
							printString("Write header error\n");
					}
					else if((buffer[2] == 'm')&&(buffer[3] == 'a')&&(buffer[4] == 'x'))	//motor maximum speed
					{
						if(length==8)
						{
							user_rpm_max=buffer[6]-0x30;
						}
						else if(length==9)
						{
							user_rpm_max=(buffer[6]-0x30)*10 + (buffer[7]-0x30);
						}
						else if(length==10)
						{
							user_rpm_max=(buffer[6]-0x30)*100 + (buffer[7]-0x30)*10 + (buffer[8]-0x30);
						}
						else if(length==11)
						{
							user_rpm_max=(buffer[6]-0x30)*1000 +(buffer[7]-0x30)*100 + (buffer[8]-0x30)*10 + (buffer[9]-0x30);
						}
						else if(length==12)
						{
							user_rpm_max=(buffer[6]-0x30)*10000 +(buffer[7]-0x30)*1000 +(buffer[8]-0x30)*100 + (buffer[9]-0x30)*10 + (buffer[10]-0x30);
						}
						else
							printString("Write maximum speed error\n");
					}
					else if((buffer[2] == 'm')&&(buffer[3] == 'i')&&(buffer[4] == 'n'))	//motor minimum speed
					{
						//printS('_');printS(length+0x30);printS('_');
						if(length==8)
						{
							user_rpm_min=buffer[6]-0x30;
						}
						else if(length==9)
						{
							user_rpm_min=(buffer[6]-0x30)*10 + (buffer[7]-0x30);
						}
						else if(length==10)
						{
							user_rpm_min=(buffer[6]-0x30)*100 + (buffer[7]-0x30)*10 + (buffer[8]-0x30);
						}
						else if(length==11)
						{
							user_rpm_min=(buffer[6]-0x30)*1000 +(buffer[7]-0x30)*100 + (buffer[8]-0x30)*10 + (buffer[9]-0x30);
						}
						else if(length==12)
						{
							user_rpm_min=(buffer[6]-0x30)*10000 +(buffer[7]-0x30)*1000 +(buffer[8]-0x30)*100 + (buffer[9]-0x30)*10 + (buffer[10]-0x30);
						}
						else
							printString("Write minimum speed error\n");
					}
					else if(buffer[2] == 'm')		//magnetic pole pair
					{
						if(length==6)
						{
							user_magmetic_pole_pair=buffer[4]-0x30;
						}
						else if(length==7)
						{
							user_magmetic_pole_pair=(buffer[4]-0x30)*10 + (buffer[5]-0x30);
						}
						else
							printString("Write magnetic pole pair error\n");
					}
					else if((buffer[2] == 'r')&&(buffer[3] == 'p')&&(buffer[4] == 'm'))		//motor speed
					{
						//printS('_');printS(length+0x30);printS('_');
						if(length==8)
						{
							user_rpm=buffer[6]-0x30;
						}
						else if(length==9)
						{
							user_rpm=(buffer[6]-0x30)*10 + (buffer[7]-0x30);
						}
						else if(length==10)
						{
							user_rpm=(buffer[6]-0x30)*100 + (buffer[7]-0x30)*10 + (buffer[8]-0x30);
						}
						else if(length==11)
						{
							user_rpm=(buffer[6]-0x30)*1000 +(buffer[7]-0x30)*100 + (buffer[8]-0x30)*10 + (buffer[9]-0x30);
						}
						else if(length==12)
						{
							user_rpm=(buffer[6]-0x30)*10000 +(buffer[7]-0x30)*1000 +(buffer[8]-0x30)*100 + (buffer[9]-0x30)*10 + (buffer[10]-0x30);
						}
						else
							printString("Write normal speed error\n");
					}
					else if((buffer[2] == 'd')&&(buffer[3] == 'u')&&(buffer[4] == 't')&&(buffer[5] == 'y'))		//duty cycle
					{
						if(length==9)
						{
							user_duty=buffer[7]-0x30;
						}
						else if(length==10)
						{
							user_duty=(buffer[7]-0x30)*10 + (buffer[8]-0x30);
						}
						else
							printString("Write duty cycle error\n");
					}
					else if((buffer[2] == 'c') || (buffer[2] == 'i'))		//current limit in mA
					{
						if(length==6)
						{
							user_current_limit=buffer[4]-0x30;
						}
						else if(length==7)
						{
							user_current_limit=(buffer[4]-0x30)*10 + (buffer[5]-0x30);
						}
						else if(length==8)
						{
							user_current_limit=(buffer[4]-0x30)*100 + (buffer[5]-0x30)*10 + (buffer[6]-0x30);
						}
						else if(length==9)
						{
							user_current_limit=(buffer[4]-0x30)*1000 +(buffer[5]-0x30)*100 + (buffer[6]-0x30)*10 + (buffer[7]-0x30);
						}
						else
							printString("Write maximum current limit error\n");
					}
					else if((buffer[2] == 'u')&&(buffer[3] == 't')&&(buffer[4] == 'i')&&(buffer[5] == 'm')&&(buffer[5] == 'e'))		//current protection time
					{
						if(length==10)
						{
							user_current_protection_time=buffer[8]-0x30;
						}
						else if(length==11)
						{
							user_current_protection_time=(buffer[8]-0x30)*10 + (buffer[9]-0x30);
						}
						else
							printString("Write over current protection time error\n");
					}
					else if(buffer[2] == 'u')		//current protection enable
					{
						if(length==6)
						{
							user_current_protection_enable = buffer[4]-0x30;
						}
						else
							printString("Write over current protection enable error\n");
					}
					else if((buffer[2] == 'o')&&(buffer[3] == 't')&&(buffer[4] == 'i')&&(buffer[5] == 'm')&&(buffer[5] == 'e'))		//lock rotor protection time
					{
						if(length==10)
						{
							user_lock_rotor_protection_time=buffer[8]-0x30;
						}
						else if(length==11)
						{
							user_lock_rotor_protection_time=(buffer[8]-0x30)*10 + (buffer[9]-0x30);
						}
						else
							printString("Write lock rotor protection time error\n");
					}
					else if(buffer[2] == 'o')		//lock rotor protection enable
					{
						if(length==6)
						{
							user_lock_rotor_protection_enable = buffer[4]-0x30;
						}
						else
							printString("Write lock rotor protection enable error\n");
					}
				}
				#endif	//end of #ifdef  FLASH_CONTROL
			}


		if(buffer[0] == 'R')
		{
			#ifdef  FLASH_CONTROL
			read_data_from_flash();
		}
		else if(buffer[0] == 'N')	// print current parameters
		{
			printString("Current data:\n");
			printString("Header: ");
			printS(user_header[4]);
			printS(user_header[3]);
			printS(user_header[2]);
			printS(user_header[1]);
			printS(user_header[0]);
			printString("\n");
			if(user_magmetic_pole_pair != -1)
			{
				printString("Magnetic Pole-pair Number: ");
				printS(user_magmetic_pole_pair+0x30);
				printString("\n");
			}
			if(user_rpm_max != -1)
			{
				printString("Maximum speed: ");
				printS((user_rpm_max/10000)+0x30);
				printS(((user_rpm_max/1000)%10)+0x30);
				printS(((user_rpm_max/100)%10)+0x30); 
				printS(((user_rpm_max/10)%10)+0x30); 
				printS((user_rpm_max%10)+0x30);
				printString("\n");
			}
			if(user_rpm_min != -1)
			{
				printString("Minimum speed: ");
				printS((user_rpm_min/10000)+0x30);
				printS(((user_rpm_min/1000)%10)+0x30);
				printS(((user_rpm_min/100)%10)+0x30); 
				printS(((user_rpm_min/10)%10)+0x30); 
				printS((user_rpm_min%10)+0x30);
				printString("\n");
			}
			if(user_rpm != -1)
			{
				printString("Normal speed: ");
				printS((user_rpm/10000)+0x30);
				printS(((user_rpm/1000)%10)+0x30);
				printS(((user_rpm/100)%10)+0x30); 
				printS(((user_rpm/10)%10)+0x30); 
				printS((user_rpm%10)+0x30);
				printString("\n");
			}
			if(user_duty != -1)
			{
				printString("Normal duty cycle: ");
				printS(((user_duty/10)%10)+0x30); 
				printS((user_duty%10)+0x30);
				printString("\n");
			}
			if(user_current_limit != -1)
			{
				printString("Maximum current limit: ");
				printS((user_current_limit/1000)+0x30);
				printS(((user_current_limit/100)%10)+0x30); 
				printS(((user_current_limit/10)%10)+0x30); 
				printS((user_current_limit%10)+0x30);
				printString(" mA\n");
			}
			if(user_current_protection_enable != -1)
			{
				printString("Over current protection: ");
				printS(user_current_protection_enable+0x30);
				printString("\n");
			}
			if(user_current_protection_time != -1)
			{
				printString("Over current protection time: ");
				printS(((user_current_protection_time/10)%10)+0x30); 
				printS((user_current_protection_time%10)+0x30);
				printString("\n");
			}
			if(user_lock_rotor_protection_enable != -1)
			{
				printString("Lock rotor protection: ");
				printS(user_lock_rotor_protection_enable+0x30);
				printString("\n");
			}
			if(user_lock_rotor_protection_time != -1)
			{
				printString("Lock rotor protection time: ");
				printS(((user_lock_rotor_protection_time/10)%10)+0x30); 
				printS((user_lock_rotor_protection_time%10)+0x30);
				printString("\n");
			}
			printString("End of data.\n");
			#endif	//end of #ifdef  FLASH_CONTROL
		}
		else if(buffer[0] == 'Z')	// erase flash page 63
		{
			#ifdef  FLASH_CONTROL
			erase_flash_page63();
			#endif	//end of #ifdef  FLASH_CONTROL
		}
		else if(buffer[0] == 'W')	// save modified data to flash
		{
			#ifdef  FLASH_CONTROL
			write_data_to_flash();
			#endif	//end of #ifdef  FLASH_CONTROL
		}
		/*
		else if(buffer[0] == 'S')		// apply modified parameters but do not save data to flash
		{
			//apply parameters
			printString("Apply modified parameters but do not save data to flash\n");
			apply_parameters();
		}
		*/
		else if(buffer[0] == 'Q')	// save default values to flash
		{
			#ifdef  FLASH_CONTROL
			printString("Write default values to flash\n");
			Unlock_Flash();
			para_header[4]='M';
			para_header[3]='Y';
			para_header[2]='S';
			para_header[1]='O';
			para_header[0]='N';
			para_pole_pair = 8;
			para_speed_max[1] = MAXSPEED>>8;
			para_speed_max[0] = MAXSPEED%256;
			para_speed_min[1] = MINSPEED>>8;
			para_speed_min[0] = MINSPEED%256;
			para_speed_normal[1] = TARGET_SPEED>>8;
			para_speed_normal[0] = TARGET_SPEED%256;
			para_duty = PWM_START_DUTY;
			para_current_limit[1] = 1200>>8;
			para_current_limit[0] = 1200%256;
			para_current_protection_enable = ENABLE_OVER_CURRENT_PROTECTION_A|(ENABLE_OVER_CURRENT_PROTECTION_C<<1)|(ENABLE_OVER_CURRENT_PROTECTION_X<<2);
			para_current_protection_time = OVER_CURRENT_TIME;
			para_lock_rotor_protection_enable = ENABLE_LOCK_ROTOR_PROTECTION;
			para_lock_rotor_protection_time = LOCK_ROTOR_TIME;
			
			total_data[0]=para_header[4];
			total_data[1]=para_header[3];
			total_data[2]=para_header[2];
			total_data[3]=para_header[1];
			total_data[4]=para_header[0];
			total_data[5]=para_pole_pair;
			total_data[6]=para_speed_max[1];
			total_data[7]=para_speed_max[0];
			total_data[8]=para_speed_min[1];
			total_data[9]=para_speed_min[0];
			total_data[0xA]=para_speed_normal[1];
			total_data[0xB]=para_speed_normal[0];
			total_data[0xC]=para_duty;
			total_data[0xD]=para_current_limit[1];
			total_data[0xE]=para_current_limit[0];
			total_data[0xF]=para_current_protection_enable;
			total_data[0x10]=para_current_protection_time;
			total_data[0x11]=para_lock_rotor_protection_enable;
			total_data[0x12]=para_lock_rotor_protection_time;
			//printString("Erase Flash Page 63\n");
			Erase_Page(0, 0xFC);   //erase one Page(1K Byte) from address 0xFC00
			for(i=0; i<DATA_LENGTH; i++)
			{
				Program_Flash_1Byte(0x00,0xFC,i,total_data[i]);
			}
			Lock_Flash();
			#endif	//end of #ifdef  FLASH_CONTROL
		}



#ifdef FLASH_CONTROL
void apply_parameters()
{
	number_motor_pole_pair = para_pole_pair;
	target_speed = user_rpm;
	PWM_duty = user_duty;
	flag_over_current_protection = para_current_protection_enable;
	flag_lock_rotor_protection = para_lock_rotor_protection_enable;
}

void read_data_from_flash()
{
	int i;
	printString("Read flash page 63 data, ");
	
	Unlock_Flash();
	
	printString("\n");
	printString("RAW data: \n");
	for(i=0; i<=DATA_LENGTH; i++)
	{
		user_header[0] = MainFlash_Read_1BYTE(0x00, 0xFC, i);
		printx(user_header[0]);printS(' ');
	}
	printString("\n");
	
	for(i=0; i<=5; i++)
	{
		user_header[4-i] = MainFlash_Read_1BYTE(0x00, 0xFC, i);
	}
	if((user_header[4]=='M')&&
		(user_header[3]=='Y')&&
		(user_header[2]=='S')&&
		(user_header[1]=='O')&&
		(user_header[0]=='N'))	
	{
		printString("Correct, data:\n");
		user_magmetic_pole_pair = MainFlash_Read_1BYTE(0x00, 0xFC, 5);
		para_speed_max[1] = MainFlash_Read_1BYTE(0x00, 0xFC, 6);
		para_speed_max[0] = MainFlash_Read_1BYTE(0x00, 0xFC, 7);
		user_rpm_max = para_speed_max[1]<<8 | para_speed_max[0];
		para_speed_min[1] = MainFlash_Read_1BYTE(0x00, 0xFC, 8);
		para_speed_min[0] = MainFlash_Read_1BYTE(0x00, 0xFC, 9);
		user_rpm_min = para_speed_min[1]<<8 | para_speed_min[0];
		para_speed_normal[1] = MainFlash_Read_1BYTE(0x00, 0xFC, 0x0a);
		para_speed_normal[0] = MainFlash_Read_1BYTE(0x00, 0xFC, 0x0b);
		user_rpm = para_speed_normal[1]<<8 | para_speed_normal[0];
		user_duty = MainFlash_Read_1BYTE(0x00, 0xFC, 0x0c);
		para_current_limit[1] = MainFlash_Read_1BYTE(0x00, 0xFC, 0x0d);
		para_current_limit[0] = MainFlash_Read_1BYTE(0x00, 0xFC, 0x0e);
		user_current_limit = para_current_limit[1]<<8 | para_current_limit[0];
		user_current_protection_enable = MainFlash_Read_1BYTE(0x00, 0xFC, 0x0f);
		user_current_protection_time = MainFlash_Read_1BYTE(0x00, 0xFC, 0x10);
		user_lock_rotor_protection_enable = MainFlash_Read_1BYTE(0x00, 0xFC, 0x11);
		user_lock_rotor_protection_time = MainFlash_Read_1BYTE(0x00, 0xFC, 0x12);
	}
	else
	{
		printString("No data.  use default values:\n");
		user_header[4] = 'M';
		user_header[3] = 'Y';
		user_header[2] = 'S';
		user_header[1] = 'O';
		user_header[0] = 'N';
		user_magmetic_pole_pair = 8;
		user_rpm_max = MAXSPEED;
		user_rpm_min = MINSPEED;
		user_rpm = TARGET_SPEED;
		user_duty = PWM_START_DUTY;
		user_current_limit = 1200;
		user_current_protection_enable = ENABLE_OVER_CURRENT_PROTECTION_A|(ENABLE_OVER_CURRENT_PROTECTION_C<<1)|(ENABLE_OVER_CURRENT_PROTECTION_X<<2);
		user_current_protection_time = OVER_CURRENT_TIME;
		user_lock_rotor_protection_enable = ENABLE_LOCK_ROTOR_PROTECTION;
		user_lock_rotor_protection_time = LOCK_ROTOR_TIME;
	}
	Lock_Flash();
	
	printString("Header: ");
	printS(user_header[4]);
	printS(user_header[3]);
	printS(user_header[2]);
	printS(user_header[1]);
	printS(user_header[0]);
	printString("\n");
	printString("Magnetic Pole-pair Number: ");
	printS(user_magmetic_pole_pair+0x30);
	printString("\n");
	printString("Maximum speed: ");
	printS((user_rpm_max/10000)+0x30);
	printS(((user_rpm_max/1000)%10)+0x30);
	printS(((user_rpm_max/100)%10)+0x30); 
	printS(((user_rpm_max/10)%10)+0x30); 
	printS((user_rpm_max%10)+0x30);
	printString("\n");
	printString("Minimum speed: ");
	printS((user_rpm_min/10000)+0x30);
	printS(((user_rpm_min/1000)%10)+0x30);
	printS(((user_rpm_min/100)%10)+0x30); 
	printS(((user_rpm_min/10)%10)+0x30); 
	printS((user_rpm_min%10)+0x30);
	printString("\n");
	printString("Normal speed: ");
	printS((user_rpm/10000)+0x30);
	printS(((user_rpm/1000)%10)+0x30);
	printS(((user_rpm/100)%10)+0x30); 
	printS(((user_rpm/10)%10)+0x30); 
	printS((user_rpm%10)+0x30);
	printString("\n");
	printString("Normal duty cycle: ");
	printS(((user_duty/10)%10)+0x30); 
	printS((user_duty%10)+0x30);
	printString("\n");
	printString("Maximum current limit: ");
	printS((user_current_limit/1000)+0x30);
	printS(((user_current_limit/100)%10)+0x30); 
	printS(((user_current_limit/10)%10)+0x30); 
	printS((user_current_limit%10)+0x30);
	printString(" mA\n");
	printString("Over current protection: ");
	printS(user_current_protection_enable+0x30);
	printString("\n");
	printString("Over current protection time: ");
	printS(((user_current_protection_time/10)%10)+0x30); 
	printS((user_current_protection_time%10)+0x30);
	printString("\n");
	printString("Lock rotor protection: ");
	printS(user_lock_rotor_protection_enable+0x30);
	printString("\n");
	printString("Lock rotor protection time: ");
	printS(((user_lock_rotor_protection_time/10)%10)+0x30); 
	printS((user_lock_rotor_protection_time%10)+0x30);
	printString("\n");
}

void write_data_to_flash()
{
	int i;
	printString("Save modified data to flash, also, apply these parameters.\n");
	Unlock_Flash();

	para_header[4]='M';
	para_header[3]='Y';
	para_header[2]='S';
	para_header[1]='O';
	para_header[0]='N';
	para_pole_pair = 8;
	para_speed_max[1] = MAXSPEED>>8;
	para_speed_max[0] = MAXSPEED%256;
	para_speed_min[1] = MINSPEED>>8;
	para_speed_min[0] = MINSPEED%256;
	para_speed_normal[1] = TARGET_SPEED>>8;
	para_speed_normal[0] = TARGET_SPEED%256;
	para_duty = PWM_START_DUTY;
	para_current_limit[1] = 1200>>8;
	para_current_limit[0] = 1200%256;
	para_current_protection_enable = 1;
	para_current_protection_time = 10;
	para_lock_rotor_protection_enable = 1;
	para_lock_rotor_protection_time = 10;

	for(i=0; i<5; i++)	//always write header
	{
		para_header[i]=user_header[i];
	}
	if(user_magmetic_pole_pair != -1)
	{
		para_pole_pair=user_magmetic_pole_pair;
	}
	if(user_rpm_max != -1)
	{
		para_speed_max[1]=user_rpm_max>>8;
		para_speed_max[0]=user_rpm_max%256;
	}
	if(user_rpm_min != -1)
	{
		para_speed_min[1]=user_rpm_min>>8;
		para_speed_min[0]=user_rpm_min%256;
	}
	if(user_rpm != -1)
	{
		para_speed_normal[1]=user_rpm>>8;
		para_speed_normal[0]=user_rpm%256;
	}
	if(user_duty != -1)
	{
		para_duty=user_duty;
	}
	if(user_current_limit != -1)
	{
		para_current_limit[1]=user_current_limit>>8;
		para_current_limit[0]=user_current_limit%256;

	}
	if(user_current_protection_enable != -1)
	{
		para_current_protection_enable=user_current_protection_enable;
	}
	if(user_current_protection_time != -1)
	{
		para_current_protection_time=user_current_protection_time;
	}
	if(user_lock_rotor_protection_enable != -1)
	{
		para_lock_rotor_protection_enable=user_lock_rotor_protection_enable;
	}
	if(user_lock_rotor_protection_time != -1)
	{
		para_lock_rotor_protection_time=user_lock_rotor_protection_time;
	}
	printString("Write modified values to flash\n");
	Unlock_Flash();
	
	total_data[0]=para_header[4];
	total_data[1]=para_header[3];
	total_data[2]=para_header[2];
	total_data[3]=para_header[1];
	total_data[4]=para_header[0];
	total_data[5]=para_pole_pair;
	total_data[6]=para_speed_max[1];
	total_data[7]=para_speed_max[0];
	total_data[8]=para_speed_min[1];
	total_data[9]=para_speed_min[0];
	total_data[0xA]=para_speed_normal[1];
	total_data[0xB]=para_speed_normal[0];
	total_data[0xC]=para_duty;
	total_data[0xD]=para_current_limit[1];
	total_data[0xE]=para_current_limit[0];
	total_data[0xF]=para_current_protection_enable;
	total_data[0x10]=para_current_protection_time;
	total_data[0x11]=para_lock_rotor_protection_enable;
	total_data[0x12]=para_lock_rotor_protection_time;

	//printString("Erase Flash Page 63\n");
	Erase_Page(0, 0xFC);   //erase one Page(1K Byte) from address 0xFC00

	for(i=0; i<DATA_LENGTH; i++)
	{
		Program_Flash_1Byte(0x00,0xFC,i,total_data[i]);
	}
	Lock_Flash();

	printString("Apply parameters\n");
	apply_parameters();
}

void erase_flash_page63()
{
	printString("Erase Flash Page 63\n");
	Unlock_Flash();
	Erase_Page(0, 0xFC);   //erase one Page(1K Byte) from address 0xFC00
	Lock_Flash();
}

#endif	//end of #ifdef  FLASH_CONTROL





sensorless delay mode timer mode code


if(mode2 == _DELAY)		//Delay mode
	{
		printString("Delay mode, Freerun, D:");printd(sensorless_duty);
		printString(", D:");printd(sensorless_delay);
		printString(", R:");printd(sensorless_round);
	}
	else if(mode2 == _TIMER)		//Timer mode
	{
		printString("Timer mode, Freerun, D:");printd(sensorless_duty);
		printString(", T: 0x");printx(TH1_tmp);printx(TL1_tmp);printS('=');printd(TH1_tmp << 8 | TL1_tmp);
		printString(", R:");printd(sensorless_round);
	}
	else 



if(mode2 == _DELAY)		//Delay mode
	{
		printString("\n");
		for (j=0 ; j < 6 ; j++)
		{
			for (i=1 ; i < sensorless_round ; i++)
			{
				if(flag_run_dir == CW)
				{
					Hal_sta_my = 5; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 4; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 6; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 2; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 3; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 1; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
				}
				else		//CCW
				{
					Hal_sta_my = 6; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 4; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 5; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 1; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 3; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 2; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
				}
			}
			if(j == 4)
			{
				if(mode1 == _START)
				{
					//Enable CMP interrupt
					CMPCFGAB = B00001110;					//CMPENA  THSELA  INTENA  POLA  CMPENB  THSELB  INTENB  POLB
					CMPCFGCD = B11101110;					//CMPENC  THSELC  INTENC  POLC  CMPEND  THSELD  INTEND  POLD
					if(flag_run_dir == CW)
					{
						CHECK_FALLING_EDGE;
					}
					else		//CCW
					{
						CHECK_RISING_EDGE;
					}
					CMP_EN = 1;								//Analog Comparator Interrupt and CAN Interrupt Enable bit
				}
			}
		}
		printS('f');
		motor_start = 0;
		mt_drive_cnt = 0;
	}
	else if(mode2 == _TIMER)		//Timer mode
	{
		printString("\n");
		sensorless_mode1 = mode1;
		mt_drive_free_cnt = 0;
		TH1_tmp = (SENSORLESS_TIMER1>>8)&0xff;
		TL1_tmp = SENSORLESS_TIMER1&0xff;
		Initial_Timer1();
	}
	else 

#define SENSORLESS_DUTY_START	20		// D	Motor: VAR2b @ 7.5V
#define SENSORLESS_DELAY		150		// D
#define SENSORLESS_ROUND		5		// R
#define SENSORLESS_TIMER1		0xA000	// T

/*
Motor			voltage	D, D, R		D,T			pair
MOTOR_HENG		7.5V	30,40,5					6	//15,70,5		6
MOTOR_VAR1		7.5V	40,60,4					6
MOTOR_VAR2		7.5V	40,60,4					6
MOTOR_VAR2b		7.5V	40,85,8		40,0xA000	6	//larger capacity 10nF+47nF
MOTOR_WANZHIDA	7.5V	40,60,4					2
MOTOR_WANZHIDA	24V		5,200,5					2
MOTOR_STAR		24V		5,150,3					6
MOTOR_ACARE		7.5V	35,300,100				2
MOTOR_DELTA		7.5V	40,150,4				4
MOTOR_DELTA		24V		10,125,3				4
MOTOR_M1		12V		10,150,5				1

MOTOR_M1		12V		20							Fast mode
*/



BYTE sensorless_duty = SENSORLESS_DUTY_START;
UINT sensorless_delay = SENSORLESS_DELAY;
BYTE sensorless_round = SENSORLESS_ROUND;



#define CHECK_RISING_EDGE	CMPCFGAB = B01101110;CMPCFGCD = B11101110;
#define CHECK_FALLING_EDGE	CMPCFGAB = B01101111;CMPCFGCD = B11111111;


	if(flag_run_dir == CW)
	{
		if((Hal_sta_my == 1) || (Hal_sta_my == 2) || (Hal_sta_my == 4))
		{
			CHECK_RISING_EDGE;
		}
		else
		{
			CHECK_FALLING_EDGE;
		}
	}
	else		//CCW
	{
		if((Hal_sta_my == 1) || (Hal_sta_my == 2) || (Hal_sta_my == 4))
		{
			CHECK_FALLING_EDGE;
		}
		else
		{
			CHECK_RISING_EDGE;
		}
	}





			if(flag_debug_mode)
			{
				if(flag_mode_type == CLOSE_LOOP)
				{
					printString("CLOSE ");
				}
				else if(flag_mode_type == OPEN_LOOP)
				{
					printString("OPEN ");
				}

				if(flag_mode_type == OPEN_LOOP)
				{
					printString("Duty:");
					printd(PWM_duty);
					printS(' ');
					printString("ADC:0x");
					printx(ADC_A_result);
					printS('=');
					printd(ADC_A_result);
					printS(' ');
				}
				else if(flag_mode_type == CLOSE_LOOP)
				{
					printString("Target:");
					printd(target_speed);
					printS(' ');
					printString("ADC:0x");
					printx(ADC_A_result);
					printS('=');
					printd(ADC_A_result);
					printS(' ');
				}
				printString("RPM:");
				printd(real_speed);printS(' ');
				if(flag_run_dir == CW)
					printString("CW");
				else
					printString("CCW");
				printString(" Duty:");printd(PWM_duty);
				printString(" Period: 0x");printx(PWM_period);
				if(flag_lock_rotor_protection)
				{
					printString(" Current: 0x");printx(ADC_A_result);
					printS(' ');
					voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
					printv(voltage);
					printS(' ');
				}
				if((flag_over_current_protection&0x02)==2)
				{
					printS(' ');
					printString("CMP limit: ");
					voltage=((unsigned long)CMPVTH_VALUE*(9/5)*1000)/255;
					printv(voltage);
					printS(' ');
				}
				if(flag_lock_rotor_protection)
				{
					printS(' ');
					printString("ADC limit: ");
					voltage=((unsigned long)OVER_CURRENT_VALUE*ADC_FULL*1000)/4096;
					printv(voltage);
					printS(' ');
				}
				printString("\n");
			}


	if(mode == _DELAY)		//Delay mode
	{
		printString("\n");
		for (j=0 ; j < 6 ; j++)
		{
			for (i=1 ; i < sensorless_round ; i++)
			{
				if(flag_run_dir == CW)
				{
					Hal_sta_my = 5; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 4; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 6; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 2; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 3; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 1; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
				}
				else		//CCW
				{
					Hal_sta_my = 6; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 4; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 5; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 1; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 3; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
					Hal_sta_my = 2; MT_drive(Hal_sta_my);DelayXms(sensorless_delay-j*0);
				}
			}
		}
	}
	else if(mode == _TIMER)		//Timer mode
	{
	}


				else if(xx == _TEST_SENSORLESS)		//SENSORLESS test
				{
					printString("[CS8963]: _TEST_SENSORLESS11111111\n");
					if(flag_sensor_type == AC_MOTOR_MODE)
					{
					if(yy == _STOP)
					{
						//Stop_Motor();
						printString("\n[CS8963]: MysonLink SENSORLESS SP\n");
						Timer1_Close();
						MtState = stop;
						real_speed = 0;
						PWM16_disable();
						motor_start = 1;
					}
					else
					{
						if(zz == _START)
						{
							printString("\n[CS8963]: MysonLink SENSORLESS ST\n");
							start_ac_motor();
						}
						else
						{
							printString("[CS8963]: SENSORLESS unknown mode. abort...\n");
							return;
						}
					}
					}
				}


		else if((buffer[0] == 't')&&(buffer[1] == 'e')&&(buffer[2] == 's')&&(buffer[3] == 't'))
		{
			PINT0EN = 0;
			Timer1_Close();
			printString("\nPCA test\n");

			PCA_use_my_hall = 1;
			mt_drive_free_cnt = 0;

			pca_free_run();

			TH1 = ac_motor_TH1;
			TL1 = ac_motor_TL1;
			Initial_Timer1();		// PCA_MODE

			P1_3 = 0;	//start UVW
		}

				//pca test
				PINT0EN = 0;
				Timer1_Close();
				printString("\nPCA test\n");
	
				PCA_use_my_hall = 1;
				mt_drive_free_cnt = 0;
	
				pca_free_run();
	
				TH1 = ac_motor_TH1;
				TL1 = ac_motor_TL1;
				Initial_Timer1();		// PCA_MODE
	
				P1_3 = 0;	//start UVW





void pca_free_run()
{
	int i;
	PINT0EN = 0;
	Timer1_Close();
	//printString("\nPCA test\n");

	P1_3 = 0;	//start UVW

	for(i = 0; i < 3; i++)
	{
		Hal_sta_my = 6;P2_4 = 1;P2_5 = 1;P2_6 = 0;printd(Hal_sta_my);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		Hal_sta_my = 4;P2_4 = 1;P2_5 = 0;P2_6 = 0;printd(Hal_sta_my);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		Hal_sta_my = 5;P2_4 = 1;P2_5 = 0;P2_6 = 1;printd(Hal_sta_my);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		Hal_sta_my = 1;P2_4 = 0;P2_5 = 0;P2_6 = 1;printd(Hal_sta_my);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		Hal_sta_my = 3;P2_4 = 0;P2_5 = 1;P2_6 = 1;printd(Hal_sta_my);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
		Hal_sta_my = 2;P2_4 = 0;P2_5 = 1;P2_6 = 0;printd(Hal_sta_my);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
			DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);DelayXms(100);
	}
	P1_3 = 1;	//stop UVW
}

void pca_test()
{
	Timer1_Close();
	SETUP_sensor_mode(PCA_MODE);
	Init_PCA_IO();
	//PCA8_Modify(PCA_duty);
	SETUP_PWM_duty(PWM_start_duty);
	PCA8_Modify(PWM_start_duty);
	PIN_CONFIG_setup_gpio(_P1_3);
	PIN_CONFIG_setup_gpio(_P1_2);
	P1_3 = 1;
	P1_2 = 1;
	PIN_CONFIG_setup_gpio(_P2_4);
	PIN_CONFIG_setup_gpio(_P2_5);
	PIN_CONFIG_setup_gpio(_P2_6);
	P2_4 = P0_4;
	P2_5 = P0_3;
	P2_6 = P0_2;
	printString("\nPCA Mode\t");
	printString("PCA duty = ");printd(PWM_start_duty);printString("\n");


	//pca test
	PINT0EN = 0;
	Timer1_Close();
	printString("\nPCA test\n");

	PCA_use_my_hall = 1;
	mt_drive_free_cnt = 0;

	pca_free_run();

	TH1 = ac_motor_TH1;
	TL1 = ac_motor_TL1;
	Initial_Timer1();		// PCA_MODE

	P1_3 = 0;	//start UVW
}

				else if(gui_cmd[3] == 0x33)	//pca get position
				{
					pca_free_run();
				}
				else if(gui_cmd[3] == 0x66)	//pca test
				{
					pca_test();
				}




	if(flag_sensor_type == AC_MOTOR_MODE)
	{
		if(Hal_sta_my == 5)
			if(flag_run_dir == CW)
				Hal_sta_my = 4;
			else
				Hal_sta_my = 1;
		else if(Hal_sta_my == 4)
			if(flag_run_dir == CW)
				Hal_sta_my = 6;
			else
				Hal_sta_my = 5;
		else if(Hal_sta_my == 6)
			if(flag_run_dir == CW)
				Hal_sta_my = 2;
			else
				Hal_sta_my = 4;
		else if(Hal_sta_my == 2)
			if(flag_run_dir == CW)
				Hal_sta_my = 3;
			else
				Hal_sta_my = 6;
		else if(Hal_sta_my == 3)
			if(flag_run_dir == CW)
				Hal_sta_my = 1;
			else
				Hal_sta_my = 2;
		else if(Hal_sta_my == 1)
			if(flag_run_dir == CW)
				Hal_sta_my = 5;
			else
				Hal_sta_my = 3;
	
		MT_drive(Hal_sta_my);

		mt_drive_free_cnt++;
		if(mt_drive_free_cnt % 6 == 0)	//speed up timer every 6 steps
		{
			if(ac_motor_TH1 > 0xd0)
			{
				ac_motor_TH1 = 0xd2;
			}
			else
			{
				ac_motor_TH1 += 0x02;
			}
		}
		TH1 = ac_motor_TH1;
		TL1 = ac_motor_TL1;
	}


			else if(flag_sensor_type == AC_MOTOR_MODE)
			{
				//real_speed = (Hal_cnt*10*60)/(6*number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				//real_speed = (Hal_cnt*10*10)/(number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				real_speed = (mt_drive_cnt*101)/(number_motor_pole_pair);	//(Hal_cnt*10*60)/(6*POLE_PAIR)		rpm
				mt_drive_cnt = 0;
				if(motor_start == 1)
				{
					if(real_speed > MINSPEED)
						motor_start = 0;
				}
				//printS('r');printd(real_speed);printS('d');printd(PWM_duty);printS(' ');
			}


void start_ac_motor()
{
	printString("AC Motor mode, D:");printd(PWM_duty);
	printString(", T: 0x");printx(ac_motor_TH1);printx(ac_motor_TL1);printS('=');printd(ac_motor_TH1 << 8 | ac_motor_TL1);
	if(flag_run_dir == CW)
		printString(", CW\n");
	else
		printString(", CCW\n");
	Initial_PWM16(PWM_period, PWM_duty);			//Initial PWM16
	TH1 = ac_motor_TH1;
	TL1 = ac_motor_TL1;
	Initial_Timer1();		// AC_MOTOR_MODE
}



	//PCA_EN = 1;												//use PWM interrupt










void SETUP_engineering_mode(unsigned char engineering_mode);


			if(flag_engineering_mode)
			{
				printString("case 1.  A0  B+  C-   PWM duty = ");printd(PWM_duty);printString("\n");

				SETUP_PWM_duty(PWM_duty);
				PWM16_Modify(PWM_period, PWM_duty);
				MT_drive(1);
				while(1)
				{
					Get_ADC_Result(SAMPLE_CURRENT_ADC);
					printString("ADC_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
					voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
					printString("v_out = ");printv(voltage);printString(" V ");
					printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
					printString("sample_current = ");printd(voltage/VOLTAGE_GAIN/RESISTANCE);printString(" mA\n");
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
			}


			if(flag_engineering_mode)
			{
				printString("case 2.  A+  B-  C0   PWM duty = ");printd(PWM_duty);printString("\n");

				SETUP_PWM_duty(PWM_duty);
				PWM16_Modify(PWM_period, PWM_duty);
				MT_drive(2);
				while(1)
				{
					Get_ADC_Result(SAMPLE_CURRENT_ADC);
					printString("ADC_instance = 0x");printx(ADC_A_result);printString(" = ");printd(ADC_A_result);printString(" ");
					voltage=((unsigned long)ADC_A_result*ADC_FULL*1000)/4096;
					printString("v_out = ");printv(voltage);printString(" V ");
					printString("v_in  = ");printv(voltage/VOLTAGE_GAIN);printString(" V ");
					printString("sample_current = ");printd(voltage/VOLTAGE_GAIN/RESISTANCE);printString(" mA\n");
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
					DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);DelayXms(200);
				}
			}
			else
			{



old
	if(PIOEDGR0)
	{
		PIOEDGR0 &= ~0x1C;
		PIOEDGF0 = 0x1C;
	}
	else if(PIOEDGF0)
	{
		PIOEDGF0 &= ~0x1C;
		PIOEDGR0 = 0x1C;
	}
new
	PIOEDGR0 &= ~0x1C;
	PIOEDGF0 &= ~0x1C;
	PIOEDGR0 = 0x1C;
	PIOEDGF0 = 0x1C;




