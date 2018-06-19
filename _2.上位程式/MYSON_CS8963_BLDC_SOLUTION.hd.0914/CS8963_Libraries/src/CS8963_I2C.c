#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "HexToBin.h"
#include "Global.h"
#include "Setup.h"
#include "Setup_function.h"
#include "CS8963_I2C.h"
#include "CS8963_Config.h"
#include "CS8963_Function.h"

extern unsigned char I2C_buffer[20];
extern unsigned char I2C_buffer_length;

void Wait_NoBusy(void)
{
	while(I2CMCR&0x01);
	if(I2CMCR&0x02)
	{
		I2CMCR  = 0x04;
	}
}

void send_I2C_data(BYTE length)
{
	int i = 0;
	//BYTE k = 0;
	I2CMSA = IIC_Slave_Addr|0x00;			//bit0 0:W 1:R
	//I2CMSA = 0x90|0x00;				//bit0 0:W 1:R
	Wait_NoBusy();
	I2CMCR = 0x03;  // start and run
	I2CMBUF = 0x00; //slave IIC adderss
	Wait_NoBusy();

	for(i=0; i<(length-1); i++)
	{
		// run
		I2CMCR  = 0x01;
		I2CMBUF = I2C_buffer[i];
		Wait_NoBusy();
	}
	// run & stop
	I2CMCR  = 0x05;
	I2CMBUF = I2C_buffer[length-1];
	Wait_NoBusy();
}

void get_I2C_data()
{
	int i;
	if((I2CSST1&0x20) == 0x20)
	{
	    I2CSST1 &= ~0x20;
		for(i=0;i<20;i++)
		{
			if(sReceive_Tab[i] == 0)
				break;
			else
			{
				I2C_buffer[i] = sReceive_Tab[i];
				sReceive_Tab[i] = 0;
			}
		}
		I2C_buffer_length = i;
	}
	else
		I2C_buffer_length = 0;
}

void mIIC_P21P20_Initial(void)
{
	MFCFGP2_1 = B01000000;  									// Master SDA1 Enable
	MFCFGP2_0 = B01000000;  									// Master SCL1 Enable
	IOCFGP2_1 = B10000010;  									// PinC_OpenDrain
	IOCFGP2_0 = B10000010; 										// PinC_OpenDrain
	I2CMTP = 40;		//4 400K								// IIC_CLK = SystemCLK/(8*(I2CMTP[7:0]+1))	   16M/80 =200K
}

void sIIC_P21P20_Initial(unsigned char slaveADD3,unsigned char slaveADD1)
{
	MFCFGP2_1 = B00100000;  										// Slave SDA1 Enable
	MFCFGP2_0 = B00100000;  										// Slave SCL1 Enable
	IOCFGP2_1 = B10000010;											// PinC_OpenDrain
	IOCFGP2_0 = B10000010; 											// PinC_OpenDrain

/*
    MFCFGP1_2 = B01000000;  										// Slave SDA1 Enable
	MFCFGP1_3 = B01000000;  										// Slave SCL1 Enable
    IOCFGP1_2 = B10000010;											// PinC_OpenDrain
	IOCFGP1_3 = B10000010; 											// PinC_OpenDrain
*/

	I2CSCON1 = 0x00;	//reset
	I2CSCON1 = 0x5c;	//0x04 only RCinterrupt//0x0c - - - - TXinterrupt RCinterrupt - - 	 ; send and receive interrupt enable
	I2CSST1 = 0x0a;		// hold time
	I2CSADR3 = 0x80|(slaveADD3>>1);  								// enable slave IIC+slave adderss3
	I2CSADR1 = 0x80|(slaveADD1>>1);									// enable slave IIC+slave adderss1
	IP = 0x40;
	SPI_sIIC_EN = 1;												// enable i2c slave1 interrupt
	EA = 1;
}

