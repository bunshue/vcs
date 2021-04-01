using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.IO;

namespace InfraServer
{
  class ListenClient
  {
    System.Net.Sockets.IrDAListener irdaListener;
    System.Net.Sockets.IrDAClient irdaClient;

    Form1 MainForm;

    // �غc�禡
    public ListenClient(IrDAListener irdaListener, Form1 MainForm)
    {
      this.irdaListener = irdaListener;
      this.MainForm = MainForm;
    }

    public void ServerThreadProc()
    {
      Stream iostream = null;

      while (true)
      {
        try
        {
          // �������~�u�Τ�ݪ��s�u
          irdaClient = irdaListener.AcceptIrDAClient();

          // ���o���A�ݪ���X�J��y
          iostream = irdaClient.GetStream();

          // �P�_��y�O�_�䴩Ū���\��
          if (iostream.CanRead)
          {
            byte[] bytes = new byte[iostream.Length];

            iostream.Read(bytes, 0, (int)iostream.Length);

            MainForm.txtMessage.Text = MainForm.txtMessage.Text + Encoding.ASCII.GetString(bytes, 0, bytes.Length) + "\r\n";
          }

          // �P�_��y�O�_�䴩�g�J�\��
          if (iostream.CanWrite)
          {
            byte[] msg = Encoding.ASCII.GetBytes("Message from Infrared Server");

            iostream.Write(msg, 0, msg.Length);
          }

          iostream.Close();
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());

          if (iostream != null)
            iostream.Close();

          if (irdaClient != null)
            irdaClient.Close();
        }
      }
    }
  }
}
