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


/*
點開 方案總管/vcs_XXXXX/Properties/Settings.settings

加入要儲存的參數 的 名稱 型別 預設值

若是數字 一定要給預設值
*/

/*  sugar
使用AxWindowsMediaPlayer播放多媒體

加入工具箱

工具箱/滑鼠右鍵/選擇項目/
/COM 元件 頁籤 /勾選Windows Media Player(wmp.dll)	/ 確定

會發現工具箱多了個Windows Media Player的控制項
就是 axWindowsMediaPlayer

*/

namespace vcs_MyPlayer3
{
    public partial class Form1 : Form
    {
        string mp3_filename = string.Empty;
        int mp3_position = 0;
        int mp3_volume = 50;
        int mp3_player_height = 50;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;

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

        void Init_WMP()
        {
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
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
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Init_WMP();

            int W = Screen.PrimaryScreen.WorkingArea.Width;
            int H = Screen.PrimaryScreen.WorkingArea.Height;
            this.ClientSize = new Size(W, mp3_player_height);
            this.Location = new Point(0, H - mp3_player_height);
            this.pictureBox1.Size = new Size(this.pictureBox1.Size.Width, mp3_player_height);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.KeyPreview = true;
            this.TopMost = true;

            lb_main_mesg1.Location = new Point(W / 2, 2);
            lb_main_mesg1.Text = "";
            lb_main_mesg1.BringToFront();


            bool flag_use_autoload_file = false;

            //lb_main_mesg1.Text += "len = " + Environment.GetCommandLineArgs().Length.ToString();
            if (Environment.GetCommandLineArgs().Length == 2)
            {
                string filename = Environment.GetCommandLineArgs()[1];
                //lb_main_mesg1.Text = filename;

                var GetExtension = Path.GetExtension(filename);

                if (GetExtension.ToLower() == ".mp3")
                {
                    mp3_filename = filename;
                    mp3_position = 0;

                    flag_use_autoload_file = true;

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

            if (flag_use_autoload_file == false)
            {
                mp3_filename = Properties.Settings.Default.filename;
                mp3_position = Properties.Settings.Default.position;
            }
            
            mp3_volume = Properties.Settings.Default.volume;
            if (mp3_volume == -1)
            {
                mp3_volume = 50;
            }
            axWindowsMediaPlayer1.Visible = false;
            axWindowsMediaPlayer1.URL = mp3_filename;
            axWindowsMediaPlayer1.settings.volume = mp3_volume;
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
            //axWindowsMediaPlayer1.Ctlcontrols.stop();

            show_main_message1("音量 : " + mp3_volume.ToString(), S_OK, 30);

            this.Focus();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if ((e.KeyData == Keys.Escape) || (e.KeyData == Keys.X))
            {
                this.Close();
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
                show_main_message1("已連上網路磁碟機", S_OK, 30);
                show_main_message1("開啟檔案", S_OK, 30);

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
                    mp3_position = 0;
                    axWindowsMediaPlayer1.URL = mp3_filename;
                    axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
                }
                else
                {
                    show_main_message1("未選取檔案", S_OK, 30);
                }
            }
            else if ((e.KeyData == Keys.D0) || (e.KeyData == Keys.NumPad0))
            {
                show_main_message1("恢復速度", S_OK, 30);
            }
            else if (e.KeyCode == Keys.Up)
            {
                //show_main_message1("上", S_OK, 30);
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    show_main_message1("CTRL + 上", S_OK, 30);
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
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    show_main_message1("CTRL + 下", S_OK, 30);
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
                    show_main_message1("暫停", S_OK, 30);
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
            Properties.Settings.Default.filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;
            Properties.Settings.Default.volume = mp3_volume;

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

                title = axWindowsMediaPlayer1.currentMedia.sourceURL + " ( " + title + " / " + author + " )";
                //title = axWindowsMediaPlayer1.currentMedia.name;
                tmp_height = e.Graphics.MeasureString(title, f).ToSize().Height;
                y_st = (H - tmp_height) / 4;
                e.Graphics.DrawString(title, f, sb, new PointF(10, y_st));

                string play_info = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + " / " + axWindowsMediaPlayer1.Ctlcontrols.currentItem.durationString
                    + " ( " + ((int)((100 * axWindowsMediaPlayer1.Ctlcontrols.currentPosition / axWindowsMediaPlayer1.Ctlcontrols.currentItem.duration))).ToString() + " %)";

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
            if (e.Y < H / 5)
            {
                flag_mouse_down_mode = 1;   //move position mode
                Form1_MouseDown(sender, e);
            }
            else
            {
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
            }
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
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



