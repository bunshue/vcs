using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for StreamReader
using System.Net;
using System.Net.Security;
using System.Security.Cryptography.X509Certificates;
using System.Runtime.InteropServices;

namespace 真的只是一個測試2_Net
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
        }

        static void download()
        {


            string url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Breathe-face-smile.svg/1200px-Breathe-face-smile.svg.png";

            using (WebClient client = new WebClient())
            {
                client.DownloadFile(new Uri(url), "Image.png");
            }
        }


        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                download();
            }
            catch (ExternalException ex)
            {
                Console.WriteLine(ex.Message);

            }
            catch (ArgumentNullException ex)
            {
                Console.WriteLine(ex.Message);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {

            //在 C# 中使用 DownloadFile() 方法從一個 URL 下載檔案
            WebClient mywebClient = new WebClient();
            mywebClient.DownloadFile("https://wiki.linuxfoundation.org/_media/wiki/logo.png", @"C:\dddddddddd\aaaaa.png");


        }

        private void button3_Click(object sender, EventArgs e)
        {
            //語法01
            //資料來源:https://shunnien.github.io/2017/07/13/Accessing-HTTPS-URL-using-csharp/
            var url = "https://www.moi.gov.tw/";//台灣內政部網址
            string results;
            // 強制認為憑證都是通過的，特殊情況再使用
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.AutomaticDecompression = DecompressionMethods.GZip;
            // 加入憑證驗證
            //request.ClientCertificates.Add(new System.Security.Cryptography.X509Certificates.X509Certificate());
            HttpWebResponse resp = (HttpWebResponse)request.GetResponse();
            using (StreamReader sr = new StreamReader(resp.GetResponseStream()))
            {
                results = sr.ReadToEnd();
                sr.Close();
            }
            //Console.WriteLine(results);
            richTextBox1.Text += results;

            richTextBox1.Text += "\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //語法02
            getUrlResponse("https://www.moi.gov.tw/");



        }

        private void button5_Click(object sender, EventArgs e)
        {
            //語法3
            string url1 = "https://www.moi.gov.tw/";
            string result = PostUrl(url1, "key=123");
            Console.WriteLine(result);

        }

        static private bool CheckValidationResult(object sender, X509Certificate certificate, X509Chain chain, SslPolicyErrors errors)
        {
            return true;// Always accept
        }

        static private HttpWebResponse getUrlResponse(string url)
        {
            HttpWebResponse resp = null;
            HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);

            if (url.StartsWith("https", StringComparison.OrdinalIgnoreCase))
            {
                ServicePointManager.ServerCertificateValidationCallback =
                        new RemoteCertificateValidationCallback(CheckValidationResult);
            }

            //...
            resp = (HttpWebResponse)req.GetResponse();
            using (StreamReader sr = new StreamReader(resp.GetResponseStream()))
            {
                String results = sr.ReadToEnd();
                Console.WriteLine(results);
                sr.Close();
            }

            //...
            return resp;
        }

        private static string PostUrl(string url, string postData)
        {
            HttpWebRequest request = null;
            if (url.StartsWith("https", StringComparison.OrdinalIgnoreCase))
            {
                request = WebRequest.Create(url) as HttpWebRequest;
                ServicePointManager.ServerCertificateValidationCallback = new RemoteCertificateValidationCallback(CheckValidationResult);
                request.ProtocolVersion = HttpVersion.Version11;
                // 這裡設置了協議類型。

                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;// SecurityProtocolType.Tls1.2; 
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls;

                request.KeepAlive = false;
                ServicePointManager.CheckCertificateRevocationList = true;
                ServicePointManager.DefaultConnectionLimit = 100;
                ServicePointManager.Expect100Continue = false;
            }
            else
            {
                request = (HttpWebRequest)WebRequest.Create(url);
            }

            request.Method = "POST";//使用get方式發送數據
            request.ContentType = null;
            request.Referer = null;
            request.AllowAutoRedirect = true;
            request.UserAgent = "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727)";
            request.Accept = "*/*";

            byte[] data = Encoding.UTF8.GetBytes(postData);
            Stream newStream = request.GetRequestStream();
            newStream.Write(data, 0, data.Length);
            newStream.Close();

            //獲取網頁響應結果
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();
            Stream stream = response.GetResponseStream();
            //client.Headers.Add("Content-Type", "application/x-www-form-urlencoded");
            string result = string.Empty;
            using (StreamReader sr = new StreamReader(stream))
            {
                result = sr.ReadToEnd();
            }

            return result;
        }


    }

    /*
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }
    */

}

