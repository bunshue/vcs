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

namespace 戰鬥飛機網路遊戲_client
{
    public partial class Form1 : Form
    {
        private Thread _thread1;
        private Socket ClientSocket;
        delegate void mydel(string str);
        public Form1()
        {
            InitializeComponent();
        }
        int Isconn = 0;
        static string co;//飛機座標
        public string CO
        {

            set { co = value; }


            get { return co; }

        }
        static string cob;//飛彈座標
        public string COB
        {

            set { cob = value; }


            get { return cob; }

        }
        static string lose;//飛彈座標
        public string LOSE
        {

            set { lose = value; }


            get { return lose; }

        }
        static string win;//飛彈座標
        public string WIN
        {

            set { win = value; }


            get { return win; }

        }
        private void Show_label4(string str)//此副程式為了避免跨執行緒錯誤
        {
            Form2 f2 = new Form2();
            mydel a = Show_label4;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if (label4.InvokeRequired) this.Invoke(a, obj);
            else this.label4.Text = (string)obj[0];

            if (f2.P == null) f2.P = (string)obj[0];
        }

        private void Show_listBox_1(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_listBox_1;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if ((listBox1.InvokeRequired)) this.Invoke(a, obj);
            else
            {

                this.listBox1.Items.Add((string)obj[0]);

            }

        }
        private void Show_listBox_2(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_listBox_2;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if ((listBox1.InvokeRequired)) this.Invoke(a, obj);
            else
            {
                this.listBox1.Items.Remove((string)obj[0]);
            }

        }
        private void Show_listBox_3()//此副程式為了避免跨執行緒錯誤
        {
            if (listBox1.InvokeRequired) listBox1.Invoke(new MethodInvoker(Show_listBox_3));
            else
            {

                this.listBox1.Items.Clear();
            }
        }

        private void Listen()
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];

            EndPoint oldEP = ClientSocket.RemoteEndPoint;
            Thread tempthread = _thread1;

