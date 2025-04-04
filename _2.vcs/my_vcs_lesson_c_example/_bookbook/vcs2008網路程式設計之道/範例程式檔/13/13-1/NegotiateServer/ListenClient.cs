using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.IO;
using System.Net.Security;
using System.Security.Authentication;

namespace NegotiateServer
{
  class ListenClient
  {
    private System.Net.Sockets.TcpListener tcpListener;
    private System.Net.Sockets.TcpClient tcpClient;

    // 建構函式
    public ListenClient(TcpListener tcpListener)
    {
      this.tcpListener = tcpListener;
    }

    public void ServerThreadProc()
    {
      NegotiateStream negotiateStream = null;
      byte[] bytes = new byte[256];
      string data = null;

      while (true)
      {
        Console.WriteLine("Waiting for a connection... ");
        try
        {
          // 處理用戶端連線
          tcpClient = tcpListener.AcceptTcpClient();

          // 取得本機相關的網路資訊
          IPEndPoint serverInfo = (IPEndPoint)tcpListener.LocalEndpoint;

          Console.WriteLine("Connection OK to Negotiate Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          data = null;

          // 建立支援用戶端與伺服端間交涉安全性通訊協定之資料串流
          negotiateStream = new NegotiateStream(tcpClient.GetStream());

          // 由伺服端呼叫驗證連接中之用戶端，並選擇性驗證伺服端
          negotiateStream.AuthenticateAsServer();

          // 判斷驗證（Authentication）是否成功
          if (negotiateStream.IsAuthenticated)
          {

            System.Security.Principal.IIdentity remoteIdentity = negotiateStream.RemoteIdentity;

            Console.WriteLine("Client identity: {0}", remoteIdentity.Name);
            Console.WriteLine("Authentication Type: {0}", remoteIdentity.AuthenticationType);
            Console.WriteLine("IsAuthenticated: {0}", negotiateStream.IsAuthenticated);
            Console.WriteLine("IsMutuallyAuthenticated: {0}", negotiateStream.IsMutuallyAuthenticated);
            Console.WriteLine("IsEncrypted: {0}", negotiateStream.IsEncrypted);
            Console.WriteLine("IsSigned: {0}", negotiateStream.IsSigned);
            Console.WriteLine("IsServer: {0}", negotiateStream.IsServer);
          }

          // 從串流中讀取資料
          int byteData = negotiateStream.Read(bytes, 0, bytes.Length);

          while (byteData != 0)
          {
            data = System.Text.Encoding.ASCII.GetString(bytes, 0, byteData);
            Console.WriteLine("Received: {0}", data);

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

            // 資料寫入至串流
            negotiateStream.Write(msg, 0, msg.Length);
            Console.WriteLine("Sent: {0}", data);

            // 從串流中讀取資料
            byteData = negotiateStream.Read(bytes, 0, bytes.Length);
          }
        }
        catch (AuthenticationException aex)
        {
          Console.WriteLine(aex.StackTrace.ToString());
        }
        catch (SocketException ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }
        catch (IOException ioex)
        {
          Console.WriteLine(ioex.StackTrace.ToString());
        }
        finally
        {
          if (negotiateStream != null)
            // 關閉串流
            negotiateStream.Close();
        }
      }
    }
  }
}