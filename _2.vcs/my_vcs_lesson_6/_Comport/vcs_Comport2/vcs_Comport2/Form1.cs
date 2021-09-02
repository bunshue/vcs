using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Comport2
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
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }

            serialPort1.PortName = "COM4";
            serialPort1.BaudRate = 115200;
            serialPort1.Open();
            richTextBox1.Text += "已連線\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen == true)
            {
                serialPort1.Close();
            }
            richTextBox1.Text += "已離線\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                byte[] data = new byte[8];

                data[0] = (byte)'^';
                data[1] = (byte)'^';
                data[2] = (byte)'^';
                data[3] = (byte)'^';
                data[4] = (byte)'^';

                serialPort1.Write(data, 0, 5);
                richTextBox1.Text += "send message ok\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (serialPort1.IsOpen)
            {
                byte[] data = new byte[8];

                data[0] = (byte)'a';
                data[1] = (byte)'b';
                data[2] = (byte)'c';
                data[3] = (byte)'d';
                data[4] = (byte)'e';
                data[5] = (byte)'f';
                data[6] = (byte)'g';

                serialPort1.Write(data, 0, 7);
                richTextBox1.Text += "send message ok\n";
            }

        }


        private void button5_Click(object sender, EventArgs e)
        {
            int BytesToRead = 0;							//緩衝區內可接收資料數

            if (serialPort1.IsOpen)
            {
                //計算serialPort1中有多少位元組 
                BytesToRead = serialPort1.BytesToRead;
                richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";

                if (BytesToRead > 0)
                {
                    //richTextBox1.Text += "BytesToRead = " + BytesToRead.ToString() + "\n";



                    Byte[] receive_buffer = new Byte[2048];		//接收資料緩衝區

                    //serialPort1.Read(放置的位元陣列 , 從第幾個位置開始存放 , 共需存放多少位元)
                    serialPort1.Read(receive_buffer, 0, BytesToRead);

                    string input = "";
                    for (int i = 0; i < BytesToRead; i++)
                    {
                        input += (char)receive_buffer[i];
                    }

                    richTextBox1.Text += input + "\n";



                }
            }


        }

    }
}
