using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace vcs_test_network
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
            string hostname = Dns.GetHostName();
            richTextBox1.Text += "hostname : " + hostname + "\n";

            IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];
            richTextBox1.Text += "serverIP : " + serverIP + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {




        }


        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}
