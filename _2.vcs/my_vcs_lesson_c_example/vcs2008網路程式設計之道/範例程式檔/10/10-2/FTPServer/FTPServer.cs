using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace FTPServer
{
  class FTPServer
  {
    static void Main(string[] args)
    {
      try
      {
        string hostname = Dns.GetHostName();
        IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

        // Port = 21
        string Port = "21";

        IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

        System.Net.Sockets.TcpListener tcpListener = new TcpListener(serverIP, Int32.Parse(Port));

        tcpListener.Start();

        Console.WriteLine("FTP server started at: " + serverIP.ToString() + ":" + Port);

        FTPSession ftpSession = new FTPSession(tcpListener);

        // °õ¦æºü
        ThreadStart serverThreadStart = new ThreadStart(ftpSession.FTPSessionThread);
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
