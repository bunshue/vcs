using System;
using System.IO;
using System.Net;
using System.Text;
using System.Net.Sockets;
using System.Net.Security;
using System.Security.Authentication;
using System.Security.Cryptography.X509Certificates;

namespace SSLClient
{
  class Client
  {
    static void Main(string[] args)
    {
      if (args.Length != 3)
      {
        Console.WriteLine("Usage: SSLClient [SSLServer DNS/IP] [Port] [Message]");
        return;
      }

      string serverHost = args[0];
      int Port = Int32.Parse(args[1]);
      string message = args[2];

      SslStream sslStream = null;

      try
      {
        TcpClient tcpClient = new TcpClient(serverHost, Port);

        Byte[] data = System.Text.Encoding.ASCII.GetBytes(message);

        // 建立支援SSL安全通訊之資料串流
        sslStream = new SslStream(tcpClient.GetStream());

        // 由用戶端呼叫驗證連接中的伺服端並選擇性驗證用戶端
        sslStream.AuthenticateAsClient(serverHost);

        // 判斷驗證（Authentication）是否成功
        if (sslStream.IsAuthenticated)
        {
          Console.WriteLine("IsAuthenticated: {0}", sslStream.IsAuthenticated);
          Console.WriteLine("IsEncrypted: {0}", sslStream.IsEncrypted);
          Console.WriteLine("IsMutuallyAuthenticated: {0}", sslStream.IsMutuallyAuthenticated);
          Console.WriteLine("IsServer: {0}", sslStream.IsServer);
          Console.WriteLine("IsSigned: {0}", sslStream.IsSigned);
        }

        // 資料寫入至串流 
        sslStream.Write(data, 0, data.Length);
        Console.WriteLine("Sent: {0}", message);

        data = new Byte[256];
        string responseData = string.Empty;

        // 從串流中讀取資料
        int bytes = sslStream.Read(data, 0, data.Length);
        responseData = System.Text.Encoding.ASCII.GetString(data, 0, bytes);
        Console.WriteLine("Received: {0}", responseData);
      }
      catch (AuthenticationException ex)
      {
        Console.WriteLine(ex.Message);
      }
      catch (SocketException ex)
      {
        Console.WriteLine(ex.Message);
      }
      catch (IOException ex)
      {
        Console.WriteLine(ex.Message);
      }
      finally
      {
        if (sslStream != null)
          // 關閉串流
          sslStream.Close();
      }

      Console.WriteLine("Press Enter to exit.");
      Console.Read();
    }
  }
}
