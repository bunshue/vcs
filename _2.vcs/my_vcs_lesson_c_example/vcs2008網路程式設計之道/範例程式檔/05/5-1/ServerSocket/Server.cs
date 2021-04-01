using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ServerSocket
{
  class Server
  {
    /// ���ε{�����D�i�J�I
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

        // ô���]�w���A��Socket�ҨϥΪ�IP��}�P�q�T��
        serverSocket.Bind(serverhost);

        // �]�w���A�ݳ̤j�Τ�ݳs����
        serverSocket.Listen(int.MaxValue);

        Console.WriteLine("Server started at: " + serverIP.ToString() + ":" + Port);

        ListenClient lc = new ListenClient(serverSocket);

        // �����
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
