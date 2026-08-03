using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;
using System.Globalization;  // for CultureInfo

using System.Speech;
using System.Speech.Recognition;  // for SpeechRecognitionEngine   //參考/加入參考/.NET/System.Speech
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
        string speech_text = "影像邊緣檢測(edge detection) 函數 Canny() Sobel()";

        // 創建識別器物件
        SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine(new CultureInfo("zh-tw"));

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
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

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

        //------------------------------------------------------------  # 60個

        // Handle the SpeechRecognized event.  
        void recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            //語音辨識結果
            richTextBox1.Text += "語音辨識結果 : " + e.Result.Text + "\n";
            richTextBox1.Text += "語音辨識信心 : " + e.Result.Confidence + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            String textFilePath = "result.txt";
            string waveFilePath = "tmp_spvoice2.wav";

            // Create an in-process speech recognizer for the en-US locale.  // 創建識別器物件
            using (SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine(new CultureInfo("zh-tw")))
            {
                // Create and load a dictation grammar.
                recognizer.LoadGrammar(new DictationGrammar());

                // Add a handler for the speech recognized event.  
                recognizer.SpeechRecognized += new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);

                // Configure input to the speech recognizer.
                recognizer.SetInputToWaveFile(waveFilePath);  // 設定語音辨識的來源裝置 為 音頻檔案
                //recognizer.SetInputToDefaultAudioDevice();  // 設定語音辨識的來源裝置 為 音頻設備

                // Modify the initial silence time-out value.
                recognizer.InitialSilenceTimeout = TimeSpan.FromSeconds(500);

                // Start synchronous speech recognition.
                RecognitionResult result = recognizer.Recognize();  // 啟動語音辨識

                if (result != null)
                {
                    //FileStream fs = new FileStream(textFilePath, FileMode.Open, FileAccess.ReadWrite);
                    StreamWriter sw = File.CreateText(textFilePath);
                    //fs.SetLength(0);//首先把文件清空了。
                    sw.Write(result.Text);//写你的字符串。
                    sw.Close();
                    richTextBox1.Text += "辨識結果 : " + result.Text + "\n";
                }
                else
                {
                    richTextBox1.Text += "辨識失敗\n";
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            // MSDN的範例, 看起來是要從麥克風輸入語音再轉文字

            // Create an in-process speech recognizer for the en-US locale.  // 創建識別器物件
            using (SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine(new CultureInfo("zh-tw")))
            {
                // Create and load a dictation grammar.  
                recognizer.LoadGrammar(new DictationGrammar());

                // Add a handler for the speech recognized event.  
                recognizer.SpeechRecognized += new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);

                // Configure input to the speech recognizer.  
                recognizer.SetInputToDefaultAudioDevice();  // 設定語音辨識的來源裝置 為 音頻設備

                // Start asynchronous, continuous speech recognition.  
                recognizer.RecognizeAsync(RecognizeMode.Multiple);  // 啟動語音辨識

                // Keep the console window open.  
                while (true)
                {
                    Console.ReadLine();
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //建立字典 dictation 聽寫

            // 創建識別器物件
            SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine();

            Choices preCmd = new Choices();
            preCmd.Add(new string[] { "name", "age" });
            GrammarBuilder gb = new GrammarBuilder();
            gb.Append(preCmd);
            //Grammar gr = new Grammar(gb);
            //recognizer.LoadGrammarAsync(gr);

            //3030

            //recognizer.LoadGrammar(new Grammar(new GrammarBuilder("test")) { Name = "testGrammar" }); // load a grammar"test"    same
            Grammar gr = new Grammar(new GrammarBuilder("test"));
            gr.Name = "testGrammar";
            recognizer.LoadGrammar(gr);

            //3030

            GrammarBuilder phrases_grammar = new GrammarBuilder();

            List<string> glossory = new List<string>();

            glossory.Add("trigger1");
            glossory.Add("trigger2");
            glossory.Add("trigger3");

            phrases_grammar.Append(new Choices(glossory.ToArray()));

            recognizer.LoadGrammar(new Grammar(phrases_grammar));
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //列出內建的語音辨識引擎名稱

            foreach (var x in SpeechRecognitionEngine.InstalledRecognizers())
            {
                richTextBox1.Text += x.Name + "\n";
            }

            foreach (var x in SpeechRecognitionEngine.InstalledRecognizers())
            {
                richTextBox1.Text += x.Culture.Name + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //測試 msdn上的範例

            recognizer.SetInputToDefaultAudioDevice();  // 設定語音辨識的來源裝置 為 音頻設備
            recognizer.SpeechRecognized += recognizer_SpeechRecognized2;
            Grammar g_HelloGoodbye = GetHelloGoodbyeGrammar();
            Grammar g_SetTextBox = GetTextBox1TextGrammar();
            recognizer.LoadGrammarAsync(g_HelloGoodbye);
            recognizer.LoadGrammarAsync(g_SetTextBox);
            recognizer.RecognizeAsync(RecognizeMode.Multiple);  // 啟動語音辨識
        }


        static Grammar GetHelloGoodbyeGrammar()
        {
            Choices ch_HelloGoodbye = new Choices();
            ch_HelloGoodbye.Add("hello");
            ch_HelloGoodbye.Add("goodbye");
            GrammarBuilder gb_result = new GrammarBuilder(ch_HelloGoodbye);
            Grammar g_result = new Grammar(gb_result);
            return g_result;
        }

        static Grammar GetTextBox1TextGrammar()
        {
            Choices ch_Colors = new Choices();
            ch_Colors.Add(new string[] { "red", "white", "blue" });
            GrammarBuilder gb_result = new GrammarBuilder();
            gb_result.Append("set text box 1");
            gb_result.Append(ch_Colors);
            Grammar g_result = new Grammar(gb_result);
            return g_result;
        }

        void recognizer_SpeechRecognized2(object sender, SpeechRecognizedEventArgs e)
        {
            string txt = e.Result.Text;
            float confidence = e.Result.Confidence;
            if (confidence < 0.65) return;

            //"I heard you say: " + txt

            if (txt.IndexOf("text") >= 0 && txt.IndexOf("box") >= 0 && txt.IndexOf("1") >= 0)
            {
                string[] words = txt.Split(' ');

                //textBox1.Text = words[4];
            }
        }


        static bool done = false;
        static bool speechOn = true;

        void recognizer_SpeechRecognized2b(object sender, SpeechRecognizedEventArgs e)
        {
            string txt = e.Result.Text;
            float confidence = e.Result.Confidence;
            Console.WriteLine("\nRecognized: " + txt);
            if (confidence < 0.60) return;

            if (txt.IndexOf("speech on") >= 0)
            {
                Console.WriteLine("Speech is now ON");
                speechOn = true;
            }

            if (txt.IndexOf("speech off") >= 0)
            {
                Console.WriteLine("Speech is now OFF");
                speechOn = false;
            }

            if (speechOn == false)
                return;

            if (txt.IndexOf("klatu") >= 0 && txt.IndexOf("barada") >= 0)
            {
                ((SpeechRecognitionEngine)sender).RecognizeAsyncCancel();
                done = true;
                Console.WriteLine("(Speaking: Farewell)");
            }

            if (txt.IndexOf("What") >= 0 && txt.IndexOf("plus") >= 0)
            {
                string[] words = txt.Split(' ');
                int num1 = int.Parse(words[2]);
                int num2 = int.Parse(words[4]);
                int sum = num1 + num2;
                Console.WriteLine("(Speaking: " + words[2] + " plus " + words[4] + " equals " + sum + ")");
            }
        }

        // recognizer_SpeechRecognized2b

        //------------------------------------------------------------  # 60個

        SpeechRecognitionEngine sr = new SpeechRecognitionEngine();

        private string Greet { get; set; }

        private void button5_Click(object sender, EventArgs e)
        {
            Choices inputs = new Choices();
            inputs.Add(new string[] { "hello", "goodbye", "my name is" });
            GrammarBuilder gb = new GrammarBuilder();
            gb.Append(inputs);
            Grammar g = new Grammar(gb);

            sr.SetInputToDefaultAudioDevice();  // 設定語音辨識的來源裝置 為 音頻設備
            sr.LoadGrammarAsync(g);
            sr.SpeechRecognized += sr_SpeechRecognized;
            sr.RecognizeAsync(RecognizeMode.Multiple);
        }

        void sr_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            MessageBox.Show("Speech recognized: " + e.Result.Text);
            if (e.Result.Text == "my name is")
            {
                // store the users name in a variable
            }
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            // Initialize an in-process speech recognition engine.
            using (SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine())
            {
                // Create a grammar.
                //  Create lists of alternative choices.
                Choices listTypes = new Choices(new string[] { "albums", "artists" });
                Choices genres = new Choices(new string[] {
          "blues", "classical", "gospel", "jazz", "rock" });

                //  Create a GrammarBuilder object and assemble the grammar components.
                GrammarBuilder mediaMenu = new GrammarBuilder("Display the list of");
                mediaMenu.Append(listTypes);
                mediaMenu.Append("in the");
                mediaMenu.Append(genres);
                mediaMenu.Append("category.");

                //  Build a Grammar object from the GrammarBuilder.
                Grammar mediaMenuGrammar = new Grammar(mediaMenu);
                mediaMenuGrammar.Name = "Media Chooser";

                // Attach event handlers.
                recognizer.LoadGrammarCompleted +=
                  new EventHandler<LoadGrammarCompletedEventArgs>(recognizer_LoadGrammarCompleted);
                recognizer.SpeechRecognized +=
                  new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized3);
                recognizer.SpeechHypothesized +=
                  new EventHandler<SpeechHypothesizedEventArgs>(recognizer_SpeechHypothesized);

                // Load the grammar object to the recognizer.
                recognizer.LoadGrammarAsync(mediaMenuGrammar);

                recognizer.SetInputToDefaultAudioDevice();  // 設定語音辨識的來源裝置 為 音頻設備

                // Start asynchronous recognition.
                recognizer.RecognizeAsync();
            }
        }

        // Handle the SpeechHypothesized event.
        static void recognizer_SpeechHypothesized(object sender, SpeechHypothesizedEventArgs e)
        {
            Console.WriteLine("Speech hypothesized: " + e.Result.Text);
        }

        // Handle the LoadGrammarCompleted event.
        static void recognizer_LoadGrammarCompleted(object sender, LoadGrammarCompletedEventArgs e)
        {
            Console.WriteLine("Grammar loaded: " + e.Grammar.Name);
            Console.WriteLine();
        }

        // Handle the SpeechRecognized event.
        static void recognizer_SpeechRecognized3(object sender, SpeechRecognizedEventArgs e)
        {
            Console.WriteLine();
            Console.WriteLine("Speech recognized: " + e.Result.Text);
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            /*
            參考
        https://blog.darkthread.net/blog/sapi-demo/

            */

            // 創建識別器物件
            SpeechRecognitionEngine recognizer = new SpeechRecognitionEngine(new CultureInfo("zh-tw"));

            recognizer.SetInputToDefaultAudioDevice();  // 設定語音辨識的來源裝置 為 音頻設備

            recognizer.LoadGrammar(new DictationGrammar());

            recognizer.SpeechRecognized += new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);

            /*
            recognizer.SpeechRecognized += (sender, e) =>
            {   //識別即念出
                Console.WriteLine(e.Result.Text);
                speak(e.Result.Text);
            };
            */
            recognizer.RecognizeAsync(RecognizeMode.Multiple);
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
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


