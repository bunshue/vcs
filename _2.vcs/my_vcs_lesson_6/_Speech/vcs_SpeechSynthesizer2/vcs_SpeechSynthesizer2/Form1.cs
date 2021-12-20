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
using System.Speech;
using System.Speech.Synthesis;  //for SpeechSynthesizer
using System.Speech.AudioFormat;    //for SpeechAudioFormatInfo

namespace vcs_SpeechSynthesizer2
{
    public partial class Form1 : Form
    {
        private SpeechSynthesizer synth = null;//語音對象

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            synth = new SpeechSynthesizer();
            synth.SpeakCompleted += new EventHandler<SpeakCompletedEventArgs>(synth_SpeakCompleted);
            //synth.SpeakStarted += SpeakStarted;
            //synth.SpeakCompleted += SpeakCompleted;
            /*
            SpeakCompleted：朗讀完成事件，朗讀完成後會觸發該時間。可以在該事件中處理播放完成後的流程。
            SpeakStarted：朗讀開始事件。
            SpeakProgress：朗讀過程事件，可以繼續一些進度條處理。
            */

            var voiceList = synth.GetInstalledVoices();
            richTextBox2.Text += "voiceList len = " + voiceList.Count.ToString() + "\n";

            foreach (InstalledVoice voice in synth.GetInstalledVoices())
            {
                VoiceInfo info = voice.VoiceInfo;
                richTextBox2.Text += "目前有安裝的人聲 Name : " + info.Name + "\n";
                richTextBox2.Text += "目前有安裝的人聲 Age : " + info.Age + "\n";
                richTextBox2.Text += "目前有安裝的人聲 Culture : " + info.Culture + "\n";
                richTextBox2.Text += "目前有安裝的人聲 AdditionalInfo : " + info.AdditionalInfo + "\n";
                richTextBox2.Text += "目前有安裝的人聲 Description : " + info.Description + "\n";
                richTextBox2.Text += "目前有安裝的人聲 Gender : " + info.Gender + "\n";
                richTextBox2.Text += "目前有安裝的人聲 Id : " + info.Id + "\n";
                richTextBox2.Text += "目前有安裝的人聲 SupportedAudioFormats Counts : " + info.SupportedAudioFormats.Count.ToString() + "\n";

                string AudioFormats = "";
                foreach (SpeechAudioFormatInfo fmt in info.SupportedAudioFormats)
                {
                    AudioFormats += String.Format("{0}\n", fmt.EncodingFormat.ToString());
                    richTextBox2.Text += "支援的 AudioFormats : " + AudioFormats + "\n";
                }

                string msg = string.Empty;
                foreach (string key in synth.Voice.AdditionalInfo.Keys)
                {
                    msg += String.Format("  {0}: {1}\n", key, synth.Voice.AdditionalInfo[key]);
                }
                richTextBox2.Text += "目前有安裝的人聲 AdditionalInfo : " + msg + "\n";
                richTextBox2.Text += "\n";
            }

            //Rate：播放語速，-10 ~ 10
            //Volume：音量調節：0 ~ 100

            richTextBox2.Text += "預設速度 : " + synth.Rate.ToString() + "\n";
            richTextBox2.Text += "預設音量 : " + synth.Volume.ToString() + "\n";

            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void synth_SpeakCompleted(object sender, EventArgs e)
        {
            richTextBox2.Text += "播放完成\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "播放\n";
            //synth.Rate = 0;       //Rate：播放語速，-10~10
            //synth.Volume = 10;    //Volume：音量調節：0~100
            //synth.SelectVoice("Microsoft Hanhan Desktop");
            richTextBox2.Text += "使用聲音 : " + synth.Voice.Name + "\n";
            synth.SpeakAsync(richTextBox1.Text);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "錄音存檔\n";
            string filename = Application.StartupPath + "\\wav_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

            synth.SetOutputToWaveFile(filename);    //保存語音文件
            //synth.SetOutputToWaveFile(filename, new SpeechAudioFormatInfo(48000, AudioBitsPerSample.Sixteen, AudioChannel.Stereo));
            //synth.SetOutputToWaveFile(filename, new SpeechAudioFormatInfo(16025, AudioBitsPerSample.Sixteen, AudioChannel.Mono));

            try
            {
                synth.SpeakAsync(richTextBox1.Text);
                //synth.SetOutputToNull();    //保存文件結束語句，必須調用該語句，否則生產的語音文件無法播放。
                //synth.SetOutputToDefaultAudioDevice();

                richTextBox2.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            synth.Pause();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            synth.Resume();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            /*
            SpeechSynthesizer synth = new SpeechSynthesizer();

            //synth.Rate = trackBarSpeed.Value;

            //synth.Volume = trackBarVolumn.Value;

            synth.SetOutputToWaveFile("aaaaa.wav");

            synth.Speak(richTextBox1.Text);

            synth.SetOutputToDefaultAudioDevice();

            MessageBox.Show("完成錄音~~", "提示");
            */


            /*
            SpeechSynthesizer synth = new SpeechSynthesizer();

            //synth.Rate = trackBarSpeed.Value;

            //synth.Volume = trackBarVolumn.Value;

            SaveFileDialog sfd = new SaveFileDialog();

            sfd.Filter = "Wave Files|*.wav";

            synth.SetOutputToWaveFile(sfd.FileName);

            synth.Speak(richTextBox1.Text);

            synth.SetOutputToDefaultAudioDevice();

            MessageBox.Show("完成錄音~~", "提示");
            */

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "Rate = " + synth.Rate.ToString() + "\n";
            richTextBox2.Text += "Volume = " + synth.Volume.ToString() + "\n";
            richTextBox2.Text += "Voice = " + synth.Voice + "\n";
            richTextBox2.Text += "State = " + synth.State.ToString() + "\n";


            foreach (InstalledVoice voice in synth.GetInstalledVoices())
            {
                VoiceInfo info = voice.VoiceInfo;
                richTextBox2.Text += " Voice Name: " + info.Name + "\n";
            }



            //synth.Rate = trackBarSpeed.Value;
            //synth.Volume = trackBarVolumn.Value;
            //synth.Rate = 0;       //Rate：播放語速，-10~10
            //synth.Volume = 10;    //Volume：音量調節：0~100


        }

        /// <summary>
        /// 開始朗讀 放在線程中
        /// </summary>
        /// <param name="VoiceObject"></param>
        public void ReadText(object VoiceObject)
        {
            try
            {
                synth.SpeakAsync(richTextBox1.Text);
            }
            catch (Exception er)
            {
                MessageBox.Show(er.ToString(), "提示", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Thread thread = new Thread(ReadText);
            thread.Start();

        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "SpeechToWavBytes 測試\n";
            string text = "豬屁股";
            byte[] TextBytes = SpeechToWavBytes(text);
            richTextBox2.Text += "len = " + TextBytes.Length.ToString() + "\n";

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
                SpeechSynthesizer synth = new SpeechSynthesizer();

                synth.SetOutputToWaveStream(memoryStream);
                synth.Speak(text);

                memoryStream.Flush();
                result = memoryStream.ToArray();
            }
            return result;
        }
    }
}
