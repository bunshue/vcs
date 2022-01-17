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

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            UdpClient C = new UdpClient();
            IPEndPoint EP = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 2019);//應為伺服端程式所在之IP
            C.Connect(EP);
            byte[] B = Encoding.Default.GetBytes(textBox1.Text);              //詢問的內容轉為byte陣列
            C.Send(B, B.Length);                                              //送出問題
            byte[] R = C.Receive(ref EP);                                     //原路接收訊息
            textBox2.Text = Encoding.Default.GetString(R);                    //接收到的byte轉為文字
        }
    }
}

