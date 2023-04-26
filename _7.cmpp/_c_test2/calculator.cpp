#include <iostream>
#include <math.h>
#include <time.h>	//����random�ݥ[
#include <fstream>
#include <time.h>
#include <windows.h>
#define StopProg 1
#define colorHeavy 30	//�`��
#define colorLight 100	//�L��
#define add +

using namespace std;
typedef unsigned long ULONG;
typedef unsigned char BYTE;

void lion();
void swap(int* pA,int* pB,int* sum);
int findSmall(int n1,int n2);

long double pow(int t1,int t2); //��t1��t2����
int bin2dec(char* bbb);
int hex2dec(char* hhh);  //�u�䴩��FFF_FFFF (7��F)
int str2num(char* sss);
long double OPERATION(char oprtr,long double oprnd1,long double oprnd2,long double& result);
int tb_debug_kernel(char* cmd_line);
double avg(int* pT);
const long double pi = 3.14159265358979;

int compare_array(int* number_array_A,int* number_array_B,int* array_A, int* array_B);

int  cmdCount=0;

int main()
{
  char            cmd_line[120];
  int             j,ret_val;
  const char LionMesg[] = "This is a lion. Lion Lion Lion\n";
  printf(LionMesg);
  printf("\nFor help on the calculator, enter:  help or ?\n");
  while(1)
  {
      cmdCount++;
      printf("\nLion>");
      gets(cmd_line);
      ret_val = tb_debug_kernel(cmd_line);

      if( ret_val == StopProg )
      {
          return 0;
      }

      for( j=0; j<120; j++)
          cmd_line[j] = 0;
  }
}

