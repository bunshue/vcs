// 動手做5-1：從序列埠監控視窗觀察變數值

#define UART_BUF_LENGTH 5

unsigned char gui_cmd[UART_BUF_LENGTH];
unsigned char gui_cmd_index = 0;
unsigned char tcount = 0;

unsigned int ADC_A_InstanceCurrent = 0;
unsigned int ADC_A_InstanceCurrent_result = 0;
unsigned int CalcCheckSum(unsigned int *pData, unsigned int len);
void Send_ADC_Result_Cmd(unsigned int value);

///**************************************************************************
// * 函數名：CalcCheSun()
// * 功  能：計算數據校驗和
// * 輸  入：數組，計算數據長度
// * 輸  出：返回校驗和的低8位
// *************************************************************************/
unsigned int CalcCheckSum(unsigned int *pData, unsigned int len)
{
    unsigned char i = 0,sum = 0;
    for (; i < len; i++)
    {
        sum += (unsigned char) pData[i];
    }
    sum = (sum^0xFF) + 1;
    return (sum&0xFF);
}

void Send_ADC_Result_Cmd(unsigned int value)
{
  int i;
  unsigned int UartTxBuf[UART_BUF_LENGTH];

  //Get_ADC_A_Result();

  UartTxBuf[0] = 0xC1;
  UartTxBuf[1] = 0x06;
  UartTxBuf[2] = 0x01;
  UartTxBuf[3] = value;
  /*
  UartTxBuf[0] = 0x55;
  UartTxBuf[1] = 0x20;
  UartTxBuf[2] = 0x01;
  UartTxBuf[3] = 0x12;
  UartTxBuf[0] = 0x41;
  UartTxBuf[1] = 0x41;
  UartTxBuf[2] = 0x41;
  UartTxBuf[3] = 0x41;
  UartTxBuf[4] = 0x41;
  */
  UartTxBuf[4] = CalcCheckSum(UartTxBuf, 4);
  for(i=0;i<UART_BUF_LENGTH;i++)
  {
    Serial.write(UartTxBuf[i]);
    //Serial.print(UartTxBuf[i]);
    //Serial.println(UartTxBuf[i]);
  }
}

void setup() {
  Serial.begin(115200);
}

/*
void loop() {
  Serial.println("");
  Serial.println("AAAA");
  Serial.println("BBBB");
  Serial.println("CCCC");
  delay(2000); //間格 2 秒
  Serial.print("aaaa");
  Serial.print("bbbb");
  Serial.print("cccc");
  delay(2000); //間格 2 秒
}
*/

unsigned int value = 1;
void loop() {
  //Serial.print("AAAAA");
  Send_ADC_Result_Cmd(value);
  value++;
  if(value > 95)
    value = 0;
  
  delay(200); //間格 2 秒
  //Serial.print("AAAAA");
  //delay(2000); //間格 2 秒
}
