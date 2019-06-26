using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1_WMP
{
    public partial class Form1 : Form
    {
        WMPLib.WindowsMediaPlayer player = new WMPLib.WindowsMediaPlayer();

        public Form1()
        {
            InitializeComponent();
            player.URL = "C:\\______test_vcs\\07    都はろみ--妻戀道中(他鄉思妻兒).mp3";
            player.settings.volume = 50;
            player.settings.autoStart = false;
            player.controls.stop();
            label1.Text = player.settings.volume.ToString();
        }

        //使用WMP播放音樂檔
        //參考/加入參考/COM/Windows Media Player 1.0 wmp.dll
        private void button1_Click(object sender, EventArgs e)
        {
            player.controls.play();
            timer1.Enabled = true;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            player.controls.pause();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            player.controls.stop();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            player.controls.fastForward();

        }

        private void button8_Click(object sender, EventArgs e)
        {
            player.controls.fastReverse();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            int volume_setup = player.settings.volume;

            if (volume_setup < 99)
            {
                volume_setup += 2;
                player.settings.volume = volume_setup;
                label1.Text = player.settings.volume.ToString();
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            int volume_setup = player.settings.volume;

            if (volume_setup > 1)
            {
                volume_setup -= 2;
                player.settings.volume = volume_setup;
                label1.Text = player.settings.volume.ToString();
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //player.URL = "https://www.youtube.com/watch?v=rjZksEz4kp0&t=337s";
            //player.controls.play();
        }

        public int MediaGetPosition()
        {
            int ret = 0;
            if (WMPLib.WMPPlayState.wmppsPlaying != player.playState)
            {
                return ret;
            }
            double curPos = player.controls.currentPosition;
            double totalLen = player.currentMedia.duration;
            ret = (int)((curPos / totalLen) * 100);
            richTextBox1.Text += "ret = " + ret.ToString() + "\n";
            return ret;
        }  

        private void timer1_Tick(object sender, EventArgs e)
        {
            label2.Text = player.controls.currentPositionString;
            label3.Text = player.controls.currentPosition.ToString();
            label4.Text = player.controls.currentMarker.ToString();

            label5.Text = player.currentMedia.durationString;
            label6.Text = player.currentMedia.duration.ToString();
            label7.Text = player.currentMedia.attributeCount.ToString();

            label8.Text = player.currentMedia.name;
            label9.Text = player.currentMedia.sourceURL;
            label10.Text = player.settings.playCount.ToString();


            progressBar1.Value = MediaGetPosition();
            if ( WMPLib.WMPPlayState.wmppsPlaying == player.playState)
            {
                label11.Text = player.controls.currentPositionString;
            }
            else
            {
                timer1.Enabled = false;
                label11.Text = "00:00";
            }  


        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "status" + "\t" + player.status + "\n";
            richTextBox1.Text += "playState" + "\t" + player.playState + "\n";
            richTextBox1.Text += "URL" + "\t" + player.URL + "\n";
            richTextBox1.Text += "versionInfo" + "\t" + player.versionInfo + "\n";
            richTextBox1.Text += "windowlessVideo" + "\t" + player.windowlessVideo + "\n";
            richTextBox1.Text += "uiMode" + "\t" + player.uiMode + "\n";

            richTextBox1.Text += "获取当前媒体信息\n";
            richTextBox1.Text += "Title" + "\t" + player.currentMedia.getItemInfo("Title") + "\n";
            richTextBox1.Text += "Author" + "\t" + player.currentMedia.getItemInfo("Author") + "\n";
            richTextBox1.Text += "Copyright" + "\t" + player.currentMedia.getItemInfo("Copyright") + "\n";
            richTextBox1.Text += "Description" + "\t" + player.currentMedia.getItemInfo("Description") + "\n";
            richTextBox1.Text += "Duration" + "\t" + player.currentMedia.getItemInfo("Duration") + "\n";
            richTextBox1.Text += "FileSize" + "\t" + player.currentMedia.getItemInfo("FileSize") + "\n";
            richTextBox1.Text += "FileType" + "\t" + player.currentMedia.getItemInfo("FileType") + "\n";
            richTextBox1.Text += "sourceURL" + "\t" + player.currentMedia.getItemInfo("sourceURL") + "\n";



        }

        private void button7_Click(object sender, EventArgs e)
        {
            if(player.settings.mute == true)
            {
                player.settings.mute = false;
            }
            else
            {
                player.settings.mute = true;
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "current rate = " + player.settings.rate.ToString() + "\n";
            player.settings.rate += 0.1;
            richTextBox1.Text += "new rate = " + player.settings.rate.ToString() + "\n";

        }
    }
}
