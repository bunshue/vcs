using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

using System.Management;    //for ManagementObjectSearcher

using System.Diagnostics;
using System.IO;

using System.Runtime.InteropServices;   //for DllImport

using System.Text.RegularExpressions;   //for Regex
namespace test_new0418
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            /*
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.StandardInput.WriteLine(@"netstat -a -n > c:\port.txt");
            */

            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 150;
            dy = 60;

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

            button15.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 4);

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //取得所有邏輯分區
            //取得本地磁盤目錄
            richTextBox1.Text += "取得所有邏輯分區\n";
            string[] logicdrives = System.IO.Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                richTextBox1.Text += "取得: " + logicdrives[i] + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
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

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button3_Click(object sender, EventArgs e)
        {
            //取得本機MAC地址

            ManagementObjectSearcher nisc = new ManagementObjectSearcher("select * from Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject nic in nisc.Get())
            {
                if (Convert.ToBoolean(nic["ipEnabled"]) == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(nic["MACAddress"]) + "\n";
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.richTextBox1.Text += "取得系統開啟的端口和狀態\n";
            try
            {
                string path = @"c:\port.txt";
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

        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);
        //參數說明 constate 連接說明 ，reder保留值
        public bool IsConnectedToInternet()
        {
            int Desc = 0;
            return InternetGetConnectedState(out  Desc, 0);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //監測目前網絡連接狀態
            if (IsConnectedToInternet())
                MessageBox.Show("已連接在網上!", "提示");
            else
                MessageBox.Show("未連接在網上!!", "提示");

        }

        public string getstr(string strUrl)
        {
            string d = @"<title>(?<title>[^<]*)</title>";
            return Regex.Match(strUrl, d).ToString();
        }

        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "提取網頁標題\n";
            string url = "https://www.youtube.com/watch?v=ViyVmAU0zgo";

            if (ValidateDate1(url))
            {
                string strl;//儲存編碼
                WebRequest wb = WebRequest.Create(url);//請求資源
                WebResponse webRed = wb.GetResponse();//響應請求
                Stream redweb = webRed.GetResponseStream();//傳回數據存入流中
                StreamReader sr = new StreamReader(redweb, Encoding.UTF8);//從流中讀出數據
                StringBuilder sb = new StringBuilder();//可變字符
                while ((strl = sr.ReadLine()) != null)
                {
                    sb.Append(strl);//讀出數據存入可變字符中
                }
                string result = getstr(sb.ToString());//呼叫正則表達式方法讀出標題
                richTextBox1.Text += "網頁標題:\t" + result + "\n";
            }
            else
            {
                MessageBox.Show("請輸入正確的網址");
                return;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //獲得硬盤序號

            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            string strHardDiskID = "";
            foreach (ManagementObject mo in searcher.Get())
            {
                strHardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            //label2.Text = strHardDiskID;
            richTextBox1.Text += "獲得硬盤序號 : " + strHardDiskID + "\n";



        }

        private void button8_Click(object sender, EventArgs e)
        {
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in searcher.Get())
            {
                string disk_name = disk["Name"].ToString();
                richTextBox1.Text += "取得硬碟 : " + disk_name + "\n";

                DriveInfo dinfo = new DriveInfo(disk_name);
                if (dinfo.IsReady == true)
                {
                    richTextBox1.Text += "驅動器總容量：" + dinfo.TotalSize + " B\n";
                    richTextBox1.Text += "驅動器剩餘容量：" + dinfo.TotalFreeSpace + " B\n"; ;
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            DriveInfo dinfo = new DriveInfo(@"C:\");
            float tsize = dinfo.TotalSize;
            float fsize = dinfo.TotalFreeSpace;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen pen1 = new Pen(Color.Red);
            Brush brush1 = new SolidBrush(Color.WhiteSmoke);
            Brush brush2 = new SolidBrush(Color.LimeGreen);
            Brush brush3 = new SolidBrush(Color.RoyalBlue);
            Font font1 = new Font("Courier New", 16, FontStyle.Bold);
            Font font2 = new Font("細明體", 9);
            g.DrawString("磁盤容量分析", font1, brush2, new Point(60, 50));
            float angle1 = Convert.ToSingle((360 * (Convert.ToSingle(fsize / 100000000000) / Convert.ToSingle(tsize / 100000000000))));
            float angle2 = Convert.ToSingle((360 * (Convert.ToSingle((tsize - fsize) / 100000000000) / Convert.ToSingle(tsize / 100000000000))));
            g.FillPie(brush2, 60, 80, 150, 150, 0, angle1);
            g.FillPie(brush3, 60, 80, 150, 150, angle1, angle2);
            g.DrawRectangle(pen1, 30, 235, 200, 50);
            g.FillRectangle(brush2, 35, 245, 20, 10);
            g.DrawString("磁盤剩餘容量:" + dinfo.TotalFreeSpace / 1000 + "KB", font2, brush2, 55, 245);
            g.FillRectangle(brush3, 35, 265, 20, 10);
            g.DrawString("磁盤已用容量:" + (dinfo.TotalSize - dinfo.TotalFreeSpace) / 1000 + "KB", font2, brush3, 55, 265);

        }


        [DllImport("shell32.dll")]
        private static extern int SHFormatDrive(IntPtr hWnd, int drive, long fmtID, int Options);
        public const long SHFMT_ID_DEFAULT = 0xFFFF;
        private void button10_Click(object sender, EventArgs e)
        {
            int drive_id = 4;   //A: 0, B: 1, C: 2, D: 3, E: 4.....

            //格式化磁盤
            try
            {
                //偽執行
                //SHFormatDrive(this.Handle, drive_id, SHFMT_ID_DEFAULT, 0);
                MessageBox.Show("格式化完成", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch
            {
                MessageBox.Show("格式化失敗", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("確定要休眠計算機嗎？") == DialogResult.OK)
            {
                //偽執行
                //Application.SetSuspendState(PowerState.Hibernate, true, true);
            }

        }
    }
}

