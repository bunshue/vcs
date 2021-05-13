using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_WindowsMediaPlayer
{
    public partial class Form1 : Form
    {
        //用來儲存音樂檔案的全路徑
        List<string> listSong = new List<string>();
        bool flag_playing = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.axWindowsMediaPlayer1.settings.autoStart = false;                     //設定不自動撥放
            this.axWindowsMediaPlayer1.settings.autoStart = true;                     //設定自動撥放
            this.trackBar1.Minimum = 0;                                               //設定音量調整Bar最小值為最小音量值(0)
            this.trackBar1.Maximum = 100;                                             //設定音量調整Bar最大值為最大音量值(100)
            this.trackBar1.Value = this.axWindowsMediaPlayer1.settings.volume;        //設定音量調整Bar目前值為目前音量值
            this.timer1.Enabled = true;
            listBox1.SelectedIndex = -1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Title = "請選擇檔案";
            ofd.Multiselect = true;
            ofd.InitialDirectory = @"D:\vcs\astro\_DATA2\_mp3\";
            ofd.Filter = "音樂檔案|*.wav|mp3檔案|*.mp3|所有檔案|*.*";
            ofd.FilterIndex = 2;
            ofd.ShowDialog();
            //獲得我們在資料夾中選擇所有檔案的全路徑
            string[] path = ofd.FileNames;
            for (int i = 0; i < path.Length; i++)
            {
                //將音樂檔案的檔名載入到ListBox中
                listBox1.Items.Add(Path.GetFileName(path[i]));
                //將音樂檔案的全路徑儲存到泛型集合中
                listSong.Add(path[i]);
            }
            listBox1.SelectedIndex = 0;
            flag_playing = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;

            if (button2.Text == "播放")
            {
                if (flag_playing == false)
                {
                    axWindowsMediaPlayer1.URL = listSong[listBox1.SelectedIndex];   //開啟檔案
                }

                axWindowsMediaPlayer1.Ctlcontrols.play();
                button2.Text = "暫停";
                flag_playing = true;
            }
            else
            {
                axWindowsMediaPlayer1.Ctlcontrols.pause();        //暫停撥放
                button2.Text = "播放";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;

            // 獲得當前選中歌曲的索引
            int index = listBox1.SelectedIndex;
            index--;
            if (index < 0)
            {
                index = listBox1.Items.Count - 1;
            }
            //將重新改變後的索引重新的賦值給當前選中項
            listBox1.SelectedIndex = index;
            axWindowsMediaPlayer1.URL = listSong[index];
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;

            int index = listBox1.SelectedIndex;
            index++;
            if (index == listBox1.Items.Count)
            {
                index = 0;
            }
            listBox1.SelectedIndex = index;
            axWindowsMediaPlayer1.URL = listSong[index];
            axWindowsMediaPlayer1.Ctlcontrols.play();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;

            axWindowsMediaPlayer1.Ctlcontrols.stop();         //停止播放
            flag_playing = false;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            //this.axWindowsMediaPlayer1.settings.volume += 1;       //音量大小+1
            //this.axWindowsMediaPlayer1.settings.volume -= 1;       //音量大小-1

            //音量控制
            this.axWindowsMediaPlayer1.settings.volume = this.trackBar1.Value;      //改變音量大小
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            //播放位置
            this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition = trackBar2.Value;          //改變撥放位置
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.axWindowsMediaPlayer1.currentMedia == null)
                return;

            this.trackBar2.Minimum = 0;
            this.trackBar2.Maximum = (int)this.axWindowsMediaPlayer1.currentMedia.duration;          //設定撥放位置調整Bar最大值
            this.trackBar2.Value = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex == -1)
                return;

            richTextBox1.Text += axWindowsMediaPlayer1.currentMedia.attributeCount.ToString() + "\n";
            richTextBox1.Text += axWindowsMediaPlayer1.currentMedia.duration.ToString() + "\n";
            richTextBox1.Text += axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";


            //axWindowsMediaPlayer1.Ctlcontrols.play();         //停止播放
            axWindowsMediaPlayer1.Ctlcontrols.currentPosition = 0;      //移動播放位置到最前面

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //播放外部的 MP3 檔案

            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            //axWindowsMediaPlayer1.settings.autoStart = false; // 不自動播放
            //axWindowsMediaPlayer1.settings.mute = true;       // 無聲
            axWindowsMediaPlayer1.URL = filename;          // 載入 mp3
            axWindowsMediaPlayer1.settings.volume = 90;       // 音量 0 ~ 100

        }
    }
}
