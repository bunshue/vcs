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

        IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

        Socket serverSocket = new Socket(AddressFamily.InterNetwork,
          SocketType.Stream, ProtocolType.Tcp);

        // 繫結設定伺服端Socket所使用的IP位址與通訊埠
        serverSocket.Bind(serverhost);

        // 設定伺服端最大用戶端連結數 Backlog = 50
        serverSocket.Listen(50);

        Console.WriteLine("DateTime server started at: " + serverhost.Address.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(serverSocket);

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
