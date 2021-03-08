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

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            using (WebClient webClient = new WebClient())
            // 從 url 讀取資訊至 stream
            using (Stream stream = webClient.OpenRead("http://jsonplaceholder.typicode.com/posts"))
            // 使用 StreamReader 讀取 stream 內的字元
            using (StreamReader reader = new StreamReader(stream))
            {
                // 將 StreamReader 所讀到的字元轉為 string
                string request = reader.ReadToEnd();
                //request.Dump();

                richTextBox1.Text += request + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 建立 webclient
            using (WebClient webClient = new WebClient())
            {
                // 指定 WebClient 的編碼
                webClient.Encoding = Encoding.UTF8;
                // 指定 WebClient 的 Content-Type header
                webClient.Headers.Add(HttpRequestHeader.ContentType, "application/json");
                // 從網路 url 上取得資料
                var body = webClient.DownloadString("http://jsonplaceholder.typicode.com/posts");
                //body.Dump();
            }
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
            string s = reader.ReadToEnd();
            //Console.WriteLine(s);
            richTextBox1.Text += s + "\n";
            data.Close();
            reader.Close();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            string remoteUri = "http://www.kindomhill.com.tw/images/";
            string fileName = "sec2-pic-06.jpg", myStringWebResource = null;
            // Create a new WebClient instance.
            WebClient myWebClient = new WebClient();
            // Concatenate the domain with the Web resource filename.
            myStringWebResource = remoteUri + fileName;
            Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, myStringWebResource);
            // Download the Web resource and save it into the current filesystem folder.
            myWebClient.DownloadFile(myStringWebResource, fileName);
            Console.WriteLine("Successfully Downloaded File \"{0}\" from \"{1}\"", fileName, myStringWebResource);
            Console.WriteLine("\nDownloaded file saved in the following file system folder:\n\t" + Application.StartupPath);

        }

        private void button6_Click(object sender, EventArgs e)
        {

            //string remoteUri = "https://www.google.com.tw/";
            string remoteUri = "http://antwrp.gsfc.nasa.gov/apod/";

            // Create a new WebClient instance.
            WebClient myWebClient = new WebClient();
            // Download home page data.
            Console.WriteLine("Downloading " + remoteUri);
            // Download the Web resource and save it into a data buffer.

            //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072; 

            byte[] myDataBuffer = myWebClient.DownloadData(remoteUri);

            // Display the downloaded data.
            string download = Encoding.ASCII.GetString(myDataBuffer);
            //Console.WriteLine(download);

            //Console.WriteLine("Download successful.");

            richTextBox1.Text += download + "\n";


        }


    }
}
