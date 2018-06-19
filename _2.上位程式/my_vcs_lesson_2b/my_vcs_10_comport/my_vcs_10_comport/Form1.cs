using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports;          //for serial ports

namespace my_vcs_10_comport
{
    public partial class Form1 : Form
    {
        string RxString = "";
        string[] COM_Ports_NameArr;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = comboBox1.Text;
            serialPort1.BaudRate = int.Parse(comboBox2.Text);

            serialPort1.Open();
            if (serialPort1.IsOpen)
            {
                button1.Enabled = false;
                button2.Enabled = true;
                richTextBox1.ReadOnly = false;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                serialPort1.Close();
                button1.Enabled = true;
                button2.Enabled = false;
                richTextBox1.ReadOnly = true;
            }
        }

        private void richTextBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            // If the port is closed, don't try to send a character.
            if (!serialPort1.IsOpen) return;

            // If the port is Open, declare a char[] array with one element.
            char[] buff = new char[1];

            // Load element 0 with the key character.
            buff[0] = e.KeyChar;

            // Send the one character buffer.
            serialPort1.Write(buff, 0, 1);

            // Set the KeyPress event as handled so the character won't
            // display locally. If you want it to display, omit the next line.
            e.Handled = true;
        }

        private void DisplayText(object sender, EventArgs e)
        {
            richTextBox1.AppendText(RxString);
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }
        private void serialPort1_DataReceived(object sender, System.IO.Ports.SerialDataReceivedEventArgs e)
        {
            //RxString = serialPort1.ReadExisting();
            //this.Invoke(new EventHandler(DisplayText));
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Send_Initial_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Initial ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Send_Disable_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Disable ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Send_Read_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Read ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Send_Disable_Read_ADC_Cmd();
            richTextBox1.AppendText("[PC]: Disable Read ADC\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Send_Reset_Demo_Board_Cmd();
            richTextBox1.AppendText("[PC]: Reset Demo Board\n");
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        public bool Send_Reset_Demo_Board_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x00;
            data[3] = 0x00;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        public bool Send_Initial_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x00;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }
        public bool Send_Disable_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x01;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        public bool Send_Read_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x02;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
        }

        public bool Send_Disable_Read_ADC_Cmd()
        {
            byte[] data = new byte[10];
            data[0] = 0xAA;
            data[1] = 0x20;
            data[2] = 0x01;
            data[3] = 0x03;
            data[4] = 0x00;
            data[5] = 0x00;
            data[6] = 0x00;
            data[7] = 0x00;
            data[8] = 0x00;
            data[9] = CalcCheckSum(data, 9);

            if (serialPort1.IsOpen)
            {
                serialPort1.Write(data, 0, data.Length);
            }
            else
            {
                return false;
            }
            return true;
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

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區
        public int BytesToRead = 0;							//緩衝區內可接收資料數
        string input ="";
        private void SerialPortTimer100ms_Tick(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;

                if (BytesToRead > 0)
                {
                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer, 0, BytesToRead);

                    if (BytesToRead == 10)
                        SpyMonitorRX();
                    else
                    {
                        //資料不是10拜，打印出來。
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                            input += (char)receive_buffer[i];

                        richTextBox1.AppendText(input);
                        richTextBox1.ScrollToCaret();		//RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
                }
            }
        }
        private void SpyMonitorRX()
        {
            if (BytesToRead == 10)
            {
                input = "";
                for (int i = 0; i < BytesToRead; i++)
                    input += (char)receive_buffer[i];

                if ((input[0] == 0x55) && (input[1] == 0x20) && (input[2] == 0x01))
                {
                    textBox3.Text = Convert.ToString(input[3], 16) + " " + Convert.ToString(input[4], 16);
                    textBox4.Text = Convert.ToString((input[3] << 8 | input[4]) * 5000 / 4096);
                }
            }
            else
            {
                //資料是10拜，但是解不出所要的資訊。
                /*
                richTextBox1.AppendText(input);
                richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                */
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            MessageBox.Show("和板子通訊。定義通訊格式。" + "\n" + "和my_vcs_07一樣，多了板子傳訊息給PC、PC解讀後顯示在GUI上。\nComport與Baud改用ComboBox選擇。\n加了Comport Scan、啟動時，先做Comport Scan。");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            Comport_Scan();
        }

        private void Comport_Scan()
        {
            string[] tempString = SerialPort.GetPortNames();
            Array.Resize(ref COM_Ports_NameArr, tempString.Length);
            tempString.CopyTo(COM_Ports_NameArr, 0);

            comboBox1.Items.Clear();    //Clear All items in Combobox

            foreach (string port in COM_Ports_NameArr)
            {
                //MessageBox.Show("get comport : " + port);
                comboBox1.Items.Add(port);
            }

            if (COM_Ports_NameArr.Length > 0)
                comboBox1.Text = COM_Ports_NameArr[0];
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Comport_Scan();
        }
    }
}
