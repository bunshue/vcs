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

    // �غc�禡
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
          // �B�z�Τ�ݳs�u
          tcpClient = tcpListener.AcceptTcpClient();

          // ���o����������������T
          IPEndPoint serverInfo = (IPEndPoint)tcpListener.LocalEndpoint;
          Console.WriteLine("Connection OK to SSL Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          data = null;

          // �إߤ䴩SSL�w���q�T����Ʀ�y
          sslStream = new SslStream(tcpClient.GetStream());

          // �إߦ��A�ݾ���
          // �����ɮ׬�test.cer
          System.Security.Cryptography.X509Certificates.X509Certificate certificate = X509Certificate.CreateFromCertFile("test.cer");

          // �Ѧ��A�ݩI�s���ҳs���������A�ݡA�ÿ�ܩ����ҥΤ��
          sslStream.AuthenticateAsServer(certificate);
          // or �HSSL 3.0��TLS 1.0�q�T��w�i��w���q�T
          // sslStream.AuthenticateAsServer(certificate, true, SslProtocols.Default, true);

          // �P�_���ҡ]Authentication�^�O�_���\
          if (sslStream.IsAuthenticated)
          {
            Console.WriteLine("IsAuthenticated: {0}", sslStream.IsAuthenticated);
            Console.WriteLine("IsEncrypted: {0}", sslStream.IsEncrypted);
            Console.WriteLine("IsMutuallyAuthenticated: {0}", sslStream.IsMutuallyAuthenticated);
            Console.WriteLine("IsServer: {0}", sslStream.IsServer);
            Console.WriteLine("IsSigned: {0}", sslStream.IsSigned);
          }

          // �q��y��Ū�����
          int byteData = sslStream.Read(bytes, 0, bytes.Length);

          while (byteData != 0)
          {
            data = System.Text.Encoding.ASCII.GetString(bytes, 0, byteData);
            Console.WriteLine("Received: {0}", data);

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

            // ��Ƽg�J�ܦ�y
            sslStream.Write(msg, 0, msg.Length);
            Console.WriteLine("Sent: {0}", data);

            // �q��y��Ū�����
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
            // ������y
            sslStream.Close();
        }
      }
    }
  }
}