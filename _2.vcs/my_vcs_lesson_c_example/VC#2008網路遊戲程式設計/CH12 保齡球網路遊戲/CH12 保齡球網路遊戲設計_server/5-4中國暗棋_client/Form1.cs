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

namespace 中國暗期_client
{
    public partial class Form1 : Form
    {
        private Thread _thread1;
        private Socket ClientSocket;
        delegate void mydel(string str);
        int Isconn = 0;
        string[] V = new string[32];
        private int priority = -1;
        public static string pos;
        public string POS
        {

            set { pos = value; }


            get { return pos; }

        }
        public static string turn;
        public string TURN
        {

            set { turn = value; }


            get { return turn; }

        }
        public Form1()
        {
            InitializeComponent();
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

            if (priority == -1) priority = int.Parse(str) ;

            f2.PRI = priority.ToString();

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

            int ii, win = 0, c_conn = 0, disconnect = 0, Disconnect = 0, Show = 0, Randnum = 0 , count_rand = 0 , turn = 0;
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
                    else if (strAll == "Randnum") Randnum = 1;
                    else if (strAll == "turn") turn = 1;
                    else if (strAll == "[11]") f2.TEMP = "[11]";//象棋位置
                    else if (strAll == "[12]") f2.TEMP = "[12]";
                    else if (strAll == "[13]") f2.TEMP = "[13]";
                    else if (strAll == "[14]") f2.TEMP = "[14]";
                    else if (strAll == "[15]") f2.TEMP = "[15]";
                    else if (strAll == "[16]") f2.TEMP = "[16]";
                    else if (strAll == "[17]") f2.TEMP = "[17]";
                    else if (strAll == "[18]") f2.TEMP = "[18]";
                    else if (strAll == "[21]") f2.TEMP = "[21]";
                    else if (strAll == "[22]") f2.TEMP = "[22]";
                    else if (strAll == "[23]") f2.TEMP = "[23]";
                    else if (strAll == "[24]") f2.TEMP = "[24]";
                    else if (strAll == "[25]") f2.TEMP = "[25]";
                    else if (strAll == "[26]") f2.TEMP = "[26]";
                    else if (strAll == "[27]") f2.TEMP = "[27]";
                    else if (strAll == "[28]") f2.TEMP = "[28]";
                    else if (strAll == "[31]") f2.TEMP = "[31]";
                    else if (strAll == "[32]") f2.TEMP = "[32]";
                    else if (strAll == "[33]") f2.TEMP = "[33]";
                    else if (strAll == "[34]") f2.TEMP = "[34]";
                    else if (strAll == "[35]") f2.TEMP = "[35]";
                    else if (strAll == "[36]") f2.TEMP = "[36]";
                    else if (strAll == "[37]") f2.TEMP = "[37]";
                    else if (strAll == "[38]") f2.TEMP = "[38]";
                    else if (strAll == "[41]") f2.TEMP = "[41]";
                    else if (strAll == "[42]") f2.TEMP = "[42]";
                    else if (strAll == "[43]") f2.TEMP = "[43]";
                    else if (strAll == "[44]") f2.TEMP = "[44]";
                    else if (strAll == "[45]") f2.TEMP = "[45]";
                    else if (strAll == "[46]") f2.TEMP = "[46]";
                    else if (strAll == "[47]") f2.TEMP = "[47]";
                    else if (strAll == "[48]") f2.TEMP = "[48]";

                    else if ((turn == 1) )
                    {
                        turn = 0;
                        f2.TURN = strAll;
                    }
                    else if ((Randnum == 1))
                    {
                        

                        V[count_rand] = strAll;
                        f2.RANDNUM = strAll;
                        count_rand++;
                        if (count_rand == 32)
                        {
                           // for (int i = 0; i < 32; ++i) f2.RANDNUM = V[i];

                             f2.FINISH = "finishRand";

                             count_rand = 0;
                        }
                        Randnum = 0;
                    }



                    else if ((c_conn == 1) && (strAll != "c_conn") && (strAll != "Show") && (strAll != "Finish") &&
                        (strAll != "Disconnect") && (strAll != "disconnect") && (strAll != "turn"))
                    {
                        c_conn = 0;
                        Show_listBox_3();

                        Show_label4(strAll);


                    }

                    else if ((Show == 1) && (strAll != "Show") && (strAll != "disconnect") && (strAll != "Finish") &&
                        (strAll != "Disconnect") && (strAll != "c_conn") && (strAll != "turn"))
                    {
                        Show = 0;
                        Show_listBox_1(strAll);//加入

                    }

                    else if ((disconnect == 1) && (strAll != "disconnect") && (strAll != "Disconnect") &&
                        (strAll != "Show") && (strAll != "c_conn") && (strAll != "turn") && (strAll != "Finish"))
                    {
                        disconnect = 0;
                        Show_label4(strAll);

                    }

                    else if ((Disconnect == 1) && (strAll != "Disconnect") && (strAll != "Finish") &&
                        (strAll != "disconnect") && (strAll != "Show") && (strAll != "c_conn") && (strAll != "turn"))
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
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (Isconn == 1)
            {
                textBox2.ReadOnly = false;
                textBox1.ReadOnly = false;
                button1.Enabled = true;
                button2.Enabled = false;
                button3.Enabled = false;
                priority = -1;
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

        private void button3_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            f2.Show();
            timer1.Enabled = true;
            timer2.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (pos != null)
            {
                byteSend = Encoding.Unicode.GetBytes(pos.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                Thread.Sleep(50);
                pos = null;
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (turn != null)
            {
                byteSend = Encoding.Unicode.GetBytes("turn".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(turn.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                turn = null;
            }
        }
    }
}
