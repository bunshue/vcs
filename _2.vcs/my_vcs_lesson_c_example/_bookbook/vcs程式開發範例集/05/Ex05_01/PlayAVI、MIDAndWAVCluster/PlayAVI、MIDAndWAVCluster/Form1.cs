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

        private void button2_Click(object sender, EventArgs e)
        {
            //Play
            this.axWindowsMediaPlayer1.URL = filename;
            this.axWindowsMediaPlayer1.Ctlcontrols.play();

            //不能直接設定播放器的大小
            //this.axWindowsMediaPlayer1.Width = this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
            //this.axWindowsMediaPlayer1.Height = this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;

            this.axWindowsMediaPlayer1.Width = 400;
            this.axWindowsMediaPlayer1.Height = 400;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Stop
            this.axWindowsMediaPlayer1.close();


            //or
            //this.axWindowsMediaPlayer1.Ctlcontrols.stop();
            //this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString();
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
        }

        private void button9_Click(object sender, EventArgs e)
        {
            /*
            int W = this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
            int H = this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;
            this.axWindowsMediaPlayer1.Width = W;
            this.axWindowsMediaPlayer1.Height = H;
            */

            this.axWindowsMediaPlayer1.Width = this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceWidth;
            this.axWindowsMediaPlayer1.Height = this.axWindowsMediaPlayer1.Ctlcontrols.currentItem.imageSourceHeight;

        }


    }
}
