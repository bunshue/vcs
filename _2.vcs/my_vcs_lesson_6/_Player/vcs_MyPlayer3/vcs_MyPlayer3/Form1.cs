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

        private const int PDF_PAGE = 5;
        private const int PDF_ZOOM_FACTOR = 130;

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

        List<String> mp3_filename_list = new List<String>();
        int current_mp3_index = 0;
        int total_mp3_count = 0;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        AxWindowsMediaPlayer axWindowsMediaPlayer1;
        WebBrowser webBrowser1;
        RichTextBox richTextBox1;

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
            int W = Screen.PrimaryScreen.WorkingArea.Width;
            int H = Screen.PrimaryScreen.WorkingArea.Height;

            if (flag_debug_mode == false)
            {
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
                int richtextbox_width = 86;
                //debug模式
                this.webBrowser1 = new WebBrowser();
                this.webBrowser1.Location = new System.Drawing.Point(0, 0);
                //this.webBrowser1.Name = "webBrowser1";
                this.webBrowser1.Size = new System.Drawing.Size(W - richtextbox_width, H - mp3_player_height);
                //this.webBrowser1.TabIndex = 2;
                //this.webBrowser1.Visible = false;   //fail
                this.Controls.Add(this.webBrowser1);

                this.richTextBox1 = new RichTextBox();
                this.richTextBox1.Location = new System.Drawing.Point(W - richtextbox_width, 0);
                this.richTextBox1.Size = new System.Drawing.Size(richtextbox_width, H - mp3_player_height);
                this.Controls.Add(this.richTextBox1);
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
                    bt_exit_setup();
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
            int width = 5;
            int w = 40; //設定按鈕大小 W
            int h = 40; //設定按鈕大小 H

            Button bt_right = new Button();  // 實例化按鈕
            bt_right.Size = new Size(w, h);
            bt_right.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_right.Image = bmp;

            bt_right.Location = new Point(this.ClientSize.Width - bt_right.Width + 0, 0 + h + h);
            bt_right.Click += bt_right_Click;     // 加入按鈕事件

            this.Controls.Add(bt_right); // 將按鈕加入表單
            bt_right.BringToFront();     //移到最上層

            Button bt_left = new Button();  // 實例化按鈕
            bt_left.Size = new Size(w, h);
            bt_left.Text = "";
            //Bitmap bmp = new Bitmap(w, h);
            //Graphics g = Graphics.FromImage(bmp);
            //Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_left.Image = bmp;

            bt_left.Location = new Point(this.ClientSize.Width - bt_left.Width - 40, 0 + h + h);
            bt_left.Click += bt_left_Click;     // 加入按鈕事件

            this.Controls.Add(bt_left); // 將按鈕加入表單
            bt_left.BringToFront();     //移到最上層
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
            this.Close();
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

        private void Form1_Load(object sender, EventArgs e)
        {
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
                if (File.Exists(pdf_filename) == true)
                {
                    pdf_filename_short = Path.GetFileName(pdf_filename);
                    current_directory = Path.GetDirectoryName(pdf_filename);

                    //預設
                    //webBrowser1.Navigate(pdf_filename);

                    //指名頁數
                    webBrowser1.Navigate(pdf_filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0&page=" + PDF_PAGE.ToString());

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

            this.Focus();
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
                show_main_message1("開啟mp3/pdf檔案", S_OK, 30);

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





                }


            }
            else if (e.KeyData == Keys.M)
            {
                show_main_message1("開啟mp3檔案", S_OK, 30);

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
                this.Focus();
                this.KeyPreview = true;
            }
            else if (e.KeyData == Keys.P)
            {
                show_main_message1("開啟pdf檔案", S_OK, 30);

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

                    show_item_location(MODE_1);
                    pdf_filename = openFileDialog1.FileName;
                    pdf_filename_short = Path.GetFileName(pdf_filename);
                    current_directory = Path.GetDirectoryName(pdf_filename);
                    webBrowser1.Navigate(pdf_filename);
                    show_main_message1("檔案 : " + pdf_filename_short.ToString(), S_OK, 30);
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

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.mp3_filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;
            Properties.Settings.Default.volume = mp3_volume;
            Properties.Settings.Default.pdf_filename = pdf_filename;

            Properties.Settings.Default.Save();
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



