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
using System.Drawing.Drawing2D; //for SmoothingMode
using System.Drawing.Imaging;   //for ImageFormat

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

//為了數字時鐘
//拷貝進來 A1XXX, DigitalXXXX Globals.cs共6個檔案 加入現有項目 *.cs 4個
//編譯後 工具箱出現新控件

namespace vcs_MyToolbox
{
    public partial class Form1 : Form
    {
        //string foldername = @"C:\dddddddddd";

        string mp3_filename = string.Empty;
        string pdf_filename = string.Empty;
        string video_filename = string.Empty;
        string mp3_filename_short = string.Empty;
        string pdf_filename_short = string.Empty;
        string video_filename_short = string.Empty;
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

        // The image of the whole screen.
        private Bitmap ScreenBm, VisibleBm;

        // The area we are selecting.
        private int X0, Y0, X1, Y1;

        AxWindowsMediaPlayer axWindowsMediaPlayer1;

        bool flag_debug_mode = true;
        bool flag_repeat_mode = true;
        bool flag_pause_mode = false;

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
        Label lb_main_mesg1 = new Label();
        TextBox tb_pdf_page = new TextBox();
        PictureBox pictureBox1 = new PictureBox();
        RichTextBox richTextBox1 = new RichTextBox();
        GroupBox groupBox1 = new GroupBox();
        Button btn_capture0 = new Button();
        Button btn_capture1 = new Button();
        Button btn_capture2 = new Button();

        Button btn_clock = new Button();
        Button btn_stopwatch = new Button();
        Button btn_countdown = new Button();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            /*
            //檢查存圖的資料夾
            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(foldername);
                richTextBox1.Text += "已建立一個新資料夾: " + foldername + "\n";
            }
            else
            {
                //richTextBox1.Text += "資料夾: " + foldername + " 已存在，不用再建立\n";
            }
            */

            add_my_toolbox_controls();

            Init_Controls();

            this.TopMost = true;
            this.ShowInTaskbar = false;

            //video
            video_filename = Properties.Settings.Default.video_filename;
            if (File.Exists(video_filename) == true)
            {
                video_filename_short = Path.GetFileName(video_filename);
                current_directory = Path.GetDirectoryName(video_filename);
            }

            //pdf
            pdf_filename = Properties.Settings.Default.pdf_filename;
            pdf_page = Properties.Settings.Default.pdf_page;

            if (File.Exists(pdf_filename) == true)
            {
                pdf_filename_short = Path.GetFileName(pdf_filename);
                current_directory = Path.GetDirectoryName(pdf_filename);
            }

            if (pdf_page == -1)
            {
                pdf_page = 0;
            }
            tb_pdf_page.Text = pdf_page.ToString();

            //mp3
            mp3_filename = Properties.Settings.Default.mp3_filename;
            mp3_position = Properties.Settings.Default.position;
            if (File.Exists(mp3_filename) == true)
            {
                mp3_filename_short = Path.GetFileName(mp3_filename);
                current_directory = Path.GetDirectoryName(mp3_filename);

                //axWindowsMediaPlayer1.URL = mp3_filename; //不立刻播放

                mp3_filename_short = Path.GetFileName(mp3_filename);
                current_directory = Path.GetDirectoryName(mp3_filename);
                show_main_message1("檔案 : " + mp3_filename_short.ToString(), S_OK, 30);

                FileInfo f = new FileInfo(mp3_filename);
                string foldername = f.DirectoryName;

                DirectoryInfo di = new DirectoryInfo(foldername);

                mp3_filename_list.Clear();

                foreach (FileInfo fi in di.GetFiles())
                {
                    if (fi.Extension.ToLower() == ".mp3")
                    {
                        mp3_filename_list.Add(fi.FullName);
                    }
                }

                total_mp3_count = mp3_filename_list.Count;

                mp3_filename_list.Sort();

                // 取出單一個List 裡的值，如同陣列(Array)用法
                for (i = 0; i < mp3_filename_list.Count; i++)
                {
                    //richTextBox1.Text += mp3_filename_list[i] + "\n";
                    if (mp3_filename_list[i] == mp3_filename)
                    {
                        current_mp3_index = i;
                        richTextBox1.Text += "select i = " + current_mp3_index.ToString() + "\n";
                    }
                }

                /*
                richTextBox1.Text += "共有 " + mp3_filename_list.Count.ToString() + " 個字串\n";

                mp3_filename_list.Sort();

                // 取出單一個List 裡的值，如同陣列(Array)用法
                for (int i = 0; i < mp3_filename_list.Count; i++)
                {
                    richTextBox1.Text += mp3_filename_list[i] + "\n";
                }
                */

                richTextBox1.Text += "len = " + total_mp3_count.ToString() + "\n";
                richTextBox1.Text += "index = " + current_mp3_index.ToString() + "\n";
            }