//開啟
//recognizer.RecognizeAsync(RecognizeMode.Multiple);
//關閉
//recognizer.RecognizeAsyncCancel();
//停止
//recognizer.RecognizeAsyncStop();

/*
Choices ch_StartStopCommands = new Choices();
ch_StartStopCommands.Add("speech on");
ch_StartStopCommands.Add("speech off");
ch_StartStopCommands.Add("klatu barada nikto");
GrammarBuilder gb_StartStop = new GrammarBuilder();
gb_StartStop.Append(ch_StartStopCommands);
Grammar g_StartStop = new Grammar(gb_StartStop);

//演示設置識別命令以添加兩個數字的能力
Choices ch_Numbers = new Choices();
ch_Numbers.Add("1");
ch_Numbers.Add("2");
ch_Numbers.Add("3");
ch_Numbers.Add("4");

GrammarBuilder gb_WhatIsXplusY = new GrammarBuilder();
gb_WhatIsXplusY.Append("What is");
gb_WhatIsXplusY.Append(ch_Numbers);
gb_WhatIsXplusY.Append("plus");
gb_WhatIsXplusY.Append(ch_Numbers);
Grammar g_WhatIsXplusY = new Grammar(gb_WhatIsXplusY);
recognizer.LoadGrammarAsync(g_StartStop);
recognizer.LoadGrammarAsync(g_WhatIsXplusY);
recognizer.RecognizeAsync(RecognizeMode.Multiple);  // 啟動語音辨識

while (done == false) { ; }
Console.WriteLine("\nHit <enter> to close shell\n");
Console.ReadLine();
*/


