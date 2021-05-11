using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Media; // SystemSounds類別、SoundPlayer類別

namespace WindowsFormsApplication1
{
    // 要加入 參考 -> Microsoft.VisualBasic
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_wav\chimes.wav";

        public Form1()
        {
            InitializeComponent();
        }

        // 播放 Windows 作業系統音效事件類型關聯的音效
        private void button1_Click(object sender, EventArgs e)
        {
            SystemSounds.Asterisk.Play();
            //SystemSounds.Beep.Play();
            //SystemSounds.Exclamation.Play();
            //SystemSounds.Hand.Play();
            //SystemSounds.Question.Play();
        }

        // 播放外部的聲音檔
        private void button2_Click(object sender, EventArgs e)
        {
            // 聲音檔與執行檔同目錄
            SoundPlayer sound1 = new SoundPlayer(filename);
            sound1.Play();  // 播放
            //sound1.PlayLooping(); // 重複循環播放
            //sound1.PlaySync(); // 播放 -- 等候播放完成後，再繼續執行程式碼

            //sound1.Stop(); // 停止播放
        }

        // 播放資源內嵌的聲音檔
        private void button3_Click(object sender, EventArgs e)
        {
            SoundPlayer sound1 = new SoundPlayer(Properties.Resources.ding);
            sound1.Play(); // 播放
            //sound1.PlayLooping(); // 重複循環播放
            //sound1.PlaySync(); // 播放 -- 等候播放完成後，再繼續執行程式碼
        }
    }
}