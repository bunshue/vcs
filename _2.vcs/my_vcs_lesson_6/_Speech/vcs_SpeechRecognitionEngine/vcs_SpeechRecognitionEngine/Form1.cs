using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Globalization; //for CultureInfo

using System.Speech;
using System.Speech.Recognition;    //for SpeechRecognitionEngine   //參考/加入參考/.NET/System.Speech
using System.Speech.Synthesis;

//語音識別
/*
在.NET4.0中，我可以借助System.Speech組件讓電腦來識別我們的聲音。
以上，當我說"name"，顯示"Darren"，我說"age",顯示"永遠21"。如何做呢？
首先要開啟電腦的語音識別功能。
右鍵電腦右下方的揚聲器，選擇"錄音設備"。
點擊默認的"麥克風"，再點擊左下角的"配置"按鈕。
點擊"啟動語音識別"。
*/

namespace vcs_SpeechRecognitionEngine
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
            show_item_location();

            //------------------------------------------------------------  # 60個

            //_recognizer.LoadGrammar(new Grammar(new GrammarBuilder("test")) { Name = "testGrammar" }); // load a grammar"test"

            /*
            Choices preCmd = new Choices();
            preCmd.Add(new string[] { "name", "age" });
            GrammarBuilder gb = new GrammarBuilder();
            gb.Append(preCmd);
            Grammar gr = new Grammar(gb);
            recEngine.LoadGrammarAsync(gr);
            recEngine.SetInputToDefaultAudioDevice();
            recEngine.SpeechRecognized += recEngine_SpeechRecognized;
            */
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
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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

        private void button0_Click(object sender, EventArgs e)
        {

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

        private void button3_Click(object sender, EventArgs e)
        {
            // Create an in-process speech recognizer for the en-US locale.  
            using (SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine(new CultureInfo("zh-tw")))
            {
                // Create and load a dictation grammar.  
                recognizer.LoadGrammar(new DictationGrammar());

                // Add a handler for the speech recognized event.  
                recognizer.SpeechRecognized += new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);

                // Configure input to the speech recognizer.  
                recognizer.SetInputToDefaultAudioDevice();

                // Start asynchronous, continuous speech recognition.  
                recognizer.RecognizeAsync(RecognizeMode.Multiple);

                // Keep the console window open.  
                while (true)
                {
                    Console.ReadLine();
                }
            }
        }

        // Handle the SpeechRecognized event.  
        static void recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            Console.WriteLine("Recognized text: " + e.Result.Text);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            SpeechRecognitionEngine sr = new SpeechRecognitionEngine();
            sr.SetInputToDefaultAudioDevice();
        }

        //------------------------------------------------------------  # 60個

        /*
        public void load_listen(VI_Profile profile, VI_Settings settings, ListView statusContainer)
        {
            this.profile = profile;
            this.settings = settings;
            this.statusContainer = statusContainer;

            vi_syn = profile.synth;

            SpeechRecognitionEngine recEngine = new SpeechRecognitionEngine(settings.recognizer_info);

            GrammarBuilder phrases_grammar = new GrammarBuilder();
            List<string> glossory = new List<string>();

            foreach (VI_Phrase trigger in profile.Profile_Triggers)
            {
                glossory.Add(trigger.value);
            }
            if (glossory.Count == 0)
            {
                MessageBox.Show("You need to add at least one Trigger");
                return;
            }
            phrases_grammar.Append(new Choices(glossory.ToArray()));

            recEngine.LoadGrammar(new Grammar(phrases_grammar));
            //set event function
            recEngine.SpeechRecognized += phraseRecognized;
            recEngine.SpeechRecognitionRejected += _recognizer_SpeechRecognitionRejected;
            recEngine.SetInputToDefaultAudioDevice();
            recEngine.RecognizeAsync(RecognizeMode.Multiple);
        }
        */
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


