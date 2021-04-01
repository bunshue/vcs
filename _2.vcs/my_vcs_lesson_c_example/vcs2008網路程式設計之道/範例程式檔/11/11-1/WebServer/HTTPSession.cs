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
    // Server Socket
    private System.Net.Sockets.Socket serverSocket;
    // Connection Socket
    private System.Net.Sockets.Socket clientSocket;

    // 建構函式
    public HTTPSession(Socket serverSocket)
    {
      this.serverSocket = serverSocket;
    }

    public void HTTPSessionThread()
    {
      while (true)
      {
        try
        {
          // 建立用戶端瀏覽器與Web Server的連結
          clientSocket = serverSocket.Accept();

          // Socket Information
          IPEndPoint clientInfo = (IPEndPoint)clientSocket.RemoteEndPoint;
          IPEndPoint serverInfo = (IPEndPoint)serverSocket.LocalEndPoint;

          Console.WriteLine("Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString());
          Console.WriteLine("Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          // Set Thread for each HTTP client Connection
          Thread clientThread = new Thread(new ThreadStart(this.ProcessRequest));
          clientThread.Start();
        }
        catch (Exception ex)
        {
          Console.WriteLine(ex.StackTrace.ToString());

          if (clientSocket.Connected)
            clientSocket.Close();
        }
      }
    }


    private void ProcessRequest()
    {
      byte[] recvBytes = new byte[1024];
      string htmlReq = "";
      int bytes;

      try
      {
        // Receive HTTP Request from Web Browser
        bytes = clientSocket.Receive(recvBytes, 0, clientSocket.Available, SocketFlags.None);
        htmlReq = Encoding.ASCII.GetString(recvBytes, 0, bytes);

        Console.WriteLine("HTTP Request: \r\n" + htmlReq);

        // Set WWW Root Path
        string rootPath = Directory.GetCurrentDirectory() + "\\WWWRoot\\";

        // Set default page
        string defaultPage = "index.html";

        string[] strArray;
        string strRequest;

        strArray = htmlReq.Trim().Split(" ".ToCharArray());

        // Determine the HTTP method (GET only)
        if (strArray[0].Trim().ToUpper().Equals("GET"))
        {
          strRequest = strArray[1].Trim().ToString();

          if (strRequest.StartsWith("/"))
            strRequest = strRequest.Substring(1);

          if (strRequest.EndsWith("/") || strRequest.Equals(""))
            strRequest = strRequest + defaultPage;

          strRequest = rootPath + strRequest;
          sendHTMLResponse(strRequest);
        }
        else // HTTP GET method not available
        {
          strRequest = rootPath + "Error\\" + "400.html";
          sendHTMLResponse(strRequest);
        }
      }
      catch (Exception ex)
      {
        Console.WriteLine("Exception: " + ex.StackTrace.ToString());

        if (clientSocket.Connected)
          clientSocket.Close();
      }
    }

    // Send HTTP Response
    private void sendHTMLResponse(string httpRequest)
    {
      try
      {
        // Get the file content of HTTP Request 
        StreamReader streamReader = new StreamReader(httpRequest, Encoding.Default);

        string strBuff = streamReader.ReadToEnd();
        streamReader.Close();
        streamReader = null;

        // Content Length of HTTP Request
        byte[] respByte = Encoding.Default.GetBytes(strBuff);

        // Set HTML Header
        string htmlHeader = "HTTP/1.0 200 OK" + "\r\n" +
          "Server: WebServer 1.0" + "\r\n" +
          "Content-Length: " + respByte.Length + "\r\n" +
          "Content-Type: " + getContentType(httpRequest) +
          "\r\n" + "\r\n";

        // The content Length of HTML Header
        byte[] headerByte = Encoding.ASCII.GetBytes(htmlHeader);

        Console.WriteLine("HTML Header: " + "\r\n" + htmlHeader);

        // 回應HTML標題至用戶端瀏覽器
        clientSocket.Send(headerByte, 0, headerByte.Length, SocketFlags.None);

        // 回應網頁內容至用戶端瀏覽器
        clientSocket.Send(respByte, 0, respByte.Length, SocketFlags.None);

        // Close HTTP Socket connection
        clientSocket.Shutdown(SocketShutdown.Both);
        clientSocket.Close();
      }
      catch (Exception ex)
      {
        Console.WriteLine("Exception: " + ex.StackTrace.ToString());

        if (clientSocket.Connected)
          clientSocket.Close();
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
