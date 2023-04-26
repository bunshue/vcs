// TestFileOperation.cpp: 主要專案檔。

#include "stdafx.h"
#include <iostream>

using namespace System;
using namespace System::IO;

int test_directory_create_delete(void);		//File1.cpp File4.cpp
int test_sub_directory_create(void);		//File2.cpp
int test_directory_move(void);				//File3.cpp

int test_file_copy_delete_move(void);		//File5.cpp File6.cpp File7.cpp
int test_get_file_info(void);				//File8.cpp
int test_get_file_info2(void);				//example on MSDN
int test_write_a_text_file(void);			//File9.cp
int test_write_a_text_file2(void);			//File13.cp
int test_read_a_text_file2(void);			//File10.cp
int test_write_a_binary_file(void);			//File11.cp
int test_read_a_binary_file(void);			//File12.cp
int test_file_read_write_binary(void);
int test_GetFileAttributes(void);
int save_folder_data(void);
int bin2hex(void);


typedef    unsigned char	   BYTE;
#define XBYTE ((unsigned char volatile xdata *) 0)

#define REGTRM        XBYTE[0xa000]
#define IOSCITRM      XBYTE[0xa001]
#define IOSCVTRM      XBYTE[0xa002]
#define T5CON         XBYTE[0xa003]
#define T5L           XBYTE[0xa004]
#define T5H           XBYTE[0xa005]
#define T5T           XBYTE[0xa006]
#define XOSCCFG       XBYTE[0xa007]
#define RTCSCND0      XBYTE[0xa008]
#define RTCSCND1      XBYTE[0xa009]
#define RTCSCND2      XBYTE[0xa00a]
#define RTCSCND3      XBYTE[0xa00b]
#define RTCCNTL       XBYTE[0xa00c]
#define RTCCNTH       XBYTE[0xa00d]
#define RTCCMD        XBYTE[0xa00e]

#define LVDCFG        XBYTE[0xa010]
#define LVDTHD        XBYTE[0xa011]
#define FLSHADM       XBYTE[0xa012]
#define INTPCT1       XBYTE[0xa013]
#define INTPCT2       XBYTE[0xa014]
#define COMPCFG       XBYTE[0xa017]


//2. Flash Controller
#define FLSHCMD       XBYTE[0xa020]
#define FLSHDAT       XBYTE[0xa021]
#define FLSHADH       XBYTE[0xa022]
#define FLSHADL       XBYTE[0xa023]
#define ISPCLKF       XBYTE[0xa024]
#define CNTPCTL       XBYTE[0xa025]
#define CNTPCTH       XBYTE[0xa026]

#define PIOEDGR0      XBYTE[0xa028]
#define PIOEDGR1      XBYTE[0xa029]
#define PIOEDGR2      XBYTE[0xa02a]
#define PIOEDGR3      XBYTE[0xa02b]
#define PIOEDGR4      XBYTE[0xa02c]
#define PIOEDGR5      XBYTE[0xa02d]

#define CMPCFGAB      XBYTE[0xa030]
#define CMPCFGCD      XBYTE[0xa031]
#define CMPVTH0       XBYTE[0xa032]
#define CMPVTH1       XBYTE[0xa033]
#define DACL          XBYTE[0xa036]
#define DACH          XBYTE[0xa037]

#define PIOEDGF0      XBYTE[0xa038]
#define PIOEDGF1      XBYTE[0xa039]
#define PIOEDGF2      XBYTE[0xa03a]
#define PIOEDGF3      XBYTE[0xa03b]
#define PIOEDGF4      XBYTE[0xa03c]
#define PIOEDGF5      XBYTE[0xa03d]

#define IOCFGP0_0     XBYTE[0xa040]
#define IOCFGP0_1     XBYTE[0xa041]
#define IOCFGP0_2     XBYTE[0xa042]
#define IOCFGP0_3     XBYTE[0xa043]
#define IOCFGP0_4     XBYTE[0xa044]
#define IOCFGP0_5     XBYTE[0xa045]
#define IOCFGP0_6     XBYTE[0xa046]
#define IOCFGP0_7     XBYTE[0xa047]

#define IOCFGP1_0     XBYTE[0xa048]
#define IOCFGP1_1     XBYTE[0xa049]
#define IOCFGP1_2     XBYTE[0xa04a]
#define IOCFGP1_3     XBYTE[0xa04b]
#define IOCFGP1_4     XBYTE[0xa04c]
#define IOCFGP1_5     XBYTE[0xa04d]
#define IOCFGP1_6     XBYTE[0xa04e]
#define IOCFGP1_7     XBYTE[0xa04f]

#define MFCFGP0_0     XBYTE[0xa050]
#define MFCFGP0_1     XBYTE[0xa051]
#define MFCFGP0_2     XBYTE[0xa052]
#define MFCFGP0_3     XBYTE[0xa053]
#define MFCFGP0_4     XBYTE[0xa054]
#define MFCFGP0_5     XBYTE[0xa055]
#define MFCFGP0_6     XBYTE[0xa056]
#define MFCFGP0_7     XBYTE[0xa057]

#define MFCFGP1_0     XBYTE[0xa058]
#define MFCFGP1_1     XBYTE[0xa059]
#define MFCFGP1_2     XBYTE[0xa05a]
#define MFCFGP1_3     XBYTE[0xa05b]
#define MFCFGP1_4     XBYTE[0xa05c]
#define MFCFGP1_5     XBYTE[0xa05d]
#define MFCFGP1_6     XBYTE[0xa05e]
#define MFCFGP1_7     XBYTE[0xa05f]

#define IOCFGP2_0     XBYTE[0xa060]
#define IOCFGP2_1     XBYTE[0xa061]
#define IOCFGP2_2     XBYTE[0xa062]
#define IOCFGP2_3     XBYTE[0xa063]
#define IOCFGP2_4     XBYTE[0xa064]
#define IOCFGP2_5     XBYTE[0xa065]
#define IOCFGP2_6     XBYTE[0xa066]
#define IOCFGP2_7     XBYTE[0xa067]

#define IOCFGP3_0     XBYTE[0xa068]
#define IOCFGP3_1     XBYTE[0xa069]
#define IOCFGP3_2     XBYTE[0xa06a]
#define IOCFGP3_3     XBYTE[0xa06b]
#define IOCFGP3_4     XBYTE[0xa06c]
#define IOCFGP3_5     XBYTE[0xa06d]
#define IOCFGP3_6     XBYTE[0xa06e]
#define IOCFGP3_7     XBYTE[0xa06f]

#define MFCFGP2_0     XBYTE[0xa070]
#define MFCFGP2_1     XBYTE[0xa071]
#define MFCFGP2_2     XBYTE[0xa072]
#define MFCFGP2_3     XBYTE[0xa073]
#define MFCFGP2_4     XBYTE[0xa074]
#define MFCFGP2_5     XBYTE[0xa075]
#define MFCFGP2_6     XBYTE[0xa076]
#define MFCFGP2_7     XBYTE[0xa077]

