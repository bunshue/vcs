using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO.Ports;

//使用委派方法, 將來自串口接收到的數據顯示出來

namespace vcs_Comport1
{
    public partial class Form1 : Form
    {
        SerialPort serialPort1 = new SerialPort();

        /// <summary>
        /// 定义委托
        /// </summary>
        /// <param name="a"></param>
        public delegate void ShowString(string a);

        /// <summary>
        /// 字符显示在文本框
        /// </summary>
        /// <param name="a"></param>
        public void ShowTxt(string a)
        {
            this.richTextBox1.AppendText(DateTime.Now.ToString() + "|" + a + "\n");
            if (richTextBox1.TextLength > 2000)
            {
                richTextBox1.Clear();
            }
        }

        /// <summary>
        /// 定义委托并初始化
        /// </summary>
        ShowString AA;
        /// <summary>
        /// 接收字符串存储
        /// </summary>
        string ReadStr = "";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            serialPort1.DataReceived += new SerialDataReceivedEventHandler(serialPort1_DataReceived);

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
                    MessageBox.Show("已經連上" + serialPort1.PortName);
                }
                else
                {
                    MessageBox.Show("無法連上Comport, 請重新連線");
                }
            }
            AA = new ShowString(ShowTxt);//初始化委托
        }

        //串口收到數據並回發
        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            ReadStr = serialPort1.ReadExisting();
            byte[] ReadBuffer;
            ReadBuffer = System.Text.ASCIIEncoding.ASCII.GetBytes(ReadStr);
            this.Invoke(AA, ReadStr);
            serialPort1.Write(ReadBuffer, 0, ReadBuffer.Length);
        }
    }
}
