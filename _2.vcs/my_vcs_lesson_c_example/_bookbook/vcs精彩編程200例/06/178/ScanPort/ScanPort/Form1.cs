using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.DirectoryServices;

namespace ScanPort
{
    public partial class Form1 : Form
    {
        //實例化DirectoryEntry對象，以便獲得局域網組名和計算機名
        DirectoryEntry DEMain = new DirectoryEntry("WinNT:");
        TcpClient TClient = null;       //實例化連接偵聽對象
        private Thread myThread;        //實例化線程對象
        string strName = "";            //記錄選擇的計算機名稱
        int intflag = 0;                //掃描到的端口號
        int intport = 0;                //記錄已用端口號
        int intstart = 0;               //掃描的開始端口號
        int intend = 0;                 //掃描的結束端口號

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "遍歷局域網中的工作組，并顯示在下拉列表控件中\n";
            //遍歷局域網中的工作組，并顯示在下拉列表控件中
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
                //判斷工作組名稱
                if (DEGroup.Name.ToLower() == comboBox1.Text.ToLower())
                {
                    //遍歷指定工作組中的所有計算機名稱，并顯示在ListBox控件中
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
            listView1.Items.Clear();            //清空ListView控件中的項
            try
            {
                if (button1.Text == "掃描")
                {
                    intport = 0;                //初始化已用端口號
                    //指定進度條最大值
                    progressBar1.Minimum = Convert.ToInt32(textBox1.Text);
                    //指定進度條最小值
                    progressBar1.Maximum = Convert.ToInt32(textBox2.Text);
                    //指定進度條初始值
                    progressBar1.Value = progressBar1.Minimum;
                    timer1.Start();             //開始運行計時器
                    button1.Text = "停止";      //設置按鈕文本為停止
                    intstart = Convert.ToInt32(textBox1.Text);  //為開始掃描的端口號賦值
                    intend = Convert.ToInt32(textBox2.Text);    //為結束掃描的端口號賦值
                    //使用自定義方法StartScan實例化線程對象
                    myThread = new Thread(new ThreadStart(this.StartScan));
                    myThread.Start();                           //開始運行掃描端口號的線程
                }
                else
                {
                    button1.Text = "掃描";      //設置按鈕文本為掃描
                    timer1.Stop();              //停止運行計時器
                    //設置進度條的值為最大值
                    progressBar1.Value = Convert.ToInt32(textBox2.Text);
                    if (myThread != null)       //判斷線程對象是否為空
                    {
                        //判斷掃描端口號的線程是否正在運行
                        if (myThread.ThreadState == ThreadState.Running)
                        {
                            myThread.Abort();   //終止線程
                        }
                    }
                }
            }
            catch { }
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (myThread != null)               //判斷線程對象是否為空
            {
                //判斷掃描端口號的線程是否正在運行
                if (myThread.ThreadState == ThreadState.Running)
                {
                    myThread.Abort();           //終止線程
                }
            }
        }

        private void listBox1_Click(object sender, EventArgs e)
        {
            strName = listBox1.SelectedItem.ToString(); //記錄選擇的計算機名稱
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (intport != 0)                           //判讀是否有可用端口號
            {
                if (listView1.Items.Count > 0)
                {
                    for (int i = 0; i < listView1.Items.Count; i++)
                    {
                        //判斷掃描到的端口號是否與列表中的重復
                        if (listView1.Items[i].Text != intport.ToString())
                        {
                            //向列表中添加掃描到的已用端口號
                            listView1.Items.Add(intport.ToString());
                        }
                    }
                }
                else
                {
                    //向列表匯總添加掃描到的已用端口號
                    listView1.Items.Add(intport.ToString());
                }
                intport = 0;
            }
            if (progressBar1.Value < progressBar1.Maximum)  //判斷進度條的當前值是否超出其最大值
            {
                progressBar1.Value += 1;                    //將進度條的值加1
            }
            if (intflag == Convert.ToInt32(textBox2.Text))  //判斷正在掃描的端口號是否是結束端口號
            {
                timer1.Stop();                              //停止運行計時器
                button1.Text = "掃描";                      //設置按鈕文本為掃描
                MessageBox.Show("端口掃描結束！");
            }
        }

        /// <summary>
        /// 掃描端口號
        /// </summary>
        private void StartScan()
        {
            while (true)
            {
                for (int i = intstart; i <= intend; i++)
                {
                    intflag = i;                            //記錄正在掃描的端口號
                    try
                    {
                        TClient = new TcpClient(strName, i);//使用記錄的計算機名稱和端口號實例化偵聽對象
                        intport = i;                        //記錄已分配的端口號
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }
    }
}

