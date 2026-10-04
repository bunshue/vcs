using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_DiskDirectoryFile1
{
    public partial class Form_Setup : Form
    {
        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "";
            lb_setup0.Text = "播放影片程式";
            lb_setup1.Text = "播放音樂程式";
            lb_setup2.Text = "播放圖片程式";
            lb_setup3.Text = "文字編輯程式";
            lb_setup4.Text = "預設搜尋路徑";
            lb_setup5.Text = "Katfile路徑";
            lb_setup6.Text = "Git路徑";

            tb_setup0.Text = Properties.Settings.Default.video_player_path;
            //tb_setup1.Text = Properties.Settings.Default.audio_player_path;
            //tb_setup2.Text = Properties.Settings.Default.picture_viewer_path;
            //tb_setup3.Text = Properties.Settings.Default.text_editor_path;

            string search_path = Properties.Settings.Default.search_path;
            string doc_foldername = Properties.Settings.Default.doc_foldername;
            string git_foldername = Properties.Settings.Default.git_foldername;
            if (Directory.Exists(search_path) == false)
            {
                tb_setup4.Text = search_path;
            }
            else
            {
                tb_setup4.Text = "";
            }
            if (Directory.Exists(doc_foldername) == false)
            {
                tb_setup5.Text = doc_foldername;
            }
            else
            {
                tb_setup5.Text = "";
            }
            if (Directory.Exists(git_foldername) == false)
            {
                tb_setup6.Text = git_foldername;
            }
            else
            {
                tb_setup6.Text = "";
            }
            show_item_location();
        }

        void show_item_location()
        {
            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 50;
            dx = 170;
            dy = 55;

            lb_setup0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_setup1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_setup2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_setup3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_setup4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            lb_setup5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            lb_setup6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            lb_main_mesg.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            tb_setup0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            tb_setup1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            tb_setup2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            tb_setup3.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            tb_setup4.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            tb_setup5.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            tb_setup6.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            int dxx = 80;
            bt_setup0.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 0);
            bt_setup1.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 1);
            bt_setup2.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 2);
            bt_setup3.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 3);
            bt_setup4.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 4);
            bt_setup5.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 5);
            bt_setup6.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 6);
            bt_setup_save.Location = new Point(x_st + dx * 4 + dxx, y_st + dy * 7);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(bt_setup_save.Right + 20, bt_setup_save.Bottom + 20);

            this.Text = "vcs_DiskDirectoryFile1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        //------------------------------------------------------------  # 60個

        private void bt_setup0_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取播放影片程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup0.Text = openFileDialog1.FileName;
            }
        }

        private void bt_setup1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取播放音樂程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup1.Text = openFileDialog1.FileName;
            }
        }

        private void bt_setup2_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取播放圖片程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup2.Text = openFileDialog1.FileName;
            }
        }

        private void bt_setup3_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取文字編輯程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup3.Text = openFileDialog1.FileName;
            }
        }

        private void bt_setup4_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "C:\\"; //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                //預設搜尋路徑
                tb_setup4.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_setup5_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "C:\\"; //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup5.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_setup6_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "C:\\"; //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_setup6.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_setup_save_Click(object sender, EventArgs e)
        {
            //儲存
            Properties.Settings.Default.video_player_path = tb_setup0.Text;
            //Properties.Settings.Default.audio_player_path = tb_setup1.Text;
            //Properties.Settings.Default.picture_viewer_path = tb_setup2.Text;
            //Properties.Settings.Default.text_editor_path = tb_setup3.Text;
            Properties.Settings.Default.search_path = tb_setup4.Text;
            Properties.Settings.Default.doc_foldername = tb_setup5.Text;
            Properties.Settings.Default.git_foldername = tb_setup6.Text;

            Properties.Settings.Default.Save();
            show_main_message("儲存設定完成", S_OK, 30);
        }

        void show_main_message(string mesg, int number, int timeout)
        {
            lb_main_mesg.Text = mesg;
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
                    lb_main_mesg.Text = "";
                }
            }
        }
    }
}