#define MFCFGP3_0     XBYTE[0xa078]
#define MFCFGP3_1     XBYTE[0xa079]
#define MFCFGP3_2     XBYTE[0xa07a]
#define MFCFGP3_3     XBYTE[0xa07b]
#define MFCFGP3_4     XBYTE[0xa07c]
#define MFCFGP3_5     XBYTE[0xa07d]
#define MFCFGP3_6     XBYTE[0xa07e]
#define MFCFGP3_7     XBYTE[0xa07f]

#define PWMAL         XBYTE[0xa080]
#define PWMAH         XBYTE[0xa081]
#define PWMBL         XBYTE[0xa082]
#define PWMBH         XBYTE[0xa083]
#define PWMCL         XBYTE[0xa084]
#define PWMCH         XBYTE[0xa085]
#define PWMTRG0L      XBYTE[0xa086]
#define PWMTRG0H      XBYTE[0xa087]

#define PWMTRG1L      XBYTE[0xa088]
#define PWMTRG1H      XBYTE[0xa089]
#define PWMCNTL       XBYTE[0xa08a]
#define PWMCNTH       XBYTE[0xa08b]
#define PWMPRDL       XBYTE[0xa08c]
#define PWMPRDH       XBYTE[0xa08d]
#define PWM16CFG      XBYTE[0xa08e]
#define PWM16INT      XBYTE[0xa08f]

#define LINCTRL       XBYTE[0xa090]
#define LINCNTRH      XBYTE[0xa091]
#define LINCNTRL      XBYTE[0xa092]
#define LINSBRH       XBYTE[0xa093]
#define LINSBRL       XBYTE[0xa094]
#define LININT 	      XBYTE[0xa095]
#define LININTEN      XBYTE[0xa096]
#define PWM16EMG      XBYTE[0xa097]

#define DBPCIDL       XBYTE[0xa098]
#define DBPCIDH       XBYTE[0xa099]
#define DBPCIDT       XBYTE[0xa09a]
#define DBPCNXL       XBYTE[0xa09b]
#define DBPCNXH       XBYTE[0xa09c]
#define DBPCNXT       XBYTE[0xa09d]
#define PWM16CHS      XBYTE[0xa09f]

#define PCACPS 	      XBYTE[0xa0a5]
#define CLRLD 	      XBYTE[0xa0a6]
#define CHRLD 	      XBYTE[0xa0a7]

#define IOCFGP4_0     XBYTE[0xa0c0]
#define IOCFGP4_1     XBYTE[0xa0c1]
#define IOCFGP4_2     XBYTE[0xa0c2]
#define IOCFGP4_3     XBYTE[0xa0c3]
#define IOCFGP4_4     XBYTE[0xa0c4]
#define IOCFGP4_5     XBYTE[0xa0c5]
#define IOCFGP4_6     XBYTE[0xa0c6]
#define IOCFGP4_7     XBYTE[0xa0c7]

#define IOCFGP5_1     XBYTE[0xa0c8]
#define IOCFGP5_2     XBYTE[0xa0c9]
#define IOCFGP5_3     XBYTE[0xa0ca]
#define IOCFGP5_4     XBYTE[0xa0cb]
#define IOCFGP5_5     XBYTE[0xa0cc]
#define IOCFGP5_6     XBYTE[0xa0cd]
#define IOCFGP5_7     XBYTE[0xa0ce]
#define IOCFGP5_8     XBYTE[0xa0cf]

#define MFCFGP4_0     XBYTE[0xa0d0]
#define MFCFGP4_1     XBYTE[0xa0d1]
#define MFCFGP4_2     XBYTE[0xa0d2]
#define MFCFGP4_3     XBYTE[0xa0d3]
#define MFCFGP4_4     XBYTE[0xa0d4]
#define MFCFGP4_5     XBYTE[0xa0d5]
#define MFCFGP4_6     XBYTE[0xa0d6]
#define MFCFGP4_7     XBYTE[0xa0d7]

#define MFCFGP5_1     XBYTE[0xa0d8]
#define MFCFGP5_2     XBYTE[0xa0d9]
#define MFCFGP5_3     XBYTE[0xa0da]
#define MFCFGP5_4     XBYTE[0xa0db]
#define MFCFGP5_5     XBYTE[0xa0dc]
#define MFCFGP5_6     XBYTE[0xa0dd]
#define MFCFGP5_7     XBYTE[0xa0de]
#define MFCFGP5_8     XBYTE[0xa0df]

#define BPINTF        XBYTE[0xa0e0]
#define BPINTE        XBYTE[0xa0e1]
#define BPINTC        XBYTE[0xa0e2]
#define BPCTRL        XBYTE[0xa0e3]
#define PC5AL         XBYTE[0xa0e4]
#define PC5AH         XBYTE[0xa0e5]
#define PC5AT         XBYTE[0xa0e6]

#define PC6AL         XBYTE[0xa0e8]
#define PC6AH         XBYTE[0xa0e9]
#define PC6AT         XBYTE[0xa0ea]
#define PC7AL         XBYTE[0xa0ec]
#define PC7AH         XBYTE[0xa0ed]
#define PC7AT         XBYTE[0xa0ee]
#define SI2CDBGID     XBYTE[0xa0ef]

#define PC1AL         XBYTE[0xa0f0]
#define PC1AH         XBYTE[0xa0f1]
#define PC1AT         XBYTE[0xa0f2]
#define PC2AL         XBYTE[0xa0f4]
#define PC2AH         XBYTE[0xa0f5]
#define PC2AT         XBYTE[0xa0f6]

#define PC3AL         XBYTE[0xa0f8]
#define PC3AH         XBYTE[0xa0f9]
#define PC3AT         XBYTE[0xa0fa]
#define PC4AL         XBYTE[0xa0fc]
#define PC4AH         XBYTE[0xa0fd]
#define PC4AT         XBYTE[0xa0fe]

#define	PinC_In			0x80
#define	PinC_InPuUp		0xa0
#define	PinC_InPuDn		0x90
#define	PinC_InHold		0xc0

#define	PinC_InOutCMOS		0x86
#define	PinC_InOut51like	0xE2
#define	PinC_InOutCMOSUp	0xa6

#define	PinC_OutCMOS		0x06
#define	PinC_OutNMOS		0x02
#define	PinC_OutNMOSUp		0x22
#define	PinC_OutPMOS		0x04
#define	PinC_OutPMOSUp		0x24
#define PinC_OpenDrain		0x82
#define	PinC_Analog 		0x08
#define	PinC_OSC		0x00
//IO Config		INEN	LATEN	PUEN	PDEN	:	ANEN	PDRVEN	NDRVEN	__
#define	PinF_IO			0x01
#define	PinF_ADC		0x04

#define	AllSeting		PinC_InOutCMOS

//IOCFGP
#define _NDRVEN_		0x02  	// NMOS driver output enable
#define _PDRVEN_		0x04  	// PMOS driver output enable
#define _ANEN_	    		0x08  	// Analog switch enable
#define _PDEN_	    		0x10  	// pull down resistor enable
#define _PUEN_     		0x20  	// pull up resistor enable
#define _LATEN_	    		0x40  	// bus latch enable
#define _INEN_	    		0x80  	// input enable

