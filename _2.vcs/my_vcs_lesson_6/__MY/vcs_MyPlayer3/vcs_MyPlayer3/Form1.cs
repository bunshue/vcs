using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D; //for SmoothingMode
using System.Runtime.InteropServices;   //for DllImport

using AxWMPLib;
/*
點開 方案總管/vcs_XXXXX/Properties/Settings.settings

加入要儲存的參數 的 名稱 型別 預設值

若是數字 一定要給預設值
*/

/*  sugar
使用AxWindowsMediaPlayer播放多媒體

加入工具箱

工具箱/滑鼠右鍵/選擇項目/
/COM元件 頁籤 /勾選Windows Media Player(wmp.dll)	/ 確定

會發現工具箱多了個Windows Media Player的控制項
就是 axWindowsMediaPlayer

*/

namespace vcs_MyPlayer3
{
    public partial class Form1 : Form
    {
        int flag_display_mode = MODE_0;

        private const int MODE_0 = 0x00;   //mp3 only
        private const int MODE_1 = 0x01;   //mp3 + pdf

        private const int PDF_ZOOM_FACTOR = 130;

        string mp3_filename = string.Empty;
        string pdf_filename = string.Empty;
        string mp3_filename_short = string.Empty;
        string pdf_filename_short = string.Empty;
        string current_directory = string.Empty;
        bool flag_already_use_webbrowser = false;

        int W = Screen.PrimaryScreen.WorkingArea.Width;
        int H = Screen.PrimaryScreen.WorkingArea.Height;
        int mp3_position = 0;
        int mp3_volume = 50;
        double mp3_rate = 1.0;
        int mp3_player_height = 50;
        int debug_panel_width = 128;
        int debug_panel_height = 0;

        int pdf_page = 0;

        List<String> mp3_filename_list = new List<String>();
        int current_mp3_index = 0;
        int total_mp3_count = 0;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        AxWindowsMediaPlayer axWindowsMediaPlayer1;
        WebBrowser webBrowser1;
        TextBox tb_pdf_page = new TextBox();
        RichTextBox richTextBox1 = new RichTextBox();
        Panel panel1 = new Panel();

        //在控件上加ToolTip
        ToolTip tooltip = new ToolTip();

        bool flag_debug_mode = true;
        bool flag_repeat_mode = true;

        public Form1()
        {
            InitializeComponent();
        }

