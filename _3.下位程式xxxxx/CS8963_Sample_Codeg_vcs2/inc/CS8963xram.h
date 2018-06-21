#define XBYTE ((unsigned char volatile xdata *) 0)

#define  REGTRM    	XBYTE[0XA000]
#define  IOSCITRM  	XBYTE[0XA001]
#define  IOSCVTRM  	XBYTE[0XA002]
#define  T5CON		XBYTE[0xa003]
#define  T5L		XBYTE[0xa004]
#define  T5H		XBYTE[0xa005]
#define  T5T		XBYTE[0xa006]
#define  XOSCCFG   	XBYTE[0XA007]
#define  RTCSCND0	XBYTE[0xa008]
#define  RTCSCND1	XBYTE[0xa009]
#define  RTCSCND2	XBYTE[0xa00a]
#define  RTCSCND3	XBYTE[0xa00b]
#define  RTCCNTL	XBYTE[0xa00c]
#define  RTCCNTH	XBYTE[0xa00d]
#define  RTCCMD    	XBYTE[0XA00E]
#define  RTCDATA   	XBYTE[0XA00F]
#define  LVDCFG    	XBYTE[0XA010]
#define  LVDTHD    	XBYTE[0XA011]
#define  INTPCT1	XBYTE[0xa013]
#define  INTPCT2	XBYTE[0xa014]
#define  COMPCFG	XBYTE[0xa017]

#define FLSHADM  XBYTE[0xa012]
#define FLSHCMD  XBYTE[0xa020]
#define FLSHDAT  XBYTE[0xa021]
#define FLSHADH  XBYTE[0xa022]
#define FLSHADL  XBYTE[0xa023]
#define ISPCLKF  XBYTE[0xa024]
#define CNTPCTL XBYTE[0xa025]
#define CNTPCTH XBYTE[0xa026]

#define  PIOEDGR0  XBYTE[0xA028]
#define  PIOEDGR1  XBYTE[0xA029]
#define  PIOEDGR2  XBYTE[0xA02A]
#define  PIOEDGR3  XBYTE[0xA02B]
#define  PIOEDGR4  XBYTE[0xA02C]
#define  PIOEDGR5  XBYTE[0xA02D]

#define  CMPCFGAB  XBYTE[0xA030]
#define  CMPCFGCD  XBYTE[0xA031]
#define  CMPVTH0  XBYTE[0xA032]
#define  CMPVTH1  XBYTE[0xA033]
#define  DACL  	  XBYTE[0xA036]
#define  DACH     XBYTE[0xA037]
#define  PIOEDGF0  XBYTE[0xA038]
#define  PIOEDGF1  XBYTE[0xA039]
#define  PIOEDGF0  XBYTE[0xA038]
#define  PIOEDGF1  XBYTE[0xA039]
#define  PIOEDGF2  XBYTE[0xa03a]
#define  PIOEDGF3  XBYTE[0xa03b]
#define  PIOEDGF4  XBYTE[0xa03c]
#define  PIOEDGF5  XBYTE[0xa03d]

#define  IOCFGP0_0  XBYTE[0XA040]
#define  IOCFGP0_1  XBYTE[0XA041]
#define  IOCFGP0_2  XBYTE[0XA042]
#define  IOCFGP0_3  XBYTE[0XA043]
#define  IOCFGP0_4  XBYTE[0XA044]
#define  IOCFGP0_5  XBYTE[0XA045]
#define  IOCFGP0_6  XBYTE[0XA046]
#define  IOCFGP0_7  XBYTE[0XA047]
#define  IOCFGP1_0  XBYTE[0XA048]
#define  IOCFGP1_1  XBYTE[0XA049]
#define  IOCFGP1_2  XBYTE[0XA04A]
#define  IOCFGP1_3  XBYTE[0XA04B]
#define  IOCFGP1_4  XBYTE[0XA04C]
#define  IOCFGP1_5  XBYTE[0XA04D]
#define  IOCFGP1_6  XBYTE[0XA04E]
#define  IOCFGP1_7  XBYTE[0XA04F]

#define  MFCFGP0_0  XBYTE[0XA050]
#define  MFCFGP0_1  XBYTE[0XA051]
#define  MFCFGP0_2  XBYTE[0XA052]
#define  MFCFGP0_3  XBYTE[0XA053]
#define  MFCFGP0_4  XBYTE[0XA054]
#define  MFCFGP0_5  XBYTE[0XA055]
#define  MFCFGP0_6  XBYTE[0XA056]
#define  MFCFGP0_7  XBYTE[0XA057]
#define  MFCFGP1_0  XBYTE[0XA058]
#define  MFCFGP1_1  XBYTE[0XA059]
#define  MFCFGP1_2  XBYTE[0XA05A]
#define  MFCFGP1_3  XBYTE[0XA05B]
#define  MFCFGP1_4  XBYTE[0XA05C]
#define  MFCFGP1_5  XBYTE[0XA05D]
#define  MFCFGP1_6  XBYTE[0XA05E]
#define  MFCFGP1_7  XBYTE[0XA05F]