//MFCFGP
#define _GPIOEN_		0x01  	// as GPIO function pin
#define _PINTEN_		0x02  	// as external interrupt pin
#define _ADA1EN_		0x04  	// as ADC pin
#define _PINTEDG_		0x08  	// interrupt edge




//MFCFGP
//MFCFGP0.0
#define ADA2EN		0x80	//ADC Channel A Enable bit.
#define CEX4EN		0x10	//CEX4EN=1 enable this pin as CEX I/O for CCP4.
#define SSNEN		0x08	//SSNEN=1 uses this pin as SPI SSN input.
#define PINT1EN		0x04	//Pin Interrupt Enable Control Bit.
#define PINT0EN		0x02	//Pin Interrupt Enable Control Bit
#define GPIOEN		0x01	//GPIO Function Enable Bit.

//MFCFGP0.1
#define ADB2EN		0x80	//ADC Channel B Enable bit.
#define CEX5EN		0x10	//CEX5EN=1 enable this pin as CEX I/O for CCP5.

//MFCFGP0.2
#define ADA1EN		0x80	//ADC Channel A Enable bit.

//MFCFGP0.3
#define ADB1EN		0x80	//ADC Channel B Enable bit.

//MFCFGP0.4
#define ADC1EN		0x80	//ADC Channel C Enable bit.

//MFCFGP0.5
#define ADD1EN		0x80	//ADC Channel D Enable bit.
#define XEMGEN4		0x10	//XEMGEN4=1 use this pin as XEMG input to PWM16 module.

//MFCFGP0.6
#define ADC2EN		0x80	//ADC Channel C Enable bit.
#define TXD2EN5		0x20	//TXD2EN5=1 uses this pin as TXD output for EUART2
#define TXD0EN		0x10	//TXD0EN=1 uses this pin as TXD output for UART0

//MFCFGP0.7
#define ADD2EN		0x80	//ADC Channel D Enable bit.
#define RXD2EN5		0x20	//RXD2EN5=1 uses this pin as RXD input for EUART2
#define RXD0EN		0x10	//RXD0EN=1 uses this pin as RXD input for UART0

//MFCFGP1.0
#define ADD3EN		0x80	//ADC Channel D Enable bit.
#define PWMAPEN		0x20	//PWMAPEN=1 uses this pin as PWM16 Channel A positive output
#define CEX0EN		0x10	//CEX0EN=1 uses this pin as CCP0 CEX I/O

//MFCFGP1.1
#define ADC4EN		0x80	//ADC Channel D Enable bit.
#define PWMANEN		0x20	//PWMAPEN=1 use this pin as PWM16 Channel A negative output
#define CEX1EN		0x10	//CEX1EN=1 uses this pin as CCP1 CEX I/O

//MFCFGP1.2
#define ADD7EN		0x80	//ADC Channel D Enable bit.
#define SSDA1EN6	0x40	//SSDA1EN6=1 enables this pin as I2CS1 SDA I/O.
#define PWMAPEN		0x20	//PWMAPEN=1 uses this pin as PWM16 Channel A positive output
#define CEX2EN		0x10	//CEX2EN=1 uses this pin as CCP2 CEX I/O

//MFCFGP1.3
#define ADD8EN		0x80	//ADC Channel D Input Enable bit.
#define SSCL1EN6	0x40	//SSCL1EN6=1 enables this pin as I2CS1 SCL I/O.
#define PWMANEN		0x20	//PWMANEN=1 use this pin as PWM16 Channel A negative output
#define CEX3EN		0x10	//CEX3EN=1 uses this pin as CCP3 CEX I/O

//MFCFGP1.4
#define RXOUTEN		0x80	//RTC Crystal Output Enable pin. RXOUT is an analog circuit output therefore ANEN in IOCFGP1.4 must also be enabled.
#define SSCL2EN		0x40	//SSCL2EN=1 enables this pin as I2CS2 SCL I/O. This must be configured as OD output.
#define PWMBPEN		0x20	//PWMBPEN=1 uses this pin as PWM16 Channel B positive output.
#define MSCLEN4		0x10	//MSCLEN4=1 enables this pin as I2CM SCL I/O. This must be configured as OD output.

//MFCFGP1.5
#define ADC1EN		0x80	//ADC Channel C Enable bit.
#define RXINEN		0x80	//RTC Crystal IN Enable pin. RXIN is an analog circuit output therefore ANEN in IOCFGP1.5 must also be enabled.
#define SSDA2EN		0x40	//SSDA2EN=1 enables this pin as I2CS2 SDA I/O. This must be configured as OD output.
#define PWMBNEN		0x20	//PWMBNEN=1 use this pin as PWM16 Channel B negative output.
#define MSDAEN4		0x10	//MSDAEN4=1 enables this pin as I2CM SDA I/O.

//MFCFGP1.6
#define ADD9EN		0x80	//ADC Channel D Input Enable bit. ADD9 is an analog circuit input therefore ANEN in IOCFGP1.6 must also be enabled.
#define T1EN		0x40	//T1EN=1 enables this pin as Timer 1 input. This must be configured as OD output.
#define PWMBPEN		0x20	//PWMBPEN=1 use this pin as PWM16 Channel B positive output.
#define CEX0EN		0x10	//CEX0EN=1 uses this pin as CCP0 CEX I/O.

//MFCFGP1.7
#define IDACEN		0x80	//Current DAC Output Enable bit. IDAC is an analog circuit output therefore ANEN in IOCFGP1.7 must also be enabled.
#define T0EN		0x40	//T0EN=1 enables this pin as Timer 0 input. This must be configured as OD output.
#define PWMBNEN		0x20	//PWMBNEN=1 use this pin as PWM16 Channel B negative output.
#define CEX1EN		0x10	//CEX1EN=1 uses this pin as CCP1 CEX I/O.

//MFCFGP2.0
#define XINEN		0x80	//Crystal IN Enable pin. XIN is an analog circuit output therefore ANEN in IOCFGP2.0 must also be enabled.
#define MSCLEN6		0x40	//MSCLEN6=1 enables this pin as I2CM SCL I/O. This must be configured as OD output.
#define SSCL1EN5	0x20	//SSCL1EN5=1 enables this pin as I2CSS1 SCL I/O. This must be configured as OD output.
#define CEX4EN		0x10	//CEX4EN=1 uses this pin as CCP4 CEX I/O.
#define MOSIEN		0x08	//MOSIEN=1 uses this pin as SPI MOSI I/O.

