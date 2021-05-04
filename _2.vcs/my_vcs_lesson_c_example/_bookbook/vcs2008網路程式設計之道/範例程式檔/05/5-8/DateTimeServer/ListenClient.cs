using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Text;

namespace DateTimeServer
{
  class ListenClient
  {
    private System.Net.Sockets.Socket serverSocket;
    private System.Net.Sockets.Socket clientSocket;

    // «Øºc¨ç¦¡
    public ListenClient(Socket serverSocket)
    {
      this.serverSocket = serverSocket;
    }

    public void ServerThreadProc()
    {
      while (true)
      {
        try
        {
          clientSocket = serverSocket.Accept();

          IPEndPoint clientInfo = (IPEndPoint)clientSocket.RemoteEndPoint;
          IPEndPoint serverInfo = (IPEndPoint)serverSocket.LocalEndPoint;

          Console.WriteLine("Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString());
          Console.WriteLine("Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          string strDate = DateTime.Now.ToShortDateString() + " " + DateTime.Now.ToLongTimeString();

          byte[] byteDate = Encoding.ASCII.GetBytes(strDate.ToCharArray());

          clientSocket.Send(byteDate, 0, byteDate.Length, SocketFlags.None);

          Console.WriteLine("To Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString() + ": " + strDate);

          clientSocket.Shutdown(SocketShutdown.Both);
          clientSocket.Close();
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());

          if (clientSocket.Connected)
            clientSocket.Close();
        }
      }
    }
  }
}
