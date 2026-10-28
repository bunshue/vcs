using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_BeginInvoke
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
            richTextBox1.Clear();
            richTextBox1.AppendText("主執行緒：已點擊按鈕，準備啟動背景執行緒...\r\n\r\n");

            // 1. 建立一個全新的背景執行緒 (模擬 Whisper 在背景辨識)
            Thread backgroundThread = new Thread(new ThreadStart(MockBackgroundWork));

            // 2. 啟動背景執行緒
            backgroundThread.Start();
        }

        // 這是「背景執行緒」在跑的程式碼 (影印室後台)
        private void MockBackgroundWork()
        {
            // 注意：這裡面絕對「不能」直接寫 richTextBox1.Text = "xxx"; 否則會當機！

            for (int i = 1; i <= 5; i++)
            {
                // 模擬耗時運算（例如 Whisper 正在辨識第 i 段音訊），每秒辨識出一個詞
                Thread.Sleep(1000);

                string resultText = string.Format("【背景回傳】成功辨識出第 {0} 句文字", i);

                // 關鍵具體作法：利用 BeginInvoke 傳送便條紙回主執行緒
                this.BeginInvoke((MethodInvoker)delegate
                {
                    // 這裡面的程式碼會被轉交給「主執行緒」安全執行
                    richTextBox1.AppendText(resultText + "\r\n");
                });
            }

            // 結束時再傳一張便條紙通知 UI
            this.BeginInvoke((MethodInvoker)delegate
            {
                richTextBox1.AppendText("\r\n主執行緒收到通知：背景工作已全部結束！\r\n");
            });

        }
    }
}
