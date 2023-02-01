using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_Clock1
{
    public partial class Form1 : Form
    {
        bool flag_debug = false;
        int flag_operation_mode = MODE_0;

        private const int MODE_0 = 0x00;   //時間模式
        private const int MODE_1 = 0x01;   //碼表模式
        private const int MODE_2 = 0x02;   //離開
        private const int MODE_3 = 0x03;   //倒數計時
        private const int MODE_4 = 0x04;   //RGB模式
        private const int MODE_5 = 0x05;   //最上層切換

        int flag_stopwatch_mode = -1;
        private const int MODE_1a = 0x00;   //碼表模式a, 歸零, 等待開始
        private const int MODE_1b = 0x01;   //碼表模式b, 開始計數
        private const int MODE_1c = 0x02;   //碼表模式c, 暫停

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int W = 200;
        private const int H = 100;

        Color rgb_color = new Color();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            this.FormBorderStyle = FormBorderStyle.None;

            if (flag_debug == false)
            {
                this.Size = new Size(W, H);
            }
            else
            {

            }

            //int ScreenWidth = Screen.PrimaryScreen.Bounds.Width;
            //int ScreenHeight = Screen.PrimaryScreen.Bounds.Height;
            int ScreenWidth = Screen.PrimaryScreen.WorkingArea.Width;
            int ScreenHeight = Screen.PrimaryScreen.WorkingArea.Height;

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(ScreenWidth - this.Width, ScreenHeight - this.Height);
        }

        //Form1 initial location
        private const int FORM1_DEFAULT_POSITION_X = 600 - 10;
        private const int FORM1_DEFAULT_POSITION_Y = 700;
        int form1_position_x_old = FORM1_DEFAULT_POSITION_X;
        int form1_position_y_old = FORM1_DEFAULT_POSITION_Y;
        bool flag_form1_mouse_down = false;
        bool flag_form1_mouse_inside = false;

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_form1_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            form1_position_x_old = e.X;
            form1_position_y_old = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_form1_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - form1_position_x_old;
                int dy = e.Y - form1_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_form1_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - form1_position_x_old;
            int dy = e.Y - form1_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int linewidth = 6;
            Graphics g = e.Graphics;
            Brush b = new SolidBrush(Color.Blue);
            Font f = new Font("標楷體", 30, FontStyle.Bold);
            Pen p = new Pen(Brushes.Blue, linewidth);

            if (flag_form1_mouse_inside == true)
            {
                //richTextBox1.Text += "Y";
                //Point px1 = new Point(W * 10 / 100, H * 90 / 100);
                //Point px2 = new Point(W * 90 / 100, H * 90 / 100);
                Point px1 = new Point(0, H / 2);
                Point px2 = new Point(W, H / 2);
                g.DrawLine(new Pen(Brushes.Gray, 3), px1, px2);
                px1 = new Point(W * 1 / 3, 0);
                px2 = new Point(W * 1 / 3, H);
                g.DrawLine(new Pen(Brushes.Gray, 3), px1, px2);
                px1 = new Point(W * 2 / 3, 0);
                px2 = new Point(W * 2 / 3, H);
                g.DrawLine(new Pen(Brushes.Gray, 3), px1, px2);

                Font f2 = new Font("標楷體", 12);
                Brush b2 = new SolidBrush(Color.Red);
                g.DrawString(" 時鐘", f2, b2, W * 0 / 3, 10);
                g.DrawString(" 馬表", f2, b2, W * 1 / 3, 10);
                g.DrawString(" 離開", f2, b2, W * 2 / 3, 10);
                g.DrawString(" 倒計時", f2, b2, W * 0 / 3, H - 25);
                g.DrawString(" RGB", f2, b2, W * 1 / 3, H - 25);
                g.DrawString(" 最上層", f2, b2, W * 2 / 3, H - 25);

                //其他 全螢幕 雙倍螢幕
            }

            if ((flag_operation_mode == MODE_0) || (flag_operation_mode == MODE_3) || (flag_operation_mode == MODE_5))
            {
                //string dt = DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //string dt = DateTime.Now.ToString();
                //string dt = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                string dt = DateTime.Now.ToString("HH:mm:ss");

                g.DrawString(dt, f, b, 10, 28);
            }
            else if (flag_operation_mode == MODE_1)
            {
                g.DrawString(stopwatch_text, f, b, 10, 10);
            }
            else if (flag_operation_mode == MODE_4)
            {
                int x_st = 5;
                int y_st = 10;
                int dx = 48;
                int dy = 32;

                Brush rr = new SolidBrush(Color.Red);
                Brush gg = new SolidBrush(Color.Green);
                Brush bb = new SolidBrush(Color.Blue);
                Brush yy = new SolidBrush(Color.Gold);
                Brush uu = new SolidBrush(Color.Blue);
                Brush vv = new SolidBrush(Color.Red);

                Font frgb = new Font("標楷體", 20, FontStyle.Bold);

                g.DrawString(rgb_color.R.ToString(), frgb, rr, x_st + dx * 0, y_st + dy * 0);
                g.DrawString(rgb_color.G.ToString(), frgb, gg, x_st + dx * 1, y_st + dy * 0);
                g.DrawString(rgb_color.B.ToString(), frgb, bb, x_st + dx * 2, y_st + dy * 0);

                RGB pp = new RGB(rgb_color.R, rgb_color.G, rgb_color.B);
                YUV yyy = new YUV();
                yyy = RGBToYUV(pp);

                g.DrawString(((int)yyy.Y).ToString(), frgb, yy, x_st + dx * 0, y_st + dy * 1);
                g.DrawString(((int)yyy.U).ToString(), frgb, uu, x_st + dx * 1, y_st + dy * 1);
                g.DrawString(((int)yyy.V).ToString(), frgb, vv, x_st + dx * 2, y_st + dy * 1);

                frgb = new Font("標楷體", 14, FontStyle.Bold);
                Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
                g.DrawString("(" + pt.X.ToString() + ", " + pt.Y.ToString() + ")", frgb, gg, x_st + dx * 0, y_st + dy * 2 - 2);

                int w = 35;
                g.FillRectangle(new SolidBrush(rgb_color), W - w - 10, 10, w, H - 20);
            }

            g.DrawRectangle(p, linewidth / 2, linewidth / 2, W - linewidth, H - linewidth);
        }

        private void timer_clock_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "(" + e.X.ToString() + ", " + e.Y.ToString() + ") ";
            int xx = e.X;
            int yy = e.Y;
            if (yy < H / 2) //上排
            {
                if (xx < W / 3) //左
                {
                    richTextBox1.Text += "零 時間模式";
                    timer_clock.Enabled = true;
                    timer_stopwatch.Enabled = false;
                    timer_countdown.Enabled = false;
                    flag_operation_mode = MODE_0;
                    this.Invalidate();
                }
                else if (xx < W * 2 / 3) //中
                {
                    richTextBox1.Text += "一 碼表模式";
                    timer_clock.Enabled = false;
                    timer_stopwatch.Enabled = false;
                    timer_countdown.Enabled = false;
                    flag_operation_mode = MODE_1;

                    do_stopwatch();
                }
                else  //右
                {
                    richTextBox1.Text += "二 離開";
                    flag_operation_mode = MODE_2;
                    Application.Exit();
                }
            }
            else   //下排
            {
                if (xx < W / 3) //左
                {
                    richTextBox1.Text += "三 倒數計時";
                    flag_operation_mode = MODE_3;
                }
                else if (xx < W * 2 / 3) //中
                {
                    richTextBox1.Text += "四 RGB模式";
                    flag_operation_mode = MODE_4;
                }
                else  //右
                {
                    richTextBox1.Text += "五 最上層切換";
                    flag_operation_mode = MODE_5;
                    if (this.TopMost == false)
                        this.TopMost = true;
                    else
                        this.TopMost = false;
                }
            }

            if (flag_operation_mode != MODE_1)
            {
                flag_stopwatch_mode = -1;
            }
        }

        void do_stopwatch()
        {
            if (flag_stopwatch_mode == -1)
            {
                flag_stopwatch_mode = MODE_1a;  //歸零, 等待開始
                richTextBox1.Text += "歸零, 等待開始\n";
                stopwatch_text = "00:00:00.0";
                this.Invalidate();
            }
            else if (flag_stopwatch_mode == MODE_1a)
            {
                flag_stopwatch_mode = MODE_1b;  //開始計數
                richTextBox1.Text += "開始計數\n";
                timer_stopwatch.Enabled = true;
                StartTime = DateTime.Now;
            }
            else if (flag_stopwatch_mode == MODE_1b)
            {
                flag_stopwatch_mode = MODE_1c;  //暫停
                richTextBox1.Text += "暫停\n";
                timer_stopwatch.Enabled = false;
            }
            else if (flag_stopwatch_mode == MODE_1c)
            {
                flag_stopwatch_mode = MODE_1a;  //歸零, 等待開始
                richTextBox1.Text += "歸零, 等待開始\n";
                stopwatch_text = "00:00:00.0";
                this.Invalidate();
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXX\n";

            }

        }

        private DateTime StartTime;
        string stopwatch_text = "";
        private void timer_stopwatch_Tick(object sender, EventArgs e)
        {
            //碼表
            TimeSpan elapsed = DateTime.Now - StartTime;

            stopwatch_text = "";
            // Start with the days if greater than 0.
            if (elapsed.Days > 0)
            {
                stopwatch_text += elapsed.Days.ToString() + ".";
            }

            // Convert milliseconds into tenths of seconds.
            int tenths = elapsed.Milliseconds / 100;

            // Compose the rest of the elapsed time.
            stopwatch_text +=
                elapsed.Hours.ToString("00") + ":" +
                elapsed.Minutes.ToString("00") + ":" +
                elapsed.Seconds.ToString("00") + "." +
                tenths.ToString("0");
            this.Invalidate();
        }

        private void timer_countdown_Tick(object sender, EventArgs e)
        {
            //倒數計時

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
        static public byte GetAValue(uint color)
        {
            return ((byte)((color) >> 24));
        }

        public Color GetColor(Point screenPoint)
        {
            IntPtr displayDC = CreateDC("DISPLAY", null, null, IntPtr.Zero);
            uint colorref = GetPixel(displayDC, screenPoint.X, screenPoint.Y);
            DeleteDC(displayDC);
            byte Red = GetRValue(colorref);
            byte Green = GetGValue(colorref);
            byte Blue = GetBValue(colorref);
            return Color.FromArgb(Red, Green, Blue);
        }

        //int cccc = 0;
        //int total_RGB_R_old = -1;
        //int total_RGB_G_old = -1;
        //int total_RGB_B_old = -1;

        private void timer_rgb_Tick(object sender, EventArgs e)
        {
            /*
            if (flag_david_test3 == true)
                show_main_message1(Control.MousePosition.X.ToString() + "," + Control.MousePosition.Y.ToString(), S_FALSE, 30);
            */
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            rgb_color = GetColor(pt);
            this.Invalidate();

            /*
            if (flag_show_cmx_lenc_result == true)
            {
                lb_yuv_y2.Text = ((int)cl.R).ToString() + "\n" + ((int)cl.G).ToString() + "\n" + ((int)cl.B).ToString() + "\n" + ((int)yyy.Y).ToString();
            }
            else
            {
                lb_yuv_y2.Text = ((int)yyy.Y).ToString();
            }

            if (flag_check_webcam_signal == true)
            {
                cccc++;
                if ((cccc % 50) == 0)
                {
                    //richTextBox1.Text += "R " + total_RGB_R.ToString() + "    " + "G " + total_RGB_G.ToString() + "    " + "B " + total_RGB_B.ToString() + "\n";
                    if ((total_RGB_R == total_RGB_R_old) && (total_RGB_G == total_RGB_G_old) && (total_RGB_B == total_RGB_B_old))
                    {
                        //richTextBox1.Text += "refresh webcam\n";
                        //button12_Click_1(sender, e);
                    }
                    else
                    {
                        total_RGB_R_old = total_RGB_R;
                        total_RGB_G_old = total_RGB_G;
                        total_RGB_B_old = total_RGB_B;
                    }
                }
            }
             * */


        }

        private void Form1_MouseEnter(object sender, EventArgs e)
        {
            flag_form1_mouse_inside = true;

        }

        private void Form1_MouseLeave(object sender, EventArgs e)
        {
            flag_form1_mouse_inside = false;

        }
    }
}
