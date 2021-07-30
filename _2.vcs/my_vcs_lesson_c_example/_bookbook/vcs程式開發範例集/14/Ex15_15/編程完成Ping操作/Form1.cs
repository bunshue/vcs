using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net.NetworkInformation;

namespace 編程完成Ping操作
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
            try
            {
                Ping PingInfo = new Ping();
                PingOptions PingOpt = new PingOptions();
                PingOpt.DontFragment = true;
                string myInfo = "hyworkhyworkhyworkhyworkhyworkhywork";
                byte[] bufferInfo = Encoding.ASCII.GetBytes(myInfo);
                int TimeOut = 120;

                richTextBox1.Text += "IP地址/機器名 : \t" + this.textBox1.Text + "\n";

                PingReply reply = PingInfo.Send(this.textBox1.Text, TimeOut, bufferInfo, PingOpt);
                if (reply.Status == IPStatus.Success)
                {
                    this.textBox2.Text = reply.RoundtripTime.ToString();
                    this.textBox3.Text = reply.Options.Ttl.ToString();
                    this.textBox4.Text = (reply.Options.DontFragment ? "發生分段" : "沒有發生分段");
                    this.textBox5.Text = reply.Buffer.Length.ToString();

                    richTextBox1.Text += "網路訊息\n耗費時間 : \t" + reply.RoundtripTime.ToString() + "\n";
                    richTextBox1.Text += "路由節點數 : \t" + reply.Options.Ttl.ToString() + "\n";
                    richTextBox1.Text += "數據分段 : \t" + (reply.Options.DontFragment ? "發生分段" : "沒有發生分段") + "\n";
                    richTextBox1.Text += "緩衝區大小 : \t" + reply.Buffer.Length.ToString() + "\n";
                }
                else
                {
                    richTextBox1.Text += "無法Ping通\n";
                }
            }
            catch (Exception ex)
            {
                //MessageBox.Show(ex.Message);
                richTextBox1.Text += "無法Ping, 錯誤訊息:\n" + ex.Message + "\n";
            }
            richTextBox1.Text += "\n";
        }
    }
}

