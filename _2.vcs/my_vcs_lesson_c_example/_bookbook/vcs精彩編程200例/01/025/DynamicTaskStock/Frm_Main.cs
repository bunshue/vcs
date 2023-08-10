using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net.Sockets;
using System.Threading;
using System.IO;
using System.Net;

namespace DynamicTaskStock
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }
        private Thread td;//創建一個線程
        private TcpListener tcpListener;//實例化偵聽對象
        string message = "";//記錄傳輸的內容
        private void StartListen()
        {
            tcpListener = new TcpListener(888);//創建TcpListener實例
            tcpListener.Start();//開始監聽
            while (true)
            {
                TcpClient tclient = tcpListener.AcceptTcpClient();//接受連接請求
                NetworkStream nstream = tclient.GetStream();//獲取數據流
                byte[] mbyte = new byte[1024];//建立緩存
                int i = nstream.Read(mbyte, 0, mbyte.Length);//將數據流寫入緩存
                message = Encoding.Default.GetString(mbyte, 0, i);//獲取傳輸的內容
            }
        }
        private void Frm_Main_Load(object sender, EventArgs e)
        {
            td = new Thread(new ThreadStart(this.StartListen));//通過線程調用StartListen方法
            td.Start();//開始運行線程
        }

        private void Frm_Main_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (this.tcpListener != null)
            {
                tcpListener.Stop();//停止偵聽對象
            }
            if (td != null)
            {
                if (td.ThreadState == ThreadState.Running)//判斷線程是否運行
                {
                    td.Abort();//終止線程
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                IPAddress[] ip = Dns.GetHostAddresses(Dns.GetHostName());//獲取本機地址
                string message = "你好兄弟";//傳輸的內容
                TcpClient client = new TcpClient(txtAdd.Text, 888);//創建TcpClient實例
                NetworkStream netstream = client.GetStream();//創建NetworkStream實例
                StreamWriter wstream = new StreamWriter(netstream, Encoding.Default);//創建StreamWriter實例
                wstream.Write(message);//將信息寫入流
                wstream.Flush();
                wstream.Close();//關閉流
                client.Close();//關閉TcpClient對象
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        bool k = true;//一個標記，用于控制圖標閃動
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (message.Length > 0)//如果網絡中傳輸了數據
            {
                if (k)//k為true時
                {
                    notifyIcon1.Icon = Properties.Resources._1;//托盤圖標為1
                    k = false;//設k為false
                }
                else//k為false時
                {
                    notifyIcon1.Icon = Properties.Resources._2;//圖盤圖標為2，透明的圖標
                    k = true;//k為true
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            message = "";//清空傳輸內容
            notifyIcon1.Icon = Properties.Resources._3;//初始化顯示的圖標
        }
    }
}