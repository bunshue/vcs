using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.DirectoryServices;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ScanPort
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        #region 实例化类对象和公共变量
        //实例化DirectoryEntry对象，以便获得局域网组名和计算机名
        DirectoryEntry DEMain = new DirectoryEntry("WinNT:");
        TcpClient TClient = null;       //实例化连接侦听对象
        private Thread myThread;        //实例化线程对象
        string strName = "";            //记录选择的计算机名称
        int intflag = 0;                //扫描到的端口号
        int intport = 0;                //记录已用端口号
        int intstart = 0;               //扫描的开始端口号
        int intend = 0;                 //扫描的结束端口号
        #endregion

        private void Form1_Load(object sender, EventArgs e)
        {
            //遍历局域网中的工作组，并显示在下拉列表控件中
            foreach (DirectoryEntry DEGroup in DEMain.Children)
            {
                comboBox1.Items.Add(DEGroup.Name);
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            foreach (DirectoryEntry DEGroup in DEMain.Children)
            {
                //判断工作组名称
                if (DEGroup.Name.ToLower() == comboBox1.Text.ToLower())
                {
                    //遍历指定工作组中的所有计算机名称，并显示在ListBox控件中
                    foreach (DirectoryEntry DEComputer in DEGroup.Children)
                    {
                        if (DEComputer.Name.ToLower() != "schema")
                        {
                            listBox1.Items.Add(DEComputer.Name);
                        }
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();            //清空ListView控件中的项
            try
            {
                if (button1.Text == "扫描")
                {
                    intport = 0;                //初始化已用端口号
                    //指定进度条最大值
                    progressBar1.Minimum = Convert.ToInt32(textBox1.Text);
                    //指定进度条最小值
                    progressBar1.Maximum = Convert.ToInt32(textBox2.Text);
                    //指定进度条初始值
                    progressBar1.Value = progressBar1.Minimum;
                    timer1.Start();             //开始运行计时器
                    button1.Text = "停止";      //设置按钮文本为停止
                    intstart = Convert.ToInt32(textBox1.Text);  //为开始扫描的端口号赋值
                    intend = Convert.ToInt32(textBox2.Text);    //为结束扫描的端口号赋值
                    //使用自定义方法StartScan实例化线程对象
                    myThread = new Thread(new ThreadStart(this.StartScan));
                    myThread.Start();                           //开始运行扫描端口号的线程
                }
                else
                {
                    button1.Text = "扫描";      //设置按钮文本为扫描
                    timer1.Stop();              //停止运行计时器
                    //设置进度条的值为最大值
                    progressBar1.Value = Convert.ToInt32(textBox2.Text);
                    if (myThread != null)       //判断线程对象是否为空
                    {
                        //判断扫描端口号的线程是否正在运行
                        if (myThread.ThreadState == ThreadState.Running)
                        {
                            myThread.Abort();   //终止线程
                        }
                    }
                }
            }
            catch { }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (myThread != null)               //判断线程对象是否为空
            {
                //判断扫描端口号的线程是否正在运行
                if (myThread.ThreadState == ThreadState.Running)
                {
                    myThread.Abort();           //终止线程
                }
            }
        }

        private void listBox1_Click(object sender, EventArgs e)
        {
            strName = listBox1.SelectedItem.ToString(); //记录选择的计算机名称
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (intport != 0)                           //判读是否有可用端口号
            {
                if (listView1.Items.Count > 0)
                {
                    for (int i = 0; i < listView1.Items.Count; i++)
                    {
                        //判断扫描到的端口号是否与列表中的重复
                        if (listView1.Items[i].Text != intport.ToString())
                        {
                            //向列表中添加扫描到的已用端口号
                            listView1.Items.Add(intport.ToString());
                        }
                    }
                }
                else
                    //向列表汇总添加扫描到的已用端口号
                    listView1.Items.Add(intport.ToString());
                intport = 0;
            }
            if (progressBar1.Value < progressBar1.Maximum)  //判断进度条的当前值是否超出其最大值
                progressBar1.Value += 1;                    //将进度条的值加1
            if (intflag == Convert.ToInt32(textBox2.Text))  //判断正在扫描的端口号是否是结束端口号
            {
                timer1.Stop();                              //停止运行计时器
                button1.Text = "扫描";                      //设置按钮文本为扫描
                MessageBox.Show("端口扫描结束！");
            }
        }

        #region 扫描端口号
        /// <summary>
        /// 扫描端口号
        /// </summary>
        private void StartScan()
        {
            while (true)
            {
                for (int i = intstart; i <= intend; i++)
                {
                    intflag = i;                            //记录正在扫描的端口号
                    try
                    {
                        TClient = new TcpClient(strName, i);//使用记录的计算机名称和端口号实例化侦听对象
                        intport = i;                        //记录已分配的端口号
                    }
                    catch { }
                }
            }
        }
        #endregion
    }
}
