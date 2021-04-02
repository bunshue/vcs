using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


//using System.Net;
using System.Net.Sockets;
using System.IO;


namespace 收取電子郵件
{
   
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
        }

        TcpClient server;//接服務器
        string sendstring;//用於儲存POP3服務命令參數
        byte[] bufferstring;//用於儲存POP3服務命令參數字節數
        NetworkStream networkstream;//接服務器與服務器進行數據交互
        StreamReader streamreader;//讀取訊息數據

        private void button2_Click(object sender, EventArgs e)
        {
            server = new TcpClient(this.textBox1.Text, 110);//實例TcpClient 類對像聯接服務器
            networkstream = server.GetStream();//實例NetworkStream類對像接收傳回發送的數據
            streamreader = new StreamReader(networkstream);//實例StreamReader類對像讀取數據

            try
            {
                sendstring = "USER "+this.textBox2.Text+"\r\n";//儲存使用者名
                bufferstring = Encoding.GetEncoding("gb2312").GetBytes(sendstring.ToCharArray());
                networkstream.Write(bufferstring, 0, bufferstring.Length);//將使用者名發送到服務器
                richTextBox1.AppendText(streamreader.ReadLine() + "\r\n");//將用使用者顯示在 richTextBox控制元件中
                sendstring = "PASS " + this.textBox3.Text + "\r\n";//儲存使用者密碼
                bufferstring = Encoding.GetEncoding("gb2312").GetBytes(sendstring.ToCharArray());
                networkstream.Write(bufferstring, 0, bufferstring.Length);//將使用者密碼發送到服務器
                richTextBox1.AppendText(streamreader.ReadLine() + "\r\n");
                sendstring = "STAT " +"\r\n";//儲存從服務器獲得所有訊息序號和字節數命令
                bufferstring = Encoding.GetEncoding("gb2312").GetBytes(sendstring.ToCharArray());
                networkstream.Write(bufferstring, 0, bufferstring.Length);//從服務器獲得所有訊息序號和字節數
                string strResult=streamreader.ReadLine();//讀取從服務器傳回的數據
                if (strResult.IndexOf('-') == -1)
                {
                    richTextBox1.AppendText(strResult + "\r\n");
                    sendstring = "LIST " + "\r\n";//儲存從服務器中獲得訊息列表和大小的命令
                    bufferstring = Encoding.GetEncoding("gb2312").GetBytes(sendstring.ToCharArray());
                    networkstream.Write(bufferstring, 0, bufferstring.Length);

                    string strInfo = streamreader.ReadLine();
                    string[] str = strInfo.Split(' ');

                    richTextBox1.AppendText("郵件數量：" + str[1] + "\r\n");
                    richTextBox1.AppendText(str[1] + ":封郵件總容量為" + str[2] + "\r\n");

                    MessageBox.Show(this.textBox2.Text + "使用者您好！！！");
                    this.groupBox1.Enabled = false;
                    button1.Enabled = true;
                }
                else
                {
                    MessageBox.Show("讀取訊息有誤，請重新登入");
                }

            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }

        private void Showinfo()
        {
            Cursor cr = Cursor.Current;//定義滑鼠游標訊息
            Cursor.Current = Cursors.WaitCursor;
            this.richTextBox1.Clear();
            try
            {
                string strResult = "";
                sendstring = "RETR " + this.textBox4.Text + "\r\n";//儲存從服務器獲得一條訊息的命令
                bufferstring = Encoding.ASCII.GetBytes(sendstring.ToCharArray());
                networkstream.Write(bufferstring, 0, bufferstring.Length);
                strResult = streamreader.ReadLine();
                if (strResult[0] != '-')
                {
                    //不斷地讀取郵件內容，只到結束標誌：英文句號
                    while (strResult != ".")
                    {
                        this.richTextBox1.AppendText(strResult + "\r\n");
                        strResult = streamreader.ReadLine();
                    }
                }
                else
                {
                    this.richTextBox1.AppendText("\r\n" + "郵件錯誤" + "\r\n");
                }
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
            Cursor.Current = cr;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Showinfo();
            Showinfo();
        }
       
        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}