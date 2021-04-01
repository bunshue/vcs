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

    // �غc�禡
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
          // �B�z�Τ�ݳs�u
          tcpClient = tcpListener.AcceptTcpClient();

          // ���o����������������T
          IPEndPoint serverInfo = (IPEndPoint)tcpListener.LocalEndpoint;

          Console.WriteLine("Connection OK to Negotiate Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          data = null;

          // �إߤ䴩�Τ�ݻP���A�ݶ���A�w���ʳq�T��w����Ʀ�y
          negotiateStream = new NegotiateStream(tcpClient.GetStream());

          // �Ѧ��A�ݩI�s���ҳs�������Τ�ݡA�ÿ�ܩ����Ҧ��A��
          negotiateStream.AuthenticateAsServer();

          // �P�_���ҡ]Authentication�^�O�_���\
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

          // �q��y��Ū�����
          int byteData = negotiateStream.Read(bytes, 0, bytes.Length);

          while (byteData != 0)
          {
            data = System.Text.Encoding.ASCII.GetString(bytes, 0, byteData);
            Console.WriteLine("Received: {0}", data);

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

            // ��Ƽg�J�ܦ�y
            negotiateStream.Write(msg, 0, msg.Length);
            Console.WriteLine("Sent: {0}", data);

            // �q��y��Ū�����
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
            // ������y
            negotiateStream.Close();
        }
      }
    }
  }
}