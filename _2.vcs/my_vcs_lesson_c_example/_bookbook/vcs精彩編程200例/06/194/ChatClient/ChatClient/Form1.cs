using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;

namespace ChatClient
{
    public partial class Form1 : Form
    {
        private TcpClient client;
        IPAddress serverIp;
        IPEndPoint ipConn;
        Socket clientSocket;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            client = new TcpClient(textBox1.Text, Convert.ToInt32(textBox2.Text));
            clientSocket = client.Client;
            byte[] bytes  = new byte[819200];
            byte[] Receivebytes = new byte[819200];
            bytes = Encoding.Unicode.GetBytes("\r\n"+"\""+textBox3.Text+"\"" + "进入了聊天室。");
            clientSocket.Send(bytes);
            clientSocket.Receive(Receivebytes);
            string serverMessage = Encoding.Unicode.GetString(Receivebytes);
            richTextBox1.Text = serverMessage+"\r\n";
            clientSocket.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            client = new TcpClient(textBox1.Text, Convert.ToInt32(textBox2.Text));
            clientSocket = client.Client;
            byte[] bytes = new byte[8192];
            byte[] receiveBytes = new byte[8192];
            bytes = Encoding.Unicode.GetBytes("\r\n"+textBox3.Text+"说："+richTextBox2.Text);
            if (clientSocket.Connected)
            {
                clientSocket.Send(bytes);
                richTextBox2.Clear();
                clientSocket.Receive(receiveBytes);
                string serverMessage = Encoding.Unicode.GetString(receiveBytes);
                richTextBox1.Clear();
                richTextBox1.Text=serverMessage+"\r\n";
            }
            clientSocket.Close();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            client = new TcpClient(textBox1.Text, Convert.ToInt32(textBox2.Text));
            clientSocket = client.Client;
            byte[] bytes = new byte[8192];
            byte[] receiveBytes = new byte[8192];
            bytes = Encoding.Unicode.GetBytes("\r\n" + " " );
            if (clientSocket.Connected)
            {
                clientSocket.Send(bytes);
                richTextBox2.Clear();
                clientSocket.Receive(receiveBytes);
                string serverMessage = Encoding.Unicode.GetString(receiveBytes);
                richTextBox1.Clear();
                richTextBox1.Text = serverMessage + "\r\n";
            }
            clientSocket.Close();
        }
    }
}