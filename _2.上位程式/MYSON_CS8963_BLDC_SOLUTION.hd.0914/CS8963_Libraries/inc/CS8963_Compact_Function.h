#ifndef __CS8963_COMPACT_FUNCTION_H__
#define __CS8963_COMPACT_FUNCTION_H__
void Initial_Timer3(void);
void Initial_Timer4(void);
void Initial_Timer5(void);
void Timer3_Close(void);
void Timer4_Close(void);
void Timer5_Close(void);
void get_current_hall_state();
void Initial_Comparator_VTH1(BYTE vth1);
void Disable_Comparator(void);
void printx(unsigned int value);
#endif
