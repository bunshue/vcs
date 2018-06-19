
/*---------------------------------------------------------------------------
  Defined registers
---------------------------------------------------------------------------*/

/*  BYTE Register  */
  sfr P0        = 0x80;   /* Port 0                    */
  sfr SP        = 0x81;   /* Stack Pointer             */
  sfr DPL       = 0x82;   /* Data Pointer 0 Low byte   */
  sfr DPH       = 0x83;   /* Data Pointer 0 High byte  */
  sfr DPL1      = 0x84;
  sfr DPH1      = 0x85;
  sfr DPS       = 0x86;
  sfr PCON      = 0x87;   /* Power Configuration       */

  sfr TCON      = 0x88;   /* Timer 0,1 Configuration   */
  sfr TMOD      = 0x89;   /* Timer 0,1 Mode            */
  sfr TL0       = 0x8A;   /* Timer 0 Low byte counter  */
  sfr TL1       = 0x8B;   /* Timer 1 Low byte counter  */
  sfr TH0       = 0x8C;   /* Timer 0 High byte counter */
  sfr TH1       = 0x8D;   /* Timer 1 High byte counter */
  sfr CKCON     = 0x8E;   /* Timer 1 High byte counter */
  sfr CKSEL     = 0x8F;   /* Timer 1 High byte counter */

  sfr P1        = 0x90;   /* Port 1                    */
  sfr EXIF      = 0x91;
  sfr WTST      = 0x92;   /* Program Wait States       */
  sfr DPX       = 0x93;   /* Data Page Pointer 0       */
  sfr CMPST     = 0x94;
  sfr DPX1      = 0x95;

  sfr SCON0     = 0x98;		/* Serial 0 Configuration    */
  sfr SBUF0     = 0x99;		/* Serial 0 I/O Buffer       */
  sfr ESP       = 0x9B;
  sfr ACON      = 0x9D;
  sfr I2CSADR3	= 0X9E;
  sfr WKMASK    = 0x9F;


  sfr P2        = 0xA0;   /* Port 2                    */
  sfr SPICR     = 0xA1;
  sfr SPIMR     = 0xA2;
  sfr SPIST     = 0xA3;
  sfr SPIDAT    = 0xA4;
  sfr SFIFO2    = 0xA5;
  sfr SBUF2     = 0xA6;
  sfr SINT2     = 0xA7;
  sfr IE        = 0xA8;   /* Interrupt Enable          */
  sfr ADCCFG    = 0xA9;
  sfr ADCDL     = 0xAA;
  sfr ADCDH     = 0xAB;

  sfr T4L		= 0xAC;
  sfr T4H		= 0xAD;
  sfr T3L		= 0xAE;
  sfr T3H		= 0xAF;

  sfr P3        = 0xB0;   /* Port 3                    */
  sfr CCAPM0    = 0xB2;
  sfr CCAPM1    = 0xB3;
  sfr CCAPM2    = 0xB4;
  sfr CCAPM3    = 0xB5;
  sfr CCAPM4    = 0xB6;
  sfr CCAPM5    = 0xB7;
  sfr IP        = 0xB8;
  sfr ADCCHSL   = 0xB9;
  sfr ADCAL     = 0xBA;
  sfr ADCAH     = 0xBB;
  sfr ADCBL     = 0xBC;
  sfr ADCBH     = 0xBD;
  sfr ADCCL     = 0xBE;
  sfr ADCCH     = 0xBF;

  sfr SCON2     = 0xC2;
  sfr SBAUD2  = 0xc3;
  sfr PMR       = 0xC4;
  sfr STATUS    = 0xC5;
  sfr MCON      = 0xC6;
  sfr TA        = 0xC7;
  sfr T2CON     = 0xC8;
  sfr TB        = 0xC9;
  sfr RLDL      = 0xCA;
  sfr RLDH      = 0xCB;
  sfr TL2       = 0xCC;
  sfr TH2       = 0xCD;
  sfr ADCAVG    = 0xCE;
  sfr T34CON    = 0xCF;

  sfr PSW       = 0xD0;
  sfr PCAMOD    = 0xD1;
  sfr CCAP0L    = 0xD2;
  sfr CCAP0H    = 0xD3;
  sfr CCAP1L    = 0xD4;
  sfr CCAP1H    = 0xD5;
  sfr CCAP2L    = 0xD6;
  sfr CCAP2H    = 0xD7;
  sfr WDCON     = 0xD8;
  sfr CL        = 0xD9;
  sfr DPXR      = 0xDA;
  sfr I2CSCON2  = 0xDB;
  sfr I2CSST2   = 0xDC;
  sfr I2CSADR2  = 0xDD;
  sfr I2CSDAT2  = 0xDE;

  sfr ACC       = 0xE0;
  sfr PCACON    = 0xE1;
  sfr CCAP3L    = 0xE2;
  sfr CCAP3H    = 0xE3;
  sfr CCAP4L    = 0xE4;
  sfr CCAP4H    = 0xE5;
  sfr CCAP5L    = 0xE6;
  sfr CCAP5H    = 0xE7;
  sfr EXIE      = 0xE8;
  sfr CH        = 0xE9;
  sfr MXAX      = 0xEA;
  sfr I2CSCON1  = 0xEB;
  sfr I2CSST1   = 0xEC;
  sfr I2CSADR1  = 0xED;
  sfr I2CSDAT1  = 0xEE;

  sfr B         = 0xF0;   /* B Working register        */
  sfr CLSR      = 0xF2;
  sfr CHSR      = 0xF3;
  sfr I2CMSA    = 0xF4;
  sfr I2CMCR    = 0xF5;
  sfr I2CMBUF   = 0xF6;
  sfr I2CMTP    = 0xF7;
  sfr EXIP      = 0xF8;
  sfr MD0       = 0xF9;
  sfr MD1       = 0xFA;
  sfr MD2       = 0xFB;
  sfr MD3       = 0xFC;
  sfr MD4       = 0xFD;
  sfr MD5       = 0xFE;
  sfr ARCON     = 0xFF;



