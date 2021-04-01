using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace DateTimeServer
{
  class Server
  {
    /// 應用程式的主進入點
    static void Main(string[] args)
    {
      try
      {
        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // DateTime Server Port = 13
        string Port = "13";

        TcpListener tcpListener = new TcpListener(serverIP, Int32.Parse(Port));

        tcpListener.Start();

        Console.WriteLine("DateTime Server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(tcpListener);

        ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
        Thread serverthread = new Thread(serverThreadStart);

        serverthread.Start();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
      finally
      {
      }
    }
  }
}
