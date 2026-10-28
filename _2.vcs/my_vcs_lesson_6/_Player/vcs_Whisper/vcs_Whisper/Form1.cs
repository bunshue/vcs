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

            // 3. 組合指令參數 (-m 指定模型, -f 指定音訊檔, -l 指定語言)
            // 中文請帶入 -l zh，如果是自動偵測可以不加 -l，但指定常能提高準確度
            //string arguments = string.Format("-m \"{0}\" -f \"{1}\" -l zh", modelPath, wavFilePath);
            // 3. 組合指令參數（新增 --prompt 參數強制引導輸出繁體）
            //string arguments = string.Format("-m \"{0}\" -f \"{1}\" -l zh --prompt \"以下是普通話的句子。\"", modelPath, wavFilePath);
            // --prompt 參數的作用是給 Whisper 一個「前情提要」。
            // 當它看到提示句是用繁體的「話」與「句」時，它在接下來的生成過程中，就會全面傾向使用繁體字集的編碼來輸出文字。
            // 加上 -nt 參數，告訴 whisper-cli 不要輸出時間戳記
            // string arguments = string.Format("-m \"{0}\" -f \"{1}\" -l zh -nt --prompt \"以下是普通話的句子。\"", modelPath, wavFilePath);

            // 建立一個長度足夠、帶有完整繁體標點符號的提示句
            string longPrompt = "以下是普通話的對話錄音。請將語音精確地轉錄為正體中文，並適當地加上逗號、句號與驚嘆號，使其成為一篇通順的文章。";
            // 組合指令參數
            string arguments = string.Format("-m \"{0}\" -f \"{1}\" -l zh -nt --prompt \"{2}\"", modelPath, wavFilePath, longPrompt);

            ProcessStartInfo startInfo = new ProcessStartInfo
            {
                FileName = whisperCliPath,
                Arguments = arguments,
                UseShellExecute = false,        // 必須為 false 才能重導向輸出
                RedirectStandardOutput = true,  // 抓取標準輸出文字
                RedirectStandardError = true,   // whisper 的進度與資訊常在標準錯誤中
                CreateNoWindow = true,          // 隱藏黑視窗
                StandardOutputEncoding = Encoding.UTF8, // 確保中文不亂碼
                StandardErrorEncoding = Encoding.UTF8
            };

            Process process = new Process();
            process.StartInfo = startInfo;

            // 處理標準文字輸出 (辨識出的歌詞/對話) (C# 4.0 支援匿名方法與事件綁定)
            process.OutputDataReceived += delegate(object snd, DataReceivedEventArgs args)
            {
                if (args.Data != null && !string.IsNullOrEmpty(args.Data))
                {
                    // 關鍵：使用 MethodInvoker 跨執行緒安全更新 UI
                    this.BeginInvoke((MethodInvoker)delegate
                    {
                        // 這裡會即時印出帶有時間戳記的文字
                        richTextBox1.AppendText(args.Data + "\r\n");
                    });
                }
            };

            // 用來接收底層的核心日誌（如初始化、硬體加速資訊、辨識進度）
            // 處理系統日誌輸出 (可選，如果要看進度可以加)
            //這裡改用 C# 2.0/4.0 穩定的 delegate(object sender, DataReceivedEventArgs e) 匿名方法來接收事件。
            process.ErrorDataReceived += delegate(object snd, DataReceivedEventArgs args)
            {
                // 如果不想看細節日誌，可以把下面這行註解掉
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

            // 啟動程序
            process.Start();

            // 開始異步讀取
            process.BeginOutputReadLine();
            process.BeginErrorReadLine();

            // 等待程式執行完畢, 一次做完
            // 一次做完 process.WaitForExit();
            //process.WaitForExit() 鎖死主執行緒
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



/*
請前往 GitHub whisper.cpp Releases 頁面。

https://docs.profuzdigital.com/books/subtitlenext-how-tos/page/whispercpp-installation-guide

在最新的發布版本 (Latest release) 的 Assets 區塊中，尋找適用於 Windows 64 位元的壓縮檔
（通常檔名類似 whisper-bin-x64.zip 或 whisper-blas-bin-x64.zip）

• 下載完成後，將 ZIP 壓縮檔解壓至你指定的資料夾（例如 C:\App\whisper.cpp-bin 或 C:\Program Files\whisper.cpp\）。
4. 下載語音模型：
• whisper.cpp 需要搭配 GGML 格式的語音模型檔案（可至 Hugging Face 的 ggerganov/whisper.cpp 頁面下載）。

Hugging Face

步驟 4：準備符合規格的 WAV 檔與語音模型
whisper.cpp 對輸入的音訊格式要求非常嚴格：
1. WAV 檔案格式：必須是 16-bit 轉量化、16000Hz (16kHz) 採樣率、單聲道 (Mono)。如果是從手機錄音或一般音樂檔（通常是 44.1kHz 或 48kHz），請先找工具轉檔，否則 whisper 會報錯。
2. 語音模型：請到 Hugging Face ggerganov/whisper.cpp 下載 ggml-base.bin 或 ggml-small.bin 檔案，放至你的資料夾中。


要取得正確的 ggml-base.bin 模型檔，請按照以下簡單步驟操作：

步驟：單獨下載模型檔

1. 打開瀏覽器，前往官方推薦存放模型的 Hugging Face whisper.cpp 頁面。
https://huggingface.co/ggerganov/whisper.cpp/tree/main

https://github.com/ggml-org/whisper.cpp/releases

2. 在檔案清單中，尋找名稱為 ggml-base.bin 的檔案（注意：不要選到帶有 .en 的，那是英文專用模型）。

• ggml-base.dll (你看到的)：這是程式運算晶片與記憶體底層架構的核心程式碼（Dynamic Link Library），是給 Windows 系統執行的。
• ggml-base.bin (你需要去下載的)：這是 OpenAI 訓練出來的「語音資料大腦」（Model Weights），是給 whisper-cli.exe 讀取並對照音訊使用的。


ggml-base.bin	140MB
ggml-small.bin（約 460MB）
ggml-medium.bin（約 1.5GB）

*/



        
