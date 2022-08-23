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

namespace ScanIP
{
    public partial class Form1 : Form
    {
        //實例化類對象及公共變量
        private Thread myThread;
        string StartIPAddress = "";
        string EndIPAddress = "";
        int intStrat = 0;                          //開始掃描地址
        int intEnd = 0;                           //終止掃描地址
        string strIP = "";
        string strflag = "";                      //掃描到的IP地址

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (myThread != null)               //判斷線程對象是否為空
            {
                //判斷掃描IP地址的線程是否正在運行
                if (myThread.ThreadState == ThreadState.Running)
                {
                    myThread.Abort();           //終止線程
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                if (button1.Text == "開始")
                {
                    listView1.Items.Clear();            //清空ListView控件中的項
                    textBox1.Enabled = textBox2.Enabled = false;
                    strIP = "";
                    strflag = textBox1.Text;
                    StartIPAddress = textBox1.Text;
                    EndIPAddress = textBox2.Text;
                    //開始掃描地址
                    intStrat = Int32.Parse(StartIPAddress.Substring(StartIPAddress.LastIndexOf(".") + 1));
                    //終止掃描地址
                    intEnd = Int32.Parse(EndIPAddress.Substring(EndIPAddress.LastIndexOf(".") + 1));
                    //指定進度條最大值
                    progressBar1.Minimum = intStrat;
                    //指定進度條最小值
                    progressBar1.Maximum = intEnd;
                    //指定進度條初始值
                    progressBar1.Value = progressBar1.Minimum;
                    timer1.Start();             //開始運行計時器
                    button1.Text = "停止";      //設置按鈕文本為停止
                    //使用自定義方法StartScan實例化線程對象
                    myThread = new Thread(new ThreadStart(this.StartScan));
                    myThread.Start();                           //開始運行掃描IP的線程
                }
                else
                {
                    textBox1.Enabled = textBox2.Enabled = true;
                    button1.Text = "開始";      //設置按鈕文本為開始
                    timer1.Stop();              //停止運行計時器
                    //設置進度條的值為最大值
                    progressBar1.Value = intEnd;
                    if (myThread != null)       //判斷線程對象是否為空
                    {
                        //判斷掃描IP地址的線程是否正在運行
                        if (myThread.ThreadState == ThreadState.Running)
                        {
                            myThread.Abort();   //終止線程
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (strIP != "")                           //判讀是否有可用IP地址
            {
                if (strIP.IndexOf(',') == -1)
                {
                    if (listView1.Items.Count > 0)
                    {
                        for (int i = 0; i < listView1.Items.Count; i++)
                        {
                            //判斷掃描到的IP地址是否與列表中的重復
                            if (listView1.Items[i].Text != strIP)
                            {
                                //向列表中添加掃描到的已用IP地址
                                listView1.Items.Add(strIP);
                            }
                        }
                    }
                    else
                        //向列表匯總添加掃描到的已用IP地址
                        listView1.Items.Add(strIP);
                }
                else
                {
                    string[] strIPS = strIP.Split(',');
                    for (int i = 0; i < strIPS.Length; i++)
                    {
                        listView1.Items.Add(strIPS[i].ToString());
                    }
                }
                strIP = "";
            }
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                listView1.Items[i].ImageIndex = 0;
            }
            if (progressBar1.Value < progressBar1.Maximum)  //判斷進度條的當前值是否超出其最大值
            {
                progressBar1.Value = Int32.Parse(strflag.Substring(strflag.LastIndexOf(".") + 1));                    //將進度條的值加1
            }
            if (strflag == textBox2.Text)  //判斷正在掃描的IP地址是否是結束IP地址
            {
                timer1.Stop();                              //停止運行計時器
                textBox1.Enabled = textBox2.Enabled = true;
                button1.Text = "開始";                      //設置按鈕文本為掃描
                MessageBox.Show("IP地址掃描結束！");
            }
        }

        //掃描局域網IP地址
        /// <summary>
        /// 掃描局域網IP地址
        /// </summary>
        private void StartScan()
        {
            //掃描的操作
            for (int i = intStrat; i <= intEnd; i++)
            {
                string strScanIP = StartIPAddress.Substring(0, StartIPAddress.LastIndexOf(".") + 1) + i.ToString();
                //轉換成IP地址
                IPAddress myScanIP = IPAddress.Parse(strScanIP);
                strflag = strScanIP;
                try
                {
                    //址獲取DNS主機信息
                    IPHostEntry myScanHost = Dns.GetHostByAddress(myScanIP);
                    //獲取主機名
                    string strHostName = myScanHost.HostName.ToString();
                    if (strIP == "")
                        strIP += strScanIP + "->" + strHostName;
                    else
                        strIP += "," + strScanIP + "->" + strHostName;
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }
    }
}