char state=0;
char Pre_state=0;
bit transmit_update;
char addr_buf;
char Read_flag;
void SPI_I2CS_EUART(void) interrupt 13
{
	switch(state)
	{
	    case 0:
		//reset
			if(Pre_state!=0)
			{

				I2CSCON1 = 0x00;	//reset
				I2CSCON1 = 0x5c;    //0x04 only RCinterrupt//0x0c - - - - TXinterrupt RCinterrupt - - 	 ; send and receive interrupt enable
				I2CSST1 = 0x0a;		// hold time
				I2CSADR3 = 0x80|(IICS1_Addr3>>1);  								// enable slave IIC+slave adderss3
				I2CSADR1 = 0x80|(IICS1_Addr1>>1);									// enable slave IIC+slave adderss1
			}
			Pre_state = 0;

			if(I2CSST1&0x40)					//address match
			{
				state = 1;
				I2CSST1 &= ~0x40;
			}else{
				state = 0;
			}

	        if(I2CSST1&0x08)					//TXBI has been set?
	        {I2CSDAT1 = 0x00;}

	        if(I2CSST1&0x10)					//restart
	        {I2CSST1 &= ~0x10;}

			if(I2CSST1&0x04)					//RCBI has been set?
	        {sReceive_Tab[0] = I2CSDAT1;}


		break;
	    case 1:
		//address Match
			Pre_state = 1;
			if(I2CSST1&0x04)					//RCBI has been set?
	        {
			    addr_buf = I2CSDAT1;

	            if(I2CSST1&0x10)					//restart
	            {
                    I2CSDAT1 = sTransmit_Tab[addr_buf];
		            addr_buf++;
			        I2CSST1 &= ~0x10;
					Read_flag = 1;
			        state = 3;
			    }else{

			        state = 2;
				}

			}else{
			    addr_buf = 0;
				state = 0;
			}

	        if(I2CSST1&0x40)					//address match
	        {
			    I2CSST1 &= ~0x40;
			}

	        if(I2CSST1&0x08)					//TXBI has been set?
	        {I2CSDAT1 = 0x00;}



		break;
	    case 2:
		//whether Read or Write
			Pre_state = 2;

			if(I2CSST1&0x04)					//RCBI has been set?
	        {

				state = 4;
				sReceive_Tab[addr_buf] = I2CSDAT1;
				//if((addr_buf>=6) && (addr_buf<=12 ))
				{
				    sTransmit_Tab[addr_buf] = sReceive_Tab[addr_buf];
				}
				addr_buf++;
			}else{


				if(I2CSST1&0x10)					//restart
	            {
			        I2CSST1 &= ~0x10;

                    I2CSDAT1 = sReceive_Tab[addr_buf];
		            addr_buf++;
					Read_flag = 1;
			    	state = 3;
		    	}else{
				    state = 0;
			    }


				/*
	            if(I2CSST1&0x40)					//address match
	            {

			        I2CSST1 &= ~0x40;
                    I2CSDAT1 = sTransmit_Tab[addr_buf];
		            addr_buf++;
			    	state = 3;
			    }else{
				    state = 0;
			    }
				*/

			}


	        if(I2CSST1&0x08)					//TXBI has been set?
	        {I2CSDAT1 = 0x00;}

		break;
	    case 3:
		//Read
			Pre_state = 3;

	        if(I2CSST1&0x08)										    //TXBI has been set?
	        {
                I2CSDAT1 = sTransmit_Tab[addr_buf];
		        addr_buf++;
				state = 3;

	        }else{
				if(Read_flag == 1)
				{
				    Read_flag = 0;
	                if(I2CSST1&0x40)					//address match
	                {
			            state = 3;
			            I2CSST1 &= ~0x40;
			        }else{
			            state = 0;
					}
			    }else{

	                if(I2CSST1&0x40)					//address match
	                {
			            state = 1;
			            I2CSST1 &= ~0x40;
			        }else{
			            state = 0;
					}
				}
			}

			if(I2CSST1&0x04)					//RCBI has been set?
	        {addr_buf = I2CSDAT1;}

	        if(I2CSST1&0x10)					//restart
	        {I2CSST1 &= ~0x10;}



		break;
	    case 4:
		//Write
			Pre_state = 4;
			if(I2CSST1&0x04)					//RCBI has been set?
	        {
				sReceive_Tab[addr_buf] = I2CSDAT1;
				//if((addr_buf>=6) && (addr_buf<=12 ))
				{
				    sTransmit_Tab[addr_buf] = sReceive_Tab[addr_buf];
				}
				addr_buf++;
			    state = 4;
			}else{

	            if(I2CSST1&0x40)					//address match
	            {
			        state = 1;
			        I2CSST1 &= ~0x40;
			    }else{
			        state = 0;
			    }
			}

	        if(I2CSST1&0x08)					//TXBI has been set?
	        {I2CSDAT1 = 0x00;}

	        if(I2CSST1&0x10)					//restart
	        {I2CSST1 &= ~0x10;}


		break;
		default:
			Pre_state = 5;
			state = 0;
		break;

	}

}




//#define IICS2_Addr		0x46			 //P1_5 P1_4(bit6-bit0)

/**********************************************************
 * Chips   : CS8963
 * Purpose : drive Function I2C
 * Filename: CS8963_I2C.C
 * Author  :
 * Date    : 2015/01/16
 **********************************************************/

