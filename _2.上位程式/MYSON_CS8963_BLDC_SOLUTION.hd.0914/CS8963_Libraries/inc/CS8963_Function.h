#ifndef __CS8963_FUNCTION_H__
#define __CS8963_FUNCTION_H__

void Reset_system(void);
void Delay1s(void);
void DelayXms2(unsigned char delay);
void DelayXms(UINT delay);
void DelayYms(void);
void Delay2us(unsigned char delay);
void DelayNticks(unsigned int ticks);
void printS(unsigned char p);
void printS2(unsigned char p);
void printS_UART(unsigned char p);
void printString2(unsigned char* p);
void printString(unsigned char* p);
void printx(ULONG value);
void printd2(unsigned long value);
void printd(long value);
void printd_sign(long value);
void print2d(unsigned long value);
void printv(unsigned long value);
void warning_light();
void all_light_on();
void all_light_off();
ULONG get_time_tick();
void get_current_time(void);
void get_system_up_time(void);
UINT adc2vac(UINT adc);
void print_error_message(UINT ERROR_number);
void print_debug_message();
void print_message();
#endif

