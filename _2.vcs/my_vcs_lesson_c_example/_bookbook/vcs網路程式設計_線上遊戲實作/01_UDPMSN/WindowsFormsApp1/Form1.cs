using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;         //匯入網路通訊協定相關參數
using System.Net.Sockets; //匯入網路插座功能函數
using System.Threading;   //匯入多執行續功能函數
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        UdpClient U; //宣告UDP通訊物件
        Thread Th;   //宣告監聽用執行續

        public Form1()
        {
            InitializeComponent();
        }

        //表單載入
        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text += " " + MyIP();                              //顯示本機IP於標題列
        }

        //關閉監聽執行續(如果有的話)
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            try
            {
                Th.Abort(); //關閉監聽執行續
                U.Close();  //關閉監聽器
            }
            catch
            {
                //忽略錯誤，程式繼續執行
            }
        }

        //找出本機IP
        private string MyIP()
        {
            string hn = Dns.GetHostName();                          //取得本機電腦名稱
            IPAddress[] ip = Dns.GetHostEntry(hn).AddressList;      //取得本機IP陣列(可能有多個)
            foreach (IPAddress it in ip)                            //列舉各個IP
            {
                if (it.AddressFamily == AddressFamily.InterNetwork) //如果是IPv4格式
                {
                    return it.ToString();                           //傳回此IP字串
                }
            }
            return "";                                              //找不到合格IP，回傳空字串
        }

        //啟動監聽按鈕程序
        private void button1_Click(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行續錯誤
            Th = new Thread(Listen); //建立監聽執行續，目標副程序→Listen
            Th.Start(); //啟動監聽執行續
            button1.Enabled = false; //使按鍵失效，不能(也不需要)重複開啟監聽
        }

        //監聽副程序
        private void Listen()
        {
            int Port = int.Parse(textBox1.Text); //設定監聽用的通訊埠
            U = new UdpClient(Port);             //監聽UDP監聽器實體
            //建立本機端點資訊
            IPEndPoint EP = new IPEndPoint(IPAddress.Parse("127.0.0.1"), Port);
            while (true) //持續監聽的無限迴圈→有訊息(True)就處理，無訊息就等待！
            {
                byte[] B = U.Receive(ref EP);                  //訊息到達時讀取資訊到B陣列
                textBox2.Text = Encoding.Default.GetString(B); //翻譯B陣列為字串
            }
        }

        //發送UDP訊息
        private void button2_Click(object sender, EventArgs e)
        {
            string IP = textBox3.Text;                           //設定發送目標IP
            int Port = int.Parse(textBox4.Text);                 //設定發送目標Port
            byte[] B = Encoding.Default.GetBytes(textBox5.Text); //字串翻譯成位元組陣列
            UdpClient S = new UdpClient();                       //建立UDP通訊器
            S.Send(B, B.Length, IP, Port);                       //發送資料到指定位置
            S.Close();                                           //關閉通訊器
        }
    }
}
