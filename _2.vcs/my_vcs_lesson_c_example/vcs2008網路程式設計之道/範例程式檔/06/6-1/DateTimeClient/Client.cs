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

      try
      {
        IPAddress hostadd = Dns.Resolve(serverHost).AddressList[0];
        IPEndPoint EPhost = new IPEndPoint(hostadd, 13);

        Socket clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

        clientSocket.Connect(EPhost);

        byte[] recvbytes = new byte[1024];

        int i = clientSocket.Receive(recvbytes, 0, clientSocket.Available, SocketFlags.None);

        string datetime = Encoding.ASCII.GetString(recvbytes, 0, i);

        Console.WriteLine("Receive {0} bytes.", i);
        Console.WriteLine("Current server date/Time: {0}", datetime);

        clientSocket.Shutdown(SocketShutdown.Both);
        clientSocket.Close();
      }
      catch (Exception e)
      {
        Console.WriteLine(e.StackTrace.ToString());
        return;
      }
      Console.WriteLine("Press any key to exit.");
      Console.Read();
    }
  }
}