//MFCFGP2.0
#define XOUTEN		0x80	//Crystal OUT Enable pin. XOUT is an analog circuit output therefore ANEN in IOCFGP2.1 must also be enabled.
#define MSDAEN6		0x40	//MSDAEN6=1 enables this pin as I2CM SDA I/O. This must be configured as OD output.
#define SSDA1EN5	0x20	//SSDA1EN5=1 enables this pin as I2CSS1 SDA I/O. This must be configured as OD output.
#define CEX4EN		0x10	//CEX4EN=1 uses this pin as CCP4 CEX I/O.
#define MISOEN		0x08	//MISOEN=1 uses this pin as SPI MISO I/O.

//MFCFGP2.2
//#define IDACEN		0x80	//Current DAC Output Enable bit. IDAC is an analog circuit output therefore ANEN in IOCFGP2.2 must also be enabled.
#define XEMGEN5		0x20	//XEMGEN5=1 enables this pin as EMG input of PWM16.
#define TXD2EN4		0x10	//TXD2EN4=1 uses this pin as EUART2 TXD output.
#define SCKEN		0x08	//SCKEN=1 uses this pin as SPI SCK I/O.

//MFCFGP2.3
#define CMPTHEN		0x80	//Comparator External Threshold Enable bit. CMPTH is an analog circuit input therefore ANEN in IOCFGP2.3 must also be enabled.
#define XEMGEN		0x20	//XEMGEN=1 enables this pin as EMG input of PWM16.
#define RXD2EN4		0x10	//RXD2EN4=1 uses this pin as EUART2 RXD input.
#define SSNEN		0x08	//SSNEN=1 uses this pin as SPI SSN input.

//MFCFGP2.4
#define CMPDEN		0x80	//Comparator D Input Enable bit. CMPD is an analog circuit input therefore ANEN in IOCFGP2.4 must also be enabled.
#define PWMCPEN		0x20	//PWMCPEN=1 use this pin as PWM16 Channel C positive output.
#define T2EN		0x10	//T2EN=1 uses this pin as Timer 2 Input.

//MFCFGP2.5
#define CMPCEN		0x80	//Comparator C Input Enable bit. CMPC is an analog circuit input therefore ANEN in IOCFGP2.5 must also be enabled.
#define PWMCNEN		0x20	//PWMCNEN=1 use this pin as PWM16 Channel C negative output.
#define CEX4EN		0x10	//CEX4EN=1 uses this pin as CCP4 CEX I/O.

//MFCFGP2.6
#define CMPBEN		0x80	//Comparator B Input Enable bit. CMPB is an analog circuit input therefore ANEN in IOCFGP2.6 must also be enabled.
#define XEMGEN		0x20	//XEMGEN=1 enables this pin as EMG input of PWM16.
#define CEX5EN		0x10	//CEX4EN=1 uses this pin as CCP5 CEX I/O.
#define SSNEN		0x08	//SSNEN=1 uses this pin as SPI SSN input.

//MFCFGP2.7
#define ADC1EN		0x80	//ADC Channel C Enable bit.
#define CMPAEN		0x80	//Comparator A Input Enable bit. CMPA is an analog circuit input therefore ANEN in IOCFGP2.7 must also be enabled.
#define XEMGEN		0x20	//XEMGEN=1 enables this pin as EMG input of PWM16.
#define T2EXEN		0x10	//T2EXEN=1 enables this pin as T2EX input for Timer 2.
#define SCKEN		0x08	//SCKEN=1 uses this pin as SPI SCK I/O.

//MFCFGP3.0
#define ADD5EN		0x80	//ADC Channel D Input Enable bit. ADD5 is an analog circuit input therefore ANEN in IOCFGP3.0 must also be enabled.
#define PWMCNEN		0x20	//PWMCNEN=1 use this pin as PWM16 Channel C negative output.
#define CEX2EN		0x10	//CEX2EN=1 enable this pin as CCP2 CEX I/O.

//MFCFGP3.1
#define ADD6EN		0x80	//ADC Channel D Input Enable bit. ADD6 is an analog circuit input therefore ANEN in IOCFGP3.1 must also be enabled.
#define PWMCPEN		0x20	//PWMCPEN=1 use this pin as PWM16 Channel C positive output.
#define CEX3EN		0x10	//CEX3EN=1 enable this pin as CCP3 CEX I/O.

//MFCFGP3.2
#define ADC1EN		0x80	//ADC Channel C Enable bit.
//#define IDACEN		0x80	//Current DAC Output Enable bit. IDAC is an analog circuit output therefore ANEN in IOCFGP3.2 must also be enabled.
//#define TXD2EN5		0x20	//TXD2EN5=1 uses this pin as EUART2 TXD output.
#define CEX4EN		0x10	//CEX4EN=1 enable this pin as CCP4 CEX I/O.
#define MOSIEN		0x08	//MOSIEN=1 uses this pin as SPI MOSI I/O.

//MFCFGP3.3
#define CMPAEN		0x80	//Comparator A Input Enable bit. CMPA is an analog circuit input therefore ANEN in IOCFGP2.7 must also be enabled.
//#define RXD2EN5		0x20	//RXD2EN5=1 uses this pin as EUART2 RXD input.
#define CEX5EN		0x10	//CEX5EN=1 enable this pin as CCP5 CEX I/O.
#define MISOEN		0x08	//MISOEN=1 uses this pin as SPI MISO I/O.




int main(array<System::String ^> ^args)
{
	//test_directory_create_delete();
	//test_sub_directory_create();
	//test_directory_move();
	//test_file_copy_delete_move();
	//test_get_file_info();					//File8.cpp
	//test_get_file_info2();
	//test_write_a_text_file();				//File9.cp
	//test_read_a_text_file();				//File10.cp
	//test_write_a_binary_file();			//File11.cp
	//test_read_a_binary_file();			//File12.cp
	//test_file_read_write_binary();
	//test_GetFileAttributes();
	//test_write_a_text_file2();			//File13.cp
	//bin2hex();
	//test_file_read_write_binary();

	save_folder_data();


	system("pause");
    return 0;
}

int test_directory_create_delete(void)
{
	String^ dir_path = gcnew String ( "D:\\__test_area\\test_file_operation_1" );
	try
	{
		if (Directory::Exists(dir_path))
		{
			Console::WriteLine("That directory exists already.");
			system("pause");

			//	測試刪除目錄	File4.cpp
			Console::WriteLine("Try to delete it");
			system("pause");
			Directory::Delete(dir_path, true);
			Console::WriteLine("Delete OK..   exit");
			system("pause");

			return 0;
		}
		else
		{
			Console::WriteLine("That directory does not exist. Create it now........");
			DirectoryInfo^ di = Directory::CreateDirectory(dir_path);
			Console::WriteLine("The directory was created successfully.");
		}
	}
	catch (Exception^ e)
	{
		Console::WriteLine("The directory process failed: {0}.",e->Message);
	}
	__finally{ };
	return 0;
}


int test_sub_directory_create(void)
{
	DirectoryInfo^ di = gcnew DirectoryInfo ( "D:\\__test_area\\test_file_operation_2" );
	try
	{
		if (! di->Exists)
		{
			Console::WriteLine("The directory does not exist, creat it.");
			di->Create();					//create directory
		}
		Console::WriteLine("Create Subdirectory.");
		di->CreateSubdirectory("SubDir");	//create subdirectory
		Console::WriteLine("The subdirectory was created successfully.");
		system("pause");
	}
	catch (Exception^ e)
	{
		Console::WriteLine("The directory process failed: {0}.",e->Message);
	}
	__finally{ };
	return 0;
}

