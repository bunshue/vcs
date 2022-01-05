using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyToolbox
{
    public partial class Form1 : Form
    {
        //自動隱藏頁面 ST
        internal AnchorStyles StopAnhor = AnchorStyles.None;
        private void mStopAnhor()
        {
            if (this.Top <= 0)
            {
                StopAnhor = AnchorStyles.Top;
            }
            else if (this.Left <= 0)
            {
                StopAnhor = AnchorStyles.Left;
            }
            else if (this.Right >= Screen.PrimaryScreen.Bounds.Width)
            {
                StopAnhor = AnchorStyles.Right;
            }
            else
            {
                StopAnhor = AnchorStyles.None;
            }
        }

        private void Form1_LocationChanged(object sender, EventArgs e)
        {
            this.mStopAnhor();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.Bounds.Contains(Cursor.Position))
            {
                switch (this.StopAnhor)
                {
                    case AnchorStyles.Top:
                        this.Location = new Point(this.Location.X, 0);
                        break;
                    case AnchorStyles.Left:
                        this.Location = new Point(0, this.Location.Y);
                        break;
                    case AnchorStyles.Right:
                        this.Location = new Point(Screen.PrimaryScreen.Bounds.Width - this.Width, this.Location.Y);
                        break;
                }
            }
            else
            {
                switch (this.StopAnhor)
                {
                    case AnchorStyles.Top:
                        this.Location = new Point(this.Location.X, (this.Height - 4) * (-1));
                        break;
                    case AnchorStyles.Left:
                        this.Location = new Point((this.Width - 4) * (-1), this.Location.Y);
                        break;
                    case AnchorStyles.Right:
                        this.Location = new Point(Screen.PrimaryScreen.Bounds.Width - 4, this.Location.Y);
                        break;
                }
            }
        }
        //自動隱藏頁面 SP

        //要增加到頁面的控件
        Button btn_00 = new Button();
        Button btn_01 = new Button();
        Button btn_02 = new Button();
        Button btn_20 = new Button();
        Button btn_21 = new Button();
        Button btn_22 = new Button();
        PictureBox pbx_clock = new PictureBox();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            add_my_toolbox_controls();
        }

        void show_item_location()
        {
            //int W = Screen.PrimaryScreen.Bounds.Width;
            //int H = Screen.PrimaryScreen.Bounds.Height;
            //this.Size = new Size(W / 4, H * 4 / 5);

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(1900, 100);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
        }

        void add_my_toolbox_controls()
        {
            int x_st = 20;
            int y_st = 20;
            int dx = 0;
            int dy = 0;
            //int offset = 0;
            int w = 0;  //控件寬度
            int h = 0;  //控件高度

            // 實例化控件

            w = 380;
            h = 160;
            pbx_clock.Width = w;
            pbx_clock.Height = h;
            pbx_clock.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pbx_clock.BackColor = Color.Red;
            pbx_clock.Paint += pbx_clock_Paint;	// 加入事件
            this.Controls.Add(pbx_clock);	// 將控件加入表單

            //pbx_clock

            x_st = 20;
            y_st = 200;

            w = 120;
            h = 120;

            dx = w + 20;
            dy = h + 20;

            btn_00.Width = w;
            btn_00.Height = h;
            btn_00.Text = "Write";
            btn_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            //btn_00.Click += btn_cmx_click;	// 加入事件
            this.Controls.Add(btn_00);	// 將控件加入表單

            btn_01.Width = w;
            btn_01.Height = h;
            btn_01.Text = "Write";
            btn_01.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            //btn_01.Click += btn_cmx_click;	// 加入事件
            this.Controls.Add(btn_01);	// 將控件加入表單

            btn_02.Width = w;
            btn_02.Height = h;
            btn_02.Text = "Write";
            btn_02.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            //btn_02.Click += btn_cmx_click;	// 加入事件
            this.Controls.Add(btn_02);	// 將控件加入表單

            btn_20.Width = w;
            btn_20.Height = h;
            btn_20.Text = "Write";
            btn_20.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            //btn_20.Click += btn_cmx_click;	// 加入事件
            this.Controls.Add(btn_20);	// 將控件加入表單

            btn_21.Width = w;
            btn_21.Height = h;
            btn_21.Text = "Write";
            btn_21.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            //btn_21.Click += btn_cmx_click;	// 加入事件
            this.Controls.Add(btn_21);	// 將控件加入表單

            btn_22.Width = w;
            btn_22.Height = h;
            btn_22.Text = "Write";
            btn_22.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            //btn_22.Click += btn_cmx_click;	// 加入事件
            this.Controls.Add(btn_22);	// 將控件加入表單

            int W = w * 3 + 20 * 4 + 20;
            int H = Screen.PrimaryScreen.Bounds.Height;
            this.Size = new Size(W, H * 4 / 5);
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void timer_clock_Tick(object sender, EventArgs e)
        {
            pbx_clock.Invalidate();
        }

        private void pbx_clock_Paint(object sender, PaintEventArgs e)
        {
            int hh = DateTime.Now.Hour;
            int mm = DateTime.Now.Minute;
            int ss = DateTime.Now.Second;

            int x_st = 30;
            int y_st = 30;
            int w = 100;
            int h = 100;
            int dx = 10;

            int i;
            for (i = 0; i < 3; i++)
            {
                e.Graphics.FillRectangle(new SolidBrush(Color.Black), x_st + (w + dx) * i, y_st, w, h);
            }

            e.Graphics.DrawLine(new Pen(Color.Red, 6), x_st, y_st + h / 2, x_st + 380, y_st + h / 2);

            int dy = 15;
            e.Graphics.DrawString(hh.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st, y_st + dy);
            e.Graphics.DrawString(mm.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st + (w + dx) * 1, y_st + dy);
            e.Graphics.DrawString(ss.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st + (w + dx) * 2, y_st + dy);
        }
    }
}
