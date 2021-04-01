using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.IO;
using System.Net.Security;
using System.Security.Authentication;
using System.Security.Principal;

namespace NegotiateClient
{
  class Client
  {
    static void Main(string[] args)
    {
      if (args.Length != 3)
      {
        Console.WriteLine("Usage: NegotiateClient [NegotiateServer DNS/IP] [Port] [Message]");
        return;
      }

      string serverHost = args[0];
      int Port = Int32.Parse(args[1]);
      string message = args[2];

      NegotiateStream negotiateStream = null;

      try
      {
        TcpClient tcpClient = new TcpClient(serverHost, Port);

        Byte[] data = System.Text.Encoding.ASCII.GetBytes(message);

        // 建立支援用戶端與伺服端間交涉安全性通訊協定之資料串流
        negotiateStream = new NegotiateStream(tcpClient.GetStream());

        // 用戶端登入網路或伺服端的帳號與密碼
        NetworkCredential credential = CredentialCache.DefaultNetworkCredentials;

        // 服務主要名稱（Service Primary Name），代表驗證伺服端的識別名稱
        string targetName = "domain\\user";

        // 已驗證資料串流所要求的安全性服務
        // 加密並簽署資料，以協助確保資料傳輸的機密性與完整性
        ProtectionLevel requiredProtectionLevel = ProtectionLevel.EncryptAndSign;

        // 設定伺服端處理序如何模擬用戶端之認證
        // 可在本機模擬用戶端的安全性內容，但無法在遠端模擬用戶端的安全性內容
        TokenImpersonationLevel allowedImpersonationLevel = TokenImpersonationLevel.Impersonation;

        // 由用戶端呼叫驗證連接中之用戶端，並選擇性驗證伺服端
        negotiateStream.AuthenticateAsClient(credential, targetName, requiredProtectionLevel, allowedImpersonationLevel);
        // or
        // negotiateStream.AuthenticateAsClient();

        // 判斷驗證（Authentication）是否成功
        if (negotiateStream.IsAuthenticated)
        {
          Console.WriteLine("IsAuthenticated: {0}", negotiateStream.IsAuthenticated);
          Console.WriteLine("IsEncrypted: {0}", negotiateStream.IsEncrypted);
          Console.WriteLine("IsMutuallyAuthenticated: {0}", negotiateStream.IsMutuallyAuthenticated);
          Console.WriteLine("IsServer: {0}", negotiateStream.IsServer);
          Console.WriteLine("IsSigned: {0}", negotiateStream.IsSigned);
        }

        // 資料寫入至串流 
        negotiateStream.Write(data, 0, data.Length);
        Console.WriteLine("Sent: {0}", message);

        data = new Byte[256];
        string responseData = string.Empty;

        // 從串流中讀取資料
        int bytes = negotiateStream.Read(data, 0, data.Length);
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
        if (negotiateStream != null)
          // 關閉串流
          negotiateStream.Close();
      }

      Console.WriteLine("Press Enter to exit.");
      Console.Read();
    }
  }
}
