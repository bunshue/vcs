using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_test_all_24_DllImport_VolumeControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //user32控制方式
        // 宣告常式 
        private const int APPCOMMAND_VOLUME_MUTE = 0x80000;
        private const int APPCOMMAND_VOLUME_UP = 0x0a0000;
        private const int APPCOMMAND_VOLUME_DOWN = 0x090000;
        private const int WM_APPCOMMAND = 0x319;

        [DllImport("user32.dll")]
        public static extern IntPtr SendMessageW(IntPtr hWnd, int Msg, IntPtr wParam, IntPtr lParam);
        
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

        //winmm控制方式
        [DllImport("winmm.dll", EntryPoint = "waveOutSetVolume")]
        public static extern int WaveOutSetVolume(IntPtr hwo, uint dwVolume);

        int audio_channel = 2;

        private void SetVol(double arg)
        {
            // winmm控制方式，涉及Xp系统波形声音的左右声道，高位为左声道，低位为右声道
            double newVolume = ushort.MaxValue * arg / 10.0;

            uint v = ((uint)newVolume) & 0xffff;
            uint Value = 0;

            //限制音量的取值範圍
            if (v < 0)
                v = 0;
            if (v > 0xffff)
                v = 0xffff;
            System.UInt32 left = (System.UInt32)v; //左聲道音量
            System.UInt32 right = (System.UInt32)v;//右聲道音量

            if (audio_channel == 0)
                right = 0;
            else if (audio_channel == 1)
                left = 0;

            Value = right << 16 | left;

            //waveOutSetVolume(0, left << 16 | right);   //邏輯左移後合併  可能左右相反
            WaveOutSetVolume(IntPtr.Zero, Value);
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            //richTextBox1.Text += "get value : " + trackBar1.Value.ToString() + "\n";
            SetVol(((double)trackBar1.Value) / 10);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            audio_channel = 0;
            SetVol(((double)trackBar1.Value) / 10);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            audio_channel = 1;
            SetVol(((double)trackBar1.Value) / 10);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            audio_channel = 2;
            SetVol(((double)trackBar1.Value) / 10);
        }
    }
}
