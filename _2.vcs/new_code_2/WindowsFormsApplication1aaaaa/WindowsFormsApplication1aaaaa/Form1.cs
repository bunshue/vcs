using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace WindowsFormsApplication1aaaaa
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
            Bitmap bmp = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            pictureBox1.Image = bmp;



            double x;
            double y;

            y = 11;
            x = Math.Sqrt(100 - y * y);

            richTextBox1.Text += "type " + typeof(int) + "\n";
            richTextBox1.Text += "type " + x.GetType() + "\n";
            richTextBox1.Text += "type " + x.ToString() + "\n";



            if (x.ToString() == "非數值")
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXx\n";
            }
            richTextBox1.Text += "x = " + x.ToString() + "\ty = " + y.ToString() + "\n\n\n";

            if (x == Double.NaN)
                richTextBox1.Text += "YYYYYY\n";

            try
            {
                x = Math.Sqrt(100 - y * y);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
            }
            richTextBox1.Text += "x = " + x.ToString() + "\ty = " + y.ToString() + "\n";


            //richTextBox1.Text += "sqrt minus = " + Math.Sqrt(-9) + "\n";



            int r = 50;
            double i;
            double j;

            x = 0;
            y = Math.Sqrt(r * r - x * x);

            double y_max = y;
            double y_min = -y;
            double x_max;
            double x_min;

            richTextBox1.Text += "y_min = " + y_min.ToString() + "\ty_max = " + y_max.ToString() + "\n";

            for (j = y_max; j >= y_min; j--)
            {
                x = Math.Sqrt(r * r - j * j);
                x_max = x;
                x_min = -x;
                //richTextBox1.Text += "y = " + j.ToString() + "\tx_min = " + x_min.ToString() + "\tx_max = " + x_max.ToString() + "\n";
                for (i = x_min; i <= x_max; i++)
                {
                    //richTextBox1.Text += "y = " + j.ToString() + "\tx_min = " + x_min.ToString() + "\tx_max = " + x_max.ToString() + "\n";
                    //richTextBox1.Text += "x = " + i.ToString() + "\tx_min = " + x_min.ToString() + "\tx_max = " + x_max.ToString() + "\n";
                    //richTextBox1.Text += "(" + i.ToString() + "," + j.ToString() + ") ";
                    //richTextBox1.Text += "(" + ((int)i).ToString() + "," + ((int)j).ToString() + ") ";


                    g.DrawEllipse(Pens.Red, (int)i + r, +r * 2 - (int)j, 1, 1);
                    pictureBox1.Image = bmp;
                    //delay(1);
                    Application.DoEvents();


                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Byte[] _data = new Byte[] { 0x02, 0x03, 0x00, 0x02, 0x00, 0x22 };     //result : 0x20 0x64
            //Byte[] _data = new Byte[] { 0x00, 0x06, 0x00, 0x02, 0x03, 0x55 };       //result : 0x14 0xE9

            //_data = System.Text.Encoding.Default.GetBytes(input);  
            UInt16 CRC = ModRTU_CRC(_data, 6);
            string hexValue = CRC.ToString("X2");

            string loCRC = "";
            string hiCRC = "";
            if (hexValue.Length == 3)
            {
                loCRC = hexValue.Substring(1, 2); //crc low byte   
                hiCRC = hexValue.Substring(0, 1); //crc high byte  
            }
            else
            {
                loCRC = hexValue.Substring(2, 2); //crc low byte   
                hiCRC = hexValue.Substring(0, 2); //crc high byte  
            }


            richTextBox1.Text += "result\thi = 0x" + hiCRC + "\t";
            richTextBox1.Text += "lo = 0x" + loCRC + "\n";
        }

        // 計算 MODBUS RTU CRC  
        UInt16 ModRTU_CRC(byte[] buf, int len)
        {
            UInt16 crc = 0xFFFF;

            for (int pos = 0; pos < len; pos++)
            {
                crc ^= (UInt16)buf[pos];          // 取出第一個byte與crc XOR

                for (int i = 8; i != 0; i--)
                {    // 巡檢每個bit  
                    if ((crc & 0x0001) != 0)
                    {      // 如果 LSB = 1   
                        crc >>= 1;                    // 右移1bit 並且 XOR 0xA001  
                        crc ^= 0xA001;
                    }
                    else                            // 如果 LSB != 1  
                        crc >>= 1;                    // 右移1bit
                }
            }

            return crc;
        }



    }
}