/*
unsigned char mSend_Tab[10] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A};	   //Master1 Send Tab
unsigned char sReceive_Tab[10] = {0};														   //Slave2 Receive	Tab

void Wait_NoBusy(void)
{
	while(I2CMCR&0x01);
	if(I2CMCR&0x02)
	{
		I2CMCR  = 0x04;
	}
}

void Initial_I2CM(unsigned char pin_scl, unsigned char pin_sda)
{
	if(pin_scl == _P2_0)			//I2CM SCL
	{
		IOCFGP2_0 = B10000010; 		// PinC_OpenDrain
		MFCFGP2_0 = B01000000;  	// Master SCL Enable
	}
	else if(pin_scl == _P1_4)		//I2CM SCL
	{
		IOCFGP1_4 = B10000010; 		// PinC_OpenDrain
		MFCFGP1_4 = B01000000;  	// Master SCL Enable
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}

	if(pin_sda == _P2_1)			//I2CM SDA
	{
		IOCFGP2_1 = B10000010; 		// PinC_OpenDrain
		MFCFGP2_1 = B01000000;  	// Master SDA Enable
	}
	else if(pin_sda == _P1_5)		//I2CM SCL
	{
		IOCFGP1_5 = B10000010; 		// PinC_OpenDrain
		MFCFGP1_5 = B01000000;  	// Master SDA Enable
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}
	I2CMTP = 79;				 // IIC_CLK = SystemCLK/(8*(I2CMTP[7:0]+1))	   16M/80 =200K
	mIIC_EN = 1;				 // Enable IIC Master Interrupt
}

void Initial_I2CS1(unsigned char pin_scl, unsigned char pin_sda)
{
	if(pin_scl == _P1_3)			//I2CS1 SCL
	{
		IOCFGP1_3 = b00000110; 		// output with CMOS push-pull. 	use to SCL.
		MFCFGP1_3 = b00000001; 		// GPIOEN is enable.	set P1_3 to GPIO type, because SCL only in burning have use.
	}
	else if(pin_scl == _P2_0)		//I2CS1 SCL
	{
		IOCFGP2_0 = b00000110; 		// output with CMOS push-pull. 	use to SCL.
		MFCFGP2_0 = b00000001; 		// GPIOEN is enable.	set P2_0 to GPIO type, because SCL only in burning have use.
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}

	if(pin_sda == _P1_2)			//I2CS1 SDA
	{
		IOCFGP1_2 = b00000110; 		// output with CMOS push-pull. 	use to SDA.
		MFCFGP1_2 = b00000001; 		// GPIOEN is enable.	set P1_2 to GPIO type, because SDA only in burning have use.
	}
	else if(pin_sda == _P2_1)		//I2CS1 SCL
	{
		IOCFGP2_1 = b00000110; 		// output with CMOS push-pull. 	use to SDA.
		MFCFGP2_1 = b00000001; 		// GPIOEN is enable.	set P2_1 to GPIO type, because SDA only in burning have use.
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}
}


void Initial_I2CS2(unsigned char pin_scl, unsigned char pin_sda)
{
	if(pin_scl == _P1_4)			//I2CS2 SCL
	{
		IOCFGP1_4 = b00000110; 		// output with CMOS push-pull. 	use to SCL.
		MFCFGP1_4 = b00000001; 		// GPIOEN is enable.	set P1_3 to GPIO type, because SCL only in burning have use.
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}

	if(pin_sda == _P1_5)			//I2CS2 SDA
	{
		IOCFGP1_5 = b00000110; 		// output with CMOS push-pull. 	use to SDA.
		MFCFGP1_5 = b00000001; 		// GPIOEN is enable.	set P1_5 to GPIO type, because SDA only in burning have use.
	}
	else
	{
		printS('W');printS('R');printS('O');printS('N');printS('G');printS('0');printS('1');printS(0x0a);printS(0x0d);
	}
}

void mIIC_Send_1byte(unsigned char slaveADD, unsigned char DAT)
{
	I2CMSA = slaveADD|0x00; 									  //bit0 0:W 1:R
	Wait_NoBusy();
	I2CMBUF = DAT; 											      //Send Data
	Wait_NoBusy();
	I2CMCR = 0x07;												  //START+SEND+STOP
	Wait_NoBusy();
}

unsigned char mIIC_Receive_1byte(unsigned char slaveADD)
{
	unsigned char receiveDAT = 0;

	I2CMSA = slaveADD|0x01; 									  // bit0=1 receive data, bit0=0 send data
	Wait_NoBusy();
	I2CMCR = 0x07;  											  // receive data with stop
	Wait_NoBusy();
	receiveDAT = I2CMBUF;
	Wait_NoBusy();
	return receiveDAT;
}

void test_send_i2c_command()
{
	unsigned char i = 0;
	EA = 1;														//enable all the interrupts
	for(i = 0;i<10;i++)
	{
		mIIC_Send_1byte(IICS2_Addr,mSend_Tab[i]);				//Master1 send mSend_Tab[] to Slave2
		printS(sReceive_Tab[i]);								//Receive the data from Slave2 INT
	}
	printS('W');
}
*/

