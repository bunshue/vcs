using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;   //for TcpClient

using System.IO;

namespace WindowsFormsApplication1ttttt
{
    public partial class Form1 : Form
    {
        TcpClient tcpClient;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime d1 = new DateTime(2006, 3, 11, 9, 15, 15);
            DateTime d2 = DateTime.Now;
            TimeSpan ts = new TimeSpan(d2.Ticks - d1.Ticks);

            richTextBox1.Text += "兩時間相距 : " + ts.TotalMilliseconds.ToString() + "\n";
            richTextBox1.Text += "兩時間相距 : " + ts.TotalHours.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string url = "http://jsonplaceholder.typicode.com/posts";

            WebClient client = new WebClient();     // 建立 webclient

            using (Stream stream = client.OpenRead(url))        // 從 url 讀取資訊至 stream
            {
                using (StreamReader sr = new StreamReader(stream))      // 使用 StreamReader 讀取 stream 內的字元
                {
                    string result = sr.ReadToEnd();        // 將 StreamReader 所讀到的字元轉為 string
                    richTextBox1.Text += result + "\n";
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string url = "http://jsonplaceholder.typicode.com/posts";

            WebClient client = new WebClient();     // 建立 webclient
            client.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            client.Headers.Add(HttpRequestHeader.ContentType, "application/json");  // 指定 WebClient 的 Content-Type header

            // 從網路 url 上取得資料
            var result = client.DownloadString(url);
            richTextBox1.Text += result + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string url = "http://jsonplaceholder.typicode.com/posts";

            WebClient client = new WebClient();     // 建立 webclient
            // Add a user agent header in case the requested URI contains a query.
            client.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)");

            Stream data = client.OpenRead(url);
            StreamReader reader = new StreamReader(data);
            string result = reader.ReadToEnd();
            richTextBox1.Text += result + "\n";
            data.Close();
            reader.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //https://upload.wikimedia.org/wikipedia/commons/b/be/%E7%90%89%E7%90%83%E5%AE%AB%E5%BB%B7%E9%9F%B3%E4%B9%90.jpg
        //http://www.csharphelper.com/essential_algs_2e_251_317.jpg
            string url = "https://www.cwb.gov.tw/Data/satellite/";
            string filename = "LCC_IR1_CR_2750/LCC_IR1_CR_2750.jpg";
            string myStringWebResource = null;

            WebClient client = new WebClient();     // 建立 webclient

            //client.Encoding = Encoding.UTF8;        // 指定 WebClient 的編碼
            client.Headers.Add(HttpRequestHeader.ContentType, "application/json");  // 指定 WebClient 的 Content-Type header
            //client.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705;)");

            // Concatenate the domain with the Web resource filename.
            myStringWebResource = url + filename;
            richTextBox1.Text += "Downloading File " + filename + " from " + myStringWebResource + "\n";
            // Download the Web resource and save it into the current filesystem folder.
            try
            {
                client.DownloadFile(myStringWebResource, filename);
                richTextBox1.Text += "OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";

            }



        }

        private void button6_Click(object sender, EventArgs e)
        {
            //string url = "https://www.google.com.tw/";
            string url = "http://antwrp.gsfc.nasa.gov/apod/";
            WebClient client = new WebClient();     // 建立 webclient

            // Download home page data.
            richTextBox1.Text += "Downloading " + url + " ...\n";

            // Download the Web resource and save it into a data buffer.
            //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            byte[] myDataBuffer = client.DownloadData(url);

            // Display the downloaded data.
            string result = Encoding.ASCII.GetString(myDataBuffer);
            richTextBox1.Text += result + "\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
