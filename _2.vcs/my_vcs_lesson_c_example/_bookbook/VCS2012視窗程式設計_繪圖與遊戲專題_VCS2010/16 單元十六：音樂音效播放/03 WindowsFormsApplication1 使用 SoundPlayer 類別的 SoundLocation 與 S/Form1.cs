using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Media; // SoundPlayer 類別

namespace WindowsFormsApplication1
{
    // 要加入 參考 -> Microsoft.VisualBasic
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 播放外部的聲音檔
        private void button2_Click(object sender, EventArgs e)
        {
            SoundPlayer sound1 = new SoundPlayer(); // 新增一個SoundPlayer物件

            sound1.SoundLocation = "chimes.wav"; // 設定聲音檔案的路徑和名稱
            sound1.Play(); // 播放
        }

        // 播放資源內嵌的聲音檔
        private void button3_Click(object sender, EventArgs e)
        {
            SoundPlayer sound1 = new SoundPlayer();// 新增一個SoundPlayer物件

            sound1.Stream = Properties.Resources.ding; // 設定檔案的串流 從專案的資源來的
            sound1.Play(); // 播放
        }
    }
}