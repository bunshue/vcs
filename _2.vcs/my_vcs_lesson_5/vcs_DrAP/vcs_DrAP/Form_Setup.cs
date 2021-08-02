using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrAP
{
    public partial class Form_Setup : Form
    {
        public Form_Setup()
        {
            InitializeComponent();
        }

        private void Form_Setup_Load(object sender, EventArgs e)
        {
            label0.Text = "播放影片程式";
            label1.Text = "播放音樂程式";
            label2.Text = "播放圖片程式";
            label3.Text = "文字編輯程式";
            label4.Text = "搜尋預設路徑";
            label5.Text = "";

            textBox0.Text = Properties.Settings.Default.video_player_path;
            textBox1.Text = Properties.Settings.Default.audio_player_path;
            textBox2.Text = Properties.Settings.Default.picture_viewer_path;
            textBox3.Text = Properties.Settings.Default.text_editor_path;
            textBox4.Text = Properties.Settings.Default.search_path;

            show_item_location();
        }

        void show_item_location()
        {
            /*
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1700;
            y_st = 12;
            dx = 190;
            dy = 50;
            */

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 50;
            dx = 150;
            dy = 55;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            label5.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            textBox0.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            textBox1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            textBox2.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            textBox3.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            textBox4.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            textBox5.Location = new Point(x_st + dx * 1, y_st + dy * 5);


            button0.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 5, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 5, y_st + dy * 6);

        }

        private void button0_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取播放影片程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox0.Text = openFileDialog1.FileName;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取播放音樂程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取播放圖片程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox2.Text = openFileDialog1.FileName;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "選取文字編輯程式";
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "程式|*.exe|所有檔|*.*";   //限定檔案格式
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;
            openFileDialog1.InitialDirectory = "C:\\";         //從目前目錄開始尋找檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox3.Text = openFileDialog1.FileName;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "C:\\"; //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox4.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                //richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //儲存
            Properties.Settings.Default.video_player_path = textBox0.Text;
            Properties.Settings.Default.audio_player_path = textBox1.Text;
            Properties.Settings.Default.picture_viewer_path = textBox2.Text;
            Properties.Settings.Default.text_editor_path = textBox3.Text;
            Properties.Settings.Default.search_path = textBox4.Text;

            Properties.Settings.Default.Save();
        }
    }
}


