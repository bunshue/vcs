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
        // 判斷作業系統是否支援
        if (!System.Net.HttpListener.IsSupported)
        {
          Console.WriteLine("作業系統不支援HttpListener類別");
          return;
        }

        System.Net.HttpListener listener = new System.Net.HttpListener();

        // HTTP Server Port = 8080
        string Port = "8080";

        string prefix = "http://*:" + Port + "/";

        // 設定Prefixes屬性，以指定HTTP伺服端的IP位址及通訊埠
        listener.Prefixes.Add(prefix);

        // 等候自用戶端的連線請求
        listener.Start();

        Console.WriteLine("HTTP server started at: " + Dns.GetHostName() + ":" + Port);

        HTTPSession httpSession = new HTTPSession(listener);

        // 執行緒
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
