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

using System.Configuration;

namespace ServerSocket
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    private void Button1_Click(object sender, EventArgs e)
    {
      try
      {
        string Host = ConfigurationManager.AppSettings["host"];
        string Port = ConfigurationManager.AppSettings["port"];

        IPAddress serverIP = Dns.Resolve(Host).AddressList[0];

        TcpListener tcpListener = new TcpListener(serverIP, Int32.Parse(Port));

        tcpListener.Start();

        ListBox1.Items.Clear();

        ListBox1.Items.Add("Server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(tcpListener, this);

        // °õ¦æºü
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