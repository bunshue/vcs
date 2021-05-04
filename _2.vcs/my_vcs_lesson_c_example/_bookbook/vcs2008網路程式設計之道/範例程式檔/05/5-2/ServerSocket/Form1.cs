using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

// �R�W�Ŷ�
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ServerSocket
{
  public partial class Form1 : Form
  {
    Socket serverSocket = null;

    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      try
      {
        serverSocket = new Socket(AddressFamily.InterNetwork,
          SocketType.Stream, ProtocolType.Tcp);

        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // Port = 80
        string Port = "80";

        IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

        // ô���]�w���A��Socket�ҨϥΪ�IP��}�P�q�T��
        serverSocket.Bind(serverhost);

        // �]�w���A�ݳ̤j�Τ�ݳs���� Backlog = 50
        serverSocket.Listen(50);

        ListBox1.Items.Clear();

        ListBox1.Items.Add("Server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(serverSocket, this);

        // �����
        ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
        Thread serverthread = new Thread(serverThreadStart);

        serverthread.Start();
      }
      catch (Exception ex)
      {
        ListBox1.Items.Add(ex.StackTrace.ToString());
      }
      finally
      {
      }
    }
  }
}