        //移動無邊框窗體 ST
        [DllImport("user32.dll")]
        public static extern bool ReleaseCapture();
        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);
        public const int WM_SYSCOMMAND = 0x0112;
        public const int SC_MOVE = 0xF010;
        public const int HTCAPTION = 0x0002;
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            ReleaseCapture();
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0);
        }
        //移動無邊框窗體 SP

        void Init_Controls()
        {
            this.panel1.BackColor = Color.Pink;
            this.panel1.Location = new System.Drawing.Point(W - debug_panel_width, 0);
            this.panel1.Size = new System.Drawing.Size(debug_panel_width, debug_panel_height);
            this.Controls.Add(this.panel1);

            this.richTextBox1.Location = new System.Drawing.Point(0, debug_panel_height / 2);
            this.richTextBox1.Size = new System.Drawing.Size(debug_panel_width, debug_panel_height / 2);
            this.panel1.Controls.Add(this.richTextBox1);

            if (flag_debug_mode == false)
            {
                this.panel1.Visible = false;

                //正常使用
                this.webBrowser1 = new WebBrowser();
                this.webBrowser1.Location = new System.Drawing.Point(0, 0);
                //this.webBrowser1.Name = "webBrowser1";
                this.webBrowser1.Size = new System.Drawing.Size(W - 10, H - mp3_player_height);
                //this.webBrowser1.TabIndex = 2;
                //this.webBrowser1.Visible = false;   //fail
                this.Controls.Add(this.webBrowser1);
            }
            else
            {
                this.panel1.Visible = true;
                //debug模式
                this.webBrowser1 = new WebBrowser();
                this.webBrowser1.Location = new System.Drawing.Point(0, 0);
                //this.webBrowser1.Name = "webBrowser1";
                this.webBrowser1.Size = new System.Drawing.Size(W - debug_panel_width, H - mp3_player_height);
                //this.webBrowser1.TabIndex = 2;
                //this.webBrowser1.Visible = false;   //fail
                this.Controls.Add(this.webBrowser1);

                int w = 120;
                int h = 120;
                tb_pdf_page.Width = w / 2;
                tb_pdf_page.Height = h / 2;
                tb_pdf_page.Font = new Font("Arial", 20);
                tb_pdf_page.Text = "5";
                //this.tb_file_l.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.textBox1_KeyPress);
                tb_pdf_page.KeyPress += new System.Windows.Forms.KeyPressEventHandler(tb_pdf_page_KeyPress);
                tb_pdf_page.TextAlign = HorizontalAlignment.Center;
                tb_pdf_page.Location = new Point(0, this.panel1.Height / 2 - tb_pdf_page.Height);
                this.panel1.Controls.Add(tb_pdf_page);    // 將控件加入表單
                tb_pdf_page.BringToFront();
            }

            this.axWindowsMediaPlayer1 = new AxWindowsMediaPlayer();
            this.axWindowsMediaPlayer1.Enabled = true;
            //this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(0, 400);
            //this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            //this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(800, 500);
            //this.axWindowsMediaPlayer1.TabIndex = 2;
            //this.axWindowsMediaPlayer1.Visible = false;   //fail
            this.axWindowsMediaPlayer1.StatusChange += new EventHandler(axWindowsMediaPlayer1_StatusChange);
            this.Controls.Add(this.axWindowsMediaPlayer1);
        }

        protected void axWindowsMediaPlayer1_StatusChange(object sender, EventArgs e)
        {
            //richTextBox1.Text += "play state = " + axWindowsMediaPlayer1.playState.ToString() + "\n";
            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
            {
                this.pictureBox1.Invalidate();
            }
            else if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsStopped)
            {
                this.pictureBox1.Invalidate();
                mp3_position = 0;

                //判断视频是否已停止播放
                if (flag_repeat_mode == true)
                {
                    //停顿2秒钟再重新播放
                    System.Threading.Thread.Sleep(2000);
                    //重新播放
                    axWindowsMediaPlayer1.Ctlcontrols.play();
                }
            }

            //通过控件的状态改变，来实现视频循环播放
            /*  0 Undefined Windows Media Player is in an undefined state.(未定义)
                1 Stopped Playback of the current media item is stopped.(停止)
                2 Paused Playback of the current media item is paused. When a media item is paused, resuming playback begins from the same location.(停留)
                3 Playing The current media item is playing.(播放)
                4 ScanForward The current media item is fast forwarding.
                5 ScanReverse The current media item is fast rewinding.
                6 Buffering The current media item is getting additional data from the server.(转换)
                7 Waiting Connection is established, but the server is not sending data. Waiting for session to begin.(暂停)
                8 MediaEnded Media item has completed playback. (播放结束)
                9 Transitioning Preparing new media item.
                10 Ready Ready to begin playing.(准备就绪)
                11 Reconnecting Reconnecting to stream.(重新连接)
            */

            //flag_repeat_mode
        }

        void show_item_location(int mode)
        {
            //使用ToolTip
            tooltip.ForeColor = Color.Blue;	//ForeColor:取得或設定工具提示的前景色彩
            tooltip.BackColor = Color.LightGray;	//BackColor:取得或設定工具提示的背景色彩.
            tooltip.AutoPopDelay = 5000;	//AutoPopDelay:當指標靜止於控制項上時,ToolTip 保持可見的時間 (以毫秒為單位).預設值為 5000.

            int W = Screen.PrimaryScreen.WorkingArea.Width;
            int H = Screen.PrimaryScreen.WorkingArea.Height;

            if (mode == MODE_0)
            {
                this.ClientSize = new Size(W, mp3_player_height);
                this.Location = new Point(0, H - mp3_player_height);
            }
            else
            {
                this.ClientSize = new Size(W, H);
                this.Location = new Point(0, 0);

                if (flag_already_use_webbrowser == false)
                {
                    bt_control_setup();
                    flag_already_use_webbrowser = true;
                }
            }

            this.pictureBox1.Size = new Size(this.pictureBox1.Size.Width, mp3_player_height);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            //this.ShowInTaskbar = false;
            this.KeyPreview = true;
            //this.TopMost = true;

            lb_main_mesg1.Location = new Point(W / 2, this.pictureBox1.Location.Y + 2);
            lb_main_mesg1.Text = "";
            lb_main_mesg1.BringToFront();
            this.Text = "MP3 Player";
        }

        void bt_control_setup()
        {
            int linewidth = 5;
            Bitmap bmp;
            Graphics g;
            Pen p = new Pen(Color.Red, linewidth);
            int type = 0;       //種類
            int x_st = 0;     //icon的 位置 X
            int y_st = 0;     //icon的 位置 Y
            int width = 40; //設定按鈕大小 W
            int height = 40; //設定按鈕大小 H
            int dx = width + 2;
            int dy = height + 2;
            int X = 2;    //這一群按鍵的起始點(最左邊)
            int Y = 150;

            width = 50;
            height = 50;

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(width, height);
            bt_exit.Text = "";
            bmp = new Bitmap(width, height);
            bt_exit.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, linewidth + 1, linewidth + 1, width - 1 - (linewidth + 1) * 2, height - 1 - (linewidth + 1) * 2);
            g.DrawLine(p, 0, 0, width - 1, height - 1);
            g.DrawLine(p, width - 1, 0, 0, height - 1);
            bt_exit.Location = new Point(this.panel1.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(width, height);
            bt_minimize.Text = "";
            bmp = new Bitmap(width, height);
            bt_minimize.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, linewidth + 1, linewidth + 1, width - 1 - (linewidth + 1) * 2, height - 1 - (linewidth + 1) * 2);
            g.DrawLine(p, width / 4, height / 2 - 1, width * 3 / 4, height / 2 - 1);
            bt_minimize.Location = new Point(this.panel1.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層

            width = 40;
            height = 40;

            type = ICON_LEFT;
            x_st = X + dx * 0;
            y_st = Y + dy * 0;
            Button bt_left = new Button();  // 實例化按鈕
            bt_left.Size = new Size(width, height);
            bt_left.Text = "";
            bmp = new Bitmap(width, height);
            bt_left.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_left.Location = new Point(x_st, y_st);
            bt_left.Click += bt_left_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_left); // 將按鈕加入表單
            bt_left.BringToFront();     //移到最上層

            type = ICON_PLAY_PAUSE;
            x_st = X + dx * 1;
            y_st = Y + dy * 0;
            Button bt_play_pause = new Button();  // 實例化按鈕
            bt_play_pause.Size = new Size(width, height);
            bt_play_pause.Text = "";
            bmp = new Bitmap(width, height);
            bt_play_pause.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_play_pause.Location = new Point(x_st, y_st);
            bt_play_pause.Click += bt_play_pause_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_play_pause); // 將按鈕加入表單
            bt_play_pause.BringToFront();     //移到最上層

            type = ICON_RIGHT;
            x_st = X + dx * 2;
            y_st = Y + dy * 0;
            Button bt_right = new Button();  // 實例化按鈕
            bt_right.Size = new Size(width, height);
            bt_right.Text = "";
            bmp = new Bitmap(width, height);
            bt_right.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_right.Location = new Point(x_st, y_st);
            bt_right.Click += bt_right_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_right); // 將按鈕加入表單
            bt_right.BringToFront();     //移到最上層

            type = ICON_UP;
            x_st = X + dx * 1;
            y_st = Y - dy * 1;
            Button bt_up = new Button();  // 實例化按鈕
            bt_up.Size = new Size(width, height);
            bt_up.Text = "";
            bmp = new Bitmap(width, height);
            bt_up.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_up.Location = new Point(x_st, y_st);
            bt_up.Click += bt_up_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_up); // 將按鈕加入表單
            bt_up.BringToFront();     //移到最上層

            type = ICON_DOWN;
            x_st = X + dx * 1;
            y_st = Y + dy * 1;
            Button bt_down = new Button();  // 實例化按鈕
            bt_down.Size = new Size(width, height);
            bt_down.Text = "";
            bmp = new Bitmap(width, height);
            bt_down.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_down.Location = new Point(x_st, y_st);
            bt_down.Click += bt_down_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_down); // 將按鈕加入表單
            bt_down.BringToFront();     //移到最上層

            type = ICON_PLUS;
            x_st = X + dx * 2;
            y_st = Y - dy * 1;
            Button bt_plus = new Button();  // 實例化按鈕
            bt_plus.Size = new Size(width, height);
            bt_plus.Text = "";
            bmp = new Bitmap(width, height);
            bt_plus.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_plus.Location = new Point(x_st, y_st);
            bt_plus.Click += bt_plus_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_plus); // 將按鈕加入表單
            bt_plus.BringToFront();     //移到最上層

            type = ICON_MINUS;
            x_st = X + dx * 2;
            y_st = Y + dy * 1;
            Button bt_minus = new Button();  // 實例化按鈕
            bt_minus.Size = new Size(width, height);
            bt_minus.Text = "";
            bmp = new Bitmap(width, height);
            bt_minus.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_minus.Location = new Point(x_st, y_st);
            bt_minus.Click += bt_minus_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_minus); // 將按鈕加入表單
            bt_minus.BringToFront();     //移到最上層

            type = ICON_PREVIOUS;
            x_st = X + dx * 1;
            y_st = Y + dy * 2;
            Button bt_previous = new Button();  // 實例化按鈕
            bt_previous.Size = new Size(width, height);
            bt_previous.Text = "";
            bmp = new Bitmap(width, height);
            bt_previous.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_previous.Location = new Point(x_st, y_st);
            bt_previous.Click += bt_previous_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_previous); // 將按鈕加入表單
            bt_previous.BringToFront();     //移到最上層

            type = ICON_NEXT;
            x_st = X + dx * 2;
            y_st = Y + dy * 2;
            Button bt_next = new Button();  // 實例化按鈕
            bt_next.Size = new Size(width, height);
            bt_next.Text = "";
            bmp = new Bitmap(width, height);
            bt_next.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);
            draw_icon(g, type, 0, 0, width, height, Color.Red);
            bt_next.Location = new Point(x_st, y_st);
            bt_next.Click += bt_next_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_next); // 將按鈕加入表單
            bt_next.BringToFront();     //移到最上層

            Font f = new Font("Arial", 12);
            SolidBrush sb = new SolidBrush(Color.Red);

            x_st = X + dx * 1;
            y_st = Y + dy * 3;
            Button bt_open_pdf = new Button();  // 實例化按鈕
            bt_open_pdf.Size = new Size(width, height);
            bt_open_pdf.Text = "";
            bmp = new Bitmap(width, height);
            bt_open_pdf.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);

            g.DrawString("pdf", f, sb, new PointF(2, 10));

            bt_open_pdf.Location = new Point(x_st, y_st);
            bt_open_pdf.Click += bt_open_pdf_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_open_pdf); // 將按鈕加入表單
            bt_open_pdf.BringToFront();     //移到最上層

            x_st = X + dx * 2;
            y_st = Y + dy * 3;
            Button bt_open_mp3 = new Button();  // 實例化按鈕
            bt_open_mp3.Size = new Size(width, height);
            bt_open_mp3.Text = "";
            bmp = new Bitmap(width, height);
            bt_open_mp3.Image = bmp;
            g = Graphics.FromImage(bmp);
            g.Clear(Color.Pink);

            g.DrawString("mp3", f, sb, new PointF(2, 10));

            bt_open_mp3.Location = new Point(x_st, y_st);
            bt_open_mp3.Click += bt_open_mp3_Click;     // 加入按鈕事件
            this.panel1.Controls.Add(bt_open_mp3); // 將按鈕加入表單
            bt_open_mp3.BringToFront();     //移到最上層

            //使用ToolTip
            tooltip.SetToolTip(bt_exit, "關閉");
            tooltip.SetToolTip(bt_minimize, "最小化");
            tooltip.SetToolTip(bt_next, "下一首");
            tooltip.SetToolTip(bt_previous, "上一首");
            tooltip.SetToolTip(bt_up, "快速播放");
            tooltip.SetToolTip(bt_down, "慢速播放");
            tooltip.SetToolTip(bt_left, "後退10秒");
            tooltip.SetToolTip(bt_right, "快進10秒");
            tooltip.SetToolTip(bt_plus, "增加音量");
            tooltip.SetToolTip(bt_minus, "降低音量");
            tooltip.SetToolTip(bt_play_pause, "播放/暫停");
            tooltip.SetToolTip(bt_open_pdf, "開啟pdf檔案");
            tooltip.SetToolTip(bt_open_mp3, "開啟mp3檔案");
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            do_close();
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_right_Click(object sender, EventArgs e)
        {
            int amount = 0;
            show_main_message1("右", S_OK, 30);
            amount = 10;
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

        private void bt_left_Click(object sender, EventArgs e)
        {
            int amount = 0;
            show_main_message1("左", S_OK, 30);
            amount = 10;
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

        private void bt_up_Click(object sender, EventArgs e)
        {
            do_up();
        }

        private void bt_down_Click(object sender, EventArgs e)
        {
            do_down();
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            do_plus();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            do_minus();
        }

        private void bt_previous_Click(object sender, EventArgs e)
        {
            //show_main_message1("上一首", S_OK, 30);
            do_previous();
        }

        private void bt_next_Click(object sender, EventArgs e)
        {
            //show_main_message1("下一首", S_OK, 30);
            do_next();
        }

        private void bt_open_pdf_Click(object sender, EventArgs e)
        {
            show_main_message1("開啟pdf", S_OK, 30);
            do_open_pdf();
        }

        private void bt_open_mp3_Click(object sender, EventArgs e)
        {
            show_main_message1("開啟mp3", S_OK, 30);
            do_open_mp3();
        }

        private void bt_play_pause_Click(object sender, EventArgs e)
        {
            show_main_message1("播放/暫停", S_OK, 30);
            do_play_pause();
        }

        private void tb_pdf_page_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                this.richTextBox1.Focus();
                e.Handled = true;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            debug_panel_height = H - mp3_player_height;

            Init_Controls();

            bool flag_use_autoload_mp3_file = false;
            bool flag_use_autoload_pdf_file = false;

            flag_display_mode = MODE_0;

            if (Environment.GetCommandLineArgs().Length == 2)
            {
                string filename = Environment.GetCommandLineArgs()[1];

                var GetExtension = Path.GetExtension(filename);

                if (GetExtension.ToLower() == ".mp3")
                {
                    mp3_filename = filename;
                    mp3_position = 0;
                    mp3_filename_short = Path.GetFileName(filename);
                    current_directory = Path.GetDirectoryName(filename);

                    flag_use_autoload_mp3_file = true;
                    flag_display_mode = MODE_0;
                }
                else if (GetExtension.ToLower() == ".pdf")
                {
                    if (File.Exists(filename) == true)
                    {
                        pdf_filename = filename;
                        pdf_filename_short = Path.GetFileName(pdf_filename);
                        current_directory = Path.GetDirectoryName(pdf_filename);
                        webBrowser1.Navigate(pdf_filename);

                        flag_use_autoload_pdf_file = true;
                        flag_display_mode = MODE_1;
                    }
                }
            }

            int i = 0;
            foreach (string arg in Environment.GetCommandLineArgs())
            {
                //lb_main_mesg1.Text += "第 " + i.ToString() + " 項 : " + arg + "\n";
                i++;
            }

            /*
            richTextBox1.Text += "取得預設資料 :\n";
            richTextBox1.Text += "filename : \t" + Properties.Settings.Default.filename + "\n";
            richTextBox1.Text += "position : \t" + Properties.Settings.Default.position.ToString() + "\n";
            */

            //區分顯示模式
            flag_display_mode = MODE_0;
            if (flag_use_autoload_mp3_file == false)
            {
                mp3_filename = Properties.Settings.Default.mp3_filename;
                mp3_position = Properties.Settings.Default.position;
                flag_display_mode = MODE_0;
                if (File.Exists(mp3_filename) == true)
                {
                    mp3_filename_short = Path.GetFileName(mp3_filename);
                    current_directory = Path.GetDirectoryName(mp3_filename);
                }
            }

            if (flag_use_autoload_pdf_file == false)
            {
                pdf_filename = Properties.Settings.Default.pdf_filename;
                pdf_page = Properties.Settings.Default.pdf_page;

                if (pdf_page == -1)
                {
                    pdf_page = 0;
                }
                tb_pdf_page.Text = pdf_page.ToString();

                if (File.Exists(pdf_filename) == true)
                {
                    pdf_filename_short = Path.GetFileName(pdf_filename);
                    current_directory = Path.GetDirectoryName(pdf_filename);

                    //預設
                    //webBrowser1.Navigate(pdf_filename);

                    //指名頁數
                    if (pdf_page > 0)
                    {
                        webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0&page=" + pdf_page.ToString());
                    }
                    else
                    {
                        webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0");
                    }

                    flag_display_mode = MODE_1;
                    show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
                }
            }
            show_item_location(flag_display_mode);

            mp3_volume = Properties.Settings.Default.volume;
            if (mp3_volume == -1)
            {
                mp3_volume = 50;
            }
            axWindowsMediaPlayer1.Visible = false;
            if (File.Exists(mp3_filename) == true)
            {
                axWindowsMediaPlayer1.URL = mp3_filename;

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

            axWindowsMediaPlayer1.settings.volume = mp3_volume;
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
            //axWindowsMediaPlayer1.Ctlcontrols.stop();

            //show_main_message1("音量 : " + mp3_volume.ToString(), S_OK, 30);

            //this.Focus();
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
                do_previous();
            }
            else if (e.KeyData == Keys.PageDown)
            {
                do_next();
            }
            else if ((e.KeyData == Keys.Escape) || (e.KeyData == Keys.X))
            {
                do_close();
            }
            else if (e.KeyData == Keys.Back)
            {
                axWindowsMediaPlayer1.Ctlcontrols.currentPosition = 0;
                show_main_message1("快退至起點", S_OK, 30);
            }
            else if (e.KeyData == Keys.H)
            {
                show_main_message1("Help", S_OK, 30);

                Help help = new Help();
                help.Show();
            }
            else if (e.KeyData == Keys.I)
            {
                show_main_message1("mp3 info", S_OK, 30);

                MediaInfo mediaInfo = new MediaInfo("filename filename filename");
                mediaInfo.Show();
            }
            else if (e.KeyData == Keys.O)
            {
                do_open_files();    //開啟 pdf或mp3 檔案
            }
            else if (e.KeyData == Keys.M)
            {
                do_open_mp3();
            }
            else if (e.KeyData == Keys.P)
            {
                do_open_pdf();
            }
            else if ((e.KeyData == Keys.D0) || (e.KeyData == Keys.NumPad0))
            {
                mp3_rate = 1;
                axWindowsMediaPlayer1_setup_rate(mp3_rate);
                show_main_message1("恢復速度 / 位置", S_OK, 30);

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
            }
            else if (e.KeyCode == Keys.Up)
            {
                //show_main_message1("上", S_OK, 30);
                if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    if (mp3_rate < 1.0)
                    {
                        mp3_rate += 0.2;
                        axWindowsMediaPlayer1_setup_rate(mp3_rate);
                    }
                    else if (mp3_rate < 5.0)
                    {
                        mp3_rate += 0.5;
                        axWindowsMediaPlayer1_setup_rate(mp3_rate);
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (mp3_rate < 5.0)
                    {
                        mp3_rate += 0.1;
                        axWindowsMediaPlayer1_setup_rate(mp3_rate);
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else
                {
                    int amount = 5;
                    axWindowsMediaPlayer1_setup_volume(true, amount);
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
                        axWindowsMediaPlayer1_setup_rate(mp3_rate);
                    }
                    else if (mp3_rate > 0.6)
                    {
                        mp3_rate -= 0.2;
                        axWindowsMediaPlayer1_setup_rate(mp3_rate);
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    if (mp3_rate > 0.6)
                    {
                        mp3_rate -= 0.1;
                        axWindowsMediaPlayer1_setup_rate(mp3_rate);
                    }
                    show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
                }
                else
                {
                    int amount = 5;
                    axWindowsMediaPlayer1_setup_volume(false, amount);
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
                axWindowsMediaPlayer1_setup_currentPosition(false, amount);
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
                axWindowsMediaPlayer1_setup_currentPosition(true, amount);
            }
            else if ((e.KeyData == Keys.Space) || (e.KeyData == Keys.Enter))
            {
                do_play_pause();
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            do_close();
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

        bool flag_mouse_down = false;
        int flag_mouse_down_mode = 0;   //nothing
        int flag_mouse_down_position = 0;
        int flag_mouse_move_position = 0;
        int flag_mouse_up_position = 0;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            flag_mouse_down_position = e.X;
            //show_main_message1(flag_mouse_down_position.ToString(), S_OK, 30);

            int H = pictureBox1.Height;
            if (e.Y < H * 3 / 5)
            {
                //richTextBox1.Text += "A h = " + H.ToString() + ", e.Y = " + e.Y.ToString() + ", H = " + this.ClientSize.Height.ToString() + ", xx = " + (this.ClientSize.Height - H * 3 / 5).ToString() + "\n";
                flag_mouse_down_mode = 1;   //move position mode
                Form1_MouseDown(sender, e);
            }
            else
            {
                //richTextBox1.Text += "BBB";
                flag_mouse_down_mode = 2;   //move play position mode
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                flag_mouse_move_position = e.X;
                //show_main_message1(flag_mouse_move_position.ToString(), S_OK, 30);

                if (flag_mouse_down_mode == 2)
                {
                    if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
                    {
                        int total = (int)axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration;
                        int W = pictureBox1.Width;
                        axWindowsMediaPlayer1.Ctlcontrols.currentPosition = total * e.X / W;
                        show_main_message1("移動播放位置", S_OK, 10);
                        this.pictureBox1.Invalidate();
                    }
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                flag_mouse_up_position = e.X;
                //show_main_message1(flag_mouse_up_position.ToString(), S_OK, 30);
                flag_mouse_down = false;
                flag_mouse_down_mode = 0;

                if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
                {
                    int total = (int)axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration;
                    int W = pictureBox1.Width;
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = total * e.X / W;
                    show_main_message1("移動播放位置", S_OK, 10);
                    this.pictureBox1.Invalidate();
                }
            }
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            //useless??

            /*
            if (this.TopMost == false)
            {
                this.TopMost = true;
                show_main_message1("置頂", S_OK, 30);
            }
            else
            {
                this.TopMost = false;
                show_main_message1("取消置頂", S_OK, 30);
            }
            */
            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
            {
                axWindowsMediaPlayer1.Ctlcontrols.pause();
                show_main_message1("暫停X", S_OK, 100);
            }
            else
            {
                axWindowsMediaPlayer1.Ctlcontrols.play();
                show_main_message1("播放", S_OK, 30);
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsPlaying)
            {
                mp3_position = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;
                this.pictureBox1.Invalidate();
            }
        }

        void do_exit()	//關閉
        {

        }

        void do_minimize()	//最小化
        {

        }

        void do_next()	//下一首
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

        void do_previous()	//上一首
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

        void do_up()	//上
        {
            if (mp3_rate < 5.0)
            {
                mp3_rate += 0.1;
                axWindowsMediaPlayer1_setup_rate(mp3_rate);
            }
            show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
        }

        void do_down()	//下
        {
            if (mp3_rate > 0.6)
            {
                mp3_rate -= 0.1;
                axWindowsMediaPlayer1_setup_rate(mp3_rate);
            }
            show_main_message1("播放速度 : " + mp3_rate.ToString("F1") + " X", S_OK, 30);
        }

        void do_left()	//左
        {
            int amount = 10;
            show_main_message1("左", S_OK, 30);
            axWindowsMediaPlayer1_setup_currentPosition(false, amount);
        }

        void do_right()	//右
        {
            int amount = 10;
            show_main_message1("右", S_OK, 30);
            axWindowsMediaPlayer1_setup_currentPosition(true, amount);
        }

        void axWindowsMediaPlayer1_setup_currentPosition(bool dir, int amount)
        {
            if (dir == true)   //forward
            {
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
            else    //backward
            {
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
        }

        void axWindowsMediaPlayer1_setup_volume(bool dir, int amount)
        {
            if (dir == true)   //volume up
            {
                if (mp3_volume <= 95)
                {
                    mp3_volume += 5;
                    axWindowsMediaPlayer1.settings.volume = mp3_volume;
                }
            }
            else   //volume down
            {
                if (mp3_volume >= 5)
                {
                    mp3_volume -= 5;
                    axWindowsMediaPlayer1.settings.volume = mp3_volume;
                }
            }
            show_main_message1("音量 : " + mp3_volume.ToString(), S_OK, 30);
        }

        void axWindowsMediaPlayer1_setup_rate(double rate)
        {
            axWindowsMediaPlayer1.settings.rate = mp3_rate;
        }

        void do_plus()	//+
        {
            int amount = 5;
            axWindowsMediaPlayer1_setup_volume(true, amount);
        }

        void do_minus()	//-
        {
            int amount = 5;
            axWindowsMediaPlayer1_setup_volume(false, amount);
        }

        void do_play_pause()	//播放/暫停
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

        void do_open_pdf()	//開啟pdf檔案
        {
            show_main_message1("開啟pdf檔案", S_OK, 30);
            openFileDialog1.Title = "開啟pdf檔案";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.pdf";
            openFileDialog1.Filter = "pdf檔(*.pdf)|*.pdf";
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
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

                show_item_location(MODE_1);
                pdf_filename = openFileDialog1.FileName;
                pdf_filename_short = Path.GetFileName(pdf_filename);
                current_directory = Path.GetDirectoryName(pdf_filename);
                webBrowser1.Navigate(pdf_filename);
                show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
                pdf_page = 0;
                tb_pdf_page.Text = pdf_page.ToString();
            }
            else
            {
                show_main_message1("未選取檔案", S_OK, 30);
                pdf_filename = "";
            }
            //this.Focus();
            this.KeyPreview = true;
        }

        void do_open_mp3()	//開啟mp3檔案
        {
            show_main_message1("開啟mp3檔案", S_OK, 30);
            openFileDialog1.Title = "開啟mp3檔案";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.mp3";
            openFileDialog1.Filter = "音樂檔案(*.mp3,*.wav,*.flac)|*.mp3;*.wav;*.flac";
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
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
            //this.Focus();
            this.KeyPreview = true;
        }

        void do_open_files()	//開啟 pdf或mp3 檔案
        {
            show_main_message1("開啟mp3/pdf檔案", S_OK, 30);
            openFileDialog1.Title = "開啟mp3/pdf檔案";
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.mp3";
            openFileDialog1.Filter = "開啟檔案(*.pdf,*.mp3,*.wav,*.flac)|*.pdf;*.mp3;*.wav;*.flac";
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
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

        void do_close()	//關閉程式
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

        private const int ICON_EMPTY = 0;   //空白
        private const int ICON_PLAY = 1;   //播放
        private const int ICON_PLAY_PAUSE = 2;   //播放/暫停
        private const int ICON_PAUSE = 3;   //暫停
        private const int ICON_STOP = 4;   //停止
        private const int ICON_NEXT = 5;   //下一首
        private const int ICON_PREVIOUS = 6;   //上一首
        private const int ICON_FASTF = 7;   //快進
        private const int ICON_REVERSEF = 8;   //快退
        private const int ICON_RECORD = 9;   //錄影
        private const int ICON_PLUS = 10;   //加
        private const int ICON_MINUS = 11;   //減
        private const int ICON_UP = 12;   //上
        private const int ICON_DOWN = 13;   //下
        private const int ICON_LEFT = 14;   //左
        private const int ICON_RIGHT = 15;   //右
        private const int ICON_OPEN = 20;   //開啟檔案
        private const int ICON_CLOSE = 21;   //關閉檔案

        void draw_icon(Graphics g, int type, int x_st, int y_st, int width, int height, Color foreground_color)
        {
            //畫在一起
            Pen p;
            SolidBrush sb;

            p = new Pen(foreground_color, 3);
            sb = new SolidBrush(foreground_color);

            int xx;
            int yy;
            Point[] points;

            if (type == ICON_PLAY_PAUSE)    //播放/暫停
            {
                points = new Point[3];
                points[0] = new Point(x_st + width / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width / 2, y_st + height / 2);
                points[2] = new Point(x_st + width / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);

                g.FillRectangle(sb, new Rectangle(x_st + width / 2, y_st + height * 2 / 8, width / 8, height / 2));
                g.FillRectangle(sb, new Rectangle(x_st + width / 2 + width * 2 / 8, y_st + height * 2 / 8, width / 8, height / 2));
            }
            else if (type == ICON_STOP)    //停止
            {
                g.FillRectangle(sb, new Rectangle(x_st + width / 8, y_st + height / 8, width * 6 / 8, height * 6 / 8));
            }
            else if (type == ICON_PAUSE)    //暫停
            {
                g.FillRectangle(sb, new Rectangle(x_st + width * 3 / 16, y_st + height * 2 / 8, width * 4 / 16, height / 2));
                g.FillRectangle(sb, new Rectangle(x_st + width * 9 / 16, y_st + height * 2 / 8, width * 4 / 16, height / 2));
            }
            else if (type == ICON_EMPTY)    //空白
            {

            }
            else if (type == ICON_NEXT)    //下一首
            {
                points = new Point[3];
                points[0] = new Point(x_st + width / 8 + width / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width / 2 + width / 8, y_st + height / 2);
                points[2] = new Point(x_st + width / 8 + width / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);

                g.FillRectangle(sb, new Rectangle(x_st + width / 2 + width / 8, y_st + height * 2 / 8, width / 8, height / 2));
            }
            else if (type == ICON_PREVIOUS)    //上一首
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 6 / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width / 8 + width / 8 + width / 8, y_st + height / 2);
                points[2] = new Point(x_st + width * 6 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);

                g.FillRectangle(sb, new Rectangle(x_st + width / 8 + width / 8, y_st + height * 2 / 8, width / 8, height / 2));

            }
            else if (type == ICON_PLUS)    //加
            {
                g.FillRectangle(sb, new Rectangle(x_st + width / 8, y_st + height * 7 / 16, width * 6 / 8, height * 2 / 16));
                g.FillRectangle(sb, new Rectangle(x_st + width * 7 / 16, y_st + height / 8, width * 2 / 16, height * 6 / 8));
            }
            else if (type == ICON_MINUS)    //減
            {
                g.FillRectangle(sb, new Rectangle(x_st + width / 8, y_st + height * 7 / 16, width * 6 / 8, height * 2 / 16));
            }
            else if (type == ICON_UP)    //上
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 4 / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 6 / 8);
                points[2] = new Point(x_st + width * 2 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);
            }
            else if (type == ICON_DOWN)    //下
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 4 / 8, y_st + height * 6 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 2 / 8);
                points[2] = new Point(x_st + width * 2 / 8, y_st + height * 2 / 8);
                g.FillPolygon(sb, points);

            }
            else if (type == ICON_LEFT)    //左
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 2 / 8, y_st + height * 4 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 2 / 8);
                points[2] = new Point(x_st + width * 6 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);
            }
            else if (type == ICON_RIGHT)    //右
            {
                points = new Point[3];
                points[0] = new Point(x_st + width * 2 / 8, y_st + height * 2 / 8);
                points[1] = new Point(x_st + width * 6 / 8, y_st + height * 4 / 8);
                points[2] = new Point(x_st + width * 2 / 8, y_st + height * 6 / 8);
                g.FillPolygon(sb, points);
            }
            else if (type == ICON_RECORD)    //錄影
            {
                g.FillEllipse(sb, new Rectangle(x_st + width / 4, y_st + height / 4, width / 2, height / 2));
            }
        }
    }
}




