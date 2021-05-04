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

        // �إߤ䴩�Τ�ݻP���A�ݶ���A�w���ʳq�T��w����Ʀ�y
        negotiateStream = new NegotiateStream(tcpClient.GetStream());

        // �Τ�ݵn�J�����Φ��A�ݪ��b���P�K�X
        NetworkCredential credential = CredentialCache.DefaultNetworkCredentials;

        // �A�ȥD�n�W�١]Service Primary Name�^�A�N�����Ҧ��A�ݪ��ѧO�W��
        string targetName = "domain\\user";

        // �w���Ҹ�Ʀ�y�ҭn�D���w���ʪA��
        // �[�K��ñ�p��ơA�H��U�T�O��ƶǿ骺���K�ʻP�����
        ProtectionLevel requiredProtectionLevel = ProtectionLevel.EncryptAndSign;

        // �]�w���A�ݳB�z�Ǧp������Τ�ݤ��{��
        // �i�b���������Τ�ݪ��w���ʤ��e�A���L�k�b���ݼ����Τ�ݪ��w���ʤ��e
        TokenImpersonationLevel allowedImpersonationLevel = TokenImpersonationLevel.Impersonation;

        // �ѥΤ�ݩI�s���ҳs�������Τ�ݡA�ÿ�ܩ����Ҧ��A��
        negotiateStream.AuthenticateAsClient(credential, targetName, requiredProtectionLevel, allowedImpersonationLevel);
        // or
        // negotiateStream.AuthenticateAsClient();

        // �P�_���ҡ]Authentication�^�O�_���\
        if (negotiateStream.IsAuthenticated)
        {
          Console.WriteLine("IsAuthenticated: {0}", negotiateStream.IsAuthenticated);
          Console.WriteLine("IsEncrypted: {0}", negotiateStream.IsEncrypted);
          Console.WriteLine("IsMutuallyAuthenticated: {0}", negotiateStream.IsMutuallyAuthenticated);
          Console.WriteLine("IsServer: {0}", negotiateStream.IsServer);
          Console.WriteLine("IsSigned: {0}", negotiateStream.IsSigned);
        }

        // ��Ƽg�J�ܦ�y 
        negotiateStream.Write(data, 0, data.Length);
        Console.WriteLine("Sent: {0}", message);

        data = new Byte[256];
        string responseData = string.Empty;

        // �q��y��Ū�����
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
          // ������y
          negotiateStream.Close();
      }

      Console.WriteLine("Press Enter to exit.");
      Console.Read();
    }
  }
}
