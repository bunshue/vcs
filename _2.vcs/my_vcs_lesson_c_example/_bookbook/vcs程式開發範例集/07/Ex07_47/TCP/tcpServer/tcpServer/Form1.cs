﻿using System;
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

namespace tcpServer
{
    public partial class Form1 : Form
    {
        IPAddress HostIP = IPAddress.Parse("192.168.2.114");
        IPEndPoint point;
        Socket socket;
        bool flag = true;
        Socket acceptedSocket;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //聲名委託
        delegate void SetTextCallback(string text);
        private void SetText(string text)
        {
            richTextBox1.AppendText(text + "\r\n");
        }

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

        private void button1_Click(object sender, EventArgs e)
        {
            HostIP = IPAddress.Parse("192.168.2.114");
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
            catch { }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                Byte[] sendByte = new Byte[64];
                string sendStr = this.textBox1.Text + "：" + this.textBox3.Text + "\r\n";
                sendByte = Encoding.BigEndianUnicode.GetBytes(sendStr.ToCharArray());
                acceptedSocket.Send(sendByte, sendByte.Length, 0);
            }
            catch (Exception ex)
            {
                richTextBox2.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }
    }
}