#define  IOCFGP2_0  XBYTE[0XA060]
#define  IOCFGP2_1  XBYTE[0XA061]
#define  IOCFGP2_2  XBYTE[0XA062]
#define  IOCFGP2_3  XBYTE[0XA063]
#define  IOCFGP2_4  XBYTE[0XA064]
#define  IOCFGP2_5  XBYTE[0XA065]
#define  IOCFGP2_6  XBYTE[0XA066]
#define  IOCFGP2_7  XBYTE[0XA067]
#define  IOCFGP3_0  XBYTE[0XA068]
#define  IOCFGP3_1  XBYTE[0XA069]
#define  IOCFGP3_2  XBYTE[0XA06A]
#define  IOCFGP3_3  XBYTE[0XA06B]
#define  IOCFGP3_4  XBYTE[0XA06C]
#define  IOCFGP3_5  XBYTE[0XA06D]
#define  IOCFGP3_6  XBYTE[0XA06E]
#define  IOCFGP3_7  XBYTE[0XA06F]

#define  MFCFGP2_0  XBYTE[0XA070]
#define  MFCFGP2_1  XBYTE[0XA071]
#define  MFCFGP2_2  XBYTE[0XA072]
#define  MFCFGP2_3  XBYTE[0XA073]
#define  MFCFGP2_4  XBYTE[0XA074]
#define  MFCFGP2_5  XBYTE[0XA075]
#define  MFCFGP2_6  XBYTE[0XA076]
#define  MFCFGP2_7  XBYTE[0XA077]
#define  MFCFGP3_0  XBYTE[0XA078]
#define  MFCFGP3_1  XBYTE[0XA079]
#define  MFCFGP3_2  XBYTE[0XA07A]
#define  MFCFGP3_3  XBYTE[0XA07B]
#define  MFCFGP3_4  XBYTE[0XA07C]
#define  MFCFGP3_5  XBYTE[0XA07D]
#define  MFCFGP3_6  XBYTE[0XA07E]
#define  MFCFGP3_7  XBYTE[0XA07F]

#define  PWMAL  XBYTE[0xa080]
#define  PWMAH  XBYTE[0xa081]
#define  PWMBL  XBYTE[0xa082]
#define  PWMBH  XBYTE[0xa083]
#define  PWMCL  XBYTE[0xa084]
#define  PWMCH  XBYTE[0xa085]

#define  PWMTRG0L   XBYTE[0xa086]
#define  PWMTRG0H   XBYTE[0xa087]
#define  PWMTRG1L   XBYTE[0xa088]
#define  PWMTRG1H   XBYTE[0xa089]
#define  PWMCNTL    XBYTE[0xa08a]
#define  PWMCNTH    XBYTE[0xa08b]
#define  PWMPRDL    XBYTE[0xa08c]
#define  PWMPRDH    XBYTE[0xa08d]
#define  PWM16CFG   XBYTE[0xa08e]
#define  PWM16INT   XBYTE[0xa08f]

#define  LINCTRL	XBYTE[0xa090]
#define  LINCNTRH	XBYTE[0xa091]
#define  LINCNTRL	XBYTE[0xa092]
#define  LINSBRH	XBYTE[0xa093]
#define  LINSBRL	XBYTE[0xa094]
#define  LININT		XBYTE[0xa095]
#define  LININTEN	XBYTE[0xa096]
#define  PWM16EMG   XBYTE[0xa097]

#define  DBPCIDL   XBYTE[0xa098]
#define  DBPCIDH   XBYTE[0xa099]
#define  DBPCIDT   XBYTE[0xa09a]
#define  DBPCNXL   XBYTE[0xa09b]
#define  DBPCNXH   XBYTE[0xa09c]
#define  DBPCNXT   XBYTE[0xa09d]
#define  PWM16CHS  XBYTE[0xa09f]

#define  PCACPS		XBYTE[0xa0a5]
#define  CLRLD		XBYTE[0xa0a6]
#define  CHRLD		XBYTE[0xa0a7]

#define  IOCFGP4_0   XBYTE[0xa0c0]
#define  IOCFGP4_1   XBYTE[0xa0c1]
#define  IOCFGP4_2   XBYTE[0xa0c2]
#define  IOCFGP4_3   XBYTE[0xa0c3]
#define  IOCFGP4_4   XBYTE[0xa0c4]
#define  IOCFGP4_5   XBYTE[0xa0c5]
#define  IOCFGP4_6   XBYTE[0xa0c6]
#define  IOCFGP4_7   XBYTE[0xa0c7]

