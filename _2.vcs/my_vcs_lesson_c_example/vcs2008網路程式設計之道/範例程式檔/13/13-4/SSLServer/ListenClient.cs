using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.IO;
using System.Net.Security;
using System.Security.Authentication;
using System.Security.Cryptography;
using System.Security.Cryptography.X509Certificates;

namespace SSLServer
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
      SslStream sslStream = null;
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
          Console.WriteLine("Connection OK to SSL Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          data = null;

          // 建立支援SSL安全通訊之資料串流
          sslStream = new SslStream(tcpClient.GetStream());

          // 建立伺服端憑證
          // 憑證檔案為test.cer
          System.Security.Cryptography.X509Certificates.X509Certificate certificate = X509Certificate.CreateFromCertFile("test.cer");

          // 由伺服端呼叫驗證連接中的伺服端，並選擇性驗證用戶端
          sslStream.AuthenticateAsServer(certificate);
          // or 以SSL 3.0或TLS 1.0通訊協定進行安全通訊
          // sslStream.AuthenticateAsServer(certificate, true, SslProtocols.Default, true);

          // 判斷驗證（Authentication）是否成功
          if (sslStream.IsAuthenticated)
          {
            Console.WriteLine("IsAuthenticated: {0}", sslStream.IsAuthenticated);
            Console.WriteLine("IsEncrypted: {0}", sslStream.IsEncrypted);
            Console.WriteLine("IsMutuallyAuthenticated: {0}", sslStream.IsMutuallyAuthenticated);
            Console.WriteLine("IsServer: {0}", sslStream.IsServer);
            Console.WriteLine("IsSigned: {0}", sslStream.IsSigned);
          }

          // 從串流中讀取資料
          int byteData = sslStream.Read(bytes, 0, bytes.Length);

          while (byteData != 0)
          {
            data = System.Text.Encoding.ASCII.GetString(bytes, 0, byteData);
            Console.WriteLine("Received: {0}", data);

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

            // 資料寫入至串流
            sslStream.Write(msg, 0, msg.Length);
            Console.WriteLine("Sent: {0}", data);

            // 從串流中讀取資料
            byteData = sslStream.Read(bytes, 0, bytes.Length);
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
          if (sslStream != null)
            // 關閉串流
            sslStream.Close();
        }
      }
    }
  }
}