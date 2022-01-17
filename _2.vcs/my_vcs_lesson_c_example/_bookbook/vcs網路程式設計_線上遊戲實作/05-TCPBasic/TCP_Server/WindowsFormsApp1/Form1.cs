using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;         //匯入網路通訊協定相關函數
using System.Net.Sockets; //匯入網路插座功能函數
using System.Threading;   //匯入多執行緒功能函數
using System.Collections; //匯入集合物件

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        TcpListener Server;             //伺服端網路監聽器(相當於電話總機)
        Socket Client;                  //給客戶用的連線物件(相當於電話分機)
        Thread Th_Svr;                  //伺服器監聽用執行緒(電話總機開放中)
        Thread Th_Clt;                  //客戶用的通話執行緒(電話分機連線中)
        Hashtable HT = new Hashtable(); //客戶名稱與通訊物件的集合(雜湊表)(key:Name, Socket)
        //開啟 Server：用 Server Thread 來監聽 Client 
        private void button1_Click(object sender, EventArgs e)
        {
            //忽略跨執行緒處理的錯誤(允許跨執行緒存取變數)
            CheckForIllegalCrossThreadCalls = false;
            Th_Svr = new Thread(ServerSub);     //宣告監聽執行緒(副程式ServerSub)
            Th_Svr.IsBackground = true;         //設定為背景執行緒
            Th_Svr.Start();                     //啟動監聽執行緒
            button1.Enabled = false;            //讓按鍵無法使用(不能重複啟動伺服器) 
        }
        //接受客戶連線要求的程式(如同電話總機)，針對每一客戶會建立一個連線，以及獨立執行緒
        private void ServerSub()
        {
            //Server IP 和 Port
            IPEndPoint EP = new IPEndPoint(IPAddress.Parse(textBox1.Text), int.Parse(textBox2.Text));
            Server = new TcpListener(EP);       //建立伺服端監聽器(總機)
            Server.Start(100);                  //啟動監聽設定允許最多連線數100人
            while (true)                        //無限迴圈監聽連線要求
            {
                Client = Server.AcceptSocket(); //建立此客戶的連線物件Client
                Th_Clt = new Thread(Listen);    //建立監聽這個客戶連線的獨立執行緒
                Th_Clt.IsBackground = true;     //設定為背景執行緒
                Th_Clt.Start();                 //開始執行緒的運作
            }
        }
        //監聽客戶訊息的程式
        private void Listen()
        {
            Socket Sck = Client; //複製Client通訊物件到個別客戶專用物件Sck
            Thread Th = Th_Clt;  //複製執行緒Th_Clt到區域變數Th
            while (true)         //持續監聽客戶傳來的訊息
            {
                try                //用 Sck 來接收此客戶訊息，inLen 是接收訊息的 byte 數目
                {
                    byte[] B = new byte[1023];   //建立接收資料用的陣列，長度須大於可能的訊息
                    int inLen = Sck.Receive(B);  //接收網路資訊(byte陣列)
                    string Msg = Encoding.Default.GetString(B, 0, inLen); //翻譯實際訊息(長度inLen)
                    string Cmd = Msg.Substring(0, 1);                     //取出命令碼 (第一個字)
                    string Str = Msg.Substring(1);                        //取出命令碼之後的訊息
                    switch (Cmd)                                          //依據命令碼執行功能
                    {
                        case "0":                    //有新使用者上線：新增使用者到名單中
                            HT.Add(Str, Sck);        //連線加入雜湊表，Key:使用者，Value:連線物件(Socket)
                            listBox1.Items.Add(Str); //加入上線者名單
                            break;
                        case "9":
                            HT.Remove(Str);             //移除使用者名稱為Name的連線物件
                            listBox1.Items.Remove(Str); //自上線者名單移除Name
                            Th.Abort();                 //結束此客戶的監聽執行緒
                            break;
                    }
                }
                catch (Exception)
                {
                    //有錯誤時忽略，通常是客戶端無預警強制關閉程式，測試階段常發生
                }
            }
        }
        //關閉視窗時 
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread(); //關閉所有執行緒 
        }
    }
}
