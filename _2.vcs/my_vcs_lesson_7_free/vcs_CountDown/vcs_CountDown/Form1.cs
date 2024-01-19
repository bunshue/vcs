using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_CountDown
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //設定執行後的表單起始位置
            //this.StartPosition = FormStartPosition.Manual;
            //this.Location = new System.Drawing.Point(0, 0);

            this.Size = new Size(512, 512);
            //this.TopMost = true;
            this.ShowInTaskbar = false;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;

            //離開按鈕的寫法
            bt_exit_setup();

            //最小化按鈕的寫法
            bt_minimize_setup();

            show_item_location();

        }

        TrackBar tbar0 = new TrackBar();

        NumericUpDown nud_hh = new NumericUpDown();
        NumericUpDown nud_mm = new NumericUpDown();
        NumericUpDown nud_ss = new NumericUpDown();
        Button bt_setup = new Button();
        RichTextBox rtb = new RichTextBox();

        void show_item_location()
        {

            int x_st = 50;
            int y_st = 50;
            int dx = 100;
            int dy = 20;
            int offset = 0;
            int w = 80;  //控件寬度
            int h = 40;  //控件高度

            // 實例化控件
            nud_hh.Text = "";
            nud_hh.Font = new Font("標楷體", 22);
            nud_hh.ForeColor = Color.Red;
            nud_hh.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            //nud_hh.AutoSize = true;
            nud_hh.Size = new Size(w, h);
            nud_hh.Maximum = 23;
            nud_hh.Minimum = 0;
            this.Controls.Add(nud_hh);     // 將控件加入表單

            nud_mm.Text = "";
            nud_mm.Font = new Font("標楷體", 22);
            nud_mm.ForeColor = Color.Red;
            nud_mm.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            //nud_mm.AutoSize = true;
            nud_mm.Size = new Size(w, h);
            nud_mm.Maximum = 59;
            nud_mm.Minimum = 0;
            this.Controls.Add(nud_mm);     // 將控件加入表單

            nud_ss.Text = "";
            nud_ss.Font = new Font("標楷體", 22);
            nud_ss.ForeColor = Color.Red;
            nud_ss.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            //nud_ss.AutoSize = true;
            nud_ss.Size = new Size(w, h);
            nud_ss.Maximum = 59;
            nud_ss.Minimum = 0;
            this.Controls.Add(nud_ss);     // 將控件加入表單

            bt_setup.Text = "設定";
            bt_setup.Font = new Font("標楷體", 16);
            bt_setup.ForeColor = Color.Red;
            bt_setup.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            //bt_setup.AutoSize = true;
            bt_setup.Size = new Size(w, h);
            // 加入按鈕事件
            //bt_setup.Click += new EventHandler(setup_timer);   //same
            bt_setup.Click += setup_timer;
            this.Controls.Add(bt_setup);     // 將控件加入表單

            rtb.Text = "";
            rtb.Font = new Font("標楷體", 14);
            //rtb.ForeColor = Color.Red;
            rtb.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            //rtb.AutoSize = true;
            rtb.Size = new Size(400, 300);
            this.Controls.Add(rtb);     // 將控件加入表單


            nud_hh.Value = DateTime.Now.Hour;
            nud_mm.Value = DateTime.Now.Minute;
            nud_ss.Value = DateTime.Now.Second;
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

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        //重定義基類OnPaint()方法
        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            int y = 0;
            g.FillRectangle(Brushes.Wheat, ClientRectangle);    //繪制窗體背景色

            //g.FillRectangle(Brushes.Blue, rect);//墳充一個矩形

            Font f = new Font("微軟正黑體", 50, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(0, y, 400, f.Height);
            g.DrawString(cnt.ToString(), f, Brushes.Black, rect);
            f.Dispose();

            using (Pen pen = new Pen(Color.Red, 1))
            {
                for (y = 0; y <= ClientRectangle.Height; y += ClientRectangle.Height / 12)
                {

                    g.DrawLine(pen, new Point(0, 0), new Point(ClientRectangle.Width, y));
                }
            }
            g.FillEllipse(Brushes.Red, new Rectangle(100, 100, 50, 50));
        }


        private void setup_timer(object sender, EventArgs e)
        {
            int hh = (int)nud_hh.Value;
            int mm = (int)nud_mm.Value;
            int ss = (int)nud_ss.Value;

            int current_time = hh * 60 * 60 + mm * 60 + ss;
            rtb.Text += "設定時間 : " + current_time.ToString() + "\n";




        }




        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            this.Invalidate();

            if (cnt > 10)
            {
                cnt = 0;
                this.TopMost = true;
                this.WindowState = FormWindowState.Normal;

            }
        }
    }
}
