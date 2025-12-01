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
using System.Net.NetworkInformation;    //for UnicastIPAddressInformation
using System.Collections;   //for IEnumerator
using System.Runtime.InteropServices;   //for DllImport
using System.IO;            //for Stream
using System.Diagnostics;   //for Process

using Microsoft.Win32;      //for RegistryKey

namespace vcs_Network1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "本機IP : " + MyIP() + "\n";

            //取得自己的 IP

            IPAddress ip = GetIP();
            if (ip != null)
            {
                richTextBox1.Text += "本機IP : " + ip.ToString() + "\n";
            }

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
                if (ipaddress.AddressFamily == AddressFamily.InterNetwork)
                {
                    richTextBox1.Text += "Local IP: " + ipaddress.ToString() + "\n";
                }
            }
        }

        //找出本機IP
        private string MyIP()
        {
            string ipv4_addr = "";
            string hn = Dns.GetHostName();                          //取得本機電腦名稱
            IPAddress[] ip = Dns.GetHostEntry(hn).AddressList;      //取得本機IP陣列(可能有多個)
            foreach (IPAddress it in ip)                            //列舉各個IP
            {
                richTextBox1.Text += it.ToString() + "\t" + it.AddressFamily + "\n";  //顯示所有IP
                if (it.AddressFamily == AddressFamily.InterNetwork) //如果是IPv4格式
                {
                    ipv4_addr = it.ToString();
                }
            }
            return ipv4_addr;
        }

        IPAddress GetIP()
        {
            foreach (IPAddress ip in Dns.GetHostEntry(Dns.GetHostName()).AddressList)
            {
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                {
                    return ip;
                }
            }
            return null;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            progressBar1.Location = new Point(x_st + dx * 0 + 60, y_st + dy * 10);

            richTextBox1.Size = new Size(800, 400);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox1.Size = new Size(800, 400);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 7-70);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Location = new Point(50, 50);
            this.Size = new Size(1500, 1000);

            //離開按鈕的寫法
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //連線到Google，使用預設的browser
            Process.Start("http://www.google.com/");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //連線到Google，使用IE
            Process.Start("IExplore.exe", "http://www.google.com");
        }

        //檢查網路連線
        private void button2_Click(object sender, EventArgs e)
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

        //網路連線狀態
        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);
        //參數說明 constate 連接說明 ，reder保留值
        public bool IsConnectedToInternet()
        {
            int Desc = 0;
            return InternetGetConnectedState(out  Desc, 0);
        }

        private void button3_Click(object sender, EventArgs e)
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

        private void button4_Click(object sender, EventArgs e)
        {
            //開啟網頁
            Process.Start("https://www.google.com.tw/?gws_rd=ssl");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //IP位址資料

            /*
            IPAddress[] ipAddresses = null;
            try
            {
                ipAddresses = Dns.GetHostAddresses(formatWWW(www));//Important.
            }
            catch (System.Exception ex)
            {
                Console.WriteLine(ex.Message);
                www = inputWWW();
                continue;
            }
            foreach (IPAddress ipAddress in ipAddresses)
            {
                Console.WriteLine(ipAddress.ToString());
            }
            */

            //網名轉IP位址
            IPAddress[] ip1 = Dns.GetHostAddresses("www.google.com");
            var query1 = from p in ip1 select p;
            foreach (var item in query1)
            {
                richTextBox1.Text += "get : " + item.ToString() + "\n";
            }

            //取得本機IP位址
            IPAddress[] ip2 = Dns.GetHostAddresses(Dns.GetHostName());
            var query2 = from p in ip2 select p;
            foreach (var item in query2)
            {
                richTextBox1.Text += "get : " + item.ToString() + "\n";
            }

            //IP位址轉網名
            IPHostEntry ip3 = Dns.GetHostEntry("192.168.2.114");
            richTextBox1.Text += "host name : " + ip3.HostName + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //獲取gateway和IP

            getxx();
        }

        private void getxx()
        {
            RegistryKey start = Registry.LocalMachine;
            RegistryKey cardServiceName, networkKey;
            string networkcardKey = @"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkCards";
            string serviceKey = @"SYSTEM\CurrentControlSet\Services\";
            string networkcardKeyName, deviceName;
            string deviceServiceName, serviceName;
            RegistryKey serviceNames = start.OpenSubKey(networkcardKey);
            if (serviceNames == null)
            {
                MessageBox.Show("Bad registry key");
                return;
            }
            string[] networkCards = serviceNames.GetSubKeyNames();
            serviceNames.Close();
            foreach (string keyName in networkCards)
            {
                richTextBox1.Text += "get keyName : " + keyName + "\n";
                networkcardKeyName = networkcardKey + "\\" + keyName;
                cardServiceName = start.OpenSubKey(networkcardKeyName);
                if (cardServiceName == null)
                {
                    MessageBox.Show(networkcardKeyName);
                    return;
                }
                deviceServiceName = (string)cardServiceName.GetValue("ServiceName");
                richTextBox1.Text += "deviceServiceName : " + deviceServiceName + "\n";
                deviceName = (string)cardServiceName.GetValue("Description");
                richTextBox1.Text += "deviceName : " + deviceName + "\n";
                MessageBox.Show(deviceName);
                serviceName = serviceKey + deviceServiceName + "\\Parameters\\Tcpip";
                richTextBox1.Text += "serviceName : " + serviceName + "\n";
                networkKey = start.OpenSubKey(serviceName);
                if (networkKey == null)
                {
                    //。。。。。。
                }
                else
                {
                    string[] ipaddresses = (string[])networkKey.GetValue("IPAddress");
                    string[] defaultGateways = (string[])networkKey.GetValue("DefaultGateway");
                    string[] subnetmasks = (string[])networkKey.GetValue("SubnetMask");
                    foreach (string ipaddress in ipaddresses)
                    {
                        MessageBox.Show(ipaddress);
                    }

                    foreach (string subnetmask in subnetmasks)
                    {
                        //。。。。。。
                    }
                    foreach (string defaultGateway in defaultGateways)
                    {
                        MessageBox.Show(defaultGateway);
                    }
                    networkKey.Close();
                }
            }
            start.Close();
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
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
                    where AddressInfo.Address.AddressFamily == AddressFamily.InterNetworkV6
                    let ipAddress = AddressInfo.Address.ToString()
                    select ipAddress);
        }

        string pic1 = "http://www.myson.com.tw/images/index/ad01.jpg";
        string pic2 = "http://www.myson.com.tw/images/index/ad02.jpg";
        string pic3 = "http://www.myson.com.tw/images/index/ad03.jpg";
        string pic4 = "http://www.myson.com.tw/images/index/ad04.jpg";
        int select = 1;
        private void button9_Click(object sender, EventArgs e)
        {
            //取得網路上的圖片並顯示

            switch (select)
            {
                case 1:
                    pictureBox1.ImageLocation = pic1; break;
                case 2:
                    pictureBox1.ImageLocation = pic2; break;
                case 3:
                    pictureBox1.ImageLocation = pic3; break;
                case 4:
                    pictureBox1.ImageLocation = pic4; break;
                default:
                    pictureBox1.ImageLocation = pic1; break;
            }
            select++;
            if (select > 4)
                select = 1;
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
            //DNS相關
            //取得電腦名稱
            richTextBox1.Text += "電腦名稱 : " + Dns.GetHostName() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            IPAddress addr;
            // 獲得本機局域網IP地址
            addr = new IPAddress(Dns.GetHostByName(Dns.GetHostName()).AddressList[0].Address);
            string cc = addr.ToString();

            richTextBox1.Text += "IP地址：" + cc + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //電腦本機IP
            System.Net.IPHostEntry IPHost = System.Net.Dns.GetHostEntry(Environment.MachineName);
            if (IPHost.AddressList.Length > 0)
            {
                richTextBox1.Text += "1電腦本機IP : " + IPHost.AddressList[0].ToString() + "\n";
                //MessageBox.Show(IPHost.AddressList[0].ToString(), "電腦本機IP");
            }

            string hostName = Dns.GetHostName(); //獲取主機名稱
            IPAddress[] addresses = Dns.GetHostAddresses(hostName); //解析主機IP地址

            string[] IP = new string[addresses.Length]; //轉換為字符串形式
            for (int i = 0; i < addresses.Length; i++)
            {
                IP[i] = addresses[i].ToString();
                richTextBox1.Text += "2電腦本機IP : " + IP[i] + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "使用HTTP頭檢測網絡資源是否有效\n";
            /*
我們有時候，需要知道某個網絡資源是否有效、可用，但是我們並不想打開或下載這個資源，因為這個資源可能很大（例如需要下載的某個文件）
一種行之有效的方式，就是利用HTTP頭返回的狀態碼來確定資源的可用性；我們通常的WEB訪問，使用的是 GET 和 POST， 這裡使用的是 HEAD 方式
            */

            string url1 = @"http://hovertree.com/themes/hvtimages/hwqlogo.png";
            string url2 = @"http://hovertree.com/themes/hvtimages/hwqlogoXXX.png";
            bool result1 = IsWebResourceAvailable(url1);
            if (result1 == true)
            {
                richTextBox1.Text += "URL : " + url1 + "\t" + "可用\n";
            }
            else
            {
                richTextBox1.Text += "URL : " + url1 + "\t" + "不可用\n";
            }
            bool result2 = IsWebResourceAvailable(url2);
            if (result2 == true)
            {
                richTextBox1.Text += "URL : " + url2 + "\t" + "可用\n";
            }
            else
            {
                richTextBox1.Text += "URL : " + url2 + "\t" + "不可用\n";
            }
        }

        static bool IsWebResourceAvailable(string webResourceAddress)
        {
            try
            {
                HttpWebRequest req = (HttpWebRequest)WebRequest.CreateDefault(new Uri(webResourceAddress));
                req.Method = "HEAD";
                req.Timeout = 1000;
                HttpWebResponse res = (HttpWebResponse)req.GetResponse();
                return (res.StatusCode == HttpStatusCode.OK);
            }
            catch (WebException wex)
            {
                Trace.Write(wex.Message); return false;
            }
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

        private void button14_Click(object sender, EventArgs e)
        {
            //讀取局域網路由的IP地址
            WebClient wc = new WebClient(); // 建立 WebClient
            wc.Encoding = Encoding.Default; // 指定 WebClient 的編碼
            string lip = wc.DownloadString("http://www.ip138.com/ip2city.asp");
            //string sip = reply.Substring(reply.IndexOf("您的IP地址是"), reply.IndexOf("</center>") - reply.IndexOf("您的IP地址是"));
            //MessageBox.Show(sip);

            //TBD
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //C# Ping a hostname on the network
            Ping ping = new Ping();

            PingReply reply = ping.Send("www.google.com");
            if (reply.Status == IPStatus.Success)
            {
                MessageBox.Show("ok");
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //抓取網頁資料 1
            string url = @"http://140.129.118.16/~richwang/";

            string rl;
            WebRequest Request = WebRequest.Create(url.Trim());

            WebResponse Response = Request.GetResponse();

            Stream resStream = Response.GetResponseStream();

            StreamReader sr = new StreamReader(resStream, Encoding.Default);
            StringBuilder sb = new StringBuilder();
            while ((rl = sr.ReadLine()) != null)
            {
                sb.Append(rl);
            }

            richTextBox1.Text += sb + "\n";

            richTextBox1.Text += "完成\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //抓取網頁資料 2
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString("http://www.lagou.com/");

            richTextBox1.Text += html + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            string name = "www.google.com";

            //透過計算機名取得IP地址
            IPAddress[] ip = null;
            try
            {
                ip = Dns.GetHostAddresses(name);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "電腦名稱 : " + name + "\n";
            richTextBox1.Text += "IP位址 : " + ip[0].ToString() + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            string ip_addr = "140.114.29.100";
            IPHostEntry hostInfo;
            try
            {
                hostInfo = Dns.Resolve(ip_addr);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "IP位址 : " + ip_addr + "\n";
            richTextBox1.Text += "電腦名稱 : " + hostInfo.HostName + "\n";
        }

        private MemoryStream GetResponse(string url)
        {
            while (true)
            {
                try
                {
                    HttpWebRequest request = WebRequest.Create(url) as HttpWebRequest;
                    //request.Headers.Add("Cookie", cookie);
                    request.Method = "GET";
                    request.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko";
                    HttpWebResponse response = request.GetResponse() as HttpWebResponse;

                    MemoryStream ms = new MemoryStream();
                    response.GetResponseStream().CopyTo(ms);

                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //下載HTML
            string url = @"D:/_git/vcs/_1.data/_html/朱冶蕙老師的電腦教室.html";
            //foreach (var fileName in fileNameList)
            {
                MemoryStream ms = GetResponse(url);
                File.WriteAllBytes("aaaaa.html", ms.ToArray());
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }
    }
}

