using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for dll

namespace vcs_ColorAnalysis2
{
    public partial class Form1 : Form
    {
        bool flag_small_mode = false;

        Bitmap bitmap1;
        Graphics g;
        Graphics g_mesg;
        Font f;
        Bitmap bmp;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.TopMost = true;

            if (flag_small_mode == true)
            {
                //checkBox1.Visible = false;
                panel1.Visible = false;
                //txtColor.Visible = false;
                //txtPoint.Visible = false;
                //txtRGB.Visible = false;

                //設定執行後的表單起始位置
                this.StartPosition = FormStartPosition.Manual;
                if (Screen.PrimaryScreen.Bounds.Width < 1920)
                    this.Location = new System.Drawing.Point(850, 0);  //SD
                else
                    this.Location = new System.Drawing.Point(1200, 0);  //FHD

                this.FormBorderStyle = FormBorderStyle.None;

                //this.Size = new Size(240, 80);

                g_mesg = this.CreateGraphics();
            }
            this.BackColor = Color.DarkGreen;
            g_mesg = this.CreateGraphics();

            pictureBox1.Size = new Size(640 + 50, 480 + 50);
            pictureBox1.Image = vcs_ColorAnalysis2.Properties.Resources.test_yuv;
            bitmap1 = (Bitmap)pictureBox1.Image;
            g = Graphics.FromImage(bitmap1);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            button1.Location = new Point(this.pictureBox1.Location.X + this.pictureBox1.Width - 130, 10);

            //設定執行後的表單起始位置

            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(100, 100);
        }

        /*
        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked == true)
            {
                this.TopMost = true;
            }
            else
            {
                this.TopMost = false;
            }
        }
        */

        [DllImport("gdi32.dll")]
        static public extern uint GetPixel(IntPtr hDC, int XPos, int YPos);
        [DllImport("gdi32.dll")]
        static public extern IntPtr CreateDC(string driverName, string deviceName, string output, IntPtr lpinitData);
        [DllImport("gdi32.dll")]
        static public extern bool DeleteDC(IntPtr DC);

        static public byte GetRValue(uint color)
        {
            return (byte)color;
        }

        static public byte GetGValue(uint color)
        {
            return ((byte)(((short)(color)) >> 8));
        }

        static public byte GetBValue(uint color)
        {
            return ((byte)((color) >> 16));
        }

        public Color GetColor(Point pt)
        {
            IntPtr hdc = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint pixel = GetPixel(hdc, pt.X, pt.Y);
            DeleteDC(hdc);

            byte Red = (byte)(pixel & 0x000000FF);
            byte Green = (byte)((pixel & 0x0000FF00) >> 8);
            byte Blue = (byte)((pixel & 0x00FF0000) >> 16);

            return Color.FromArgb(Red, Green, Blue);
        }

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

        int cnt = 0;
        Brush b = new SolidBrush(Color.White);
        Color cl_old;

