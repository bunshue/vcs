using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Speech.Synthesis;  //for SpeechSynthesizer, 需要 參考/加入參考/.NET/System.Speech

using SpeechLib;

namespace vcs_SpeechSynthesizer3
{
    public partial class Form1 : Form
    {
        private SpeechSynthesizer synth = null;//語音對象

        class VoiceClass
        {

        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            synth = new SpeechSynthesizer();
        }

        /// <summary>
        /// 獲得朗讀設置對象
        /// </summary>
        /// <returns></returns>
        private VoiceClass GetVoiceClass()
        {
            VoiceClass setViceClass = new VoiceClass();
            setViceClass.VoiceName = cboTokens.Text;
            setViceClass.Rate = int.Parse(cboSpeed.Text);
            setViceClass.Volume = tbVoice.Value;
            setViceClass.VoiceText = txtInput.Text;
            return setViceClass;
        }

        /// <summary>
        /// 開始朗讀 放在線程中
        /// </summary>
        /// <param name="VoiceObject"></param>
        public void RingVoice(object VoiceObject)
        {
            try
            {
                //VoiceClass voiceClass = (VoiceClass)VoiceObject;
                //synth = GetSpeechSynthesizerInstance();
                //synth.SelectVoice(voiceClass.VoiceName);
                //synth.Rate = voiceClass.Rate;
                //synth.Volume = voiceClass.Volume;
                //synth.SpeakAsync(voiceClass.VoiceText);

                //synth.SelectVoice();
                synth.Rate = 5;
                synth.Volume = 5;
                synth.SpeakAsync(richTextBox1.Text);


            }
            catch (Exception er)
            {
                MessageBox.Show(er.ToString(), "提示", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //讀出richtextbox裡的文字
            SpeechVoiceSpeakFlags spFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
            SpVoice sp = new SpVoice();
            sp.Speak(richTextBox1.Text, spFlags);
            */
            //打開

            Thread thread = new Thread(RingVoice);
            thread.Start(setViceClass);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //播放

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //暫停

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //繼續

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //保存

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //退出

        }

    }
}
