using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets; //ServerSocket = new Socket(...)時使用
using System.Threading;  //Thread時使用
using System.Text;       //Encoding.Unicode.GetString(...) 時使用
using System.IO;         //使用FileInfo類別，來建立一個檔案實體物件


namespace 中國暗棋網路遊戲_server
{
    public partial class Form1 : Form
    {
        private Socket ServerSocket, SocketForClient;
        private Thread _thread1, _thread2;
        private Hashtable ht = new Hashtable(); // 使用hashtable 來記錄client-socket 的資訊
        //注意：後面這個= new Hashtable(); --- 不可以省略
        private Hashtable htname = new Hashtable(); //記錄登錄名稱
        private Hashtable name_score = new Hashtable(); //記錄猜對題數名稱
        delegate void mydel(string str);
        int c_conn = 0;
        int disconnect;
        int num;
        int[] Rvalue = new int[32]; //存取亂數
        string[] temp = new string[1024];
        string[] temp_score = new string[1024];
        public Form1()
        {
            InitializeComponent();
        }
        protected override void Dispose(bool disposing)
        {
            //清除資源
            try
            {
                --c_conn;
                Show_label2();
                ServerSocket.Shutdown(SocketShutdown.Both);
                ServerSocket.Close();
                SocketForClient.Shutdown(SocketShutdown.Both);
                SocketForClient.Close();
                _thread1.Abort();
                _thread2.Abort();

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
        private void Show_button1()//此副程式為了避免跨執行緒錯誤
        {
            if (button1.InvokeRequired) button1.Invoke(new MethodInvoker(Show_button1));
            else
            {
                button1.Enabled = false;
            }
        }
        private void Show_textBox1()//此副程式為了避免跨執行緒錯誤
        {
            if (textBox1.InvokeRequired) label3.Invoke(new MethodInvoker(Show_textBox1));
            else
            {

                textBox1.ReadOnly = false;
            }
        }

        private void MainService() //這個副程式，將會偵測是否有Client端用戶目前已經連線了
        {
            try
            {

                IPEndPoint serverhost = new IPEndPoint(IPAddress.Parse(textBox1.Text), 233);
                ServerSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                ServerSocket.Bind(serverhost);
                ServerSocket.Listen(50); //設定暫止連接佇列的長度為50	
                MessageBox.Show("伺服器啟動 !");
                Show_button1();
                while (true)  //無限迴圈檢查連線的Client的Socket資訊
                {

                    //如果主機socket偵聽到client的資訊，就記錄其SocketForClient資料
                    // ****** 兩種寫法皆可 *******************************
                    SocketForClient = ServerSocket.Accept();
                    ++c_conn;
                    ht.Add(SocketForClient.RemoteEndPoint, SocketForClient);

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
                MessageBox.Show("IP錯誤，請重新輸入！");
                Show_textBox1();
            }
        }
        private void Show_label2()
        {
            if (label2.InvokeRequired) label2.Invoke(new MethodInvoker(Show_label2));
            else
            {

                label2.Text = c_conn.ToString();
            }
        }

        private void Show_label3_1()//此副程式為了避免跨執行緒錯誤
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
            int ii, name = 0, count_temp = 0, turn = 0; ;
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

                    if (strAll == "disconnect") disconnect = 1; // 表示有人斷線                                           
                    if (disconnect == 1)
                    {
                        if ((strAll != "disconnect") && (strAll != ""))
                        {



                            --c_conn;
                            htname.Remove(strAll);
                            ht.Remove(sock.RemoteEndPoint);
                            byteSend = Encoding.Unicode.GetBytes("disconnect".ToCharArray());
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
                            byteSend = Encoding.Unicode.GetBytes("Disconnect".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                            }
                            Thread.Sleep(50);
                            byteSend = Encoding.Unicode.GetBytes(strAll.ToCharArray());
                            foreach (DictionaryEntry dc in ht)
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
                            disconnect = 0;

                        }

                    }


                    else  // 有人進來時
                    {

                        if (strAll == "name")
                        {
                            name = 1;
                            byteSend = Encoding.Unicode.GetBytes("c_conn".ToCharArray());
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
                        else if ((name == 1) && (strAll != "") && (strAll != "name") && (strAll != "win"))
                        {
                            htname.Add(strAll, sock);
                            Show_label2();
                            Show_label3((string)strAll);
                            foreach (DictionaryEntry de in htname)   //把上限者的名稱暫存在temp裡面
                            {

                                temp[count_temp] = (string)de.Key;
                                ++count_temp;
                            }
                            Thread.Sleep(50);

                            name = 0;
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
                        else if (strAll == "turn")
                        {
                            turn = 1;
                            byteSend = Encoding.Unicode.GetBytes("turn".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            
                            Thread.Sleep(50);
                        }
                        else if ((turn == 1) && (strAll != "") && (strAll != "name") && (strAll != "turn"))
                        {
                            turn = 0;
                            byteSend = Encoding.Unicode.GetBytes(strAll.ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }

                            Thread.Sleep(50);
                        }
                        else if (strAll == "[11]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[11]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[12]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[12]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[13]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[13]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[14]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[14]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[15]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[15]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[16]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[16]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[17]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[17]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[18]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[18]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[21]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[21]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[22]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[22]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[23]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[23]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[24]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[24]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[25]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[25]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[26]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[26]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[27]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[27]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[28]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[28]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[31]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[31]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[32]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[32]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[33]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[33]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[34]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[34]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[35]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[35]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[36]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[36]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[37]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[37]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[38]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[38]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[41]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[41]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[42]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[42]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[43]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[43]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[44]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[44]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[45]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[45]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[46]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[46]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[47]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[47]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
                        }
                        else if (strAll == "[48]")
                        {
                            byteSend = Encoding.Unicode.GetBytes("[48]".ToCharArray());
                            foreach (DictionaryEntry dc in ht)
                            {

                                socketTemp = (Socket)dc.Value;  //de.Value = client端的IP 
                                socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                            }
                            Thread.Sleep(50);
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
                MessageBox.Show("請輸入IP");

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            int temp;
            Socket socketTemp;
            Random rndObj = new Random();
            
            if (c_conn >= 1)
            {
                for (int i = 0; i < 32; ++i)Rvalue[i] = i;

                for (int i = 0; i < 32; ++i)
                {
                    
                    num = rndObj.Next(i , 31); //亂數取0~31
                    temp = Rvalue[num];
                    Rvalue[num] = Rvalue[i];
                    Rvalue[i] = temp;
                }
                      
                button2.Text = "決定了!";
                button2.Enabled = false;
               
                for (int i = 0; i < 32; i++)
                {

                    byteSend = Encoding.Unicode.GetBytes("Randnum".ToCharArray());
                    foreach (DictionaryEntry dc in ht)
                    {

                        socketTemp = (Socket)dc.Value;  //de.Value = client端的IP
                        socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                    }
                    Thread.Sleep(50);
                    byteSend = Encoding.Unicode.GetBytes(Rvalue[i].ToString().ToCharArray());
                    foreach (DictionaryEntry dc in ht)
                    {

                        socketTemp = (Socket)dc.Value;  //de.Value = client端的IP
                        socketTemp.SendTo(byteSend, (EndPoint)dc.Key);


                    }
                    Thread.Sleep(50);

                }
                /*
                byteSend = Encoding.Unicode.GetBytes("Finish".ToCharArray());
                foreach (DictionaryEntry dc in ht)
                {

                    socketTemp = (Socket)dc.Value;  //de.Value = client端的IP
                    socketTemp.SendTo(byteSend, (EndPoint)dc.Key);
                }
                Thread.Sleep(50);
            */
              
            }
            else
            {
                MessageBox.Show("沒有人上線");
            }
            button2.Text = "再產生一次";
            button2.Enabled = true;
        }
        
    }
}
