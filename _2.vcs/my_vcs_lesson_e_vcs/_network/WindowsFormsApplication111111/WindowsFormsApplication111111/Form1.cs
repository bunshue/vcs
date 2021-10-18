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

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            */

            //建立 WebRequest 並指定目標的 uri
            WebRequest request = WebRequest.Create("http://jsonplaceholder.typicode.com/posts");
            // 使用 HttpWebRequest.Create 實際上也是呼叫 WebRequest.Create
            //WebRequest request = HttpWebRequest.Create("http://jsonplaceholder.typicode.com/posts");
            //指定 request 使用的 http verb
            request.Method = "GET";
            //使用 GetResponse 方法將 request 送出，如果不是用 using 包覆，請記得手動 close WebResponse 物件，避免連線持續被佔用而無法送出新的 request
            using (var httpResponse = (HttpWebResponse)request.GetResponse())
            //使用 GetResponseStream 方法從 server 回應中取得資料，stream 必需被關閉
            //使用 stream.close 就可以直接關閉 WebResponse 及 stream，但同時使用 using 或是關閉兩者並不會造成錯誤，養成習慣遇到其他情境時就比較不會出錯
            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                var result = streamReader.ReadToEnd();

                richTextBox1.Text += result + "\n";
                //result.Dump();
            }

        }

        //根據Url位址得到網頁的html源碼
        private string GetWebContent(string Url)
        {
            string strResult = "";
            try
            {
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(Url);
                //聲明一個HttpWebRequest請求
                request.Timeout = 30000;
                //設置連接逾時時間
                request.Headers.Set("Pragma", "no-cache");
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("GB2312");
                StreamReader streamReader = new StreamReader(streamReceive, encoding);
                strResult = streamReader.ReadToEnd();
            }
            catch
            {
                MessageBox.Show("出錯"); //HTTP://ike.126.com
            }
            return strResult;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //要抓取的URL位址
            //string Url = "HTTP://list.mp3.baidu.com/topso/mp3topsong.html?id=1#top2";
            string Url = "http://jsonplaceholder.typicode.com/posts";


            //得到指定Url的源碼


            string strWebContent = GetWebContent(Url);


            richTextBox1.Text += strWebContent + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string Url = "http://www.google.com/webhp?hl=zh-TW";
            HttpWebRequest req = (HttpWebRequest)HttpWebRequest.Create(Url);
            req.Method = "GET";
            using (WebResponse wr = req.GetResponse())
            {
                //在這裡對接收到的頁面內容進行處理
                //richTextBox1.Text += wr + "\n";
                Stream streamReceive = wr.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("Big5");
                StreamReader streamReader = new StreamReader(streamReceive, encoding);
                string strResult = streamReader.ReadToEnd();

                richTextBox1.Text += strResult + "\n";



            }

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

