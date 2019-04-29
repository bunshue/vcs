#include "systemc.h"
#include "tb_device.h"
#include "module_dc.h"
#include "module_ve.h"
#include "tb_debug_ui.h"

FILE  *script_file;
bool  script_flag;
int  cmdCount;
int  pause=0;

void init_debug_ui()
{
  script_flag = false;
}

int tb_debug_ui(int &cycles)
{
  char            cmd_line[120];
  int             j;
  int             ret_val;
  printf("\nFor help on the debugging interface, enter:  help or ?\n");
  while(1)
  {
      if( script_flag )
      {
          fgets(cmd_line, 120, script_file);
          if( cmd_line[0] == ';' || cmd_line[0] == '\n' || cmd_line[0] == '#' || cmd_line[0] == '%' || strncmp(cmd_line,"//",2)==0)
              j=0;      //�M�wŪ�X�ӨC��O�_�n��
          if( feof(script_file) )
          {
              fclose(script_file);
              script_flag = 0;
          }
          else if( j>0 )
          {
              cmdCount++;
              printf("\nCommand %d : \t%s",cmdCount,cmd_line);
              ret_val = tb_debug_kernel(cmd_line, cycles);
              if (pause)
              {
                  system("pause");                  
              }
          }      
      }
      else
      {   
          printf("\ntb_dvr>");
          gets(cmd_line);
          ret_val = tb_debug_kernel(cmd_line, cycles);
      }
      if( ret_val == TB_DEBUG_STOP )
        return TB_DEBUG_STOP;

      if( ret_val == TB_DEBUG_RUN )
        return TB_DEBUG_RUN;

      for( j=0; j<120; j++)
          cmd_line[j] = 0;
  }
}

