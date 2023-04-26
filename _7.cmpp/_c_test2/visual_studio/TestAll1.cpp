// TestAll1.cpp: �D�n�M���ɡC

#include "stdafx.h"
#include <iostream>

#define b11111111 0xff
#define countof(a) (sizeof(a) / sizeof(*(a)))

using namespace System;
using namespace System::IO;
using namespace std;		//for cin, cout

void swap(unsigned char* a, unsigned char* b);
int test_DateTime();
int test_list();
int test_GetLastAccessTime();
int test_DriveInfo();
int TestSorting(void);
int test_NewFunction();
int test_string(void);
int TestWriteLine(void);


#define WD000 0<<2|0<<7|0<<6	//Time Out Value =     131072
#define WD001 0<<2|0<<7|1<<6	//Time Out Value =    1048576
#define WD010 0<<2|1<<7|0<<6	//Time Out Value =    8388608
#define WD011 0<<2|1<<7|1<<6	//Time Out Value =   67108864
#define WD100 1<<2|0<<7|0<<6	//Time Out Value =  134217728
#define WD101 1<<2|0<<7|1<<6	//Time Out Value =  268435456
#define WD110 1<<2|1<<7|0<<6	//Time Out Value =  536870912
#define WD111 1<<2|1<<7|1<<6	//Time Out Value = 1073741824

union Wtemp
{
	unsigned char tempB[6];			//0XAA 0XBB
	unsigned int tempW;				//0XAABB
};

//enum _MtState
enum
{
	start,			//0
	stop,			//1
};


int main(array<System::String ^> ^args)
{
	int age;
	//test_DateTime();

	//test_list();
	//test_GetLastAccessTime();
	//test_DriveInfo();
	//test_FileFunction1();
	//test_FileFunction2();
	//test_DirectoryFunction1();
	//test_DirectoryFunction2();
	TestSorting();
	test_string();
	TestWriteLine();
	test_NewFunction();

	Console::Write("Input Age:");
	age=Convert::ToInt32(Console::ReadLine());
	Console::WriteLine("age�G {0}\n\n", age);

	Console::WriteLine("WD000�G {0}", WD000);
	Console::WriteLine("WD001�G {0}", WD001);
	Console::WriteLine("WD010�G {0}", WD010);
	Console::WriteLine("WD011�G {0}", WD011);
	Console::WriteLine("WD100�G {0}", WD100);
	Console::WriteLine("WD101�G {0}", WD101);
	Console::WriteLine("WD110�G {0}", WD110);
	Console::WriteLine("WD111�G {0}", WD111);


	system("pause");
	return 0;
}

int test_DateTime()
{
	DateTime dt=DateTime::Now;
	Console::WriteLine("�ɡG {0}", dt);
	Console::WriteLine("�~�G {0}", dt.Year);
	Console::WriteLine("��G {0}", dt.Month);
	Console::WriteLine("��G {0}", dt.Day);
	Console::WriteLine("�ɡG {0}", dt.Hour);
	Console::WriteLine("���G {0}", dt.Minute);
	Console::WriteLine("��G {0}", dt.Second);
	Console::WriteLine("�P�G {0}", dt.DayOfWeek);
	Console::Read();		//�ѿ�J�˸mŪ���@�Ӧr���A��ϥΪ̫��UEnter���Y����Ū���C

	DateTime d = DateTime(2014,10,29,1,2,3);	//�إߪ���d�N��2014�~10��29��1��2��3��
	//DateTime d = DateTime(2014,10,29);		//�إߪ���d�N��2014�~10��29��
	Console::WriteLine("�ɡG {0}", d);
	Console::WriteLine("�~�G {0}", d.Year);
	Console::WriteLine("��G {0}", d.Month);
	Console::WriteLine("��G {0}", d.Day);
	Console::WriteLine("�ɡG {0}", d.Hour);
	Console::WriteLine("���G {0}", d.Minute);
	Console::WriteLine("��G {0}", d.Second);
	Console::WriteLine("�P�G {0}", d.DayOfWeek);

	int n = d.Day;
	Console::WriteLine(  "get number : {0}", n );

	Console::WriteLine(  "�{�b�ɨ�:{0}��{1}��{2}��", dt.Hour, dt.Minute, dt.Second );

	Console::Read();		//�ѿ�J�˸mŪ���@�Ӧr���A��ϥΪ̫��UEnter���Y����Ū���C

	return 0;
}


