using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net.NetworkInformation;
namespace 编程实现Ping操作
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                Ping PingInfo = new Ping();
                PingOptions PingOpt = new PingOptions();
                PingOpt.DontFragment = true;
                string myInfo = "hyworkhyworkhyworkhyworkhyworkhywork";
                byte[] bufferInfo = Encoding.ASCII.GetBytes(myInfo);
                int TimeOut = 120;
                PingReply reply = PingInfo.Send(this.textBox1.Text, TimeOut, bufferInfo, PingOpt);
                if (reply.Status == IPStatus.Success)
                {
                    this.textBox2.Text = reply.RoundtripTime.ToString();
                    this.textBox3.Text = reply.Options.Ttl.ToString();
                    this.textBox4.Text = (reply.Options.DontFragment ? "发生分段" : "没有发生分段");
                    this.textBox5.Text = reply.Buffer.Length.ToString();
                }
                else
                {
                    MessageBox.Show("无法Ping通");
                }
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}