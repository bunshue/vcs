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

        System.Net.Sockets.TcpListener tcpListener = new TcpListener(serverIP, Int32.Parse(Port));

        tcpListener.Start();

        Console.WriteLine("HTTP server started at: " + serverIP.ToString() + ":" + Port);

        HTTPSession httpSession = new HTTPSession(tcpListener);

        // °õ¦æºü
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