int test_list()
{
	int selection;
	printf("1. test_directory_create_delete()\n");
	printf("2. test_file_create_copy_delete()\n");
	printf("3. test_file_read_write_text()\n");
	printf("4. test_file_read_write_binary()\n");
	printf("5. test_file_copy_move()\n");
	printf("6. test_DateTime()\n");

	cout << "\n�п�J�ﶵ(1-6)�G";
	cin >> selection;
	switch(selection)
	{
	case  1:	printf("You select 1 test_directory_create_delete()\n");
		//test_directory_create_delete();
		break;
	case  2:	printf("You select 2 test_file_create_copy_delete()\n");
		//test_file_create_copy_delete();
		break;
	case  3:	printf("You select 3 test_file_read_write_text();\n");
		//test_file_read_write_text();
		break;
	case  4:	printf("You select 4 test_file_read_write_binary()\n");
		//test_file_read_write_binary();
		break;
	case  5:	printf("You select 5 test_file_copy_move();\n");
		//test_file_copy_move();
		break;
	case  6:	printf("You select 6 test_DateTime();\n");
		//test_DateTime();
		break;

	default:	printf("Unknown selection\n");
		break;
	}

	return 0;
}

int test_DriveInfo()
{
	// Array to store drive string
	array<DriveInfo^>^ allDrives = DriveInfo::GetDrives();
	DriveInfo^ d;
	// For each drive...
	for each (d in allDrives)
	{
		// Get the following info...
		Console::WriteLine("Drive: {0}", d->Name);						//���o�Ϻо��W�١A�Ҧp C:\�C
		Console::WriteLine("  File type:\t\t{0}", d->DriveType);		//���o�Ϻ������A�Ҧp CD-ROM�B�������B�����ΩT�w���C
		Console::WriteLine("  Root Directory:\t{0}", d->RootDirectory);	//���o�ϺЪ��ڥؿ��C
		// More, if the drive is ready, get the following info...
		if (d->IsReady == true)		//�o�ӭȪ�ܺϺо��O�_�w�N���C
		{
			Console::WriteLine("  Volume label:\t\t{0}", d->VolumeLabel);	//���o�γ]�w�ϺЪ��Ϻаϼ��ҡC
			Console::WriteLine("  File system:\t\t{0}", d->DriveFormat);	//���o�ɮרt�Ϊ��W�١A�Ҧp NTFS �� FAT32�C
			Console::WriteLine("  Total size of drive:            {0, 15} bytes", d->TotalSize);	//���o�Ϻо��W�x�s�Ŷ����`�j�p�A�H�줸�լ����C
			Console::WriteLine("  Available space to current user:{0, 15} bytes", d->AvailableFreeSpace);	//��ܺϺо��W���i�ΪŶ��q�A�H�줸�լ����C
			Console::WriteLine("  Total available space:          {0, 15} bytes", d->TotalFreeSpace);	//���o�Ϻо��W�i�ΪŶ����`�q�A�H�줸�լ����C
			Console::WriteLine();
		}
		else
		{
			Console::WriteLine("  �Ϻ� {0} ���N��" , d->Name);
		}
	}
	return 0;
}

void swap(unsigned char* a, unsigned char* b)
{
	unsigned char c;
	c=*a;
	*a=*b;
	*b=c;
	return;
}

int TestSorting(void)
{
	unsigned char data[]="KJIHGFEDCBA";
	int i,j;
	int swap_number=0;
	int compare_number=0;

	printf("sizeof data is %d\n",sizeof(data));

	for(i=0;i<(sizeof(data)-1);i++)
	{
		printf("data[%d]=%c\n",i,data[i]);
	}
	swap(&data[0],&data[1]);

	printf("\n\nresult:\n");
	for(i=0;i<(sizeof(data)-1);i++)
	{
		for(j=i+1;j<(sizeof(data)-1);j++)
		{
			compare_number++;
			if(data[i]>data[j])
			{
				swap(&data[i],&data[j]);
				swap_number++;
			}
		}
	}

	for(i=0;i<(sizeof(data)-1);i++)
	{
		printf("data[%d]=%c\n",i,data[i]);
	}
	printf("\ncompare_number=%d\n",compare_number);
	printf("swap_number=%d\n",swap_number);
	system("pause");
    return 0;
}

