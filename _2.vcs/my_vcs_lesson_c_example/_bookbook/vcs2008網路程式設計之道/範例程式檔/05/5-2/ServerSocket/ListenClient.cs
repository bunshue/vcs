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

    private Form1 MainForm;

    // �غc�禡
    public ListenClient(Socket serverSocket, Form1 MainForm)
    {
      this.serverSocket = serverSocket;
      this.MainForm = MainForm;
    }

    public void ServerThreadProc()
    {
      while (true)
      {
        try
        {
          // �B�z�Τ�ݳs�u
          clientSocket = serverSocket.Accept();

          // ���o����������������T
          IPEndPoint serverInfo = (IPEndPoint)serverSocket.LocalEndPoint;

          // ���o�s���Τ�ݬ����������s����T
          IPEndPoint clientInfo = (IPEndPoint)clientSocket.RemoteEndPoint;

          MainForm.ListBox1.Items.Add("Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());
          MainForm.ListBox1.Items.Add("Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString());
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }
      }
    }
  }
}
