using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace NegotiateServer
{
  class NegotiateServer
  {
    static void Main(string[] args)
    {
      try
      {
        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // 設定交涉（Negotiate）安全性通訊協定之通訊通訊埠為8080
        string Port = "8080";

        TcpListener tcpListener = new TcpListener(serverIP, Int32.Parse(Port));

        tcpListener.Start();

        Console.WriteLine("Negotiate server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(tcpListener);

        // 執行緒
        ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
        Thread serverthread = new Thread(serverThreadStart);

        serverthread.Start();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
