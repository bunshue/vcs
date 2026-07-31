using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using SpeechLib;    //for SpVoiceClass
using System.Threading;

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
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            richTextBox1.Size = new Size(500, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(800, 750);
            this.Text = "vcs_SpeechLib";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個        

        private void button0_Click(object sender, EventArgs e)
        {
            string article1 = "Insight Medical Solutions Inc.";
            string article2 = "群曜醫電股份有限公司";

            SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;

            SpVoice Voice = new SpVoice();

            Voice.Speak(article1, SpFlags);
            Voice.Speak(article2, SpFlags);

            richTextBox1.Text += "完成\n";

            //------------------------------------------------------------  # 60個

            /*
            // 生成聲音文件(Wav)
            string filename = "tmp_generated_audio.wav";

            SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpVoice Voice = new SpVoice();
            SpeechStreamFileMode SpFileMode = SpeechStreamFileMode.SSFMCreateForWrite;
            SpFileStream SpFileStream = new SpFileStream();
            SpFileStream.Open(filename, SpFileMode, false);
            Voice.AudioOutputStream = SpFileStream;
            Voice.Speak(article1 + article2, SpFlags);
            Voice.WaitUntilDone(100);
            SpFileStream.Close();

            richTextBox1.Text += "已存檔 : " + filename + "\n";
            */

            //------------------------------------------------------------  # 60個

            string text = "VCS將Text轉成語音";

            SpVoice sv = new SpVoice();

            //sv.Rate = 0;  // 設置朗讀速度
            //SpeechVoiceSpeakFlags SSF = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            //sv.Speak(text, SSF);

            //------------------------------------------------------------  # 60個

            // 生成聲音文件

            SpeechVoiceSpeakFlags SVSF = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpeechStreamFileMode SSFM = SpeechStreamFileMode.SSFMCreateForWrite;
            SpFileStream SFS = new SpFileStream();
            string filename = "tmp_spvoice.wav";
            SFS.Open(filename, SSFM, false);
            sv.AudioOutputStream = SFS;
            sv.Speak(text, SVSF);
            sv.WaitUntilDone(System.Threading.Timeout.Infinite);
            SFS.Close();

            richTextBox1.Text += "done\n";

        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //SpVoiceClass1
            string article1 = "Insight Medical Solutions Inc.";
            string article2 = "群曜醫電股份有限公司";

            SpeechVoiceSpeakFlags spFlags = SpeechVoiceSpeakFlags.SVSFDefault;

            richTextBox1.Text += "\n應用一: 只說英文\n";

            //應用一: 只說英文
            SpVoiceClass spvc1 = new SpVoiceClass();
            //Item(1)女聲
            spvc1.Voice = spvc1.GetVoices(string.Empty, string.Empty).Item(1);
            //SVSFDefault: Specifies that the default settings
            spvc1.Speak(article1, spFlags);

            //------------------------------  # 30個

            richTextBox1.Text += "應用二: 說中文\n";
            SpVoiceClass spvc2 = new SpVoiceClass();
            spvc2.Voice = spvc2.GetVoices(string.Empty, string.Empty).Item(0);//Item(0)中文女聲

            spvc2.Speak(article2, spFlags);

            Thread.Sleep(1000);

            spvc2.Speak(article2, spFlags);
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //SpVoiceClass2
            SpVoiceClass spvc = new SpVoiceClass();

            /*
            int value = spvc.Volume;
            richTextBox1.Text += "Volume = " + value.ToString() + "\n";

            value = 70;
            spvc.SetVolume((ushort)(value));
            value = spvc.Volume;
            richTextBox1.Text += "Volume = " + value.ToString() + "\n";

            //------------------------------  # 30個

            int rate = spvc.Rate;
            richTextBox1.Text += "Rate = " + rate.ToString() + "\n";
            rate = 5;
            spvc.SetRate(rate);
            rate = spvc.Rate;
            richTextBox1.Text += "Rate = " + rate.ToString() + "\n";

            //------------------------------  # 30個
            */

            ISpeechObjectTokens tokens = spvc.GetVoices(string.Empty, string.Empty);
            //spvc.Voice = tokens.Item(0);

            //設定中文
            spvc.Voice = spvc.GetVoices(string.Empty, string.Empty).Item(0);

            //設定英文
            //spvc.Voice = spvc.GetVoices(string.Empty, string.Empty).Item(1);

            string text = "VCS將Text轉成語音";
            spvc.Speak(text, SpeechVoiceSpeakFlags.SVSFlagsAsync);

            SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            spvc.Speak(text, SpFlags);

            //Stop
            //spvc.Speak(string.Empty, SpeechVoiceSpeakFlags.SVSFPurgeBeforeSpeak);
            //Pause
            //spvc.Pause();
            //Resume
            //spvc.Resume();
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }
        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
            if (!Directory.Exists(filePath))
                Directory.CreateDirectory(filePath);
*/

// SpeechLib    的 SpVoice
// SpeechLib    的 SpVoiceClass()
// DotNetSpeech 的 SpVoice vo = new SpVoiceClass();

/*
dll檔案選sapi.dll
參考出現SpeechLib
引用要寫 using SpeechLib;
          
//------------------------------------------------------------  # 60個

微軟 SAPI.SpVoice C# 使用方法 + 實例
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/192842.html

//------------------------------------------------------------  # 60個

*/

