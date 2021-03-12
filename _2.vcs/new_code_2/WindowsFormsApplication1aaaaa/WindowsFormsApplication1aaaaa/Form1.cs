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


    }
}