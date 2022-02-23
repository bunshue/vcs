using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;        //for Directory
using System.Diagnostics;   //for Process

/*
儲存參數
點開 方案總管/vcs_XXXXX/Properties/Settings.settings
加入要儲存的參數 的 名稱 型別 預設值
若是數字 一定要給預設值
*/

using AxWMPLib;
/*  sugar
使用AxWindowsMediaPlayer播放多媒體

加入工具箱

工具箱/滑鼠右鍵/選擇項目/
/COM元件 頁籤 /勾選Windows Media Player(wmp.dll)	/ 確定

會發現工具箱多了個Windows Media Player的控制項
就是 axWindowsMediaPlayer

拉一個Windows Media Player控件進表單, 參考裡面就會出現AxWMPLib和WMPLib
*/

namespace vcs_MyToolbox
{
    public partial class Form1 : Form
    {
        string mp3_filename = string.Empty;
        string pdf_filename = string.Empty;
        string mp3_filename_short = string.Empty;
        string pdf_filename_short = string.Empty;
        string current_directory = string.Empty;
        bool flag_already_use_webbrowser = false;

        int mp3_position = 0;
        int mp3_volume = 50;
        double mp3_rate = 1.0;
        int mp3_player_height = 50;

        int pdf_page = 0;

        List<String> mp3_filename_list = new List<String>();
        int current_mp3_index = 0;
        int total_mp3_count = 0;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        AxWindowsMediaPlayer axWindowsMediaPlayer1;

        bool flag_debug_mode = true;
        bool flag_repeat_mode = true;


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
        PictureBox pbx_clock = new PictureBox();
        Button btn_00 = new Button();
        Button btn_01 = new Button();
        Button btn_02 = new Button();
        Button btn_10 = new Button();
        Button btn_11 = new Button();
        Button btn_12 = new Button();
        Button btn_20 = new Button();
        Button btn_21 = new Button();
        Button btn_22 = new Button();
        Button btn_20s = new Button();
        Button btn_21s = new Button();
        Label lb_debug0 = new Label();
        Label lb_debug1 = new Label();
        Label lb_debug2 = new Label();
        TextBox tb_pdf_page = new TextBox();
        RichTextBox richTextBox1 = new RichTextBox();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            add_my_toolbox_controls();

            Init_Controls();

            this.TopMost = true;
            this.ShowInTaskbar = false;


            pdf_page = Properties.Settings.Default.pdf_page;

            if (pdf_page == -1)
            {
                pdf_page = 0;
            }
            tb_pdf_page.Text = pdf_page.ToString();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            bool conversionSuccessful = int.TryParse(tb_pdf_page.Text, out pdf_page);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到int數字： " + pdf_page + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
            }

            Properties.Settings.Default.mp3_filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;
            Properties.Settings.Default.volume = mp3_volume;
            Properties.Settings.Default.pdf_filename = pdf_filename;

            Properties.Settings.Default.pdf_page = pdf_page;