            mp3_volume = Properties.Settings.Default.volume;
            if (mp3_volume == -1)
            {
                mp3_volume = 50;
            }

            axWindowsMediaPlayer1.settings.volume = mp3_volume;
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;

            richTextBox1.Text += "mp3檔案 : " + mp3_filename + "\n";
            richTextBox1.Text += "位置 : " + mp3_position.ToString() + "\n";
            richTextBox1.Text += "音量 : " + mp3_volume.ToString() + "\n";

            this.KeyPreview = true;
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

            mp3_position = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;
            Properties.Settings.Default.mp3_filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;
            Properties.Settings.Default.volume = mp3_volume;
            Properties.Settings.Default.pdf_filename = pdf_filename;
            Properties.Settings.Default.pdf_page = pdf_page;
            Properties.Settings.Default.video_filename = video_filename;

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
            h = 90;

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
            btn_21s.Width = w / 3;
            btn_21s.Height = h / 3;
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
            this.Controls.Add(tb_pdf_page);	// 將控件加入表單
            tb_pdf_page.BringToFront();

            btn_22.Width = w;
            btn_22.Height = h;
            btn_22.Text = "";
            btn_22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            btn_22.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_22);	// 將控件加入表單

            btn_clock.Width = w * 6 / 10;
            btn_clock.Height = h * 5 / 10;
            btn_clock.Text = "時鐘";
            btn_clock.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            btn_clock.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_clock);	// 將控件加入表單

            btn_stopwatch.Width = w * 6 / 10;
            btn_stopwatch.Height = h * 5 / 10;
            btn_stopwatch.Text = "碼表";
            btn_stopwatch.Location = new Point(x_st + dx * 2, y_st + dy * 3+45);
            btn_stopwatch.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_stopwatch);	// 將控件加入表單

            btn_countdown.Width = w * 6 / 10;
            btn_countdown.Height = h * 5 / 10;
            btn_countdown.Text = "倒數";
            btn_countdown.Location = new Point(x_st + dx * 2, y_st + dy * 3 + 90);
            btn_countdown.Click += btn_click_function;	// 加入事件
            this.Controls.Add(btn_countdown);	// 將控件加入表單


            //groupBox1 ST
            groupBox1.Width = w * 2 - 20;
            groupBox1.Height = h + 35;
            groupBox1.Text = "截圖";
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            groupBox1.BackColor = Color.Pink;
            //groupBox1.Click += btn_click_function;	// 加入事件
            this.Controls.Add(groupBox1);	// 將控件加入表單

            btn_capture0.Width = w * 3 / 4;
            btn_capture0.Height = h * 3 / 5;
            btn_capture0.Text = "截圖存檔";
            btn_capture0.Location = new Point(10, 10);
            btn_capture0.Click += btn_click_function;	// 加入事件
            this.groupBox1.Controls.Add(btn_capture0);	// 將控件加入表單

            btn_capture1.Width = w * 3 / 4;
            btn_capture1.Height = h * 3 / 5;
            btn_capture1.Text = "全屏截圖";
            btn_capture1.Location = new Point(110, 10);
            btn_capture1.Click += btn_click_function;	// 加入事件
            this.groupBox1.Controls.Add(btn_capture1);	// 將控件加入表單

            btn_capture2.Width = w * 3 / 4;
            btn_capture2.Height = h * 3 / 5;
            btn_capture2.Text = "自選截圖";
            btn_capture2.Location = new Point(110, 65);
            btn_capture2.Click += btn_click_function;	// 加入事件
            this.groupBox1.Controls.Add(btn_capture2);	// 將控件加入表單
            //groupBox1 SP

            //lb_main_mesg1.Text = "AAAAAAA";
            lb_main_mesg1.Font = new Font("標楷體", 20);
            lb_main_mesg1.ForeColor = Color.Red;
            //lb_main_mesg1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_main_mesg1.Location = new Point(x_st + dx * 0, y_st + dy * 3 - 16 + 150);
            lb_main_mesg1.AutoSize = true;
            this.Controls.Add(lb_main_mesg1);     // 將控件加入表單

            //pictureBox1
            pictureBox1.Width = w * 3 + 40;
            pictureBox1.Height = h / 2;
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 22 + 150);
            pictureBox1.BackColor = Color.Pink;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox1.Click += pictureBox1_click;	// 加入事件
            pictureBox1.Paint += pictureBox1_Paint; // 加入事件
            pictureBox1.MouseDown += pictureBox1_MouseDown;
            pictureBox1.MouseUp += pictureBox1_MouseUp;

            this.Controls.Add(pictureBox1);	// 將控件加入表單

            richTextBox1.Width = w * 3 + 40;
            richTextBox1.Height = h * 1 + 10;
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 4 - 40 + 150);
            this.Controls.Add(richTextBox1);	// 將控件加入表單

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

            mp3_position = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;
            Properties.Settings.Default.mp3_filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;
            Properties.Settings.Default.volume = mp3_volume;
            Properties.Settings.Default.pdf_filename = pdf_filename;
            Properties.Settings.Default.pdf_page = pdf_page;
            Properties.Settings.Default.video_filename = video_filename;

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
                    show_main_message1("Git資料夾不存在", S_OK, 30);
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

                if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
                {
                    flag_pause_mode = true;
                    axWindowsMediaPlayer1.Ctlcontrols.pause();
                    show_main_message1("暫停", S_OK, 100);
                }
                else
                {
                    if (flag_pause_mode == false)
                    {
                        show_main_message1("播放mp3", S_OK, 30);
                        //axWindowsMediaPlayer1.Ctlcontrols.play();

                        if (File.Exists(mp3_filename) == true)
                        {
                            //string mp3_filename = @"C:\_git\vcs\_1.data\______test_files1\_mp3\16.監獄風雲.mp3";
                            axWindowsMediaPlayer1.URL = mp3_filename;
                        }
                        else
                        {
                            richTextBox1.Text += "無 mp3 檔案\n";
                        }
                    }
                    else
                    {
                        axWindowsMediaPlayer1.Ctlcontrols.play();
                        show_main_message1("繼續", S_OK, 100);
                    }
                }
            }
            else if (sender.Equals(btn_20s))
            {
                richTextBox1.Text += "你按了開啟 mp3 檔案\n";

                openFileDialog1.Title = "單選檔案";
                openFileDialog1.FileName = "";              //預設開啟的檔名
                openFileDialog1.DefaultExt = "*.mp3";
                openFileDialog1.Filter = "mp3檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|MP4檔(*.mp4)|*.mp4|所有檔案(*.*)|*.*";   //存檔類型
                openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
                openFileDialog1.RestoreDirectory = true;
                //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
                //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
                openFileDialog1.Multiselect = false;    //單選
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    /*
                    richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    richTextBox1.Text += "Name: " + f.Name + "\n";
                    richTextBox1.Text += "FullName: " + f.FullName + "\n";
                    richTextBox1.Text += "Extension: " + f.Extension + "\n";
                    richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                    richTextBox1.Text += "Directory: " + f.Directory + "\n";
                    richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                    */

                    mp3_filename = openFileDialog1.FileName;
                    mp3_filename_short = Path.GetFileName(mp3_filename);
                    current_directory = Path.GetDirectoryName(mp3_filename);
                    mp3_position = 0;
                    axWindowsMediaPlayer1.URL = mp3_filename;
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
                    axWindowsMediaPlayer1.Ctlcontrols.play();
                    show_main_message1("檔案 : " + mp3_filename_short.ToString(), S_OK, 30);

                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    string foldername = f.DirectoryName;

                    DirectoryInfo di = new DirectoryInfo(foldername);

                    mp3_filename_list.Clear();

                    foreach (FileInfo fi in di.GetFiles())
                    {
                        if (fi.Extension.ToLower() == ".mp3")
                        {
                            mp3_filename_list.Add(fi.FullName);
                        }
                    }

                    total_mp3_count = mp3_filename_list.Count;

                    mp3_filename_list.Sort();

                    // 取出單一個List 裡的值，如同陣列(Array)用法
                    for (int i = 0; i < mp3_filename_list.Count; i++)
                    {
                        //richTextBox1.Text += mp3_filename_list[i] + "\n";
                        if (mp3_filename_list[i] == openFileDialog1.FileName)
                        {
                            current_mp3_index = i;
                            richTextBox1.Text += "select i = " + current_mp3_index.ToString() + "\n";
                        }
                    }


                    /*
                    richTextBox1.Text += "共有 " + mp3_filename_list.Count.ToString() + " 個字串\n";

                    mp3_filename_list.Sort();

                    // 取出單一個List 裡的值，如同陣列(Array)用法
                    for (int i = 0; i < mp3_filename_list.Count; i++)
                    {
                        richTextBox1.Text += mp3_filename_list[i] + "\n";
                    }
                    */

                    richTextBox1.Text += "len = " + total_mp3_count.ToString() + "\n";
                    richTextBox1.Text += "index = " + current_mp3_index.ToString() + "\n";

                }
                else
                {
                    show_main_message1("未選取檔案", S_OK, 30);
                    mp3_filename = "";
                    mp3_position = 0;
                }

            }
            else if (sender.Equals(btn_21))
            {
                text = btn_21.Text;

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

                //用Adobe開啟pdf檔案
                //string filename = "C:\\______test_files1\\__RW\\_pdf\\note_Linux_workstation.pdf";
                //Process process;
                //process = Process.Start(filename);

                if (File.Exists(pdf_filename) == true)
                {
                    Form2 fm = new Form2(pdf_filename, pdf_page);
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

                openFileDialog1.Title = "單選檔案";
                openFileDialog1.FileName = "";              //預設開啟的檔名
                openFileDialog1.DefaultExt = "*.pdf";
                openFileDialog1.Filter = "pdf檔(*.pdf)|*.pdf|所有檔案(*.*)|*.*";   //存檔類型
                //openFileDialog1.Filter = "mp3檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|MP4檔(*.mp4)|*.mp4|所有檔案(*.*)|*.*";   //存檔類型
                openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
                openFileDialog1.RestoreDirectory = true;
                //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
                //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
                openFileDialog1.Multiselect = false;    //單選
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    /*
                    richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    richTextBox1.Text += "Name: " + f.Name + "\n";
                    richTextBox1.Text += "FullName: " + f.FullName + "\n";
                    richTextBox1.Text += "Extension: " + f.Extension + "\n";
                    richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                    richTextBox1.Text += "Directory: " + f.Directory + "\n";
                    richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                    */

                    pdf_filename = openFileDialog1.FileName;
                    pdf_filename_short = Path.GetFileName(pdf_filename);
                    current_directory = Path.GetDirectoryName(pdf_filename);

                    pdf_page = 0;
                    tb_pdf_page.Text = pdf_page.ToString();

                    Form2 fm = new Form2(pdf_filename, pdf_page);
                    fm.Show();
                    flag_already_use_webbrowser = true;

                }
                else
                {
                    show_main_message1("未選取檔案", S_OK, 30);
                    pdf_filename = "";
                }
            }
            else if (sender.Equals(btn_22))
            {
                text = btn_22.Text;
            }
            else if (sender.Equals(btn_capture0))
            {
                text = btn_capture0.Text;

                //截圖存檔

                IDataObject dataObject = Clipboard.GetDataObject();   //GetDataObject() 讀取當前剪貼簿中的數據內容
                if (dataObject.GetDataPresent(DataFormats.Bitmap))  //圖片類
                {
                    richTextBox1.Text += "取得圖片\n";

                    //取出Bitmap資料, 可做處理
                    Bitmap bitmap1 = (Bitmap)dataObject.GetData(DataFormats.Bitmap);  //取得Bitmap資料
                    if (bitmap1 != null)
                    {
                        string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                        try
                        {
                            bitmap1.Save(@filename, ImageFormat.Jpeg);

                            richTextBox1.Text += "存檔成功\n";
                            richTextBox1.Text += "已存檔 : " + filename + "\n";
                            timer1.Enabled = true;
                        }
                        catch (Exception ex)
                        {
                            richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "無圖可存\n";
                        timer1.Enabled = true;
                    }
                }
                else
                {
                    richTextBox1.Text += "無圖片\n";
                    timer1.Enabled = true;
                }
            }
            else if (sender.Equals(btn_capture1))
            {
                text = btn_capture1.Text;

                //全螢幕截圖

                this.Hide();    // Hide this form.
                delay(100);

                /*
                //全螢幕截圖 法一
                //建立空白畫布
                Bitmap bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
                //取得畫布的繪圖物件用以繪圖
                Graphics g = Graphics.FromImage(bitmap1);
                g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
                IntPtr dc1 = g.GetHdc();
                g.ReleaseHdc(dc1);

                //將裁切出的矩形存成JPG圖檔。
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                try
                {
                    bitmap1.Save(@filename, ImageFormat.Jpeg);
                    //richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                    label1.Text = "存檔成功";
                    timer1.Enabled = true;
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                */

                //全螢幕截圖 法二
                // Get the screen's image.
                using (Bitmap bitmap1 = GetScreenImage())
                {
                    //存成bmp檔
                    string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                    bitmap1.Save(filename, ImageFormat.Jpeg);
                    richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                    timer1.Enabled = true;
                }
                this.Show();    // Show this form again.

            }
            else if (sender.Equals(btn_capture2))
            {
                text = btn_capture2.Text;

                //自選截圖
                // Get the whole screen's image.
                ScreenBm = GetScreenImage();

                // Display a copy.
                VisibleBm = (Bitmap)ScreenBm.Clone();

                // Display it.
                //button1.Visible = false;
                //button2.Visible = false;
                //button3.Visible = false;
                this.BackgroundImage = VisibleBm;
                this.Location = new Point(0, 0);
                this.ClientSize = VisibleBm.Size;
                this.MouseDown += Form1_MouseDown;
                this.Show();
            }
            else if (sender.Equals(btn_clock))
            {
                text = btn_clock.Text;
                //時鐘
            }
            else if (sender.Equals(btn_stopwatch))
            {
                text = btn_stopwatch.Text;
                //碼表
            }
            else if (sender.Equals(btn_countdown))
            {
                text = btn_countdown.Text;
                //倒數
            }
            else
            {
                text = "unknown";
            }
            show_main_message1("你按了 " + text, S_OK, 30);
        }

        // Get the screen's image.
        private Bitmap GetScreenImage()
        {
            // Make a bitmap to hold the result.
            Bitmap bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height, PixelFormat.Format24bppRgb);

            // Copy the image into the bitmap.
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.CopyFromScreen(Screen.PrimaryScreen.Bounds.X, Screen.PrimaryScreen.Bounds.Y, 0, 0, Screen.PrimaryScreen.Bounds.Size, CopyPixelOperation.SourceCopy);
            }

            // Return the result.
            return bitmap1;
        }

        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        // Start selecting an area.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Down\n";
            X0 = e.X;
            Y0 = e.Y;
            X1 = e.X;
            Y1 = e.Y;

            this.MouseDown -= Form1_MouseDown;
            this.MouseMove += Form1_MouseMove;
            this.MouseUp += Form1_MouseUp;
        }

        // Continue selecting an area.
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            X1 = e.X;
            Y1 = e.Y;

            using (Graphics gr = Graphics.FromImage(VisibleBm))
            {
                // Copy the original image.
                gr.DrawImage(ScreenBm, 0, 0);

                // Draw the selected area.
                Rectangle rect = new Rectangle(
                    Math.Min(X0, X1),
                    Math.Min(Y0, Y1),
                    Math.Abs(X1 - X0),
                    Math.Abs(Y1 - Y0));
                gr.DrawRectangle(Pens.Yellow, rect);
            }
            this.Refresh();
        }

        // Finish selecting an area.
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "Up\n";
            this.Visible = false;
            this.MouseMove -= Form1_MouseMove;
            this.MouseUp -= Form1_MouseUp;

            // Save the selected part of the image.
            int wid = Math.Abs(X1 - X0);
            int hgt = Math.Abs(Y1 - Y0);
            Rectangle dest_rect = new Rectangle(0, 0, wid, hgt);
            Rectangle source_rect = new Rectangle(
                Math.Min(X0, X1),
                Math.Min(Y0, Y1),
                Math.Abs(X1 - X0),
                Math.Abs(Y1 - Y0));

            using (Bitmap selection = new Bitmap(wid, hgt))
            {
                // Copy the selected area.
                using (Graphics gr = Graphics.FromImage(selection))
                {
                    gr.DrawImage(ScreenBm, dest_rect, source_rect, GraphicsUnit.Pixel);
                }

                // Save the selected area.
                //存成bmp檔
                string filename = "C:\\dddddddddd\\Image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                selection.Save(filename, ImageFormat.Jpeg);
                richTextBox1.Text += "全螢幕截圖1，存檔檔名：" + filename + "\n";
                Form1_Load(sender, e);
                timer1.Enabled = true;
                this.Show();    // Show this form again.
            }

            // Dispose of the other bitmaps.
            this.BackgroundImage = null;
            ScreenBm.Dispose();
            VisibleBm.Dispose();
            ScreenBm = null;
            VisibleBm = null;
        }

        //string filename = @"C:\_git\vcs\_1.data\______test_files1\_icon\快.ico";
        int i = 0; //先設置一個全局變量 i ,用來控制圖片索引,然後創建定時事件,雙擊定時控件就可以編輯 
        private Icon icon1 = new Icon(@"C:\_git\vcs\_1.data\______test_files1\_icon\快.ico");
        private Icon icon2 = new Icon(@"C:\_git\vcs\_1.data\______test_files1\_icon\影.ico"); //兩個圖標 切換顯示 以達到消息閃動的效果

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

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
            }
        }


        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.T)
            {
                show_main_message1("Test 1", S_OK, 30);
            }
            else if (e.KeyData == Keys.T)
            {
                show_main_message1("Test 2", S_OK, 30);
            }
            else if (e.KeyData == Keys.PageUp)
            {
                show_main_message1("上一首", S_OK, 30);

                if (current_mp3_index > 0)
                {
                    current_mp3_index--;
                    mp3_filename = mp3_filename_list[current_mp3_index];
                    mp3_position = 0;
                    axWindowsMediaPlayer1.URL = mp3_filename;
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
                    mp3_filename_short = Path.GetFileName(mp3_filename);
                    current_directory = Path.GetDirectoryName(mp3_filename);
                    show_main_message1("檔案 : " + mp3_filename_short.ToString(), S_OK, 30);
                }
            }
            else if (e.KeyData == Keys.PageDown)
            {
                show_main_message1("下一首", S_OK, 30);
                if (current_mp3_index < (total_mp3_count - 2))
                {
                    current_mp3_index++;
                    mp3_filename = mp3_filename_list[current_mp3_index];
                    mp3_position = 0;
                    axWindowsMediaPlayer1.URL = mp3_filename;
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
                    mp3_filename_short = Path.GetFileName(mp3_filename);
                    current_directory = Path.GetDirectoryName(mp3_filename);
                    show_main_message1("檔案 : " + mp3_filename_short.ToString(), S_OK, 30);
                }
            }
            else if ((e.KeyData == Keys.Escape) || (e.KeyData == Keys.X))
            {
                this.Close();
            }
            else if (e.KeyData == Keys.Back)
            {
                axWindowsMediaPlayer1.Ctlcontrols.currentPosition = 0;
                show_main_message1("快退至起點", S_OK, 30);
            }
            else if (e.KeyData == Keys.H)
            {
                show_main_message1("Help", S_OK, 30);

                //Help help = new Help();
                //help.Show();
            }
            else if (e.KeyData == Keys.I)
            {
                show_main_message1("mp3 info", S_OK, 30);

                //MediaInfo mediaInfo = new MediaInfo("filename filename filename");
                //mediaInfo.Show();
            }
            else if (e.KeyData == Keys.O)
            {
                show_main_message1("開啟mp3/pdf檔案", S_OK, 30);
                openFileDialog1.Title = "開啟mp3/pdf檔案";
                openFileDialog1.FileName = "";              //預設開啟的檔名
                openFileDialog1.DefaultExt = "*.mp3";
                openFileDialog1.Filter = "mp3檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|MP4檔(*.mp4)|*.mp4|所有檔案(*.*)|*.*";   //存檔類型
                openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
                openFileDialog1.RestoreDirectory = true;
                //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
                //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
                openFileDialog1.Multiselect = false;    //單選
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    /*
                    richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    richTextBox1.Text += "Name: " + f.Name + "\n";
                    richTextBox1.Text += "FullName: " + f.FullName + "\n";
                    richTextBox1.Text += "Extension: " + f.Extension + "\n";
                    richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                    richTextBox1.Text += "Directory: " + f.Directory + "\n";
                    richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                    */





                }


            }
            else if (e.KeyData == Keys.M)
            {
                show_main_message1("開啟mp3檔案", S_OK, 30);
                openFileDialog1.Title = "開啟mp3檔案";
                openFileDialog1.FileName = "";              //預設開啟的檔名
                openFileDialog1.DefaultExt = "*.mp3";
                openFileDialog1.Filter = "mp3檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|MP4檔(*.mp4)|*.mp4|所有檔案(*.*)|*.*";   //存檔類型
                openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
                openFileDialog1.RestoreDirectory = true;
                //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
                //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
                openFileDialog1.Multiselect = false;    //單選
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    /*
                    richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    richTextBox1.Text += "Name: " + f.Name + "\n";
                    richTextBox1.Text += "FullName: " + f.FullName + "\n";
                    richTextBox1.Text += "Extension: " + f.Extension + "\n";
                    richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                    richTextBox1.Text += "Directory: " + f.Directory + "\n";
                    richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                    */

                    mp3_filename = openFileDialog1.FileName;
                    mp3_filename_short = Path.GetFileName(mp3_filename);
                    current_directory = Path.GetDirectoryName(mp3_filename);
                    mp3_position = 0;
                    axWindowsMediaPlayer1.URL = mp3_filename;
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
                    axWindowsMediaPlayer1.Ctlcontrols.play();
                    show_main_message1("檔案 : " + mp3_filename_short.ToString(), S_OK, 30);

                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    string foldername = f.DirectoryName;

                    DirectoryInfo di = new DirectoryInfo(foldername);

                    mp3_filename_list.Clear();

                    foreach (FileInfo fi in di.GetFiles())
                    {
                        if (fi.Extension.ToLower() == ".mp3")
                        {
                            mp3_filename_list.Add(fi.FullName);
                        }
                    }

                    total_mp3_count = mp3_filename_list.Count;

                    mp3_filename_list.Sort();

                    // 取出單一個List 裡的值，如同陣列(Array)用法
                    for (int i = 0; i < mp3_filename_list.Count; i++)
                    {
                        //richTextBox1.Text += mp3_filename_list[i] + "\n";
                        if (mp3_filename_list[i] == openFileDialog1.FileName)
                        {
                            current_mp3_index = i;
                            richTextBox1.Text += "select i = " + current_mp3_index.ToString() + "\n";
                        }
                    }


                    /*
                    richTextBox1.Text += "共有 " + mp3_filename_list.Count.ToString() + " 個字串\n";

                    mp3_filename_list.Sort();

                    // 取出單一個List 裡的值，如同陣列(Array)用法
                    for (int i = 0; i < mp3_filename_list.Count; i++)
                    {
                        richTextBox1.Text += mp3_filename_list[i] + "\n";
                    }
                    */

                    richTextBox1.Text += "len = " + total_mp3_count.ToString() + "\n";
                    richTextBox1.Text += "index = " + current_mp3_index.ToString() + "\n";

                }
                else
                {
                    show_main_message1("未選取檔案", S_OK, 30);
                    mp3_filename = "";
                    mp3_position = 0;
                }
                this.Focus();
                this.KeyPreview = true;
            }
            else if (e.KeyData == Keys.P)
            {
                show_main_message1("開啟pdf檔案", S_OK, 30);
                openFileDialog1.Title = "開啟pdf檔案";
                openFileDialog1.FileName = "";              //預設開啟的檔名
                openFileDialog1.DefaultExt = "*.pdf";
                openFileDialog1.Filter = "pdf檔(*.pdf)|*.pdf|所有檔案(*.*)|*.*";   //存檔類型
                //openFileDialog1.Filter = "mp3檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|MP4檔(*.mp4)|*.mp4|所有檔案(*.*)|*.*";   //存檔類型
                openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
                openFileDialog1.RestoreDirectory = true;
                //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
                //openFileDialog1.InitialDirectory = "c:\\";  //預設開啟的路徑
                openFileDialog1.Multiselect = false;    //單選
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    /*
                    richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                    FileInfo f = new FileInfo(openFileDialog1.FileName);
                    richTextBox1.Text += "Name: " + f.Name + "\n";
                    richTextBox1.Text += "FullName: " + f.FullName + "\n";
                    richTextBox1.Text += "Extension: " + f.Extension + "\n";
                    richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                    richTextBox1.Text += "Directory: " + f.Directory + "\n";
                    richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
                    */

                    /*
                    show_item_location(MODE_1);
                    pdf_filename = openFileDialog1.FileName;
                    pdf_filename_short = Path.GetFileName(pdf_filename);
                    current_directory = Path.GetDirectoryName(pdf_filename);
                    webBrowser1.Navigate(pdf_filename);
                    show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
                    pdf_page = 0;
                    tb_pdf_page.Text = pdf_page.ToString();
                    */
                }
                else
                {
                    show_main_message1("未選取檔案", S_OK, 30);
                    pdf_filename = "";
                }
                this.Focus();
                this.KeyPreview = true;
            }
            else if ((e.KeyData == Keys.D0) || (e.KeyData == Keys.NumPad0))
            {
                mp3_rate = 1;
                axWindowsMediaPlayer1.settings.rate = mp3_rate;
                show_main_message1("恢復速度 / 位置", S_OK, 30);
                /*
                int W = Screen.PrimaryScreen.WorkingArea.Width;
                int H = Screen.PrimaryScreen.WorkingArea.Height;

                if (flag_display_mode == MODE_0)
                {
                    this.ClientSize = new Size(W, mp3_player_height);
                    this.Location = new Point(0, H - mp3_player_height);
                }
                else
                {
                    this.ClientSize = new Size(W, H);
                    this.Location = new Point(0, 0);
                }
                */
            }
            else if (e.KeyCode == Keys.Up)
            {
                //show_main_message1("上", S_OK, 30);
                if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    if (mp3_rate < 1.0)
                    {
                        mp3_rate += 0.2;
                        axWindowsMediaPlayer1.settings.rate = mp3_rate;
                    }
                    else if (mp3_rate < 5.0)
                    {
                        mp3_rate += 0.5;
                        axWindowsMediaPlayer1.settings.rate = mp3_rate;
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (mp3_rate < 5.0)
                    {
                        mp3_rate += 0.1;
                        axWindowsMediaPlayer1.settings.rate = mp3_rate;
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else
                {
                    if (mp3_volume <= 95)
                    {
                        mp3_volume += 5;
                        axWindowsMediaPlayer1.settings.volume = mp3_volume;
                    }
                    show_main_message1("音量 : " + mp3_volume.ToString(), S_OK, 30);
                }
            }
            else if (e.KeyCode == Keys.Down)
            {
                //show_main_message1("下", S_OK, 30);
                if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    if (mp3_rate >= 1.5)
                    {
                        mp3_rate -= 0.5;
                        axWindowsMediaPlayer1.settings.rate = mp3_rate;
                    }
                    else if (mp3_rate > 0.6)
                    {
                        mp3_rate -= 0.2;
                        axWindowsMediaPlayer1.settings.rate = mp3_rate;
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (mp3_rate > 0.6)
                    {
                        mp3_rate -= 0.1;
                        axWindowsMediaPlayer1.settings.rate = mp3_rate;
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else
                {
                    if (mp3_volume >= 5)
                    {
                        mp3_volume -= 5;
                        axWindowsMediaPlayer1.settings.volume = mp3_volume;
                    }
                    show_main_message1("音量 : " + mp3_volume.ToString(), S_OK, 30);
                }
            }
            else if (e.KeyCode == Keys.Left)
            {
                int amount = 0;
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    show_main_message1("CTRL + 左", S_OK, 30);
                    amount = 60;
                }
                else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    show_main_message1("SHIFT + 左", S_OK, 30);
                    amount = 120;
                }
                else if ((Control.ModifierKeys & Keys.Alt) == Keys.Alt)
                {
                    show_main_message1("ALT + 左", S_OK, 30);
                    amount = 180;
                }
                else
                {
                    show_main_message1("左", S_OK, 30);
                    amount = 10;
                }

                //檢查過頭
                if (axWindowsMediaPlayer1.Ctlcontrols.currentPosition <= amount)
                {
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = 0;
                    show_main_message1("快退至起點", S_OK, 30);
                }
                else
                {
                    //快退
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition -= amount;
                    show_main_message1("快退 : " + amount.ToString(), S_OK, 30);
                }
            }
            else if (e.KeyCode == Keys.Right)
            {
                int amount = 0;
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    show_main_message1("CTRL + 右", S_OK, 30);
                    amount = 60;
                }
                else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    show_main_message1("SHIFT + 右", S_OK, 30);
                    amount = 120;
                }
                else if ((Control.ModifierKeys & Keys.Alt) == Keys.Alt)
                {
                    show_main_message1("ALT + 右", S_OK, 30);
                    amount = 180;
                }
                else
                {
                    show_main_message1("右", S_OK, 30);
                    amount = 10;
                }

                //檢查過頭
                if ((axWindowsMediaPlayer1.Ctlcontrols.currentPosition + amount) > axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration)
                {
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration - 10;
                    show_main_message1("快進至檔尾" + amount.ToString(), S_OK, 30);
                }
                else
                {
                    //快進
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition += amount;
                    show_main_message1("快進 : " + amount.ToString(), S_OK, 30);
                }
            }
            else if ((e.KeyData == Keys.Space) || (e.KeyData == Keys.Enter))
            {
                //show_main_message1("空白鍵", S_OK, 30);
                //richTextBox1.Text += "state = " + axWindowsMediaPlayer1.playState + "\n";
                if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
                {
                    axWindowsMediaPlayer1.Ctlcontrols.pause();
                    show_main_message1("暫停", S_OK, 100);
                }
                else
                {
                    axWindowsMediaPlayer1.Ctlcontrols.play();
                    show_main_message1("播放", S_OK, 30);
                }
            }
        }

        int flag_mouse_down_mode = 0;   //nothing

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down_mode = 1;   //move position mode
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down_mode = 0;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int x_st = 0;
            int y_st = H * 3 / 4;

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(Color.Black);

            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
            {
                int total = (int)axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration;
                int current = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;

                SolidBrush sb = new SolidBrush(Color.Green);
                //e.Graphics.FillRectangle(sb, 0, 0, W * current / total, H);

                x_st = W * current / total;

                int linewidth = 5;
                e.Graphics.DrawLine(new Pen(Color.Gold, linewidth), 0, y_st, x_st, y_st);
                e.Graphics.DrawLine(new Pen(Color.Gray, linewidth), x_st, y_st, W, y_st);

                int r = 16;
                if (flag_mouse_down_mode == 2)
                {
                    e.Graphics.FillEllipse(Brushes.Red, x_st - r / 2, y_st - r / 2, r, r);
                    e.Graphics.DrawEllipse(new Pen(Color.White, 2), x_st - r / 2, y_st - r / 2, r, r);
                }
                else
                {
                    e.Graphics.FillEllipse(Brushes.White, x_st - r / 2, y_st - r / 2, r, r);
                    e.Graphics.DrawEllipse(new Pen(Color.Blue, 2), x_st - r / 2, y_st - r / 2, r, r);
                }

                Font f = new Font("標楷體", 14);

                int tmp_width = 0;
                int tmp_height = 0;

                string title = axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");
                string author = axWindowsMediaPlayer1.currentMedia.getItemInfo("Author");
                string artist = axWindowsMediaPlayer1.currentMedia.getItemInfo("Artist");

                title = Path.GetFileName(mp3_filename) + "  ( " + title + " / " + author + " )";

                tmp_height = e.Graphics.MeasureString(title, f).ToSize().Height;
                y_st = (H - tmp_height) / 4;
                e.Graphics.DrawString(title, f, sb, new PointF(10, y_st));

                string current_time = DateTime.Now.ToString("HH:mm:ss");
                string play_info = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + " / " + axWindowsMediaPlayer1.Ctlcontrols.currentItem.durationString
                    + " (" + ((int)((100 * axWindowsMediaPlayer1.Ctlcontrols.currentPosition / axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration))).ToString() + " %) "
                    + current_time;

                tmp_width = e.Graphics.MeasureString(play_info, f).ToSize().Width;
                tmp_height = e.Graphics.MeasureString(play_info, f).ToSize().Height;
                //richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";

                y_st = (H - tmp_height) / 4;
                e.Graphics.DrawString(play_info, f, sb, new PointF(W - tmp_width - 10, y_st));
            }
            else
            {
                e.Graphics.DrawLine(new Pen(Color.Gray, 10), 0, y_st, W, y_st);
            }
            e.Graphics.DrawRectangle(new Pen(Color.Red, 1), 0, 0, W - 1, H - 1);
        }
    }
}

