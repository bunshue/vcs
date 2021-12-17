using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Speech;
using System.Speech.Recognition;    //for SpeechRecognitionEngine
//參考/加入參考/.NET/System.Speech

using System.Speech.Synthesis;
using System.Threading;

//語音識別
/*
在.NET4.0中，我可以借助System.Speech組件讓電腦來識別我們的聲音。

[1]

以上，當我說"name"，顯示"Darren"，我說"age",顯示"永遠21"。如何做呢？

首先要開啟電腦的語音識別功能。

右鍵電腦右下方的揚聲器，選擇"錄音設備"。

點擊默認的"麥克風"，再點擊左下角的"配置"按鈕。

[2]

點擊"啟動語音識別"。
*/

namespace speech
{
    public partial class Form1 : Form
    {
        SpeechRecognitionEngine recEngine = new SpeechRecognitionEngine();
        //SpeechRecognitionEngine _recognizer = new SpeechRecognitionEngine();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //_recognizer.LoadGrammar(new Grammar(new GrammarBuilder("test")) { Name = "testGrammar" }); // load a grammar"test"

            Choices preCmd = new Choices();

            preCmd.Add(new string[] { "name", "age" });

            GrammarBuilder gb = new GrammarBuilder();

            gb.Append(preCmd);

            Grammar gr = new Grammar(gb);

            recEngine.LoadGrammarAsync(gr);

            recEngine.SetInputToDefaultAudioDevice();

            recEngine.SpeechRecognized += recEngine_SpeechRecognized;


        }

        void recEngine_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            switch (e.Result.Text)
            {
                case "name":
                    richTextBox1.Text += "\nDarren";
                    break;
                case "age":
                    richTextBox1.Text += "\n永遠21";
                    break;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //_recognizer.LoadGrammar(new Grammar(new GrammarBuilder("test")) { Name = "testGrammar" }); // load a grammar"test"    same

            /*
            Grammar gr = new Grammar(new GrammarBuilder("test"));
            gr.Name = "testGrammar";
            _recognizer.LoadGrammar(gr);
            */

            recEngine.RecognizeAsync(RecognizeMode.Multiple);



        }

        private void button2_Click(object sender, EventArgs e)
        {
            recEngine.RecognizeAsyncStop();

        }
    }
}
