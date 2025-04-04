
//7.1 general status

0x0100 MODE_SELECT
0x0103 SOFTWARE_RESET
0x0106 FAST_STANDBY_CTRL
0x300A Hi CHIP ID
0x300B Lo CHIP ID
0x302A CHIP REVISION
0x3820 IMAGE_ORIENTATION
0x4A00 FRAME_COUNT


//7.2 SCCB control
0x0107 CCI_ADDRESS_PGM_ID
0x3031 SCCB

//7.3 IO control

0x3001 PCLK_HREF_VSYNC OEN
0x3002 IO Y OEN
0x3009 OUTPUT DRIVE CAPABILITY CTRL

//7.4 clock configuration

0x3080 PRE_PLL_CLK_DIV
0x3081 PLL_MULTIPLIER
0x3082 VT_SYS_CLK_DIV
0x3083 VT_PIXEL_CLK_DIV
0x3103 SYS_CLK_DIV
0x301E SPI_CLK_DIV

//7.5 gain/exposure control

0x3501 Hi EXPO
0x3502 Lo EXPO
0x3503 GAIN_EXPO_CTRL
0x350A Hi GAIN
0x350B Lo GAIN


//7.6 analog control [0x3600 ~ 0x363F]
0x3600~0x363F RSVD

//7.7 sensor control [0x3700 ~ 0x370C]

0x3700~0x370C RSVD

//7.8 PSRAM control [0x3780 ~ 0x3785]


0x3780~0x3785 RSVD

//7.9 frame timing [0x3800 ~ 0x381D, 0x3820 ~ 0x3829]

0x3800 H_CROP_START_H
0x3801 H_CROP_START_L
0x3802 V_CROP_START_H
0x3803 V_CROP_START_L
0x3804 H_CROP_END_H
0x3805 H_CROP_END_L
0x3806 V_CROP_END_H
0x3807 V_CROP_END_L
0x3808 H_OURPUT_SIZE_H
0x3809 H_OUTPUT_SIZE_L
0x380A V_OUTPUT_SIZE_H
0x380B V_OUTPUT_SIZE_L
0x380C TIMING_HTS_H
0x380D TIMING_HTS_L
0x380E TIMING_VTS_H
0x380F TIMING_VTS_L
0x3810 H_WIN_OFF_H
0x3811 H_WIN_OFF_L
0x3812 V_WIN_OFF_H
0x3813 V_WIN_OFF_L
0x3814 VSYNC CS POINT_H
0x3815 VSYNC CS POINT_L
0x3816 VSYNC START ROW_H
0x3817 VSYNC START ROW_L
0x3818 VSYNC END ROW_H
0x3819 VSYNC END ROW_L
0x381A HSYNC FIRST_H
0x381B HSYNC FIRST_L
0x381C REG1C_H
0x381D REG1C_L
0x3820 FORMAT0
0x3821 FORMAT1
0x3822 CS RST FSIN_H
0x3823 CS RST FSIN_L
0x3824 R RST FSIN_H
0x3825 R RST FSIN_L
0x3826 FVTS_H
0x3827 FVTS_L
0x3828 LN SYNC POINT_H
0x3829 LN SYNC POINT_L

//7.10 AEC control
0x3A00 AEC CTRL0
0x3A01 MIN EXPO
0x3A02 AEC CTRL2
0x3A03 AEC CTRL3
0x3A04 AEC CTRL4
0x3A05 AEC CTRL5
0x3A06 B50 STEP_H
0x3A07 B50 STEP_L
0x3A08 B60 STEP_H
0x3A09 B60 STEP_L
0x3A0A B50 EXPO MAX_H
0x3A0B B50 EXPO MAX_L
0x3A0C B60 EXPO MAX_H
0x3A0D B60 EXPO MAX_L
0x3A0E VTS_50_H
0x3A0F VTS_50_L
0x3A10 VTS_60_H
0x3A11 VTS_60_L
0x3A12 MAX GAIN_H
0x3A13 MAX GAIN_L
0x3A14 MIN GAIN
0x3A15 AEC CTRL15
0x3A16 AEC CTRL16
0x3A17 AEC CTRL17
0x3A18 AEC CTRL18
0x3A19 AEC CTRL19
0x3A1A AEC CTRL1A

