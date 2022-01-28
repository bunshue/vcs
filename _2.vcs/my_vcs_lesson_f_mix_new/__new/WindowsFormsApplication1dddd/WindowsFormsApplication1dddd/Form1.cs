using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;

using System.Diagnostics;

namespace WindowsFormsApplication1dddd
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
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
    }
}
