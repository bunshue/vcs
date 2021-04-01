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

        // ô���]�w���A��Socket�ҨϥΪ�IP��}�P�q�T��
        serverSocket.Bind(serverhost);

        // �]�w���A�ݳ̤j�Τ�ݳs���� Backlog = 100
        serverSocket.Listen(100);

        Console.WriteLine("HTTP server started at: " + serverhost.Address.ToString() + ":" + Port);

        HTTPSession httpSession = new HTTPSession(serverSocket);

        // �����
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