        private void timer1_Tick(object sender, EventArgs e)
        {
            //if (flag_small_mode == true)
            {
                int offset_x = 50;
                Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                Color cl = GetColor(pt);
                if (cl_old != cl)
                {
                    //this.Size = new Size(240, 80);
                    cnt = 0;
                    g_mesg.Clear(BackColor);

                    g_mesg.DrawString(cl.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(offset_x + 5, 0));
                    g_mesg.DrawString(cl.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Lime), new PointF(offset_x + 5 + 75, 0));
                    g_mesg.DrawString(cl.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(offset_x + 5 + 150, 0));

                    cl_old = cl;

                    int rr = cl.R;
                    int gg = cl.G;
                    int bb = cl.B;

                    RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
                    YUV yy = new YUV();
                    yy = RGBToYUV(pp);

                    g_mesg.DrawString(((int)yy.Y).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Gold), new PointF(offset_x + 5, 35));
                    //g.DrawString(((int)yy.U).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 75, 35));
                    //g.DrawString(((int)yy.V).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5 + 150, 35));
                }
                else
                {
                    cnt++;
                    if ((cnt > 25) && (cnt % 5) == 0)
                    {
                        //this.Size = new Size(240, 55);
                        g_mesg.Clear(BackColor);
                        g_mesg.DrawString(DateTime.Now.ToString("HH:mm:ss"), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(offset_x + 20, 5));
                    }
                }
            }
            //else
            {
                //txtPoint.Text = Control.MousePosition.X.ToString() + ", " + Control.MousePosition.Y.ToString();
                Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                Color cl = GetColor(pt);
                panel1.BackColor = cl;
                //txtRGB.Text = cl.R.ToString() + ", " + cl.G.ToString() + ", " + cl.B.ToString();
                //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();
            }
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************
        #region 移動無邊框表單
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }

        }
        #endregion

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void pictureBox1_MouseHover(object sender, EventArgs e)
        {
            //richTextBox1.Text += 
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += e.X.ToString() + ", " + e.Y.ToString() + "  ";

            //if (flag_small_mode == true)
            {
                int offset_x = 120;
                Point pt = new Point(e.X, e.Y);
                //Color cl = GetColor(pt); //wrong
                Color cl = bitmap1.GetPixel(e.X, e.Y);

                if (cl_old != cl)
                {
                    //this.Size = new Size(240, 80);
                    cnt = 0;
                    g_mesg.Clear(BackColor);

                    g_mesg.DrawString(cl.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(offset_x + 5, 0));
                    g_mesg.DrawString(cl.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Lime), new PointF(offset_x + 5 + 75, 0));
                    g_mesg.DrawString(cl.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(offset_x + 5 + 150, 0));

                    cl_old = cl;

                    int rr = cl.R;
                    int gg = cl.G;
                    int bb = cl.B;

                    RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
                    YUV yy = new YUV();
                    yy = RGBToYUV(pp);

                    g_mesg.DrawString(((int)yy.Y).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Gold), new PointF(offset_x + 5, 35));
                    //g.DrawString(((int)yy.U).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 75, 35));
                    //g.DrawString(((int)yy.V).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5 + 150, 35));
                }
                else
                {
                    cnt++;
                    if ((cnt > 25) && (cnt % 5) == 0)
                    {
                        //this.Size = new Size(240, 55);
                        g_mesg.Clear(BackColor);
                        g_mesg.DrawString(DateTime.Now.ToString("HH:mm:ss"), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(offset_x + 20, 5));
                    }
                }
            }
            //else
            {
                //txtPoint.Text = Control.MousePosition.X.ToString() + ", " + Control.MousePosition.Y.ToString();
                Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                Color cl = GetColor(pt);
                panel1.BackColor = cl;
                ///txtRGB.Text = cl.R.ToString() + ", " + cl.G.ToString() + ", " + cl.B.ToString();
                //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();
            }


                
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Point[] points = new Point[7];
            points[0] = new Point(615, 255);
            points[1] = new Point(314, 260);
            points[2] = new Point(331, 285);
            points[3] = new Point(13, 276);
            points[4] = new Point(8, 270);
            points[5] = new Point(613, 250);
            points[6] = new Point(10, 273);

            int len = points.Length;
            for (int i = 0; i < len; i++)
            {
                Color pt = bitmap1.GetPixel(points[i].X, points[i].Y);
                richTextBox1.Text += "i = " + i.ToString() + "\t";
                richTextBox1.Text += points[i].X.ToString() + ", " + points[i].Y.ToString() + "\t";
                richTextBox1.Text += pt.R.ToString() + ", " + pt.G.ToString() + ", " + pt.B.ToString() + "\t";
                RGB pp = new RGB(pt.R, pt.G, pt.B);
                YUV yyy = new YUV();
                yyy = RGBToYUV(pp);
                richTextBox1.Text += "Y = " + ((int)(yyy.Y)).ToString() + "\n";

                g.DrawEllipse(Pens.White, points[i].X, points[i].Y, 20, 20);

                //g.DrawEllipse(new Pen(Color.FromArgb(255, 255, (j / 2) % 256, (j / 2) % 256), 1), i, j, 1, 1);

            }

            pictureBox1.Image = bitmap1;

        }

    }
}