int test_directory_move(void)
{
	String^ path1 = "D:\\__test_area\\_test_move_file\\directory1";		//Source directory
	String^ path2 = "D:\\__test_area\\_test_move_file\\directory2";		//Destination directory

	try
	{
		if (!Directory::Exists(path1))
		{
			Console::WriteLine("Source directory does not exist, leave.....");
			return 0;
		}
		if (Directory::Exists(path2))
		{
			Console::WriteLine("Destination directory already exists, leave.....");
			return 0;
		}

		Console::WriteLine("Move directory......");
		Directory::Move(path1, path2);
		Console::WriteLine("Move directory...... OK");
	}

	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	return 0;
}

int test_file_copy_delete_move()
{
	String^ path1 = "D:\\__test_area\\_test_move_file\\_test_move_file1\\test1.txt";
	String^ path2 = "D:\\__test_area\\_test_move_file\\_test_move_file2\\test2.txt";
	try
	{
		if (  !File::Exists( path1 ) )
		{
			Console::WriteLine("Original file does not exist, leave........");
			return 0;
		}
		else
			Console::WriteLine("Original file does exist........");

		if (  File::Exists( path2 ) )
		{
			Console::WriteLine("Destination file exists, can not copy......");
			Console::WriteLine("Delete the distination file");
			File::Delete( path2 );
			Console::WriteLine("Delete the distination file OK, need to run it again.");
			return 0;
		}
		else
			Console::WriteLine("Destination file does not exist, continue........");

		// Copy the file.	File5.cpp
		Console::WriteLine("Copy file.");
		File::Copy( path1 , path2 , true);	//選擇true為允許覆寫相同名稱的檔案，否則為flase。
		Console::WriteLine("The file was copied OK.");
		system("pause");

		// Delete the file.	File6.cpp
		Console::WriteLine("Test Delete File");
		Console::WriteLine("Delete {0}",path1);
		File::Delete(path1);
		Console::WriteLine("{0} was deleted",path1);
		system("pause");

		// Move the file.	File7.cpp
		Console::WriteLine("Test Move File");
		File::Move( path2, path1 );
		Console::WriteLine( "{0} was moved to {1}.", path2, path1 );
		system("pause");
	}
	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	return 0;
}

int test_get_file_info(void)					//File8.cpp
{
	String^ dir_path = "D:\\__test_area\\TestFileOperationFiles";

	if (!Directory::Exists(dir_path))
	{
		Console::WriteLine("Directory {0} does not exist, leave.....", dir_path);
		return 0;
	}

	DirectoryInfo^ di = gcnew DirectoryInfo(dir_path);	//實做目錄資料物件

	array<DirectoryInfo^> ^fiArr2 = di->GetDirectories();	//由目錄資料物件取出子目錄資料
	Console::WriteLine("The directory {0} contains the following files:",di->Name);

	for each (DirectoryInfo ^f in fiArr2)		//顯示所有檔案名稱與大小
	{
		if((f->Attributes & FileAttributes::Directory) == FileAttributes::Directory)
			Console::WriteLine("{0} is a directory",f->Name);
		else
			Console::WriteLine("{0} is a file",f->Name);

		Console::WriteLine("name: {0}",f->FullName);
	}

	array<FileInfo^> ^fiArr = di->GetFiles();			//由目錄資料物件取出檔案資料
	Console::WriteLine("The directory {0} contains the following files:",di->Name);

	for each (FileInfo ^f in fiArr)		//顯示所有檔案名稱與大小
	{
		if((f->Attributes & FileAttributes::Directory) == FileAttributes::Directory)
			Console::WriteLine("{0} is a directory",f->Name);
		else
			Console::WriteLine("{0} is a file",f->Name);

		Console::WriteLine("{0} ----- {1} bytes. {2}   {3}  {4}",f->Name, f->Length, f->CreationTime, f->FullName, f->Extension);
	}

	//實做檔案資料物件
	FileInfo^ f = gcnew FileInfo("D:\\__test_area\\TestFileOperationFiles\\folder1\\pic016.jpg");
	Console::WriteLine("\n{0} ----- {1} bytes.",f->Name, f->Length);



	return 0;
}



int test_get_file_info2(void)					//example on MSDN
{
   try
   {
      DirectoryInfo^ di = gcnew DirectoryInfo( "D:\\__test_area\\TestFileOperationFiles" );

      // Get only subdirectories that contain the letter "f."
      array<DirectoryInfo^>^dirs = di->GetDirectories( "*f*" );
      Console::WriteLine( "The number of directories containing the letter f is {0}.", dirs->Length );
      Collections::IEnumerator^ myEnum = dirs->GetEnumerator();
      while ( myEnum->MoveNext() )
      {
         DirectoryInfo^ diNext = safe_cast<DirectoryInfo^>(myEnum->Current);
         Console::WriteLine( "The number of files in {0} is {1}", diNext, diNext->GetFiles()->Length );
      }
   }
   catch ( Exception^ e )
   {
      Console::WriteLine( "The process failed: {0}", e );
   }
   return 0;

}

int test_write_a_text_file(void)			//File9.cp
{
	String^ fid = "D:\\__test_area\\TestFileOperationFiles\\test_write_a_text_file.txt";

	if (File::Exists(fid)){
		Console::WriteLine("File already exists! Remove it.");
		File::Delete(fid);
		Console::WriteLine("File {0} removed, continue.....",fid);
	}

	StreamWriter^ sw = File::CreateText(fid);

	//開始寫資料到檔案裏面
	sw->WriteLine("This is a lion.");
	sw->WriteLine("This is a mouse.");
	sw->WriteLine("This is a cat.");
	sw->WriteLine("This is a dog.");
	sw->WriteLine("This is a elephant.");
	sw->Write("The date Now is: {0}", DateTime::Now);

	sw->WriteLine();
	sw->Close();
	Console::Write("Process was completed!\n");

	return 0;
}

int test_read_a_text_file(void)			//File10.cp
{
	int linenumber=0;
	try
	{
		String^ fid = "D:\\__test_area\\TestFileOperationFiles\\test_read_a_text_file.txt";

		if (!File::Exists(fid)){
			Console::WriteLine("File does not exist, exit....");
			return 0;
		}

		StreamReader^ sr = gcnew StreamReader(fid);

		String^ line;

		while((line=sr->ReadLine())!=nullptr)
		{
			linenumber++;
			Console::Write("{0}\t",linenumber);
			Console::WriteLine(line);
		}
	}
	catch (Exception^ e)
	{
		Console::WriteLine("The file could not be read: {0}.",e->Message);
	}
	__finally{ };
	return 0;
}


