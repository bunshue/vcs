using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace WebServer
{
  class WebServer
  {
    static void Main(string[] args)
    {
      try
      {
        //IPAddress serverIP = IPAddress.Parse("127.0.0.1") ;
        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // HTTP Server Port = 80
        string Port = "80";

        IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

        Socket serverSocket = new Socket(AddressFamily.InterNetwork,
          SocketType.Stream, ProtocolType.Tcp);

        // 繫結設定伺服端Socket所使用的IP位址與通訊埠
        serverSocket.Bind(serverhost);

        // 設定伺服端最大用戶端連結數 Backlog = 100
        serverSocket.Listen(100);

        Console.WriteLine("HTTP server started at: " + serverhost.Address.ToString() + ":" + Port);

        HTTPSession httpSession = new HTTPSession(serverSocket);

        // 執行緒
        ThreadStart serverThreadStart = new ThreadStart(httpSession.HTTPSessionThread);
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
