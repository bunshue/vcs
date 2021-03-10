using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net.Sockets;   //for TcpClient

namespace vcs_TCPIP
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
            TCP_Connect();
        }

        int try_count = 0;
        public void TCP_Connect()
        {
            richTextBox1.Text += "TCP 連線...\n";
            tcpClient = new TcpClient();
            IAsyncResult result = tcpClient.BeginConnect("192.168.10.100", 6300, null, null);
            result.AsyncWaitHandle.WaitOne(3000, true);

            if (!result.IsCompleted)
            {
                if (try_count < 3)
                {
                    richTextBox1.Text += "TCP 連線失敗\t第 " + try_count.ToString() + " 次\n";
                    try_count++;
                    tcpClient.Close();
                    TCP_Connect();
                }
                else
                {
                    tcpClient.Close();
                    richTextBox1.Text += "TCP 連線失敗\n";
                }
            }
        }
    }
}

