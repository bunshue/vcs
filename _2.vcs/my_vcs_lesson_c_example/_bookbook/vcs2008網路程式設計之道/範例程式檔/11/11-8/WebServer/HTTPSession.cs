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

    // �غc�禡
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
          // �HHttpListener���O��GetContext��k���ݶǤJ���Τ�ݽШD 
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
        // �HRequest�ݩʨ��oHTTP���A�ݪ���J��y�A�h�Τ�ݤ��ШD
        httpReq = context.Request;

        //
        // ���HttpListenerRequest���O���ݩʨ��oHTTP�ШD���������e
        //

        // �Τ�ݩү౵����MIME����
        string[] types = httpReq.AcceptTypes;
        if (types != null)
        {
          Console.WriteLine("�Τ�ݩү౵����MIME����:");

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
          Console.WriteLine("   �����ݩ�: {0}", cookie.Domain);
          Console.WriteLine("   ���Ĵ���: {0} (expired? {1})", cookie.Expires, cookie.Expired);
          Console.WriteLine("   URI���|�ݩ�: {0}", cookie.Path);
          Console.WriteLine("   �q�T��: {0}", cookie.Port);
          Console.WriteLine("   �w���h��: {0}", cookie.Secure);
          Console.WriteLine("   �o�X���ɶ�: {0}", cookie.TimeStamp);
          Console.WriteLine("   ����: RFC {0}", cookie.Version == 1 ? "2109" : "2965");
          Console.WriteLine("   ���e: {0}", cookie.ToString());
        }

        // �Τ�ݩҶǰe��Ƥ��e�����D��T
        System.Collections.Specialized.NameValueCollection headers = httpReq.Headers;

        foreach (string key in headers.AllKeys)
        {
          string[] values = headers.GetValues(key);

          if (values.Length > 0)
          {
            Console.WriteLine("�Τ�ݩҶǰe��Ƥ��e�����D��T:");
            foreach (string value in values)
            {
              Console.WriteLine("   {0}", value);
            }
          }
        }

        Console.WriteLine("HTTP�q�T��w��k: {0}", httpReq.HttpMethod);
        Console.WriteLine("HTTP�ШD�O�_�ۥ����e�X? {0}", httpReq.IsLocal);
        Console.WriteLine("�O�_�O������ʳs��: {0}", httpReq.KeepAlive);
        Console.WriteLine("Local End Point: {0}", httpReq.LocalEndPoint.ToString());
        Console.WriteLine("Remote End Point: {0}", httpReq.RemoteEndPoint.ToString());
        Console.WriteLine("HTTP�q�T��w������: {0}", httpReq.ProtocolVersion);
        Console.WriteLine("URL: {0}", httpReq.Url.OriginalString);
        Console.WriteLine("Raw URL: {0}", httpReq.RawUrl);
        Console.WriteLine("Query: {0}", httpReq.QueryString);
        Console.WriteLine("Referred by: {0}", httpReq.UrlReferrer);

        //
        // End of ���HttpListenerRequest���O���ݩʨ��oHTTP�ШD���������e
        //

        // ���o�۹�URL
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

        // �HResponse�ݩʨ��oHTTP���A�ݪ���X��y�A�hHTTP���A�ݤ��^��
        httpResp = context.Response;

        // HTTP�^����Ƥ��e���j�p
        httpResp.ContentLength64 = respByte.Length;

        // HTTP�^����Ƥ��e��MIME�榡
        httpResp.ContentType = getContentType(httpRequest);

        // ���o���A��HTTP�^������Ʀ�y
        System.IO.Stream output = httpResp.OutputStream;

        // �^��HTML�������e�ܥΤ���s����
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
