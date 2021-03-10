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
            DateTime d1 = new DateTime(2021, 3, 8);
            DateTime d2 = DateTime.Now;
            TimeSpan ts = new TimeSpan(d1.Ticks - d2.Ticks);

            richTextBox1.Text += "兩時間相距 : " + ts.TotalMilliseconds.ToString() + "\n";
            richTextBox1.Text += "兩時間相距 : " + ts.TotalHours.ToString() + "\n";




        }

        private void button2_Click(object sender, EventArgs e)
        {
            string url = "http://jsonplaceholder.typicode.com/posts";

            WebClient client = new WebClient();
            // 從 url 讀取資訊至 stream
            using (Stream stream = client.OpenRead(url))
            {
                // 使用 StreamReader 讀取 stream 內的字元
                using (StreamReader sr = new StreamReader(stream))
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
            // 指定 WebClient 的編碼
            client.Encoding = Encoding.UTF8;
            // 指定 WebClient 的 Content-Type header
            client.Headers.Add(HttpRequestHeader.ContentType, "application/json");
            // 從網路 url 上取得資料
            var result = client.DownloadString(url);
            richTextBox1.Text += result + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string url = "http://jsonplaceholder.typicode.com/posts";

            WebClient client = new WebClient();

            // Add a user agent header in case the
            // requested URI contains a query.

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
            string url = "http://www.kindomhill.com.tw/images/";
            string filename = "sec2-pic-06.jpg";
            string myStringWebResource = null;

            WebClient client = new WebClient();     // Create a new WebClient instance.
            // Concatenate the domain with the Web resource filename.
            myStringWebResource = url + filename;
            Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", filename, myStringWebResource);
            // Download the Web resource and save it into the current filesystem folder.
            client.DownloadFile(myStringWebResource, filename);
            Console.WriteLine("Successfully Downloaded File \"{0}\" from \"{1}\"", filename, myStringWebResource);
            Console.WriteLine("\nDownloaded file saved in the following file system folder:\n\t" + Application.StartupPath);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //string url = "https://www.google.com.tw/";
            string url = "http://antwrp.gsfc.nasa.gov/apod/";

            WebClient client = new WebClient();     // Create a new WebClient instance.
            // Download home page data.
            Console.WriteLine("Downloading " + url);
            // Download the Web resource and save it into a data buffer.

            //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            byte[] myDataBuffer = client.DownloadData(url);

            // Display the downloaded data.
            string result = Encoding.ASCII.GetString(myDataBuffer);
            //Console.WriteLine(download);

            //Console.WriteLine("Download successful.");

            richTextBox1.Text += result + "\n";
        }
    }
}