int test_write_a_binary_file(void)			//File11.cp
{
	unsigned char i;
	String^ fid = "D:\\__test_area\\TestFileOperationFiles\\test_write_a_binary_file.dat";

	if (File::Exists(fid)){
		Console::WriteLine("File already exists! Remove it.");
		File::Delete(fid);
		Console::WriteLine("File {0} removed, continue.....",fid);
	}

	FileStream^ fs = gcnew FileStream(fid, FileMode::CreateNew);

	//開始寫資料到檔案裏面
	BinaryWriter^ w =gcnew BinaryWriter(fs);
	for(i=0;i<100;i++)
		w->Write(i);
	w->Close();
	fs->Close();
	Console::Write("Process was completed!\n");

	return 0;
}


int test_read_a_binary_file(void)			//File12.cp
{
	int linenumber=0;
	try
	{
		String^ fid = "D:\\__test_area\\TestFileOperationFiles\\samsung_46es6600.bin";
		if (!File::Exists(fid)){
			Console::WriteLine("File does not exist, exit....");
			return 0;
		}

		FileStream^ fs = gcnew FileStream(fid, FileMode::Open, FileAccess::Read);

		BinaryReader^ br = gcnew BinaryReader(fs);

		int no;

		while((no=br->ReadInt32())!=0)
		{
			linenumber++;
			Console::Write("{0}\t",linenumber);
			Console::WriteLine(no);
		}
		br->Close();
		fs->Close();
	}
	catch (System::IO::EndOfStreamException^ e)
	{
		Console::WriteLine("End of File: {0}", e->Message);
	}
	__finally{ };
	return 0;
}

int test_write_a_text_file2(void)			//File13.cp
{
	String^ fid = "D:\\__test_area\\TestFileOperationFiles\\PhoneBook.txt";

	if (File::Exists(fid)){
		Console::WriteLine("File already exists! Remove it.");
		File::Delete(fid);
		Console::WriteLine("File {0} removed, continue.....",fid);
	}

	StreamWriter^ sw = gcnew StreamWriter(fid);
	String^ name;
	String^ phone;
	String^ age;

	Console::Write("Input Name:");
	name=Console::ReadLine();
	while(name->Length!=0)
	{
		Console::Write("Input Phone:");
	phone=Console::ReadLine();
	Console::Write("Input Age:");
	age=Console::ReadLine();
	sw->WriteLine(name+" "+phone+" "+age);
	Console::Write("Input Name:");
	name=Console::ReadLine();
	}
	sw->WriteLine("This is a lion.");
	sw->WriteLine("This is a mouse.");
	sw->WriteLine("This is a cat.");
	sw->WriteLine("This is a dog.");
	sw->WriteLine("This is a elephant.");
	sw->Write("The date Now is: {0}", DateTime::Now);

	sw->WriteLine();
	sw->Close();
	Console::Write("Process was completed!\n");

	return 0;
}


int test_GetFileAttributes(void)
{
	Console::WriteLine( "測試檔案屬性");
	String^ path = "D:\\__test_area\\file_path_old.txt";

	// Check the file existency.
	if (  !File::Exists( path ) )
	{
		Console::WriteLine( "File {0} does not exist, creat it.", path);
		File::Create( path );
	}

	if ( (File::GetAttributes( path ) & FileAttributes::Hidden) == FileAttributes::Hidden )
	{
		// Show the file.
		Console::WriteLine( "檔案 {0} 是個隱藏檔，設為非隱藏檔", path );
		File::SetAttributes(path, File::GetAttributes( path ) & ~FileAttributes::Hidden);
		Console::WriteLine( "OK，檔案 {0} 已被設為非隱藏檔", path );
	}
	else
	{
		// Hide the file.
		Console::WriteLine( "檔案 {0} 是個非隱藏檔，設為隱藏檔", path );
		File::SetAttributes( path, static_cast<FileAttributes>(File::GetAttributes( path ) | FileAttributes::Hidden) );
		Console::WriteLine( "OK，檔案 {0} 已被設為隱藏檔", path );
	}
	return 0;
}











//-----------------------------------------------------------------------------------------------------------------------------------

int test_directory_create_delete2()
{
	String^ dir_path = gcnew String ( "D:\\__test_area\\_test_vs2008 " );
	try
	{
		if (Directory::Exists(dir_path))
		{
			Console::WriteLine("That directory exists already.");
			system("pause");

			/*	測試刪除目錄
			Console::WriteLine("Try to delete it");
			system("pause");
			Directory::Delete(dir_path);
			Console::WriteLine("Delete OK..   exit");
			system("pause");
			*/

			return 0;
		}
		else
		{
			Console::WriteLine("That directory does not exist. Create it now........");
			DirectoryInfo^ di = Directory::CreateDirectory(dir_path);
			Console::WriteLine("The directory was created successfully.");
		}
	}
	catch (Exception^ e)
	{
		Console::WriteLine("The directory process failed: {0}.",e->Message);
	}
	return 0;
}

int test_file_create_copy_delete()
{
	//String^ file_path = gcnew String ( "D:\\__test_area\_test_vs2008\test_file.txt" );
	String^ file_path = gcnew String ( "D:\\testfile.txt" );
	String^ file_path_old = gcnew String ( "D:\\testfileold.txt" );
	try
	{
		if (File::Exists(file_path))
		{
			Console::WriteLine("That file exists already.");
			system("pause");

			Console::WriteLine("Copy file.");
			File::Copy( file_path_old , file_path , true);	//選擇true為允許覆寫相同名稱的檔案，否則為flase。
			Console::WriteLine("The file was copied OK.");
			system("pause");

			/*	測試刪除檔案
			Console::WriteLine("Try to delete it");
			system("pause");
			File::Delete(file_path);
			Console::WriteLine("Delete OK..   exit");
			system("pause");
			*/

			return 0;
		}
		else
		{
			Console::WriteLine("That file does not exist. Create it now........");
			FileStream^ fs = File::Create( file_path );
			Console::WriteLine("The file was created successfully.");
			system("pause");
		}
	}
	catch (Exception^ e)
	{
		Console::WriteLine("The file process failed: {0}.",e->Message);
	}
	return 0;
}

int test_file_read_write_text()
{
	String^ file_path = gcnew String ( "D:\\testfileold.txt" );
	Console::WriteLine("Open the stream and read it back.");
	StreamReader^ sr = File::OpenText( file_path );
	try
	{
		String^ s = "";
		while ( s = sr->ReadLine() )
	    {
			Console::WriteLine("get line data: ");
			Console::WriteLine( s );
		}
	}
	finally
	{
		if ( sr )
			delete (IDisposable^)sr;
	}
	system("pause");
	return 0;
}


