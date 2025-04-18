﻿using System;
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

namespace 樂透網路遊戲設計_client
{
    public partial class Form1 : Form
    {
        int i = 0, count = 0, Add = 0; //i-樂透動畫用,count-樂透球計時用
        private Thread _thread1;
        private Socket ClientSocket;
        delegate void mydel(string str);
        public Form1()
        {
            InitializeComponent();
           
        }
        int Isconn = 0;
        private int priority = -1;
        static string number;
        public string NUMBER
        {

            set { number = value; }


            get { return number; }

        }
        public static string update;
        public string UPDATE
        {

            set { update = value; }


            get { return update; }

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

            int ii, score = 0, c_conn = 0, disconnect = 0, Disconnect = 0, Show = 0, update = 0, Randnum = 0, count_rand = 0;
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
                    else if (strAll == "update") update = 1;
                    else if (strAll == "Randnum") Randnum = 1;

                    if ((Randnum == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "Show") && (strAll != "Randnum") &&
                        (strAll != "Disconnect") && (strAll != "disconnect") && (strAll != "update") && (strAll != "score"))
                    {
                        Randnum = 0;

                        f2.RANDNUM = strAll;
                        count_rand++;
                        if (count_rand == 5)
                        {
                            f2.FINISH = "finishRand";
                         
                            count_rand = 0;
                        }
                        

                    }
                    if ((update == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "Randnum") &&
                       (strAll != "Show") && (strAll != "Disconnect") && (strAll != "disconnect") &&
                       (strAll != "update"))
                    {
                        update = 0;
                        f2.NUMBER = strAll;


                    }


                    if ((c_conn == 1) && (strAll != "") && (strAll != "c_conn") && (strAll != "Show") && (strAll != "Randnum") &&
                        (strAll != "Disconnect") && (strAll != "disconnect") && (strAll != "update") && (strAll != "score"))
                    {
                        c_conn = 0;
                        Show_listBox_3();

                        Show_label4(strAll);


                    }

                    if ((Show == 1) && (strAll != "") && (strAll != "Show") && (strAll != "disconnect") && (strAll != "Randnum") &&
                        (strAll != "Disconnect") && (strAll != "c_conn") && (strAll != "update") && (strAll != "score") && (Randnum == 0))
                    {
                        Show = 0;
                        Show_listBox_1(strAll);//加入

                    }

                    if ((disconnect == 1) && (strAll != "") && (strAll != "disconnect") && (strAll != "Disconnect") &&
                        (strAll != "Show") && (strAll != "c_conn") && (strAll != "update") && (strAll != "score") && 
                        (strAll != "Randnum") && (Randnum == 0)) 
                    {
                        disconnect = 0;
                        Show_label4(strAll);

                    }

                    if ((Disconnect == 1) && (strAll != "") && (strAll != "Disconnect") && (strAll != "score") && (strAll != "Randnum") &&
                        (strAll != "disconnect") && (strAll != "Show") && (strAll != "c_conn") && (strAll != "update") && (Randnum == 0))
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

       
        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("選擇遊戲玩法後，要輸入好號碼開始遊戲才會開啟喔。\n按開始遊戲後樂透球會開始轉動，並陸續開出號碼。\n小樂透玩法裡，每一個欄位記得都要填上數字喔！\n一分鐘樂透玩法裡，每一分鐘都會自動開出一組號碼，開出號碼後玩家有一分鐘的時間選擇新號碼，\n選號時間結束後玩家就不得輸入新的號碼，所以動作要快喔！", "遊戲說明", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

            i++;
            count++;
            pictureBox1.Image = imageList1.Images[i]; //樂透動畫
            if(i == 6) i = 0;
            if (count == 1000)
            {
                pictureBox1.Image = imageList1.Images[0];
                count = 0;
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
                    timer1.Enabled = true;
                    
                    
                }
                catch
                {
                    timer1.Enabled = false;
                    MessageBox.Show("IP錯誤");
                    textBox1.ReadOnly = false;
                    textBox2.ReadOnly = false;
                    button4.Enabled = false;
                    button2.Enabled = false;
                    button1.Enabled = true;

                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
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
                timer1.Enabled = false;
                MessageBox.Show("已斷線!");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            
            f2.Show(this);
            timer2.Enabled = true;
            timer3.Enabled = true;
            
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
             byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            string strAll;
            if ((number != null) && (priority != -1))
            {
                byteSend = Encoding.Unicode.GetBytes("update".ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                strAll = priority.ToString() + "|" + "玩家" + textBox2.Text + "猜對" + number + "個";
                byteSend = Encoding.Unicode.GetBytes(strAll.ToCharArray());
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
              //  Thread.Sleep(50);
                number = null;
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
           byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (update == "update")
            {
                
                update = null;
            }
        }

    }
}