/*
private void button1_Click(object sender, EventArgs e)
{
    if (axWindowsMediaPlayer1.currentMedia == null)
        return;


    richTextBox1.Text += "attributeCount:\t" + axWindowsMediaPlayer1.currentMedia.attributeCount.ToString() + "\n";
    richTextBox1.Text += "duration:\t" + axWindowsMediaPlayer1.currentMedia.duration.ToString() + "\n";
    richTextBox1.Text += "durationString:\t" + axWindowsMediaPlayer1.currentMedia.durationString + "\n";
    richTextBox1.Text += "name:\t" + axWindowsMediaPlayer1.currentMedia.name + "\n";
    richTextBox1.Text += "sourceURL:\t" + axWindowsMediaPlayer1.currentMedia.sourceURL + "\n";

    richTextBox1.Text += "currentPosition:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
    richTextBox1.Text += "currentPositionString:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";
    richTextBox1.Text += "currentMarker:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentMarker.ToString() + "\n";

    richTextBox1.Text += "playCount:\t" + axWindowsMediaPlayer1.settings.playCount.ToString() + "\n";

    //info
    //axWindowsMediaPlayer1
    richTextBox1.Text += "status:\t" + axWindowsMediaPlayer1.status + "\n";
    richTextBox1.Text += "playState:\t" + axWindowsMediaPlayer1.playState + "\n";
    richTextBox1.Text += "URL:\t" + axWindowsMediaPlayer1.URL + "\n";
    richTextBox1.Text += "versionInfo:\t" + axWindowsMediaPlayer1.versionInfo + "\n";
    richTextBox1.Text += "windowlessVideo:\t" + axWindowsMediaPlayer1.windowlessVideo + "\n";
    richTextBox1.Text += "uiMode:\t" + axWindowsMediaPlayer1.uiMode + "\n";


    //axWindowsMediaPlayer1.settings
    richTextBox1.Text += "show baseURL = " + axWindowsMediaPlayer1.settings.baseURL + "\n";
    richTextBox1.Text += "show balance = " + axWindowsMediaPlayer1.settings.balance.ToString() + "\n";
    richTextBox1.Text += "show rate = " + axWindowsMediaPlayer1.settings.rate.ToString() + "\n";
    richTextBox1.Text += "show volume = " + axWindowsMediaPlayer1.settings.volume.ToString() + "\n";
    richTextBox1.Text += "show playCount = " + axWindowsMediaPlayer1.settings.playCount.ToString() + "\n";
    richTextBox1.Text += "show mute = " + axWindowsMediaPlayer1.settings.mute.ToString() + "\n";
    richTextBox1.Text += "show currentPlaylist.count = " + axWindowsMediaPlayer1.currentPlaylist.count.ToString() + "\n";
    //richTextBox1.Text += "show baseURL = " + axWindowsMediaPlayer1.currentPlaylist.Item.name + "\n";
    richTextBox1.Text += "show currentPlaylist.name = " + axWindowsMediaPlayer1.currentPlaylist.name + "\n";
    richTextBox1.Text += "show URL = " + axWindowsMediaPlayer1.URL + "\n";
    richTextBox1.Text += "show currentPosition = " + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
    richTextBox1.Text += "show currentItem.duration = " + axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration.ToString() + "\n";
    richTextBox1.Text += "show currentMedia.duration = " + axWindowsMediaPlayer1.currentMedia.duration.ToString() + "\n";
    richTextBox1.Text += "播放位置用字串顯示：" + axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";

    //axWindowsMediaPlayer1.currentMedia
    richTextBox1.Text += "获取当前媒体信息\n";
    richTextBox1.Text += "Title:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title") + "\n";   //標題
    richTextBox1.Text += "Author:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Author") + "\n"; //作者
    richTextBox1.Text += "Artist:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Artist") + "\n";
    richTextBox1.Text += "Genre:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Genre") + "\n";
    richTextBox1.Text += "WM/Genre:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("WM/Genre") + "\n";
    richTextBox1.Text += "Copyright:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Copyright") + "\n";
    richTextBox1.Text += "Description:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Description") + "\n";
    richTextBox1.Text += "持續時間:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Duration") + " 秒\n";
    richTextBox1.Text += "檔案大小:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("FileSize") + " Bytes\n";
    richTextBox1.Text += "檔案類型:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("FileType") + "\n";
    richTextBox1.Text += "sourceURL:\t" + axWindowsMediaPlayer1.currentMedia.getItemInfo("sourceURL") + "\n";
    richTextBox1.Text += "header : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("header") + "\n";
    richTextBox1.Text += "album : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("album") + "\n";
    richTextBox1.Text += "year : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("year") + "\n";
    richTextBox1.Text += "comment : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("comment") + "\n";
    richTextBox1.Text += "track : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("track") + "\n";
    richTextBox1.Text += "zero-byte : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("zero-byte") + "\n";

    richTextBox1.Text += "currentPositionString:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";
    richTextBox1.Text += "currentPosition:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
    richTextBox1.Text += "currentMarker:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentMarker.ToString() + "\n";
    richTextBox1.Text += "currentItem:\t" + axWindowsMediaPlayer1.Ctlcontrols.currentItem.ToString() + "\n";

    richTextBox1.Text += "媒體長度:\t" + axWindowsMediaPlayer1.currentMedia.duration.ToString() + " 秒\n";
    richTextBox1.Text += "影像寬度:\t" + axWindowsMediaPlayer1.currentMedia.imageSourceWidth.ToString() + "\n";
    richTextBox1.Text += "影像高度:\t" + axWindowsMediaPlayer1.currentMedia.imageSourceHeight.ToString() + "\n";
    richTextBox1.Text += "Name:\t" + axWindowsMediaPlayer1.currentMedia.name + "\n";
    richTextBox1.Text += "全螢幕:\t" + axWindowsMediaPlayer1.fullScreen.ToString() + "\n";
    richTextBox1.Text += "播放器寬:\t" + axWindowsMediaPlayer1.Width.ToString() + "\n";
    richTextBox1.Text += "播放器高:\t" + axWindowsMediaPlayer1.Height.ToString() + "\n";
    richTextBox1.Text += "播放器名:\t" + axWindowsMediaPlayer1.Name + "\n";
    richTextBox1.Text += "聲量:\t" + axWindowsMediaPlayer1.settings.volume.ToString() + "\n";
    richTextBox1.Text += "URL:\t" + axWindowsMediaPlayer1.URL + "\n";
    richTextBox1.Text += "版本:\t" + axWindowsMediaPlayer1.versionInfo + "\n";
    //richTextBox1.Text += "XXXXXc:\t" + axWindowsMediaPlayer1.windowlessVideo + "\n";
    //richTextBox1.Text += "XXXXX:\t" + axWindowsMediaPlayer1.Ctlcontrols.isAvailable.ToString() + "\n";

    int W = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
    int H = axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;
    richTextBox1.Text += "W : " + W.ToString() + "\n";
    richTextBox1.Text += "H : " + H.ToString() + "\n";
    if (W == 0)
    {
        axWindowsMediaPlayer1.Visible = false;
    }
}
*/



