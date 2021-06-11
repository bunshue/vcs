using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.Windows;

using System.Net;
using System.Net.Sockets; //ServerSocket = new Socket(...)時使用
using System.Threading;  //Thread時使用
using System.Text;       //Encoding.Unicode.GetString(...) 時使用
using System.IO;         //使用FileInfo類別，來建立一個檔案實體物件


namespace _server
{
    public partial class Form1 : System.Windows.Forms.Form
    {

        private Socket ServerSocket, SocketForClient;
        private Thread _thread1, _thread2;
        private Hashtable ht = new Hashtable();
        private Hashtable name_score = new Hashtable(); // 使用hashtable 來記錄client-socket 的資訊
        //注意：後面這個= new Hashtable(); --- 不可以省略
        private Hashtable htname = new Hashtable(); //記錄登錄名稱
        string[] temp = new string[1024];
        string[] tempscore = new string[1024];
        delegate void mydel(string str);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            //清除資源
            try
            {
                --c_conn; //上線人數減一
                Show_label2(); //Show label2內容 = 上線人數
                _thread1.Abort();
                _thread2.Abort();
                ServerSocket.Shutdown(SocketShutdown.Both);
                ServerSocket.Close();
                SocketForClient.Shutdown(SocketShutdown.Both);
                SocketForClient.Close();
                Application.Exit();
            }
            catch
            {
                --c_conn;
                Show_label2();
                Application.Exit();

            }
            Application.Exit();

            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }
        private void Show_textBox1()//此副程式為了避免跨執行緒錯誤
        {
            if (textBox1.InvokeRequired)
            {
                label3.Invoke(new MethodInvoker(Show_textBox1));
            }
            else
            {

                textBox1.Text = "";
                textBox1.ReadOnly = false;
            }
        }
        private void Show_button1()//此副程式為了避免跨執行緒錯誤
        {
            if (button1.InvokeRequired)
            {
                button1.Invoke(new MethodInvoker(Show_button1));
            }
            else
            {


                button1.Enabled = false;
            }
        }
        int c_conn = 0;
        private void MainService() //這個副程式，將會偵測是否有Client端用戶目前已經連線了
        {

            try
            {
                IPEndPoint serverhost = new IPEndPoint(IPAddress.Parse(textBox1.Text), 233);
                ServerSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                ServerSocket.Bind(serverhost);
                ServerSocket.Listen(50); //設定暫止連接佇列的長度為50	
                MessageBox.Show("伺服器啟動 !", "伺服器");
                Show_button1();
                while (true)  //無限迴圈檢查連線的Client的Socket資訊
                {

                    //如果主機socket偵聽到client的資訊，就記錄其SocketForClient資料
                    // ****** 兩種寫法皆可 *******************************
                    SocketForClient = ServerSocket.Accept();
                    ++c_conn;
                    ht.Add(SocketForClient.RemoteEndPoint, SocketForClient);
                    Show_label2();



                    //Socket s = ServerSocket.Accept();
                    //SocketForClient = s;
                    // *************************************

                    //使用執行緒來偵測該client端的socket是否有傳遞資料過來
                    _thread2 = new Thread(new ThreadStart(ClientService)); //不同Socket連線進入者都會開啟一個thread
                    _thread2.Start();

                    Thread.Sleep(200); //等待傳值給thread中的變數，防止多用戶造成衝突				
                }
            }

            catch
            {
                MessageBox.Show("IP錯誤，請重新輸入！", "伺服器");
                Show_textBox1();
                button1.Enabled = true;
            }

        }
        private void Show_label2()
        {
            if (label2.InvokeRequired)
            {
                label2.Invoke(new MethodInvoker(Show_label2));
                //richTextBox1.Text += "aaaaaaa\n";
            }
            else
            {
                label2.Text = c_conn.ToString();
                //richTextBox1.Text += "bbbbbbb\n";
            }
        }
        private void Show_label3_1()
        {
            if (label3.InvokeRequired) label3.Invoke(new MethodInvoker(Show_label3_1));
            else
            {

                label3.Text = "";
            }
        }
        private void Show_label3(string str)
        {

            mydel a = Show_label3;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if (label3.InvokeRequired) this.Invoke(a, obj);
            else this.label3.Text = label3.Text + (string)obj[0] + "\n";

        }
        private void ClientService() //這個副程式，乃是無限迴圈中偵測是否有Client傳送訊息
        {
            // *********************************************
            // *******關鍵步驟*****************************
            //   因為下面while()....裡面在會一直偵測client端所傳來的訊息
            //   如果寫成SocketForClient.ReceiveFrom(...), 那麼只會有一組最後連線上的SocketForClient可以保持暢通連線，那麼其它的client都無法使用這個被使用中的SocketForClient了
            //   所以正確的寫法是先在while()外面先宣告Socket sock = SocketForClient，然後在while(..)內完全使用這個暫時的變數sock，那麼就不會有被佔用的SocketForClient這個問題了
            Socket sock = SocketForClient;
            // *********************************************
            // *********************************************
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];


            EndPoint oldEP = sock.RemoteEndPoint;
            int ii, six = 0, off_line = 0, name = 0, count_temp = 0, count_score = 0;
            string strAll = "";

            Socket socketTemp;

