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
    private System.Net.Sockets.TcpListener tcpListener;
    // Connection Socket
    private System.Net.Sockets.Socket clientSocket;

    // 建構函式
    public HTTPSession(TcpListener tcpListener)
    {
      this.tcpListener = tcpListener;
    }

    public void HTTPSessionThread()
    {
      while (true)
      {
        try
        {
          // 建立用戶端瀏覽器與Web Server的連結
          clientSocket = tcpListener.AcceptSocket();

          // Socket Information
          IPEndPoint clientInfo = (IPEndPoint)clientSocket.RemoteEndPoint;

          Console.WriteLine("Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString());

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
        FileStream fs = new FileStream(httpRequest, FileMode.Open, FileAccess.Read, FileShare.None);
        BinaryReader br = new BinaryReader(fs);

        // The content Length of HTTP Request
        byte[] respByte = new byte[(int)fs.Length];
        br.Read(respByte, 0, (int)fs.Length);

        br.Close();
        fs.Close();

        // Set HTML Header
        string htmlHeader = "HTTP/1.0 200 OK" + "\r\n" +
          "Server: WebServer 1.0" + "\r\n" +
          "Content-Length: " + respByte.Length + "\r\n" +
          "Content-Type: " + getContentType(httpRequest) +
          "\r\n" + "\r\n";

        // Content Length of HTML Header
        byte[] headerByte = Encoding.ASCII.GetBytes(htmlHeader);

        Console.WriteLine("HTML Header: " + "\r\n" + htmlHeader);

        // Send HTML Header back to Web Browser
        clientSocket.Send(headerByte, 0, headerByte.Length, SocketFlags.None);

        // Send HTML Content back to Web Browser
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
