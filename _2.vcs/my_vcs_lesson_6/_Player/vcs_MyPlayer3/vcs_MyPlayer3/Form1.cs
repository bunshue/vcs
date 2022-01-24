using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
/*
點開 方案總管/vcs_XXXXX/Properties/Settings.settings

加入要儲存的參數 的 名稱 型別 預設值

若是數字 一定要給預設值
*/

namespace vcs_MyPlayer3
{
    public partial class Form1 : Form
    {
        string mp3_filename = string.Empty;
        int mp3_position = 0;

        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lb_title.Text = "";
            lb_main_mesg1.Text = "";
            lb_main_mesg2.Text = "";
            lb_main_mesg3.Text = "";

            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.StartPosition = FormStartPosition.CenterScreen;
            //this.WindowState = FormWindowState.Maximized;
            this.ControlBox = false;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.TopMost = true;
            this.KeyPreview = true;

            richTextBox1.Text += "取得預設資料 :\n";
            richTextBox1.Text += "filename : \t" + Properties.Settings.Default.filename + "\n";
            richTextBox1.Text += "position : \t" + Properties.Settings.Default.position.ToString() + "\n";

            mp3_filename = Properties.Settings.Default.filename;
            mp3_position = Properties.Settings.Default.position;

            lb_title.Text = mp3_filename;



        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape)
            {
                this.Close();
            }
            else if (e.KeyData == Keys.X)
            {
                this.Close();
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
                openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
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

                    lb_title.Text = mp3_filename;

                }
                else
                {
                    richTextBox1.Text += "未選取檔案\n";
                }

            }
            else if (e.KeyData == Keys.Up)
            {
                show_main_message1("上", S_OK, 30);
            }
            else if (e.KeyData == Keys.Down)
            {
                show_main_message1("下", S_OK, 30);
            }
            else if (e.KeyCode == Keys.Left)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    show_main_message1("CTRL + 左", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    show_main_message1("SHIFT + 左", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Alt) == Keys.Alt)
                {
                    show_main_message1("ALT + 左", S_OK, 30);
                }
                else
                {
                    show_main_message1("左", S_OK, 30);
                }
            }
            else if (e.KeyCode == Keys.Right)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    show_main_message1("CTRL + 右", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Shift) == Keys.Shift)
                {
                    show_main_message1("SHIFT + 右", S_OK, 30);
                }
                else if ((Control.ModifierKeys & Keys.Alt) == Keys.Alt)
                {
                    show_main_message1("ALT + 右", S_OK, 30);
                }
                else
                {
                    show_main_message1("右", S_OK, 30);
                }
            }
            else if (e.KeyData == Keys.Space)
            {
                show_main_message1("空白鍵", S_OK, 30);
            }

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.filename = mp3_filename;
            Properties.Settings.Default.position = mp3_position;

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

        void show_main_message2(string mesg, int number, int timeout)
        {
            lb_main_mesg2.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        void show_main_message3(string mesg, int number, int timeout)
        {
            lb_main_mesg3.Text = mesg;
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
    }
}

