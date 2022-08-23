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

namespace _client
{
    public partial class Form1 : Form
    {
        private Thread _thread1;
        private Socket ClientSocket;
        Form2 f2 = new Form2();
        delegate void mydel(string str);
        int Isconn = 0;

        static string namescore;
        public string NAMESCORE
        {

            set { namescore = value; }


            get { return namescore; }

        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        /*
        protected override void Dispose(bool disposing)
        {
            //清除資源


            if (Isconn == 1)
            {
                byte[] byteReceieve = new byte[1024];
                byte[] byteSend = new byte[1024];
                string disconnect = "disconnect";
                Isconn = 0;
                byteSend = Encoding.Unicode.GetBytes(disconnect.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());//若斷線，則傳給server斷線的字串
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                ClientSocket.Shutdown(SocketShutdown.Both);
                ClientSocket.Close();
                _thread1.Abort();

                Application.Exit();
            }
            else Application.Exit();
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }
         */

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

        private void Show_label4(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_label4;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if (label4.InvokeRequired) this.Invoke(a, obj);
            else this.label4.Text = (string)obj[0];
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

            int ii, six = 0, c_conn = 0, disconnect = 0, Disconnect = 0, Show = 0, update = 0;
            string strAll;
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
                    else if (strAll == "six") six = 1;
                    if ((c_conn == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "Show") &&
                        (strAll != "Disconnect") && (strAll != "disconnect") && (strAll != "score"))
                    {
                        c_conn = 0;
                        Show_listBox_3();
                        Show_label4(strAll);
                    }

                    if ((Show == 1) && (strAll != "") && (strAll != "Show") && (strAll != "disconnect") &&
                        (strAll != "Disconnect") && (strAll != "c_conn") && (strAll != "score"))
                    {
                        Show = 0;
                        Show_listBox_1(strAll);
                    }

                    if ((disconnect == 1) && (strAll != "") && (strAll != "disconnect") && (strAll != "Disconnect") &&
                        (strAll != "Show") && (strAll != "c_conn") && (strAll != "score"))
                    {
                        disconnect = 0;
                        Show_label4(strAll);
                    }

                    if ((Disconnect == 1) && (strAll != "") && (strAll != "Disconnect") && (strAll != "score") &&
                        (strAll != "disconnect") && (strAll != "Show") && (strAll != "c_conn"))
                    {
                        Disconnect = 0;
                        Show_listBox_2(strAll);
                    }
                    if ((six == 1) && (strAll != "") && (strAll != "disconnect") && (strAll != "Disconnect") &&
                       (strAll != "Show") && (strAll != "c_conn") && (strAll != "six"))
                    {
                        six = 0;
                        f2.NAMESCORE = strAll;
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

            Form2 f2 = new Form2();
            f2.SNAME = textBox2.Text;
            if (textBox2.Text == "")
            {
                MessageBox.Show("請輸入姓名", "玩家");
            }
            if (textBox1.Text == "")
            {
                MessageBox.Show("請輸入IP位址", "玩家");
            }
            else
            {
                try
                {
                    if (Isconn == 0)
                    {
                        ClientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                        IPEndPoint hostEP = new IPEndPoint(IPAddress.Parse(textBox1.Text), 233);

                        button1.Enabled = false;
                        button3.Enabled = true;
                        button2.Enabled = true;
                        textBox1.ReadOnly = true;
                        textBox2.ReadOnly = true;
                        ClientSocket.Connect(hostEP);
                        Isconn = 1;
                        _thread1 = new Thread(new ThreadStart(Listen));//讓_thread1去執行Listen()副函式
                        _thread1.Start();//啟動_thread1
                        Thread.Sleep(200);
                        byteSend = Encoding.Unicode.GetBytes("name".ToCharArray());
                        ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);//傳送byteSend資料給Server
                        Thread.Sleep(50);
                        byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                        ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);//傳送byteSend資料給Server
                        MessageBox.Show("連線成功！", "玩家");
                    }
                }
                catch
                {
                    MessageBox.Show("IP錯誤", "玩家");

                    button1.Enabled = true;
                    button2.Enabled = false;
                    textBox1.ReadOnly = false;
                    textBox2.ReadOnly = false;
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (Isconn == 1)
            {
                textBox1.ReadOnly = false;
                textBox2.ReadOnly = false;
                button1.Enabled = true;
                button2.Enabled = false;
                byteSend = Encoding.Unicode.GetBytes("disconnect".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());//若斷線，則傳給server斷線的字串
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Isconn = 0;
                ClientSocket.Shutdown(SocketShutdown.Both);
                ClientSocket.Close();
                _thread1.Abort();
                label4.Text = "";
                listBox1.Items.Clear();
                MessageBox.Show("已離線!", "玩家");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            timer1.Enabled = true;
            f2.Show(this);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];

            if (namescore != null)
            {
                byteSend = Encoding.Unicode.GetBytes("six".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(namescore.ToCharArray());//若斷線，則傳給server斷線的字串
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                namescore = null;
            }
        }
    }
}

