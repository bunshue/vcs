using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ServerSocket
{
  class ListenClient
  {
    private System.Net.Sockets.TcpListener tcpListener;
    private System.Net.Sockets.Socket clientSocket;

    private Form1 MainForm;

    // �غc�禡
    public ListenClient(TcpListener tcpListener, Form1 MainForm)
    {
      this.tcpListener = tcpListener;
      this.MainForm = MainForm;
    }

    public void ServerThreadProc()
    {
      while (true)
      {
        try
        {
          // �B�z�Τ�ݳs�u
          clientSocket = tcpListener.AcceptSocket();

          // ���o����������������T
          IPEndPoint serverInfo = (IPEndPoint)tcpListener.LocalEndpoint;

          // ���o�s���Τ�ݬ����������s����T
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
