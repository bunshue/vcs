using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for Process, Stopwatch

namespace vcs_Draw8_Time
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        string filename = "C:\\______test_files\\vcs_reference2\\書頁\\2016122615573727.jpg";

        public struct RGB
        {
            private byte _r;
            private byte _g;
            private byte _b;

            public RGB(byte r, byte g, byte b)
            {
                this._r = r;
                this._g = g;
                this._b = b;
            }

            public byte R
            {
                get { return this._r; }
                set { this._r = value; }
            }

            public byte G
            {
                get { return this._g; }
                set { this._g = value; }
            }

            public byte B
            {
                get { return this._b; }
                set { this._b = value; }
            }

            public bool Equals(RGB rgb)
            {
                return (this.R == rgb.R) && (this.G == rgb.G) && (this.B == rgb.B);
            }
        }

        public struct YUV
        {
            private double _y;
            private double _u;
            private double _v;

            public YUV(double y, double u, double v)
            {
                this._y = y;
                this._u = u;
                this._v = v;
            }

            public double Y
            {
                get { return this._y; }
                set { this._y = value; }
            }

            public double U
            {
                get { return this._u; }
                set { this._u = value; }
            }

            public double V
            {
                get { return this._v; }
                set { this._v = value; }
            }

            public bool Equals(YUV yuv)
            {
                return (this.Y == yuv.Y) && (this.U == yuv.U) && (this.V == yuv.V);
            }
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "量測時間ST\t";
            if (rb1.Checked == true)
            {
                richTextBox1.Text += "黑白\n";
                label1.Text = "約耗時 21 秒, 目前無法中斷";
            }
            else if (rb2.Checked == true)
            {
                richTextBox1.Text += "測光\n";
                label1.Text = "約耗時 12 秒, 目前無法中斷";
            }
            else
                richTextBox1.Text += "其他\n";

            bitmap1 = new Bitmap(filename);
            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中

            delay(10);

            //g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            Stopwatch stopwatch = new Stopwatch();

            int w = bitmap1.Width;
            int h = bitmap1.Height;

            int xx;
            int yy;
            Color c;
            double y_total = 0;

            stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            for (yy = 0; yy < h; yy++)
            {
                for (xx = 0; xx < w; xx++)
                {
                    c = bitmap1.GetPixel(xx, yy);
                    if (rb1.Checked == true)
                    {
                        bitmap1.SetPixel(xx, yy, Color.FromArgb((c.R + c.G + c.B) / 3, (c.R + c.G + c.B) / 3, (c.R + c.G + c.B) / 3));
                    }
                    else if (rb2.Checked == true)
                    {
                        RGB pp = new RGB(c.R, c.G, c.B);
                        YUV yyy = new YUV();
                        yyy = RGBToYUV(pp);
                        y_total += yyy.Y;
                    }
                    else
                    {

                    }
                }
            }

            // Stop timing
            stopwatch.Stop();

            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中

            if (rb2.Checked == true)
                richTextBox1.Text += "亮度 : " + (y_total / (w * h)).ToString() + "\n";

            richTextBox1.Text += "總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
            label1.Text = "完成, 總時間 : " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
