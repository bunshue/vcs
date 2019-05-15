using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
參考:
C#利用AxWindowsMediaPlayer播放mp3
http://kikilala-tw.blogspot.com/2009/09/caxwindowsmediaplayermp3.html

工具箱/所有Windows Form，右鍵，選擇項目 選COM元件，選Windows Media Player wmp.dll，
工具箱就會出現Windows Media Player控件
*/

namespace vcs_WMP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int state = 0;

        private void Form1_Load(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.settings.autoStart = false;   //設定不自動撥放
            axWindowsMediaPlayer1.URL = @"C:\______test_vcs\監獄風雲.mp3";
            axWindowsMediaPlayer1.settings.rate = 1;    //播放速度
            //axWindowsMediaPlayer1.settings.getMode("loop"); //useless
        }

        private void button3_Click(object sender, EventArgs e)
        {
            openFileDialog1.Multiselect = true;
            openFileDialog1.Filter = "mp3文件|*.mp3|wav文件|*.wav|wma文件|*.wma|wmv文件|*.wmv|所有格式|*.*";

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //axWindowsMediaPlayer1.URL = openFileDialog1.FileName;
                //axWindowsMediaPlayer1.Ctlcontrols.stop();     //改成設定autoStart = false

                axWindowsMediaPlayer1.currentPlaylist = axWindowsMediaPlayer1.newPlaylist("播放列表", "");
                foreach (string fn in openFileDialog1.FileNames)
                {
                    axWindowsMediaPlayer1.currentPlaylist.appendItem(axWindowsMediaPlayer1.newMedia(fn));
                    richTextBox1.Text += "加入播放清單: " + fn + "\n";
                }
                
                state = 1;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if ((state == 1) || (state == 3))
            {
                axWindowsMediaPlayer1.Ctlcontrols.play();
                state = 2;
            }
            else if (state == 2)
            {
                axWindowsMediaPlayer1.Ctlcontrols.pause();
                state = 3;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (state > 0)
            {
                axWindowsMediaPlayer1.Ctlcontrols.stop();
                state = 1;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
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

            richTextBox1.Text += "Title : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Artist : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("Artist") + "\n";
            richTextBox1.Text += "Genre : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("Genre") + "\n";
            richTextBox1.Text += "WM/Genre : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("WM/Genre") + "\n";
            richTextBox1.Text += "Copyright : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("Copyright") + "\n";
            richTextBox1.Text += "Description : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("Description") + "\n";
            richTextBox1.Text += "持續時間 : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("Duration") + " 秒\n";
            richTextBox1.Text += "檔案大小 : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("FileSize") + " Bytes\n";
            richTextBox1.Text += "檔案類型 : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("FileType") + "\n";
            richTextBox1.Text += "sourceURL : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("sourceURL") + "\n";
            richTextBox1.Text += "header : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("header") + "\n";
            richTextBox1.Text += "album : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("album") + "\n";
            richTextBox1.Text += "year : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("year") + "\n";
            richTextBox1.Text += "comment : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("comment") + "\n";
            richTextBox1.Text += "track : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("track") + "\n";
            richTextBox1.Text += "zero-byte : " + axWindowsMediaPlayer1.currentMedia.getItemInfo("zero-byte") + "\n";









        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int balance = axWindowsMediaPlayer1.settings.balance;
            balance += 10;
            if (balance > 100)
                balance = -100;
            axWindowsMediaPlayer1.settings.balance = balance;
        }

    }
}
