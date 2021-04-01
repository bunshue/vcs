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

    private Form1 MainForm;

    // �غc�禡
    public ListenClient(TcpListener tcpListener, Form1 MainForm)
    {
      this.tcpListener = tcpListener;
      this.MainForm = MainForm;
    }

    public void ServerThreadProc()
    {
      NegotiateStream negotiateStream = null;
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

          MainForm.ListBox1.Items.Add("Connection OK to Negotiate Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          data = null;

          // �إߤ䴩�Τ�ݻP���A�ݶ���A�w���ʳq�T��w����Ʀ�y
          negotiateStream = new NegotiateStream(tcpClient.GetStream());

          // �Ѧ��A�ݩI�s���ҳs�������Τ�ݡA�ÿ�ܩ����Ҧ��A��
          negotiateStream.AuthenticateAsServer();

          // �P�_���ҡ]Authentication�^�O�_���\
          if (negotiateStream.IsAuthenticated)
          {

            System.Security.Principal.IIdentity remoteIdentity = negotiateStream.RemoteIdentity;

            MainForm.ListBox1.Items.Add("Client identity: " + remoteIdentity.Name);
            MainForm.ListBox1.Items.Add("Authentication Type: " + remoteIdentity.AuthenticationType);
            MainForm.ListBox1.Items.Add("IsAuthenticated: " + negotiateStream.IsAuthenticated);
            MainForm.ListBox1.Items.Add("IsMutuallyAuthenticated: " + negotiateStream.IsMutuallyAuthenticated);
            MainForm.ListBox1.Items.Add("IsEncrypted: " + negotiateStream.IsEncrypted);
            MainForm.ListBox1.Items.Add("IsSigned: " + negotiateStream.IsSigned);
            MainForm.ListBox1.Items.Add("IsServer: " + negotiateStream.IsServer);
          }

          // �q��y��Ū�����
          int byteData = negotiateStream.Read(bytes, 0, bytes.Length);

          while (byteData != 0)
          {
            data = System.Text.Encoding.ASCII.GetString(bytes, 0, byteData);
            MainForm.ListBox1.Items.Add("Received: " + data);

            byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);

            // ��Ƽg�J�ܦ�y
            negotiateStream.Write(msg, 0, msg.Length);
            MainForm.ListBox1.Items.Add("Sent: " + data);

            // �q��y��Ū�����
            byteData = negotiateStream.Read(bytes, 0, bytes.Length);
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
          if (negotiateStream != null)
            // ������y
            negotiateStream.Close();
        }
      }
    }
  }
}
