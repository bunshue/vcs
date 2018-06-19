#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "CS8963_UART.h"
#include "CS8963_Setup.h"
#include "CS8963_Function.h"
#include "CS8963_PWM.h"
#include "Setup.h"
#include "Setup_function.h"

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function
 * Filename: CS8963_Function.C
 * Author  :
 * Date    : 2015/01/13
 **********************************************************/

void Reset_system(void)
{
	PINT0EN = 0;
	PWM16_disable();
	MtState = stop;
	target_speed = 0;
	printString("[CS8963]: RESET\n");
	TA=0xAA;
	TA=0x55;
	WDCON = 0x01;			//reset watchdog timer
	TA=0x00;
	WDCON = 0x02;			//WDIF WTRF EWT RWT
	CKCON &= ~0xC7;
}

void Delay1s(void)
{
	unsigned char i,j,k;
 	for(i=0;i<100;i++)
	 	for(j=0;j<100;j++)
			for(k=0;k<16;k++)
				;
}

void DelayXms2(unsigned char delay )
{
	unsigned char i,j;
 	for(i=0;i<delay;i++)
		for(j=0;j<30;j++)
			;
}

void DelayXms(UINT delay)
{
	int i,j;
 	for(i=0;i<delay;i++)
		for(j=0;j<100;j++)
			;
}

void DelayYms(void)
{
	int j;
	for(j=0;j<10;j++)
		;
}

void Delay2us(unsigned char delay)
{
	unsigned char k;

  	for(k=0;k<delay;k++)
		;
}

void DelayNticks(unsigned int ticks)
{
	unsigned int k;
  	for(k=0;k<ticks;k++)
		;
}

void printS2(unsigned char p)
{
	UART1_Send_1byte(p);
}

void printS(unsigned char p)
{
#ifdef NO_PRINT_WHEN_RUNNING
	if(MtState == stop)
#endif
		UART1_Send_1byte(p);
}

void printS_UART(unsigned char p)
{
	ES0 = 0;
	SBUF0 = p;
	while (!TI0);
	TI0 = 0;
	ES0 = 1;
}

void printString2(unsigned char* p)
{
	int len=0;
	while(1)
	{
		if(p[len]=='\0')
			break;
		if(p[len]=='\n')
		{
			printS2(0x0a);printS(0x0d);
		}
		else
		{
			printS2(p[len]);
		}
		len++;
	}
}

void printString(unsigned char* p)
{
	int len=0;
#ifdef NO_PRINT_WHEN_RUNNING
	if(MtState == stop)
#endif
	{
	while(1)
	{
		if(p[len]=='\0')
			break;
		if(p[len]=='\n')
		{
			printS(0x0a);printS(0x0d);
		}
		else
		{
			printS(p[len]);
		}
		len++;
	}
	}
}

void printhex(BYTE value)
{
	BYTE nibble = 0;
	nibble = (value>>4)&0xf;
	if(nibble > 9)
		printS(nibble+0x41-10);
	else
		printS(nibble+0x30);
	nibble = (value)&0xf;
	if(nibble > 9)
		printS(nibble+0x41-10);
	else
		printS(nibble+0x30);
}

void printx(ULONG value)
{
	BYTE value3 = 0;
	BYTE value2 = 0;
	BYTE value1 = 0;
	BYTE value0 = 0;
	BYTE need_to_print_zero = 0;

	value3 = (value>>24)&0xff;
	value2 = (value>>16)&0xff;
	value1 = (value>>8)&0xff;
	value0 = (value)&0xff;

	if(value3 > 0)
	{
		need_to_print_zero = 1;
		printhex(value3);
	}
	if((value2 > 0) || (need_to_print_zero == 1))
	{
		need_to_print_zero = 1;
		printhex(value2);
	}
	if((value1 > 0) || (need_to_print_zero == 1))
	{
		need_to_print_zero = 1;
		printhex(value1);
	}
	printhex(value0);
}

void printd2(unsigned long value)
{
	if(value>=100000000)
		printS2('X');
	if(value>=10000000)
		printS2(((value/10000000)%10)+0x30);
	if(value>=1000000)
		printS2(((value/1000000)%10)+0x30);
	if(value>=100000)
		printS2(((value/100000)%10)+0x30);
	if(value>=10000)
		printS2(((value/10000)%10)+0x30);
	if(value>=1000)
		printS2(((value/1000)%10)+0x30);
	if(value>=100)
		printS2(((value/100)%10)+0x30);
	if(value>=10)
		printS2(((value/10)%10)+0x30);
	printS2(((value)%10)+0x30);
}

void printd(long value)
{
	if(value < 0)
	{
		printS('-');
		printd(-value);
		return;
	}
	if(value>=100000000)
		printS('X');
	if(value>=10000000)
		printS(((value/10000000)%10)+0x30);
	if(value>=1000000)
		printS(((value/1000000)%10)+0x30);
	if(value>=100000)
		printS(((value/100000)%10)+0x30);
	if(value>=10000)
		printS(((value/10000)%10)+0x30);
	if(value>=1000)
		printS(((value/1000)%10)+0x30);
	if(value>=100)
		printS(((value/100)%10)+0x30);
	if(value>=10)
		printS(((value/10)%10)+0x30);
	printS(((value)%10)+0x30);
}

void printd_sign(long value)
{
	if(value<0)
	{
		value= -value;
		printS('-');
	}
	else
		printS('+');
	printd(value);
}

