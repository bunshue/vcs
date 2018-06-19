#ifndef __CS8963_CONFIG_H__
#define __CS8963_CONFIG_H__
 
#define _P0_0	18
#define _P0_1	17
#define _P0_2	16
#define _P0_3	15
#define _P0_4	14
#define _P0_5	13
#define _P0_6	12
#define _P0_7	11
#define _P1_0	10
#define _P1_1	9
#define _P1_2	4
#define _P1_3	3
#define _P1_4	8
#define _P1_5	7
#define _P1_6	2
#define _P1_7	1
#define _P2_0	31
#define _P2_1	30
#define _P2_2	29
#define _P2_3	28
#define _P2_4	27
#define _P2_5	26
#define _P2_6	25
#define _P2_7	24
#define _P3_0	6
#define _P3_1	5
#define _P3_2	23
#define _P3_3	22
#define _VSS		32
#define _VDDC	19
#define _VDD		20
#define _RSTN	21

#define PIN1		1
#define PIN2		2
#define PIN3		3
#define PIN4		4
#define PIN5		5
#define PIN6		6
#define PIN7		7
#define PIN8		8
#define PIN9		9
#define PIN10	10
#define PIN11	11
#define PIN12	12
#define PIN13	13
#define PIN14	14
#define PIN15	15
#define PIN16	16
#define PIN17	17
#define PIN18	18
#define PIN19	19
#define PIN20	20
#define PIN21	21
#define PIN22	22
#define PIN23	23
#define PIN24	24
#define PIN25	25
#define PIN26	26
#define PIN27	27
#define PIN28	28
#define PIN29	29
#define PIN30	30
#define PIN31	31
#define PIN32	32

void PIN_CONFIG_setup_pwmap(unsigned char pin);
void PIN_CONFIG_setup_pwman(unsigned char pin);
void PIN_CONFIG_setup_pwmbp(unsigned char pin);
void PIN_CONFIG_setup_pwmbn(unsigned char pin);
void PIN_CONFIG_setup_pwmcp(unsigned char pin);
void PIN_CONFIG_setup_pwmcn(unsigned char pin);
void PIN_CONFIG_setup_xemg(unsigned char pin, unsigned char select);
void PIN_CONFIG_setup_hallsensor_a(unsigned char pin);
void PIN_CONFIG_setup_hallsensor_b(unsigned char pin);
void PIN_CONFIG_setup_hallsensor_c(unsigned char pin);
void PIN_CONFIG_setup_i2c_scl(unsigned char pin);
void PIN_CONFIG_setup_i2c_sda(unsigned char pin);
void PIN_CONFIG_setup_uart_txd(unsigned char pin);
void PIN_CONFIG_setup_uart_rxd(unsigned char pin);
void PIN_CONFIG_setup_euart2_rxd(unsigned char pin);
void PIN_CONFIG_setup_euart2_txd(unsigned char pin);
void PIN_CONFIG_setup_adc(unsigned char pin);
void PIN_CONFIG_setup_cmp(BYTE pin, BYTE VTH, BYTE enable);
void PIN_CONFIG_setup_gpio(unsigned char pin);
void PIN_CONFIG_setup_key(unsigned char pin);
void PIN_CONFIG_setup_dac(unsigned char pin);
#endif

