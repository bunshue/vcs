using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using System.Net;

namespace ScanIP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        #region 实例化类对象及公共变量
        private Thread myThread;
        string StartIPAddress = "";
        string EndIPAddress = "";
        int intStrat =0;                          //开始扫描地址
        int intEnd = 0;                           //终止扫描地址
        string strIP = "";
        string strflag = "";                      //扫描到的IP地址
        #endregion

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                if (button1.Text == "开始")
                { 
                    listView1.Items.Clear();            //清空ListView控件中的项
                    textBox1.Enabled = textBox2.Enabled = false;
                    strIP = "";
                    strflag = textBox1.Text;
                    StartIPAddress = textBox1.Text;
                    EndIPAddress = textBox2.Text;
                    //开始扫描地址
                    intStrat = Int32.Parse(StartIPAddress.Substring(StartIPAddress.LastIndexOf(".") + 1));
                    //终止扫描地址
                    intEnd = Int32.Parse(EndIPAddress.Substring(EndIPAddress.LastIndexOf(".") + 1));
                    //指定进度条最大值
                    progressBar1.Minimum = intStrat;
                    //指定进度条最小值
                    progressBar1.Maximum = intEnd;
                    //指定进度条初始值
                    progressBar1.Value = progressBar1.Minimum;
                    timer1.Start();             //开始运行计时器
                    button1.Text = "停止";      //设置按钮文本为停止
                    //使用自定义方法StartScan实例化线程对象
                    myThread = new Thread(new ThreadStart(this.StartScan));
                    myThread.Start();                           //开始运行扫描IP的线程
                }
                else
                {
                    textBox1.Enabled = textBox2.Enabled = true;
                    button1.Text = "开始";      //设置按钮文本为开始
                    timer1.Stop();              //停止运行计时器
                    //设置进度条的值为最大值
                    progressBar1.Value = intEnd;
                    if (myThread != null)       //判断线程对象是否为空
                    {
                        //判断扫描IP地址的线程是否正在运行
                        if (myThread.ThreadState == ThreadState.Running)
                        {
                            myThread.Abort();   //终止线程
                        }
                    }
                }
            }
            catch { }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (strIP != "")                           //判读是否有可用IP地址
            {
                if (strIP.IndexOf(',') == -1)
                {
                    if (listView1.Items.Count > 0)
                    {
                        for (int i = 0; i < listView1.Items.Count; i++)
                        {
                            //判断扫描到的IP地址是否与列表中的重复
                            if (listView1.Items[i].Text != strIP)
                            {
                                //向列表中添加扫描到的已用IP地址
                                listView1.Items.Add(strIP);
                            }
                        }
                    }
                    else
                        //向列表汇总添加扫描到的已用IP地址
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
                listView1.Items[i].ImageIndex = 0;
            if (progressBar1.Value < progressBar1.Maximum)  //判断进度条的当前值是否超出其最大值
                progressBar1.Value = Int32.Parse(strflag.Substring(strflag.LastIndexOf(".") + 1));                    //将进度条的值加1
            if (strflag == textBox2.Text)  //判断正在扫描的IP地址是否是结束IP地址
            {
                timer1.Stop();                              //停止运行计时器
                textBox1.Enabled = textBox2.Enabled = true;
                button1.Text = "开始";                      //设置按钮文本为扫描
                MessageBox.Show("IP地址扫描结束！");
            }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (myThread != null)               //判断线程对象是否为空
            {
                //判断扫描IP地址的线程是否正在运行
                if (myThread.ThreadState == ThreadState.Running)
                {
                    myThread.Abort();           //终止线程
                }
            }
        }

        #region 扫描局域网IP地址
        /// <summary>
        /// 扫描局域网IP地址
        /// </summary>
        private void StartScan()
        {
            //扫描的操作
            for (int i = intStrat; i <= intEnd; i++)
            {
                string strScanIP = StartIPAddress.Substring(0, StartIPAddress.LastIndexOf(".") + 1) + i.ToString();
                //转换成IP地址
                IPAddress myScanIP = IPAddress.Parse(strScanIP);
                strflag = strScanIP;
                try
                {
                    //址获取DNS主机信息
                    IPHostEntry myScanHost = Dns.GetHostByAddress(myScanIP);
                    //获取主机名
                    string strHostName = myScanHost.HostName.ToString();
                    if (strIP == "")
                        strIP += strScanIP + "->" + strHostName;
                    else
                        strIP += "," + strScanIP + "->" + strHostName;
                }
                catch { }
            }
        }
        #endregion
    }
}
