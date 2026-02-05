using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for dll

namespace vcs_ColorPicker1
{
    public partial class Form1 : Form
    {
        bool flag_show_alpha = false;

        Graphics g;
        Font f;
        Bitmap bmp;

        bool flag_measure_8_points = false;  // false : 一般模式, true : 量測8點模式
        bool flag_no_update = false;
        bool flag_recording_point1 = false;
        bool flag_recording_point2 = false;
        int record_time1 = 0;
        int record_time2 = 0;
        Point pt_st;
        Point pt_sp;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //表單 連結 ContextMenuStrip (快捷功能表 / 右鍵選單)
            this.ContextMenuStrip = contextMenuStrip1;

            this.TopMost = true;

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            if (Screen.PrimaryScreen.Bounds.Width < 1920)
                this.Location = new System.Drawing.Point(850, 0);  //SD
            else
                this.Location = new System.Drawing.Point(1200, 0);  //FHD

            this.FormBorderStyle = FormBorderStyle.None;

            if (flag_measure_8_points == false)  // 一般模式
            {
                this.Size = new Size(240, 80);  // 一般模式
            }
            else
            {
                this.Size = new Size(240, 300);  // 量測8點模式
            }

            g = this.CreateGraphics();
        }

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
            if (flag_no_update == true)
            {
                return;
            }

            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);

            if (flag_measure_8_points == false)  // 一般模式
            {
                if (cl_old != cl)
                {
                    cnt = 0;
                    g.Clear(BackColor);

                    g.DrawString(cl.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5, 75 * 0));
                    g.DrawString(cl.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Lime), new PointF(5 + 75 * 1, 0));
                    g.DrawString(cl.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 75 * 2, 0));
                    if (flag_show_alpha == true)
                    {
                        this.Size = new Size(240 + 70, 80);
                        g.DrawString(cl.A.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 75 * 3, 0));
                    }
                    else
                    {
                        this.Size = new Size(240, 80);
                    }

                    cl_old = cl;

                    int rr = cl.R;
                    int gg = cl.G;
                    int bb = cl.B;

                    RGB pp = new RGB((byte)rr, (byte)gg, (byte)bb);
                    YUV yy = new YUV();
                    yy = RGBToYUV(pp);

                    g.DrawString(((int)yy.Y).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Yellow), new PointF(5, 35));
                    g.DrawString(((int)yy.U).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 75, 35));
                    g.DrawString(((int)yy.V).ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5 + 150, 35));
                }
                else
                {
                    cnt++;
                    if ((cnt > 25) && (cnt % 5) == 0)
                    {
                        this.Size = new Size(240, 55);
                        g.Clear(BackColor);
                        g.DrawString(DateTime.Now.ToString("HH:mm:ss"), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(20, 5));
                    }
                }
            }
            else  // 量測8點模式
            {
                g.Clear(BackColor);
                g.DrawRectangle(new Pen(Color.Gray, 20), 0, 0, this.ClientSize.Width, this.ClientSize.Height);

                g.DrawString(cl.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5, 0));
                g.DrawString(cl.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Lime), new PointF(5 + 75, 0));
                g.DrawString(cl.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 150, 0));

                if ((flag_recording_point1 == false) && (flag_recording_point2 == false))
                {
                    g.DrawString("選取第一點", new Font("Consolas", 18), new SolidBrush(Color.Magenta), new PointF(15, 0 + 46));
                    g.DrawString(cnt.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Cyan), new PointF(5 + 160, 0 + 34));
                    g.DrawString("20", new Font("Consolas", 30), new SolidBrush(Color.Cyan), new PointF(5 + 160, 0 + 34 + 34));
                }
                if ((flag_recording_point1 == true) && (flag_recording_point2 == false))
                {
                    g.DrawString("選取第二點", new Font("Consolas", 18), new SolidBrush(Color.Magenta), new PointF(15, 0 + 46));
                    g.DrawString(cnt.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Cyan), new PointF(5 + 160, 0 + 34));
                    g.DrawString("20", new Font("Consolas", 30), new SolidBrush(Color.Cyan), new PointF(5 + 160, 0 + 34 + 34));
                }

                if ((flag_recording_point1 == true) && (flag_recording_point2 == false))
                {
                    g.DrawRectangle(new Pen(Color.Red, 20), 0, 0, this.ClientSize.Width, this.ClientSize.Height);
                }
                if ((flag_recording_point1 == true) && (flag_recording_point2 == true))
                {
                    g.DrawRectangle(new Pen(Color.Green, 20), 0, 0, this.ClientSize.Width, this.ClientSize.Height);
                }

                if (flag_recording_point1 == false)
                {
                    if (cl_old == cl)
                    {
                        cnt++;
                    }
                    else
                    {
                        cnt = 0;
                    }

                    //if ((cl.R > 230) && (cl.G > 230) && (cl.B > 230))
                    if (cnt > 20)
                    {
                        record_time1++;
                        g.DrawRectangle(new Pen(Color.FromArgb((record_time1 * 12) % 256, 255, 0, 0), 20), 0, 0, this.ClientSize.Width, this.ClientSize.Height);
                        //if (record_time1 >= 20)
                        {
                            flag_recording_point1 = true;
                            pt_st = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                            cnt = 0;
                        }
                    }
                    else
                    {
                        record_time1 = 0;
                    }
                }

                if ((flag_recording_point1 == true) && (flag_recording_point2 == false))
                {
                    if (cl_old == cl)
                    {
                        cnt++;
                    }
                    else
                    {
                        cnt = 0;
                    }

                    //if ((cl.R < 20) && (cl.G < 20) && (cl.B < 20))
                    if (cnt > 20)
                    {
                        record_time2++;
                        g.DrawRectangle(new Pen(Color.FromArgb((record_time2 * 12) % 256, 0, 255, 0), 20), 0, 0, this.ClientSize.Width, this.ClientSize.Height);
                        //if (record_time2 >= 20)
                        {
                            flag_recording_point2 = true;
                            pt_sp = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                        }
                    }
                    else
                    {
                        record_time2 = 0;
                    }
                }

                if ((flag_recording_point1 == true) && (flag_recording_point2 == true))
                {
                    int x_st = pt_st.X;
                    int dx = (pt_sp.X - pt_st.X) / 7;
                    int dy = 36;
                    g.Clear(BackColor);
                    g.DrawRectangle(new Pen(Color.Green, 20), 0, 0, this.ClientSize.Width, this.ClientSize.Height);

                    for (int i = 0; i < 8; i++)
                    {
                        Point p = new Point(x_st + dx * i, pt_st.Y);
                        Color c = GetColor(p);
                        g.DrawString(c.R.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Red), new PointF(5, 0 + i * dy));
                        g.DrawString(c.G.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Lime), new PointF(5 + 75, 0 + i * dy));
                        g.DrawString(c.B.ToString(), new Font("Consolas", 30), new SolidBrush(Color.Blue), new PointF(5 + 150, 0 + i * dy));
                    }
                    flag_no_update = true;
                }
                cl_old = cl;
            }
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            if (flag_measure_8_points == false)  // 一般模式
            {
                Application.Exit();
            }
            else  // 量測8點模式
            {
                flag_no_update = false;
                flag_recording_point1 = false;
                flag_recording_point2 = false;
                record_time1 = 0;
                record_time2 = 0;
            }
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

        private void toolStripMenuItem1a_Click(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem1b_Click(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem1c_Click(object sender, EventArgs e)
        {
            toolStripMenuItem1c.Checked = !toolStripMenuItem1c.Checked;
            flag_show_alpha = toolStripMenuItem1c.Checked;
            if (flag_show_alpha == true)
            {
                this.Size = new Size(240 + 70, 80);
                g = this.CreateGraphics();
            }
            else
            {
                this.Size = new Size(240, 80);
                g = this.CreateGraphics();
            }
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