int tb_debug_kernel(char* cmd_line)
{
    //**************simulation control***********************
    char            cmd_name[40];
    char            cmd_arg[20][40];
    unsigned int    cmd_str_ptr=0;
    unsigned int    arg_num,j,k; 
    const char LionMesg[] = "This is a lion. Lion Lion Lion\n";

    //********************parsing ***********************
    // clear buffers
    for( j=0; j<40; j++)
        cmd_name[j] = 0;
    for( j=0; j<20; j++)
        for( k=0; k<40; k++)
            cmd_arg[j][k] = 0;
    cmd_str_ptr = 0;
    while((cmd_line[cmd_str_ptr]==' ' || cmd_line[cmd_str_ptr]=='\t') && cmd_str_ptr<120)
        cmd_str_ptr ++;			//��Ū��ťթ�tab�ɡA���csp����m
    j = 0;
    while((cmd_line[cmd_str_ptr]!=' ' && cmd_line[cmd_str_ptr]!='\t') && cmd_line[cmd_str_ptr]!='\0' && cmd_line[cmd_str_ptr]!='\n' && cmd_str_ptr<120)  
        cmd_name[j++] = cmd_line[cmd_str_ptr++];    //get first command name //��Ĥ@�Ӧr��Ū�icmd_name
    cmd_name[j]='\0';
    if( cmd_str_ptr >= 120 )
        printf("Invalid input\n");
    // similarly, then get the arguments, too
    arg_num=0;
    while(1)
    {
        j=0;
        while((cmd_line[cmd_str_ptr]==' ' || cmd_line[cmd_str_ptr]=='\t') && cmd_str_ptr<120) 
            cmd_str_ptr ++;
        if( cmd_line[cmd_str_ptr] >= 120 || cmd_line[cmd_str_ptr]=='\0'|| cmd_line[cmd_str_ptr]=='\n')
            break;
        while(cmd_line[cmd_str_ptr]!='\0' && cmd_line[cmd_str_ptr]!=' '&& cmd_line[cmd_str_ptr]!='\t' && cmd_line[cmd_str_ptr]!='\n' && cmd_str_ptr<120)
            cmd_arg[arg_num][j++] = cmd_line[cmd_str_ptr++];
        cmd_arg[arg_num][j]='\0';
        if( j > 1 || j==1 && cmd_arg[arg_num][j]!=' ') // && cmd_arg[arg_num][j]!='\0')
            arg_num++;
    }
    
  // �}�l�U���\�� ///////////////////////////////////////////////////////

  // readme ////////////////////////////////////////////////////////////////
  if ( strcmp(cmd_name, "readme") == 0)
  {
    cout << "Readme!!\n";
  }
          
  // help ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "help") == 0 || strcmp(cmd_name, "?") == 0 )
  {
	  printf("\n");
	  printf("  L             IIIIIIIII         O        NNN       NNN\n");
	  printf("  L                 I           O   O       N N       N\n");
	  printf("  L                 I         O       O     N   N     N\n");
	  printf("  L                 I        O         O    N    N    N\n");
	  printf("  L                 I        O         O    N     N   N\n");
	  printf("  L                 I        O         O    N      N  N\n");
	  printf("  L                 I         O       O     N       N N\n");
	  printf("  L                 I           O   O       N        N\n");
	  printf("  LLLLLLLLLLL   IIIIIIIII         O        NNN       NNN\n");
    printf("Referecnce command:\n");
    printf("? or help\t\tFor this help menu\n");
    printf("hex2dec aaaa\t\t�Q���i��  ��    �Q�i��\n");
    printf("hex2bin aaaa\t\t�Q���i��  ��    �G�i��\n");
    printf("dec2hex 4096\t\t  �Q�i��  ��  �Q���i��\n");
    printf("dec2bin 4096\t\t  �Q�i��  ��    �G�i��\n");
    printf("bin2hex 11111111\t  �G�i��  ��  �Q���i��\n");
    printf("bin2dec 11111111\t  �G�i��  ��    �Q�i��\n");
    printf("str2num 1111\n");
    printf("pow 2 4\n");
    printf("add 2 4\n");
    printf("sub 2 4\n");
    printf("mul 2 4\n");
    printf("div 2 4\n");
    printf("123+456-789*123/456\n");
	printf("cmpfiles -f1 p1.yuv -f2 p2.yuv -size 32 8\tCompare file p1.yuv with p2.yuv.\n");


    printf("\nquit \t\t\tLeave the calculator.\n");
    printf("\n\nnote: DOS commands are also available.\n");
  }

  // version ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "ver") == 0)
  {
      //printf("\nCalculator 2004  [���� 0.9.0] [ Oct 13, 2004 �P���T ]\n");
      printf("++------------------------------------------------------------------------++\n");
      printf("||                       Calculator 2004 (TM)                             ||\n");
      printf("||            Version: 0.9.0 () -- Wed Oct 13 12:00:00 2004               ||\n");
      printf("||        Copyright (c) 1987-2004 by Realtek Semiconductor Corp.          ||\n");
      printf("||                        All Rights Reserved                             ||\n");
      printf("||                                                                        ||\n");
      printf("||     For support, send email to calculator-support@realtek.com.tw       ||\n");
      printf("||                                                                        ||\n");
      printf("||     This program is proprietary and confidential information of        ||\n");
      printf("||   Realtek Semiconductor Corp. and may be used and disclosed only as    ||\n");
      printf("|| authorized in a license agreement controlling such use and disclosure. ||\n");
      printf("++------------------------------------------------------------------------++\n");
	  printf("\n");
	  printf("  L             IIIIIIIII         O        NNN       NNN\n");
	  printf("  L                 I           O   O       N N       N\n");
	  printf("  L                 I         O       O     N   N     N\n");
	  printf("  L                 I        O         O    N    N    N\n");
	  printf("  L                 I        O         O    N     N   N\n");
	  printf("  L                 I        O         O    N      N  N\n");
	  printf("  L                 I         O       O     N       N N\n");
	  printf("  L                 I           O   O       N        N\n");
	  printf("  LLLLLLLLLLL   IIIIIIIII         O        NNN       NNN\n");
	  printf(LionMesg);
  }

  // lion ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "lion") == 0 || strcmp(cmd_name, "mouse") == 0 )
  {
	  printf("\n");
	  printf("  L             IIIIIIIII         O        NNN       NNN\n");
	  printf("  L                 I           O   O       N N       N\n");
	  printf("  L                 I         O       O     N   N     N\n");
	  printf("  L                 I        O         O    N    N    N\n");
	  printf("  L                 I        O         O    N     N   N\n");
	  printf("  L                 I        O         O    N      N  N\n");
	  printf("  L                 I         O       O     N       N N\n");
	  printf("  L                 I           O   O       N        N\n");
	  printf("  LLLLLLLLLLL   IIIIIIIII         O        NNN       NNN\n");

	  char mytext[]={"�v���A�n�ڡI�I"};
	  char title[]={"LionMouse"};
	  printf("The return value = %d", MessageBox(NULL,mytext,title,MB_OKCANCEL) );
	  printf(LionMesg);

  }

  else if ( cmd_name[0] >= 48 && cmd_name[0] <= 57)
  {
      if ( cmd_name[0] == 48 && strlen(cmd_name) == 1)
      {
          printf("See you next time. Bye~\n\n");
          return StopProg;
      }
      char oprtr[10];
      long double oprnd [10];
      long double result=0;
      long double result_last=0;
      int  oprnd_num=0;
      int  oprtr_num=0;
      int  length=0;
      int  ret;
      int  k;
      int decimal_flag;
      

      //printf("total length=%d\n",strlen(cmd_name));
      for (int i=0;i<strlen(cmd_name);i++)
      {
          if ( cmd_name[i] == '+' || cmd_name[i] == '-' || cmd_name[i] == '*' || cmd_name[i] == '/')
          {
              decimal_flag=0;
              result=result_last;
              oprnd[oprnd_num]=0;
              oprtr[oprtr_num]=cmd_name[i];
              //printf("now i=%d\tlength=%d\n",i,length);
              for (k=0;k<length;k++)
              {
                  //printf("now cmd_name[%d]=%c\n",k+i-length,cmd_name[k+i-length]);
                  if (cmd_name[k+i-length] == '.')
                  {
                      //printf("decimal exists.\n");
                      decimal_flag++;
                  }
              }
              if (decimal_flag==1)
              {
                  long double decimal=0;
                  int idx;
                  //printf("decimal exists.\n");
                  for (idx=0;idx<length;idx++)
                  {
                      if (cmd_name[idx+i-length] == '.')
                      {
                          //printf("small point at %d.\n",idx);
                          break;
                      }
                  }
                  for (k=0;k<idx;k++)
                  {
                      oprnd[oprnd_num]+=(cmd_name[k+i-length]-48)*pow(10,length-idx-k-1);
                      //printf("now ��Ƴ����� %f\n",oprnd[oprnd_num]);
                  }
                  for (k=0;k<(length-idx-1);k++)
                  {
                      decimal+=(cmd_name[length-idx+k+1]-48)*pow(10,-1-k);
                      //printf("now �p�Ƴ����� %f\n",decimal);
                  }
                  //decimal=decimal/pow(10,i-idx-1);
                  //printf("���=%f\t�p��=%f\n",oprnd[oprnd_num],decimal);
                  oprnd[oprnd_num]=oprnd[oprnd_num]+decimal;
                  //printf("����%f\n",oprnd[oprnd_num]);
              }
              else if (decimal_flag==0)
              {
                  for (k=0;k<length;k++)
                  {
                      oprnd[oprnd_num]+=(cmd_name[k+i-length]-48)*pow(10,length-k-1);
                  }

              }
              else
              {
                  printf("Illegal number.\n");
                  break;
              
              }
              if (oprnd_num==0)
              {
                  result_last=oprnd[0];
              }
              else if (oprnd_num>=1)
              {
                  ret=OPERATION(oprtr[oprtr_num-1],result_last,oprnd[oprnd_num],result);
                  if(ret==-1)
                  {
                      printf("Illegal operation!!\n");
                  }
                  result_last=result;
              }
              oprnd_num++;
              oprtr_num++;
              length=-1;
          }
          length++;
      }
      oprnd[oprnd_num]=0;
      //printf("nnnnow i=%d\tlength=%d\n",i,length);
      //      for (k=0;k<length;k++)
      //      {
      //          oprnd[oprnd_num]+=(cmd_name[k+i-length]-48)*pow(10,length-k-1);
      //      }
      decimal_flag=0;
      for (k=0;k<length;k++)
      {
          //printf("now cmd_name[%d]=%c\n",k+i-length,cmd_name[k+i-length]);
          if (cmd_name[k+i-length] == '.')
          {
              //printf("decimal exists.\n");
              //printf("���ɦb%d��m�C\n",k+i-length);

              decimal_flag++;
          }
      }
      if (decimal_flag==1)
      {
          long double decimal=0;
          int idx;
          //printf("decimal exists.\n");
          for (idx=0;idx<length;idx++)
          {
              if (cmd_name[idx+i-length] == '.')
              {
                  //printf("small point at %d.\n",idx);
                  break;
              }
          }
          for (k=0;k<idx;k++)
          {
              oprnd[oprnd_num]+=(cmd_name[k+i-length]-48)*pow(10,length-idx-k-1);
              //printf("now ��Ƴ����� %f\n",oprnd[oprnd_num]);
          }
          for (k=0;k<(length-idx-1);k++)
          {
              decimal+=(cmd_name[length-idx+k+1]-48)*pow(10,-1-k);
              //printf("now �p�Ƴ����� %f\n",decimal);
          }
          //decimal=decimal/pow(10,i-idx-1);
          //printf("���=%f\t�p��=%f\n",oprnd[oprnd_num],decimal);
          oprnd[oprnd_num]=oprnd[oprnd_num]+decimal;
          //printf("����%f\n",oprnd[oprnd_num]);
      }
      else if (decimal_flag==0)
      {
          for (k=0;k<length;k++)
          {
              oprnd[oprnd_num]+=(cmd_name[k+i-length]-48)*pow(10,length-k-1);
          }
      }
      else
      {
          printf("Illegal number.\n");
      }
      ret=OPERATION(oprtr[oprtr_num-1],result_last,oprnd[oprnd_num],result);
      if(ret==-1)
      {
          printf("Illegal operation!!\n");
      }
      else
          printf("%s  =>   %.15f\n",cmd_name,result);
  }

  else if ( strcmp(cmd_name, "r") == 0)
  {
  //ex: cmpfiles -tf1 t1.txt -tf2 t2.txt	=> 4
	  int cmpfiles_fail=0;
	  const ULONG BufferSize=1500;      //�ɮ׸��`�@�h�֭�byte�A�ݧ�j
	  char mem_read[BufferSize][20];    //�C�Ӧr��̤j�e�q
	  int dataCount1=0;      //���Ī�data�`��
	  int nonhex=0;
	  ifstream fin("l1.txt");
	  if(!fin)
		  {
			  printf("�ɮ�l1.txt�䤣��A�A�O���O����a��F\n");
			  printf("The command is NOT accomplished.\n");
			  cmpfiles_fail=1;
		  }
		  else
		  {
			  //printf("�ɮ� %s �w�}��\n",cmd_arg_file_t_1);
			  printf("�ɮ� l1.txt �w�}��\n");
			  while(!fin.eof())//���٨S��Ū���ɧ���
			  {
				  fin >> mem_read[dataCount1];
				  printf("���ɪ�mem_read[%2d]���G%s\n",dataCount1,mem_read[dataCount1]);
				  //printf("mem_read[%d]=%s\teof=%d\tlength=%d\n",dataCount1,mem_read[dataCount1],fin.eof(),strlen(mem_read[dataCount1]));
				  mem_read[dataCount1][strlen(mem_read[dataCount1])]='\0';
				  dataCount1++;
				  cout << "\n";

			  }
		  }

  }

  // �������ɮ׬O�_�@��
  // cmpfiles ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "cmpfiles") == 0)
  {   
      //cout <<"here";
	  int cmpfiles_fail=0;
      char cmd_arg_file_b_1[20]="";
      char cmd_arg_file_b_2[20]="";
      char cmd_arg_file_t_1[20]="";
      char cmd_arg_file_t_2[20]="";
      int  cmd_arg_width=-1;      
      int  cmd_arg_height=-1;      
      bool  showMesg=0;      
	  bool  showGrid=0;
      int  arg_num_i=0;
      while(arg_num_i < arg_num)
      {
          printf("����arg_num_i=%d\n",arg_num_i);
		  if( strcmp(cmd_arg[arg_num_i], "-f1") == 0 )
          {
              strcpy(cmd_arg_file_b_1 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-f2") == 0 )
          {
              strcpy(cmd_arg_file_b_2 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-tf1") == 0 )
          {
              strcpy(cmd_arg_file_t_1 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-tf2") == 0 )
          {
              strcpy(cmd_arg_file_t_2 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-size") == 0 )
          {
              cmd_arg_width =str2num(cmd_arg[arg_num_i +1]);
              cmd_arg_height=str2num(cmd_arg[arg_num_i +2]);
              arg_num_i += 2;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-m") == 0 )
          {
              showMesg=1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-g") == 0 )
          {
              showGrid=1;
          } 
          arg_num_i += 1;
      }

	  if((arg_num==7 || arg_num==8 || arg_num==9) && strlen(cmd_arg_file_b_1) && strlen(cmd_arg_file_b_2) && cmd_arg_width!=-1 && cmd_arg_height!=-1 )
      //cmpfiles -f1 p1.yuv -f2 p2.yuv -size 32 8 => 7
      {
          cout << "there";
		  FILE  *image_file1;
		  BYTE  *data1;                      //buffer�j�p
		  BYTE  *data2;                      //buffer�j�p
		  BYTE  *data3;                      //buffer�j�p
		  data1 = new BYTE[cmd_arg_width*cmd_arg_height];
		  data2 = new BYTE[cmd_arg_width*cmd_arg_height];
		  data3 = new BYTE[cmd_arg_width*cmd_arg_height];
          image_file1 = fopen(cmd_arg_file_b_1, "rb");
          if(!image_file1)
          {
              printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",cmd_arg_file_b_1);
              printf("The command is NOT accomplished.\n");
              cmpfiles_fail=1;
          }
		  else
          {
              int i=0;
			  
              while(i<cmd_arg_width*cmd_arg_height)
                  data1[i++] = fgetc(image_file1);
			  //printf("�ɮ� %s �@�� %d ���I\n",cmd_arg_file_b_1,i);
			  int j=0;
			  fclose(image_file1);
		  }
		  if (!cmpfiles_fail)
		  {
			  FILE  *image_file2;
			  image_file2 = fopen(cmd_arg_file_b_2, "rb");
			  if(!image_file2)
			  {
				  printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",cmd_arg_file_b_2);
				  printf("The command is NOT accomplished.\n");
				  cmpfiles_fail=1;
			  }
			  else
			  {
				  int j=0;
				  while(j<cmd_arg_width*cmd_arg_height)
					  data2[j++] = fgetc(image_file2);
				  //printf("�ɮ� %s �@�� %d ���I\n",cmd_arg_file_b_2,j);
				  fclose(image_file2);
			  }
		  }
		  if(!cmpfiles_fail)
		  {
			  int k=0;
			  int mismatch=0;
			  printf("�������ɮת��e %d ���I\n",cmd_arg_width*cmd_arg_height);
			  while(k<cmd_arg_width*cmd_arg_height)
			  {
//				  data3[k]=data2[k]-data1[k];
				  //00����	FF����
				  if (data1[k]!=data2[k])
				  {
					  if (showMesg)
					  {
						  printf("�b %3d �I��줣�P��\t",k);
						  printf("�ɮ�1��%2x �ɮ�2��%2x\n",data1[k],data2[k]);
					  }
					  mismatch++;
					  data3[k]=0;
				  }
				  else
				  {
					  data3[k]=255;
				  }
				  k++;
			  }
			  if (!mismatch)
				  printf("The two files are the same.\n");
			  else
			  {
				  if(showGrid)
				  {
					  cout << "show grid\n";
					  //�W
					  for (int i=0;i<cmd_arg_width;i++)
					  {
						  if(!(i%2))
							  data3[i]=colorHeavy;
						  else
							  data3[i]=colorLight;
					  }
					  //�U
					  for (i=cmd_arg_width*cmd_arg_height-cmd_arg_width;i<cmd_arg_width*cmd_arg_height;i++)
					  {
						  if((i+cmd_arg_height)%2)
							  data3[i]=colorHeavy;
						  else
							  data3[i]=colorLight;
					  }
					  //���k
					  for (i=1;i<(cmd_arg_height-1);i++)
					  {
						  if(!(i%2))
						  {
							  data3[i*cmd_arg_width]=colorHeavy;
							  data3[(i+1)*cmd_arg_width-1]=colorLight;
						  }
						  else
						  {
							  data3[i*cmd_arg_width]=colorLight;
							  data3[(i+1)*cmd_arg_width-1]=colorHeavy;
						  }
					  }
				  }			//cmpfiles -f1 A -f2 B -size 352 288 -g
				  FILE  *image_file3;
				  image_file3 = fopen("difference.yuv", "wb");
				  int i=0;
				  while(i<cmd_arg_width*cmd_arg_height)
				  {
					  fputc(data3[i], image_file3);
					  i++;
				  }

				  fclose(image_file3);
				  printf("The two files are NOT the same.\n");
				  printf("�B�@��%d�Ӥ��P�I\n",mismatch);
				  float likeness;
				  likeness=100*(cmd_arg_width*cmd_arg_height-mismatch);
				  likeness=likeness/(cmd_arg_width*cmd_arg_height);
				  printf("��Ϫ��ۦ��׬� %0.2f %%\n",likeness);
				  printf("�w�g���Ϫ��ۮt�s�b�ɮ�difference.yuv�ؤF�C\n");
			  }
          }
		  delete [] data1;
		  delete [] data2;
		  delete [] data3;
      }

	  if(cmpfiles_fail==1)
	  {
	  printf("Usage: \n\
cmpfiles [-f1 image_file1] [-f2 image_file2] [-size width height] \n\
Description: \n\
Compare two files. \n\
Options: \n\
-f1:   Binary image file 1\n\
-f2:   Binary image file 2\n\
-size:Image size \n\
Reference command:\n\
cmpfiles -f1 p1.yuv -f2 p2.yuv -size 32 8\n\
Compare file p1.yuv with p2.yuv.\n\
");
	  }
	  else
	  {
		  printf("The command is accomplished.\n");
	  }
}
  
  // �[��
  // inc ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "inc") == 0)
  {   
      //inc -f1 foreman_A.y -f2 foreman_A2.y -size 352 288 -q 10	=>9
      cout <<"here inc";
	  int inc_fail=0;
      char cmd_arg_file_b_1[20]="";
      char cmd_arg_file_b_2[20]="";
      int  cmd_arg_width=-1;      
      int  cmd_arg_height=-1;      
      int  cmd_arg_quantity=-1;      
      int  arg_num_i=0;
      while(arg_num_i < arg_num)
      {
          printf("����arg_num_i=%d\n",arg_num_i);
          if( strcmp(cmd_arg[arg_num_i], "-f1") == 0 )
          {
              strcpy(cmd_arg_file_b_1 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-f2") == 0 )
          {
              strcpy(cmd_arg_file_b_2 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-size") == 0 )
          {
              cmd_arg_width =str2num(cmd_arg[arg_num_i +1]);
              cmd_arg_height=str2num(cmd_arg[arg_num_i +2]);
              arg_num_i += 2;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-q") == 0 )
          {
              cmd_arg_quantity =str2num(cmd_arg[arg_num_i +1]);
          } 
          arg_num_i += 1;
      }
      
       if((arg_num==9) && strlen(cmd_arg_file_b_1) && strlen(cmd_arg_file_b_2) && cmd_arg_width!=-1 && cmd_arg_height!=-1 && cmd_arg_quantity!=-1)
      //inc -f1 foreman.y -f2 foreman2.y -size 352 288 -q 10	=>9
      {
		  FILE  *image_file1;
		  FILE  *image_file2;
		  BYTE  *data1;                      //buffer�j�p
		  BYTE  *data2;                      //buffer�j�p
		  data1 = new BYTE[cmd_arg_width*cmd_arg_height];
		  data2 = new BYTE[cmd_arg_width*cmd_arg_height];
          image_file1 = fopen(cmd_arg_file_b_1, "rb");
		  image_file2 = fopen(cmd_arg_file_b_2, "wb");
          printf("�v���W�j�q %d \n",cmd_arg_quantity);
		  if(!image_file1)
          {
              printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",cmd_arg_file_b_1);
              printf("The command is NOT accomplished.\n");
              inc_fail=1;
          }
		  else
          {
              int i=0;
			  
              while(i<cmd_arg_width*cmd_arg_height)
              {
                  data1[i] = fgetc(image_file1);
				  if ((data1[i]+cmd_arg_quantity)>255)
					  data2[i]=255;
				  else if ((data1[i]+cmd_arg_quantity)<0)
					  data2[i]=0;
				  else
					  data2[i]=data1[i];
				  fputc(data2[i], image_file2);
				  i++;
			  }
			  printf("�ɮ� %s �@�� %d ���I\n",cmd_arg_file_b_1,i);
			  fclose(image_file1);
			  fclose(image_file2);
		  }
		  delete [] data1;
		  delete [] data2;
	   }
  	  if(inc_fail==1)
	  {
	  printf("Usage: \n\
inc [-f1 image_file1] [-f2 image_file2] [-size width height] \n\
Description: \n\
Compare two files. \n\
Options: \n\
-f1:   Binary image file 1\n\
-f2:   Binary image file 2\n\
-size:Image size \n\
Reference command:\n\
inc -f1 p1.yuv -f2 p2.yuv -size 32 8\n\
Compare file p1.yuv with p2.yuv.\n\
");
	  }
	  else
	  {
		  printf("The command is accomplished.\n");
	  }
}


  // IVPD	��IVPD�����G
  // stat ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "stat") == 0 || strcmp(cmd_name, "s") == 0 )
  {   
      //stat
      cout <<"here stat\n";
	  int stat_fail=0;
      char stat_file[20];
      int  cmd_arg_width=16;      
      int  cmd_arg_height=16;      
      int  arg_num_i=0;
	  int data[256];
	  int blk0[128];
	  int blk1[128];
	  int d01=0;
	  int d0=0;
	  int d1=0;
	  int dd=0;
	  int result;

	  strcpy(stat_file, cmd_arg[0]);
	  FILE  *image_file;
	  image_file = fopen(stat_file, "rb");
	  if(!image_file)
	  {
		  printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",stat_file);
		  printf("The command is NOT accomplished.\n");
	  }
	  else
	  {
		  int i=0;
		  int idx_i=0;
		  int idx_j=0;
		  while(i<256)
		  {
			  data[i] = fgetc(image_file);
			  if((i%32)<16)
			  {
				  blk0[idx_i]=data[i];
				  idx_i++;
			  }
			  else
			  {
				  blk1[idx_j]=data[i];
				  idx_j++;
			  }
			  i++;
		  }
		  fclose(image_file);
//ivpd	DF
		  for (i=0;i<128;i++)
		  {
			  d01=d01+abs(blk1[i]-blk0[i]);
		  }
		  for (i=0;i<(64-16);i++)
		  {
			  d01=d01+abs(blk1[i]-blk0[i+16]);
		  }
		  for (i=64;i<(128-16);i++)
		  {
			  d01=d01+abs(blk1[i]-blk0[i+16]);
		  }
//ivpd	SF
		  for (i=0;i<(128-16);i++)
		  {
			  d0=d0+abs(blk0[i]-blk0[i+16]);
			  d1=d1+abs(blk1[i]-blk1[i+16]);
		  }
		  dd=d0+d1;

		  result=(d01<<16 | dd);
		  
		  printf("d01 = %d\n",d01);
		  printf("d0 = %d\n",d0);
		  printf("d1 = %d\n",d1);
		  printf("dd = %d\n",dd);
		  printf("result = %d\n",result);
		  printf("result = %08x\n",result);

		  if((d0-d1>0)&&(d01-dd>0))
		  {
			  printf("�ŦX����Ado��d1�j %d ",d0-d1);
		  }

	  }
  }

  // AVGVPD	��AVGVPD�����G
  // stat ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "avgvpd") == 0 || strcmp(cmd_name, "a") == 0 )
  {   
      //stat
      cout <<"here AVGVPD\n";
	  int stat_fail=0;
      char stat_file[20];
      int  cmd_arg_width=16;      
      int  cmd_arg_height=16;      
      int  arg_num_i=0;
	  float data[256];
	  float blk0[128];
	  float blk1[128];
	  float d01=0;
	  float d0=0;
	  float d1=0;
	  float dd=0;
	  float result;

	  strcpy(stat_file, cmd_arg[0]);
	  FILE  *image_file;
	  image_file = fopen(stat_file, "rb");
	  if(!image_file)
	  {
		  printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",stat_file);
		  printf("The command is NOT accomplished.\n");
	  }
	  else
	  {
		  int i=0;
		  int idx_i=0;
		  int idx_j=0;
		  while(i<256)
		  {
			  data[i] = fgetc(image_file);
			  i++;
		  }

		  for (i=0;i<256;i++)
		  {
			  data[i]=(int)(-(data[i])/2);	//rounding first if int
			  printf("data[%d]=%f\t",i,data[i]);
			  data[i]=floor(data[i]);	//rounding
			  printf("data[%d]=%f\t",i,data[i]);
		  }

		  fclose(image_file);

		  i=0;
		  while(i<256)
		  {
			  //data[i] = fgetc(image_file);
			  if((i%32)<16)
			  {
				  blk0[idx_i]=data[i];
				  idx_i++;
			  }
			  else
			  {
				  blk1[idx_j]=data[i];
				  idx_j++;
			  }
			  i++;
		  }
//ivpd	DF
		  for (i=0;i<128;i++)
		  {
			  d01=d01+abs(blk1[i]-blk0[i]);
		  }
		  for (i=0;i<(64-16);i++)
		  {
			  d01=d01+abs(blk1[i]-blk0[i+16]);
		  }
		  for (i=64;i<(128-16);i++)
		  {
			  d01=d01+abs(blk1[i]-blk0[i+16]);
		  }
//ivpd	SF
		  for (i=0;i<(128-16);i++)
		  {
			  d0=d0+abs(blk0[i]-blk0[i+16]);
			  d1=d1+abs(blk1[i]-blk1[i+16]);
		  }
		  dd=d0+d1;

		  result=((int)d01<<16 | int(dd));
		  
		  printf("d01 = %d\n",d01);
		  printf("d0 = %d\n",d0);
		  printf("d1 = %d\n",d1);
		  printf("dd = %d\n",dd);
		  printf("result = %d\n",result);
		  printf("result = %08x\n",result);

		  if((d0-d1>0)&&(d01-dd>0))
		  {
			  //printf("�ŦX����Ado��d1�j %d ",d0-d1);
		  }

	  }
  }

  // BLKDC	��BLKDC�����G
  // stat ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "blkdc") == 0 || strcmp(cmd_name, "blk") == 0 )
  {   
      //stat
      cout <<"here BLKDC\n";
	  int stat_fail=0;
      char stat_file[20];
      int  cmd_arg_width=64;      
      int  cmd_arg_height=64;      
      int  arg_num_i=0;
	  float data[4096];
	  float result;
	  //strcpy(stat_file, cmd_arg[0]);
	  strcpy(stat_file, "4k_rand_0.y");
	  FILE  *image_file;
	  image_file = fopen(stat_file, "rb");
	  if(!image_file)
	  {
		  printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",stat_file);
		  printf("The command is NOT accomplished.\n");
	  }
	  else
	  {
		  int i=0;
		  int idx_i=0;
		  int idx_j=0;
		  while(i<4096)
		  {
			  data[i] = fgetc(image_file);
			  i++;
		  }
		  fclose(image_file);
		  result=100;
		  printf("\nTotal=%f\n",result);

		  for (i=0;i<2048;i++)
		  {
			  printf("data[%d]=%f\t",i,data[i]);
			  result+=data[i];
		  }
		  printf("\nTotal=%f\n",result);

		  printf("\nBLKDC=%f\n",result/2048);


	  }
  }



  // verfiltk332
  // 332 ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "v") == 0 || strcmp(cmd_name, "verfiltk") == 0 )
  {   
      //stat
      cout <<"here VERFILTK_332\n";
	  int verfiltk_fail=0;
      char verfiltk_file[20];
      int  cmd_arg_width=64;      
      int  cmd_arg_height=64;      
      int  arg_num_i=0;
	  float data[4096];
	  float result;
	  //strcpy(verfiltk_file, cmd_arg[0]);
	  strcpy(verfiltk_file, "verfiltk332_2.y");
	  FILE  *image_file;
	  image_file = fopen(verfiltk_file, "rb");
	  if(!image_file)
	  {
		  printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",verfiltk_file);
		  printf("The command is NOT accomplished.\n");
	  }
	  else
	  {
		  int i=0;
		  int idx_i=0;
		  int idx_j=0;
		  while(i<4096)
		  {
			  data[i] = fgetc(image_file);
			  i++;
		  }
		  fclose(image_file);


		  int A,AR,AG,AB,B;
/*
		  A=0xaa;
		  AR=(A>>5)&0x7;
		  AG=(A>>2)&0x7;
		  AB=(A>>0)&0x3;
		  B=(AR&0x7)<<5|(AG&0x7)<<2|(AB&0x3)<<0;
		  printf("A =%d\n", A);
		  printf("AR=%d\n",AR);
		  printf("AG=%d\n",AG);
		  printf("AB=%d\n",AB);
		  printf("B =%d\n", B);
*/

		  int source_R,source_G,source_B;
		  for (i=64;i<72;i++)
		  {
			  A=data[i];
			  AR=(A>>5)&0x7;
			  AG=(A>>2)&0x7;
			  AB=(A>>0)&0x3;
			  B=(AR&0x7)<<5|(AG&0x7)<<2|(AB&0x3)<<0;
			  printf("source = ox %x = %d\t",A,A);
			  //printf("A =%d\n", A);
			  //printf("AR=%d\n",AR);
			  //printf("AG=%d\n",AG);
			  //printf("AB=%d\n",AB);
			  //printf("B =%d\n", B);
			  source_R=(AR&0x7)<<5|(AR&0x7)<<2|(AR&0x7)>>1;
			  source_G=(AG&0x7)<<5|(AG&0x7)<<2|(AG&0x7)>>1;
			  source_B=(AB&0x3)<<6|(AB&0x3)<<4|(AB&0x3)<<2|(AB&0x3)<<0;
			  printf("source_R=%d\t",source_R);
			  printf("source_G=%d\t",source_G);
			  printf("source_B=%d\n",source_B);

			  cout << "\n";
		  }




	  }
  }



  // deblock
  else if ( strcmp(cmd_name, "d") == 0 || strcmp(cmd_name, "deblock") == 0 )
  {   
      //stat
      cout <<"here DEBLOCK\n";
	  int deblock_fail=0;
      char deblock_file[20];
      int  cmd_arg_width=64;
      int  cmd_arg_height=64;
      int  arg_num_i=0;
	  float data[4096];
	  float data2[256];
	  float result;
	  //strcpy(deblock_file, cmd_arg[0]);
	  strcpy(deblock_file, "D:/_/_pattern/4k_rand_0.y");
	  FILE  *image_file;
	  image_file = fopen(deblock_file, "rb");
	  if(!image_file)
	  {
		  printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",deblock_file);
		  printf("The command is NOT accomplished.\n");
	  }
	  else
	  {
		  int i=0;
		  int idx_i=0;
		  int idx_j=0;
		  int AAA;
		  while(i<4096)
		  {
			  data[i] = fgetc(image_file);
			  i++;
		  }
		  fclose(image_file);

		  for(i=0;i<10;i++)
		  {
			  printf("aaa=%4d",data[i]);
		  }



		  for(i=0;i<256;i++)
		  {
			  data2[i]=data[(i/16)*64+i%16];
			  printf("%4d",data[i]);
			  printf("kkk=%4d",data[(i/16)*64+i%16]);
		  }









	  }
  }





  // ���h�m��A�d�U�¥�
  // truncate ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "truncate") == 0)
  {   
      //truncate -f1 foreman_A.y -f2 foreman_A2.y -size 352 288 =>7
      cout <<"here truncate";
	  int truncate_fail=0;
      char cmd_arg_file_b_1[20]="";
      char cmd_arg_file_b_2[20]="";
      int  cmd_arg_width=-1;      
      int  cmd_arg_height=-1;      
      int  arg_num_i=0;
      while(arg_num_i < arg_num)
      {
          printf("����arg_num_i=%d\n",arg_num_i);
          if( strcmp(cmd_arg[arg_num_i], "-f1") == 0 )
          {
              strcpy(cmd_arg_file_b_1 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-f2") == 0 )
          {
              strcpy(cmd_arg_file_b_2 , cmd_arg[arg_num_i +1]);
              arg_num_i += 1;
          } 
          else if( strcmp(cmd_arg[arg_num_i], "-size") == 0 )
          {
              cmd_arg_width =str2num(cmd_arg[arg_num_i +1]);
              cmd_arg_height=str2num(cmd_arg[arg_num_i +2]);
              arg_num_i += 2;
          } 
          arg_num_i += 1;
      }
	  if((arg_num==7) && strlen(cmd_arg_file_b_1) && strlen(cmd_arg_file_b_2) && cmd_arg_width!=-1 && cmd_arg_height!=-1 )
      //truncate -f1 NR_in.yuv -f2 NR_in_BW.yuv -size 480 384 => 7
      {
          cout << "there2\n";
		  FILE  *image_file1;
		  FILE  *image_file2;
		  BYTE  *data;                      //buffer�j�p�A�ϧιL�j�i��|����B�z�A�����q�B�z
		  data = new BYTE[cmd_arg_width*cmd_arg_height*1.5];
		  image_file1 = fopen(cmd_arg_file_b_1, "rb");
		  image_file2 = fopen(cmd_arg_file_b_2, "wb");
		  if(!image_file1)
          {
              printf("�ɮ� %s �䤣��A�A�O���O����a��F�H�I\n",cmd_arg_file_b_1);
              printf("The command is NOT accomplished.\n");
              truncate_fail=1;
          }
		  else
          {
			  int i=0;
              while(i<cmd_arg_width*cmd_arg_height*1.5)
              {
                  data[i] = fgetc(image_file1);
                  if (i<cmd_arg_width*cmd_arg_height)
                  {
                  	  fputc(data[i], image_file2);
                  }
                  i++;
              }
              fclose(image_file1);
              fclose(image_file2);
		  }
          delete [] data;
	  }
	  if(truncate_fail==1)
	  {
	  printf("Usage: \n\
truncate [-f1 image_file1] [-f2 image_file2] [-size width height] \n\
Description: \n\
Compare two files. \n\
Options: \n\
-f1:   Binary image file 1\n\
-f2:   Binary image file 2\n\
-size:Image size \n\
Reference command:\n\
truncate -f1 p1.yuv -f2 p2.yuv -size 32 8\n\
��m��Ϥ�p1.yuv �����¥ճ�����X�Ӧs�� p2.yuv.\n\
");
	  }
	  else
	  {
		  printf("The command is accomplished.\n");
	  }
  }

  // �W�d��N�i(�s���¥շ�)
  // get ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "get") == 0)
  {   
      //get
      cout <<"here get\n";
	  int truncate_fail=0;
      char cmd_arg_file_b_1[20]="akiyo.yuv";
      char cmd_arg_file_b_2[20]="akiyo10.y";
      int  cmd_arg_width=352;
      int  cmd_arg_height=288;
      int  idx=10;	//�n�쪺��N�i(N����Ӥj)

		  FILE  *image_file1;
		  FILE  *image_file2;
		  BYTE  *data;                      //buffer�j�p�A�ϧιL�j�i��|����B�z�A�����q�B�z
		  data = new BYTE[cmd_arg_width*cmd_arg_height*1.5*idx];
		  image_file1 = fopen(cmd_arg_file_b_1, "rb");
		  image_file2 = fopen(cmd_arg_file_b_2, "wb");
          int i1=cmd_arg_width*cmd_arg_height*(idx-1)*1.5;
		  int i2=cmd_arg_width*cmd_arg_height*(idx)*1.5;
		  int i3=cmd_arg_width*cmd_arg_height*(idx)*1.5-cmd_arg_width*cmd_arg_height*0.5;
   		  printf("i1=%d\n",i1);
		  printf("i2=%d\n",i2);
		  printf("i3=%d\n",i3);

		  int j=0;
          while(j<i3)
              {
                  data[j] = fgetc(image_file1);
                  if (j>=i1)
                  {
                  	  fputc(data[j], image_file2);
					  //printf("j=%d\n",j);
                  }
                  j++;
              }
			  printf(" finally j=%d\n",j);
              fclose(image_file1);
              fclose(image_file2);
          delete [] data;
  }

  // lion ////////////////////////////////////////////////////////////////
  //ex: lions a.txt b.txt	=> 2
  else if ( strcmp(cmd_name, "lions") == 0)
  {
	  char cmd_arg_file_t_1[20]="";
      char cmd_arg_file_t_2[20]="";
	  const ULONG BufferSize=21480;      //�ɮ׸��`�@�h�֭�byte�A�ݧ�j
	  char mem_read_1[BufferSize][20];    //�C�Ӧr��̤j�e�q
	  char mem_read_2[BufferSize][20];    //�C�Ӧr��̤j�e�q
	  strcpy(cmd_arg_file_t_1 , cmd_arg[0]);
	  strcpy(cmd_arg_file_t_2 , cmd_arg[1]);
	  int cmp_txt_fail=0;
	  bool showMesg=0;
	  bool showGrid=0;
	  if( strcmp(cmd_arg[2], "-m") == 0 || strcmp(cmd_arg[2], "-mice") == 0 )
	  {
		  showMesg=1;
	  } 

	  if((arg_num==2 || (arg_num==3 && showMesg) )&& strlen(cmd_arg_file_t_1) && strlen(cmd_arg_file_t_2))
      {
        ifstream fin1(cmd_arg_file_t_1);
        ifstream fin2(cmd_arg_file_t_2);
        if(!fin1 || !fin2)
        {
			if(!fin1)
				printf("%s : No such file or directory.\n",cmd_arg_file_t_1);
			else
				printf("%s : No such file or directory.\n",cmd_arg_file_t_2);
			printf("The command is NOT accomplished.\n");
			cmp_txt_fail=1;
        }
        else
        {
          printf("File %s and %s are opened.\n",cmd_arg_file_t_1,cmd_arg_file_t_2);
          int dataCount1=0;      //���Ī�data�`��
          int dataCount2=0;      //���Ī�data�`��
          int writemem;
          int nonbin=0;
          int nonhex=0;
          int i;
          int binorhex=1;   //�w�]��Ƴ��Ohex��
          int BitNum=8;

          while(!fin1.eof())//���٨S��Ū���ɧ���
          {
			  fin1 >> mem_read_1[dataCount1];
            //cout << "���ɪ�dataCount1���G" << dataCount1 << '\n';
            //printf("mem_read_1[%d]=%s\teof=%d\tlength=%d\n",dataCount1,mem_read_1[dataCount1],fin1.eof(),strlen(mem_read_1[dataCount1]));
            mem_read_1[dataCount1][strlen(mem_read_1[dataCount1])]='\0';
            nonbin=0;
            nonhex=0;
            writemem=0;
            //�}�l���R��Ū�쪺�C�@�r�ꪺ���
            if (strcmp(mem_read_1[dataCount1],"%bin%") == 0 || strcmp(mem_read_1[dataCount1],"//%bin%") == 0)
            {
              binorhex=0;   //�N�O��binary
              BitNum=8;
              //printf("Data type is changed to binary!\n");
              continue;
            }
            else if (strcmp(mem_read_1[dataCount1],"%hex%") == 0 || strcmp(mem_read_1[dataCount1],"//%hex%") == 0)
            {
              binorhex=1;   //�N�O��hex
              BitNum=2;
              //printf("Data type is changed to hex!\n");
              continue;
            }
            else if (mem_read_1[dataCount1][0]=='\n' || mem_read_1[dataCount1][0]==';' ||mem_read_1[dataCount1][0]=='/' || mem_read_1[dataCount1][0]=='%')
            {
              continue;     //�������p
            }
            //??
            if (mem_read_1[dataCount1][0]=='\n' || mem_read_1[dataCount1][0]==';' ||mem_read_1[dataCount1][0]=='/')
            {
              cout << "���椣��\n";
              continue;     //�������p
            }

            if ((writemem ==1 || fin1.eof() ==1) && !cmp_txt_fail)     //�g���    1.Ū��@ 2.Ū��EOF
            {
              //cout << "read the end.\n";
              BYTE  *data_file_t_1;     //buffer�j�p
              data_file_t_1 = new BYTE[dataCount1];
              if (binorhex==1)  //hex��
              {
                for (i=0;i<dataCount1;i++)
                {
                  data_file_t_1[i] = hex2dec(mem_read_1[i]);
                }
              }
			  /*
			  printf("\n�ɮ�%sŪ�쪺��Ʀ@%d���A�̧Ǭ��G\n",cmd_arg_file_t_1,dataCount1);
			  for (i=0;i<dataCount1;i++)
			  {
				  printf("%0x\t",data_file_t_1[i]);
			  }                      
			  cout << '\n';*/
			  delete [] data_file_t_1;
			  int ret=0;
              if (ret==-1)
              {
                printf("Error encountered when writing data.\n");
                cmp_txt_fail=1;
              }
            }
			dataCount1++;
          }
          fin1.close();
          while(!fin2.eof())//���٨S��Ū���ɧ���
          {
			  fin2 >> mem_read_2[dataCount2];
            //cout << "���ɪ�dataCount2���G" << dataCount2 << '\n';
            //printf("mem_read_2[%d]=%s\teof=%d\tlength=%d\n",dataCount2,mem_read_2[dataCount2],fin2.eof(),strlen(mem_read_2[dataCount2]));
            mem_read_2[dataCount2][strlen(mem_read_2[dataCount2])]='\0';
            nonbin=0;
            nonhex=0;
            writemem=0;
            //�}�l���R��Ū�쪺�C�@�r�ꪺ���
            if (strcmp(mem_read_2[dataCount2],"%bin%") == 0 || strcmp(mem_read_2[dataCount2],"//%bin%") == 0)
            {
              binorhex=0;   //�N�O��binary
              BitNum=8;
              //printf("Data type is changed to binary!\n");
              continue;
            }
            else if (strcmp(mem_read_2[dataCount2],"%hex%") == 0 || strcmp(mem_read_2[dataCount2],"//%hex%") == 0)
            {
              binorhex=1;   //�N�O��hex
              BitNum=2;
              //printf("Data type is changed to hex!\n");
              continue;
            }
            else if (mem_read_2[dataCount2][0]=='\n' || mem_read_2[dataCount2][0]==';' ||mem_read_2[dataCount2][0]=='/' || mem_read_2[dataCount2][0]=='%')
            {
              continue;     //�������p
            }
            //??
            if (mem_read_2[dataCount2][0]=='\n' || mem_read_2[dataCount2][0]==';' ||mem_read_2[dataCount2][0]=='/')
            {
              cout << "���椣��\n";
              continue;     //�������p
            }

            if ((writemem ==1 || fin2.eof() ==1) && !cmp_txt_fail)     //�g���    1.Ū��@ 2.Ū��EOF
            {
              //cout << "read the end.\n";
              BYTE  *data_file_t_2;     //buffer�j�p
              data_file_t_2 = new BYTE[dataCount2];
              if (binorhex==1)  //hex��
              {
                for (i=0;i<dataCount2;i++)
                {
                  data_file_t_2[i] = hex2dec(mem_read_2[i]);
                }
              }

/*			  printf("\n�ɮ�%sŪ�쪺��Ʀ@%d���A�̧Ǭ��G\n",cmd_arg_file_t_2,dataCount2);
			  for (i=0;i<dataCount2;i++)
			  {
				  printf("%0x\t",data_file_t_2[i]);
			  }                      
*/
			  delete [] data_file_t_2;
			  int ret=0;
              if (ret==-1)
              {
                printf("Error encountered when writing data.\n");
                cmp_txt_fail=1;
              }
            }
			dataCount2++;
          }
          fin2.close();
		  dataCount1--;
		  dataCount2--;
/*
			  printf("\n�ɮ�%sŪ�쪺��Ʀ@%d���A�̧Ǭ��G\n",cmd_arg_file_t_1,dataCount1);
			  for (i=0;i<dataCount1;i++)
			  {
				  printf("%0s\t",mem_read_1[i]);
			  }                      
			  printf("\n�ɮ�%sŪ�쪺��Ʀ@%d���A�̧Ǭ��G\n",cmd_arg_file_t_2,dataCount2);
			  for (i=0;i<dataCount2;i++)
			  {
				  printf("%0s\t",mem_read_2[i]);
			  }
*/
		      int dataCount3;
			  dataCount3=findSmall(dataCount1,dataCount2);
			  printf("�ɮ� %s ���ӼƬ� %d\t�ɮ� %s ���ӼƬ� %d\n",cmd_arg_file_t_1,dataCount1,cmd_arg_file_t_2,dataCount2);
			  if(dataCount1!=dataCount2)
			  {
				  printf("����ɮ׭ӼƴN���@�˦h�F�A��M���@���o�C\n");
				  printf("���p�Ƭ�%d\n",dataCount3);
			  }
			  else
			  {
				  printf("����ɮ׭ӼƤ@�˦h�A�U�� %d ���I\n",dataCount3);
			  }

		  if(!cmp_txt_fail)
		  {
			  int k=0;
			  int mismatch=0;
			  printf("�������ɮת��e %d ���I\n",dataCount3);
			  while(k<dataCount3)
			  {
			  if ( strcmp(mem_read_1[k],mem_read_2[k]) != 0 )
				  {
					  if (showMesg)
					  {
						  printf("�b %3d �I��줣�P��\t",k);
						  printf("�ɮ�1��%s �ɮ�2��%s\n",mem_read_1[k],mem_read_2[k]);
					  }
					  mismatch++;
				  }
				  k++;
			  }
			  if (!mismatch)
			  {
				  printf("The two files are the same.\n");
				  printf("��Ϫ��ۦ��׬� 100 %%\n");
			  }
			  else
			  {
				  printf("The two files are NOT the same.\n");
				  printf("�B�@��%d�Ӥ��P�I\n",mismatch);
				  float likeness;
				  likeness=100*(dataCount3-mismatch);
				  likeness=likeness/(dataCount3);
				  printf("��Ϫ��ۦ��׬� %0.2f %%\n",likeness);
			  }
          }

        
		}


      }
      else
      {
		  lion();
        cmp_txt_fail=1;
        if (arg_num>=1)
		{
          printf("\nIllegal parameter, please input again.\n");
		}

	  printf("Usage: \n\
lions [text_file1] [text_file2] || [-mice] \n\
Description: \n\
Compare two text files. \n\
Options: \n\
Text image file 1\n\
Text image file 2\n\
-mice : show message or not.\n\
Reference command:\n\
lions a.txt b.txt -mice\n\
Compare text file a.txt with b.txt, message is also shown.\n\
");

      }

	  //printf("The command is accomplished.\n");
  }


  else if ( strcmp(cmd_name, "test") == 0 || strcmp(cmd_name, "t") == 0 )
  //���հ϶�
  {
	  int aaa=10;
	  int bbb;
	  int ccc;
	  int ddd;
	  bbb=aaa*8;
	  ccc=aaa<<3;		//�]�O�K�����N�� sll	����3�줸
	  ddd=aaa>>1;		//���H�G
	  printf("bbb=%d\tccc=%d\n",bbb,ccc);	//result: bbb=80  ccc=80

	  printf("bbb=%x\tccc=%x\n",bbb,ccc);	//result: bbb=80  ccc=80
	  printf("ddd=%d\n",ddd);


	srand( (unsigned)time( NULL ) );	//����random�ݥ[
	
	int rrr;

	for(int i=0;i<100;i++)
	{
		rrr=rand()%2;
		printf("Got: %d\t",rrr);
		if (i%8==7)
			printf("\n");
	}


	printf("aaa/3=%d\n",aaa/3);

	

	float abc,abcd;
	aaa=10;
	abc=(float)aaa/3;
	printf("abc=%f\n",abc);
	abcd=floor(abc);
	printf("abcd=%d\n",abcd);

	int pp1,pp2;
	pp1=5;
	pp2=pow(2,pp1);
	printf("pp2=%d\n",pp2);

	pp2=sqrt(pp1);

	printf("\n\npp2=%d\n",pp2);
   
	int vmem=15;
	vmem=vmem/8*8;
	printf("now vmem=%d\n",vmem);

	int AAA[10]={0,1,2,3,4,5,6,7,8,9};

	/*
	cout << " �ʺA�O����t�m���� " << "\n\n";
	int num;
	int sum=0;
	int* pT;
	cout << "�п�J�Ӽ�"  <<"\n" ;
	cin >> num;
	pT=new int[num];
	for(i=0;i<num;i++)
	{
		pT[i]=AAA[i];
		//scanf("Input %d score\n",&pT[i]);
		sum+=pT[i];
	}
	printf("�M��%d\n",sum);
	delete[] pT;
*/

	float AAAA=100;
	AAAA=AAAA/3;
	printf("AAAA=%f\n",AAAA);



	//ABCD�t0123	//for deblock test
	int A,B,C,D;
	A=100,B=100,C=100,D=100;
	printf("A=%d\tB=%d\tC=%d\tD=%d\n",A,B,C,D);

	A=rand()%4;
	B=rand()%4;
	printf("A=%d\tB=%d\tC=%d\tD=%d\n",A,B,C,D);
    while(B==A)
		B=rand()%4;
	C=rand()%4;
    while(C==A || C==B)
		C=rand()%4;
	D=rand()%4;
    while(D==A || D==B || D==C)
		D=rand()%4;
	printf("A=%d\tB=%d\tC=%d\tD=%d\n",A,B,C,D);


	//�Ϋ��жǰѼƴ���

	int num1,num2,sum;
	num1=5;num2=10;sum=3;
	printf("num1=%d\tnum2=%d\tsum=%d\n",num1,num2,sum);
	swap(&num1,&num2,&sum);
	printf("num1=%d\tnum2=%d\tsum=%d\n",num1,num2,sum);

	//enum ����
  enum
  {
    VERFILT = 20,
	HORFILT,
	DECIMATE,
	HORDEC
  };
printf("VERFILT=%d\n",VERFILT);
printf("HORFILT=%d\n",HORFILT);
printf("DECIMATE=%d\n",DECIMATE);



int BA0,BA1,BA2,BA3,OA0,OA1,OA2,OA3;
int n,m,N,M;
int vmem_size;
int block_factor_A,block_factor_B,block_factor_C;
int VM_ADDR;
int BA_A,BA_B,BA_C;
int hor_OA_A,hor_OA_B,hor_OA_C,ver_OA_A,ver_OA_B,ver_OA_C;
vmem_size=1024;
VM_ADDR=0;
block_factor_A=0;
block_factor_B=1;
block_factor_C=2;

BA_A=VM_ADDR*8+(vmem_size/3)/8*8*block_factor_A;
BA_B=VM_ADDR*8+(vmem_size/3)/8*8*block_factor_B;
BA_C=VM_ADDR*8+(vmem_size/3)/8*8*block_factor_C;

hor_OA_A
hor_OA_B
hor_OA_C
ver_OA_A
ver_OA_B
ver_OA_C

�w���n��W_AXH_A�j�p
�htime_W_A=W_A/8;time_H_A=H_A;

spz blockA��32X3 => W 4���AH 3���A�@12���A��12���I
spz blockA��WXH => time_W_A = W_A/8 ���Atime_H_A = H_A ���A�@time_W_A*time_H_A���A��time_W_A*time_H_A���I

block_A�Ψ�
A00=BA_A+ver_OA_A*0+hor_OA_A*0
A01=BA_A+ver_OA_A*0+hor_OA_A*1
A02=BA_A+ver_OA_A*0+hor_OA_A*2
A03=BA_A+ver_OA_A*0+hor_OA_A*3
		:
	BA_A+ver_OA_A*0+hor_OA_A*(time_W_A-1)

A04=BA_A+ver_OA_A*1+hor_OA_A*0
A05=BA_A+ver_OA_A*1+hor_OA_A*1
A06=BA_A+ver_OA_A*1+hor_OA_A*2
A07=BA_A+ver_OA_A*1+hor_OA_A*3
		:
BA_A+ver_OA_A*0+hor_OA_A*(time_W_A-1)


A08=BA_A+ver_OA_A*2+hor_OA_A*0
A09=BA_A+ver_OA_A*2+hor_OA_A*1
A10=BA_A+ver_OA_A*2+hor_OA_A*2
A11=BA_A+ver_OA_A*2+hor_OA_A*3
		:
BA_A+ver_OA_A*2+hor_OA_A*(time_W_A-1)

		:
		:

BA_A+ver_OA_A*(time_H_A-1)+hor_OA_A*(time_W_A-1)		//last

spz blockB��32X2 => W 4���AH 2���A�@8���A��8���I
block_B�Ψ�
B00=BA_B+ver_OA_B*0+hor_OA_B*0
B01=BA_B+ver_OA_B*0+hor_OA_B*1
B02=BA_B+ver_OA_B*0+hor_OA_B*2
B03=BA_B+ver_OA_B*0+hor_OA_B*3
B04=BA_B+ver_OA_B*1+hor_OA_B*0
B05=BA_B+ver_OA_B*1+hor_OA_B*1
B06=BA_B+ver_OA_B*1+hor_OA_B*2
B07=BA_B+ver_OA_B*1+hor_OA_B*3
�T�{�o12<->8���I�Ҥ��ۦP�A


�w���n��W_BXH_B�j�p
�htime_W_B=W_B/8;time_H_B=H_B;

spz blockB��32X2 => W 4���AH 2���A�@8���A��8���I
spz blockB��WXH => time_W_B = W_B/8 ���Atime_H_B = H_B ���A�@time_W_B*time_H_B���A��time_W_B*time_H_B���I

block_B�Ψ�
B00=BA_B+ver_OA_B*0+hor_OA_B*0
B01=BA_B+ver_OA_B*0+hor_OA_B*1
B02=BA_B+ver_OA_B*0+hor_OA_B*2
B03=BA_B+ver_OA_B*0+hor_OA_B*3
		:
	BA_B+ver_OA_B*0+hor_OA_B*(time_W_B-1)

B04=BA_B+ver_OA_B*1+hor_OA_B*0
B05=BA_B+ver_OA_B*1+hor_OA_B*1
B06=BA_B+ver_OA_B*1+hor_OA_B*2
B07=BA_B+ver_OA_B*1+hor_OA_B*3
		:
BA_B+ver_OA_B*0+hor_OA_B*(time_W_B-1)

BA_B+ver_OA_B*(time_H_B-1)+hor_OA_B*(time_W_B-1)		//last



//compare test

int array_A[]={1, 2, 3, 4, 5};
int array_B[]={6, 7, 8, 9, 10, 11, 12};
int hit;
int number_array_A;
int number_array_B;

number_array_A=sizeof(array_A)/4;
number_array_B=sizeof(array_B)/4;

hit= compare_array(&number_array_A,&number_array_B,array_A, array_B);

if(hit)
printf("����\n");
else
printf("�S����\n");


}

/*
double avg(int* pT)
{
    printf("\nindex\tvalue\taddress\n");
    for(int i=0;i<5;i++)
    {
        printf("%d\t%d\t%x\n",i,*(pT+i),pT+i);
    }
    //printf("size of t[] is %d\n",sizeof(t));
    cout << '\n';
    double sum=0;
    for(i=0;i<5;i++)
    {
        //sum+= *(pT+i);
        sum+= pT[i];
    }
    return sum/5;
}
*/



  else if ( strcmp(cmd_name, "hw") == 0 || strcmp(cmd_name, "h") == 0 )
  //HW test
  {
	  int pic_W=256;
	  int pic_H=16;
	  int w,h,N;
	  printf("�Ϥ��j�p���G%d X %d\n",pic_W,pic_H);

	  N=1;w=4,h=1;
	  for(w=1;w<=(pic_W/8);w++)
//	  for(w=1;w<=4;w++)
		  for(h=1;h<=(32/w);h++)
		  {
//			  printf("���ɭn��WXH=%dX%d\n",w*8,h*8);

			  printf("\t//W=%d,H=%d\n",w*8,h*8);
			  printf("\tli\tHW,((%d-1)<<10|(%d-1))\n",h*8,w*8);
			  printf("\tDO_STATISTICS\n");
			  if(h*8*w*8>2048)
				  printf("���i�H�I\n");
			  N++;
		  }

		  printf("totally %d cases.\n",N);
  }

  else if ( strcmp(cmd_name, "blkdc") == 0 || strcmp(cmd_name, "b") == 0 )
  //HW test
  {
      #define Max 1024
	  int w,h,W,H,N;
	  N=1;
	  for(w=3;w<=10;w++)
		  for(h=0;h<=6;h++)
		  {
			  W=pow(2,w);
			  H=pow(2,h);
			  if (W*H<=Max)
			  {
			  //printf("���ɭn��WXH=%dX%d\n",W,H);

			  //printf("\t//W=%d,H=%d\n",W,H);
				  printf("N=%d\t",N);

			  printf("\tli\tHW,((%d-1)<<10|(%d-1));\tDO_BLKDC\n",H,W);
			  //printf("\tDO_STATISTICS\n");
			  N++;
			  }
			  else if(W*H>Max)
			  {
				  printf("���i�H�I\n");
			  }
			  
		  }
		  printf("totally %d cases.\n",N);
  }

  else if ( strcmp(cmd_name, "horint2") == 0 || strcmp(cmd_name, "hor") == 0 )
  //HW test
  {
      #define Max 1024
	  int W,H,N;
	  N=0;
	  for(W=8;W<=1024;W+=43)
		  for(H=1;H<=64;H++)
		  {
			  if (W*H<=Max)
			  {
			  //printf("���ɭn��WXH=%dX%d\n",W,H);

			  //printf("\t//W=%d,H=%d\n",W,H);
			  printf("\tli\tHW,((%d-1)<<10|(%d-1));\tHORINT2\tHW\n",H,W);
			  //printf("\tDO_STATISTICS\n");
			  N++;
			  }
			  else if(W*H>Max)
			  {
				  //printf("���i�H�I\n");
			  }
			  
		  }
		  printf("totally %d cases.\n",N);
  }

else if ( strcmp(cmd_name, "pic") == 0 || strcmp(cmd_name, "yuv") == 0 )
  {

#define  FILENAME "horfilt0.y"
	  
	  for(int i=0;i<256;i++)
	  {
		  printf("%3d%4X\n",i,i);
	  }
  }

  else if ( strcmp(cmd_name, "hexdec") == 0 || strcmp(cmd_name, "dechex") == 0 )
  {
	  for(int i=0;i<256;i++)
	  {
		  printf("%3d%4X\n",i,i);
	  }
  }


  // quit ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "quit") == 0 || strcmp(cmd_name, "exit") == 0 || strcmp(cmd_name, "q") == 0 || strcmp(cmd_name, "0") == 0)
  {
      printf("See you next time. Bye~\n\n");
      return StopProg;
  }
  
  else if ( strcmp(cmd_name, "\0") == 0 )   //��Enter => �S�Ƶo�͡A�G����Ƥ]�S���C
  {
  }

  else if ( strcmp(cmd_name, "cat") == 0 )
  {
      char cmd_line2[40];
      strcpy(cmd_line2,"type ");
      strcat(cmd_line2,cmd_arg[0]);
      system(cmd_line2);
  }

  else if ( strcmp(cmd_name, "ll") == 0 || strcmp(cmd_name, "ls") == 0 )
  {
      system("dir");
  }

  //���P�򩳪��ഫ
  //�Q���i����Q�i��
  else if ( strcmp(cmd_name, "hex2dec") == 0 || strcmp(cmd_name, "h2d") == 0 )
  {
      if (arg_num == 1)
      {
          int convert_val;
          convert_val = hex2dec(cmd_arg[0]);
          printf("%s  hex2dec =>   %d\n",cmd_arg[0],convert_val);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("hex2dec fff111\n");
      }
  }

  //�G�i����Q�i��
  else if ( strcmp(cmd_name, "bin2dec") == 0 || strcmp(cmd_name, "b2d") == 0 )
  {
      if (arg_num == 1)
      {
          int convert_val;
          convert_val = bin2dec(cmd_arg[0]);
          printf("%s  bin2dec =>   %d\n",cmd_arg[0],convert_val);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("bin2dec 11111111\n");
      }
  }

  //�Q�i����G�i��
  else if ( strcmp(cmd_name, "dec2bin") == 0 || strcmp(cmd_name, "d2b") == 0 )
  {
      if (arg_num == 1)
      {
		  int n=0;
		  int Q,R;
		  int result[100];
		  Q=atoi(cmd_arg[0]);
		  while(Q>0)
		  {
			  R=Q%2;
			  result[n]=R;
			  Q=Q/2;
			  n++;
		  }
		  printf("%s  dec2bin => ",cmd_arg[0]);
		  for(int i=n-1;i>=0;i--)
		  {
			  printf("%d",result[i]);
			  if (i%4==0 && i/4!=0)
				  printf("_");
		  }
		  printf("\t�@ %d �줸\n",n);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("dec2bin 63\n");
      }
  }

  //�Q���i����G�i��
  else if ( strcmp(cmd_name, "hex2bin") == 0 || strcmp(cmd_name, "h2b") == 0 )
  {
      if (arg_num == 1)
      {
          int convert_val_d;
          convert_val_d = hex2dec(cmd_arg[0]);

		  int n=0;
		  int Q,R;
		  int result[100];
		  Q=convert_val_d;
		  while(Q>0)
		  {
			  R=Q%2;
			  result[n]=R;
			  Q=Q/2;
			  n++;
		  }
		  printf("%s  hex2bin => ",cmd_arg[0]);
		  for(int i=n-1;i>=0;i--)
		  {
			  printf("%d",result[i]);
			  if (i%4==0 && i/4!=0)
				  printf("_");
		  }
		  printf("\t�@ %d �줸\n",n);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("hex2bin fff111\n");
      }
  }

  //�Q�i����Q���i��
  else if ( strcmp(cmd_name, "dec2hex") == 0 || strcmp(cmd_name, "d2h") == 0)
  {
      if (arg_num == 1)
      {
          printf("%s  dec2hex =>   0x%x\n",cmd_arg[0],atoi(cmd_arg[0]));
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("dec2hex 123456\n");
      }
  }

  //�G�i����Q���i��
  else if ( strcmp(cmd_name, "bin2hex") == 0 || strcmp(cmd_name, "b2h") == 0 )
  {
      if (arg_num == 1)
      {
          int convert_val;
          convert_val = bin2dec(cmd_arg[0]);
		  printf("�ন�Q�i��ɪ��Ȭ��G%d\n",convert_val);
          printf("%s  bin2hex =>   0x%x\n",cmd_arg[0],convert_val);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("bin2hex 11111111\n");
      }
  }

  else if ( strcmp(cmd_name, "str2num") == 0 )
  {
      if (arg_num == 1)
      {
          int convert_val;
          convert_val = str2num(cmd_arg[0]);
          printf("%s  str2num =>   %d\n",cmd_arg[0],convert_val);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("str2num 111111\n");
      }
  }

  else if ( strcmp(cmd_name, "sin") == 0 )
  {
      if (arg_num == 2 && strcmp(cmd_arg[0], "-r") == 0 )
      {
          printf("sin %s  =>   %f\n",cmd_arg[1],sin(atof(cmd_arg[1])));
          //default �� radius �A �����ഫ
      }
      else if (arg_num == 2 && strcmp(cmd_arg[0], "-d") == 0 )
      {
          long double R;
          R=atof(cmd_arg[1])*pi/180;
          printf("sin %s  =>   %f\n",cmd_arg[1],sin(R));
      }
      else if (arg_num == 1 )
      {
          long double R;
          R=atof(cmd_arg[0])*pi/180;
          printf("sin %s  =>   %f\n",cmd_arg[0],sin(R));
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("sin -r 1.7\n");
          printf("sin -d 30\n");
          printf("sin 30    // default unit is degree.\n");
      }
  }

  else if ( strcmp(cmd_name, "cos") == 0 )
  {
      if (arg_num == 2 && strcmp(cmd_arg[0], "-r") == 0 )
      {
          printf("cos %s  =>   %f\n",cmd_arg[1],cos(atof(cmd_arg[1])));
          //default �� radius �A �����ഫ
      }
      else if (arg_num == 2 && strcmp(cmd_arg[0], "-d") == 0 )
      {
          long double R;
          R=atof(cmd_arg[1])*pi/180;
          printf("cos %s  =>   %f\n",cmd_arg[1],cos(R));
      }
      else if (arg_num == 1 )
      {
          long double R;
          R=atof(cmd_arg[0])*pi/180;
          printf("cos %s  =>   %f\n",cmd_arg[0],cos(R));
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("cos -r 1.7\n");
          printf("cos -d 30\n");
          printf("cos 60    // default unit is degree.\n");
      }
  }

  else if ( strcmp(cmd_name, "pow") == 0 )
  {
      if (arg_num == 2)
      {
          long double result;
          printf("op1=%f\top2=%f\n",atof(cmd_arg[0]),atof(cmd_arg[1]));
          result = pow(atoi(cmd_arg[0]),atoi(cmd_arg[1]));
          printf("%s  ^  %s  =>   %f\n",cmd_arg[0],cmd_arg[1],result);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("pow 2 6\n");
      }
  }

  else if ( strcmp(cmd_name, "add") == 0 || strcmp(cmd_name, "a") == 0 || strcmp(cmd_name, "+") == 0)
  {
      if (arg_num == 2)
          printf("%s  +  %s  =>   %f\n",cmd_arg[0],cmd_arg[1],atof(cmd_arg[0])+atof(cmd_arg[1]));
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("add 600 800\n");
      }
  }

  else if ( strcmp(cmd_name, "sub") == 0 || strcmp(cmd_name, "s") == 0 || strcmp(cmd_name, "-") == 0)
  {
      if (arg_num == 2)
          printf("%s  -  %s  =>   %f\n",cmd_arg[0],cmd_arg[1],atof(cmd_arg[0])-atof(cmd_arg[1]));
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("sub 600 800\n");
      }
  }

  else if ( strcmp(cmd_name, "mul") == 0 || strcmp(cmd_name, "m") == 0 || strcmp(cmd_name, "*") == 0)
  {
      if (arg_num == 2)
          printf("%s  *  %s  =>   %f\n",cmd_arg[0],cmd_arg[1],atof(cmd_arg[0])*atof(cmd_arg[1]));
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("mul 600 800\n");
      }
  }

  else if ( strcmp(cmd_name, "div") == 0 || strcmp(cmd_name, "d") == 0  || strcmp(cmd_name, "/") == 0)
  {
      if (arg_num == 2)
          printf("%s  /  %s  =>   %f\n",cmd_arg[0],cmd_arg[1],atof(cmd_arg[0])/atof(cmd_arg[1]));
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("div 600 800\n");
      }
  }

  // for checking ////////////////////////////////////////////////////////////////
  else      //for others input commands
  {
      system(cmd_line);
  }
  return 0;
}

long double OPERATION(char oprtr,long double oprnd1,long double oprnd2,long double& result)
{
    printf("op1=%f,\top2=%f\n",oprnd1,oprnd2);
    if (oprtr=='+')
    {
        //printf("Perform ADD operation.\n");
        result=oprnd1+oprnd2;
    }
    else if (oprtr=='-')
    {
        //printf("Perform SUB operation.\n");
        result=oprnd1-oprnd2;
    }
    else if (oprtr=='*')
    {
        //printf("Perform MUL operation.\n");
        result=oprnd1*oprnd2;
    }
    else if (oprtr=='/')
    {
        //printf("Perform DIV operation.\n");
        result=oprnd1/oprnd2;
    }
    else
    {
        //printf("No proper operation.\n");
        return -1;
    }
    return result;
}

long double pow(int t1,int t2)  //��t1��t2����
{
    long double ddd=1;
    if (t2 ==0)
        return ddd;
    else if (t2 > 0)
    {
        for (int i=0;i<t2;i++)
            ddd*=t1;
        return ddd;
    }
    else
    {
        for (int i=0;i<-t2;i++)
            ddd*=t1;
        return 1/ddd;
    }

}

double avg(int* pT)
{
    printf("\nindex\tvalue\taddress\n");
    for(int i=0;i<5;i++)
    {
        printf("%d\t%d\t%x\n",i,*(pT+i),pT+i);
    }
    //printf("size of t[] is %d\n",sizeof(t));
    cout << '\n';
    double sum=0;
    for(i=0;i<5;i++)
    {
        //sum+= *(pT+i);
        sum+= pT[i];
    }
    return sum/5;
}

int bin2dec(char* bbb)
{
    int ddd=0;
    printf("��J���`�줸�Ƭ� %d\n",strlen(bbb));
    for (int i=0;i<strlen(bbb);i++)
    {
        ddd+=(bbb[i]-48)*pow(2,(strlen(bbb)-i-1));
    }
    return ddd;
}

int str2num(char* sss)
{
    int nnn=0;
    if (strncmp(sss,"0x",2)==0)
        nnn=hex2dec(sss);
    else
        nnn=atoi(sss);
    return nnn;
}

int hex2dec(char* hhh)  //�u�䴩��FFF_FFFF (7��F)
{
    int val;
    int result=0;
    int length=strlen(hhh);
    for (int i=0;i<length;i++)
    {
        switch(hhh[i])
        {
        case '0':
        case 'x':
        case 'X':
            val=0;
            break;
        case '1':
            val=1;
            break;
        case '2':
            val=2;
            break;
        case '3':
            val=3;
            break;
        case '4':
            val=4;
            break;
        case '5':
            val=5;
            break;
        case '6':
            val=6;
            break;
        case '7':
            val=7;
            break;
        case '8':
            val=8;
            break;
        case '9':
            val=9;
            break;
        case 'a':
        case 'A':
            val=10;
            break;
        case 'b':
        case 'B':
            val=11;
            break;
        case 'c':
        case 'C':
            val=12;
            break;
        case 'd':
        case 'D':
            val=13;
            break;
        case 'e':
        case 'E':
            val=14;
            break;
        case 'f':
        case 'F':
            val=15;
            break;
        default:
            return -1;
        }
        result += val*pow(16,length-i-1);
    }
    return result;
}

void lion()
  {
	  printf("\n");
	  printf("  L             IIIIIIIII         O        NNN       NNN\n");
	  printf("  L                 I           O   O       N N       N\n");
	  printf("  L                 I         O       O     N   N     N\n");
	  printf("  L                 I        O         O    N    N    N\n");
	  printf("  L                 I        O         O    N     N   N\n");
	  printf("  L                 I        O         O    N      N  N\n");
	  printf("  L                 I         O       O     N       N N\n");
	  printf("  L                 I           O   O       N        N\n");
	  printf("  LLLLLLLLLLL   IIIIIIIII         O        NNN       NNN\n");
  }

int findSmall(int n1,int n2)
{
	int result;
	if (n1>n2)
		result=n2;
	else
		result=n1;
	return result;
}

int int_rand(int max)
{
	int tmp;
	tmp = (int) (((float) max) * (rand()/(1.0+RAND_MAX))); 
	return tmp;
}

int range_rand(int min, int max)
{
	int tmp;
	if(min > max){
		tmp = min;
		min = max;
		max = tmp;
	}
	tmp = min + (int_rand(max-min+1));
	return tmp;
}

void swap(int* pA,int* pB,int* sum)
{
	int tmp;
	*sum=*pA+*pB;
	tmp=*pA;
	*pA=*pB;
	*pB=tmp;

}

















/*
�Y����even-odd�ɡA

		// spz : mem_size=8*16=128;  VMA=0
		BA0=VMA*8;
		BA3=BA0+T/2;	//���ä��i��BA3�bBA0���e�A�Υi�洫
		//decide VMEM shape
		VMEM_W=8*range_rand(1,(mem_size/2)/8);
		VMEM_H=(mem_size/2)/VMEM_W;
		//decide operation size
		W=8*range_rand(1,VMEM_W/8);
		H=8*range_rand(1,VMEM_H);
		//number_w=W/8;
		//number_h=H;
		//horizontal pitch 8*range_rand(number_w,VMEM_W/w);
		//vertical pitch     range_rand(number_h,VMEM_H/h);
		if (W==8)
			OA0=  8*range_rand(1,VMEM_W/8);
		else
			OA0=     8*range_rand(1,(VMEM_W/8-1)/(W/8-1));
		//OA1=VMEM_W;
		if (H==1)
			OA1=VMEM_W*range_rand(1,VMEM_H);
		else
			OA1=VMEM_W*range_rand(1,(VMEM_H  -1)/(H  -1));



  */


int compare_array(int* number_array_A,int* number_array_B,int* array_A, int* array_B)
{
	int i,j;
	int break_flag=0;
	for(i=0;i<*number_array_A;i++)
	{
		for(j=0;j<*number_array_B;j++)
		{
			//printf("Compare array_A[%d]=%d with array_B[%d]=%d\n",i,array_A[i],j,array_B[j]);
			if(array_A[i]==array_B[j])
			{
				break_flag=1;
				return 1;
				break;
			}
		}
		if(break_flag)
			break;
	}
	return 0;
}
