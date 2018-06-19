#include "CS8963_Flash.h"
#include "CS8963SFR.h"
#include "CS8963xram.h"
#include "Global.h"
#include "CS8963_Function.h"
#include "Setup.h"
#include "Setup_function.h"

#define IFB_ByteWrite 0x01
#define IFB_ByteRead 0x02
#define MainMemory_ByteWrite 0x04
#define page_Erase 0x08
#define MainMemory_ByteRead 0x10
#define Command_Fail (FLSHCMD&0x20)	   //1 is command fail, 0 is right
#define ByteWrite_VerifyResult (FLSHCMD&0x80)	   //1 is match, 0 is mismatch
#define fail 0xaa
#define success 0x55
#define tempDAT 0x01

BYTE returnValue = 0x00;
BYTE program_tab[4]={0x55, 0xaa, 0x5a, 0xa5};

void Unlock_Flash(void)
{
	TB = 0xaa;
	TB = 0x55;
	CNTPCTL = 0x00;
	CNTPCTH = 0xff;
	TB = 0x00;
}

void Lock_Flash(void)
{
	TB = 0xaa;
	TB = 0x55;
	CNTPCTL = 0xff;
	CNTPCTH = 0x00;
	TB = 0x00;
}

void ISPCLKF_initial(void)
{
	TB = 0xAA;
	TB = 0x55;
	ISPCLKF = 0x45;		//datasheet 0x45
	TB = 0x00;
}

void IFB_Write_1Byte(BYTE ADDH,BYTE ADD,BYTE DAT)
{
	TB = 0xAA;
	TB = 0x55;
	FLSHADH = ADDH;
	FLSHADL = ADD;
	FLSHDAT = DAT;
	FLSHCMD = IFB_ByteWrite;  //IFB write command
	TB = 0x00;
}


void Erase_Page(bit highADD, BYTE pageADD)
{
	TB = 0xaa;
	TB = 0x55;
	FLSHADL = 0x00;	// ADDR[7:0]
	FLSHADH = pageADD;	// ADDR[15:8]
	FLSHADM = highADD; // ADDR[16]
	FLSHCMD = 0x08;  //Flash Erase enable
	TB = 0x00;

	if(Command_Fail)
		returnValue = fail;
	else
		returnValue = success;
}


void Erase_All(void)
{
	BYTE i;

	for(i=4; i<0x40; i++)
	{
		Erase_Page(0, i);
		if(returnValue == fail)
			break;
	}
	if(returnValue == success)
	{
		for(i=0x00; i<0x40; i++)
		{
			Erase_Page(1, i);
			if(returnValue == fail)
				break;
		}
	}
}

void Program_Flash_1Byte(bit highADD, BYTE midADD, BYTE lowADD, BYTE writeDAT)
{
	TB = 0xaa;
	TB = 0x55;
	FLSHADM = highADD; // ADDR[16]
	FLSHADH = midADD;	// ADDR[15:8]
	FLSHADL = lowADD;	// ADDR[7:0]

	FLSHDAT = writeDAT;
	//FLSHDAT = writeDAT;
	//FLSHCMD = MainMemory_ByteWrite;
	TB = 0x00;

	TB = 0xaa;
	TB = 0x55;
	FLSHCMD = MainMemory_ByteWrite;
	TB = 0x00;
#if 0
	if(ByteWrite_VerifyResult)
		returnValue = success;
	else
		returnValue = fail;
#endif

#if 1
	if(Command_Fail)
		returnValue = fail;
	else
		returnValue = success;
#endif
}