int test_file_copy_move()
{
	String^ path0 = "D:\\__test_area\\file_path_old.txt";
	String^ path1 = "D:\\__test_area\\_test_move_file\\_test_move_file1\\test1.txt";
	String^ path2 = "D:\\__test_area\\_test_move_file\\_test_move_file2\\test2.txt";
	try
	{
		if (  !File::Exists( path0 ) )
		{
			Console::WriteLine("Original file does not exist, leave........");
			return 1;
		}

		if (  !File::Exists( path1 ) )
		{
			// This statement ensures that the file is created,
			// but the handle is not kept.
			FileStream^ fs = File::Create( path1 );
			if ( fs )
				delete (IDisposable^)fs;
		}

		// Ensure that the target does not exist.
		if ( File::Exists( path2 ) )
			File::Delete( path2 );

		// Copy the file.
		Console::WriteLine("Copy file.");
		File::Copy( path0 , path1 , true);	//選擇true為允許覆寫相同名稱的檔案，否則為flase。
		Console::WriteLine("The file was copied OK.");
		system("pause");

		// Move the file.
		Console::WriteLine("Move file.");
		File::Move( path1, path2 );
		Console::WriteLine( "{0} was moved to {1}.", path1, path2 );
		system("pause");

		// See if the original exists now.
		if ( File::Exists( path1 ) )
		{
			Console::WriteLine( "The original file still exists, which is unexpected." );
		}
		else
		{
			Console::WriteLine( "The original file no longer exists, which is expected." );
		}
	}
	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	return 0;
}

int test_GetLastAccessTime()
{
	try
	{
		String^ path = "D:\\__test_area\\file_path_old.txt";
		// Check the file existency.
		if (  !File::Exists( path ) )
		{
			Console::WriteLine( "File {0} does not exist, creat it.", path);
			File::Create( path );
		}
		File::SetLastAccessTime( path, DateTime(2006,3,11,9,15,30) );
		// Get the creation time of a well-known directory.
		DateTime dt = File::GetLastAccessTime( path );
		Console::WriteLine( "The last access time for this file was {0}.", dt );

		// Update the last access time.
		File::SetLastAccessTime( path, DateTime::Now );
		dt = File::GetLastAccessTime( path );
		Console::WriteLine( "The last access time for this file was {0}.", dt );
	}
	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	return 0;
}


int test_FileFunction1()
{
	String^ path = Path::GetTempFileName();	//取得任意的檔案名稱
	Console::WriteLine(" Get file name {0}" , path);

	FileInfo^ fi1 = gcnew FileInfo( path );
	//Create a file to write to.
	StreamWriter^ sw = fi1->CreateText();
	try
	{
		sw->WriteLine( "Hello" );
		sw->WriteLine( "And" );
		sw->WriteLine( "Welcome" );
	}
	finally
	{
		if ( sw )
			delete (IDisposable^)sw;
	}

	//Open the file to read from.
	StreamReader^ sr = fi1->OpenText();
	try
	{
		String^ s = "";
		while ( s = sr->ReadLine() )
		{
			Console::WriteLine( s );
		}
	}
	finally
	{
		if ( sr )
			delete (IDisposable^)sr;
	}

	try
	{
		String^ path2 = Path::GetTempFileName();	//取得任意的檔案名稱

		Console::WriteLine(" Get file name {0}" , path2);

		FileInfo^ fi2 = gcnew FileInfo( path2 );

		//Ensure that the target does not exist.
		fi2->Delete();

		//Copy the file.
		fi1->CopyTo( path2 );
		Console::WriteLine( "{0} was copied to {1}.", path, path2 );

		//Delete the newly created file.
		fi2->Delete();
		Console::WriteLine( "{0} was successfully deleted.", path2 );
	}
	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	return 0;
}

int test_FileFunction2()
{
	//String^ path = Path::GetTempFileName();	//取得任意的檔案名稱
	String^ path1 = "D:\\__test_area\\file_path_old222222.txt";

	FileInfo^ fi1 = gcnew FileInfo( path1 );
	//Create a file to write to.
	StreamWriter^ sw = fi1->CreateText();
	try
	{
		sw->WriteLine( "Hello" );
		sw->WriteLine( "And" );
		sw->WriteLine( "Welcome" );
	}
	finally
	{
		if ( sw )
			delete (IDisposable^)sw;
	}

	try
	{
		String^ path2 = "D:\\__test_area\\file_path_old222222_copy.txt";

		FileInfo^ fi2 = gcnew FileInfo( path2 );

		//Ensure that the target does not exist.
		fi2->Delete();

		//Copy the file.
		fi1->CopyTo( path2 );
		Console::WriteLine( "{0} was copied to {1}.", path1, path2 );

		/*
		//Delete the newly created file.
		fi2->Delete();
		Console::WriteLine( "{0} was successfully deleted.", path2 );
		*/
	}
	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	Console::WriteLine( "Name: {0}", fi1 -> Name );
	Console::WriteLine( "FullName: {0}", fi1 -> FullName );		//取得目錄或檔案的完整路徑
	Console::WriteLine( "Length: {0} Bytes", fi1 -> Length );	//檔案大小
	Console::WriteLine( "Directory: {0}", fi1 -> Directory );	//父代目錄的執行個體。
	Console::WriteLine( "DirectoryName: {0}", fi1 -> DirectoryName );	//目錄完整路徑的字串
	Console::WriteLine( "Exists: {0}", fi1 -> Exists );		//這個值指出檔案是否存在。
	Console::WriteLine( "IsReadOnly: {0}", fi1 -> IsReadOnly );	//目前檔案是否為唯讀
	Console::WriteLine( "Extension: {0}", fi1 -> Extension );	//表示檔案的副檔名部分
	Console::WriteLine( "Attributes: {0}", fi1 -> Attributes );	//目前檔案或目錄的屬性
	Console::WriteLine( "CreationTime: {0}", fi1 -> CreationTime );	//建立時間
	Console::WriteLine( "CreationTimeUtc: {0}", fi1 -> CreationTimeUtc );	//建立時間，國際標準時間
	Console::WriteLine( "LastAccessTime: {0}", fi1 -> LastAccessTime );	//上次存取時間
	Console::WriteLine( "LastAccessTimeUtc: {0}", fi1 -> LastAccessTimeUtc );	//上次存取時間，國際標準時間
	Console::WriteLine( "LastWriteTime: {0}", fi1 -> LastWriteTime );	//上次寫入時間
	Console::WriteLine( "LastWriteTimeUtc: {0}", fi1 -> LastWriteTimeUtc );	//上次寫入時間，國際標準時間
	return 0;
}


int test_DirectoryFunction1()
{
	try
	{
		String^ path = "c:\\__test_area\\_TestGetLastWriteTime";
		if (  !Directory::Exists( path ) )			//檢查子目錄是否存在
		{
			Directory::CreateDirectory( path );		//建立子目錄
		}
		else
		{
			// Take an action that will affect the write time.
			Directory::SetLastWriteTime( path, DateTime(1985,4,3) );	//設定子目錄最後寫入時間
		}

		// Get the last write time of a well-known directory.
		DateTime dt = Directory::GetLastWriteTime( path );				//取得子目錄最後寫入時間
		Console::WriteLine( "The last write time for this directory was {0}", dt );

		//Update the last write time.
		Directory::SetLastWriteTime( path, DateTime::Now );				//設定子目錄最後寫入時間
		dt = Directory::GetLastWriteTime( path );						//取得子目錄最後寫入時間
		Console::WriteLine( "The last write time for this directory was {0}", dt );
	}
	catch ( Exception^ e )
	{
		Console::WriteLine( "The process failed: {0}", e );
	}
	return 0;
}

