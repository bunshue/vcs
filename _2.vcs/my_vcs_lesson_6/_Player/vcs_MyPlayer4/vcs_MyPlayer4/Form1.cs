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


namespace vcs_MyPlayer4
{
    public partial class Form1 : Form
    {
        string mp3_filename = string.Empty;

        double mp3_rate = 1.0;

        /*
        int mp3_position = 0;
        int mp3_volume = 50;
        int mp3_player_height = 50;
        
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        */

        AxWMPLib.AxWindowsMediaPlayer axWindowsMediaPlayer1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.StartPosition = FormStartPosition.CenterScreen;
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.KeyPreview = true;
            this.TopMost = true;

            Init_WMP();

        }

        void Init_WMP()
        {
            this.axWindowsMediaPlayer1 = new AxWMPLib.AxWindowsMediaPlayer();
            this.axWindowsMediaPlayer1.Enabled = true;
            this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(0, 0);
            this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(640*1, 480*1);
            //this.axWindowsMediaPlayer1.Dock = DockStyle.Fill;
            //this.axWindowsMediaPlayer1.TabIndex = 2;
            //this.axWindowsMediaPlayer1.Visible = false;   //fail
            //this.axWindowsMediaPlayer1.StatusChange += new EventHandler(axWindowsMediaPlayer1_StatusChange);
            this.Controls.Add(this.axWindowsMediaPlayer1);
        }

        //delay 10000 約 10秒
        //C# 不lag的延遲時間
        private void delay(int delay_milliseconds)
        {
            delay_milliseconds *= 2;
            DateTime time_before = DateTime.Now;
            while (((TimeSpan)(DateTime.Now - time_before)).TotalMilliseconds < delay_milliseconds)
            {
                Application.DoEvents();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //string filename = @"C:\______test_files\__RW\_avi\i2c.avi";
            //string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            string filename = @"D:\vcs\_烏龍派出所\_烏龍派出所251~300\烏龍派出所268(日語).mp4";

            //axWindowsMediaPlayer1.Visible = false;
            axWindowsMediaPlayer1.URL = filename;
            //axWindowsMediaPlayer1.settings.volume = mp3_volume;
            //axWindowsMediaPlayer1.Ctlcontrols.currentPosition = mp3_position;
            //axWindowsMediaPlayer1.settings.mute = true;

            axWindowsMediaPlayer1.Ctlcontrols.play();


            delay(300);

            int W = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
            int H = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
            axWindowsMediaPlayer1.Width = W + 2;
            axWindowsMediaPlayer1.Height = H + 2;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            //this.Size = new Size(W, H);






        }

        private void button2_Click(object sender, EventArgs e)
        {

            int W = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
            int H = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
            axWindowsMediaPlayer1.Width = W + 2;
            axWindowsMediaPlayer1.Height = H + 2;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";


            //axWindowsMediaPlayer1.DisplayRectangle = new Rectangle(0, 0, 300, 200);
            //axWindowsMediaPlayer1.fullScreen = true;
            //axWindowsMediaPlayer1.uiMode


            //axWindowsMediaPlayer1.uiMode = "invisible";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //info
            //axWindowsMediaPlayer1.Ctlcontrols
            //axWindowsMediaPlayer1.Ctlcontrols.fastForward();

            //richTextBox1.Text += "rate = " + axWindowsMediaPlayer1.display
            /*
            */

            //richTextBox1.Text += "rate = " + axWindowsMediaPlayer1.settings.rate.ToString() + "\n";

            richTextBox1.Text += "R ";

            //axWindowsMediaPlayer1.Ctlcontrols.fastReverse();    //無路用


            //獲取當前媒體信息
            string Title = axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");   //媒體標題
            string Author = axWindowsMediaPlayer1.currentMedia.getItemInfo("Author");   //藝術家
            string Copyright = axWindowsMediaPlayer1.currentMedia.getItemInfo("Copyright");   //版權信息
            string Description = axWindowsMediaPlayer1.currentMedia.getItemInfo("Description");   //媒體內容描述
            string Duration = axWindowsMediaPlayer1.currentMedia.getItemInfo("Duration");   //持續時間（秒）
            string FileSize = axWindowsMediaPlayer1.currentMedia.getItemInfo("FileSize");   //文件大小
            string FileType = axWindowsMediaPlayer1.currentMedia.getItemInfo("FileType");   //文件類型
            string sourceURL = axWindowsMediaPlayer1.currentMedia.getItemInfo("sourceURL");   //原始地址


            richTextBox1.Text += "Title : " + Title + "\n";
            richTextBox1.Text += "Author : " + Author + "\n";
            richTextBox1.Text += "Copyright : " + Copyright + "\n";
            richTextBox1.Text += "Description : " + Description + "\n";
            richTextBox1.Text += "Duration : " + Duration + "\n";
            richTextBox1.Text += "FileSize : " + FileSize + "\n";
            richTextBox1.Text += "FileType : " + FileType + "\n";
            richTextBox1.Text += "sourceURL : " + sourceURL + "\n";


            //axWindowsMediaPlayer1.currentMedia.setItemInfo("Copyright", "lion-mouse");    //通過屬性名設置媒體信息

        }

        private void button11_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.fullScreen = true;
        }

    }
}
