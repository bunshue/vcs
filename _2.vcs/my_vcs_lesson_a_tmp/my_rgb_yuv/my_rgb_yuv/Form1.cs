using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_rgb_yuv
{
    public partial class Form1 : Form
    {
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


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            bool conversionSuccessful = false;
            int rr = 0;
            int gg = 0;
            int bb = 0;

            conversionSuccessful = int.TryParse(textBox1.Text, out rr);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "rr： " + rr.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse R 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox2.Text, out gg);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "gg： " + gg.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse G 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox3.Text, out bb);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "bb： " + bb.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse B 失敗\n";
                return;
            }


            RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
            YUV yy = new YUV();
            yy = RGBToYUV(pp);
            richTextBox1.Text += "Y = " + yy.Y.ToString() + "\n";
            richTextBox1.Text += "U = " + yy.U.ToString() + "\n";
            richTextBox1.Text += "V = " + yy.V.ToString() + "\n";

        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

    }
}
