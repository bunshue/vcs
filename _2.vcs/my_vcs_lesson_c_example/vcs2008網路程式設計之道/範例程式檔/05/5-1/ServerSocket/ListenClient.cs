using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ServerSocket
{
  class ListenClient
  {
    private System.Net.Sockets.Socket serverSocket;
    private System.Net.Sockets.Socket clientSocket;

    // 建構函式
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
          // 處理用戶端連線
          clientSocket = serverSocket.Accept();

          // 取得本機相關的網路資訊
          IPEndPoint serverInfo = (IPEndPoint)serverSocket.LocalEndPoint;

          // 取得連結用戶端相關的網路連接資訊
          IPEndPoint clientInfo = (IPEndPoint)clientSocket.RemoteEndPoint;

          Console.WriteLine("Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());
          Console.WriteLine("Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString());
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }
      }
    }
  }
}
