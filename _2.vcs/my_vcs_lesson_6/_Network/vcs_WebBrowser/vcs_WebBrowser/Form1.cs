using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser
{
    public partial class Form1 : Form
    {
        //參考資料：http://abgne.tw/code-snippets/dotnet-webbrowser.html
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 預設載入的頁面
            //webBrowser1.Navigate("https://www.google.com.tw/");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 上一頁
            webBrowser1.GoBack();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 下一頁
            webBrowser1.GoForward();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 重新整理
            webBrowser1.Refresh();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 停止
            webBrowser1.Stop();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // 首頁
            webBrowser1.GoHome();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 前往網址輸入框中的網址
            webBrowser1.Navigate(textBox1.Text);
        }

        private void textBox1_KeyUp(object sender, KeyEventArgs e)
        {
            // 如果在網址輸入框中按下 Enter 則前往網址輸入框中的網址
            if (e.KeyCode == Keys.Enter)
            {
                webBrowser1.Navigate(textBox1.Text);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("http://www.yahoo.com.tw");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("https://www.google.com.tw/");
        }

        private void button9_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5");
        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            // 把目前的網址顯示在網址輸入框中
            textBox1.Text = webBrowser1.Url.ToString();
            this.Text = "傳送完成";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate("about:blank");
        }

    }
}
