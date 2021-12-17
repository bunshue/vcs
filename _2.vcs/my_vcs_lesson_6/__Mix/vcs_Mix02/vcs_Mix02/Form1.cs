using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Management;    //for ManagementObjectSearcher
using System.Net;

using Microsoft.VisualBasic.Devices;    //for Computer

namespace vcs_Mix02
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.StandardInput.WriteLine(@"netstat -a -n > c:\dddddddddd\port.txt");

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
            dy = 80;

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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 25);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 50);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 75);
            label4.Location = new Point(x_st + dx * 3, y_st + dy * 10);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string filename1 = @"C:\______test_files\compare\aaaa.txt";
            string filename2 = @"C:\______test_files\compare\bbbb.txt";

            StreamReader sr1 = new StreamReader(filename1);
            StreamReader sr2 = new StreamReader(filename2);
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))
            {
                MessageBox.Show("兩個文件相等");
            }
            else
            {
                MessageBox.Show("兩個文件不相等");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //取得所有邏輯分區
            //取得本地磁盤目錄
            richTextBox1.Text += "取得所有邏輯分區\n";
            string[] logicdrives = System.IO.Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                richTextBox1.Text += "取得: " + logicdrives[i] + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string name = "www.google.com";

            //透過計算機名取得IP地址
            IPAddress[] ip = null;
            try
            {
                ip = Dns.GetHostAddresses(name);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "電腦名稱 : " + name + "\n";
            richTextBox1.Text += "IP位址 : " + ip[0].ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string ip_addr = "140.114.29.100";
            IPHostEntry hostInfo;
            try
            {
                hostInfo = Dns.Resolve(ip_addr);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "IP位址 : " + ip_addr + "\n";
            richTextBox1.Text += "電腦名稱 : " + hostInfo.HostName + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //取得本機MAC地址

            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if (Convert.ToBoolean(mo["ipEnabled"]) == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(mo["MACAddress"]) + "\n";
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            richTextBox1.Text += "取得系統開啟的端口和狀態\n";
            try
            {
                string path = @"c:\dddddddddd\port.txt";
                using (StreamReader sr = new StreamReader(path))
                {
                    while (sr.Peek() >= 0)
                    {
                        this.richTextBox1.Text += sr.ReadLine() + "\r\n";
                    }
                }
            }
            catch (Exception hy)
            {
                MessageBox.Show(hy.Message);
            }
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
            show_button_text(sender);

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

        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //參考/加入參考/.Net/Microsoft.VisualBasic
            Computer myComputer = new Computer();
            label0.Text = "物理內存總量（M）：" + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024);
            label1.Text = "可用物理內存（M）：" + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024);
            label2.Text = "虛擬內存總量（M）：" + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024);
            label3.Text = "可用虛擬內存（M）：" + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024);

            label4.Text = "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + " 秒";


        }

    }
}
