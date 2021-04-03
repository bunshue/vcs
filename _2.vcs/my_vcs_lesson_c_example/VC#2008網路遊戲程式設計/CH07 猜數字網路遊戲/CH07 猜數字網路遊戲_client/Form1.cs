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

namespace 猜數字_網路對戰_client
{
    public partial class Form1 : System.Windows.Forms.Form
    {
        private Thread _thread1;
        private Socket ClientSocket;
        private Hashtable htname = new Hashtable(); //記錄登錄名稱

        delegate void mydel(string str);
        int Isconn = 0;
        
        
        public Form1()
        {
            InitializeComponent();
        }
        public static string win;
        public string Win
        {

           set{win = value;}


           get{return win;}

        }
        

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
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
        private void button2_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            if (Isconn == 1)
            {
                
                f2.Show();
                timer1.Enabled = true;
                
            }
            else
            {
                MessageBox.Show("還沒和server連線");
            }

        }
        private void Show_label2(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_label2;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if (label2.InvokeRequired) this.Invoke(a, obj);

            else this.label2.Text = (string)obj[0];
        }
        
        private void Show_listBox1(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_listBox1;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if ((listBox1.InvokeRequired)) this.Invoke(a, obj);
            else
            {

                this.listBox1.Items.Add((string)obj[0]);                  
                
            }
            
        }
        private void Show_listBox2(string str)//此副程式為了避免跨執行緒錯誤
        {
            mydel a = Show_listBox2;
            object[] obj;
            obj = new object[1];
            obj[0] = str;
            if ((listBox1.InvokeRequired)) this.Invoke(a, obj);
            else
            {
                this.listBox1.Items.Remove((string)obj[0]);
            } 

        }
        private void Show_listBox3()//此副程式為了避免跨執行緒錯誤
        {
            if (listBox1.InvokeRequired) listBox1.Invoke(new MethodInvoker(Show_listBox3));
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
            int ii, c_conn = 0, disconnect = 0, Show = 0, Disconnect = 0, A = 0, Randnum = 0;
            string strAll;
            Form2 f2 = new Form2();
            while (true)
            {

                //ii = ClientSocket.ReceiveFrom(byteReceieve,ref oldEP);
                //ii = ClientSocket.ReceiveFrom(byteReceieve, 0, byteReceieve.Length, SocketFlags.None, ref oldEP);
                try
                {
                    ii = ClientSocket.ReceiveFrom(byteReceieve, 0, byteReceieve.Length, SocketFlags.None, ref oldEP);
                    strAll = Encoding.Unicode.GetString(byteReceieve, 0, ii);
                    /*
                    
                     * */
                    if (strAll == "c_conn") c_conn = 1;
                    else if (strAll == "Randnum") Randnum = 1;
                    else if (strAll == "Show") Show = 1;
                    else if (strAll == "win") A = 1;                                                                       
                    else if (strAll == "disconnect") disconnect = 1;
                    else  if (strAll == "Disconnect") Disconnect = 1;

                    else if ((strAll != textBox2.Text) && (A == 1) && (strAll != "c_conn") && (strAll != "disconnect") &&   //判斷是否是自己的名稱
                        (c_conn == 0) && (disconnect == 0) && (strAll != "Show") && (Show == 0) &&
                        (strAll != "Disconnect") && (Disconnect == 0) && (strAll != "win") && (strAll != "Randnum"))
                    {
                        MessageBox.Show("你輸了。");
                       
                        A = 0;
                    }


                    else if ((c_conn == 1))
                   {
                            c_conn = 0;
                            Show_listBox3();
                            Show_label2(strAll);

                   }


                    else if ((Show == 1))
                   {
                                

                                
                                Show_listBox1(strAll);
                                Show = 0;
                                
                   }

                   else if ((disconnect == 1))
                   {
                            disconnect = 0;
                            Show_label2(strAll);
                           
                   }

                   else if ((Disconnect == 1))
                   {
                            Disconnect = 0;
                            Show_listBox2(strAll);
                            

                   }
                   else if ((Randnum == 1))
                    {
                          Randnum = 0;
                          f2.Rand = strAll;
                          
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

            if (textBox3.Text == "")
            {
                MessageBox.Show("請輸入伺服器IP位址!");
            }
            if (textBox2.Text == "")
            {
                MessageBox.Show("請輸入暱稱");
            }
            else
            {
                try
                {
                    ClientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                    IPEndPoint hostEP = new IPEndPoint(IPAddress.Parse(textBox3.Text), 233);
                    ClientSocket.Connect(hostEP);
                    Isconn = 1; //已經連線
                    _thread1 = new Thread(new ThreadStart(Listen));
                    _thread1.Start();
                    Thread.Sleep(200);

                    
                    byteSend = Encoding.Unicode.GetBytes("name".ToCharArray());
                    ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                    Thread.Sleep(50);
                    byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());
                    ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                    button1.Enabled = false;
                    button4.Enabled = true;
                    textBox2.ReadOnly = true;
                    textBox3.ReadOnly = true;
                    MessageBox.Show("連線成功！");

                }
                catch
                {
                    MessageBox.Show("無法與伺服器主機連上線");
                }
            }
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            
        
            MessageBox.Show("本遊戲唯一種益智遊戲，\n網路版，伺服器會決定一個０～９９９數字，將此數字命名為Ｘ，決定此數字後玩家猜Ｘ，若猜的數字比Ｘ大，則顯示 < Ｘ，否則 顯示 > Ｘ。看誰猜到就贏。", "遊戲說明",
               MessageBoxButtons.OK, MessageBoxIcon.Information);
        
        }

        private void button4_Click(object sender, EventArgs e)
        {
            byte[] byteReceieve = new byte[1024];
            byte[] byteSend = new byte[1024];
            if (Isconn == 1)
            {
                
                Isconn = 0;
                byteSend = Encoding.Unicode.GetBytes("disconnect".ToCharArray());//若斷線，則傳給server斷線的字串
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);
                Thread.Sleep(50);
                byteSend = Encoding.Unicode.GetBytes(textBox2.Text.ToCharArray());//若斷線，則傳給server斷線的字串
                ClientSocket.Send(byteSend, 0, byteSend.Length, SocketFlags.None);

                ClientSocket.Shutdown(SocketShutdown.Both);
                ClientSocket.Close();
                _thread1.Abort();

                textBox2.ReadOnly = false;
                textBox3.ReadOnly = false;
                button1.Enabled = true;
                button4.Enabled = false;
                label2.Text = "";
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
                timer1.Enabled = false;
            }
                        
        }
    }
}
