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
參考/加入參考/COM/Microsoft Speech Object Library, 選sapi.dll

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
            string article1 = "When his father died, he left an estate of one million dollars.";
            string article2 = "他父親去世時留下了一百萬元遺產。";
            string article3 = "When his father died, he left an estate of one million dollars. 他父親去世時留下了一百萬元遺產。";

            #region 應用一: 只說英文
            SpVoiceClass voice1 = new SpVoiceClass();
            //Item(1)女聲
            voice1.Voice = voice1.GetVoices(string.Empty, string.Empty).Item(1);
            //SVSFDefault: Specifies that the default settings
            voice1.Speak(article1, SpeechVoiceSpeakFlags.SVSFDefault);
            #endregion


            #region 應用二: 說中文
            SpVoiceClass voice2 = new SpVoiceClass();
            voice2.Voice = voice2.GetVoices(string.Empty, string.Empty).Item(0);//Item(0)中文女聲
            voice2.Speak(article2, SpeechVoiceSpeakFlags.SVSFDefault);

            System.Threading.Thread.Sleep(3000);
            voice2.Speak(article2, SpeechVoiceSpeakFlags.SVSFDefault);

            System.Threading.Thread.Sleep(3000);
            voice2.Speak(article2, SpeechVoiceSpeakFlags.SVSFDefault);

            #endregion


        }
    }
}
