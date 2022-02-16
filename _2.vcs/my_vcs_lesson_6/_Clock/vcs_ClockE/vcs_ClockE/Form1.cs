using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

//Form1屬性的BackColor改成Color.White
//Form1屬性的TransparencyKey改成Color.White

namespace vcs_ClockE
{
    public partial class Form1 : Form
    {
        //移動無邊框窗體 ST
        [DllImport("user32.dll")]
        public static extern bool ReleaseCapture();
        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);
        public const int WM_SYSCOMMAND = 0x0112;
        public const int SC_MOVE = 0xF010;
        public const int HTCAPTION = 0x0002;
        //移動無邊框窗體 SP

        int R = 100;
        int total_time = 10;
        int remaining_time = 6;
        bool flag_draw_countdown = true;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.ClientSize = new Size(R * 2, R * 2);

            this.FormBorderStyle = FormBorderStyle.None;
            this.TransparencyKey = Color.White;

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);
            this.TopMost = true;
            //this.Invalidate();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();

            current_value--;
            if (current_value <= 0)
            {
                flag_draw_countdown = false;
            }
        }

        int current_value = 360;
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Pen p;
            
            p = new Pen(Color.Red, 2);

            //e.Graphics.DrawRectangle(p, this.ClientRectangle);

            int linewidth = 10;
            p = new Pen(Color.Lime, linewidth);
            e.Graphics.DrawEllipse(p, linewidth, linewidth, R * 2 - linewidth * 2, R * 2 - linewidth * 2);

            SolidBrush sb = new SolidBrush(Color.Blue);
            Font f = new Font("標楷體", 26);
            string current_time = DateTime.Now.ToString("HH:mm:ss");
            int tmp_width = 0;
            int tmp_height = 0;

            tmp_width = e.Graphics.MeasureString(current_time, f).ToSize().Width;
            tmp_height = e.Graphics.MeasureString(current_time, f).ToSize().Height;

            e.Graphics.DrawString(current_time, f, sb, new PointF((R * 2 - tmp_width) / 2, (R * 2 - tmp_height) / 2));

            p = new Pen(Color.Red, 2);
            //e.Graphics.DrawRectangle(p, (R * 2 - tmp_width) / 2, (R * 2 - tmp_height) / 2,tmp_width,tmp_height);

            e.Graphics.DrawArc(new Pen(Color.Green, 5), new Rectangle(linewidth, linewidth, R * 2 - linewidth * 2, R * 2 - linewidth * 2), current_value - 90, -current_value);

        }

        //移動無邊框窗體 ST
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            ReleaseCapture();
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0);
        }
        //移動無邊框窗體 SP
    }
}

