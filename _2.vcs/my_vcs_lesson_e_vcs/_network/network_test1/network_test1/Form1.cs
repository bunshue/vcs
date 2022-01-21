using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Mail;  //for SmtpClient
using System.Xml;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

using System.Diagnostics;

namespace network_test1
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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "檢查URL鏈接是否有效\n";
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/11093.html";
            bool ret = CheckUri(url);
            richTextBox1.Text += "結果 : \t" + ret.ToString() + "\n";

            url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/11093XX.html";
            ret = CheckUri(url);
            richTextBox1.Text += "結果 : \t" + ret.ToString() + "\n";


        }

        /// <summary>
        /// 檢查url鏈接是否有效
        /// </summary>
        /// <param name="strUri"></param>
        /// <returns></returns>
        public static bool CheckUri(string strUri)
        {
            try
            {
                System.Net.HttpWebRequest.Create(strUri).GetResponse();
                return true;
            }
            catch
            {
                return false;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //httpWebRequest 文件下載，
            const string uri = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/SMS_K%C3%B6nig_Albert.jpg/450px-SMS_K%C3%B6nig_Albert.jpg";
            var req = WebRequest.Create(uri) as HttpWebRequest;
            //req.ContentType = "application/octet-stream";
            if (req != null)
            {
                var response = req.GetResponse() as HttpWebResponse;
                if (response != null)
                {
                    Console.WriteLine("ContentType:" + response.ContentType);
                    var stream = response.GetResponseStream();
                    if (stream != null)
                    {
                        string format = string.Empty;
                        switch (response.ContentType)
                        {
                            case "image/jpeg":
                                format = "jpg";
                                break;
                            case "audio/amr":
                                format = "amr";
                                break;
                        }

                        var path = string.Format(@"1.{0}", format);
                        //var fs = new FileStream($"c:\\1.{format}", FileMode.Create);
                        var fs = File.Create(path);
                        richTextBox1.Text += "下載完成, 檔案 : \t" + path + "\n";

                        int count = 0;
                        do
                        {
                            var buffer = new byte[4096];
                            count = stream.Read(buffer, 0, buffer.Length);
                            fs.Write(buffer, 0, count);
                        } while (count > 0);
                    }
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
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
            //獲取遠程網頁中的所有鏈接URL
            string url = @"https://pydoing.blogspot.com/";
            System.Net.WebClient client = new WebClient();
            byte[] page = client.DownloadData(url);
            string content = System.Text.Encoding.UTF8.GetString(page);
            string regex = "href=[\\\"\\\'](http:\\/\\/|\\.\\/|\\/)?\\w+(\\.\\w+)*(\\/\\w+(\\.\\w+)?)*(\\/|\\?\\w*=\\w*(&\\w*=\\w*)*)?[\\\"\\\']";
            Regex re = new Regex(regex);
            MatchCollection matches = re.Matches(content);

            System.Collections.IEnumerator enu = matches.GetEnumerator();
            while (enu.MoveNext() && enu.Current != null)
            {
                Match match = (Match)(enu.Current);
                //Console.Write(match.Value + "\r\n");
                richTextBox1.Text += "sssss : " + match.Value + "\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

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