//7.11 BLC control
0x4000 BLC CTRL00
0x4001 BLC CTRL01
0x4002 BLK LVL TARGET_H
0x4003 BLK LVL TARGET_L
0x4004 HWIN OFF_H
0x4005 HWIN OFF_L
0x4006 HWIN PAD_H
0x4007 HWIN PAD_L
0x4008 BLC CTRL08
0x4009 BLC CTRL09
0x400A OFF LIM TH_H
0x400B OFF LIM TH_L
0x400C~0x400D RSVD
0x400E BLC CTRL 0E
0x400F BLC CTRL 0F
0x4010 BLC CTRL10
0x4011 BLC CTRL11
0x4012 BLC CTRL12
0x4013 BLC CTRL13
0x4014 BLC CTRL14
0x4015 BLC CTRL15
0x4016 OFF TRIG TH_H
0x4017 OFF TRIG TH_L
0x4018~0x401F RSVD
0x4020 OFF CMP TH000
0x4021 OFF CMP K000
0x4022 OFF CMP TH001
0x4023 OFF CMP K001
0x4024 OFF CMP TH010
0x4025 OFF CMP K010
0x4026 OFF CMP TH011
0x4027 OFF CMP K011
0x4028 OFF CMP TH100
0x4029 OFF CMP K100
0x402A OFF CMP TH101
0x402B OFF CMP K101
0x402C OFF CMP TH110
0x402D OFF CMP K110
0x402E OFF CMP TH111
0x402F OFF CMP K111
0x4030 OFF MAN000_H
0x4031 OFF MAN000_L
0x4032 OFF MAN001_H
0x4033 OFF MAN001_L
0x4034 OFF MAN010_H
0x4035 OFF MAN010_L
0x4036 OFF MAN011_H
0x4037 OFF MAN011_L
0x4038 OFF MAN100_H
0x4039 OFF MAN100_L
0x403A OFF MAN101_H
0x403B OFF MAN101_L
0x403C OFF MAN110_H
0x403D OFF MAN110_L
0x403E OFF MAN111_H
0x403F OFF MAN111_L
0x4040 BLC OFFSET000_H
0x4041 BLC OFFSET000_L
0x4042 BLC OFFSET001_H
0x4043 BLC OFFSET001_L
0x4044 BLC OFFSET010_H
0x4045 BLC OFFSET010_L
0x4046 BLC OFFSET011_H
0x4047 BLC OFFSET011_L
0x4048 BLC OFFSET100_H
0x4049 BLC OFFSET100_L
0x404A BLC OFFSET101_H
0x404B BLC OFFSET101_L
0x404C BLC OFFSET110_H
0x404D BLC OFFSET110_L
0x404E BLC OFFSET111_H
0x404F BLC OFFSET111_L


//7.12 frame control [0x4201 ~ 0x4202]

0x4201 FC CTRL1
0x4202 FC CTRL2


//7.13 output data clipping [0x4300 ~ 0x4307]
0x4300 YMAX_H
0x4301 YMAX_L
0x4302 YMIN_H
0x4303 YMIN_L
0x4304 UVMAX_H
0x4305 UVMAX_L
0x4306 UVMIN_H
0x4307 UVMIN_L


//7.14 output format control [0x4308]

0x4308 FMT CTRL


//7.15 DVP control

0x4700 RSVD
0x4701 VSYNC WIDTH LINE
0x4702 VSYNC WIDTH PIXEL_H
0x4703 VSYNC WIDTH PIXEL_L
0x4704 VSYNC MODE
0x4705 VSYNC DELAY_H
0x4706 VSYNC DELAY_M
0x4707 VSYNC DELAY_L
0x4708 POLARITY CTRL

//7.16 SPI control [0x4F01 ~ 0x4F02]
0x4F01 CORE REG1
0x4F02 CORE REG2


//7.17 ISP control [0x5000 ~ 0x500B]
0x5000 ISP CTRL00
0x5001 ISP CTRL01
0x5002 ISP CTRL02
0x5003 RSVD
0x5004 ISP CTRL04
0x5005 ISP CTRL05
0x5006 ISP CTRL06
0x5007 ISP CTRL07
0x5008 ISP CTRL08
0x5009 ISP CTRL09
0x500A RSVD
0x500B ISP CTRL0B

//7.18 test pattern [0x5080]

0x5080 PRE CTRL00

//7.19 LENC control [0x5100 ~ 0x511C]

0x5100 RED X0_H
0x5101 RED X0_L
0x5102 RED Y0_H
0x5103 RED Y0_L
0x5104 RED A1
0x5105 RED A2
0x5106 RED B1
0x5107 RED B2
0x5108 GRN X0_H
0x5109 GRN X0_L
0x510A GRN Y0_H
0x510B GRN Y0_L
0x510C GRN A1
0x510D GRN A2
0x510E GRN B1
0x510F GRN B2
0x5110 BLUE X0_H
0x5111 BLUE X0_L
0x5112 BLUE Y0_H
0x5113 BLUE Y0_L
0x5114 BLUE A1
0x5115 BLUE A2
0x5116 BLUE B1
0x5117 BLUE B2
0x5118 LENC CTRL
0x5119 LENC COEF TH
0x511A LENC GAIN THRE1
0x511B LENC GAIN THRE2
0x511C COEF MAN

