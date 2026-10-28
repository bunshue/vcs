using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_Whisper
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
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox1.Right + 10, richTextBox1.Bottom + 10);
            this.Text = "vcs_Whisper";

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
            //語音辨識0

            richTextBox1.Clear();
            richTextBox1.AppendText("開始進行語音辨識，請稍候...\r\n");

            // 1. 設定你解壓縮後的 whisper-cli.exe 路徑
            //string whisperCliPath = @"C:\App\whisper.cpp-bin\whisper-cli.exe";
            string whisperCliPath = @"D:\_git\vcs\_vcs_new_test1\whisper-bin-x64\Release\whisper-cli.exe";

            // 2. 設定你的模型檔 (.bin) 與要辨識的 WAV 檔路徑
            string modelPath = @"D:\_git\vcs\_big_files\ggml-base.bin";
            string wavFilePath = @"C:\App\whisper.cpp-bin\input_16khz.wav";
            wavFilePath = @"D:\_git\vcs\_4.python\audio_video\老北京22222.wav";

            // 3. 組合指令參數
            string arguments = string.Format("-m \"{0}\" -f \"{1}\" -l zh", modelPath, wavFilePath);

            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = whisperCliPath;
            startInfo.Arguments = arguments;
            startInfo.UseShellExecute = false;
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardError = true;
            startInfo.CreateNoWindow = true;
            startInfo.StandardOutputEncoding = Encoding.UTF8;
            startInfo.StandardErrorEncoding = Encoding.UTF8;

            Process process = new Process();
            process.StartInfo = startInfo;

            // 處理標準文字輸出 (辨識出的歌詞/對話)
            process.OutputDataReceived += delegate(object snd, DataReceivedEventArgs args)
            {
                if (args.Data != null && !string.IsNullOrEmpty(args.Data))
                {
                    // 關鍵：使用 MethodInvoker 跨執行緒安全更新 UI
                    this.BeginInvoke((MethodInvoker)delegate
                    {
                        richTextBox1.AppendText(args.Data + "\r\n");
                    });
                }
            };

            // 處理系統日誌輸出 (可選，如果要看進度可以加)
            process.ErrorDataReceived += delegate(object snd, DataReceivedEventArgs args)
            {
                if (args.Data != null && !string.IsNullOrEmpty(args.Data))
                {
                    this.BeginInvoke((MethodInvoker)delegate
                    {
                        // 這裡為了不干擾主要辨識文字，您可以選擇印到偵錯視窗，或寫到另一個 textBox
                        System.Diagnostics.Debug.WriteLine("[系統資訊] " + args.Data);
                    });
                }
            };

            // 處理程式執行完畢後的動作
            process.EnableRaisingEvents = true;
            process.Exited += delegate(object snd, EventArgs args)
            {
                this.BeginInvoke((MethodInvoker)delegate
                {
                    richTextBox1.AppendText("\r\n--- 辨識結束 ---\r\n");
                    process.Dispose();
                });
            };

            // 啟動程序與異步讀取
            process.Start();
            process.BeginOutputReadLine();
            process.BeginErrorReadLine();
        }

        //------------------------------------------------------------  # 60個

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

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

