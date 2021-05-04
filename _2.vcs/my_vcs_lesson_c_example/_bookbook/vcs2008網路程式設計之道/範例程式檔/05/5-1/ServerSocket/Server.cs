using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ServerSocket
{
  class Server
  {
    /// 應用程式的主進入點
    static void Main(string[] args)
    {
      try
      {
        Socket serverSocket = new Socket(AddressFamily.InterNetwork,
          SocketType.Stream, ProtocolType.Tcp);

        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // Port = 80
        string Port = "80";

        IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

        // 繫結設定伺服端Socket所使用的IP位址與通訊埠
        serverSocket.Bind(serverhost);

        // 設定伺服端最大用戶端連結數
        serverSocket.Listen(int.MaxValue);

        Console.WriteLine("Server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(serverSocket);

        // 執行緒
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
