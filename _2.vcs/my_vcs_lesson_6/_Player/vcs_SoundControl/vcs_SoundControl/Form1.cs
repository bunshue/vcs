using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic;            //for AudioPlayMode //引用Microsoft.VisualBasic命名空間
using Microsoft.VisualBasic.Devices;    //for Computer      //引用Microsoft.VisualBasic.Devices命名空間
using System.Runtime.InteropServices;   //for DllImport

//參考/加入參考/.NET/Microsoft.VisualBasic

namespace vcs_SoundControl
{
    public partial class Form1 : Form
    {
        // C# 控制電腦靜音與音量 
        // 使用Windows API控制電腦靜音與音量
        // 宣告常式 
        private const int APPCOMMAND_VOLUME_MUTE = 0x80000;
        private const int APPCOMMAND_VOLUME_UP = 0x0a0000;
        private const int APPCOMMAND_VOLUME_DOWN = 0x090000;
        private const int WM_APPCOMMAND = 0x319;

        [DllImport("user32.dll")]
        public static extern IntPtr SendMessageW(IntPtr hWnd, int Msg, IntPtr wParam, IntPtr lParam);

        //for Computer,          //參考/加入參考/.NET/Microsoft.VisualBasic
        Computer myComputer = new Computer();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            //richTextBox1.Size = new Size(400, 690);
            //richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(900, 750);
            this.Text = "vcs_SoundControl";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            // 聲音變大 
            SendMessageW(this.Handle, WM_APPCOMMAND, this.Handle, (IntPtr)APPCOMMAND_VOLUME_UP);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 聲音變小 
            SendMessageW(this.Handle, WM_APPCOMMAND, this.Handle, (IntPtr)APPCOMMAND_VOLUME_DOWN);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 靜音 
            SendMessageW(this.Handle, WM_APPCOMMAND, this.Handle, (IntPtr)APPCOMMAND_VOLUME_MUTE);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 播放在 Windows 音效配置中事件相關的音效
            myComputer.Audio.PlaySystemSound(System.Media.SystemSounds.Asterisk);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 播放外部的聲音檔
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_wav\chimes.wav";
            myComputer.Audio.Play(filename); // 聲音檔與執行檔同目錄
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 播放資源內嵌的聲音檔
            myComputer.Audio.Play(Properties.Resources.ding, AudioPlayMode.WaitToComplete);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_wav\";
            string filename = string.Empty;

            Random rnd = new Random();  //產生亂數物件rnd
            int testNum = rnd.Next(1, 11);  //產生1~10的亂數
            richTextBox1.Text += testNum.ToString() + "\n";
            filename = foldername + Convert.ToString(testNum) + ".wav";  //合併成數字聲音檔
            richTextBox1.Text += "filename = " + filename + "\n";

            Computer myComputer = new Computer();
            //播放數字聲音檔
            myComputer.Audio.Play(filename, AudioPlayMode.WaitToComplete);
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/



