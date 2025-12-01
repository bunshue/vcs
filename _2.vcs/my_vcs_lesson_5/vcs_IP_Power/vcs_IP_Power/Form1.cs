using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;               //for WebClient

namespace vcs_IP_Power
{
    public partial class Form1 : Form
    {
        bool flag_debug_mode = false;

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
            int x_st = 10;
            int y_st = 10;
            int w = 170;
            int h = 170;
            int dx = w + 10;
            int dy = h + 10;

            if (flag_debug_mode == true)
            {
                button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
                button2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
                button3.Location = new Point(x_st + dx * 1, y_st + dy * 1);
                button4.Location = new Point(x_st + dx * 0, y_st + dy * 2);

                richTextBox1.Size = new Size(400, 530);
                richTextBox1.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0);
                bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
                this.Size = new Size(800, 590);
            }
            else
            {
                w = 150;
                h = 150;
                dx = w + 5;
                dy = h + 5;
                button0.Size = new Size(w, h);
                button1.Size = new Size(w, h);
                button2.Size = new Size(w, h);
                button3.Size = new Size(w, h);
                button4.Size = new Size(w, h);
                button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
                button2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
                button3.Location = new Point(x_st + dx * 1, y_st + dy * 1);
                button4.Location = new Point(x_st + dx * 0, y_st + dy * 2);

                richTextBox1.Size = new Size(400, 460);
                richTextBox1.Location = new Point(x_st + dx * 2+10, y_st + dy * 0);
                bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
                this.Size = new Size(340, 520);
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void Command_IP_Power_Reset()
        {
            richTextBox1.Text += "設定主機重開\n";

            //# reset
            string url = @"http://192.168.2.123/set.cmd?user=admin+pass=12345678+cmd=setpowercycle&p61=1";
            richTextBox1.Text += "reset\n";
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";
        }

        void Command_IP_Power_Info()
        {
            richTextBox1.Text += "測試IPPower\n";

            //# 2.1 To get firmware version : getversion
            richTextBox1.Text += "getversion\n";
            string url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getversion";
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //# 2.2 To get MACaddress：getmac
            richTextBox1.Text += "getmac\n";
            url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getmac";
            wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //# 2.3 To get the status of power on/ off： getpower
            richTextBox1.Text += "getpower\n";
            url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getpower";
            wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //# 2.6 Get current Amp value : getcurrent
            url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getcurrent";
            richTextBox1.Text += "getcurrent\n";
            wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";
        }

        void Command_IP_Power_ON()
        {
            //# 上電
            string url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=setpower&p61=1";
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";
        }

        void Command_IP_Power_OFF()
        {
            //# 下電
            string url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=setpower&p61=0";
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString(url);
            richTextBox1.Text += html + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Command_IP_Power_Reset();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Command_IP_Power_Info();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Command_IP_Power_ON();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Command_IP_Power_OFF();
        }
    }
}
