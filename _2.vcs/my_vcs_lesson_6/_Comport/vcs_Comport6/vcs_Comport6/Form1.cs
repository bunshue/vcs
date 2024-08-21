using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//using System.IO.Ports;          //for serial ports

namespace vcs_Comport6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }


        private void button1_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = "COM4";
            serialPort1.BaudRate = 115200;

            //serialPort1.Open(); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Open();
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                if (serialPort1.IsOpen)
                {
                    //MessageBox.Show("已經連上" + serialPort1.PortName);
                }
                else
                {
                    MessageBox.Show("無法連上Comport, 請重新連線");
                }
            }

            if (serialPort1.IsOpen)
            {
                //button1.Enabled = false;
                //button2.Enabled = true;
                richTextBox1.Text += "已連上 COM4\n";
            }
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input = "";

        private void button2_Click(object sender, EventArgs e)
        {
            //讀取
            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;
                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";

                if (BytesToRead > 0)
                {
                    if (BytesToRead > 2048)
                    {
                        serialPort1.DiscardInBuffer();  //丟棄UART buffer內的資料
                    }
                    else if (BytesToRead > 0)
                    {
                        //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                        serialPort1.Read(receive_buffer, 0, BytesToRead);

                        /*
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += (char)receive_buffer[i];
                        richTextBox1.Text += input + "\n";
                        */

                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += receive_buffer[i].ToString("X2") + " ";
                        richTextBox1.Text += input + "\n";

                        //richTextBox1.Text += receive_buffer_tmp[i].ToString("X2") + " ";

                    }
                }
            }
        }

        private byte CalcCheckSum(byte[] pData, int len)
        {
            byte sum = 0x00;
            short ii = 0;
            for (ii = 0; ii < len; ii++)
            {
                sum += pData[ii];
            }
            sum = (byte)((sum ^ 0xFF) + 1);
            return sum;
        }

        public bool Send_IMS_Data0(byte cc, byte xx, byte yy, byte zz)  //directly send data
        {
            byte[] data = new byte[5];

            data[0] = cc;
            data[1] = xx;
            data[2] = yy;
            data[3] = zz;
            data[4] = CalcCheckSum(data, 4);
            //richTextBox1.Text += "Send data:\t" + ((int)data[0]).ToString("X2") + " " + ((int)data[1]).ToString("X2") + " " + ((int)data[2]).ToString("X2") + " " + ((int)data[3]).ToString("X2") + " " + ((int)data[4]).ToString("X2") + "\n";
            //serialPort2.Write(data, 0, data.Length);
            try
            {   //可能會產生錯誤的程式區段
                serialPort1.Write(data, 0, data.Length);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "xxx錯誤訊息e02 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }
            return true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //寫入
            Send_IMS_Data0(0xFF, 0x11, 0x52, 0x00); //directly send uart command
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //關閉
            serialPort1.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Info
        }
    }
}
