using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for WebRequest
using System.IO;    //for Stream

namespace vcs_GetWebPageData1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //使用 WebBrowser 取得網頁原始碼
            string txtUrl = @"https://www.google.com.tw/";  //預設網址
            //string txtUrl = @"C:/My_Link.html";

            this.webBrowser1.Navigate(txtUrl);  // WebBrowser1 網頁載入

            // 使用 WebBrowser.DocumentStream 取得網頁內容
            // 使用 StreamReader 讀入資料流，設定編碼為 Encoding.Default
            //System.IO.StreamReader getReader = new System.IO.StreamReader(this.webBrowser1.DocumentStream, System.Text.Encoding.Default);
            //string gethtml = getReader.ReadToEnd();	//讀取所有文字內容
            string htmlB = webBrowser1.DocumentText;
            this.richTextBox1.Text += htmlB;
        }

        public static string myUrl = "https://www.google.com.tw/";    //要抓取的網頁
        private void button2_Click(object sender, EventArgs e)
        {
            //讀取網頁的內容
            string data = getContent(myUrl);
            richTextBox1.Text += "data:" + data + "\n";
        }
        private string getContent(string Url)
        {
            string strResult = "";
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(Url);
            //聲明一個HttpWebRequest請求
            request.Timeout = 30000;
            //設置連接逾時時間
            request.Headers.Set("Pragma", "no-cache");
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Stream streamReceive = response.GetResponseStream();
            Encoding encoding = Encoding.GetEncoding("BIG5");
            StreamReader streamReader = new StreamReader(streamReceive, encoding);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            strResult = streamReader.ReadToEnd();	//讀取所有文字內容
            streamReader.Close();
            return strResult;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //C#,從網頁上下載檔案範例
            string url = "http://blog.darkthread.net/images/darkthreadbanner.gif";
            HttpWebRequest httpRequest = (HttpWebRequest)WebRequest.Create(url);
            HttpWebResponse httpResponse = (HttpWebResponse)httpRequest.GetResponse();

            System.IO.Stream dataStream = httpResponse.GetResponseStream();
            byte[] buffer = new byte[8192];

            FileStream fs = new FileStream("C:\\______test_files\\aaaaaaaa.gif", FileMode.Create, FileAccess.Write);
            int size = 0;
            do
            {
                size = dataStream.Read(buffer, 0, buffer.Length);
                if (size > 0)
                    fs.Write(buffer, 0, size);
            } while (size > 0);
            fs.Close();
            httpResponse.Close();

            richTextBox1.Text += "Done at " + DateTime.Now.ToString("HH:mm:ss.fff") + "\n";
        }

    }
}
