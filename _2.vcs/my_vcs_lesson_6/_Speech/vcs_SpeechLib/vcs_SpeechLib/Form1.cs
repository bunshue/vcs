using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using SpeechLib;
/*
參考/加入參考/COM/Microsoft Speech Object Library 5.4 選 C:\Windows\System32\Speech\Common\sapi.dll

把參考SpeechLib的屬性 [內嵌Interop類型]設為 False
*/

namespace vcs_SpeechLib
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

        private void button2_Click(object sender, EventArgs e)
        {
            string article1 = "Insight Medical Solutions Inc.";
            string article2 = "群曜醫電股份有限公司";

            richTextBox1.Text += "\n應用一: 只說英文\n";
            //應用一: 只說英文
            SpVoiceClass voice1 = new SpVoiceClass();
            //Item(1)女聲
            voice1.Voice = voice1.GetVoices(string.Empty, string.Empty).Item(1);
            //SVSFDefault: Specifies that the default settings
            voice1.Speak(article1, SpeechVoiceSpeakFlags.SVSFDefault);

            richTextBox1.Text += "應用二: 說中文\n";
            SpVoiceClass voice2 = new SpVoiceClass();
            voice2.Voice = voice2.GetVoices(string.Empty, string.Empty).Item(0);//Item(0)中文女聲
            voice2.Speak(article2, SpeechVoiceSpeakFlags.SVSFDefault);

            System.Threading.Thread.Sleep(1000);
            voice2.Speak(article2, SpeechVoiceSpeakFlags.SVSFDefault);

            richTextBox1.Text += "應用三: 說英文中文\n";
            //讀出richtextbox裡的文字
            SpeechVoiceSpeakFlags spFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpVoice sp = new SpVoice();
            sp.Speak(article1 + article2, spFlags);
        }
    }
}
