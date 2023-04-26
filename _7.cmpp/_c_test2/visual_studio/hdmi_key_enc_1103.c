#include <stdio.h>
#include <ctype.h>	//for isprint()
#include <string.h>
#define START 0
#define LENGTH 100

void print_pk(unsigned char* Aksv, unsigned char* PK);

int main(int argc,char* argv[])
{
	FILE* 	fp1;
	FILE* 	fp2;
	FILE* 	fp3;
	char* 	file_decrypt = "/home/david/HDMI_key_dec.bin";
	char* 	file_encrypt = "/home/david/HDMI_key_enc_for_writer.txt";
	char* 	file_AES     = "/home/david/AES";
        int	i,j,k;
	unsigned char Aksv[5];
	unsigned char Zero[3];
       	unsigned char PK[280];
	unsigned char pnt=0x55;
	unsigned char DK1,DK2,DK3,DK4,DK5,DK6,DK7;
	unsigned char DK[280];
	int set_ST;
	int set_length;
	set_ST=START;
	set_length=LENGTH;
	printf("HDMI key encryption, set_ST=%d set_length=%d\n",set_ST,set_length);

	//Read HDMI key file : key.bin
	if((fp1=fopen(file_decrypt,"rb"))==NULL)
	{
		printf("[HDMI]: HDMI Device Private Key file does not exist!!!!\n");
		return 1;
	}
	//Create HDMI_key_enc_for_writer.txt, HDMI writer use
	if((fp2=fopen(file_encrypt,"w"))==NULL)
	{
		printf("[HDMI]: HDMI Device Private Key output file create fails.\n");
		return 1;
	}
	
	for(k=set_ST;k<(set_ST+set_length);k++)
	{
		//printf("File position : %d = 0x%x\n",4+308*k,4+308*k);
		//fseek(fp1,4+308*k,SEEK_SET);
		fseek(fp1,308*k,SEEK_SET);
		for(i=0;i<5;i++)
		{
			Aksv[i]=fgetc(fp1);
		}
		//fseek(fp1,3,SEEK_CUR);
		for(i=0;i<3;i++)
		{
			Zero[i]=fgetc(fp1);
		}
		for(i=0;i<280;i++)
		{
			PK[i]=fgetc(fp1);
		}
		print_pk(Aksv,PK);
		if((Zero[0]!=0)||(Zero[1]!=0)||(Zero[2]!=0))
		{
			printf("Zero test fails!!!!!!! exit\n");
			return 1;
		}
		//Temperally print HDMI key content
		//print_pk(Aksv,PK);
		
		//Doing HDMI key encryption
		for(i=0; i<5; i++)
		{
			for(j=0; j<8; j++)
			{
				DK1=PK[i*56+j*7]^pnt;
				DK2=DK1^(~PK[i*56+j*7+1]);
				DK3=DK2^PK[i*56+j*7+2];
				DK4=DK3^PK[i*56+j*7+3];
				DK5=DK4^PK[i*56+j*7+4];
				DK6=DK5^(~PK[i*56+j*7+5]);
				DK7=DK6^(~PK[i*56+j*7+6]);
				//printf("i=%d j=%d PK1=0x%x PK2=0x%x PK3=0x%x PK4=0x%x PK5=0x%x PK6=0x%x PK7=0x%x\n",i,j,PK[i*56+j*7],PK[i*56+j*7+1],PK[i*56+j*7+2],PK[i*56+j*7+3],PK[i*56+j*7+4],PK[i*56+j*7+5],PK[i*56+j*7+6]);
				//printf("DK1=0x%x DK2=0x%x DK3=0x%x DK4=0x%x DK5=0x%x DK6=0x%x DK7=0x%x\n",DK1,DK2,DK3,DK4,DK5,DK6,DK7);
				DK[i*56+j*7]=PK[i*56+j*7]^pnt;
				DK[i*56+j*7+1]=DK1^(~PK[i*56+j*7+1]);
				DK[i*56+j*7+2]=DK2^PK[i*56+j*7+2];
				DK[i*56+j*7+3]=DK3^PK[i*56+j*7+3];
				DK[i*56+j*7+4]=DK4^PK[i*56+j*7+4];
				DK[i*56+j*7+5]=DK5^(~PK[i*56+j*7+5]);
				DK[i*56+j*7+6]=DK6^(~PK[i*56+j*7+6]);
			}
		}

		for(i=0;i<sizeof(DK);i++)
		{
			fprintf(fp2,"%02x ",DK[i]);
			if((i%7)==6)
				fprintf(fp2,"\n");
		}
		for(i=0;i<sizeof(Aksv);i++)
		{
			fprintf(fp2,"%02x ",Aksv[i]);
		}
		fprintf(fp2,"\n\n");
		printf("\n");
	}
	fclose(fp1);
	fclose(fp2);

	//Create AES_CCMP, HDMI DvdPlayer use
	if((fp3=fopen(file_AES,"wb"))==NULL)
	{
		printf("[HDMI]: HDMI Device Private Key output file create fails.\n");
		return 1;
	}
	fseek(fp3,0,SEEK_SET);
	for(i=0;i<280;i++)
		fputc(DK[i],fp3);
	for(i=0;i<5;i++)
		fputc(Aksv[i],fp3);
	fclose(fp3);
	return 0;
}

void print_pk(unsigned char* Aksv, unsigned char* PK)
{
	int i;
	printf("Aksv:\t");
	for(i=0;i<5;i++)
	{
		printf("%02X ",Aksv[i]);
	}
	printf("\n");
	/*
	printf("Print PK:\n");
	for(i=0;i<280;i++)
	{
		printf("%02X ",PK[i]);
		if((i%16)==15)
		printf("\n");
	}
	printf("\n");
	*/
}

