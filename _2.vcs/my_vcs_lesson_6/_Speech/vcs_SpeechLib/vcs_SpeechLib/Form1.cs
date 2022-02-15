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

        private void button3_Click(object sender, EventArgs e)
        {
            //fail

            return;

            Speach sp = Speach.instance();
            sp.Volume = 100;
            sp.Rate = 1;
            sp.AnalyseSpeak(this.richTextBox1.Text.Trim());
            //try
            //{
            //   SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            //   SpVoice Voice = new SpVoice();
            //   ///3表示是汉用，0124都表示英语，就是口音不同
            //   Voice.Voice = Voice.GetVoices(string.Empty, string.Empty).Item(0);
            //   //voice.Voice =voice.GetVoices(string.Empty, string.Empty).Item(0);
            //   Voice.Speak(this.textBox1.Text, SpFlags);
            //}
            //catch (Exception er)
            //{
            //   MessageBox.Show("An Error Occured!", "SpeechApp", MessageBoxButtons.OK, MessageBoxIcon.Error);
            //}

        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                string filename = Application.StartupPath + "\\wav_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".wav";

                SpeechVoiceSpeakFlags SpFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
                SpVoice Voice = new SpVoice();

                SpeechStreamFileMode SpFileMode = SpeechStreamFileMode.SSFMCreateForWrite;
                SpFileStream SpFileStream = new SpFileStream();
                SpFileStream.Open(filename, SpFileMode, false);
                Voice.AudioOutputStream = SpFileStream;
                Voice.Speak(this.richTextBox1.Text, SpFlags);
                Voice.WaitUntilDone(100);
                SpFileStream.Close();

                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show("An Error Occured!", "SpeechApp", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }

        }
    }

    public class Speach
    {
        private static Speach _Instance = null;
        private SpeechLib.SpVoiceClass voice = null;
        private Speach()
        {
            BuildSpeach();
        }
        public static Speach instance()
        {
            if (_Instance == null)
                _Instance = new Speach();
            return _Instance;
        }
        private void SetChinaVoice()
        {
            voice.Voice = voice.GetVoices(string.Empty, string.Empty).Item(3);
        }
        private void SetEnglishVoice()
        {
            voice.Voice = voice.GetVoices(string.Empty, string.Empty).Item(1);
        }
        private void SpeakChina(string strSpeak)
        {
            SetChinaVoice();
            Speak(strSpeak);
        }
        private void SpeakEnglishi(string strSpeak)
        {
            SetEnglishVoice();
            Speak(strSpeak);
        }

        public void AnalyseSpeak(string strSpeak)
        {
            int iCbeg = 0;
            int iEbeg = 0;
            bool IsChina = true;
            for (int i = 0; i < strSpeak.Length; i++)
            {
                /*
                char chr = strSpeak;
                if (IsChina)
                {
                    if (chr <= 122 && chr >= 65)
                    {
                        int iLen = i - iCbeg;
                        string strValue = strSpeak.Substring(iCbeg, iLen);
                        SpeakChina(strValue);
                        iEbeg = i;
                        IsChina = false;
                    }
                }
                else
                {
                    if (chr > 122 || chr < 65)
                    {
                        int iLen = i - iEbeg;
                        string strValue = strSpeak.Substring(iEbeg, iLen);

                        this.SpeakEnglishi(strValue);
                        iCbeg = i;
                        IsChina = true;
                    }
                }
                */
            }//end for
            if (IsChina)
            {
                int iLen = strSpeak.Length - iCbeg;
                string strValue = strSpeak.Substring(iCbeg, iLen);
                SpeakChina(strValue);
            }
            else
            {
                int iLen = strSpeak.Length - iEbeg;
                string strValue = strSpeak.Substring(iEbeg, iLen);
                SpeakEnglishi(strValue);
            }

        }
        private void BuildSpeach()
        {
            if (voice == null)
                voice = new SpVoiceClass();
        }
        public int Volume
        {
            get
            {
                return voice.Volume;
            }
            set
            {
                voice.SetVolume((ushort)(value));
            }
        }
        public int Rate
        {
            get
            {
                return voice.Rate;
            }
            set
            {
                voice.SetRate(value);
            }
        }
        private void Speak(string strSpeack)
        {
            try
            {
                voice.Speak(strSpeack, SpeechVoiceSpeakFlags.SVSFlagsAsync);
            }
            catch (Exception err)
            {
                throw (new Exception("发生一个错误：" + err.Message));
            }
        }

        public void Stop()
        {
            voice.Speak(string.Empty, SpeechLib.SpeechVoiceSpeakFlags.SVSFPurgeBeforeSpeak);
        }
        public void Pause()
        {
            voice.Pause();
        }
        public void Continue()
        {
            voice.Resume();
        }


    }//end class
}