//7.20 AWB control [0x5200 ~ 0x5230, 0x5238 ~ 0x523D]

0x5200 R AWB CTRL00
0x5201 R AWB CTRL01
0x5202 R AWB CTRL02
0x5203 R AWB CTRL03
0x5204 R WIN BL X_H
0x5205 R WIN BL X_L
0x5206 R WIN BL Y_H
0x5207 R WIN BL Y_L
0x5208 R WIN TR X_H
0x5209 R WIN TR X_L
0x520A R WIN TR Y_H
0x520B R WIN TR Y_L
0x520C R SKIN DX_H
0x520D R SKIN DX_L
0x520E R SKIN DY_H
0x520F R SKIN DY_L
0x5210 R SKIN RX_H
0x5211 R SKIN RY_L
0x5212 R AWB CTRL12
0x5213 R AWB CTRL13
0x5214 R AWB CTRL14
0x5215 R AWB CTRL15
0x5216 R AWB CTRL16
0x5217 R AWB CTRL17
0x5218 R AWB CTRL18
0x5219 R AWB CTRL19
0x521A R AWB MAN R_H
0x521B R AWB MAN R_L
0x521C R AWB MAN G_H
0x521D R AWB MAN G_L
0x521E R AWB MAN B_H
0x521F R AWB MAN B_L
0x5220 R LOCAL LIMIT_H
0x5221 R LOCAL LIMIT_L
0x5222 R WP LOCAL LIMIT_H
0x5223 R WP LOCAL LIMIT_L
0x5224 R SENSOR GAIN TH_H
0x5225 R SENSOR GAIN TH_L
0x5226 R SENSOR GAIN TH2_H
0x5227 R SENSOR GAIN TH2_L
0x5228 R WIN SX_H
0x5229 R WIN SX_L
0x522A R WIN EX_H
0x522B R WIN EX_L
0x522C R WIN SY_H
0x522D R WIN SY_L
0x522E R WIN EY_H
0x522F R WIN EY_L
0x5230 R AWB CTRL30
0x5238 R GAIN O_H
0x5239 R GAIN O_L
0x523A G GAIN O_H
0x523B G GAIN O_L
0x523C B GAIN O_H
0x523D B GAIN O_L

//7.21 gamma control [0x5300 ~ 0x5310]

0x5300 GAMMA CTRL
0x5301 YST1
0x5302 YST2
0x5303 YST3
0x5304 YST4
0x5305 YST5
0x5306 YST6
0x5307 YST7
0x5308 YST8
0x5309 YST9
0x530A YST10
0x530B YST11
0x530C YST12
0x530D YST13
0x530E YST14
0x530F YST15
0x5310 YSLP15


//7.22 DPC control [0x5400 ~ 0x5405, 0x540E ~ 0x540F]


0x5400 DPC CTRL00
0x5401 DPC CTRL01
0x5402 DPC CTRL02
0x5403 DPC CTRL03
0x5404 DPC CTRL04
0x5405 DPC CTRL05
0x540E DPC CTRL0E
0x540F RO BTHRE


//7.23 CIP control [0x5500 ~ 0x5514]

0x5500 SHRP MT GAIN TH1
0x5501 SHRP MT GAIN TH2
0x5502 SHRP MT TH1
0x5503 SHRP MT TH2
0x5504 DNS GAIN TH1
0x5505 DNS GAIN TH2
0x5506 DNS TH1
0x5507 DNS TH2
0x5508 CIP CTRL
0x5509 SHRP TH GAIN TH1
0x550A SHRP TH GAIN TH2
0x550B SHRP TH1
0x550C SHRP TH2
0x550D RECURSIVE DNS EN
0x550E SHRP MT
0x550F DNS TH
0x5510 SHRP TH
0x5511 R LOW_THR
0x5512 R WEIGHT1
0x5513 R WEIGHT2
0x5514 R SHARPENMT P


//7.24 CMX control [0x5600 ~ 0x5605, 0x5612, 0x5615]

0x5600 CMX11
0x5601 CMX12
0x5602 CMX13
0x5603 CMX14
0x5604 CMX15
0x5605 CMX16
0x5612 CMXSIGN
0x5615 CMX CTRL



//7.25 SDE control [0x5800, 0x5803 ~ 0x580C]

0x5800 SDE EN CTRL
0x5803 SATURATION TH2
0x5804 SATURATION TH1
0x5805 Y OFFSET
0x5806 Y GAIN
0x5807 Y BRIGHT
0x5808 SIGN BITS
0x5809 UVADJ GAIN TH1
0x580A UVADJ GAIN TH2
0x580B UVADJ MAN EN
0x580C UV ADJ

















