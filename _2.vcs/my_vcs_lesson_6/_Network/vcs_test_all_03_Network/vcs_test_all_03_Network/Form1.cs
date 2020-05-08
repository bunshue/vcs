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

namespace vcs_test_all_03_Network
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
                MessageBox.Show("已連接在網上!", "提示");
            else
                MessageBox.Show("未連接在網上!!", "提示"); 

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
                MessageBox.Show(we.ToString());
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



    }
}
