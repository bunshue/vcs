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
using System.Net.NetworkInformation;    //for UnicastIPAddressInformation

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
            dx = 225;
            dy = 50;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 13);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

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
            System.Diagnostics.Process.Start("http://www.google.com/");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //連線到Google，使用IE
            System.Diagnostics.Process.Start("IExplore.exe", "http://www.google.com");
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

        private void button3_Click(object sender, EventArgs e)
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

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

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
            {
                if (ip.AddressFamily == AddressFamily.InterNetwork)
                {
                    return ip;
                }
            }
            return null;
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
    }
}

