using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;         //匯入網路通訊協定相關函數
using System.Net.Sockets; //匯入網路插座功能函數
using System.Threading;   //匯入多執行緒功能函數
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Thread Th;//網路監聽執行緒

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            Th = new Thread(Listen); //建立監聽執行緒
            Th.IsBackground = true;  //設定為背景執行緒
            Th.Start();              //開始監聽
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Th.Abort();//關閉執行緒
        }

        //伺服端監聽程式
        private void Listen()
        {
            UdpClient U = new UdpClient(2019);
            //int cnt = 0;
            while (true)
            {
                //cnt++;
                //this.Text = cnt.ToString();
                richTextBox1.Text += "A1";
                IPEndPoint EP = new IPEndPoint(IPAddress.Any, 2019); //建立監聽端點資訊(接收任何IP)
                richTextBox1.Text += "A2";
                byte[] B = U.Receive(ref EP);
                string A = Encoding.Default.GetString(B);            //翻譯資訊為字串
                string M = "Unknown Command";
                richTextBox1.Text += "A3";
                if (A == "Time?")
                {
                    M = DateTime.Now.ToString();
                }
                richTextBox1.Text += "A4";
                B = Encoding.Default.GetBytes(M);
                U.Send(B, B.Length, EP);                             //回應詢問資料(循原路回去)
                richTextBox1.Text += "A5";
            }
        }
    }
}