void print2d(unsigned long value)
{
	if(value<10)
		printS('0');
	if(value>=10)
		printS(((value/10)%10)+0x30);
	printS(((value)%10)+0x30);
}

void printv(unsigned long value)	//print voltage
{
	if (value==0)
	{
		printS('0');
	}
	else
	{
		if(value>=1000000)
			printS((value/1000000)+0x30);
		if(value>=100000)
			printS((value/100000)+0x30);
		if(value>=10000)
			printS(((value/10000)%10)+0x30);
		if(value>=1000)
			printS(((value/1000)%10)+0x30);
		else
			printS('0');
		printS('.');
		printS(((value/100)%10)+0x30);
		printS(((value/10)%10)+0x30);
		printS(((value)%10)+0x30);
	}
}

void warning_light()		//Valid in CM2209D
{
	while(1)
	{
		P1_7 = 0;	//D11 ON, 0V
		P1_6 = 0;	//D12 ON
		P0_5 = 0;	//D13 ON
		P0_1 = 0;	//D15 ON
		DelayXms(100);
		P1_7 = 1;	//D11 OFF, 5V
		P1_6 = 1;	//D12 OFF
		P0_5 = 1;	//D13 OFF
		P0_1 = 1;	//D15 OFF
		DelayXms(100);
	}
}

void all_light_on()			//Valid in CM2209D
{
	P1_7 = 0;	//D11 ON, 0V
	P1_6 = 0;	//D12 ON
	P0_5 = 0;	//D13 ON
	P0_1 = 0;	//D15 ON
}

void all_light_off()			//Valid in CM2209D
{
	P1_7 = 1;	//D11 OFF, 5V
	P1_6 = 1;	//D12 OFF
	P0_5 = 1;	//D13 OFF
	P0_1 = 1;	//D15 OFF
}

ULONG get_time_tick()
{
	return T5_count;
}

void get_current_time(void)
{
	if(T5_count == 0)
		printString("Get current time fail. You should turn on Timer5 first by typing `clock' .\n");
	else
	{
		printd(T5_count/86400);printS(':');
		print2d((T5_count%86400)/3600);printS(':');
		print2d(((T5_count%86400)%3600)/60);printS(':');
		print2d(((T5_count%86400)%3600)%60);printString("\n");
	}
}

void get_system_up_time(void)
{
	if(T5_count == 0)
		printString("Get system up time fail. You should turn on Timer5 first by typing `clock' .\n");
	else
	{
		printString("System Up Time: ");
		printd(T5_count/86400);printString(" Days, ");
		printd((T5_count%86400)/3600);printString(" Hours, ");
		printd(((T5_count%86400)%3600)/60);printString(" Minutes, ");
		printd(((T5_count%86400)%3600)%60);printString(" Seconds\n");
	}
}

UINT adc2vac(UINT adc)
{
	UINT result = 0;
	result = (adc/16)*185/256*3*5/7;
	return result;
}

void print_error_message(UINT ERROR_number)
{
	if(ERROR_number == _ERROR_NONE)
		printString("No error\n");
	if(((ERROR_number >> 0) & 0x01) == 1)
		printString("Parameter error\n");
	if(((ERROR_number >> 1) & 0x01) == 1)
		printString("Over Voltage\n");
	if(((ERROR_number >> 2) & 0x01) == 1)
		printString("Under Voltage\n");
	if(((ERROR_number >> 3) & 0x01) == 1)
		printString("Lock Rotor\n");
	if(((ERROR_number >> 4) & 0x01) == 1)
		printString("Hall error\n");
	if(((ERROR_number >> 5) & 0x01) == 1)
		printString("Over Current A\n");
	if(((ERROR_number >> 6) & 0x01) == 1)
		printString("Over Current C\n");
	if(((ERROR_number >> 7) & 0x01) == 1)
		printString("Over Current X\n");
	if(((ERROR_number >> 8) & 0x01) == 1)
		printString("UVW lack phase\n");
	if(((ERROR_number >> 9) & 0x01) == 1)
		printString("UVW short\n");
	if(((ERROR_number >> 10) & 0x01) == 1)
		printString("Power recover\n");
}

void print_debug_message()
{
	if(flag_mode_type == CLOSE_LOOP)
	{
		printS('C');
		//PWM_duty=(PWM_PERIOD-((PWMAH <<8) + PWMAL))/4;
		printString(" t:");printd(target_speed);
	}
	else if(flag_mode_type == OPEN_LOOP)
		printS('O');
	printString(" d:");printd(PWM_duty);
	//printString(" p:");printd((PWMAH <<8) + PWMAL);
	printString(" r:");printd(real_speed);
	//printString(" prd:0x");printx(PWM_period);
	if(flag_run_dir == CW)
		printString(" CW");
	else
		printString(" CCW");
	printString("\n");
}

void print_message()
{
	if(flag_mode_type == CLOSE_LOOP)
	{
		printS('C');
		//PWM_duty=(PWM_PERIOD-((PWMAH <<8) + PWMAL))/4;
		printString(" t:");printd(target_speed);
	}
	else if(flag_mode_type == OPEN_LOOP)
		printS('O');
	printString(" d:");printd(PWM_duty);printS(' ');
	//printString(" p:");printd((PWMAH <<8) + PWMAL);printS(' ');
	printString("r:");printd(real_speed);printString("\n");
}
