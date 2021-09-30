using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser5
{
    public partial class Form1 : Form
    {
        int cnt = 0;
        bool finished = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            webBrowser1.ScriptErrorsSuppressed = true;  //關閉 指令碼偵錯視窗
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string url = "www.yahoo.com";

            richTextBox1.Text += "連線到 " + url + "\n";
            cnt = 0;
            finished = false;
            webBrowser1.Navigate(url);
        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            //只使用DocumentCompleted事件,結果會觸發事件多次

            cnt++;
            //richTextBox1.Text += "webBrowser1_DocumentCompleted " + cnt.ToString() + "\n";


            //這樣再也不會發生重複執行的狀況
            richTextBox1.Text += "讀取中..." + cnt.ToString() + "\n";
            if (webBrowser1.ReadyState < WebBrowserReadyState.Complete || finished == true)
            {
                richTextBox1.Text += "----\n";
                return;
            }
            finished = true;
            richTextBox1.Text += "讀取完成\n";
        }

    }
}

