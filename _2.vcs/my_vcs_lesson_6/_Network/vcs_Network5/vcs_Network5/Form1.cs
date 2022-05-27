using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for HttpWebRequest, WebClient
using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.Collections;   //for Stack
using System.Text.RegularExpressions;


//using System.Xml;
//using System.Management;
//using System.Runtime.InteropServices;

using Microsoft.Win32;


namespace vcs_Network5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            show_item_location();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 185;
            dy = 85;

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

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            button24.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 11);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            int w = 0;
            int h = 0;

            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            w = this.ClientSize.Width - richTextBox1.Location.X - 10;   //border : 10
            h = this.ClientSize.Height - richTextBox1.Location.Y - 10;   //border : 10
            richTextBox1.Size = new Size(w, h);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

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

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //讀取局域網路由的IP地址

            //讀取局域網路由的IP地址
            WebClient wc = new WebClient(); // 建立 WebClient
            wc.Encoding = Encoding.Default; // 指定 WebClient 的編碼
            string lip = wc.DownloadString("http://www.ip138.com/ip2city.asp");
            //string sip = reply.Substring(reply.IndexOf("您的IP地址是"), reply.IndexOf("</center>") - reply.IndexOf("您的IP地址是"));
            //MessageBox.Show(sip);

            //TBD

        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //調用系統IPCONFIG獲取本機局域網IP以及其他相關信息

            string result = GetIPConfigReturns();
            richTextBox1.Text += "  " + result + "\n";

        }

        /// <summary> 
        /// 獲取IPCONFIG返回值 
        /// </summary> 
        /// <returns>返回 IPCONFIG輸出</returns> 
        public static string GetIPConfigReturns()
        {
            string version = Environment.OSVersion.VersionString;

            if (version.Contains("Windows"))
            {
                //調用ipconfig ,並傳入參數: /all 
                ProcessStartInfo psi = new ProcessStartInfo("ipconfig", "/all");

                psi.CreateNoWindow = true; //若為false，則會出現cmd的黑窗體 
                psi.RedirectStandardOutput = true;
                psi.UseShellExecute = false;

                Process p = Process.Start(psi);

                return p.StandardOutput.ReadToEnd();
            }

            return string.Empty;
        }


        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //檢測網絡連接（主要是局域網）

            //檢測網絡連接（主要是局域網）
            string ip;
            ip = "10.1.148.1";
            // string ip = "192.192.132.229";

            //  string strRst = CmdPing(ip);

            //   MessageBox.Show(strRst);
            string str = CmdPingh(ip);
            MessageBox.Show(str);
        }

        private static string CmdPing(string strIp)//方法1
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            string pingrst;
            p.Start();
            p.StandardInput.WriteLine("ping -n 1 " + strIp);
            p.StandardInput.WriteLine("exit");
            string strRst = p.StandardOutput.ReadToEnd();
            if (strRst.IndexOf("(0% loss)") != -1)
                pingrst = "連接";
            else if (strRst.IndexOf("Destination host unreachable.") != -1)
                pingrst = "無法到達目的主機";
            else if (strRst.IndexOf("Request timed out.") != -1)
                pingrst = "超時";
            else if (strRst.IndexOf("Unknown host") != -1)
                pingrst = "無法解析主機";
            else
                pingrst = strRst;
            p.Close();
            return pingrst;
        }

        public static string CmdPingh(string _strHost)   //與上面的方法一樣，不同寫法而已
        {
            string m_strHost = _strHost;
            Process process = new Process();
            process.StartInfo.FileName = "cmd.exe";
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.RedirectStandardInput = true;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.CreateNoWindow = true;
            string pingrst = string.Empty;
            process.StartInfo.Arguments = "ping   " + m_strHost + "   -n   1";
            process.Start();
            process.StandardInput.AutoFlush = true;
            string temp = "ping   " + m_strHost + "   -n   1";
            process.StandardInput.WriteLine(temp);
            process.StandardInput.WriteLine("exit");
            string strRst = process.StandardOutput.ReadToEnd();
            if (strRst.IndexOf("(0%   loss)") != -1)
                pingrst = "連接";
            else if (strRst.IndexOf("Destination   host   unreachable.") != -1)
                pingrst = "無法到達目的主機";
            else if (strRst.IndexOf("Request   timed   out.") != -1)
                pingrst = "超時";
            else if (strRst.IndexOf("Unknown   host") != -1)
                pingrst = "無法解析主機";
            else
                pingrst = strRst;
            process.Close();
            return pingrst;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取gateway和IP

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

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //抓取網頁資料 2
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString("http://www.lagou.com/");

            richTextBox1.Text += html + "\n";
        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button30_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button31_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button33_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button34_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }
    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}

