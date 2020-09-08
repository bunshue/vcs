using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RGB2YUV
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

            lb_y.Text = "Y";
            lb_u.Text = "U";
            lb_v.Text = "V";
            lb_r.Text = "R";
            lb_g.Text = "G";
            lb_b.Text = "B";
        }

        public static YUV RGBToYUV(RGB rgb)
        {
            double y = rgb.R * .299000 + rgb.G * .587000 + rgb.B * .114000;
            double u = rgb.R * -.168736 + rgb.G * -.331264 + rgb.B * .500000 + 128;
            double v = rgb.R * .500000 + rgb.G * -.418688 + rgb.B * -.081312 + 128;

            return new YUV(y, u, v);
        }

        public static RGB YUVToRGB(YUV yuv)
        {
            byte r = (byte)(yuv.Y + 1.4075 * (yuv.V - 128));
            byte g = (byte)(yuv.Y - 0.3455 * (yuv.U - 128) - (0.7169 * (yuv.V - 128)));
            byte b = (byte)(yuv.Y + 1.7790 * (yuv.U - 128));

            return new RGB(r, g, b);
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
                //richTextBox1.Text += "rr： " + rr.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse R 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox2.Text, out gg);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "gg： " + gg.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse G 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox3.Text, out bb);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "bb： " + bb.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse B 失敗\n";
                return;
            }

            RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
            YUV yy = new YUV();
            yy = RGBToYUV(pp);
            lb_y.Text = "Y = " + yy.Y.ToString();
            lb_u.Text = "U = " + yy.U.ToString();
            lb_v.Text = "V = " + yy.V.ToString();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            bool conversionSuccessful = false;
            int yy = 0;
            int uu = 0;
            int vv = 0;

            conversionSuccessful = int.TryParse(textBox4.Text, out yy);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "yy： " + yy.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse Y 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox5.Text, out uu);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "uu： " + uu.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse U 失敗\n";
                return;
            }

            conversionSuccessful = int.TryParse(textBox6.Text, out vv);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "vv： " + vv.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse V 失敗\n";
                return;
            }

            YUV yyy = new YUV(yy, uu, vv);
            RGB rrr = new RGB();
            rrr = YUVToRGB(yyy);
            lb_r.Text = "R = " + rrr.R.ToString();
            lb_g.Text = "G = " + rrr.G.ToString();
            lb_b.Text = "B = " + rrr.B.ToString();

        }
    }
}
