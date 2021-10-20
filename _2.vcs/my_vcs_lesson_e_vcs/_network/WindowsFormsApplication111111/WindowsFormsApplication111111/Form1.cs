using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;	    //for HttpWebRequest和HttpWebResponse
using System.IO;

using System.Threading; //for ThreadPool

namespace WindowsFormsApplication111111
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

        private void button4_Click(object sender, EventArgs e)
        {

            webBrowser1.Navigate("https://dotblogs.com.tw/joysdw12/2013/10/17/winform-webbrowser-html-operate");

        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            if (webBrowser1.ReadyState == WebBrowserReadyState.Complete)
            {
                ThreadPool.QueueUserWorkItem(o =>
                {
                    FormWork();
                });
            }

        }

        private void FormWork()
        {
            // 進行操作
            richTextBox1.Text += "get : " + webBrowser1.Document.GetElementById("name") + "\n";
        }
    }
}

