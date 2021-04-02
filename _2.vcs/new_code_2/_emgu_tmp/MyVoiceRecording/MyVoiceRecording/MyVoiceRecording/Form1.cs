using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace MyVoiceRecording
{
    public partial class Form1 : Form
    {
        bool playing = false;
        string voiceDirectory = Application.StartupPath + "\\";
        string fileName;

        //使用非託管(Unmanaged)的DLL
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(
         string lpstrCommand,
         string lpstrReturnString,
         int uReturnLength,
         int hwndCallback
        );

        public Form1()
        {
            InitializeComponent();
        }

        //開始錄音
        private void button1_Click(object sender, EventArgs e)
        {
            mciSendString("set wave bitpersample 8", "", 0, 0);
            mciSendString("set wave samplespersec 20000", "", 0, 0);
            mciSendString("set wave channels 2", "", 0, 0);
            mciSendString("set wave format tag pcm", "", 0, 0);
            mciSendString("open new type WAVEAudio alias movie", "", 0, 0);
            mciSendString("record movie", "", 0, 0);

            button1.Enabled = false;
            button2.Enabled = true;
        }

        //結束錄音
        private void button2_Click(object sender, EventArgs e)
        {
            //檔案存放的路徑
            fileName = string.Format("{0}{1}{2}", voiceDirectory, DateTime.Now.ToString("yyyyMMddHmmss"), ".avi");

            mciSendString("stop movie", "", 0, 0);
            mciSendString("save movie " + fileName, "", 0, 0);  
            mciSendString("close movie", "", 0, 0);

            button1.Enabled = true;
            button2.Enabled = false;
            button3.Enabled = true;
            richTextBox1.Text += "filename = " + fileName + "\n";
        }

        //播放錄音檔
        private void button3_Click(object sender, EventArgs e)
        {
            if (!playing)
            {
                playing = true;
                button3.Text = "停止";
                //播放錄製的檔案
                this.axWindowsMediaPlayer1.URL = fileName;
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }
            else
            {
                axWindowsMediaPlayer1.Ctlcontrols.stop();
                playing = false;
                button3.Text = "播放";
            }  
        }

        /// <summary>
        /// MediaPlayer的狀態改變事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void axWindowsMediaPlayer1_PlayStateChange(object sender, AxWMPLib._WMPOCXEvents_PlayStateChangeEvent e)
        {
            //當檔案播放完成時
            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsStopped)
            {
                playing = false;
                button3.Text = "播放";  
            } 
        }  
        


    }
}
