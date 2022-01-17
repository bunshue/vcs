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
using System.Threading;   //匯入多執行緒功能函
using Microsoft.VisualBasic.PowerPacks;//匯入VB向量繪圖功能

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Socket T;    //通訊物件
        Thread Th;  //網路監聽執行緒 
        string User;//使用者 
        ShapeContainer CVS; //畫布物件(棋盤)
        byte[,] S;        //對應棋盤狀態的陣列：0為空格，1為黑子，2為白子

        public Form1()
        {
            InitializeComponent();
        }

        //繪製棋盤與加入畫布 
        private void Form1_Load(object sender, EventArgs e)
        {
            Bitmap bg = new Bitmap(570, 570);          //棋盤影像物件
            Graphics g = Graphics.FromImage(bg);       //棋盤影像繪圖物件
            g.Clear(Color.White);                      //設白色為背景色
            for (int i = 15; i <= 555; i += 30)
            {
                g.DrawLine(Pens.Black, i, 15, i, 555);
            }//畫19條垂直線
            for (int j = 15; j <= 555; j += 30)
            {
                g.DrawLine(Pens.Black, 15, j, 555, j);
            }//畫19條水平線
            panel1.BackgroundImage = bg;               //貼上棋盤影像為panel1的背景
            CVS = new ShapeContainer();                //宣告畫布物件
            panel1.Controls.Add(CVS);                  //畫布物件加入panel1
            S = new byte[19, 19];                      //宣告棋盤資訊陣列 
        }

        //登入伺服器 
        private void button1_Click(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false; //忽略跨執行緒操作的錯誤
            User = textBox3.Text;                            //使用者名稱
            string IP = textBox1.Text;                       //伺服器IP
            int Port = int.Parse(textBox2.Text);             //伺服器Port 
            try
            {
                IPEndPoint EP = new IPEndPoint(IPAddress.Parse(IP), Port);//建立伺服器端點資訊
                //建立TCP通訊物件
                T = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                T.Connect(EP);           //連上Server的EP端點(類似撥號連線)
                Th = new Thread(Listen); //建立監聽執行緒
                Th.IsBackground = true;  //設定為背景執行緒
                Th.Start();              //開始監聽
                textBox4.Text = "已連線伺服器！" + "\r\n"; Send("0" + User);//隨即傳送自己的 UserName 給 Server
                button1.Enabled = false; //讓連線按鍵失效，避免重複連線
            }
            catch
            {
                textBox4.Text = "無法連上伺服器！" + "\r\n";//連線失敗時顯示訊息 
            }
        }

        //清除重玩按鍵 
        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex >= 0)
            {
                Send("5" + "C" + "|" + listBox1.SelectedItem);//送出清除訊息給對手
            }
            CVS.Shapes.Clear();                               //清除棋子
            S = new byte[19, 19];                             //清除棋盤資訊
            panel1.Enabled = true;                            //開放任一方下棋 
        }

        //傳送訊息給 Server(Send Message to the Server)
        private void Send(string Str)
        {
            byte[] B = Encoding.Default.GetBytes(Str);//翻譯字串Str為Byte陣列B
            T.Send(B, 0, B.Length, SocketFlags.None); //使用連線物件傳送資料
        }

        //監聽 Server 訊息 (Listening to the Server)
        private void Listen()
        {
            EndPoint ServerEP = (EndPoint)T.RemoteEndPoint;  //Server 的 EndPoint
            byte[] B = new byte[1023];                       //接收用的 byte 陣列
            int inLen = 0;                                   //接收的位元組數目
            string Msg;                                      //接收到的完整訊息
            string St;                                       //命令碼
            string Str;                                      //訊息內容(不含命令碼)
            while (true)                                     //無限次監聽迴圈
            {
                try
                {
                    inLen = T.ReceiveFrom(B, ref ServerEP);    //收聽資訊並取得位元組數
                }
                catch (Exception)
                {
                    T.Close();                                 //關閉通訊器
                    listBox1.Items.Clear();                    //清除線上名單
                    MessageBox.Show("伺服器斷線了！");         //顯示斷線
                    button1.Enabled = true;                    //連線按鍵恢復可用
                    Th.Abort();                                //刪除執行緒
                }
                Msg = Encoding.Default.GetString(B, 0, inLen); //解讀完整訊息
                St = Msg.Substring(0, 1);                      //取出命令碼 (第一個字)
                Str = Msg.Substring(1);                        //取出命令碼之後的訊息
                switch (St)                                    //依命令碼執行功能
                {
                    case "L":                                  //接收線上名單
                        listBox1.Items.Clear();                //清除名單
                        string[] M = Str.Split(',');           //拆解名單成陣列
                        for (int i = 0; i < M.Length; i++) listBox1.Items.Add(M[i]); //加入名單
                        break;
                    case "5":                        //清棋盤訊息
                        CVS.Shapes.Clear();          //清除棋子
                        S = new byte[19, 19];        //清除棋盤資訊
                        panel1.Enabled = true;       //開放任一方下棋
                        break;
                    case "6":                        //對手下棋訊息
                        string[] D = Str.Split(','); //切割座標訊息
                        int x = int.Parse(D[0]);     //水平向的棋格
                        int y = int.Parse(D[1]);     //垂直向的棋格
                        Chess(x, y, Color.White);    //畫白子
                        S[x, y] = 2;                 //記為白子
                        panel1.Enabled = true;       //對手下好了，輪到你下棋
                        if (chk5(x, y, 2))
                        {
                            MessageBox.Show("你輸了！");//檢查對手是否五連線了？
                        }
                        break;
                }
            }
        }

        //畫棋子的副程序
        private void Chess(int i, int j, Color BW)
        {
            OvalShape C = new OvalShape(); //建立一個圓形的Shape物件
            C.Width = 26;                  //寬度(略小於棋格)
            C.Height = 26;                 //高度
            C.Left = i * 30 + 2;           //左邊座標
            C.Top = j * 30 + 2;            //頂部座標
            C.FillStyle = FillStyle.Solid; //實心填滿
            C.FillColor = BW;              //填黑或白色
            C.Parent = CVS;                //將圓形Shape加入畫布(棋盤)
        }

        //下棋的動作 
        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            int i = e.X / 30;             //算出是第幾個水平向的棋格
            int j = e.Y / 30;             //算出是第幾個垂直向的棋格
            if (S[i, j] == 0)
            {
                Chess(i, j, Color.Black); //畫黑子
                S[i, j] = 1;              //記為黑子
                if (listBox1.SelectedIndex >= 0) //如果有對手時
                {
                    Send("6" + i.ToString() + "," + j.ToString() + "|" + listBox1.SelectedItem);
                    panel1.Enabled = false;     //輪到對手，你不能繼續下棋
                }
                if (chk5(i, j, 1))
                {
                    MessageBox.Show("你贏了！");
                }
            }
        }

        //檢查是否五連線的程式
        private bool chk5(int i, int j, byte tg)
        {
            int n = 0;                                       //連線棋子數目
            int ii, jj;                                      //檢查水平連線
            for (int k = -4; k <= 4; k++)
            {
                ii = i + k;
                if (ii >= 0 && ii < 19)                      //檢視其格在棋盤範圍內
                {
                    if (S[ii, j] == tg)                      //棋種正確
                    {
                        n += 1;                              //連線數加一
                        if (n == 5) return true;             //達到5連線回傳true
                    }
                    else
                    { n = 0; }                               //連線中斷，歸零重新計算 
                }
            }
            //檢查垂直連線
            n = 0;                                           //連線棋子數目歸零
            for (int k = -4; k <= 4; k++)
            {
                jj = j + k;
                if (jj >= 0 && jj < 19)                      //檢視棋格在棋盤範圍內
                {
                    if (S[i, jj] == tg)                      //棋種正確
                    {
                        n += 1;                              //連線數加一
                        if (n == 5) return true;             //達到5連線回傳true
                    }
                    else
                    { n = 0; }                               //連線中斷，歸零重新計算 
                }
            }
            //檢查左上到右下連線
            n = 0;                                           //連線棋子數目歸零
            for (int k = -4; k <= 4; k++)
            {
                ii = i + k; jj = j + k;
                if (ii >= 0 && ii < 19 && jj >= 0 && jj < 19)//檢視棋格範圍
                {
                    if (S[ii, jj] == tg)                     //棋種正確
                    {
                        n += 1;                              //連線數加一
                        if (n == 5) return true;             //達到5連線回傳true
                    }
                    else
                    { n = 0; }                               //連線中斷，歸零重新計算 
                }
            }
            //檢查右上到左下連線
            n = 0;                                           //連線棋子數目歸零
            for (int k = -4; k <= 4; k++)
            {
                ii = i - k; jj = j + k;
                if (ii >= 0 && ii < 19 && jj >= 0 && jj < 19)  //檢視棋格範圍
                {
                    if (S[ii, jj] == tg)                     //棋種正確
                    {
                        n += 1;                              //連線數加一
                        if (n == 5) return true;             //達到5連線回傳true
                    }
                    else
                    { n = 0; }                               //連線中斷，歸零重新計算 
                }
            }
            return false;                                    //未發現五子連線
        }

        //關閉視窗離線
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (button1.Enabled == false)
            {
                Send("9" + User); //傳送自己的離線訊息給伺服器
                T.Close();        //關閉網路通訊器
            }
        }
    }
}



