using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace DateTimeServer
{
  class Server
  {
    /// ���ε{�����D�i�J�I
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

        // ô���]�w���A��Socket�ҨϥΪ�IP��}�P�q�T��
        serverSocket.Bind(serverhost);

        // �]�w���A�ݳ̤j�Τ�ݳs���� Backlog = 50
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
