using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace NegotiateServer
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void btnStart_Click(object sender, EventArgs e)
    {
      try
      {
        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // 設定交涉（Negotiate）安全性通訊協定之通訊通訊埠為8080
        string Port = "8080";

        TcpListener tcpListener = new TcpListener(serverIP, Int32.Parse(Port));

        tcpListener.Start();

        ListBox1.Items.Clear();

        ListBox1.Items.Add("Negotiate server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(tcpListener, this);

        // 執行緒
        ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
        Thread serverthread = new Thread(serverThreadStart);

        serverthread.Start();
      }
      catch (Exception ex)
      {
        ListBox1.Items.Add(ex.StackTrace.ToString());
      }
    }
  }
}