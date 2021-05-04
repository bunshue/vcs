using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.VisualBasic;
using Microsoft.VisualBasic.Devices;

namespace WindowsFormsApplication1
{
    // 要加入 參考 -> Microsoft.VisualBasic
    public partial class Form1 : Form
    {
        Computer myComputer = new Computer();
        public Form1()
        {
            InitializeComponent();
        }

        // 播放在 Windows 音效配置中事件相關的音效
        private void button1_Click(object sender, EventArgs e)
        {
            myComputer.Audio.PlaySystemSound(System.Media.SystemSounds.Asterisk);
        }

        // 播放外部的聲音檔
        private void button2_Click(object sender, EventArgs e)
        {
            myComputer.Audio.Play("chimes.wav"); // 聲音檔與執行檔同目錄
        }

        // 播放資源內嵌的聲音檔
        private void button3_Click(object sender, EventArgs e)
        {
            myComputer.Audio.Play(Properties.Resources.ding, AudioPlayMode.WaitToComplete);
        }
    }
}