void Program_All(BYTE DAT)
{
   BYTE i,j,m;

   for(i = 0x10; i<=0xff; i++)	  // form 4K start
		  {
     		for( j = 0; j<0xf9; j+=8)
	     		{
				   for(m = 0; m<8; m++)
				       {
				          	Program_Flash_1Byte(0, i, j+m, DAT<<m);
		   					if(returnValue == fail)
		      					break;
					   }
				   //printf("J = %d .\n", (WORD)j);
		   		   if(returnValue == fail)
		      			break;
				   if(j == 0xf8)
				        break;
		 		}
			//printf("I = %d .\n", (WORD)i);
		   	if(returnValue == fail)
		      	break;
			if( i == 0xff)
			    break;
		  }
   if(returnValue == success)
          {
   				for(i = 0; i<=0xff; i++)
		  			{
     					for( j = 0; j<0xf9; j+=8)
	     					{
							    for(m = 0; m<8; m++)
								     {
	       						 		Program_Flash_1Byte(1, i, j+m,DAT<<m);
		   								if(returnValue == fail)
		      									break;
									 }
		   						if(returnValue == fail)
		      						 break;
								if( j == 0xf8)
								     break;
							}
		   				if(returnValue == fail)
		      					break;
						if( i == 0xff)
			    				break;
					}
		  }
}

BYTE MainFlash_Read_1BYTE(bit highADD, BYTE midADD, BYTE lowADD)
{
   BYTE DAT;

   TB = 0xAA;
   TB = 0x55;
   FLSHADL = lowADD;
   FLSHADH = midADD;
   FLSHADM = highADD;
   FLSHCMD = MainMemory_ByteRead;  //IFB read enable
   TB = 0x00;

   TB = 0xAA;
   TB = 0x55;
   DAT = FLSHDAT;
   TB = 0x00;

   if(Command_Fail)
       returnValue = fail;
   else
	   returnValue = success;

   return DAT;
}

void Verify(BYTE verifyDAT)
{
   BYTE k,l,m;

   for(k = 0x10; k<=0xff; k++)
       {
	      	for(l = 0x00; l<0xf9; l+=8)
			    {
				    for(m = 0; m < 8; m++)
					    {
   							if(MainFlash_Read_1BYTE(0, k, l+m) == verifyDAT<<m)
				      			returnValue = success;
							else
					    		{
				            		returnValue = fail;
									break;
						 		}
						 }
					if(returnValue == fail)
					    break;
					if(l == 0xf8)
					    break;
				 }
		   	if(returnValue == fail)
		      	break;
			if(k == 0xff)
			    break;
		 }

   if(returnValue == success)
         {
   			for(k = 0x00; k<=0xff; k++)
       			{
	      			for(l = 0x00; l<0xf9; l+=8)
			    		{
   							for(m = 0; m<8; m++)
							    {
									if(MainFlash_Read_1BYTE(1, k, l+m) == verifyDAT<<m)
				      						returnValue = success;
									else
					    				{
				            				returnValue = fail;
											break;
						 				}
								 }
		   					if(returnValue == fail)
		      					break;
							if(l == 0xf8)
							    break;
				 		}
		   			if(returnValue == fail)
		      			break;
					if(k == 0xff)
			    		break;
			   }
		 }
	 //UART0_Send_1byte(returnValue);
}

/*
void Flash_Read_Write_Test(void)
{
   BYTE m;
   LWORD kk=1;

   ISPCLKF = 0x40;
   while(1)
   		{
		    RAM_Test();
			Unlock_Flash();
   			Erase_All();
			if(returnValue == success)
   				Program_All(tempDAT);
			if(returnValue == success)
				Verify(tempDAT);
			Lock_Flash();

   			if(returnValue == success)
			   {
       			   printf("Program flash %ld times reault: Pass.\n", kk);
			   }
   			if(returnValue == fail)
			   {
       			   printf("Program flash %ld times reault: Fail, please check.\n", kk);
			 	   while(1);
			   }
			kk++;

      while(0)
         {
		     if( UART0_Receive_1byte() == 0x55)
			 do
			     {
				     UART0_Send_1byte(MainFlash_Read_1BYTE(1, 0x60, m));
			     } 	 while(m++<0xff);
		 }
	 }
}
*/