            while (true)
            {
                //ii = SocketForClient.ReceiveFrom(byteReceieve,ref oldEP);
                //ii = sock.ReceiveFrom(byteReceieve, 0, byteReceieve.Length, SocketFlags.None, ref oldEP);//使用指定的 SocketFlags，
                //接收指定位元組數目的資料至資料緩衝區的指定位置，並儲存端點。 
                try
                {
                    // ii = SocketForClient.Receive(byteReceieve);
                    ii = sock.ReceiveFrom(byteReceieve, 0, byteReceieve.Length, SocketFlags.None, ref oldEP);//使用指定的 SocketFlags，
                    strAll = Encoding.Unicode.GetString(byteReceieve, 0, ii);


                    if (strAll == "disconnect") off_line = 1;

                    if ((off_line == 1))//off_line = 1 表示有人斷線  
                    {
                        if ((strAll != "disconnect") && (strAll != ""))
                        {
                            --c_conn;

                            htname.Remove(strAll);//移除hashtable裡有收到此字串的東西
                            ht.Remove(sock.RemoteEndPoint);
                            byteSend = Encoding.Unicode.GetBytes("disconnect".ToCharArray());
                            foreach (DictionaryEntry dc in ht)//傳給每一個client
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                            Thread.Sleep(50);
                            byteSend = Encoding.Unicode.GetBytes(c_conn.ToString().ToCharArray());//將c_conn整數變數轉成字串後再轉成陣列形式存給byteSend
                            foreach (DictionaryEntry dc in ht)//傳給每一個client
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                            Thread.Sleep(50);
                            byteSend = Encoding.Unicode.GetBytes("Disconnect".ToCharArray());
                            foreach (DictionaryEntry dc in ht)//傳給每一個client
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                            Thread.Sleep(50);
                            byteSend = Encoding.Unicode.GetBytes(strAll.ToCharArray());
                            foreach (DictionaryEntry dc in ht)//傳給每一個client
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                            Show_label3_1();
                            foreach (DictionaryEntry de in htname)
                            {

                                Show_label3((string)de.Key);
                            }
                            Show_label2();

                            off_line = 0;
                        }
                    }

                    else  // 有人進來時
                    {


                        if (strAll == "six")
                        {
                            six = 1;
                            byteSend = Encoding.Unicode.GetBytes("six".ToCharArray());//將six字串轉成陣列形式存給byteSend
                            foreach (DictionaryEntry dc in ht)//傳給每一個client
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                        }
                        if (six == 1)
                        {
                            if ((strAll != "") && (strAll != "six") && (strAll != "name"))
                            {
                                name_score.Add(strAll, null);//把收到的字串存入hashtable裡面

                                foreach (DictionaryEntry de in name_score)   //把上線者的名稱暫存在temp裡面
                                {

                                    tempscore[count_score] = (string)de.Key;
                                    ++count_score;
                                }
                                Thread.Sleep(50);
                                if (count_score == c_conn)
                                {
                                    for (int i = 0; i < c_conn; ++i)
                                    {
                                        byteSend = Encoding.Unicode.GetBytes("six".ToCharArray());//將six字串轉成陣列形式存給byteSend
                                        foreach (DictionaryEntry dc in ht)//傳給每一個client
                                        {

                                            socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                            socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                                        }
                                        Thread.Sleep(50);

                                        byteSend = Encoding.Unicode.GetBytes(tempscore[i].ToCharArray()); //將tempscore[i]轉成陣列形式存給byteSend
                                        foreach (DictionaryEntry dc in ht)//傳給每一個client
                                        {

                                            socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                            socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                                        }
                                        Thread.Sleep(50);
                                    }

                                    for (int i = 0; i < c_conn; ++i)
                                    {
                                        name_score.Remove(tempscore[i]);
                                        tempscore[i] = null;
                                    }

                                    count_score = 0;
                                }
                                six = 0;
                            }
                        }

                        if (strAll == "name")
                        {
                            name = 1;

                            byteSend = Encoding.Unicode.GetBytes("c_conn".ToCharArray()); //將c_conn轉成陣列形式存給byteSend
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                            byteSend = Encoding.Unicode.GetBytes(c_conn.ToString().ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                            Thread.Sleep(50);

                        }
                        if ((name == 1) && (strAll != "name") && (strAll != ""))
                        {

                            htname.Add(strAll, SocketForClient);
                            Show_label3((string)strAll);
                            Show_label2();
                            foreach (DictionaryEntry de in htname)   //把上限者的名稱暫存在temp裡面
                            {

                                temp[count_temp] = (string)de.Key;
                                ++count_temp;
                            }
                            Thread.Sleep(50);

                            for (int i = 0; i < c_conn; ++i)
                            {
                                byteSend = Encoding.Unicode.GetBytes("Show".ToCharArray());
                                foreach (DictionaryEntry dc in ht)
                                {

                                    socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                    socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                                }
                                Thread.Sleep(50);

                                byteSend = Encoding.Unicode.GetBytes(temp[i].ToCharArray());
                                foreach (DictionaryEntry dc in ht)
                                {

                                    socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                    socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                                }
                                Thread.Sleep(50);
                            }

                            for (int i = 0; i < c_conn; ++i) temp[i] = null;

                            if (count_temp == c_conn) count_temp = 0;

                            name = 0;
                        }

                    }

                }


                catch
                {
                    ;
                }

            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {
                textBox1.ReadOnly = true;
                _thread1 = new Thread(new ThreadStart(MainService));
                _thread1.Start();
            }
            else
            {
                MessageBox.Show("請輸入IP", "伺服器");
                textBox1.Text = "";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //_thread1.Abort();
            _thread1.Join();

        }
    }
}


