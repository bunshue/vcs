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

    private Form1 MainForm;

    // �غc�禡
    public ListenClient(TcpListener tcpListener, Form1 MainForm)
    {
      this.tcpListener = tcpListener;
      this.MainForm = MainForm;
    }

    public void ServerThreadProc()
    {
      SslStream sslStream = null;
      byte[] bytes = new byte[256];
      string data = null;

      while (true)
      {
        MainForm.ListBox1.Items.Add("Waiting for a connection... ");
        try
        {
          // �B�z�Τ�ݳs�u
          tcpClient = tcpListener.AcceptTcpClient();

          // ���o����������������T
          IPEndPoint serverInfo = (IPEndPoint)tcpListener.LocalEndpoint;
          MainForm.ListBox1.Items.Add("Connection OK to SSL Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

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
            MainForm.ListBox1.Items.Add("IsAuthenticated: " + sslStream.IsAuthenticated);
            MainForm.ListBox1.Items.Add("IsEncrypted: " + sslStream.IsEncrypted);
            MainForm.ListBox1.Items.Add("IsMutuallyAuthenticated: " + sslStream.IsMutuallyAuthenticated);
            MainForm.ListBox1.Items.Add("IsServer: " + sslStream.IsServer);
            MainForm.ListBox1.Items.Add("IsSigned: " + sslStream.IsSigned);
          }

          // �q��y��Ū�����
          int byteData = sslStream.Read(bytes, 0, bytes.Length);

          while (byteData != 0)
          {
            data = System.Text.Encoding.ASCII.GetString(bytes, 0, byteData);
            MainForm.ListBox1.Items.Add("Received: " + data);

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

            // ��Ƽg�J�ܦ�y
            sslStream.Write(msg, 0, msg.Length);
            MainForm.ListBox1.Items.Add("Sent: " + data);

            // �q��y��Ū�����
            byteData = sslStream.Read(bytes, 0, bytes.Length);
          }
        }
        catch (AuthenticationException aex)
        {
          MainForm.ListBox1.Items.Add(aex.StackTrace.ToString());
        }
        catch (SocketException ex)
        {
          MainForm.ListBox1.Items.Add(ex.StackTrace.ToString());
        }
        catch (IOException ioex)
        {
          MainForm.ListBox1.Items.Add(ioex.StackTrace.ToString());
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