int test_DirectoryFunction2()
{
   try
   {
	   Console::WriteLine( "現在的工作目錄： {0}", Environment::CurrentDirectory );
      // Get the creation time of a well-known directory.
      DateTime dt = Directory::GetCreationTime( Environment::CurrentDirectory );	//取得子目錄的建立時間

      // Give feedback to the user.
      if ( DateTime::Now.Subtract( dt ).TotalDays > 364 )
      {
         Console::WriteLine( "This directory is over a year old." );
      }
      else
      if ( DateTime::Now.Subtract( dt ).TotalDays > 30 )
      {
         Console::WriteLine( "This directory is over a month old." );
      }
      else
      if ( DateTime::Now.Subtract( dt ).TotalDays <= 1 )
      {
         Console::WriteLine( "This directory is less than a day old." );
      }
      else
      {
         Console::WriteLine( "This directory was created on {0}", dt );
      }
   }
   catch ( Exception^ e )
   {
      Console::WriteLine( "The process failed: {0}", e );
   }
	return 0;
}

int save_folder_data(void)
{
	String^ dir_path = "D:\\__test_area\\TestFileOperationFiles";
	String^ fid =      "D:\\__test_area\\save_folder_data.txt";

	if (!Directory::Exists(dir_path))
	{
		Console::WriteLine("Directory {0} does not exist, leave.....", dir_path);
		return 0;
	}
	if (File::Exists(fid)){
		//Console::WriteLine("File already exists! Remove it.");
		File::Delete(fid);
		//Console::WriteLine("File {0} removed, continue.....",fid);
	}

	DirectoryInfo^ di = gcnew DirectoryInfo(dir_path);	//實做目錄資料物件

	StreamWriter^ sw = File::CreateText(fid);

	array<DirectoryInfo^> ^fiArr2 = di->GetDirectories();	//由目錄資料物件取出子目錄資料		//GetDirectories() 傳回目前目錄的子目錄。
	//Console::WriteLine("The directory {0} contains the following folders:",di->Name);
	//sw->WriteLine("The directory {0} contains the following folders:",di->Name);

	for each (DirectoryInfo ^f in fiArr2)		//顯示所有檔案名稱與大小
	{
		/*
		if((f->Attributes & FileAttributes::Directory) == FileAttributes::Directory)
			Console::WriteLine("{0} is a directory",f->Name);
		else
			Console::WriteLine("{0} is a file",f->Name);
		*/

		Console::WriteLine("Folder {0}:",f->Name);

		array<FileInfo^> ^fiArr2 = f->GetFiles();
		for each (FileInfo ^f in fiArr2)		//子目錄內的所有檔案
		{
			/*
			if((f->Attributes & FileAttributes::Directory) == FileAttributes::Directory)
				Console::WriteLine("{0} is a directory",f->Name);
			else
				Console::WriteLine("{0} is a file",f->Name);
			*/

			if(f->Extension == ".jpg")
			{
				Console::WriteLine("{0,30} {1} bytes. {2}",f->Name, f->Length, f->Extension);
				sw->WriteLine("{0,-30} {1,10} bytes. {2,5}",f->Name, f->Length, f->Extension);
			}
		}
		Console::WriteLine();
	}

	sw->WriteLine();
	sw->WriteLine();

	array<FileInfo^> ^fiArr = di->GetFiles();			//由目錄資料物件取出檔案資料		//GetFiles() 從目前的目錄傳回檔案清單。
	Console::WriteLine("The directory {0} contains the following files:",di->Name);
	sw->WriteLine("The directory {0} contains the following files:",di->Name);

	for each (FileInfo ^f in fiArr)		//顯示所有檔案名稱與大小
	{
		/*
		if((f->Attributes & FileAttributes::Directory) == FileAttributes::Directory)
			Console::WriteLine("{0} is a directory",f->Name);
		else
			Console::WriteLine("{0} is a file",f->Name);
		*/
		if(f->Extension == ".jpg")
		{
			Console::WriteLine("{0,30} {1} bytes. {2}",f->Name, f->Length, f->Extension);
			sw->WriteLine("{0,-30} {1,10} bytes. {2,5}",f->Name, f->Length, f->Extension);
		}
	}
	Console::WriteLine();


	/*
	//實做檔案資料物件
	FileInfo^ f = gcnew FileInfo("D:\\__test_area\\TestFileOperationFiles\\folder1\\pic016.jpg");
	Console::WriteLine("\n{0} ----- {1} bytes.",f->Name, f->Length);
	*/

	sw->Close();
	//Console::Write("Process was completed!\n");

	return 0;
}


int bin2hex(void)
{
	Console::WriteLine("Read a binary file and convert it to hex file");

	array<Byte>^ data=File::ReadAllBytes("D:\\__test_area\\TestFileOperationFiles\\samsung_46es6600.bin");

	//Console::WriteLine("File length");

	printf("File length is %d\n",data->Length);

	String^ fid = "D:\\__test_area\\TestFileOperationFiles\\samsung_46es660022222.txt";

	if (File::Exists(fid)){
		Console::WriteLine("File already exists! Remove it.");
		File::Delete(fid);
		Console::WriteLine("File {0} removed, continue.....",fid);
	}

	StreamWriter^ sw = File::CreateText(fid);

	//開始寫資料到檔案裏面
	for(int i=0;i<data->Length;i++)
	{
		sw->Write("{0:X2}",data[i]);	//十六進位、二位數
		if((i%16)==15)
			sw->WriteLine();
		else
			sw->Write(" ");
	}
	sw->WriteLine();
	sw->Close();
	Console::Write("Process was completed!\n");
	return 0;
}

int test_file_read_write_binary()
{
	Console::WriteLine("Read binary file test.bin and write its data to testnew.bin");
	array<Byte>^ data=File::ReadAllBytes("D:\\__test_area\\TestFileOperationFiles\\samsung_46es6600.bin");

	Console::WriteLine("File length");

	printf("File length is %d\n",data->Length);

	printf("[vincent]: Content of the binary data:\n");
	for(int i=0;i<data->Length;i++)
	{
		printf("%02x,",data[i]);
		if((i%16)==15)
			printf("\n");
		if(i==127)
			printf("\n");
	}
	printf("\n");

	printf("Change some values...........\n");
	data[0x00]=0x01;
	data[0x01]=0x92;
	data[0x0E]=0x06;
	data[0x11]=0x02;
	data[0xFF]=0x01;

	printf("Save data to another file.\n");

	String^ new_file_path = gcnew String ( "D:\\__test_area\\TestFileOperationFiles\\samsung_46es660022222.bin" );

	File::WriteAllBytes( new_file_path , data );

	Console::Write("Process was completed!\n");

	return 0;
}

