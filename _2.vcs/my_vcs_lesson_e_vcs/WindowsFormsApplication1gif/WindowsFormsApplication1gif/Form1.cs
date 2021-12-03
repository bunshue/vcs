using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;

using System.Drawing.Imaging;
using System.IO;

using System.Data.OleDb;

using System.Diagnostics;


using System.IO.Ports;
using System.Threading;

using System.Runtime.InteropServices;

namespace WindowsFormsApplication1gif
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_case1\_case1a\_case1aa\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            //string filename = @"C:\______test_files\picture1.jpg";

            var GetFileName = Path.GetFileName(filename);
            var GetFileNameWithoutExtension = Path.GetFileNameWithoutExtension(filename);
            var GetDirectoryName = Path.GetDirectoryName(filename);
            var GetFullPath = Path.GetFullPath(filename);

            //richTextBox1.Text += "filename\t" + filename + "\n";
            richTextBox1.Text += "GetFullPath\t" + GetFullPath + "\n";
            richTextBox1.Text += "GetDirectoryName\t" + GetDirectoryName + "\n";
            //richTextBox1.Text += "GetFileName\t" + GetFileName + "\n";
            richTextBox1.Text += "GetFileNameWithoutExtension\t" + GetFileNameWithoutExtension + "\n";

            label1.Text = "原檔名 :";
            textBox1.Text = filename;

            label2.Text = "檔名 :";
            textBox2.Text = GetFileNameWithoutExtension;

            label3.Text = "新檔名 :";
            textBox3.Text = GetFileNameWithoutExtension;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bmp = new Bitmap(300, 200);
            Graphics g = Graphics.FromImage(bmp);
            Font f = new Font("arial", 11f);
            Brush b = Brushes.Blue;

            string txt = "Rotate text animation!";
            SizeF sz = g.MeasureString(txt, f);
            g.Clear(Color.WhiteSmoke);
            g.DrawString(txt, f, b, 50 - sz.Width / 2, 50 - sz.Height / 2);
            g.Flush();

            for (int i = 1; i < 36; ++i)
            {
                g.Clear(Color.WhiteSmoke);
                g.TranslateTransform(50, 50);
                g.RotateTransform(10f * i);
                g.DrawString(txt, f, b, sz.Width / -2, sz.Height / -2);
                g.ResetTransform();
                g.DrawString("Hello", f, Brushes.Red, -50 + i * 4, 20);
                g.DrawString("Yeah", f, Brushes.Orange, 60, -20 + i * 4);

                g.Flush();

                pictureBox1.Image = bmp;
                Application.DoEvents();
                delay(300);
            }

            f.Dispose();
            g.Dispose();
            bmp.Dispose();

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
            //動態處理DataTable
            //動態處理DataTable

            //1.創建表實例
            DataTable dt = new DataTable();

            //2.建立表結構
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.創建新行
            DataRow dr = dt.NewRow();

            //4.為新行賦值
            dr[0] = "1";
            dr[1] = "林林";

            //5.將新行添加到表
            dt.Rows.Add(dr);


            /*
            //1.創建表實例
            DataTable dt=new DataTable();

            //2.建立表結構
            dt.Columns.Add("ID");
            dt.Columns.Add("Name");

            //3.添加新行
            dt.Rows.Add("1", "Name");
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {


        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            var ext = Path.GetExtension(filename);


            richTextBox1.Text += "副檔名 : " + ext + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            var GetFileName = Path.GetFileName(filename);
            var GetFileNameWithoutExtension = Path.GetFileNameWithoutExtension(filename);
            var GetExtension = Path.GetExtension(filename);
            var GetDirectoryName = Path.GetDirectoryName(filename);
            var GetFullPath = Path.GetFullPath(filename);

            richTextBox1.Text += "GetFullPath\t" + GetFullPath + "\n";
            richTextBox1.Text += "GetDirectoryName\t" + GetDirectoryName + "\n";
            richTextBox1.Text += "GetFileName\t" + GetFileName + "\n";
            richTextBox1.Text += "GetFileNameWithoutExtension\t" + GetFileNameWithoutExtension + "\n";
            richTextBox1.Text += "GetExtension\t" + GetExtension + "\n";



            richTextBox1.Text += "新全檔名 : " + GetDirectoryName + "\\" + textBox3.Text + GetExtension + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            int lower = 0x20;
            int upper = 0xD7FF;

            string result = NextString(lower, upper, 30);
            richTextBox1.Text += result + "\n";

        }

        public string NextString(int charLowerBound, int charUpperBound, int length)
        {
            Random r = new Random();
            return new String(
                Enumerable.Repeat(0, length)
                    .Select(p => (char)r.Next(charLowerBound, charUpperBound))
                    .ToArray());
        }


        //计算两点GPS坐标距离 
        /// <summary>
        ///计算两点GPS坐标的距离
        /// </summary>
        /// <param name="n1">第一点的纬度坐标</param>
        /// <param name="e1">第一点的经度坐标</param>
        /// <param name="n2">第二点的纬度坐标</param>
        /// <param name="e2">第二点的经度坐标</param>
        /// <returns></returns>
        public static double Distance(double n1, double e1, double n2, double e2)
        {
            double jl_jd = 102834.74258026089786013677476285;   // 米/度
            double jl_wd = 111712.69150641055729984301412873;   // 米/度
            double b = Math.Abs((e1 - e2) * jl_jd);
            double a = Math.Abs((n1 - n2) * jl_wd);
            return Math.Sqrt((a * a + b * b));
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }


        //鼠標點擊按鈕拖動窗體

        //記錄窗體的X坐標 
        private int startX;

        //記錄窗體的Y坐標 
        private int startY;

        private void button8_MouseDown(object sender, MouseEventArgs e)
        {
            //判斷點擊的是不是左鍵 
            if (e.Button == MouseButtons.Left)
            {
                //得到窗體的X值 
                startX = e.X;

                //得到窗體的Y值 
                startY = e.Y;
            }
        }

        private void button8_MouseMove(object sender, MouseEventArgs e)
        {
            //判斷點擊的是不是左鍵 
            if (e.Button == MouseButtons.Left)
            {
                //重新繪制窗體X 
                this.Left += e.X - startX;

                //重新繪制窗體Y 
                this.Top += e.Y - startY;
            }
        }
    }
}