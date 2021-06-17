using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
使用AxWindowsMediaPlayer播放多媒體

加入工具箱

工具箱/滑鼠右鍵/選擇項目/
/COM 元件 頁籤 /勾選Windows Media Player(wmp.dll)	/ 確定


會發現工具箱多了個Windows Media Player的控制項
就是 axWindowsMediaPlayer

*/


namespace vcs_axWindowsMediaPlayer
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\enka.avi";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label3.Text = "";
            axWindowsMediaPlayer1.Dock = DockStyle.Fill;     //填滿整個表單

            //this.axWindowsMediaPlayer1.settings.autoStart = false;                     //設定不自動播放, 預設是自動播放

            this.trackBar1.Minimum = 0;                                               //設定音量調整Bar最小值為最小音量值(0)
            this.trackBar1.Maximum = 100;                                             //設定音量調整Bar最大值為最大音量值(100)
            this.trackBar1.Value = this.axWindowsMediaPlayer1.settings.volume;        //設定音量調整Bar目前值為目前音量值

            this.timer1.Enabled = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //表單標題顯示多媒體檔案路徑
            this.Text = "播放檔案 : \t" + filename;
            //axWindowsMediaPlayer1播放開檔對話方塊所選擇的多媒體檔
            axWindowsMediaPlayer1.URL = filename;   //開啟檔案
            this.trackBar2.Maximum = (int)this.axWindowsMediaPlayer1.currentMedia.duration;          //設定播放位置調整Bar最大值
        }

        private void button2_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.play();　　　　//開始播放多媒體檔
            richTextBox1.Text += "播放\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.pause();　　　　//暫停播放多媒體檔
            richTextBox1.Text += "暫停\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.stop(); 　　　 //停止播放多媒體檔
            richTextBox1.Text += "停止\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.previous();　　//播放上一段
            richTextBox1.Text += "播放上一段\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.next(); 　　　 //播放下一段
            richTextBox1.Text += "播放下一段\n";
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            //音量
            this.axWindowsMediaPlayer1.settings.volume = this.trackBar1.Value;      //改變音量大小
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {

        }

        private void trackBar2_MouseDown(object sender, MouseEventArgs e)
        {
            timer1.Enabled = false;

        }

        private void trackBar2_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void trackBar2_MouseUp(object sender, MouseEventArgs e)
        {
            timer1.Enabled = true;
            //播放位置
            this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition = trackBar2.Value;          //改變播放位置
            label3.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + " / " + axWindowsMediaPlayer1.currentMedia.durationString + " " + (axWindowsMediaPlayer1.Ctlcontrols.currentPosition / axWindowsMediaPlayer1.currentMedia.duration).ToString("P0");
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.axWindowsMediaPlayer1.currentMedia == null)
                return;


            this.trackBar2.Maximum = (int)this.axWindowsMediaPlayer1.currentMedia.duration;          //設定播放位置調整Bar最大值

            this.trackBar2.Value = (int)axWindowsMediaPlayer1.Ctlcontrols.currentPosition;

            //richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentPosition.ToString() + "\n";
            //richTextBox1.Text += this.axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + "\n";

            label3.Text = axWindowsMediaPlayer1.Ctlcontrols.currentPositionString + " / " + axWindowsMediaPlayer1.currentMedia.durationString + " " + (axWindowsMediaPlayer1.Ctlcontrols.currentPosition / axWindowsMediaPlayer1.currentMedia.duration).ToString("P0");
        }
    }
}
