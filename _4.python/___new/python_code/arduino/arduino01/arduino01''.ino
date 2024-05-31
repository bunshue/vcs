/*
本程式為SR04超音波感測器的範例

首先要安裝ErickSimoes/Ultrasonic的函式庫
VCC接5V，GND接地。Trig接到pin 12，Echo接到pin 13。
*/

#include <Ultrasonic.h>

Ultrasonic ultrasonic(12, 13);
int distance;

#define UART_BUF_LENGTH 10
unsigned char gui_cmd[UART_BUF_LENGTH];
unsigned char gui_cmd_index = 0;
unsigned char tcount = 0;


unsigned int ADC_A_InstanceCurrent = 0;
unsigned int ADC_A_InstanceCurrent_result = 0;
unsigned int CalcCheckSum(unsigned int *pData, unsigned int len);
void Send_ADC_Result_Cmd();

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

void Send_ADC_Result_Cmd()
{
  int i;
  unsigned int UartTxBuf[UART_BUF_LENGTH];

  //Get_ADC_A_Result();

  UartTxBuf[0] = 0x55;
  UartTxBuf[1] = 0x20;
  UartTxBuf[2] = 0x01;
  UartTxBuf[3] = 0x12;
  UartTxBuf[4] = 0x34;
  UartTxBuf[5] = 0;
  UartTxBuf[6] = 0;
  UartTxBuf[7] = 0;
  UartTxBuf[8] = 0;
  UartTxBuf[9] = CalcCheckSum(UartTxBuf, 9);
  for(i=0;i<UART_BUF_LENGTH;i++)
  {
    Serial.print(UartTxBuf[i]);
    //Serial.println(UartTxBuf[i]);
    //printS(UartTxBuf[i]);
  }
}




void setup() {
  Serial.begin(9600);
}

void loop() {

  Send_ADC_Result_Cmd();
  /*
  distance = ultrasonic.read(); //不加參數就是輸出CM，可用read(INC)輸出英寸
  
  Serial.print("Distance in CM: ");
  Serial.println(distance);
  */
  delay(500); //每次間格0.5秒
}
