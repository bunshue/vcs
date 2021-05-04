using System;
using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Text;

namespace DateTimeClient
{
  class Client
  {
    static void Main(string[] args)
    {
      if (args.Length != 1)
      {
        Console.WriteLine("Usage: DateTimeClient [DateTimeServer DNS/IP]");

        return;
      }

      string serverHost = args[0];

      TcpClient tcpClient = new TcpClient();
      Stream networkStream;

      try
      {
        tcpClient.Connect(serverHost, 13);

        networkStream = tcpClient.GetStream();
      }
      catch (Exception)
      {
        Console.WriteLine("Can not connect to {0}", serverHost);
        return;
      }

      try
      {
        if (networkStream.CanRead)
        {
          byte[] recvbytes = new byte[tcpClient.ReceiveBufferSize];

          int i = networkStream.Read(recvbytes, 0, (int)tcpClient.ReceiveBufferSize);

          string datetime = Encoding.ASCII.GetString(recvbytes, 0, i);

          Console.WriteLine("Receive {0} bytes.", i);
          Console.WriteLine("Current server date/Time: {0}", datetime);
        }
        else
        {
          Console.WriteLine("Network Input Stream is unreadable.");
          tcpClient.Close();
          return;
        }

        tcpClient.Close();
      }
      catch (Exception ec)
      {
        Console.WriteLine(ec.StackTrace.ToString());
        return;
      }
      Console.WriteLine("Press any key to exit.");
      Console.Read();
    }
  }
}
