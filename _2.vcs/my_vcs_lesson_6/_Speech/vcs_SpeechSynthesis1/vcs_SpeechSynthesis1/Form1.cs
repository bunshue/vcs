using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考/加入參考/.NET/System.Speech
using System.Speech.Synthesis;  // for SpeechSynthesizer

namespace vcs_SpeechSynthesis1
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
            //最簡易
            //SpeechSynthesizer synth = new SpeechSynthesizer();
            //synth.Speak("這是 Copilot 的回覆，現在用電腦喇叭播放出來。");

            // 建立語音合成器
            SpeechSynthesizer synth = new SpeechSynthesizer();

            // 設定語音輸出到預設音效裝置 (電腦喇叭)
            synth.SetOutputToDefaultAudioDevice();

            // 可選：設定語速與音量
            synth.Rate = 0;   // -10 (最慢) 到 10 (最快)，0 為正常速度
            synth.Volume = 100; // 0 到 100

            // 可選：選擇不同的語音 (取決於系統安裝的語音包)
            foreach (var voice in synth.GetInstalledVoices())
            {
                richTextBox1.Text += "可用語音: " + voice.VoiceInfo.Name + "\n";
                //Console.WriteLine(
            }
            synth.SelectVoice("Microsoft Hanhan Desktop"); // 中文語音
            //synth.SelectVoice("Microsoft Zira Desktop"); // 英文語音

            // 播放文字
            string textToSpeak = "這是 Copilot 的回覆，現在用電腦喇叭播放出來。";
            synth.Speak(textToSpeak);

        }
    }
}