/*-------------------------------------------------------------------------
  BIT Register
  -------------------------------------------------------------------------*/

/*  P0  */

  sbit P0_7     = P0^7;
  sbit P0_6     = P0^6;
  sbit P0_5     = P0^5;
  sbit P0_4     = P0^4;
  sbit P0_3     = P0^3;
  sbit P0_2     = P0^2;
  sbit P0_1     = P0^1;
  sbit P0_0     = P0^0;

/*  P1  */
  sbit P1_7     = P1^7;
  sbit P1_6     = P1^6;
  sbit P1_5     = P1^5;
  sbit P1_4     = P1^4;
  sbit P1_3     = P1^3;
  sbit P1_2     = P1^2;
  sbit P1_1     = P1^1;
  sbit P1_0     = P1^0;

/*  P2  */
  sbit P2_7     = P2^7;
  sbit P2_6     = P2^6;
  sbit P2_5     = P2^5;
  sbit P2_4     = P2^4;
  sbit P2_3     = P2^3;
  sbit P2_2     = P2^2;
  sbit P2_1     = P2^1;
  sbit P2_0     = P2^0;

/*  P3  */
  sbit P3_7     = P3^7;
  sbit P3_6     = P3^6;
  sbit P3_5     = P3^5;
  sbit P3_4     = P3^4;
  sbit P3_3     = P3^3;
  sbit P3_2     = P3^2;
  sbit P3_1     = P3^1;
  sbit P3_0     = P3^0;

/*  TCON  */
  sbit IT0      = TCON^0;
  sbit PINT0F   = TCON^1;	//Pin INT0 Interrupt Flag bit
  sbit IT1      = TCON^2;
  sbit PINT1F   = TCON^3;	//Pin INT1 Interrupt Flag bit
  sbit TR0      = TCON^4;		//Timer 0 Run Control bit. Set to enable Timer 0
  sbit TF0      = TCON^5;		//Timer 0 Interrupt Flag. TF0 is cleared by hardware when entering the interrupt routine
  sbit TR1      = TCON^6;		//Timer 1 Run Control bit. Set to enable Timer 1
  sbit TF1      = TCON^7;		//Timer 1 Interrupt Flag bit. TF1 is cleared by hardware when entering the interrupt routine

