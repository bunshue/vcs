using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;   //for DNS, WebRequest, IPAddress
using System.Net.Sockets;   // for AddressFamily
using System.Collections;   //for IEnumerator
using System.Runtime.InteropServices;   //for DllImport
using System.IO;    //for Stream
using System.Threading;
using System.Net.NetworkInformation;    //for UnicastIPAddressInformation

namespace vcs_Network1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //連線到Google，使用預設的browser
            System.Diagnostics.Process.Start("http://www.google.com/");

        }

        private void button3_Click(object sender, EventArgs e)
        {            
            //連線到Google，使用IE
            System.Diagnostics.Process.Start("IExplore.exe", "http://www.google.com");

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //開啟網頁
            System.Diagnostics.Process.Start("https://www.google.com.tw/?gws_rd=ssl");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得本機電腦的主機名稱
            string strHostName = Dns.GetHostName(); //取得本機的 IpHostEntry 類別實體
            richTextBox1.Text += "主機名稱 ：" + strHostName + "\n";

            //取得所有 IP 位址
            richTextBox1.Text += "取得所有 IP 位址 1\n";
            IPAddress[] IPS = Dns.GetHostEntry(strHostName).AddressList;
            IEnumerator iEnums = IPS.GetEnumerator();
            while (iEnums.MoveNext())
            {
                richTextBox1.Text += "IP : " + iEnums.Current.ToString() + "\n";
            }

            richTextBox1.Text += "\n" + "取得所有 IP 位址 2\n";
            // 取得本機的IpHostEntry類別實體，MSDN建議新的用法
            IPHostEntry iphostentry = Dns.GetHostEntry(strHostName);

            // 取得所有 IP 位址
            foreach (IPAddress ipaddress in iphostentry.AddressList)
            {
                // 只取得IP V4的Address
                if (ipaddress.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork)
                {
                    richTextBox1.Text += "Local IP: " + ipaddress.ToString() + "\n";
                }
            }

        }

        //網路連線狀態
        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);
        //參數說明 constate 連接說明 ，reder保留值
        public bool IsConnectedToInternet()
        {
            int Desc = 0;
            return InternetGetConnectedState(out  Desc, 0);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //網路連線狀態
            if (IsConnectedToInternet())
            {
                richTextBox1.Text += "已連接在網上!\n";
            }
            else
            {
                richTextBox1.Text += "未連接在網上!!\n";
            }
        }

        string pic1 = "http://www.myson.com.tw/images/index/ad01.jpg";
        string pic2 = "http://www.myson.com.tw/images/index/ad02.jpg";
        string pic3 = "http://www.myson.com.tw/images/index/ad03.jpg";
        string pic4 = "http://www.myson.com.tw/images/index/ad04.jpg";
        int select = 1;

        private void button7_Click(object sender, EventArgs e)
        {
            //取得網路上的圖片並顯示
            //法一
            //this.pictureBox1.Image = ReadImageFromUrl(pic1);
            //法二
            switch (select)
            { 
                case 1:
                    pictureBox1.ImageLocation = pic1;   break;
                case 2:
                    pictureBox1.ImageLocation = pic2;   break;
                case 3:
                    pictureBox1.ImageLocation = pic3;   break;
                case 4:
                    pictureBox1.ImageLocation = pic4;   break;
                default:
                    pictureBox1.ImageLocation = pic1;   break;
            }
            select++;
            if (select > 4)
                select = 1;
        }
        private Image ReadImageFromUrl(string urlImagePath)
        {
            Uri uri = new Uri(urlImagePath);
            WebRequest webRequest = WebRequest.Create(uri);
            Stream stream = webRequest.GetResponse().GetResponseStream();
            Image res = Image.FromStream(stream);
            return res;

        }

        private void button8_Click(object sender, EventArgs e)
        {
            Uri urlCheck = new Uri("http://tw.yahoo.com");
            System.Net.WebRequest request = System.Net.WebRequest.Create(urlCheck);
            System.Net.WebResponse response;
            try
            {
                response = request.GetResponse();
                //Response.Write("OK");
                richTextBox1.Text += "網頁存在\n";
            }
            catch (Exception)
            {
                //Response.Write("Error");
                richTextBox1.Text += "網頁不存在\n";
            }

        }

        private void button9_Click(object sender, EventArgs e)
        {
            try
            {
                //下載純文字
                WebClient wc = new WebClient();
                string somestring = wc.DownloadString("http://snowball.tartarus.org/otherlangs/english_cpp.txt");
                richTextBox1.Text += somestring;
            }
            catch (WebException we)
            {
                // add some kind of error processing
                richTextBox1.Text += we.ToString() + "n";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //[c#] 取得src內的網址
            string s = "<img src=\"http://www.yahoo.com.tw/1.gif\"/>";
            System.Text.RegularExpressions.Match m = System.Text.RegularExpressions.Regex.Match(s, "\"(.*?)\"");
            string res = m.Groups[1].Value;
            richTextBox1.Text += res;

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //C# 可以實作 ping 網路連線檢查
            //INIT PING OBJECT
            System.Net.NetworkInformation.Ping objPing = new System.Net.NetworkInformation.Ping();

            //設定測試連線及逾時時間
            System.Net.NetworkInformation.PingReply PingResult = objPing.Send("www.google.com.tw", 5000);

            //取得結果
            string pingMsg = (PingResult.Status == System.Net.NetworkInformation.IPStatus.Success) ? "連線成功" : "無法連線";

            richTextBox1.Text += pingMsg + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            IPAddress ip = GetIP();
            if (ip != null)
            {
                richTextBox1.Text += "IP : " + ip.ToString() + "\n";
            }

        }

        IPAddress GetIP()
        {
            foreach (IPAddress ip in Dns.GetHostEntry(Dns.GetHostName()).AddressList)
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                    return ip;
            return null;
        }


        public class MyWebClient : WebClient
        {
            protected override WebRequest GetWebRequest(Uri uri)
            {
                WebRequest WR = base.GetWebRequest(uri);
                WR.Timeout = 30 * 1000;     //30秒
                return WR;
            }
        }

        ////.Net C# 讓 WebClient 擁有 Timeout 功能
        private void button24_Click(object sender, EventArgs e)
        {
            MyWebClient MWC = new MyWebClient();
            string HTML = MWC.DownloadString("http://www.google.com.tw/");
            richTextBox1.Text += HTML;
            //Console.WriteLine(HTML);


        }

        private void button13_Click(object sender, EventArgs e)
        {
            //C# 網路連線檢查
            //C# 可以實作 ping 網路連線檢查
            //INIT PING OBJECT
            System.Net.NetworkInformation.Ping objPing = new System.Net.NetworkInformation.Ping();

            try
            {
                //設定測試連線及逾時時間
                System.Net.NetworkInformation.PingReply PingResult = objPing.Send("www.google.com.tw", 5000);

                //取得結果
                string pingMsg = (PingResult.Status == System.Net.NetworkInformation.IPStatus.Success) ? "連線成功" : "無法連線";

                richTextBox1.Text += pingMsg + "\n";

            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }

        private WebClient client = new WebClient();
        private void button14_Click(object sender, EventArgs e)
        {
            Thread th = new Thread(new ThreadStart(StartDownload));
            th.Start();
        }

        private void StartDownload()
        {
            string URL = "http://weisico.com/program/2015/0630/237.html";
            int n = URL.LastIndexOf("/");
            string URLAddress = URL;//.Substring(0, n);
            string fileName = URL.Substring(n + 1, URL.Length - n - 1);
            string Dir = @"C:\______test_files\";
            //下载文件，直接覆盖
            string Path = Dir + fileName;

            //Datetime.Now.ToFileTime.ToString()用于区别下载时间
            // string Path = Dir +DateTime.Now.ToFileTime().ToString() + fileName  ;

            try
            {
                WebRequest myre = WebRequest.Create(URLAddress);

                Stream stream = client.OpenRead(URLAddress);
                StreamReader reader = new StreamReader(stream);

                FileStream outputStream = new FileStream(Path, FileMode.OpenOrCreate);
                try
                {
                    int bufferSize = 100; // 网络速度快的话可以设置大一点，慢的话可以小一点
                    int nRealCount;
                    byte[] bBuffer = new byte[bufferSize];
                    nRealCount = stream.Read(bBuffer, 0, bufferSize);

                    // 下载，一面读一面下载是最好的方式。这样就不用声明多大的数组了
                    while (nRealCount > 0)
                    {
                        outputStream.Write(bBuffer, 0, nRealCount);
                        nRealCount = stream.Read(bBuffer, 0, bBuffer.Length);
                    }
                    MessageBox.Show("下载完毕!");
                }
                catch (WebException exp)
                {
                    MessageBox.Show(exp.Message, "Error");
                    this.Text = "";
                }
                finally
                {
                    stream.Close();
                    reader.Close();
                    outputStream.Close();
                }

                //Application.Exit();

            }
            catch (Exception exp)
            {
                MessageBox.Show(exp.Message);
                //MessageBox.Show("请输入正确的文件地址");
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            string strURL = "http://google.com.tw";
            //string strURL = "http://www.yahoo.com.tw";
            string web_data = GetWebPage(strURL);
            if (web_data == "fail")
                richTextBox1.Text += "抓取網頁失敗";
            else
                richTextBox1.Text += "抓取網頁成功";
        }

        public String GetWebPage(String sURL)
        {
            try
            {
                WebClient wc = new WebClient();
                wc.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");
                byte[] bd = wc.DownloadData(sURL);
                return (Encoding.Default.GetString(bd));
            }
            catch
            {
                return ("fail");
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            HttpWebRequest httpRequest = null;
            HttpWebResponse httpResponse;

            string result = "";
            String txtURL = "https://www.google.com.tw/";
            char[] cbuffer = new char[256];
            int byteRead = 0;
            try
            {

                Uri httpURL = new Uri(txtURL);
                httpRequest = (HttpWebRequest)WebRequest.Create(httpURL);
                httpResponse = (HttpWebResponse)httpRequest.GetResponse();
                System.IO.Stream respStream = httpResponse.GetResponseStream();
                System.IO.StreamReader respStreamReader = new StreamReader(respStream);
                byteRead = respStreamReader.Read(cbuffer, 0, 256);
                while (byteRead != 0)
                {
                    string response = new string(cbuffer, 0, byteRead);
                    result = result + response;
                    byteRead = respStreamReader.Read(cbuffer, 0, 256);
                    richTextBox1.Text += response + "\n";
                }
            }
            catch (Exception)
            {

            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //下載檔案的範例 - 使用WebClient
            WebClient wc = new WebClient();
            wc.DownloadFile("http://s.pimg.tw/qrcode/charleslin74/blog.png", "C:\\______test_files\\blog.png");
            richTextBox1.Text += "下載完成\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //取得網卡的IPV6位置
            foreach (var ip in GetLocalIPV6IP())
            {
                richTextBox1.Text += "ip = " + ip.ToString() + "\n";
            }
        }

        private static IEnumerable<String> GetLocalIPV6IP()
        {
            return (from adapter in NetworkInterface.GetAllNetworkInterfaces()
                    where adapter.NetworkInterfaceType == NetworkInterfaceType.Ethernet
                    from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType<UnicastIPAddressInformation>()
                    where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6
                    let ipAddress = AddressInfo.Address.ToString()
                    select ipAddress);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //從FTP下載檔案
            System.Net.WebClient webClient = new System.Net.WebClient();
            //下載FTP檔案到指定位置
            webClient.DownloadFile("http://ftp.tku.edu.tw/Linux/Fedora/releases/27/Everything/x86_64/iso/Fedora-Everything-netinst-x86_64-27-1.6.iso", @"C:\______test_files\fedora27.iso");

        }

        private void button23_Click(object sender, EventArgs e)
        {
            // Download and display the text file.
            richTextBox1.Clear();
            richTextBox1.Text += "取得網頁純文字檔...\n";

            const string url = "http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP950.TXT";
            richTextBox1.Text += GetTextFile(url);
            //richTextBox1.Select(0, 500);  //useless

        }

        // Get the text file at a given URL.
        private string GetTextFile(string url)
        {
            try
            {
                url = url.Trim();
                if (!url.ToLower().StartsWith("http")) url = "http://" + url;
                WebClient web_client = new WebClient();
                MemoryStream image_stream = new MemoryStream(web_client.DownloadData(url));
                StreamReader reader = new StreamReader(image_stream);
                string result = reader.ReadToEnd();
                reader.Close();
                return result;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error downloading file " +
                    url + '\n' + ex.Message,
                    "Download Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            }
            return "";
        }

        private void button29_Click(object sender, EventArgs e)
        {
            String host;

            host = "www.google.com";

            if (IsInternetConnected(host))
                richTextBox1.Text += host + "\t連線OK\n";
            else
                richTextBox1.Text += host + "\t無法連線\n";

            host = "http://csharphelper.com/";

            if (IsInternetConnected(host))
                richTextBox1.Text += host + "\t連線OK\n";
            else
                richTextBox1.Text += host + "\t無法連線\n";
        }

        // Return true if a ping to Google works.
        private bool IsInternetConnected(String host)
        {
            return IsInternetConnected(host, 1000);
        }
        private bool IsInternetConnected(String host, int timeout)
        {
            try
            {
                Ping ping = new Ping();
                PingReply reply = ping.Send(host, timeout);
                return (reply.Status == IPStatus.Success);
            }
            catch
            {
                return false;
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //取得網頁資料並存成檔案

            string url = "file:///C:/_git/vcs/_1.data/_html/My_Link.html";
            // Get the response.
            try
            {
                // Get the web response.
                string result = GetWebResponse(url);
                //Console.WriteLine(result.Replace("\\r\\n", "\r\n"));
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Read Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        // Get a web response.
        private string GetWebResponse(string url)
        {
            // Make a WebClient.
            WebClient web_client = new WebClient();

            // Get the indicated URL.
            Stream response = web_client.OpenRead(url);

            // Read the result.
            using (StreamReader stream_reader = new StreamReader(response))
            {
                // Get the results.
                string result = stream_reader.ReadToEnd();

                // Close the stream reader and its underlying stream.
                stream_reader.Close();

                // Return the result.

                richTextBox1.Text += result + "\n";

                string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";
                StreamWriter sw = File.CreateText(filename);
                sw.Write(result);
                sw.Close();

                return result;
            }
        }




    }
}
