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

    // 建構函式
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
          // 接受紅外線用戶端的連線
          irdaClient = irdaListener.AcceptIrDAClient();

          // 取得伺服端的輸出入串流
          iostream = irdaClient.GetStream();

          // 判斷串流是否支援讀取功能
          if (iostream.CanRead)
          {
            byte[] bytes = new byte[iostream.Length];

            iostream.Read(bytes, 0, (int)iostream.Length);

            MainForm.txtMessage.Text = MainForm.txtMessage.Text + Encoding.ASCII.GetString(bytes, 0, bytes.Length) + "\r\n";
          }

          // 判斷串流是否支援寫入功能
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
