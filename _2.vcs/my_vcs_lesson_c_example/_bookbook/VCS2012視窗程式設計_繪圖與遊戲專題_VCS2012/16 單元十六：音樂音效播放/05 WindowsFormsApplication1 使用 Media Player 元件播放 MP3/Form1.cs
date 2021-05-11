using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 播放外部的聲音檔
        //  public domain mp34U
        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            //axWindowsMediaPlayer1.settings.autoStart = false; // 不自動播放
            //axWindowsMediaPlayer1.settings.mute = true;       // 無聲
            axWindowsMediaPlayer1.URL = filename;          // 載入 mp3
            axWindowsMediaPlayer1.settings.volume = 90;       // 音量 0 ~ 100
        }
    }
}