/*  T2CON  */
  sbit CPRL2   = T2CON^0;
  sbit CT2     = T2CON^1;
  sbit TR2     = T2CON^2;
  sbit EXEN2   = T2CON^3;
  sbit TCLK    = T2CON^4;
  sbit RCLK    = T2CON^5;
  sbit EXF2    = T2CON^6;
  sbit TF2     = T2CON^7;

/*  SCON0 */
  sbit RI0      = SCON0^0;
  sbit TI0      = SCON0^1;
  sbit RB08     = SCON0^2;
  sbit TB08     = SCON0^3;
  sbit REN0     = SCON0^4;
  sbit SM02     = SCON0^5;
  sbit SM01     = SCON0^6;
  sbit SM00     = SCON0^7;

/*  IE   */
  sbit PINT0EN      = IE^0;		//Pin PINT0.x Interrupt Enable bit
  sbit ET0      = IE^1;			//Timer 0 Interrupt Enable bit
  sbit PINT1EN      = IE^2;		//Pin PINT1.x Interrupt Enable bit
  sbit ET1      = IE^3;			//Timer 1 Interrupt Enable bit
  sbit ES0      = IE^4;			//UART0 Interrupt Enable bit
  sbit ET2      = IE^5;			//Timer 2 Interrupt Enable bit
  sbit ES       = IE^6;			//LIN-capable 16550-like UART2 Interrupt Enable bit
  sbit EA       = IE^7;			//Global Interrupt Enable bit

/*  EXIE   */
  sbit mIIC_EN  = EXIE^0;		//I2C Master Interrupt Enable bit
  sbit LVDT_EN  = EXIE^1;		//Low Voltage Detection Interrupt Enable bit
  sbit CMP_EN   = EXIE^2;		//Analog Comparator Interrupt and CAN Interrupt Enable bit
  sbit ADC_EN   = EXIE^3;		//ADC/PWM Interrupt Enable bit
  sbit WDT_EN   = EXIE^4;		//Watchdog Timer Interrupt Enable bit
  sbit PCA_EN   = EXIE^5;		//PCA Interrupt Enable bit
  sbit SPI_sIIC_EN   = EXIE^6;	//SPI and I2C Slave Interrupt Enable bit
  sbit RTC_EN   = EXIE^7;		//RTC Interrupt Enable and Timer 3 Interrupt Enable bit

/*  IP   */
  sbit PX0      = IP^0;
  sbit PT0      = IP^1;
  sbit PX1      = IP^2;
  sbit PT1      = IP^3;
  sbit PS0      = IP^4;
  sbit PT2      = IP^5;
  sbit PS2      = IP^7;

/*  PSW   */
  sbit P        = PSW^0;
  sbit F1       = PSW^1;
  sbit OV       = PSW^2;
  sbit RS0      = PSW^3;
  sbit RS1      = PSW^4;
  sbit F0       = PSW^5;
  sbit AC       = PSW^6;
  sbit CY       = PSW^7;


  sbit EI2CMP   = EXIP^0;
  sbit EINT2P   = EXIP^1;
  sbit EINT3P   = EXIP^2;
  sbit EINT4P   = EXIP^3;
  sbit EWDIP    = EXIP^4;
  sbit EINT6P   = EXIP^5;
  sbit EINT7P   = EXIP^6;
  sbit EINT8P   = EXIP^7;


/*  WDCON   */
  sbit RWT       = WDCON^0;
  sbit EWT       = WDCON^1;
  sbit WTRF      = WDCON^2;
  sbit WDIF      = WDCON^3;

/*  EUART2   */
#define EUART2_TIF									(SINT2 & 0x01)
#define EUART2_TIF_CLR								(SINT2 &= (~0x01))
#define EUART2_RIF									(SINT2 & 0x20)
#define EUART2_RIF_CLR								(SINT2 &= (~0x20))

/*-------------------------------------------------------------------------
  BIT Values
  -------------------------------------------------------------------------*/

/* TMOD Bit Values */
  #define T0_M0_   0x01
  #define T0_M1_   0x02
  #define T0_CT_   0x04
  #define T0_GATE_ 0x08
  #define T1_M0_   0x10
  #define T1_M1_   0x20
  #define T1_CT_   0x40
  #define T1_GATE_ 0x80

/* CKCON Bit Values  */
  #define MD_    0x07
  #define T0M_   0x08
  #define T1M_   0x10
  #define T2M_   0x20
