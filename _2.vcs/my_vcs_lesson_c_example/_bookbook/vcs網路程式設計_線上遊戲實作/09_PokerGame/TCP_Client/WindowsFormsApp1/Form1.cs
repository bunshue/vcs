using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;          //匯入允許讀取和寫入文件和目錄函數
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
        //公用變數
        Socket T;                                    //通訊物件
        Thread Th;                                   //網路監聽執行緒
        string User;                                 //使用者
        bool run;                                    //控制主表單無限迴圈開關
        bool receive;                                //接收到訊號旗標
        string Mesg;                                 //接收到的公告訊號內容
        bool me;                                     //輪到自已出牌旗標
        string nextOne;                              //下一位出牌者
        string[] P7 = new string[8];                 //牌面出牌狀態
        List<PictureBox> Pk = new List<PictureBox>();//玩家手上的牌
        List<string> win = new List<string>();       //輸贏順位
        private void Form1_Load(object sender, EventArgs e)
        {
            this.Show();
            run = true;//開啟主表單監聽旗標
            while (run)
            {
                if (receive)//有訊息
                {
                    GetMessage();
                }
                Application.DoEvents();
            }
        }
        //主表單監聽到訊息後處理內容
        private void GetMessage()
        {
            string St = Mesg.Substring(0, 1);//命令碼
            string Str = Mesg.Substring(1);  //訊息內容(不含命令碼)
            switch (St)
            {
                case "A":          //發牌訊息
                    DealCards(Str);//新增牌面物件
                    break;
                case "B":          //出牌訊息
                    PlayCards(Str);//牌桌上顯示出牌狀態
                    break;
                case "C":                            //某玩家牌出完了
                    string[] winner = Str.Split('|');//出牌內容|出完牌的人
                    PlayCards(winner[0]);            //牌桌上顯示出牌狀態
                    WinCards(winner[1]);             //贏的玩家
                    break;
            }
        }
        //新增牌面物件
        private void DealCards(string S)
        {
            string[] F = S.Split('|');//全部的牌依玩家分發
            int nc = 0;               //每人收到牌數
            for (int i = 0; i < F.Length - 1; i++)
            {
                string[] U = F[i].Split(',');//玩家名稱,牌1,牌2...
                nc = U.Length - 1;           //每人收到牌數
                if (U[0] == User)            //是自己的牌
                {
                    for (int j = 1; j < U.Length; j++)//收到的牌
                    {   //牌的圖檔路徑
                        string fn1 = System.Environment.CurrentDirectory + "\\PokerCards\\" + U[j] + ".png";
                        PictureBox Pc = new PictureBox();             //宣告一個新的PictureBox物件
                        Pc.Name = "P" + j.ToString();                 //物件名稱
                        Pc.Tag = U[j];                                //牌面(花色+號碼)
                        Pc.Size = new Size(100, 140);                 //物件大小
                        Pc.SizeMode = PictureBoxSizeMode.StretchImage;//圖片顯示模式，圖片延伸符合PictureBox大小
                        Pc.Left = (j - 1) * 20;                       //圖片左邊位置
                        Pc.Top = label6.Bottom + 20;                  //圖片上邊位置
                        Pc.Image = Image.FromFile(fn1);               //圖片路徑來源
                        Pc.MouseDown += new MouseEventHandler(PictureBox_MouseDown);//加入事件副程式(滑鼠按到牌面上的延伸動作)
                        this.Controls.Add(Pc);                        //把圖片加入Form1裡
                        Pc.BringToFront();                            //移到上一層
                        Pk.Add(Pc);                                   //把圖加入物件陣列(玩家手上的牌)                            
                    }
                }
            }
            label6.Text = "剩餘牌數：" + nc.ToString();
            button2.Enabled = false;                           //不能重複發牌
            for (int i = 0; i < listBox1.Items.Count - 1; i++) //依listBox1名單決定出牌順序
            {
                if (User == listBox1.Items[i].ToString())
                {
                    nextOne = listBox1.Items[i + 1].ToString();//決定下一位出牌者
                    break;
                }
            }
            if (User == listBox1.Items[listBox1.Items.Count - 1].ToString())
                nextOne = listBox1.Items[0].ToString();
            receive = false; Mesg = "";                       //清空訊息,關閉收到訊息旗標
        }
        //牌桌上顯示出牌狀態
        private void PlayCards(string S)
        {
            int n = int.Parse(S.Substring(2));//出牌的數字
            string m = S.Substring(0, 2);     //出牌的花色
            string fn2 = System.Environment.CurrentDirectory + "\\PokerCards\\" + S + ".png";//此牌的圖檔路徑
            if (n == 7)//牌面數字7
            {
                for (int i = 0; i <= 6; i += 2)
                {
                    if (P7[i] == null)
                    {
                        P7[i] = S;    //出牌內容紀錄在陣列裡
                        P7[i + 1] = S;
                        //取得表單內pictureBox物件
                        PictureBox P1 = this.Controls.Find("pictureBox" + (i + 1).ToString(), false).FirstOrDefault() as PictureBox;
                        PictureBox P2 = this.Controls.Find("pictureBox" + (i + 2).ToString(), false).FirstOrDefault() as PictureBox;
                        P1.Image = Image.FromFile(fn2);
                        P2.Image = Image.FromFile(fn2);
                        break;
                    }
                }
            }
            else
            {   //其它非7的牌面數字
                for (int i = 0; i <= 6; i += 2)
                {
                    if (P7[i] == null) continue;                 //牌桌上空的
                    int nmax = int.Parse(P7[i].Substring(2));    //牌桌上上排數字
                    int nmin = int.Parse(P7[i + 1].Substring(2));//牌桌上下排數字
                    string mm = P7[i].Substring(0, 2);           //牌桌上花色
                    if (m != mm) continue;//花色不同
                    if (n == nmax + 1)    //牌面數字增加
                    {
                        P7[i] = S;
                        PictureBox P1 = this.Controls.Find("pictureBox" + (i + 1).ToString(), false).FirstOrDefault() as PictureBox;
                        P1.Image = Image.FromFile(fn2);
                        break;
                    }
                    else if (n == nmin - 1)//牌面數字減少
                    {
                        P7[i + 1] = S;
                        PictureBox P2 = this.Controls.Find("pictureBox" + (i + 2).ToString(), false).FirstOrDefault() as PictureBox;
                        P2.Image = Image.FromFile(fn2);
                        break;
                    }
                }
            }
            receive = false; Mesg = ""; //清空訊息,關閉收到訊息旗標
        }
        //玩家贏牌
        private void WinCards(string S)
        {
            win.Add(S);//贏的玩家
            listBox2.Items.Add("第" + win.Count.ToString() + "名:" + S);
            if (win.Count == 3)//第3名牌出完(遊戲結束)
            {
                textBox4.Text = "遊戲結束!";
                me = false;
                button3.Enabled = false;
            }
            else
            {   //從新決定下一位出牌者
                nextOne = "";
                int meid = -1;//自己在名單上的索引位置
                for (int i = 0; i < listBox1.Items.Count; i++)
                {
                    if (listBox1.Items[i].ToString() == User)
                    {
                        meid = i; break;
                    }
                }
                int nextid = meid + 1;                              //下一位出牌者在名單上的索引位置
                if (nextid == listBox1.Items.Count) nextid = 0;
                while (nextid != meid)
                {
                    bool ck = false;                                //是否在贏的名單上
                    nextOne = listBox1.Items[nextid].ToString();    //下一位玩家
                    for (int i = 0; i < win.Count; i++)             //贏的玩家名單
                    {
                        if (nextOne == win[i]) { ck = true; break; }//此玩家已經贏了
                    }
                    if (ck == false) break;                         //此玩家尚未出完牌
                                                                    //此玩家已經贏了找下一位
                    if (nextid < listBox1.Items.Count - 1)
                        nextid += 1;
                    else
                        nextid = 0;
                }
            }
            receive = false; Mesg = "";                             //清空訊息,關閉收到訊息旗標
        }
        //出牌前判定規則出牌
        private bool Rules(PictureBox Pc)
        {
            int n = int.Parse(Pc.Tag.ToString().Substring(2));//出牌的數字
            string m = Pc.Tag.ToString().Substring(0, 2);     //出牌的花色
            if (n == 7)
            {
                return true;
            }
            else
            {
                for (int i = 0; i <= 6; i += 2)
                {
                    if (P7[i] == null) continue;                 //沒牌跳過
                    int nmax = int.Parse(P7[i].Substring(2));    //牌桌上上排數字
                    int nmin = int.Parse(P7[i + 1].Substring(2));//牌桌上下排數字
                    string mm = P7[i].Substring(0, 2);           //牌面上花色
                    if (m != mm) continue;                       //花色不同
                    if (n == nmax + 1)
                    {
                        return true;
                    }
                    else if (n == nmin - 1)
                    {
                        return true;
                    }
                }
            }
            return false;//出牌錯誤
        }
        //出牌事件副程式
        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (me == false) return;                         //不能出牌
            PictureBox Pc = (PictureBox)sender;              //被選到的牌
            if (e.Button == MouseButtons.Left)               //選牌
            {
                //其它牌回原位
                for (int i = 0; i < Pk.Count; i++)
                {
                    PictureBox P0 = Pk[i];
                    P0.Top = label6.Bottom + 20;
                }
                Pc.Top = label6.Bottom;                       //選中的牌上移位置
            }
            else if (e.Button == MouseButtons.Right)          //出牌
            {
                if (Rules(Pc) == false) return;               //規則判斷
                if (Pk.Count > 1)                             //剩多於1張牌
                {
                    Send("1" + "B" + Pc.Tag);                 //送出出牌訊息(1=廣播,B=出牌)
                    Send("2" + "輪到你出牌!" + "|" + nextOne);//送出私人訊息給下一位出牌者(2=私訊)
                    textBox4.Text = "等待...";
                }
                else
                {   //剩1張牌，我贏了
                    Send("1" + "C" + Pc.Tag + "|" + User);    //送出出牌訊息(1=廣播,C=牌出完了)
                    if (win.Count < 2) Send("2" + "輪到你出牌!" + "|" + nextOne);//前2名需送出私人訊息給下一位出牌者
                    textBox4.Text = "結束遊戲!";
                }
                for (int i = 0; i < Pk.Count; i++)            //刪除自己手上的牌
                {
                    PictureBox P0 = Pk[i];
                    if (P0.Name == Pc.Name)
                    {
                        Pk.RemoveAt(i);//刪除已出的牌
                        Pc.Dispose();  //刪除物件
                        break;
                    }
                }
                label6.Text = "剩餘牌數：" + Pk.Count.ToString();
                me = false;             //關閉出牌旗標
                button3.Enabled = false;//關閉跳過按鍵
            }
        }
        //發牌
        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.Items.Count != 4) { MessageBox.Show("遊戲需要4人參加!"); return; }
            List<string> myList = new List<string>();         //資料夾內所有圖檔路徑清單
            //取得執行檔目錄下的PorkerCards資料夾路徑
            string folderName = System.Environment.CurrentDirectory + "\\PokerCards";
            foreach (string fname in System.IO.Directory.GetFiles(folderName))
            {
                myList.Add(fname);//資料夾內所有檔案路徑加入清單
            }
            //隨機發牌
            List<string> ranList = new List<string>();//隨機發牌圖檔路徑清單
            Random ran = new Random();
            while (myList.Count > 0)
            {
                int RandKey = ran.Next(0, myList.Count - 1);//從0~myList.Count - 1裡隨機產生數字
                string s = myList[RandKey];                 //數字對應到myList清單裡圖檔路徑
                ranList.Add(s);                             //把路徑加入ranList隨機清單裡
                myList.RemoveAt(RandKey);                   //移除原有清單裡的路徑
            }
            int m = 52 / 4;     //每人擁有牌數
            int mn = 0;         //每人發牌計數
            int Pid = -1;       //listBox1裡索引直
            string sendC = "";  //發牌內容
            for (int i = 0; i < 52; i++)//52張牌迴圈
            {

                string[] Ps = ranList[i].Split('\\');       //切割檔案路徑
                string[] Pn = Ps[Ps.Length - 1].Split('.'); //切割檔名與副檔名(例：梅花1.png)
                mn++;
                if (mn == 1 || mn > m)//每個玩家拿到第一張牌
                {
                    mn = 1; Pid += 1;
                    string player = listBox1.Items[Pid].ToString();//依listBox1裡名單順序發牌
                    sendC += player + "," + Pn[0] + ",";//(例：玩家,牌1)
                }
                else
                {
                    if (mn < m) sendC += Pn[0] + ",";  //串接發牌內容(例：玩家,牌1,牌2...)
                    if (mn == m) sendC += Pn[0] + "|"; //已達一個玩家的牌數，用"|"分割下一位玩家
                }
            }
            Send("1" + "A" + sendC);                   //送發牌訊息給所有人(1=廣播,A=發牌)
            me = true;                                 //由發牌者第1位出牌
            textBox4.Text = "輪到你出牌!";             //提醒出牌
            button3.Enabled = true;                    //開啟跳過按鍵
        }
        //跳過
        private void button3_Click(object sender, EventArgs e)
        {
            Send("2" + "輪到你出牌!" + "|" + nextOne);//送出私人訊息給下一位出牌者
            textBox4.Text = "等待...";
            button3.Enabled = false;
        }
        //登入伺服器
        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox3.Text == "") { MessageBox.Show("請輸入玩家名稱"); return; }
            Control.CheckForIllegalCrossThreadCalls = false; //忽略跨執行緒操作的錯誤
            User = textBox3.Text;                            //使用者名稱
            string IP = textBox1.Text;                       //伺服器IP
            int Port = int.Parse(textBox2.Text);             //伺服器Port
            try
            {
                IPEndPoint EP = new IPEndPoint(IPAddress.Parse(IP), Port);          //建立伺服器端點資訊
                //建立TCP通訊物件
                T = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                T.Connect(EP);           //連上Server的EP端點(類似撥號連線)
                Th = new Thread(Listen); //建立監聽執行緒
                Th.IsBackground = true;  //設定為背景執行緒
                Th.Start();              //開始監聽
                textBox4.Text = "已連線伺服器！" + "\r\n";
                Send("0" + User);        //隨即傳送自己的 UserName 給 Server
                button1.Enabled = false; //讓連線按鍵失效，避免重複連線
            }
            catch
            {
                textBox4.Text = "無法連上伺服器！" + "\r\n";  //連線失敗時顯示訊息
            }
        }
        //傳送訊息給 Server
        private void Send(string Str)
        {
            byte[] B = Encoding.Default.GetBytes(Str); //翻譯文字成Byte陣列
            T.Send(B, 0, B.Length, SocketFlags.None);  //傳送訊息給伺服器
        }
        //監聽 Server 訊息 (Listening to the Server)
        private void Listen()
        {
            EndPoint ServerEP = (EndPoint)T.RemoteEndPoint; //Server 的 EndPoint
            byte[] B = new byte[1023];                      //接收用的 Byte 陣列
            int inLen = 0;                                  //接收的位元組數目
            string Msg;                                     //接收到的完整訊息
            string St;                                      //命令碼
            string Str;                                     //訊息內容(不含命令碼)
            while (true)                                    //無限次監聽迴圈
            {
                try
                {
                    inLen = T.ReceiveFrom(B, ref ServerEP); //收聽資訊並取得位元組數
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
                        for (int i = 0; i < M.Length; i++) listBox1.Items.Add(M[i]);//加入名單
                        break;
                    case "1":                                  //接收廣播訊息
                        Mesg = Str;                            //訊息複製到公用變數
                        receive = true;                        //開啟收到訊息旗標
                        break;
                    case "2":                                  //接收私人訊息
                        textBox4.Text = Str;                   //接收訊息內容
                        me = true;                             //輪到我出牌
                        button3.Enabled = true;                //開啟跳過按鍵
                        break;
                }
            }
        }
        //關閉表單
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (button1.Enabled == false)
            {
                Send("9" + User);//傳送自己的離線訊息給伺服器
                T.Close();       //關閉網路通訊器
            }
            run = false;         //關閉主表單監聽旗標
            Application.DoEvents();
        }
    }
}
