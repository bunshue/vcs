using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace WebServer
{
  class WebServer
  {
    static void Main(string[] args)
    {
      try
      {
        // �P�_�@�~�t�άO�_�䴩
        if (!System.Net.HttpListener.IsSupported)
        {
          Console.WriteLine("�@�~�t�Τ��䴩HttpListener���O");
          return;
        }

        System.Net.HttpListener listener = new System.Net.HttpListener();

        // HTTP Server Port = 8080
        string Port = "8080";

        string prefix = "http://*:" + Port + "/";

        // �]�wPrefixes�ݩʡA�H���wHTTP���A�ݪ�IP��}�γq�T��
        listener.Prefixes.Add(prefix);

        // ���ԦۥΤ�ݪ��s�u�ШD
        listener.Start();

        Console.WriteLine("HTTP server started at: " + Dns.GetHostName() + ":" + Port);

        HTTPSession httpSession = new HTTPSession(listener);

        // �����
        ThreadStart serverThreadStart = new ThreadStart(httpSession.HTTPSessionThread);
        Thread serverthread = new Thread(serverThreadStart);

        serverthread.Start();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }
  }
}