int tb_debug_kernel(char* cmd_line, int &cycles)
{
  cycles = 0;

    //**************simulation control***********************
    char            cmd_name[40];
    char            cmd_arg[20][40];
    unsigned int    cmd_str_ptr=0;
    unsigned int    arg_num,j,k; 
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

  // run ////////////////////////////////////////////////////////////////
  if( strcmp(cmd_name, "run") == 0 )
  {
    if( arg_num == 0 )  // this is the case of free run
    {
      cycles = -1;
      return TB_DEBUG_RUN;
    }
    else if( strcmp(cmd_arg[0] , "-c")==0 )
    {
      cycles = atoi(cmd_arg[1]);
      return TB_DEBUG_RUN;
    }
    else
    {
        printf("Illegal parameter, please input again.\n");
        printf("Referecnce command:\n");
        printf("run \t\t\tFree run.\n");
        printf("run -c 1000\t\tRun 1000 cycles.\n");
    }
  }

  // version ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "ver") == 0)
  {
    printf("\nReaktek DVR 2004  [���� 0.9.1] [ Aug 5, 2004 �P���| ]\n"); 
  }

  // time ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "time") == 0)
  {
    cout << "Current time is: " << sc_time_stamp()<< '\n';
  }

  // list ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "list") == 0)
  {
      int list_fail=0;
      if( strcmp(cmd_arg[0],"-n")==0 || strcmp(cmd_arg[0],"-name")==0)    //list all module names
      {
          int i=0;
          printf("All module names:\n");
          printf("deviceCount\tmodule name\n");
          while (i<CDebugImp::m_deviceCount)
          {
              printf("%d\t\t%s\n",i,CDebugImp::m_deviceTable[i]->getName());
              i++;
          }
      }
      else if( strcmp(cmd_arg[0],"-r")==0)    //list all register names
      {
          int i=0;
          printf("All module names:\n");
          printf("regCount\tregisterName\n");
          while (i<IRegBase::m_regCount)
          {
              printf("%d\t\t%s\n",i,IRegBase::m_regTable[i]->m_registerName);
              i++; 
          }
      }
      else
      {
          list_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }
      if(list_fail==1)
      {
          printf("Referecnce command:\n");
          printf("list -n\t\t\tFor listing all module names.\n");
          printf("list -r\t\t\tFor listing all register names.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }
      
  // help ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "help") == 0 || strcmp(cmd_name, "?") == 0 )
  {
    printf("Referecnce command:\n");
    printf("? or help\tFor this help menu\n");
    printf("list -?\t\tFor list function help.\n");
    printf("run -?\t\tFor run function help.\n");
    printf("script -?\tFor script function help.\n");
    printf("read -?\t\tFor read function help.\n");
    printf("write -?\tFor write function help\n");
    printf("load -?\t\tFor load function help.\n");
    printf("loadimg \tFor loadimg function help.\n");
    printf("store -?\tFor store function help.\n");
    printf("storeimg -?\tFor storeimg function help.\n");
    printf("loadprog -?\tFor loadprog function help\n");
    printf("setbreak -?\tFor setbreak function help.\n");
    printf("clrbreak \tFor clrbreak function help.\n");
    printf("setceibreak -?\tFor setceibreak function help.\n");
    printf("clrceibreak \tFor clrceibreak function help.\n");
    printf("quit \t\tLeave the debugging interface.\n");
  }
      
  // read ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "read") == 0)
  {
    int k=0;
    int isfield=0;      //���T�{���L�nŪfield�A�Ycmd_arg[1]�O�_��'.'
    while(k<strlen(cmd_arg[1]))
    {
      if (cmd_arg[1][k]=='.')
        isfield++;
      k++;
    }

    if( strcmp(cmd_arg[0],"-p")==0 && arg_num==3)   //ex: read -p -d ME_
    {
      int i=0; int match=0;
      printf("Register name\tValue(%s)\n",cmd_arg[1]);
      while (i<IRegBase::m_regCount)
      {
        if (strncmp(IRegBase::m_regTable[i]->m_registerName,cmd_arg[2],strlen(cmd_arg[2]))==0)
        {
          if(strcmp(cmd_arg[1],"-d")==0)
            printf("%s\t%d\n",IRegBase::m_regTable[i]->m_registerName,IRegBase::m_regTable[i]->read());
          else if(strcmp(cmd_arg[1],"-h")==0)
            printf("%s\t%x\n",IRegBase::m_regTable[i]->m_registerName,IRegBase::m_regTable[i]->read());
          match++;
        }
        i++;
      }
      if (match==0) //�ݬݬO�_�����W�r�۲Ū�
        printf("No matched register name found\n");
    }
    else if( ( strcmp(cmd_arg[0],"-h")==0 || strcmp(cmd_arg[0],"-d")==0) && arg_num==2 )    //ex: read -d ME_CTRL
    {
      if(isfield==0)      //�Lfield���p�A��J�u��register
      {
        int i=0; int match=0;
        printf("Field name\tValue(%s)\n",cmd_arg[0]);
        while (i<IRegBase::m_regCount)
        {
          if (strcmp(IRegBase::m_regTable[i]->m_registerName,cmd_arg[1])==0)
          {
            if(strcmp(cmd_arg[0],"-d")==0)
              IRegBase::m_regTable[i]->print(false);
            else if(strcmp(cmd_arg[0],"-h")==0)
              IRegBase::m_regTable[i]->print(true);
            else
              printf("Invalid parameter\n");
            match++;
          }
          i++;
        }
        if (match==0)   //�ݬݬO�_�����W�r�۲Ū�
            printf("No matched register name found\n");
      }
      if(isfield!=0)  //��field���p�A��J��field    ex: read -d ME_CTRL.tw
      {
        //1.����cmd_arg[1]����cmd_arg_register��cmd_arg_field
        //2.���O�_����register�A3.�Y���A���O�_����field
        //4.Ū��ơA
        //6.�Y�L��register��field�A�h��ܵL��register��field�C
        char cmd_arg_register[40];
        char cmd_arg_field[40];
        int i=0;
        while(cmd_arg[1][i]!='.')
        {
          cmd_arg_register[i]=cmd_arg[1][i];
          i++;
        }
        cmd_arg_register[i]='\0';
        //cout << "Register :\t" << cmd_arg_register << '\n';
        int j=0;
        i++;
        while(cmd_arg[1][i]!='\0')
        {
          cmd_arg_field[j]=cmd_arg[1][i];
          i++;j++;
        }
        cmd_arg_field[j]='\0';
        //cout << "Field :\t" << cmd_arg_field << '\n';
        i=0;int match=0;
        printf("Field name\tValue(%s)\n",cmd_arg[0]);
        while (i<IRegBase::m_regCount)
        {
          if (strcmp(IRegBase::m_regTable[i]->m_registerName,cmd_arg_register)==0)
          {
            ULONG data;
            if( IRegBase::m_regTable[i]->readField(cmd_arg_field, &data) )
            {
              if( strcmp(cmd_arg[0] , "-d")==0 )
                printf("%s\t%d\n",cmd_arg_field,data);
              else if( strcmp(cmd_arg[0] , "-h")==0 )
                printf("%s\t%x\n",cmd_arg_field,data);
              else
                printf("Invalid parameter\n");
              match++;
            }
          }
          i++;
        }
        if (match==0)   //�ݬݬO�_�����W�r�۲Ū�
          printf("No matched register or field name found, and no data is read.\n");
      }
    }
    else    //read�\��H�~�A��L��J���~�����p
    {
      printf("Referecnce command:\n");
      printf("read -?\t\t\tFor reading help\n");
      printf("read -p -h ME_\t\tRead registers whose name prefixed as ME_\n");
      printf("read -d ME_CTRL\t\tRead the ME_CTRL register in decimal\n");
      printf("read -d ME_CTRL.tw\tRead the register ME_CTRL and field tw in decimal\n");
    }
  }

  // readme ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "readme") == 0)
  {
    cout << "Readme!!\n";
  }
          
  //write ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "write") == 0)
  {
    int k=0;
    int isfield=0;                  //�T�{���L�n�g��field�A�Ycmd_arg[1]�O�_��'.'
    while(k<strlen(cmd_arg[0]))
    {
      if (cmd_arg[0][k]=='.')
        isfield++;
      k++;
    }

    if(arg_num==2 && isfield==0)    //�Lfield���p
    {
      // TBD: write register
      //1.���O�_����register�A2.�Y���A��arg[1]�令�ƭȡA3.�g���
      //4.�Y�L��register�A�h��ܵL��register�C
      int i=0;int match=0;
      while (i<IRegBase::m_regCount)
      {
        if (strcmp(IRegBase::m_regTable[i]->m_registerName,cmd_arg[0])==0)
        {
          IRegBase::m_regTable[i]->write(atoi(cmd_arg[1]));     //�g���
          match++;
        }
        i++;
      }
      if (match==0) //�ݬݬO�_�����W�r�۲Ū�
        printf("No matched register name found, and no data is written.\n");
    }
    else if(arg_num==2 && isfield!=0)  //��field���p
    {
      //1.����cmd_arg[0]����cmd_arg_register��cmd_arg_field
      //2.���O�_����register�A3.�Y���A���O�_����field
      //4.��arg[1]�令�ƭȡA5.�g��ơA
      //6.�Y�L��register��field�A�h��ܵL��register��field�C
      char cmd_arg_register[40];
      char cmd_arg_field[40];
      //cout << "cmd_arg[0] is " << cmd_arg[0] <<'\n';
      int i=0;
      while(cmd_arg[0][i]!='.')
      {
        cmd_arg_register[i]=cmd_arg[0][i];
        i++;
      }
      cmd_arg_register[i]='\0';
      //cout << "Register :\t" << cmd_arg_register << '\n';
      int j=0;
      i++;
      while(cmd_arg[0][i]!='\0')
      {
        cmd_arg_field[j]=cmd_arg[0][i];
        i++;j++;
      }
      cmd_arg_field[j]='\0';
      //cout << "Field :\t\t" << cmd_arg_field << '\n';
      i=0;int match=0;
      while (i<IRegBase::m_regCount)
      {
        if (strcmp(IRegBase::m_regTable[i]->m_registerName,cmd_arg_register)==0)
        {
            ULONG data;
            IRegBase::m_regTable[i]->writeField(cmd_arg_field,atoi(cmd_arg[1]));  //�g���
            IRegBase::m_regTable[i]->readField(cmd_arg_field, &data);   //�A����Ū�X��
            if( data == atoi(cmd_arg[1]))       //���gŪ����ƬO���O�@��
            {
                printf("Write data OK!\n");
            }
            else
            {
                printf("Write data fail!\n");
                printf("Maybe invalid field name or write-value.\n");
                printf("Please write again, or enter: write -? for writing help.\n");
            }
            match++;
        }
        i++;
      }
      if (match==0) //�ݬݬO�_�����W�r�۲Ū�
        printf("No matched register name found, and no data is written.\n");
    }
    else    //write�\��H�~�A��L��J���~�����p
    {
      printf("Referecnce command:\n");
      printf("write -?\t\tFor writing help\n");
      printf("write ME_CTRL 1\t\tWrite the ME_CTRL register with 1 in heximal\n");
      printf("write ME_CTRL.tw 1\tWrite the register ME_CTRL and field tw with 1 in heximal\n");
    }
  }
          
  // load ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "load") == 0)
  {   
      int load_fail=0;
      if(arg_num==5 && strcmp(cmd_arg[0] , "-f")==0 && (strcmp(cmd_arg[2] , "-name")==0 || strcmp(cmd_arg[2] , "-n")==0) )
      //ex: load -f tb_inst -n DC 1280000
      {
          FILE  *image_file;
          BYTE  *data;      //buffer�j�p
          int   length=0;   //�n�쪺����
          int   i=0;
          image_file = fopen(cmd_arg[1], "rb");
          if(!image_file)
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[1]);
              printf("�A�O���O���ɮש���a��F�H�I\n");
              load_fail=1;
          }
          else
          {
              printf("File %s was opened OK!\n",cmd_arg[1]);
          }
          while(!load_fail)
          {
              fgetc(image_file);
              if( feof(image_file) )
                  break;
              length ++;
          }
          if (!load_fail)
          {
              data = new BYTE[length];
              fseek(image_file, 0, SEEK_SET);
              while(i<length)
                  data[i++] = fgetc(image_file);
              int ret;
              ret=CDebugImp::memWrite(cmd_arg[3] ,data, atoi(cmd_arg[4]), length);
              delete [] data;
              fclose(image_file);
              if (ret==TB_ERROR)
              {
                  printf("�g��Ʈɵo�Ϳ��~�I\n");
                  load_fail=1;
                  if (script_flag)
                  {
                      script_flag=0;
                      fclose(script_file);
                  }
              }
          }
      }
      else if(arg_num==4 && strcmp(cmd_arg[0] , "-tf")==0 && ( strcmp(cmd_arg[2] , "-name")==0 || strcmp(cmd_arg[2] , "-n")==0 || strcmp(cmd_arg[2] , "-addr")==0 ) )
      //ex: load -tf loadmem2.txt  -n DC
      //ex: load -tf loadmem2.txt  -addr 0x00002379
      {
          //FILE *mem_file;
          const ULONG BufferSize=1500;      //�ɮ׸��`�@�h�֭�byte�A�ݧ�j
          char mem_read[BufferSize][20];    //�C�Ӧr��̤j�e�q
          
          ifstream fin(cmd_arg[1]);
          if(!fin)
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[1]);
              printf("�A�O���O���ɮש���a��F�H�I\n");
              load_fail=1;
          }
          else
          {
              printf("File %s was opened OK!�C\n",cmd_arg[1]);
              int dataCount=0;      //���Ī�data�`��
              char AddressJump[20];
              int Ai=0;                 //Address�Ӽƫ���
              int writemem;
              int nonbin=0;
              int nonhex=0;
              int i;
              int dataCountLast=0;
              int Bl;
              int Bl_sum=0;
              int Addr_next=0;
              int binorhex=0;   //�w�]��Ƴ��Obinary��
              int BitNum=8;
              int loadAddr=0;
              char addr2module[10];
              int addr,addr_offset;

              //�Y�O-addr => ���Ѧ�}��X���ݪ�module
              //ex: load -tf loadmem2.txt  -addr 0x18009004
              if (strcmp(cmd_arg[2] , "-addr")==0 )
              {
                  addr = hex2dec(cmd_arg[3]);
                  printf("Addr=%d in dec\n",addr);
                  printf("result=%x in hex\n",addr);
                  if     (addr >= 0x00000000 && addr <= 0x0fffffff)
                  {
                      addr_offset=addr;
                      strcpy(addr2module,"DC");
                      loadAddr=1;
                      printf("In Region 1\t offset is %x\n",addr_offset);
                  }
                  else if(addr >= 0x10000000 && addr <= 0x10001fff)
                  {
                      addr_offset=addr-0x10000000;
                      strcpy(addr2module,"module2");
                      loadAddr=1;
                      printf("In Region 2\t offset is %x\n",addr_offset);
                  }
                  else if(addr >= 0x10002000 && addr <= 0x10007fff)
                  {
                      addr_offset=addr-0x10002000;
                      strcpy(addr2module,"module3");
                      loadAddr=1;
                      printf("In Region 3\t offset is %x\n",addr_offset);
                  }
                  else if(addr >= 0x18000000 && addr <= 0x1803ffff)
                  {
                      //���ϰ�ݴM��register
                      int findReg=0;
                      char reg_name[40];
                      findReg=addr2reg(addr,reg_name);
                      if (findReg==-1)
                      {
                          printf("Can't find register in address %x.",addr);
                      }
                      else
                      {
                          addr_offset=addr-0x18000000;
                          printf("Find register %s\n",reg_name);
                          strcpy(addr2module,"module4");
                          loadAddr=1;
                          printf("In Region 4\t offset is %x\n",addr_offset);
                      }
                  }
                  else if(addr >= 0x1e000000 && addr <= 0x1fcfffff)
                  {
                      addr_offset=addr-0x1e000000;
                      strcpy(addr2module,"module5");
                      loadAddr=1;
                      printf("In Region 5\t offset is %x\n",addr_offset);
                  }
                  else
                  {
                      strcpy(addr2module,"No module");
                      loadAddr=0;
                      load_fail=1;
                      printf("Out of region\n");
                  }
                  printf("����addr=%x,\taddr_offset=%x\n",addr,addr_offset);
                  printf("module=%s\n",addr2module);
                  
              }
              //ex: load -tf loadmem2.txt -n DC
              while(!fin.eof())//���٨S��Ū���ɧ���
              {
                  fin >> mem_read[dataCount];
                  //cout << "���ɪ�dataCount���G" << dataCount << '\n';
                  //printf("mem_read[%d]=%s\teof=%d\tlength=%d\n",dataCount,mem_read[dataCount],fin.eof(),strlen(mem_read[dataCount]));
                  mem_read[dataCount][strlen(mem_read[dataCount])]='\0';
                  //int loadstop=0;
                  nonbin=0;
                  nonhex=0;
                  writemem=0;
                  //�}�l���R��Ū�쪺�C�@�r�ꪺ���
                  if (strcmp(mem_read[dataCount],"%bin%") == 0 || strcmp(mem_read[dataCount],"//%bin%") == 0)
                  {
                      binorhex=0;   //�N�O��binary
                      BitNum=8;
                      //printf("Data type is changed to binary!\n");
                      continue;
                  }
                  else if (strcmp(mem_read[dataCount],"%hex%") == 0 || strcmp(mem_read[dataCount],"//%hex%") == 0)
                  {
                      binorhex=1;   //�N�O��hex
                      BitNum=2;
                      //printf("Data type is changed to hex!\n");
                      continue;
                  }
                  else if (mem_read[dataCount][0]=='\n' || mem_read[dataCount][0]==';' ||mem_read[dataCount][0]=='/' || mem_read[dataCount][0]=='%')
                  {
                      continue;     //�������p
                  }                  if (mem_read[dataCount][0]=='\n' || mem_read[dataCount][0]==';' ||mem_read[dataCount][0]=='/')
                  {
                      //cout << "���椣��\n";
                      continue;     //�������p
                  }
                  else if (mem_read[dataCount][0]=='@') //Ū��p�ѹ�    => �}�l�g���
                  {
                      //cout << "Ū��p�ѹ��F\n";
                      if ( strlen(mem_read[dataCount]) ==1)
                          continue;
                      int i=1;
                      while(i<strlen(mem_read[dataCount]))
                      {
                          AddressJump[i-1]=mem_read[dataCount][i];
                          i++;
                      }
                      AddressJump[i-1]='\0';
                      if (hex2dec(AddressJump) == -1)
                      {
                          printf("��}%s�����D�A�������p\n",AddressJump);
                          continue;
                      }
                      else 
                      {
                          Ai++;
                          writemem=1;
                      }
                  }
                  else if (strlen(mem_read[dataCount])!=BitNum)
                  {
                      if (strlen(mem_read[dataCount])!=0)
                          //cout << "invalid data read!\n";  //�]����Ƥ@�w�n�T�w����(2or8bits)
                      if (!fin.eof())  //�ˬd�S�L�A��Ƥ���
                          continue;
                  }
                  //�ˬd���binary���
                  else if (binorhex==0)  //�N�Obin���ɭ�
                  {
                      for (i=0;i<BitNum;i++)
                      {
                          if(mem_read[dataCount][i] !='0' && mem_read[dataCount][i]!='1')
                          {
                              //cout << "invalid data read!\n";  //�]����Ƥ@�w�n0��1
                              nonbin=1;
                          }
                      }
                      if (nonbin==1 &&  !fin.eof())  //�ˬd�S�L�A��Ƥ���
                      {
                          continue;
                      }
                      else
                      {
                          //cout << "�ˬdOK�I\n";
                          dataCount++;
                      }
                  }
                  //�ˬd���hex���
                  else if (binorhex==1)  //�N�Ohex���ɭ�
                  {
                      if ( hex2dec(mem_read[dataCount]) == -1 )
                      {
                          //cout << "invalid data read!\n";  //�]����Ƥ@�w�nhex
                          nonhex=1;
                      }
                      if (nonhex==1 && !fin.eof())  //�ˬd�S�L�A��Ƥ���
                      {
                          continue;
                      }
                      else
                      {
                          //cout << "�ˬdOK�I\n";
                          dataCount++;
                      }
                  }
                  if ((writemem ==1 || fin.eof() ==1) && !load_fail)     //�g���    1.Ū��@ 2.Ū��EOF
                  {
                      //cout << "�}�l�g���\n";
                      Bl=dataCount-dataCountLast;
                      if (Ai==1 && Bl==0)   //�Ĥ@��g@XX�A�����g���ʧ@�C
                      {
                          Addr_next=hex2dec(AddressJump);   //�g��}�@�w�Ohex
                          continue;
                      }
                      else if (Bl==0)        //Bl=0�ɡA�N���μg��ƤF
                      {
                          Addr_next=hex2dec(AddressJump);   //�g��}�@�w�Ohex
                          continue;
                      }
                      BYTE  *data_load;     //buffer�j�p
                      data_load = new BYTE[Bl];
                      if (binorhex==0)  //binary��
                      {
                          for (i=0;i<Bl;i++)
                          {
                              data_load[i] = bin2dec(mem_read[i+Bl_sum]);
                          }
                      }
                      if (binorhex==1)  //hex��
                      {
                          for (i=0;i<Bl;i++)
                          {
                              data_load[i] = hex2dec(mem_read[i+Bl_sum]);
                          }
                      }
                      printf("\n�����g�i��}%0x����Ʀ@%d���A�̧Ǭ��G\n",Addr_next,Bl);
                      for (i=0;i<Bl;i++)
                      {
                          printf("%0x\t",data_load[i]);
                      }
                      cout << '\n';
                      if(loadAddr==1)
                      {
                          strcpy(cmd_arg[3],addr2module);
                          Addr_next=addr_offset;
                      }
                      int ret;
                      ret=CDebugImp::memWrite(cmd_arg[3] ,data_load, Addr_next,Bl);
                      delete [] data_load;
                      if (ret==TB_ERROR)
                      {
                          printf("�g��Ʈɵo�Ϳ��~�I\n");
                          load_fail=1;
                          if (script_flag)
                          {
                              script_flag=0;
                              fclose(script_file);
                          }
                      }
                      dataCountLast=dataCount;
                      if (fin.eof() !=1)
                          Addr_next=hex2dec(AddressJump);
                      Bl_sum+=Bl;
                  }
                  //else if (mem_read[dataCount][0]=='@') //�ѤF�o�椰��N��
                    //  continue;
              }
          fin.close();
          }
      }
      else
      {
          load_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }
      if(load_fail==1)
      {
          printf("Referecnce command:\n");
          printf("load -f tb_inst -n DC 1280000\n");
          printf("//load instruction to DC memory position 1280000.\n");
          printf("load -tf loadmem2.txt  -n DC\n");
          printf("//load memory format loadmem2.txt to module DC in text mode.\n");
          printf("load -tf loadmem2.txt  -addr 0x00002379\n");
          printf("//load memory format loadmem2.txt to module at address 0x00002379 in text mode.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }
          
  // store ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "store") == 0)
  {
    // TBD: store
    // 1) store module name address to file
    //  store buffer to a file
    //  then use use CDebug::memRead to read buffer data 
    //  from assigned address
    // 2) store memory map address ( later)
      // TBD: load 
      // 1) load to module name address
      //  load from a file to a buffer
      //  then use use CDebug::memWrite to write buffer data      
      //  assigned address
      // 2) load to memory map address ( later)
      int store_fail=0;
      if(arg_num==7 && ( strcmp(cmd_arg[0] , "-name")==0 || strcmp(cmd_arg[0] , "-n")==0 ) && strcmp(cmd_arg[5] , "-f")==0 )
      //store -n ME 0 -l 512 -f tmem.yuv
      {
          FILE  *image_file;
          BYTE  *data;     //buffer�j�p
          int   length=atoi(cmd_arg[4]);      //�n�쪺����
          int   i=0;
          image_file = fopen(cmd_arg[6], "wb");
          if(!image_file)   //�n���O�b�g���ɮ׶}�Ҥ@�w�S���D
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[6]);
              store_fail=1;
          }
          data = new BYTE[length];
          int ret;
          ret=CDebugImp::memRead(cmd_arg[1] ,data, atoi(cmd_arg[2]), length);
          while(i<length)
              fputc( data[i++], image_file);
          fclose(image_file);
          delete [] data;
          if (ret==TB_ERROR)
          {
              printf("Ū��Ʈɵo�Ϳ��~�I\n");
              store_fail=1;
          }
      }
      else if(arg_num>=7 && (strcmp(cmd_arg[0] , "-name")==0 || strcmp(cmd_arg[0] , "-n")==0) && strcmp(cmd_arg[5] , "-tf")==0 )
      //store -n DC 0 -l 128 -tf savedata5.txt -b -c this is a DVR
      {
          FILE  *image_file;
          BYTE  *data;     //buffer�j�p
          int   length=atoi(cmd_arg[4]);    //�n�쪺����
          int   big_end=0;                  //�w�]��little endian
          big_end=(!strcmp(cmd_arg[7],"-b"))?1:0;
          int   i=0;
          image_file = fopen(cmd_arg[6], "aw");
          if(!image_file)   //�n���O�b�g���ɮ׶}�Ҥ@�w�S���D
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[6]);
              store_fail=1;
          }
          data = new BYTE[length];
          int ret;
          ret=CDebugImp::memRead(cmd_arg[1] ,data, atoi(cmd_arg[2]), length);
          if (ret==TB_ERROR)
          {
              printf("Ūtf��Ʈɵo�Ϳ��~�I\n");
              store_fail=1;
              fclose(image_file);
              delete [] data;
          }

          //for (i=0;i<length;i++)
              //printf("Ū�X�Ӫ���%d����ƬO�G%d\n",i,data[i]);
      
          char comment_word[100];

          if (!store_fail && arg_num > 7 && (strcmp(cmd_arg[7] , "-c")==0 || strcmp(cmd_arg[8] , "-c")==0)) //�[�Wcomment
          {
              strcpy(comment_word,"//");
              int cmt;
              cmt=(!strcmp(cmd_arg[7] , "-c"))?8:9;
              for (int k=cmt;k<arg_num;k++)
              {
                  strcat(comment_word," ");
                  strcat(comment_word,cmd_arg[k]);
              }
              //printf("comment is :   %s",comment_word);
              fputs(comment_word, image_file);
              fputs("\n", image_file);
          }

          if (!store_fail && big_end==0)   // Big-endian��
          {
              fputs("// Big endian", image_file);
              fputs("\n", image_file);
              i=0; 
              while(i<length)
              {
                  //printf("�N�n�g�i����%d����ƬO�G%d\n",i,data[i]);
                  fprintf(image_file,"%0x",data[i]);
                  //fputc( data[i],  image_file);
                  if (i%8==7)
                      fputc( '\n', image_file);
                  else
                      fputc( ' ',  image_file);
                  i++;
              }
              if (i%8!=0)
                  fputs( "\n", image_file);
              fclose(image_file);
              delete [] data;
          }
          else if (!store_fail) // Little-endian��
          {
              int i=0;
              int Q;
              int R;
              Q=length/8;
              R=length%8;
              fputs("// Little endian", image_file);
              fputs("\n", image_file);
              for (int j=1;j<(Q+1);j++)
              {
                  for (int k=0;k<8;k++)
                  {
                      fprintf(image_file,"%0x",data[8*j-k-1]);
                      //printf("�{�b�n�s%0x\t",data[8*j-k-1]);
                      if (k!=7)
                          fputc( ' ',  image_file);
                  }
                  fputc( '\n', image_file);
              }
              if(R!=0)
              {
                  for (j=0;j<(8-R);j++)
                  {
                      fprintf(image_file,"%s","cd");
                      fputc( ' ',  image_file);
                  }
                  for (j=8-R;j<8;j++)
                  {
                      fprintf(image_file,"%0x",data[8*(Q+1)-j-1]);
                      //printf("�{�b�n�s%0x\t",data[8*(Q+1)-j-1]);
                      fputc( ' ',  image_file);
                  }
                  fputc( '\n', image_file);
              }
              fclose(image_file);
              delete [] data;
          }
      }
      else
      {
          store_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }      
      if(store_fail==1)
      {
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ) && script_flag)
          {
              script_flag=0;
              fclose(script_file);
          }
          printf("Referecnce command:\n");
          printf("store -n DC 0 -l 128 -f  savedata.txt\n");
          printf("store -n DC 0 -l 128 -tf savedata.txt\n");
          printf("store -n DC 0 -l 128 -tf savedata.txt -b\n");
          printf("store -n DC 0 -l 128 -tf savedata.txt -c this is a DVR\n");
          printf("store -n DC 0 -l 128 -tf savedata.txt -b -c this is a DVR\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }

  // loadimg ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "loadimg") == 0)
  {   
      // TBD: load 
      // 1) load to module name address
      //  load from a file to a buffer
      //  then use use CDebug::memWrite to write buffer data      
      //  assigned address
      // 2) load to memory map address ( later)
      int loadimg_fail=0;
      if(arg_num==6 && (strcmp(cmd_arg[3] , "-n")==0 || strcmp(cmd_arg[3] , "-name")==0 ))
      //loadimg silent_cif.yuv 352 288 -n DC 0
      {
          FILE  *image_file;
          BYTE  *data;                      //buffer�j�p
          int   width=atoi(cmd_arg[1]);     //�n�쪺����
          int   height=atoi(cmd_arg[2]);    //�n�쪺����
          int   i=0;
          image_file = fopen(cmd_arg[0], "rb");
          if(!image_file)
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[0]);
              printf("�A�O���O���ɮש���a��F�H�I\n");
              loadimg_fail=1;
          }
          if(!loadimg_fail)
          {
              data = new BYTE[width*height];
              while(i<width*height)
                  data[i++] = fgetc(image_file);
              int ret;
              ret=CDebugImp::memImgLoad( cmd_arg[4], atoi(cmd_arg[5]), data, width,height);
              delete [] data;
              fclose(image_file);
              if (ret==TB_ERROR)
              {
                  printf("Ū��Ʈɵo�Ϳ��~�I\n");
                  loadimg_fail=1;
                  if (script_flag)
                  {
                      script_flag=0;
                      fclose(script_file);
                  }
              }
          }
      }
      else
      {
          loadimg_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }      
      if(loadimg_fail==1)
      {
          printf("Referecnce command:\n");
          printf("loadimg silent_cif.yuv 352 288 -n DC 0\n");
          printf("//load from file silent_cif.yuv with width=352, height=288 on module DC at index=0.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }
          
  // storeimg ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "storeimg") == 0)
  {
    // TBD: store
    // 1) store module name address to file
    //  store buffer to a file
    //  then use use CDebug::memRead to read buffer data 
    //  from assigned address
    // 2) store memory map address ( later)
      // TBD: load 
      // 1) load to module name address
      //  load from a file to a buffer
      //  then use use CDebug::memWrite to write buffer data      
      //  assigned address
      // 2) load to memory map address ( later)
      int storeimg_fail=0;

      if(arg_num==7 && (strcmp(cmd_arg[0] , "-n") ==0 ||strcmp(cmd_arg[0] , "-name") ==0) && strcmp(cmd_arg[5] , "-f") ==0)
      //storeimg -n DC 0 352 288 -tf silent_bak.yuv
      {
          cout << "hello!";
          FILE  *image_file;
          BYTE  *data;     //buffer�j�p
          int   width=atoi(cmd_arg[3]);     //�n�쪺����
          int   height=atoi(cmd_arg[4]);    //�n�쪺����
          int   i=0;
          image_file = fopen(cmd_arg[6], "wb");
          if(!image_file)       //�n���O�b�g���ɮ׶}�Ҥ@�w�S���D
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[6]);
              storeimg_fail=1;
          }
          data = new BYTE[width*height];
          int ret;
          ret=CDebugImp::memImgStore(cmd_arg[1],atoi(cmd_arg[2]), data, width,height);
          while(i<width*height)
              fputc(data[i++], image_file);
          fclose(image_file);
          delete [] data;
          if (ret==TB_ERROR)
          {
              printf("�g��Ʈɵo�Ϳ��~�I\n");
              storeimg_fail=1;
              if (script_flag)
              {
                  script_flag=0;
                  fclose(script_file);
              }
          }
      }
      else
      {
          storeimg_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }      
      if(storeimg_fail==1)
      {
          printf("Referecnce command:\n");
          printf("storeimg -n DC 0 352 288 -f silent_bak.yuv\n");
          printf("//store image on module DC on index0, width=352, height=288 at image file silent_bak.yuv.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }

  // loadprog ////////////////////////////////////////////////////////////////
  // EX: loadprog -n CPU -f file
  else if ( strcmp(cmd_name, "loadprog") == 0)
  {   
      int loadprog_fail=0;
      if(arg_num==4 && (strcmp(cmd_arg[0] , "-name")==0 ||strcmp(cmd_arg[0] , "-n")==0)&& strcmp(cmd_arg[2] , "-f")==0)
      {
          FILE *inst_file;
          inst_file = fopen(cmd_arg[3], "rb");   //���T�wbin or asc
          if(!inst_file)
          {
              printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[3]);
              printf("�A�O���O���ɮש���a��F�H�I\n");
              printf("�����O������!\n");
              loadprog_fail=1;
          }
          else
          {
              printf("File %s was opened OK!\n",cmd_arg[3]);
              int ret;
              ret=CDebugImp::progLoad(cmd_arg[1],inst_file);
              fclose(inst_file);
              if (ret==TB_ERROR)
              {
                  printf("Ū��Ʈɵo�Ϳ��~�I\n");
                  loadprog_fail=1;
              }
          }
      }
      else
      {
      	loadprog_fail=1;
        if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
            printf("Illegal parameter, please input again.\n");
      }
      if (loadprog_fail==1)
      {
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ) && script_flag)
          {
              script_flag=0;
              fclose(script_file);
          }
          printf("Referecnce command:\n");
          printf("loadprog -n CPU -f file.txt\n");
          printf("//load program from file file.txt on CPU.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }
   
  // setbreak ////////////////////////////////////////////////////////////////
  // EX: setbreak -n DC -pc 0x11ff
  else if ( strcmp(cmd_name, "setbreak") == 0)
  {   
      int setbreak_fail=0;
      if(arg_num==4 && (strcmp(cmd_arg[0] , "-name")==0 || strcmp(cmd_arg[0] , "-n")==0 ) && strcmp(cmd_arg[2] , "-pc")==0)
      {
          int ret;
          ret=CDebugImp::setBreakPoint(cmd_arg[1],hex2dec(cmd_arg[3]));
          if (ret==TB_ERROR)
          {
              printf("�ʧ@�o�Ϳ��~�I\n");
              setbreak_fail=1;
              if (script_flag)
              {
                  script_flag=0;
                  fclose(script_file);
              }
          }
      }
      else
      {
      	setbreak_fail=1;
        if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
            printf("Illegal parameter, please input again.\n");
      }
      if (setbreak_fail==1)
      {
          printf("Referecnce command:\n");
          printf("setbreak -n DC -pc 0x11ff\n");
          printf("//Set breakpoint on module DC when program counter is at 0x11ff.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }

  // clrbreak ////////////////////////////////////////////////////////////////
  // EX: clrbreak -n DC -pc 0x11ff
  else if ( strcmp(cmd_name, "clrbreak") == 0)
  {   
      int clrbreak_fail=0;
      if(arg_num==4 && (strcmp(cmd_arg[0] , "-n")==0 || strcmp(cmd_arg[0] , "-name")==0) && strcmp(cmd_arg[2] , "-pc")==0)
      {
          int ret;
          ret=CDebugImp::clearBreakPoint(cmd_arg[1],hex2dec(cmd_arg[3]));
          if (ret==TB_ERROR)
          {
              printf("�ʧ@�o�Ϳ��~�I\n");
              clrbreak_fail=1;
              if (script_flag)
              {
                  script_flag=0;
                  fclose(script_file);
              }
          }
      }
      else
      {
          clrbreak_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }
      if (clrbreak_fail==1)
      {
          printf("Referecnce command:\n");
          printf("clrbreak -n DC -pc 0x11ff\n");
          printf("//Clear breakpoint on module DC when program counter is at 0x11ff.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }

  // setceibreak ////////////////////////////////////////////////////////////////
  // EX: setceibreak -n DC -code LDMCCIT
  else if ( strcmp(cmd_name, "setceibreak") == 0)
  {
      int setceibreak_fail=0;
      if(arg_num==4 && (strcmp(cmd_arg[0] , "-n")==0 || strcmp(cmd_arg[0] , "-name")==0 ) && strcmp(cmd_arg[2] , "-code")==0)
      {
          int main_opcode;
          int sub_opcode;
          //printf("cmd_name is %s\n",cmd_arg[3]);
          setceibreak_fail=findOpSubop(cmd_arg[3],main_opcode,sub_opcode);
          if (setceibreak_fail!=-1)
          {
              //printf("Got: Main_OPCODE=%d\tSub_OPCODE=%d\n",main_opcode,sub_opcode);
              int ret;
              ret=CDebugImp::setCEIBreak(cmd_arg[1],main_opcode,sub_opcode);
              if (ret==TB_ERROR)
              {
                  printf("�ʧ@�o�Ϳ��~�I\n");
                  cout << "�����O������" << '\n';
                  setceibreak_fail=1;
              }
          }
          else
          {
              cout << "�����O������" << '\n';
              setceibreak_fail=1;
          }
      }
      else
      {
          setceibreak_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }
      if (setceibreak_fail==1)
      {
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ) && script_flag)
          {
              script_flag=0;
              fclose(script_file);
          }
          printf("Referecnce command:\n");
          printf("setceibreak -n DC -code LDMCCIT\n");
          printf("//set cei breakpoint on module DC when code is LDMCCIT.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }

  // clrceibreak ////////////////////////////////////////////////////////////////
  // EX: clrceibreak -n DC -code LDMCCIT
  else if ( strcmp(cmd_name, "clrceibreak") == 0)
  {   
      int clrceibreak_fail=0;
      if(arg_num==4 && (strcmp(cmd_arg[0] , "-name")==0 || strcmp(cmd_arg[0] , "-n")==0 ) && strcmp(cmd_arg[2] , "-code")==0)
      {
          int main_opcode;
          int sub_opcode;
          //printf("cmd_name is %s\n",cmd_arg[3]);
          clrceibreak_fail=findOpSubop(cmd_arg[3],main_opcode,sub_opcode);
          if (clrceibreak_fail!=-1)
          {
              //printf("Got: Main_OPCODE=%d\tSub_OPCODE=%d\n",main_opcode,sub_opcode);
              int ret;
              ret=CDebugImp::clearCEIBreak(cmd_arg[1],main_opcode,sub_opcode);
              if (ret==TB_ERROR)
              {
                  printf("�ʧ@�o�Ϳ��~�I\n");
                  cout << "�����O������" << '\n';
                  clrceibreak_fail=1;
              }
          }
          else
          {
              cout << "�����O������" << '\n';
              clrceibreak_fail=1;
          }
      }
      else
      {
          clrceibreak_fail=1;
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ))
              printf("Illegal parameter, please input again.\n");
      }
      if (clrceibreak_fail==1)
      {
          if (arg_num>=1 && ( strcmp(cmd_arg[0] , "-?") !=0 ) && script_flag)
          {
              script_flag=0;
              fclose(script_file);
          }
          printf("Referecnce command:\n");
          printf("clrceibreak -n DC -code LDMCCIT\n");
          printf("//Clear cei breakpoint on module DC when code is LDMCCIT.\n");
      }
      else
      {
          printf("�����O���Q����!\n");
      }
  }
  
  // script ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "script") == 0 || strcmp(cmd_name, "s") == 0)
  {
      int script_help=0;
      cmdCount =0;
      if(arg_num==1 && strcmp(cmd_arg[0],"-?") != 0)
      {
          if( script_flag == true )
          {
              cout << "Double script call!! Not allowed!!\n";
          }
          else
          {
              script_file = fopen(cmd_arg[0], "r");
              if( script_file == NULL )
              {
                  printf("�ɮ�%s�L�k�}�ҡC\n",cmd_arg[0]);
                  printf("�A�O���O���ɮש���a��F�H�I\n");                  
                  script_help=1;
              }
              else
              {
                  script_flag = true;
                  printf("�ɮ�%s�w�}�ҡCŪ�����O��.......\n",cmd_arg[0]);
              }

          }
      }
      else if(arg_num==1 && strcmp(cmd_arg[0],"-?") == 0)
          script_help=1;
      else if(arg_num==0)
      {
          if( script_flag == true )
          {
              cout << "Double script call!! Not allowed!!\n";
          }
          else
          {
              printf("No script file specfied. Load the default script file: script.txt\n");
              script_file = fopen("script.txt", "r");
              if( script_file == NULL )
              {
                  printf("�ɮ�script.txt�䤣��\n");
                  script_help=1;
              }
              else
                  script_flag = true;
          }
      }
      else
      {
          printf("Illegal parameter, please input again.\n");
          script_help=1;
      }
      if (script_help==1)
      {
          printf("Referecnce command:\n");
          printf("script\t\t\tFor loading the dafault file.\n");
          printf("script script.txt\tFor loading script.txt file.\n");    
      }
  }
          
  else if ( strcmp(cmd_name, "test") == 0 || strcmp(cmd_name, "t") == 0 )   //for test case
  {
      int kkk=IRegBase::m_regCount;
      printf("total number is =%d\n",kkk);
      for (int i=0;i<kkk;i++)
      {
          printf("�s��%d\t��}%x\t�W�r%s\n",i,IRegBase::m_regTable[i]->m_address,IRegBase::m_regTable[i]->m_registerName);
      }
      printf("TB_OK is %d\n",TB_OK);
      printf("TB_ERROR is %d\n",TB_ERROR);
      printf("TB_DEBUG_STOP is %d\n",TB_DEBUG_STOP);
      printf("TB_DEBUG_DONE is %d\n",TB_DEBUG_DONE);
 
  }


  // quit ////////////////////////////////////////////////////////////////
  else if ( strcmp(cmd_name, "quit") == 0 || strcmp(cmd_name, "exit") == 0 || strcmp(cmd_name, "q") == 0 || strcmp(cmd_name, "0") == 0)
  {
      printf("�����F�O�a�I�H�A���I�I\n");
      return TB_DEBUG_STOP;
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

  else if ( strcmp(cmd_name, "p") == 0 )
  {
      system("pause");
  }

  else if ( strcmp(cmd_name, "pauseon") == 0 )
  {
      pause=1;
      printf("Pause on mode.\n");
  }

  else if ( strcmp(cmd_name, "pauseoff") == 0 )
  {
      pause=0;
      printf("Pause off mode.\n");
  }

  // for checking ////////////////////////////////////////////////////////////////
  else      //for others input commands
  {
      int valid_cmd;
      valid_cmd=system(cmd_line);
      if(valid_cmd)
      {
          //printf("%s: Command not found.\n",cmd_name);
          printf("For help on the debugging interface, enter:  help or ?\n");
      }
  }
  return TB_DEBUG_DONE;
}


int pow(int t1,int t2)  //��t1��t2����
{
    int ddd=1;
    for (int i=0;i<t2;i++)
        ddd*=t1;
    return ddd;
}

int bin2dec(char* bbb)  //�u�䴩�@��byte��
{
    int ddd=0;
    ddd=(bbb[0]-48)*128+(bbb[1]-48)*64+(bbb[2]-48)*32+(bbb[3]-48)*16+(bbb[4]-48)*8+(bbb[5]-48)*4+(bbb[6]-48)*2+(bbb[7]-48)*1;
    return ddd;
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

int addr2reg(int& addr, char *reg_name)
{
    int totalReg=IRegBase::m_regCount;
    int foundRegister=0;
    for (int i=0;i<totalReg;i++)
    {
        if (addr==IRegBase::m_regTable[i]->m_address)
        {
            printf("found register.\n");
            printf("�s��%d\t��}%x\t�W�r%s\n",i,IRegBase::m_regTable[i]->m_address,IRegBase::m_regTable[i]->m_registerName);
            strcpy(reg_name,IRegBase::m_regTable[i]->m_registerName);
            foundRegister=1;
        }
    }
    if (foundRegister==0)
    {
        return -1;
    }
    return 0;
}

int findOpSubop(char* cmd_name,int &OPCODE, int &SUBOPCODE)
{
    int cmd_num;
    int match=0;
    cmd_num=sizeof(task)/sizeof(task[1]);
    struct list *ptr;
    for (int i=0;i<cmd_num;i++)
    {
        ptr=&task[i];
        if(strcmp(ptr->name,cmd_name)==0)
        {
            ptr=&task[i];
            match=1;
            break;
        }
    }
    if (match==0)
    {
        printf("�䤣��P�W�٪����O!\n");
        return -1;
    }
    OPCODE=ptr->OPCODE;
    SUBOPCODE=ptr->SUBOPCODE;
    //    OPCODE=task[i].OPCODE;
    //    SUBOPCODE=task[i].SUBOPCODE;
    return 0;
}