#define  IOCFGP5_1   XBYTE[0xa0c8]
#define  IOCFGP5_2   XBYTE[0xa0c9]
#define  IOCFGP5_3   XBYTE[0xa0ca]
#define  IOCFGP5_4   XBYTE[0xa0cb]
#define  IOCFGP5_5   XBYTE[0xa0cc]
#define  IOCFGP5_6   XBYTE[0xa0cd]
#define  IOCFGP5_7   XBYTE[0xa0ce]
#define  IOCFGP5_8   XBYTE[0xa0cf]


#define  MFCFGP4_0   XBYTE[0xa0d0]
#define  MFCFGP4_1   XBYTE[0xa0d1]
#define  MFCFGP4_2   XBYTE[0xa0d2]
#define  MFCFGP4_3   XBYTE[0xa0d3]
#define  MFCFGP4_4   XBYTE[0xa0d4]
#define  MFCFGP4_5   XBYTE[0xa0d5]
#define  MFCFGP4_6   XBYTE[0xa0d6]
#define  MFCFGP4_7   XBYTE[0xa0d7]

#define  MFCFGP5_1   XBYTE[0xa0d8]
#define  MFCFGP5_2   XBYTE[0xa0d9]
#define  MFCFGP5_3   XBYTE[0xa0da]
#define  MFCFGP5_4   XBYTE[0xa0db]
#define  MFCFGP5_5   XBYTE[0xa0dc]
#define  MFCFGP5_6   XBYTE[0xa0dd]
#define  MFCFGP5_7   XBYTE[0xa0de]
#define  MFCFGP5_8   XBYTE[0xa0df]

#define  BPINTF      XBYTE[0xa0e0]
#define  BPINTE      XBYTE[0xa0e1]
#define  BPINTC      XBYTE[0xa0e2]
#define  BPCTRL      XBYTE[0xa0e3]
#define  PC5AL       XBYTE[0xa0e4]
#define  PC5AH       XBYTE[0xa0e5]
#define  PC5AT       XBYTE[0xa0e6]

#define  PC6AL       XBYTE[0xa0e8]
#define  PC6AH       XBYTE[0xa0e9]
#define  PC6AT       XBYTE[0xa0ea]
#define  PC7AL       XBYTE[0xa0ec]
#define  PC7AH       XBYTE[0xa0ed]
#define  PC7AT       XBYTE[0xa0ee]
#define  SI2CDBGID   XBYTE[0xa0ef]

#define  PC1AL       XBYTE[0xa0f0]
#define  PC1AH       XBYTE[0xa0f1]
#define  PC1AT       XBYTE[0xa0f2]
#define  PC2AL       XBYTE[0xa0f4]
#define  PC2AH       XBYTE[0xa0f5]
#define  PC2AT       XBYTE[0xa0f6]

#define  PC3AL       XBYTE[0xa0f8]
#define  PC3AH       XBYTE[0xa0f9]
#define  PC3AT       XBYTE[0xa0fa]
#define  PC4AL       XBYTE[0xa0fc]
#define  PC4AH       XBYTE[0xa0fd]
#define  PC4AT       XBYTE[0xa0fe]

#define	PinC_In				0x80
#define	PinC_InPuUp			0xa0
#define	PinC_InPuDn			0x90
#define	PinC_InHold			0xc0

#define	PinC_InOutCMOS		0x86
#define	PinC_InOut51like	0xE2
#define	PinC_InOutCMOSUp	0xa6

#define	PinC_OutCMOS		0x06
#define	PinC_OutNMOS		0x02
#define	PinC_OutNMOSUp		0x22
#define	PinC_OutPMOS		0x04
#define	PinC_OutPMOSUp		0x24
#define PinC_OpenDrain      0x82
#define	PinC_Analog 		0x08
#define	PinC_OSC			0x00
//IO Config					INEN	LATEN	PUEN	PDEN	:	ANEN	PDRVEN	NDRVEN	__
#define	PinF_IO				0x01
#define	PinF_ADC			0x04

#define	AllSeting			PinC_InOutCMOS

//IOCFGP
#define _NDRVEN_			0x02  	// NMOS driver output enable
#define _PDRVEN_			0x04  	// PMOS driver output enable
#define _ANEN_	    		0x08  	// Analog switch enable
#define _PDEN_	    		0x10  	// pull down resistor enable
#define _PUEN_     			0x20  	// pull up resistor enable
#define _LATEN_	    		0x40  	// bus latch enable
#define _INEN_	    		0x80  	// input enable

//MFCFGP
#define _GPIOEN_			0x01  	// as GPIO function pin
#define _PINTEN_			0x02  	// as external interrupt pin
#define _ADA1EN_			0x04  	// as ADC pin
#define _PINTEDG_			0x08  	// interrupt edge 
