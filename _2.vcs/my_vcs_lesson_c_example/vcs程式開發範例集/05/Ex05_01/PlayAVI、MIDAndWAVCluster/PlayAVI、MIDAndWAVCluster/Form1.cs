using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace PlayAVIMIDAndWAVCluster
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_avi\enka.avi";
        //string filename = @"D:\_______VIDEO_ALL_all3\纪录片《毛泽东出访苏联》.mp4";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Load
            this.axWindowsMediaPlayer1.newMedia(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //Play
            this.axWindowsMediaPlayer1.URL = filename;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Stop
            this.axWindowsMediaPlayer1.close();


            //or
            //this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            //this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString();
        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            if (bt_pause.Text == "暫停")
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.pause();

                bt_pause.Text = "繼續";

            }
            else
            {
                this.axWindowsMediaPlayer1.Ctlcontrols.play();

                bt_pause.Text = "暫停";
            }
        }

        private WMPLib.WindowsMediaPlayerClass c;
        private WMPLib.IWMPMedia m;

        private void bt_info_Click(object sender, EventArgs e)
        {
            /*
            c = new WMPLib.WindowsMediaPlayerClass();
            m = c.newMedia(filename);
            richTextBox1.Text += "歌手名:\t" + m.getItemInfo("Author") + "\n" + "歌  名:\t" + m.getItemInfo("Title") + "\n";
            */

            richTextBox1.Text += "currentPositionString:\t" + this.axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";
            richTextBox1.Text += "currentPosition:\t" + this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
            richTextBox1.Text += "currentMarker:\t" + this.axWindowsMediaPlayer1.Ctlcontrols.currentMarker.ToString() + "\n";
            richTextBox1.Text += "currentItem:\t" + this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.ToString() + "\n";

            richTextBox1.Text += "媒體長度:\t" + this.axWindowsMediaPlayer1.currentMedia.duration.ToString() + " 秒\n";
            richTextBox1.Text += "影像寬度:\t" + this.axWindowsMediaPlayer1.currentMedia.imageSourceWidth.ToString() + "\n";
            richTextBox1.Text += "影像高度:\t" + this.axWindowsMediaPlayer1.currentMedia.imageSourceHeight.ToString() + "\n";
            richTextBox1.Text += "Name:\t" + this.axWindowsMediaPlayer1.currentMedia.name + "\n";
            richTextBox1.Text += "全螢幕:\t" + this.axWindowsMediaPlayer1.fullScreen.ToString() + "\n";
            richTextBox1.Text += "播放器寬:\t" + this.axWindowsMediaPlayer1.Width.ToString() + "\n";
            richTextBox1.Text += "播放器高:\t" + this.axWindowsMediaPlayer1.Height.ToString() + "\n";
            richTextBox1.Text += "播放器名:\t" + this.axWindowsMediaPlayer1.Name + "\n";
            richTextBox1.Text += "聲量:\t" + this.axWindowsMediaPlayer1.settings.volume.ToString() + "\n";
            richTextBox1.Text += "URL:\t" + this.axWindowsMediaPlayer1.URL + "\n";
            richTextBox1.Text += "版本:\t" + this.axWindowsMediaPlayer1.versionInfo + "\n";
            //richTextBox1.Text += "XXXXXc:\t" + this.axWindowsMediaPlayer1.windowlessVideo + "\n";
            //richTextBox1.Text += "XXXXX:\t" + this.axWindowsMediaPlayer1.Ctlcontrols.isAvailable.ToString() + "\n";


            richTextBox1.Text += "\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.settings.volume++;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.settings.volume--;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.fullScreen = true;

        }

        private void button8_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition += 10;

        }

        private void button7_Click(object sender, EventArgs e)
        {
            this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition -= 10;

        }


    }
}
