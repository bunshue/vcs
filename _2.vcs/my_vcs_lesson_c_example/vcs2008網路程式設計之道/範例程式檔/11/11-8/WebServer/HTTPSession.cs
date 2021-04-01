using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Text;
using System.IO;

namespace WebServer
{
  public class HTTPSession
  {
    System.Net.HttpListener listener = null;
    System.Net.HttpListenerRequest httpReq = null;
    System.Net.HttpListenerResponse httpResp = null;
    System.Net.HttpListenerContext context = null;

    // 建構函式
    public HTTPSession(HttpListener listener)
    {
      this.listener = listener;
    }

    public void HTTPSessionThread()
    {
      while (true)
      {
        try
        {
          // 以HttpListener類別的GetContext方法等待傳入之用戶端請求 
          context = listener.GetContext();

          // Set Thread for each HTTP client Connection
          Thread clientThread = new Thread(new ThreadStart(this.ProcessRequest));
          clientThread.Start();
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());
        }
      }
    }

    private void ProcessRequest()
    {
      // Set WWW Root Path
      string rootPath = Directory.GetCurrentDirectory() + "\\WWWRoot\\";

      // Set default page
      string defaultPage = "index.html";

      try
      {
        // 以Request屬性取得HTTP伺服端的輸入串流，則用戶端之請求
        httpReq = context.Request;

        //
        // 顯示HttpListenerRequest類別的屬性取得HTTP請求之相關內容
        //

        // 用戶端所能接受的MIME類型
        string[] types = httpReq.AcceptTypes;
        if (types != null)
        {
          Console.WriteLine("用戶端所能接受的MIME類型:");

          foreach (string type in types)
          {
            Console.WriteLine("   {0}", type);
          }
        }

        // Content Length
        Console.WriteLine("Content Length {0}", httpReq.ContentLength64);

        // Content Type
        if (httpReq.ContentType != null)
        {
          Console.WriteLine("Content Type {0}", httpReq.ContentType);
        }

        // Cookie
        foreach (Cookie cookie in httpReq.Cookies)
        {
          Console.WriteLine("Cookie:");
          Console.WriteLine("   {0} = {1}", cookie.Name, cookie.Value);
          Console.WriteLine("   網域屬性: {0}", cookie.Domain);
          Console.WriteLine("   有效期限: {0} (expired? {1})", cookie.Expires, cookie.Expired);
          Console.WriteLine("   URI路徑屬性: {0}", cookie.Path);
          Console.WriteLine("   通訊埠: {0}", cookie.Port);
          Console.WriteLine("   安全層級: {0}", cookie.Secure);
          Console.WriteLine("   發出的時間: {0}", cookie.TimeStamp);
          Console.WriteLine("   版本: RFC {0}", cookie.Version == 1 ? "2109" : "2965");
          Console.WriteLine("   內容: {0}", cookie.ToString());
        }

        // 用戶端所傳送資料內容的標題資訊
        System.Collections.Specialized.NameValueCollection headers = httpReq.Headers;

        foreach (string key in headers.AllKeys)
        {
          string[] values = headers.GetValues(key);

          if (values.Length > 0)
          {
            Console.WriteLine("用戶端所傳送資料內容的標題資訊:");
            foreach (string value in values)
            {
              Console.WriteLine("   {0}", value);
            }
          }
        }

        Console.WriteLine("HTTP通訊協定方法: {0}", httpReq.HttpMethod);
        Console.WriteLine("HTTP請求是否自本機送出? {0}", httpReq.IsLocal);
        Console.WriteLine("是否保持持續性連結: {0}", httpReq.KeepAlive);
        Console.WriteLine("Local End Point: {0}", httpReq.LocalEndPoint.ToString());
        Console.WriteLine("Remote End Point: {0}", httpReq.RemoteEndPoint.ToString());
        Console.WriteLine("HTTP通訊協定的版本: {0}", httpReq.ProtocolVersion);
        Console.WriteLine("URL: {0}", httpReq.Url.OriginalString);
        Console.WriteLine("Raw URL: {0}", httpReq.RawUrl);
        Console.WriteLine("Query: {0}", httpReq.QueryString);
        Console.WriteLine("Referred by: {0}", httpReq.UrlReferrer);

        //
        // End of 顯示HttpListenerRequest類別的屬性取得HTTP請求之相關內容
        //

        // 取得相對URL
        string url = httpReq.RawUrl;

        if (url.StartsWith("/"))
          url = url.Substring(1);

        if (url.EndsWith("/") || url.Equals(""))
          url = url + defaultPage;

        string strRequest = rootPath + url;

        sendHTMLResponse(strRequest);
      }
      catch (Exception ex)
      {
        Console.WriteLine("Exception: " + ex.StackTrace.ToString());
      }
    }

    // Send HTTP Response
    private void sendHTMLResponse(string httpRequest)
    {
      try
      {
        // Get the file content of HTTP Request 
        FileStream fs = new FileStream(httpRequest, FileMode.Open, FileAccess.Read, FileShare.None);
        BinaryReader br = new BinaryReader(fs);

        // The content Length of HTTP Request
        byte[] respByte = new byte[(int)fs.Length];
        br.Read(respByte, 0, (int)fs.Length);

        br.Close();
        fs.Close();

        // 以Response屬性取得HTTP伺服端的輸出串流，則HTTP伺服端之回應
        httpResp = context.Response;

        // HTTP回應資料內容的大小
        httpResp.ContentLength64 = respByte.Length;

        // HTTP回應資料內容的MIME格式
        httpResp.ContentType = getContentType(httpRequest);

        // 取得伺服端HTTP回應之資料串流
        System.IO.Stream output = httpResp.OutputStream;

        // 回應HTML網頁內容至用戶端瀏覽器
        output.Write(respByte, 0, respByte.Length);

        output.Close();
        httpResp.Close();
      }
      catch (Exception ex)
      {
        Console.WriteLine("Exception: " + ex.StackTrace.ToString());

        if (httpResp != null)
          httpResp.Close();
      }
    }

    // MIME: Get Content Type
    private string getContentType(string httpRequest)
    {
      if (httpRequest.EndsWith("html"))
        return "text/html";
      else if (httpRequest.EndsWith("htm"))
        return "text/html";
      else if (httpRequest.EndsWith("txt"))
        return "text/plain";
      else if (httpRequest.EndsWith("gif"))
        return "image/gif";
      else if (httpRequest.EndsWith("jpg"))
        return "image/jpeg";
      else if (httpRequest.EndsWith("jpeg"))
        return "image/jpeg";
      else if (httpRequest.EndsWith("pdf"))
        return "application/pdf";
      else if (httpRequest.EndsWith("pdf"))
        return "application/pdf";
      else if (httpRequest.EndsWith("doc"))
        return "application/msword";
      else if (httpRequest.EndsWith("xls"))
        return "application/vnd.ms-excel";
      else if (httpRequest.EndsWith("ppt"))
        return "application/vnd.ms-powerpoint";
      else
        return "text/plain";
    }
  }
}
