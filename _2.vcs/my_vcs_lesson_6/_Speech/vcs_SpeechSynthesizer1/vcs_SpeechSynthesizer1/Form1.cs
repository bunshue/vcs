using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for MemoryStream
using System.Threading;

//實現語音朗讀功能
//參考/加入參考/.NET/System.Speech
//C#把文字轉換成聲音，
//在System.Speech命名空間下，
//SpeechSynthesizer類可以把文字讀出來
//把文字轉換成聲音, 使用微軟的NET_SystemSpeech

using System.Speech;
using System.Speech.Synthesis;  // for SpeechSynthesizer
using System.Speech.AudioFormat;    //for SpeechAudioFormatInfo

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

            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            synth = new SpeechSynthesizer();
            synth.SpeakCompleted += new EventHandler<SpeakCompletedEventArgs>(synth_SpeakCompleted);
            //synth.SpeakStarted += synth_SpeakStarted;
            /*
            SpeakCompleted：朗讀完成事件，朗讀完成後會觸發該時間。可以在該事件中處理播放完成後的流程。
            SpeakStarted：朗讀開始事件。
            SpeakProgress：朗讀過程事件，可以繼續一些進度條處理。
            */

            trackBar1.Value = synth.Rate;
            trackBar2.Value = synth.Volume;

            update_rate_volume();
        }

        private void synth_SpeakCompleted(object sender, EventArgs e)
        {
            richTextBox1.Text += "播放完成\n";
        }

        void update_rate_volume()
        {
            label1.Text = "播放速度 : " + trackBar1.Value.ToString();
            //synth.Pause();
            synth.Rate = trackBar1.Value;
            //synth.Resume();

            label2.Text = "音量大小 : " + trackBar2.Value.ToString();
            //synth.Pause();
            synth.Volume = trackBar2.Value;
            //synth.Resume();
        }

        private void show_item_location()
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
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);

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

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        /// <summary>
        /// 開始朗讀 放在線程中
        /// </summary>
        /// <param name="VoiceObject"></param>
        public void ReadText(object VoiceObject)
        {
            try
            {
                synth.SpeakAsync(richTextBox1.Text);	//開始進行異步朗讀，參數是朗讀的文本。
            }
            catch (Exception er)
            {
                MessageBox.Show(er.ToString(), "提示", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用thread播放
            Thread thread = new Thread(ReadText);
            thread.Start();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SpeechToWavBytes 測試\n";
            string text = "豬屁股";
            byte[] TextBytes = SpeechToWavBytes(text);
            richTextBox1.Text += "len = " + TextBytes.Length.ToString() + "\n";
        }

        /// <summary>
        /// See interface docs.
        /// </summary>
        /// <param name="speechText"></param>
        /// <returns></returns>
        public byte[] SpeechToWavBytes(string text)
        {
            if (text == null)
            {
                return null;
            }
            byte[] result = new byte[] { };

            using (MemoryStream memoryStream = new MemoryStream())
            {
                synth = new SpeechSynthesizer();

                synth.SetOutputToWaveStream(memoryStream);
                synth.Speak(text);	//開始進行朗讀，參數是朗讀的文本

                memoryStream.Flush();
                result = memoryStream.ToArray();
            }
            return result;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            synth = new SpeechSynthesizer();

            synth.SelectVoice("Microsoft Hanhan Desktop");	//選擇當前朗讀的人員，參數是朗讀者名稱，如：Microsoft Sam
            synth.Speak("Hi there, I am darkthread.");		//開始進行朗讀，參數是朗讀的文本

            synth.SelectVoice("Microsoft Zira Desktop");	//選擇當前朗讀的人員，參數是朗讀者名稱，如：Microsoft Sam
            synth.Speak("Hi there, I am darkthread.");		//開始進行朗讀，參數是朗讀的文本

            var pb = new PromptBuilder();
            pb.StartVoice("Microsoft Hanhan Desktop");
            pb.AppendText("大家好，我是黑暗執行緒");
            //https://msdn.microsoft.com/zh-tw/library/hh378418(v=office.14).aspx
            pb.AppendSsmlMarkup("<voice name=\"Microsoft David Desktop\">darkthread</voice>");
            pb.EndVoice();
            synth.Speak(pb);	//開始進行朗讀，參數是朗讀的文本

            synth.SelectVoice("Microsoft Tracy Desktop");	//選擇當前朗讀的人員，參數是朗讀者名稱，如：Microsoft Sam
            synth.Speak("大家好，我是黑暗執行緒");		//開始進行朗讀，參數是朗讀的文本
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private SpeechSynthesizer synth = null;//語音對象

        private void button10_Click(object sender, EventArgs e)
        {
            //播放
            richTextBox1.Text += "播放\n";
            //synth.Rate = 0;       //Rate：播放語速，-10~10
            //synth.Volume = 10;    //Volume：音量調節：0~100
            //synth.SelectVoice("Microsoft Hanhan Desktop");	//選擇當前朗讀的人員，參數是朗讀者名稱，如：Microsoft Sam
            richTextBox1.Text += "使用聲音 : " + synth.Voice.Name + "\n";
            synth.SpeakAsync(richTextBox1.Text);	//開始進行異步朗讀，參數是朗讀的文本。
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //錄音存檔
            richTextBox1.Text += "錄音存檔\n";
            string filename = Application.StartupPath + "\\wav_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

            synth.SetOutputToWaveFile(filename);    //保存語音文件,調用該方法後需要調用Speak方法。參數是保存文件的路徑。
            //synth.SetOutputToWaveFile(filename, new SpeechAudioFormatInfo(48000, AudioBitsPerSample.Sixteen, AudioChannel.Stereo));
            //synth.SetOutputToWaveFile(filename, new SpeechAudioFormatInfo(16025, AudioBitsPerSample.Sixteen, AudioChannel.Mono));

            try
            {
                synth.SpeakAsync(richTextBox1.Text);	//開始進行異步朗讀，參數是朗讀的文本。
                //synth.SetOutputToNull();    //保存文件結束語句，必須調用該語句，否則生產的語音文件無法播放。
                //      SetOutputToNull()：保存文件結束語句，必須調用該語句，否則生產的語音文件無法播放。

                //synth.SetOutputToDefaultAudioDevice();
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //暫停
            synth.Pause();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //繼續
            synth.Resume();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //錄音
            richTextBox1.Text += "錄音存檔\n";
            string filename = Application.StartupPath + "\\wav_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

            synth = new SpeechSynthesizer();

            synth.Rate = trackBar1.Value;
            synth.Volume = trackBar2.Value;

            synth.SetOutputToWaveFile(filename);	//保存語音文件,調用該方法後需要調用Speak方法。參數是保存文件的路徑。

            synth.Speak(richTextBox1.Text);	//開始進行朗讀，參數是朗讀的文本

            synth.SetOutputToDefaultAudioDevice();

            richTextBox1.Text += "已存檔 : " + filename + "\n";

        }

        private void bt_info_Click(object sender, EventArgs e)
        {
            show_speech_info();
        }

        void show_speech_info()
        {
            richTextBox1.Clear();
            richTextBox1.Text += "播放速度 Rate = " + synth.Rate.ToString() + "\t\t範圍 : -10 ~ 10\n";
            richTextBox1.Text += "音量大小 Volume = " + synth.Volume.ToString() + "\t範圍 : 0 ~ 100\n";

            //richTextBox1.Text += "Voice = " + synth.Voice + "\n";
            richTextBox1.Text += "當前朗讀的人員 = " + synth.Voice.Name + "\n";
            //richTextBox1.Text += "State = " + synth.State.ToString() + "\n";

            foreach (InstalledVoice voice in synth.GetInstalledVoices())
            {
                VoiceInfo info = voice.VoiceInfo;
                richTextBox1.Text += "目前已安裝的朗讀人員 : " + info.Name + "\n";
            }
            ListInstalledVoices();
        }

        void ListInstalledVoices()
        {
            richTextBox1.Text += "\n列出Windows 裝了哪些語音以及其支援語系\n";
            synth = new SpeechSynthesizer();

            var voiceList = synth.GetInstalledVoices();		//GetInstalledVoices 獲取當前系統中安裝的語音播放人員，返回一個VoiceInfo對象集合
            richTextBox1.Text += "目前有安裝的人聲 有 " + voiceList.Count.ToString() + " 種\n";
            int i = 1;
            foreach (InstalledVoice voice in synth.GetInstalledVoices())
            {
                richTextBox1.Text += "第 " + (i++).ToString() + " 種\n";
                VoiceInfo info = voice.VoiceInfo;
                richTextBox1.Text += "目前有安裝的人聲 Name : " + info.Name + "\n";
                richTextBox1.Text += "目前有安裝的人聲 Age : " + info.Age + "\n";
                richTextBox1.Text += "目前有安裝的人聲 DisplayName : " + info.Culture.DisplayName + "\n";
                richTextBox1.Text += "目前有安裝的人聲 Culture : " + info.Culture + "\n";
                richTextBox1.Text += "目前有安裝的人聲 AdditionalInfo : " + info.AdditionalInfo + "\n";
                richTextBox1.Text += "目前有安裝的人聲 Description : " + info.Description + "\n";
                richTextBox1.Text += "目前有安裝的人聲 Gender : " + info.Gender + "\n";
                richTextBox1.Text += "目前有安裝的人聲 Id : " + info.Id + "\n";
                richTextBox1.Text += "目前有安裝的人聲 SupportedAudioFormats Counts : " + info.SupportedAudioFormats.Count.ToString() + "\n";

                string AudioFormats = "";
                foreach (SpeechAudioFormatInfo fmt in info.SupportedAudioFormats)
                {
                    AudioFormats += String.Format("{0}\n", fmt.EncodingFormat.ToString());
                    richTextBox1.Text += "支援的 AudioFormats : " + AudioFormats + "\n";
                }

                string msg = string.Empty;
                foreach (string key in synth.Voice.AdditionalInfo.Keys)
                {
                    msg += String.Format("  {0}: {1}\n", key, synth.Voice.AdditionalInfo[key]);
                }
                richTextBox1.Text += "目前有安裝的人聲 AdditionalInfo : " + msg + "\n";
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "預設速度 : " + synth.Rate.ToString() + "\n";
            richTextBox1.Text += "預設音量 : " + synth.Volume.ToString() + "\n";
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            update_rate_volume();
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            update_rate_volume();
        }
    }
}
