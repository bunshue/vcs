using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Media; //for SoundPlayer

using System.Runtime.InteropServices;   //for MCI
namespace vcs_PlaySound
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            SystemSounds.Asterisk.Play();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SystemSounds.Beep.Play();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SystemSounds.Exclamation.Play();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            SystemSounds.Hand.Play();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            SystemSounds.Question.Play();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_wav\start.wav";

            SoundPlayer player = new SoundPlayer();
            player.SoundLocation = filename;
            player.Load(); //同步加載聲音
            player.Play(); //啟用新線程播放
            //player.PlayLooping(); //循環播放模式
            //player.PlaySync(); //UI線程播放
        }
    }
}
