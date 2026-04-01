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

namespace vcs_SpeechSynthesizer1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(750, 340);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 750);
            this.Text = "vcs_SpeechSynthesizer1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
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
