using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Threading;
using System.Net.Sockets;

namespace Win_Talk
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

        #region//定義變數
        IPAddress HostIP = IPAddress.Parse("127.0.0.1");
        IPEndPoint point;
        Socket socket;
        bool flag = true;
        Socket acceptedSocket;
        #endregion

        #region//聲名委託
        delegate void SetTextCallback(string text);
        private void SetText(string text)
        {
            textBox2.AppendText(text + "\r\n");
        }
        #endregion

        #region//程序方法
        private void Proccess()
        {
            if (acceptedSocket.Connected)
            {
                while (flag)
                {
                    byte[] receiveByte = new byte[64];
                    acceptedSocket.Receive(receiveByte, receiveByte.Length, 0);
                    string strInfo = Encoding.BigEndianUnicode.GetString(receiveByte);
                    this.Invoke(new SetTextCallback(SetText), new object[] { strInfo });

                }
            }
        }
        #endregion

        private void button3_Click(object sender, EventArgs e)
        {
            socket.Close();
            acceptedSocket.Close();
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            try
            {
                Byte[] sendByte = new Byte[64];
                string sendStr = this.textBox1.Text + "：" + this.textBox3.Text + "\r\n";
                sendByte = Encoding.BigEndianUnicode.GetBytes(sendStr.ToCharArray());
                acceptedSocket.Send(sendByte, sendByte.Length, 0);
            }
            catch { }
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            HostIP = IPAddress.Parse(textBox1.Text.Trim());
            try
            {
                point = new IPEndPoint(HostIP, Int32.Parse("11000"));
                socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                socket.Bind(point);
                socket.Listen(50);
                acceptedSocket = socket.Accept();
                Thread thread = new Thread(new ThreadStart(Proccess));
                thread.Start();
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }
    }
}