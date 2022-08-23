using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Threading;

namespace ChatServer
{
    public partial class Form1 : Form
    {
        private TcpListener listener;
        private int port = 8888;
        private Thread listenerThread;

        public Form1()
        {
            InitializeComponent();
            CheckForIllegalCrossThreadCalls = false;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Start();
        }

        public void Start()
        {
            listenerThread = new Thread(new ThreadStart(ServerListener));
            listenerThread.Start();
        }

        protected void ServerListener()
        {
            try
            {
                IPAddress ipAddress = Dns.Resolve("localhost").AddressList[0];
                listener = new TcpListener(ipAddress, port);
                listener.Start();

                while (true)
                {
                    Socket socket = listener.AcceptSocket();
                    byte[] bytes = new byte[8192];
                    byte[] sendBytes = new byte[8192];
                    if (socket.Receive(bytes) >= 0)
                    {
                        string receiveMessage = Encoding.Unicode.GetString(bytes);
                        richTextBox1.AppendText(receiveMessage + "\r\n");
                        sendBytes = Encoding.Unicode.GetBytes(richTextBox1.Text);
                        socket.Send(sendBytes);
                        socket.Close();
                    }

                }
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }

        public void Stop()
        {
            listenerThread.Abort();
        }

        public void Suspend()
        {
            listenerThread.Suspend();
        }

        public void Resume()
        {
            listenerThread.Resume();
        }
    }
}
