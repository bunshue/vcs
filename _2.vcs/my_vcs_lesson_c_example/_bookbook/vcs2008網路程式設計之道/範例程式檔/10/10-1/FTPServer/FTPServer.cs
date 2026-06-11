using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace FTPServer
{
    class FTPServer
    {
        static void Main(string[] args)
        {
            try
            {
                Socket serverSocket = new Socket(AddressFamily.InterNetwork,
                  SocketType.Stream, ProtocolType.Tcp);

                string hostname = Dns.GetHostName();
                IPAddress serverIP = Dns.Resolve(hostname).AddressList[0];

                // Port = 21
                string Port = "21";

                IPEndPoint serverhost = new IPEndPoint(serverIP, Int32.Parse(Port));

                // 繫結設定伺服端Socket所使用的IP位址與通訊埠
                serverSocket.Bind(serverhost);

                // 設定伺服端最大用戶端連結數 Backlog = 50
                serverSocket.Listen(50);

                Console.WriteLine("FTP server started at: " + serverIP.ToString() + ":" + Port);

                FTPSession ftpSession = new FTPSession(serverSocket);

                // 執行緒
                ThreadStart serverThreadStart = new ThreadStart(ftpSession.FTPSessionThread);
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
