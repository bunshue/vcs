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

namespace 大家來找碴網路遊戲_client
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
        private int priority = -1;
        public static string win;
        public string WIN
        {

            set { win = value; }


            get { return win; }

        }
        public static string lose;
        public string LOSE
        {

            set { lose = value; }


            get { return lose; }

        }
        private void Show_label4(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_label4;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if (label4.InvokeRequired) this.Invoke(a, obj);
            else this.label4.Text = (string)obj[0];

            if (priority == -1) priority = int.Parse(str) - 1;

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

            int ii, score = 0, c_conn = 0, disconnect = 0, Disconnect = 0, Show = 0 , win = 0 , lose = 0;
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
                    else if (strAll == "win") win = 1;
                    else if (strAll == "lose") lose = 1;

                    if ((win == 1) && (strAll != "") && (strAll != "c_conn") &&
                       (strAll != "Show") && (strAll != "Disconnect") && (strAll != "disconnect") &&
                       (strAll != "win") && (strAll != "lose") && (strAll != textBox2.Text) && (disconnect == 0))
                    {
                        
                        MessageBox.Show("你輸了");
                        win = 0;

                    }
                    if ((lose == 1) && (strAll != "") && (strAll != "c_conn") &&
                       (strAll != "Show") && (strAll != "Disconnect") && (strAll != "disconnect") &&
                       (strAll != "win") && (strAll != textBox2.Text) && (disconnect == 0) && (strAll != "lose") && (Disconnect == 0))
                    {
                        
                        MessageBox.Show("對方超過次數了");
                        lose = 0;

                    }

                    if ((c_conn == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "Show") &&
                        (strAll != "Disconnect") && (strAll != "disconnect") && (strAll != "win"))
                    {
                        c_conn = 0;
                        Show_listBox_3();

                        Show_label4(strAll);


                    }

                    if ((Show == 1) && (strAll != "") && (strAll != "Show") && (strAll != "disconnect") &&
                        (strAll != "Disconnect") && (strAll != "c_conn") && (strAll != "win"))
                    {
                        Show = 0;
                        Show_listBox_1(strAll);//加入

                    }

                    if ((disconnect == 1) && (strAll != "") && (strAll != "disconnect") && (strAll != "Disconnect") &&
                        (strAll != "Show") && (strAll != "c_conn") && (strAll != "win"))
                    {
                        
                        Show_label4(strAll);
                        disconnect = 0;
                    }

                    if ((Disconnect == 1) && (strAll != "") && (strAll != "Disconnect") &&
                        (strAll != "disconnect") && (strAll != "Show") && (strAll != "c_conn") && (strAll != "win"))
                    {
                        
                        Show_listBox_2(strAll);
                        Disconnect = 0;
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
                    button3.Enabled = true;
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
                    button3.Enabled = false;
                    button2.Enabled = false;
                    button1.Enabled = true;

                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            f2.Show();
            timer1.Enabled = true;
            timer2.Enabled = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (Isconn == 1)
            {
                textBox2.ReadOnly = false;
                textBox1.ReadOnly = false;
                button1.Enabled = true;
                button2.Enabled = false;
                button3.Enabled = false;
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
            
                MessageBox.Show("已斷線!");
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (win == "win")
            {
                byteSend = Encoding.Unicode.GetBytes("win".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                win = null;
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (lose == "lose")
            {
                byteSend = Encoding.Unicode.GetBytes("lose".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                lose = null;
            }
        }
    }
}
