using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace ServerSocket
{
  class ListenClient
  {
    private System.Net.Sockets.TcpListener tcpListener;
    private System.Net.Sockets.TcpClient tcpClient;

    private Form1 MainForm;

    // 建構函式
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
          // 處理用戶端連線
          tcpClient = tcpListener.AcceptTcpClient();

          // 取得本機相關的網路資訊
          IPEndPoint serverInfo = (IPEndPoint)tcpListener.LocalEndpoint;

          MainForm.ListBox1.Items.Add("Connection OK to Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());
        }
        catch (Exception ex)
        {
          MainForm.ListBox1.Items.Add(ex.StackTrace.ToString());
        }
      }
    }
  }
}