            Properties.Settings.Default.Save();
        }

        void Init_Controls()
        {
            this.axWindowsMediaPlayer1 = new AxWindowsMediaPlayer();
            this.axWindowsMediaPlayer1.Enabled = true;
            //this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(0, 400);
            //this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            //this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(800, 500);
            //this.axWindowsMediaPlayer1.TabIndex = 2;
            //this.axWindowsMediaPlayer1.Visible = false;   //fail
            this.axWindowsMediaPlayer1.StatusChange += new EventHandler(axWindowsMediaPlayer1_StatusChange);
            this.Controls.Add(this.axWindowsMediaPlayer1);
            axWindowsMediaPlayer1.Visible = false;
        }

        protected void axWindowsMediaPlayer1_StatusChange(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsStopped)
            {
                mp3_position = 0;

                //判斷影片是否已經停止播放
                if (flag_repeat_mode == true)
                {
                    //停頓2秒後再重新播放
                    System.Threading.Thread.Sleep(2000);
                    //重新播放
                    axWindowsMediaPlayer1.Ctlcontrols.play();
                }
            }
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
            btn_00.Text = "小算盤";
            btn_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            btn_00.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_00);	// 將控件加入表單

            btn_01.Width = w;
            btn_01.Height = h;
            btn_01.Text = "WinMerge";
            btn_01.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            btn_01.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_01);	// 將控件加入表單

            btn_02.Width = w;
            btn_02.Height = h;
            btn_02.Text = "Matlab";
            btn_02.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            btn_02.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_02);	// 將控件加入表單

            btn_10.Width = w;
            btn_10.Height = h;
            btn_10.Text = "Git";
            btn_10.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            btn_10.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_10);	// 將控件加入表單

            btn_11.Width = w;
            btn_11.Height = h;
            btn_11.Text = "Visual C#";
            btn_11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            btn_11.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_11);	// 將控件加入表單

            btn_12.Width = w;
            btn_12.Height = h;
            btn_12.Text = "";
            btn_12.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            btn_12.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_12);	// 將控件加入表單

            btn_20.Width = w;
            btn_20.Height = h;
            btn_20.Text = "mp3";
            btn_20.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            btn_20.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_20);	// 將控件加入表單
            btn_20s.Width = w / 3;
            btn_20s.Height = h / 3;
            btn_20s.Text = "open";
            btn_20s.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            btn_20s.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_20s);	// 將控件加入表單
            btn_20s.BringToFront();

            btn_21.Width = w;
            btn_21.Height = h;
            btn_21.Text = "pdf";
            btn_21.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            btn_21.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_21);	// 將控件加入表單
            btn_21s.Width = w/3;
            btn_21s.Height = h/3;
            btn_21s.Text = "open";
            btn_21s.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            btn_21s.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_21s);	// 將控件加入表單
            btn_21s.BringToFront();

            tb_pdf_page.Width = w / 3;
            tb_pdf_page.Height = h / 3;
            tb_pdf_page.Text = "5";
            tb_pdf_page.TextAlign = HorizontalAlignment.Center;
            tb_pdf_page.Location = new Point(x_st + dx * 1, y_st + dy * 2 + btn_21.Height - tb_pdf_page.Height);
            tb_pdf_page.Click += btn_click_function;	// 加入事件
            this.Controls.Add(tb_pdf_page);	// 將控件加入表單
            tb_pdf_page.BringToFront();

            btn_22.Width = w;
            btn_22.Height = h;
            btn_22.Text = "";
            btn_22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            btn_22.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_22);	// 將控件加入表單

            richTextBox1.Width = w * 3 + 40;
            richTextBox1.Height = h * 2 - 20;
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            this.Controls.Add(richTextBox1);	// 將控件加入表單

            //lb_debug0.Text = "AAAAAAA";
            lb_debug0.Font = new Font("標楷體", 22);
            lb_debug0.ForeColor = Color.Red;
            lb_debug0.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_debug0.AutoSize = true;
            this.Controls.Add(lb_debug0);     // 將控件加入表單

            //lb_debug1.Text = "BBBBBBB";
            lb_debug1.Font = new Font("標楷體", 22);
            lb_debug1.ForeColor = Color.Red;
            lb_debug1.Location = new Point(x_st + dx * 0, y_st + dy * 3+50);
            lb_debug1.AutoSize = true;
            this.Controls.Add(lb_debug1);     // 將控件加入表單

            //lb_debug2.Text = "CCCCCCC";
            lb_debug2.Font = new Font("標楷體", 22);
            lb_debug2.ForeColor = Color.Red;
            lb_debug2.Location = new Point(x_st + dx * 0, y_st + dy * 3+100);
            lb_debug2.AutoSize = true;
            this.Controls.Add(lb_debug2);     // 將控件加入表單

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
            bool conversionSuccessful = int.TryParse(tb_pdf_page.Text, out pdf_page);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到int數字： " + pdf_page + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
            }

            Properties.Settings.Default.mp3_filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;
            Properties.Settings.Default.volume = mp3_volume;
            Properties.Settings.Default.pdf_filename = pdf_filename;

            Properties.Settings.Default.pdf_page = pdf_page;

            Properties.Settings.Default.Save();

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

        void btn_click_function(object sender, EventArgs e)
        {
            string text = string.Empty;

            if (sender.Equals(btn_00))
            {
                //Process.Start(@"C:\WINDOWS\system32\calc.exe");   same
                Process.Start("calc");
                text = btn_00.Text;
            }
            else if (sender.Equals(btn_01))
            {
                Process.Start(@"C:\Program Files (x86)\WinMerge\WinMergeU.exe");
                text = btn_01.Text;
            }
            else if (sender.Equals(btn_02))
            {
                text = btn_02.Text;
            }
            else if (sender.Equals(btn_10))
            {
                text = btn_10.Text;
                string foldername = @"C:\_git\vcs";
                if (Directory.Exists(foldername) == true)
                {
                    Process.Start(foldername);
                }
                else
                {
                    lb_debug1.Text = "Git資料夾不存在";
                }
            }
            else if (sender.Equals(btn_11))
            {
                text = btn_11.Text;
            }
            else if (sender.Equals(btn_12))
            {
                text = btn_12.Text;
            }
            else if (sender.Equals(btn_20))
            {
                text = btn_20.Text;
                lb_debug1.Text = "播放mp3";

                string mp3_filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
                axWindowsMediaPlayer1.URL = mp3_filename;
            }
            else if (sender.Equals(btn_20s))
            {
                richTextBox1.Text += "你按了開啟 mp3 檔案\n";
            }
            else if (sender.Equals(btn_21))
            {
                text = btn_21.Text;

                //用Adobe開啟pdf檔案
                string filename = "C:\\______test_files\\__RW\\_pdf\\note_Linux_workstation.pdf";
                //Process process;
                //process = Process.Start(filename);

                bool conversionSuccessful = int.TryParse(tb_pdf_page.Text, out pdf_page);    //out為必須
                if (conversionSuccessful == true)
                {
                    richTextBox1.Text += "得到int數字： " + pdf_page + "\n";
                }
                else
                {
                    richTextBox1.Text += "int.TryParse 失敗\n";
                    pdf_page = 0;
                }

                if (File.Exists(filename) == true)
                {
                    Form2 fm = new Form2(filename, pdf_page);
                    fm.Show();
                    flag_already_use_webbrowser = true;
                }
                else
                {

                }
            }
            else if (sender.Equals(btn_21s))
            {
                richTextBox1.Text += "你按了開啟 pdf 檔案\n";




                pdf_page = 0;
                tb_pdf_page.Text = pdf_page.ToString();
            }
            else if (sender.Equals(btn_22))
            {
                text = btn_22.Text;


                pdf_page = 6;

                Properties.Settings.Default.pdf_page = pdf_page;

                Properties.Settings.Default.Save();



                pdf_page = Properties.Settings.Default.pdf_page;

                richTextBox1.Text += "pdf_page = " + pdf_page.ToString() + "\n";
            }
            else
            {
                text = "unknown";
            }

            lb_debug0.Text = "你按了 " + text;
        }

        //string filename = @"C:\______test_files\_icon\快.ico";
        int i = 0; //先設置一個全局變量 i ,用來控制圖片索引,然後創建定時事件,雙擊定時控件就可以編輯 
        private Icon icon1 = new Icon(@"C:\______test_files\_icon\快.ico");
        private Icon icon2 = new Icon(@"C:\______test_files\_icon\影.ico"); //兩個圖標 切換顯示 以達到消息閃動的效果

        //定時器 不斷閃動圖標
        private void timer_notifyicon_Tick(object sender, EventArgs e)
        {
            i++;
            if ((i % 2) == 0)
            {
                this.notifyIcon1.Icon = icon1;
            }
            else
            {
                this.notifyIcon1.Icon = icon2;
            }
        }


    }
}