int test_string(void)
{
	char hello1[]={'H','e','l','l','o'};
	String^ Hello2 =gcnew String("Hello again");
	String^ Hello3 = "Hello World!";

	String^ data1 = "Hello Visual C++! ";
	String^ data2 = data1->Substring(6,8);

	Console::WriteLine("{0}", data1);
	Console::WriteLine("{0} {1}", data1, data1->Length);
	Console::WriteLine("{0} {1}", data2, data2->Length);


	String^ data3 = "ABCDEFGabcdefg";

	Console::WriteLine("To lower is {0}", data3->ToLower());
	Console::WriteLine("To upper is {0}", data3->ToUpper());
	Console::WriteLine("GetType is {0}", data3->GetType());
	Console::WriteLine("GetType is {0}", data3->GetTypeCode());
	return 0;
}

int TestWriteLine(void)
{
	String^ dddd = "Hello World!";

	Console::WriteLine("{0}", dddd);
	Console::WriteLine("{0,30}", dddd);		//�����S�w���ת��r��A�e���ɪť�
	Console::WriteLine("{0,-30}", dddd);	//�����S�w���ת��r��A�᭱�ɪť�

	Console::WriteLine("->{0,30}<-", dddd);
	
	int a=255;

	Console::WriteLine("{0:X8}", a);



// Console::WriteLine ���U�����u�榡���r�X
Console::WriteLine("{0, 8 :C}", 2);     // $2.00
Console::WriteLine("{0, 8 :C3}", 2);    // $2.000
Console::WriteLine("{0 :D3}", 2);       // 002
Console::WriteLine("{0 :E}", 2);        // 2.000000E+000
Console::WriteLine("{0 :G}", 2);        // 2
Console::WriteLine("{0 :N}", 2500000.00);    // 2,500,00.00
Console::WriteLine("{0 :x4}", 12);      // 000c
Console::WriteLine("{0, 2 :x}", 12);    //  c
Console::WriteLine("{0 :000.000}", 12.23);   // 012.230
Console::WriteLine("{0 :r}", 15.62);    // 15.62

/*
Console::WriteLine("{0 :d}", System.DateTime.Now);    // 2012-3-27
Console::WriteLine("{0 :D}", System.DateTime.Now);    // 2012�~3��27��
Console::WriteLine("{0 :t}", System.DateTime.Now);    // 11:43
Console::WriteLine("{0 :T}", System.DateTime.Now);    // 11:43:34

Console::WriteLine("{0 :f}", System.DateTime.Now);    // 2012�~3��27�� 11:43
Console::WriteLine("{0 :F}", System.DateTime.Now);    // 2012�~3��27�� 11:43:34

Console::WriteLine("{0 :g}", System.DateTime.Now);    // 2012-3-27 11:43
Console::WriteLine("{0 :G}", System.DateTime.Now);    // 2012-3-27 11:43:34

Console::WriteLine("{0 :M}", System.DateTime.Now);    // 3��27��
Console::WriteLine("{0 :r}", System.DateTime.Now);// Tue, 27 Mar 2012 11:43:34 GMT
Console::WriteLine("{0 :s}", System.DateTime.Now);    // 2012-03-27T11:43:34
Console::WriteLine("{0 :u}", System.DateTime.Now);    // 2012-03-27 11:43:34Z
Console::WriteLine("{0 :U}", System.DateTime.Now);    // 2012�~3��27�� 3:43:34
Console::WriteLine("{0 :Y}", System.DateTime.Now);    // 2012�~3��

Console::WriteLine("{0 :dd}", System.DateTime.Now);   // 27
Console::WriteLine("{0 :ddd}", System.DateTime.Now);  // �G
Console::WriteLine("{0 :dddd}", System.DateTime.Now); // �P���G

Console::WriteLine("{0 :f}", System.DateTime.Now);    // 2012�~3��27�� 11:46
Console::WriteLine("{0 :ff}", System.DateTime.Now);   // 18
Console::WriteLine("{0 :fff}", System.DateTime.Now);  // 187
Console::WriteLine("{0 :ffff}", System.DateTime.Now); // 1875
Console::WriteLine("{0 :fffff}", System.DateTime.Now); // 18750

Console::WriteLine("{0 :gg}", System.DateTime.Now);   // ����
Console::WriteLine("{0 :ggg}", System.DateTime.Now);  // ����
Console::WriteLine("{0 :gggg}", System.DateTime.Now); // ����
Console::WriteLine("{0 :ggggg}", System.DateTime.Now);     // ����
Console::WriteLine("{0 :gggggg}", System.DateTime.Now);    // ����

Console::WriteLine("{0 :hh}", System.DateTime.Now);   // 11
Console::WriteLine("{0 :HH}", System.DateTime.Now);   // 11

Console::WriteLine("{0 :mm}", System.DateTime.Now);   // 50
Console::WriteLine("{0 :MM}", System.DateTime.Now);   // 03

Console::WriteLine("{0 :MMM}", System.DateTime.Now);  // �T��
Console::WriteLine("{0 :MMMM}", System.DateTime.Now); // �T��

Console::WriteLine("{0 :ss}", System.DateTime.Now);   // 43
Console::WriteLine("{0 :tt}", System.DateTime.Now);   // �W��

Console::WriteLine("{0 :yy}", System.DateTime.Now);   // 12
Console::WriteLine("{0 :yyyy}", System.DateTime.Now); // 2012
Console::WriteLine("{0 :zz}", System.DateTime.Now);   // +08
Console::WriteLine("{0 :zzz}", System.DateTime.Now);  // +08:00
Console::WriteLine("{0 :hh:mm:ss}", System.DateTime.Now);  // 11�G43�G34
Console::WriteLine("{0 :dd/MM/yyyy}", System.DateTime.Now); // 27-03-2012
*/


/*
	Console::WriteLine(L"size of Wtemp = {0}",sizeof(Wtemp));

	unsigned char SCON0=0xff;


    unsigned char RIF      = SCON0^0;
    unsigned char TIF      = SCON0^1;
    unsigned char RB8      = SCON0^2;
    unsigned char TB8      = SCON0^3;
    unsigned char REN      = SCON0^4;
    unsigned char SM2      = SCON0^5;
    unsigned char SM1      = SCON0^6;
    unsigned char SM0      = SCON0^7;


	Console::WriteLine("RIF={0}",RIF);
	Console::WriteLine("TIF={0}",TIF);
	Console::WriteLine("RB8={0}",RB8);
	Console::WriteLine("TB8={0}",TB8);
	Console::WriteLine("REN={0}",REN);
	Console::WriteLine("SM2={0}",SM2);
	Console::WriteLine("SM1={0}",SM1);
	Console::WriteLine("SM0={0}",SM0);
*/

	/*
	unsigned char 	 MtState = start;

	switch(MtState)
	{
	case start:
			Console::WriteLine("start MtState={0}",MtState);
		break;

	case stop:
			Console::WriteLine("stop MtState={0}",MtState);
		break;

	default:
			Console::WriteLine("others MtState={0}",MtState);
		break;
	}
	*/
    return 0;
}

int test_NewFunction()
{
	int aaa=0;
	printf("aaa=%d\n",aaa);

	aaa=123;
	printf("aaa=%d\n",aaa);


	aaa=b11111111;


	printf("aaa=%d\n",aaa);



	unsigned char Tx1_Buffer[123];
	unsigned char Tx2_Buffer[]="This is a lion-mouse.";

	int number;
	number = countof(Tx1_Buffer);
	printf("number=%d\n",number);
	number = countof(Tx2_Buffer);
	printf("number=%d\n",number);

	//I2C_TypeDef I2C;
	//printf("size of I2C_TypeDef=%d\n",sizeof(I2C));


	return 0;
}


/*
int test_NewFunction()
{


	return 0;
}
*/