#ifdef SAVE_FACTORY_DATA
void save_factory_data_time(void)
{
	int i;
	unsigned char flash_data[8]={0};
	int time_data[8]={0};
	ULONG time_old=0;
	ULONG time_new=0;

	printString("save_factory_data_time\n");

	Unlock_Flash();
	
	printString("Read date_string from flash page 62, data: \n");
	for(i=0;i<4;i++)
	{		
		flash_data[i]=MainFlash_Read_1BYTE(0x00, 0xF8, i);
		printd(flash_data[i]);
		printString("\n");
	}
	printString("\n");

	if(flash_data[0] == 0xff)
	{
		printString("No recorded data\n");
	}
	else
	{
		printString("Last recorded data: ");
		time_old=((ULONG)flash_data[0]<<24)|((ULONG)flash_data[1]<<16)|((ULONG)flash_data[2]<<8)|((ULONG)flash_data[3]);
		//time_old=(flash_data[0]<<24)|(flash_data[1]<<16)|(flash_data[2]<<8)|(flash_data[3]);
		printd(time_old);
		printString("\n");
	}

	time_new = time_old + SAVE_FACTORY_DATA_PERIOD;


	printString("time_diff: ");	printd(T5_count);printString("\n");
	printString("time_old: ");	printd(time_old);printString("\n");


	printString("time_new: ");	printd(time_new);printString("\n");


	flash_data[0] = (time_new >>24)&0xff;
	flash_data[1] = (time_new >>16)&0xff;
	flash_data[2] = (time_new >>8)&0xff;
	flash_data[3] = (time_new >>0)&0xff;

	for(i=0;i<4;i++)
	{		
		printd(flash_data[i]);printString("\n");
	}


	for(i=0; i<4; i++)
	{
		Program_Flash_1Byte(0x00,0xF8,i,flash_data[i]);
	}


	printString("------------Read date_string from flash page 62, data: \n");
	for(i=0;i<4;i++)
	{		
		flash_data[i]=MainFlash_Read_1BYTE(0x00, 0xF8, i);
	}

	for(i=0;i<4;i++)
	{		
		printd(flash_data[i]);printString("\n");
	}


	printString("\n");printString("\n");printString("\n");




	Lock_Flash();

}


void save_factory_data_time_222(void)
{
	int i;
	int j;
	unsigned char flash_data[8]={0};
	int time_data[8]={0};
	ULONG time_new=0;

	printString("save_factory_data_time\n");

	Unlock_Flash();


	for(j=0;j<3;j++)
	{
	
		time_new += 11111;

		printString("time_new: ");	printd(time_new);printString("\n");


		flash_data[0] = (time_new >>24)&0xff;
		flash_data[1] = (time_new >>16)&0xff;
		flash_data[2] = (time_new >>8)&0xff;
		flash_data[3] = (time_new >>0)&0xff;

		for(i=0;i<4;i++)
		{		
			printd(flash_data[i]);printString("   ");
		}
		printString("\n");


		for(i=0; i<4; i++)
		{
			Program_Flash_1Byte(0x00,0xF8,i,flash_data[i]);
		}


		printString("------------Read date_string from flash page 62, data: \n");
		for(i=0;i<4;i++)
		{		
			flash_data[i]=MainFlash_Read_1BYTE(0x00, 0xF8, i);
		}

		for(i=0;i<4;i++)
		{		
			printd(flash_data[i]);printString("   ");
		}
		printString("\n");



		for(i=0;i<4;i++)
		{		
			printd(flash_data[i]);printString("   ");
		}
		printString("\n");


		for(i=0; i<4; i++)
		{
			Program_Flash_1Byte(0x00,0xF8,i,flash_data[i]);
		}


		printString("------------Read date_string from flash page 62, data: \n");
		for(i=0;i<4;i++)
		{		
			flash_data[i]=MainFlash_Read_1BYTE(0x00, 0xF8, i);
		}

		for(i=0;i<4;i++)
		{		
			printd(flash_data[i]);printString("   ");
		}
		printString("\n");


		printString("\n");printString("\n");printString("\n");


	}

	Lock_Flash();

}
#endif

