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
                richTextBox1.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0);
                bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
                this.Size = new Size(340, 520);
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //讓 WebClient 擁有 Timeout 功能
        public class MyWebClient : WebClient
        {
            protected override WebRequest GetWebRequest(Uri uri)
            {
                WebRequest WR = base.GetWebRequest(uri);
                WR.Timeout = 3 * 1000;     //3秒
                return WR;
            }
        }

        void Command_IP_Power_Reset()
        {
            richTextBox1.Text += "斷電重開\n";
            Application.DoEvents();

            string url = @"http://192.168.2.123/set.cmd?user=admin+pass=12345678+cmd=setpowercycle&p61=1";
            //WebClient wc = new WebClient();
            MyWebClient wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            try
            {
                string html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }
        }

        void Command_IP_Power_Info()
        {
            richTextBox1.Text += "取得 IP Power 的 狀態\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "取得 IP Power 的 韌體版本 getversion\n";
            Application.DoEvents();

            string url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getversion";
            //WebClient wc = new WebClient();
            MyWebClient wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            string html = string.Empty;
            try
            {
                html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "取得 IP Power 的 MAC 位址 getmac\n";
            Application.DoEvents();

            url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getmac";
            //wc = new WebClient();
            wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            try
            {
                html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "取得 IP Power 的 電源狀態 getpower\n";
            Application.DoEvents();

            url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getpower";
            //wc = new WebClient();
            wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            try
            {
                html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "取得 IP Power 的 電流值 getcurrent\n";
            Application.DoEvents();

            url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=getcurrent";
            //wc = new WebClient();
            wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            try
            {
                html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        void Command_IP_Power_ON()
        {
            richTextBox1.Text += "上電\n";
            Application.DoEvents();

            string url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=setpower&p61=1";
            //WebClient wc = new WebClient();
            MyWebClient wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            try
            {
                string html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }
        }

        void Command_IP_Power_OFF()
        {
            richTextBox1.Text += "下電\n";
            Application.DoEvents();

            string url = @"http://192.168.2.123/set.cmd?user=root+pass=12345678+cmd=setpower&p61=0";
            //WebClient wc = new WebClient();
            MyWebClient wc = new MyWebClient();
            wc.Encoding = Encoding.UTF8;
            try
            {
                string html = wc.DownloadString(url);
                richTextBox1.Text += html + "\n";
            }
            catch (WebException ex)
            {
                richTextBox1.Text += "WebException\t" + ex.Message + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }
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
