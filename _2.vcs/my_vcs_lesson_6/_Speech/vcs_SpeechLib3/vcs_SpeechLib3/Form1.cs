using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using SpeechLib;        //參考/加入參考/COM/Microsoft Speech Object Library 5.4	C:\Windows\System32\Speech\Common\sapi.dll

namespace vcs_SpeechLib3
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
            //讀出richtextbox裡的文字
            SpeechVoiceSpeakFlags spFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpVoice sp = new SpVoice();
            sp.Speak(richTextBox1.Text, spFlags);
        }
    }
}
