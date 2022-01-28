using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Threading;


namespace WindowsFormsApplication1sssss
{
    public partial class Form1 : Form
    {
        //private string[,] LanHost;
        //private Thread[] thread;
        //private System.Windows.Forms.ColumnHeader columnHeader1;
        //private System.Windows.Forms.ColumnHeader columnHeader2;
        private string str;

        private Thread[] many_thread;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        /// <summary>
        /// 多線程搜索方法
        /// </summary>
        private void LanSearchThreadMethod()
        {
            int Currently_i = Convert.ToUInt16(Thread.CurrentThread.Name);  //當前進程名稱
        }

        /// <summary>
        /// 多線程搜索方法
        /// </summary>
        private void MyThreadMethod()
        {
            int Currently_i = Convert.ToUInt16(Thread.CurrentThread.Name);  //當前進程名稱
            Console.Write(Currently_i.ToString() + " ");

            Thread.Sleep(1000);

            /*
            IPAddress ScanIP = IPAddress.Parse(str + "." + Convert.ToString(Currently_i + 1));  //獲得掃描IP地址
            IPHostEntry ScanHost = null;
            ScanHost = Dns.GetHostByAddress(ScanIP);   //獲得掃描IP地址主機信息

            if (ScanHost != null)
            {
                LanHost[Currently_i, 0] = ScanIP.ToString();
                LanHost[Currently_i, 1] = ScanHost.HostName;
            }
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string localhost = (Dns.GetHostByName(Dns.GetHostName())).AddressList[0].ToString();  //本地主機IP地址
            str = localhost.Substring(0, localhost.LastIndexOf("."));

            richTextBox1.Text += "本地主機IP地址 : " + localhost + "\n";
            richTextBox1.Text += "str : " + str + "\n";

            for (int i = 0; i < 255/20; i++)  //建立255個線程掃描IP
            {
                IPAddress ScanIP = IPAddress.Parse(str + "." + Convert.ToString(i + 1));  //獲得掃描IP地址
                richTextBox1.Text += "IP :" + ScanIP.ToString() + "\n";

                //IPHostEntry ScanHost = null;
                //ScanHost = Dns.GetHostByAddress(ScanIP);   //獲得掃描IP地址主機信息

                /*
                if (ScanHost != null)
                {
                    //LanHost[i, 0] = ScanIP.ToString();
                    //LanHost[i, 1] = ScanHost.HostName;
                    richTextBox1.Text += i.ToString() + "\t" + ScanIP.ToString() + "\t" + ScanHost.HostName + "\n";
                }
                */

                /*
                threadMethod = new ThreadStart(LanSearchThreadMethod);
                thread[i] = new Thread(threadMethod);
                thread[i].Name = i.ToString();
                thread[i].Start();
                if (!thread[i].Join(100))    //Thread.Join(100)不知道這處這麼用對不對，感覺沒什麼效果一樣
                {
                    thread[i].Abort();
                }

                int Currently_i = Convert.ToUInt16(Thread.CurrentThread.Name);  //當前進程名稱

                */

            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            many_thread = new Thread[10];

            ThreadStart threadMethod;

            for (int i = 0; i < 10; i++)  //建立255個線程掃描IP
            {
                threadMethod = new ThreadStart(MyThreadMethod);
                many_thread[i] = new Thread(threadMethod);
                many_thread[i].Name = i.ToString();
                many_thread[i].Start();

                /*
                if (!many_thread[i].Join(100))    //Thread.Join(100)不知道這處這麼用對不對，感覺沒什麼效果一樣
                {
                    many_thread[i].Abort();
                }
                */
                Thread.Sleep(1234);
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            /*
            string sss = Thread.CurrentThread.Name;  //當前進程名稱

            richTextBox1.Text += "sss : " + sss + "\n";
            */
            int i;
            for (i = 0; i < 10; i++)
            {
                many_thread[i].Abort();

            }


        }
    }
}


