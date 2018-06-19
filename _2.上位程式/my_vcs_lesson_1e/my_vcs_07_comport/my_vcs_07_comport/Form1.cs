using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_07_comport
{
    public partial class Form1 : Form
    {
        string RxString = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            serialPort1.PortName = textBox1.Text;
            serialPort1.BaudRate = int.Parse(textBox2.Text);

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
            RxString = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(DisplayText));
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

        private void button8_Click(object sender, EventArgs e)
        {
            MessageBox.Show("和板子通訊。定義通訊格式。PC發命令給板子。");
        }
    }
}
