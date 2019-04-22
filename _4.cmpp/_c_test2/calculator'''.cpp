#include <iostream>
#include "math.h"
#include <fstream>
#include <time.h>
#include <windows.h>
#define StopProg 1
#define colorHeavy 30	//深色
#define colorLight 100	//淺色
#define add +
using namespace std;
typedef unsigned long ULONG;
typedef unsigned char BYTE;

void lion();
int findSmall(int n1,int n2);

long double pow(int t1,int t2); //算t1的t2次方
int bin2dec(char* bbb);
int hex2dec(char* hhh);  //只支援到FFF_FFFF (7個F)
int str2num(char* sss);
long double OPERATION(char oprtr,long double oprnd1,long double oprnd2,long double& result);
int tb_debug_kernel(char* cmd_line);
double avg(int* pT);
const long double pi = 3.14159265358979;


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
        cmd_str_ptr ++;			//當讀到空白或tab時，找到csp的位置
    j = 0;
    while((cmd_line[cmd_str_ptr]!=' ' && cmd_line[cmd_str_ptr]!='\t') && cmd_line[cmd_str_ptr]!='\0' && cmd_line[cmd_str_ptr]!='\n' && cmd_str_ptr<120)  
        cmd_name[j++] = cmd_line[cmd_str_ptr++];    //get first command name //把第一個字串讀進cmd_name
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
    
  // 開始各項功能 ///////////////////////////////////////////////////////

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
    printf("hex2dec aaaa\t\t十六進位  轉    十進位\n");
    printf("hex2bin aaaa\t\t十六進位  轉    二進位\n");
    printf("dec2hex 4096\t\t  十進位  轉  十六進位\n");
    printf("dec2bin 4096\t\t  十進位  轉    二進位\n");
    printf("bin2hex 11111111\t  二進位  轉  十六進位\n");
    printf("bin2dec 11111111\t  二進位  轉    十進位\n");
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
      //printf("\nCalculator 2004  [版本 0.9.0] [ Oct 13, 2004 星期三 ]\n");
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
	  char mytext[]={"師叔你好啊！！"};
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
                      //printf("now 整數部分為 %f\n",oprnd[oprnd_num]);
                  }
                  for (k=0;k<(length-idx-1);k++)
                  {
                      decimal+=(cmd_name[length-idx+k+1]-48)*pow(10,-1-k);
                      //printf("now 小數部分為 %f\n",decimal);
                  }
                  //decimal=decimal/pow(10,i-idx-1);
                  //printf("整數=%f\t小數=%f\n",oprnd[oprnd_num],decimal);
                  oprnd[oprnd_num]=oprnd[oprnd_num]+decimal;
                  //printf("全部%f\n",oprnd[oprnd_num]);
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
              //printf("此時在%d位置。\n",k+i-length);

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
              //printf("now 整數部分為 %f\n",oprnd[oprnd_num]);
          }
          for (k=0;k<(length-idx-1);k++)
          {
              decimal+=(cmd_name[length-idx+k+1]-48)*pow(10,-1-k);
              //printf("now 小數部分為 %f\n",decimal);
          }
          //decimal=decimal/pow(10,i-idx-1);
          //printf("整數=%f\t小數=%f\n",oprnd[oprnd_num],decimal);
          oprnd[oprnd_num]=oprnd[oprnd_num]+decimal;
          //printf("全部%f\n",oprnd[oprnd_num]);
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
	  const ULONG BufferSize=1500;      //檔案裡總共多少個byte，需改大
	  char mem_read[BufferSize][20];    //每個字串最大容量
	  int dataCount1=0;      //有效的data總數
	  int nonhex=0;
	  ifstream fin("l1.txt");
	  if(!fin)
		  {
			  printf("檔案l1.txt找不到，你是不是放錯地方了\n");
			  printf("The command is NOT accomplished.\n");
			  cmpfiles_fail=1;
		  }
		  else
		  {
			  //printf("檔案 %s 已開啟\n",cmd_arg_file_t_1);
			  printf("檔案 l1.txt 已開啟\n");
			  while(!fin.eof())//當還沒有讀到檔尾時
			  {
				  fin >> mem_read[dataCount1];
				  printf("此時的mem_read[%2d]為：%s\n",dataCount1,mem_read[dataCount1]);
				  //printf("mem_read[%d]=%s\teof=%d\tlength=%d\n",dataCount1,mem_read[dataCount1],fin.eof(),strlen(mem_read[dataCount1]));
				  mem_read[dataCount1][strlen(mem_read[dataCount1])]='\0';
				  dataCount1++;
				  cout << "\n";

			  }
		  }

  }

  // 比較兩個檔案是否一樣
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
          printf("此時arg_num_i=%d\n",arg_num_i);
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
		  BYTE  *data1;                      //buffer大小
		  BYTE  *data2;                      //buffer大小
		  BYTE  *data3;                      //buffer大小
		  data1 = new BYTE[cmd_arg_width*cmd_arg_height];
		  data2 = new BYTE[cmd_arg_width*cmd_arg_height];
		  data3 = new BYTE[cmd_arg_width*cmd_arg_height];
          image_file1 = fopen(cmd_arg_file_b_1, "rb");
          if(!image_file1)
          {
              printf("檔案 %s 找不到，你是不是放錯地方了？！\n",cmd_arg_file_b_1);
              printf("The command is NOT accomplished.\n");
              cmpfiles_fail=1;
          }
		  else
          {
              int i=0;
			  
              while(i<cmd_arg_width*cmd_arg_height)
                  data1[i++] = fgetc(image_file1);
			  //printf("檔案 %s 共有 %d 個點\n",cmd_arg_file_b_1,i);
			  int j=0;
			  fclose(image_file1);
		  }
		  if (!cmpfiles_fail)
		  {
			  FILE  *image_file2;
			  image_file2 = fopen(cmd_arg_file_b_2, "rb");
			  if(!image_file2)
			  {
				  printf("檔案 %s 找不到，你是不是放錯地方了？！\n",cmd_arg_file_b_2);
				  printf("The command is NOT accomplished.\n");
				  cmpfiles_fail=1;
			  }
			  else
			  {
				  int j=0;
				  while(j<cmd_arg_width*cmd_arg_height)
					  data2[j++] = fgetc(image_file2);
				  //printf("檔案 %s 共有 %d 個點\n",cmd_arg_file_b_2,j);
				  fclose(image_file2);
			  }
		  }
		  if(!cmpfiles_fail)
		  {
			  int k=0;
			  int mismatch=0;
			  printf("比較兩個檔案的前 %d 個點\n",cmd_arg_width*cmd_arg_height);
			  while(k<cmd_arg_width*cmd_arg_height)
			  {
//				  data3[k]=data2[k]-data1[k];
				  //00全黑	FF全白
				  if (data1[k]!=data2[k])
				  {
					  if (showMesg)
					  {
						  printf("在 %3d 點找到不同值\t",k);
						  printf("檔案1為%2x 檔案2為%2x\n",data1[k],data2[k]);
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
					  //上
					  for (int i=0;i<cmd_arg_width;i++)
					  {
						  if(!(i%2))
							  data3[i]=colorHeavy;
						  else
							  data3[i]=colorLight;
					  }
					  //下
					  for (i=cmd_arg_width*cmd_arg_height-cmd_arg_width;i<cmd_arg_width*cmd_arg_height;i++)
					  {
						  if((i+cmd_arg_height)%2)
							  data3[i]=colorHeavy;
						  else
							  data3[i]=colorLight;
					  }
					  //左右
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
				  printf("且共有%d個不同點\n",mismatch);
				  float likeness;
				  likeness=100*(cmd_arg_width*cmd_arg_height-mismatch);
				  likeness=likeness/(cmd_arg_width*cmd_arg_height);
				  printf("兩圖的相似度為 %0.2f %%\n",likeness);
				  printf("已經把兩圖的相差存在檔案difference.yuv裏了。\n");
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
  
  // 加料
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
          printf("此時arg_num_i=%d\n",arg_num_i);
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
		  BYTE  *data1;                      //buffer大小
		  BYTE  *data2;                      //buffer大小
		  data1 = new BYTE[cmd_arg_width*cmd_arg_height];
		  data2 = new BYTE[cmd_arg_width*cmd_arg_height];
          image_file1 = fopen(cmd_arg_file_b_1, "rb");
		  image_file2 = fopen(cmd_arg_file_b_2, "wb");
          printf("影像增強量 %d \n",cmd_arg_quantity);
		  if(!image_file1)
          {
              printf("檔案 %s 找不到，你是不是放錯地方了？！\n",cmd_arg_file_b_1);
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
			  printf("檔案 %s 共有 %d 個點\n",cmd_arg_file_b_1,i);
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


  // 殺去彩色，留下黑白
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
          printf("此時arg_num_i=%d\n",arg_num_i);
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
		  BYTE  *data;                      //buffer大小，圖形過大可能會不能處理，應分段處理
		  data = new BYTE[cmd_arg_width*cmd_arg_height*1.5];
		  image_file1 = fopen(cmd_arg_file_b_1, "rb");
		  image_file2 = fopen(cmd_arg_file_b_2, "wb");
		  if(!image_file1)
          {
              printf("檔案 %s 找不到，你是不是放錯地方了？！\n",cmd_arg_file_b_1);
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
把彩色圖片p1.yuv 中的黑白部分抽出來存成 p2.yuv.\n\
");
	  }
	  else
	  {
		  printf("The command is accomplished.\n");
	  }
  }

  // 獨留第N張(存成黑白照)
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
      int  idx=10;	//要抓的第N張(N不能太大)

		  FILE  *image_file1;
		  FILE  *image_file2;
		  BYTE  *data;                      //buffer大小，圖形過大可能會不能處理，應分段處理
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
	  const ULONG BufferSize=21480;      //檔案裡總共多少個byte，需改大
	  char mem_read_1[BufferSize][20];    //每個字串最大容量
	  char mem_read_2[BufferSize][20];    //每個字串最大容量
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
          int dataCount1=0;      //有效的data總數
          int dataCount2=0;      //有效的data總數
          int writemem;
          int nonbin=0;
          int nonhex=0;
          int i;
          int binorhex=1;   //預設資料都是hex的
          int BitNum=8;

          while(!fin1.eof())//當還沒有讀到檔尾時
          {
			  fin1 >> mem_read_1[dataCount1];
            //cout << "此時的dataCount1為：" << dataCount1 << '\n';
            //printf("mem_read_1[%d]=%s\teof=%d\tlength=%d\n",dataCount1,mem_read_1[dataCount1],fin1.eof(),strlen(mem_read_1[dataCount1]));
            mem_read_1[dataCount1][strlen(mem_read_1[dataCount1])]='\0';
            nonbin=0;
            nonhex=0;
            writemem=0;
            //開始分析所讀到的每一字串的資料
            if (strcmp(mem_read_1[dataCount1],"%bin%") == 0 || strcmp(mem_read_1[dataCount1],"//%bin%") == 0)
            {
              binorhex=0;   //就是選binary
              BitNum=8;
              //printf("Data type is changed to binary!\n");
              continue;
            }
            else if (strcmp(mem_read_1[dataCount1],"%hex%") == 0 || strcmp(mem_read_1[dataCount1],"//%hex%") == 0)
            {
              binorhex=1;   //就是選hex
              BitNum=2;
              //printf("Data type is changed to hex!\n");
              continue;
            }
            else if (mem_read_1[dataCount1][0]=='\n' || mem_read_1[dataCount1][0]==';' ||mem_read_1[dataCount1][0]=='/' || mem_read_1[dataCount1][0]=='%')
            {
              continue;     //忽略不計
            }
            //??
            if (mem_read_1[dataCount1][0]=='\n' || mem_read_1[dataCount1][0]==';' ||mem_read_1[dataCount1][0]=='/')
            {
              cout << "此行不算\n";
              continue;     //忽略不計
            }

            if ((writemem ==1 || fin1.eof() ==1) && !cmp_txt_fail)     //寫資料    1.讀到@ 2.讀到EOF
            {
              //cout << "read the end.\n";
              BYTE  *data_file_t_1;     //buffer大小
              data_file_t_1 = new BYTE[dataCount1];
              if (binorhex==1)  //hex時
              {
                for (i=0;i<dataCount1;i++)
                {
                  data_file_t_1[i] = hex2dec(mem_read_1[i]);
                }
              }
			  /*
			  printf("\n檔案%s讀到的資料共%d筆，依序為：\n",cmd_arg_file_t_1,dataCount1);
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
          while(!fin2.eof())//當還沒有讀到檔尾時
          {
			  fin2 >> mem_read_2[dataCount2];
            //cout << "此時的dataCount2為：" << dataCount2 << '\n';
            //printf("mem_read_2[%d]=%s\teof=%d\tlength=%d\n",dataCount2,mem_read_2[dataCount2],fin2.eof(),strlen(mem_read_2[dataCount2]));
            mem_read_2[dataCount2][strlen(mem_read_2[dataCount2])]='\0';
            nonbin=0;
            nonhex=0;
            writemem=0;
            //開始分析所讀到的每一字串的資料
            if (strcmp(mem_read_2[dataCount2],"%bin%") == 0 || strcmp(mem_read_2[dataCount2],"//%bin%") == 0)
            {
              binorhex=0;   //就是選binary
              BitNum=8;
              //printf("Data type is changed to binary!\n");
              continue;
            }
            else if (strcmp(mem_read_2[dataCount2],"%hex%") == 0 || strcmp(mem_read_2[dataCount2],"//%hex%") == 0)
            {
              binorhex=1;   //就是選hex
              BitNum=2;
              //printf("Data type is changed to hex!\n");
              continue;
            }
            else if (mem_read_2[dataCount2][0]=='\n' || mem_read_2[dataCount2][0]==';' ||mem_read_2[dataCount2][0]=='/' || mem_read_2[dataCount2][0]=='%')
            {
              continue;     //忽略不計
            }
            //??
            if (mem_read_2[dataCount2][0]=='\n' || mem_read_2[dataCount2][0]==';' ||mem_read_2[dataCount2][0]=='/')
            {
              cout << "此行不算\n";
              continue;     //忽略不計
            }

            if ((writemem ==1 || fin2.eof() ==1) && !cmp_txt_fail)     //寫資料    1.讀到@ 2.讀到EOF
            {
              //cout << "read the end.\n";
              BYTE  *data_file_t_2;     //buffer大小
              data_file_t_2 = new BYTE[dataCount2];
              if (binorhex==1)  //hex時
              {
                for (i=0;i<dataCount2;i++)
                {
                  data_file_t_2[i] = hex2dec(mem_read_2[i]);
                }
              }

/*			  printf("\n檔案%s讀到的資料共%d筆，依序為：\n",cmd_arg_file_t_2,dataCount2);
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
			  printf("\n檔案%s讀到的資料共%d筆，依序為：\n",cmd_arg_file_t_1,dataCount1);
			  for (i=0;i<dataCount1;i++)
			  {
				  printf("%0s\t",mem_read_1[i]);
			  }                      
			  printf("\n檔案%s讀到的資料共%d筆，依序為：\n",cmd_arg_file_t_2,dataCount2);
			  for (i=0;i<dataCount2;i++)
			  {
				  printf("%0s\t",mem_read_2[i]);
			  }
*/
		      int dataCount3;
			  dataCount3=findSmall(dataCount1,dataCount2);
			  printf("檔案 %s 的個數為 %d\t檔案 %s 的個數為 %d\n",cmd_arg_file_t_1,dataCount1,cmd_arg_file_t_2,dataCount2);
			  if(dataCount1!=dataCount2)
			  {
				  printf("兩個檔案個數就不一樣多了，當然不一樣囉。\n");
				  printf("較小數為%d\n",dataCount3);
			  }
			  else
			  {
				  printf("兩個檔案個數一樣多，各有 %d 個點\n",dataCount3);
			  }

		  if(!cmp_txt_fail)
		  {
			  int k=0;
			  int mismatch=0;
			  printf("比較兩個檔案的前 %d 個點\n",dataCount3);
			  while(k<dataCount3)
			  {
			  if ( strcmp(mem_read_1[k],mem_read_2[k]) != 0 )
				  {
					  if (showMesg)
					  {
						  printf("在 %3d 點找到不同值\t",k);
						  printf("檔案1為%s 檔案2為%s\n",mem_read_1[k],mem_read_2[k]);
					  }
					  mismatch++;
				  }
				  k++;
			  }
			  if (!mismatch)
			  {
				  printf("The two files are the same.\n");
				  printf("兩圖的相似度為 100 %%\n");
			  }
			  else
			  {
				  printf("The two files are NOT the same.\n");
				  printf("且共有%d個不同點\n",mismatch);
				  float likeness;
				  likeness=100*(dataCount3-mismatch);
				  likeness=likeness/(dataCount3);
				  printf("兩圖的相似度為 %0.2f %%\n",likeness);
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




  // quit ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "quit") == 0 || strcmp(cmd_name, "exit") == 0 || strcmp(cmd_name, "q") == 0 || strcmp(cmd_name, "0") == 0)
  {
      printf("See you next time. Bye~\n\n");
      return StopProg;
  }
  
  else if ( strcmp(cmd_name, "\0") == 0 )   //按Enter => 沒事發生，故什麼事也沒做。
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

  //不同基底的轉換
  //十六進位轉十進位
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

  //二進位轉十進位
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

  //十進位轉二進位
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
		  printf("\t共 %d 位元\n",n);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("dec2bin 63\n");
      }
  }

  //十六進位轉二進位
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
		  printf("\t共 %d 位元\n",n);
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          printf("Referecnce command:\n");
          printf("hex2bin fff111\n");
      }
  }

  //十進位轉十六進位
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

  //二進位轉十六進位
  else if ( strcmp(cmd_name, "bin2hex") == 0 || strcmp(cmd_name, "b2h") == 0 )
  {
      if (arg_num == 1)
      {
          int convert_val;
          convert_val = bin2dec(cmd_arg[0]);
		  printf("轉成十進位時的值為：%d\n",convert_val);
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
          //default 為 radius ， 不用轉換
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
          //default 為 radius ， 不用轉換
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

long double pow(int t1,int t2)  //算t1的t2次方
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
    printf("輸入的總位元數為 %d\n",strlen(bbb));
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

int hex2dec(char* hhh)  //只支援到FFF_FFFF (7個F)
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