            int ii, c_conn = 0, disconnect = 0, Disconnect = 0, Show = 0, co = 0 , cob = 0 , lose = 0 , win = 0;
            string strAll;
            Form2 f2 = new Form2();
            while (true)
            {

                try
                {

                    ii = ClientSocket.ReceiveFrom(byteReceieve, 0, byteReceieve.Length, SocketFlags.None, ref oldEP);


                    strAll = Encoding.Unicode.GetString(byteReceieve, 0, ii);

                    if (strAll == "c_conn") c_conn = 1;
                    else if (strAll == "Show") Show = 1;
                    else if (strAll == "disconnect") disconnect = 1;
                    else if (strAll == "Disconnect") Disconnect = 1;
                    else if (strAll == "co") co = 1;
                    else if (strAll == "cob") cob = 1;
                    else if (strAll == "lose") lose = 1;
                    else if (strAll == "win") win = 1;

                    if ((win == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "win") && (lose == 0) &&
                       (strAll != "Show") && (strAll != "cob") && (strAll != "co") && (strAll != "lose") && (strAll != textBox2.Text))
                    {
                        win = 0;
                        f2.LOSE = "lose";
                        MessageBox.Show("被擊敗了！");
                        

                    }
                    else if ((lose == 1) && (strAll != "") && (strAll != "c_conn") && (win == 0) && (strAll != "Show") &&
                        (strAll != "cob") && (strAll != "co") && (strAll != "lose") && (strAll != textBox2.Text) && (strAll != "win"))
                    {
                        lose = 0;
                        f2.LOSE = "lose";
                        MessageBox.Show("對方撞壁，你贏了！");
                        

                    }
                    else if ((cob == 1) && (strAll != "") && (strAll != "c_conn") &&
                       (strAll != "Show") && (strAll != "cob") && (strAll != "co") && (co == 0) && (strAll != "win") && (strAll != "lose"))
                    {
                        cob = 0;
                        f2.COB = strAll;
                        

                    }

                    else if ((co == 1) && (strAll != "co") && (strAll != "") && (strAll != "c_conn") && (strAll != "Show") && 
                        (strAll != "cob") && (strAll != "win") && (strAll != "lose"))
                    {
                        co = 0;
                        f2.CO = strAll;
                        

                    }

                    else if ((c_conn == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "Show"))
                    {
                        c_conn = 0;
                        Show_listBox_3();
                        Show_label4(strAll);


                    }

                    else if ((Show == 1) && (strAll != "") && (strAll != "Show") && (strAll != "c_conn"))
                    {
                        Show = 0;
                        Show_listBox_1(strAll);//加入

                    }

                    else if ((disconnect == 1) && (strAll != "") && (strAll != "disconnect") && (strAll != "Disconnect") &&
                        (strAll != "Show") && (strAll != "c_conn"))
                    {
                        disconnect = 0;
                        Show_label4(strAll);

                    }

                    else if ((Disconnect == 1) && (strAll != "") && (strAll != "Disconnect") &&
                        (strAll != "disconnect"))
                    {
                        Disconnect = 0;
                        Show_listBox_2(strAll);

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
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];


            if (textBox2.Text == "")
            {
                MessageBox.Show("請輸入姓名");
            }
            else if (textBox1.Text == "")
            {
                MessageBox.Show("請輸入IP位址");
            }
            else
            {
                try
                {
                    ClientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                    IPEndPoint hostEP = new IPEndPoint(IPAddress.Parse(textBox1.Text), 233);

                    textBox1.ReadOnly = true;
                    textBox2.ReadOnly = true;
                    button4.Enabled = true;
                    button2.Enabled = true;
                    button1.Enabled = false;
                    ClientSocket.Connect(hostEP);
                    Isconn = 1;
                    _thread1 = new Thread(new ThreadStart(Listen));
                    _thread1.Start();
                    Thread.Sleep(200);
                    byteSend = Encoding.Unicode.GetBytes("name".ToCharArray());
                    ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                    Thread.Sleep(50);
                    byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                    ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);


                    MessageBox.Show("連線成功！");

                    // btnStart.Enabled = false;
                    textBox1.Enabled = false;
                 


                }
                catch
                {
                  
                    MessageBox.Show("IP錯誤");
                    textBox1.ReadOnly = false;
                    textBox2.ReadOnly = false;
                    button4.Enabled = false;
                    button2.Enabled = false;
                    button1.Enabled = true;

                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();

            f2.Show(this);
            timer1.Enabled = true;
            timer2.Enabled = true;
            timer3.Enabled = true;
            timer4.Enabled = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("本遊戲為一種戰鬥機遊戲，\n單機版，\n發射飛彈將敵機擊落即可。\n飛機飛行時，不能離開白色框框，會爆炸！", "遊戲說明", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            Form2 f2 = new Form2();
            if (Isconn == 1)
            {
                textBox2.ReadOnly = false;
                textBox1.ReadOnly = false;
                button1.Enabled = true;
                button2.Enabled = false;
                button4.Enabled = false;
                label4.Text = "";
                listBox1.Items.Clear();
                byteSend = Encoding.Unicode.GetBytes("disconnect".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Isconn = 0;
                ClientSocket.Shutdown(SocketShutdown.Both);
                ClientSocket.Close();
                _thread1.Abort();
                f2.P = null;
                MessageBox.Show("已斷線!");
            }
        }

        private void timer1_Tick(object sender, EventArgs e)//此timer來檢查是否有飛機移動
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (co != null)
            {
                byteSend = Encoding.Unicode.GetBytes("co".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(co.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                co = null;
            }
           
        }

        private void timer2_Tick(object sender, EventArgs e)//此timer來檢查是否設出飛彈
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (cob != null)
            {
                byteSend = Encoding.Unicode.GetBytes("cob".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(cob.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                cob = null;
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (lose != null)
            {
                byteSend = Encoding.Unicode.GetBytes("lose".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                lose = null;
            }
        }

        private void timer4_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (win != null)
            {
                byteSend = Encoding.Unicode.GetBytes("win".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                win = null;
            }
        }
    }
}
