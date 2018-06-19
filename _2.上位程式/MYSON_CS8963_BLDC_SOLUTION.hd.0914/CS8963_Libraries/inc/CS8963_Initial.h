#ifndef __CS8963_INITIAL_H__
#define __CS8963_INITIAL_H__

void Initial_IO(void);
void Initial_Comparator_VTH1(BYTE vth1);
void Disable_Comparator(void);
void Initial_PAC_IO(void);
void Initial_REGTRM(unsigned char regtrm);
BYTE IFB_Read_1Byte(unsigned char ADD);
void IFB_Read_256Byte(void);
void Initial_Comparator_Sensorless(void);
void check_comparator_edge(void);
#endif

