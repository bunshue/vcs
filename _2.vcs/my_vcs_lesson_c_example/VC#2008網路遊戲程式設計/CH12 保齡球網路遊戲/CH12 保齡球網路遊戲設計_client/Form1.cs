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

namespace 保齡球網路遊戲設計_client
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
        int Isconn = 0, up = 0;
        private int Pri = -1;
        static string count;
        public string COUNT
        {

            set { count = value; }


            get { return count; }

        }
        static string score;
        public string SCORE
        {

            set { score = value; }


            get { return score; }

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

            if (Pri == -1)
            {
                Pri = int.Parse(str);
                f2.PRI = str;
            }
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

        private void Listen()//利用Tthread 接收訊號
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];

            EndPoint oldEP = ClientSocket.RemoteEndPoint;
            Thread tempthread = _thread1;

            int ii, c_conn = 0, disconnect = 0, Disconnect = 0, Show = 0, PP = 0 , score = 0;
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
                    else if (strAll == "four") up = 1;
                    else if (strAll == "AAA") up = 0;
                    else if (strAll == "++") PP = 1;
                    else if (strAll == "score") score = 1;

                    else if ((score == 1))
                    {
                        
                        f2.SCORE = strAll;
                        score = 0;
                        
                    }
                    else if ((PP == 1))
                    {
                        
                        f2.TEMP = strAll;
                        PP = 0;

                    }
                    else if ((c_conn == 1))
                    {
                        
                        Show_listBox_3();
                        Show_label4(strAll);
                        c_conn = 0;
                    }

                    else if ((Show == 1))
                    {
                       
                        Show_listBox_1(strAll);
                        Show = 0;
                    }

                    else if ((disconnect == 1))
                    {
                        
                        Show_label4(strAll);
                        disconnect = 0;


                    }

                    else if ((Disconnect == 1))
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
                    textBox1.ReadOnly = true;
                    textBox2.ReadOnly = true;
                    button4.Enabled = true;
                    button2.Enabled = true;
                    button1.Enabled = false;

                    MessageBox.Show("連線成功！");




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
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (Isconn == 1)
            {
                Pri = -1;
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

                MessageBox.Show("已斷線!");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {

            MessageBox.Show("此遊戲為三個人玩，進入遊戲後，先調整球的位置，再選擇球的力道，按下開始就可以了", "說明");     //跳出使用說明
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            
            if (up == 0)
            {
                f2.Show(this);
                timer1.Enabled = true;
                timer2.Enabled = true;
            }
            else 
            {
                if (Pri >= 4)
                    MessageBox.Show("人數已滿(三個)");
                else
                {
                    f2.Show(this);
                    timer1.Enabled = true;
                    timer2.Enabled = true;
                }
            }
        }

        private void timer1_Tick(object sender, EventArgs e)//檢查Form2的保齡球是否已經發完
        {
            /*
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (count != null)
            {
                byteSend = Encoding.Unicode.GetBytes("++".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(80);
                byteSend = Encoding.Unicode.GetBytes(count.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                count = null;
            }
             * */
        }

        private void timer2_Tick(object sender, EventArgs e)//檢查玩家是否有分數
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            string strAll;
            if (score != null)
            {
                byteSend = Encoding.Unicode.GetBytes("score".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                strAll = Pri + "|" + "玩家" + textBox2.Text + "得" +  score + "分";
                byteSend = Encoding.Unicode.GetBytes(strAll.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                score = null;
            }
        }
    }
}
