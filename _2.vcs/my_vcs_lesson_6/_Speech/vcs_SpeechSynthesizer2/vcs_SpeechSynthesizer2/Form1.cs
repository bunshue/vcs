using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Speech;
using System.Speech.Synthesis;

//參考/加入參考/.NET/System.Speech

namespace vcs_SpeechSynthesizer2
{
    public partial class Form1 : Form
    {
        private SpeechSynthesizer ss;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ss = new SpeechSynthesizer();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //ss.Rate = trackBarSpeed.Value;
            //ss.Volume = trackBarVolumn.Value;
            ss.SpeakAsync(richTextBox1.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ss.Pause();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            ss.Resume();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            /*
            SpeechSynthesizer ss = new SpeechSynthesizer();

            //ss.Rate = trackBarSpeed.Value;

            //ss.Volume = trackBarVolumn.Value;

            ss.SetOutputToWaveFile("aaaaa.wav");

            ss.Speak(richTextBox1.Text);

            ss.SetOutputToDefaultAudioDevice();

            MessageBox.Show("完成錄音~~", "提示");
            */


            /*
            SpeechSynthesizer ss = new SpeechSynthesizer();

            //ss.Rate = trackBarSpeed.Value;

            //ss.Volume = trackBarVolumn.Value;

            SaveFileDialog sfd = new SaveFileDialog();

            sfd.Filter = "Wave Files|*.wav";

            ss.SetOutputToWaveFile(sfd.FileName);

            ss.Speak(richTextBox1.Text);

            ss.SetOutputToDefaultAudioDevice();

            MessageBox.Show("完成錄音~~", "提示");
            */

        }
    }
}
