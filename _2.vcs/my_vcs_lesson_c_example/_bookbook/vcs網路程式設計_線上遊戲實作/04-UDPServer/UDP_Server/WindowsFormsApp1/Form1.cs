using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading.Tasks;
using System.Net;         //匯入網路通訊協定相關函數
using System.Net.Sockets; //匯入網路插座功能函數
using System.Threading;   //匯入多執行緒功能函數

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Thread Th;//網路監聽執行緒                               
        private void Form1_Load(object sender, EventArgs e)
        {
            Th = new Thread(Listen); //建立監聽執行緒
            Th.IsBackground = true;  //設定為背景執行緒
            Th.Start();              //開始監聽
        }

        //伺服端監聽程式
        private void Listen()
        {
            UdpClient U = new UdpClient(2019);
            while (true)
            {
                IPEndPoint EP = new IPEndPoint(IPAddress.Any, 2019); //建立監聽端點資訊(接收任何IP)
                byte[] B = U.Receive(ref EP);
                string A = Encoding.Default.GetString(B);            //翻譯資訊為字串
                string M = "Unknown Command";
                if (A == "Time?")
                {
                    M = DateTime.Now.ToString();
                }
                B = Encoding.Default.GetBytes(M);
                U.Send(B, B.Length, EP);                             //回應詢問資料(循原路回去)
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Th.Abort();//關閉執行緒
        }
    }
}
