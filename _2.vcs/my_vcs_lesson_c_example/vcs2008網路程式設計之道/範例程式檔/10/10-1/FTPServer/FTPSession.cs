using System;
using System.Collections.Generic;
using System.Text;

using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.IO;

namespace FTPServer
{
  class FTPSession
  {
    // Server Socket
    private System.Net.Sockets.Socket serverSocket;
    // Connection Socket
    private System.Net.Sockets.Socket clientSocket;
    // Data Socket
    private System.Net.Sockets.Socket dataSocket;

    // FTP Root Path
    private string rootPath = Directory.GetCurrentDirectory() + "\\FTPRoot\\";
    private string currentPath;
    private string currentPathStr = "/";

    private string loginName = "";
    private bool blnBinary;

    // Data Socket IP and Port
    private string clientIP = "";
    private int dataPort;

    // 建構函式
    public FTPSession(Socket serverSocket)
    {
      this.serverSocket = serverSocket;
      this.currentPath = rootPath;
    }

    public void FTPSessionThread()
    {
      while (true)
      {
        try
        {
          clientSocket = serverSocket.Accept();

          // Socket Information
          IPEndPoint clientInfo = (IPEndPoint)clientSocket.RemoteEndPoint;
          IPEndPoint serverInfo = (IPEndPoint)serverSocket.LocalEndPoint;

          Console.WriteLine("Client: " + clientInfo.Address.ToString() + ":" + clientInfo.Port.ToString());
          Console.WriteLine("Server: " + serverInfo.Address.ToString() + ":" + serverInfo.Port.ToString());

          // Set Thread for each FTP client Connection
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

    private void resetDefault()
    {
      currentPath = rootPath;
      currentPathStr = "/";
      Console.WriteLine("currentPath: " + currentPath);
    }

    private void showMessage(string Msg)
    {
      byte[] sendByte = Encoding.Default.GetBytes(Msg + "\r\n");

      clientSocket.Send(sendByte, 0, sendByte.Length, SocketFlags.None);
      Console.WriteLine(Msg);
    }

    private void showData(string Msg)
    {
      IPAddress dataIP = Dns.Resolve(clientIP).AddressList[0];
      IPEndPoint dataHost = new IPEndPoint(dataIP, dataPort);

      try
      {
        byte[] sendByte = Encoding.Default.GetBytes(Msg);

        // Establish data connection
        dataSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        dataSocket.Connect(dataHost);

        dataSocket.Send(sendByte, 0, sendByte.Length, SocketFlags.None);
        Console.WriteLine(Msg);

        dataSocket.Close();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
        dataSocket.Close();
      }
    }

    private void ProcessRequest()
    {
      byte[] recvBytes = new byte[128];

      string ftpCmd = "";
      string strDate = DateTime.Now.ToShortDateString() + " " + DateTime.Now.ToLongTimeString();
      string strMsg;
      int bytes;

      strMsg = "220 .Net FTP Server (Version 1.0.0) " + strDate + "\r\n" + "220 Welcome to .NET FTP Server";

      showMessage(strMsg);

      ftpCmd = "";

      // if FTP command is not "QUIT"
      while (!(ftpCmd.ToLower().StartsWith("quit")))
      {
        try
        {
          bytes = clientSocket.Receive(recvBytes);
          ftpCmd = Encoding.ASCII.GetString(recvBytes, 0, bytes);

          Console.WriteLine("FTP Command: " + ftpCmd);

          ftpCommand(ftpCmd);
        }
        catch (Exception ex)
        {
          Console.WriteLine("Exception: " + ex.StackTrace.ToString());
          ftpCmd = "quit";
        }
      }

      // Close FTP Session
      try
      {
        if (clientSocket.Connected)
          clientSocket.Close();
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.StackTrace.ToString());
      }
    }

    private void ftpCommand(string cmd)
    {
      string[] ftpCmdtok;
      string strArg;
      string ftpCmd = "";

      if (cmd == null)
        cmd = "";

      ftpCmdtok = cmd.Trim().Split(" ".ToCharArray());

      ftpCmd = ftpCmdtok[0].ToLower().Trim();

      // user: Login
      // 表示使用者的登錄名稱
      if (ftpCmd.Equals("user"))
      {
        try
        {
          loginName = ftpCmdtok[1].Trim();

          if (loginName.ToLower().Trim() == "anonymous")
            showMessage("331 Anonymous access allowed, send identity (e-mail name) as password.");
          else
            showMessage("331 Password required for " + loginName + ".");
        }
        catch
        {
          showMessage("500 User syntax.");
        }
      }

      // pass: Verify password
      // 表示使用者密碼
      else if (ftpCmd.Equals("pass"))
      {
        // Add the logic of verifying password here
        showMessage("230 " + loginName + " user logged in.");
        resetDefault();
      }

      // quit
      // 結束FTP Client端與Server端的通訊連結
      else if (ftpCmd.Equals("quit"))
      {
        showMessage("221 Service closing control connection. Goodbye.");
        resetDefault();
      }

      // port
      else if (ftpCmd.Equals("port"))
      {
        string[] strPort;

        try
        {
          // PORT h1,h2,h3,h4,p1,p2
          strPort = ftpCmdtok[1].Trim().Split(",".ToCharArray());

          // h1
          clientIP = strPort[0].ToString() + "." + strPort[1].ToString() + "." + strPort[2].ToString() + "." + strPort[3].ToString();

          // Port = p1 * 256 + p2
          dataPort = Int32.Parse(strPort[4].ToString()) * 256 + Int32.Parse(strPort[5].ToString());

          // Demo only 
          showMessage("PORT " + ftpCmdtok[1].Trim() + ".");
          showMessage("200 PORT command successful.");
        }
        catch
        {
          showMessage("500 PORT number syntax.");
        }
      }

      // list: List Directory (dir)
      // 列出FTP Server端目錄與檔案的詳細內容
      // 包括建檔日期、時間、檔案大小、目錄與檔案名稱等
      else if (ftpCmd.Equals("list"))
      {
        if (ftpCmdtok.Length > 1)
          strArg = ftpCmdtok[1].Trim();
        else
          strArg = "";

        listDirectory(strArg, true);
      }

      // NLST: Name List (ls)
      // 僅顯示目錄與檔案名稱，不顯示其詳細內容
      else if (ftpCmd.Equals("nlst"))
      {
        if (ftpCmdtok.Length > 1)
          strArg = ftpCmdtok[1].Trim();
        else
          strArg = "";

        listDirectory(strArg, false);
      }

      // cdup: Change to Parent Directory
      // 用以改變FTP Server至使用者根目錄
      else if (ftpCmd.Equals("cdup"))
      {
        changeDirectory(".");
      }

      // cwd: Change Directory (cd)
      // 改變目前FTP Server的工作目錄
      else if (ftpCmd.Equals("cwd"))
      {
        strArg = ftpCmdtok[1].Trim();
        changeDirectory(strArg);
      }

      // xpwd: Current Directory (pwd)
      // 顯示FTP Server端的目錄
      else if (ftpCmd.Equals("xpwd"))
      {
        showMessage("257 \"" + currentPathStr + "\" is current directory.");
        Console.WriteLine("Physical Path: " + currentPath);
      }

      // xmkd: Make Directory (mkdir)
      // 建立FTP Server端的目錄
      else if (ftpCmd.Equals("xmkd"))
      {
        strArg = ftpCmdtok[1].Trim();
        makeDirectory(strArg);
      }

      // xrmd: Remove Directory (rmdir)
      // 移除FTP Server端的目錄
      else if (ftpCmd.Equals("xrmd"))
      {
        strArg = ftpCmdtok[1].Trim();
        removeDirectory(strArg);
      }

      // dele: Remove File (delete)
      // 刪除FTP Server端檔案
      else if (ftpCmd.Equals("dele"))
      {
        strArg = ftpCmdtok[1].Trim();
        removeFile(strArg);
      }

      // noop: No Operation
      else if (ftpCmd.Equals("noop"))
      {
        showMessage("200 OK.");
      }

      // syst
      else if (ftpCmd.Equals("syst"))
      {
        showMessage("215 .NET FTP Server.");
      }

      //  help: Remote Help (remotehelp)
      else if (ftpCmd.Equals("help"))
      {
        string strHelp;
        strHelp = "214-The following commands are recognized(* ==>//s unimplemented).... " + "\r\n" + "214 HELP command successful.";
        showMessage(strHelp);
      }

      // type
      // 資料型態（Data Type）
      else if (ftpCmd.Equals("type"))
      {
        try
        {
          strArg = ftpCmdtok[1].Trim();

          // Binary
          if (strArg.ToLower().IndexOf("i") != -1)
          {
            blnBinary = true;
            showMessage("200 TYPE set to I.");
          }
          // ASCII
          else if (strArg.ToLower().IndexOf("a") != -1)
          {
            blnBinary = false;
            showMessage("200 TYPE set to A.");
          }
          else
            showMessage("500 TYPE " + strArg + " syntax.");
        }
        catch
        {
          showMessage("500 TYPE syntax.");
        }
      }

      // mode
      // 傳輸模式（Transmission Mode）
      else if (ftpCmd.Equals("mode"))
      {
        try
        {
          strArg = ftpCmdtok[1].Trim();

          if (strArg.ToLower().Equals("s"))
            showMessage("200 MODE S.");
          else
            showMessage("500 MODE " + strArg + " syntax.");
        }
        catch
        {
          showMessage("500 MODE syntax.");
        }
      }

      // stru
      // 資料結構（Data Structure）
      else if (ftpCmd.Equals("stru"))
      {
        try
        {
          strArg = ftpCmdtok[1].Trim();

          if (strArg.ToLower().Equals("f"))
            showMessage("200 STRU F.");
          else
            showMessage("501 STRU " + strArg + " not found.");
        }
        catch
        {
          showMessage("500 STRU syntax.");
        }
      }

      else
        showMessage("502 " + ftpCmd + " not implemented. Invalid command.");
    }

    // Change Directory
    private void changeDirectory(string ftpPath)
    {
      string strPath = "";

      try
      {
        if (ftpPath == "." || ftpPath == "/")
          strPath = rootPath;
        else if (ftpPath.StartsWith(".."))
        {
          if (currentPath == rootPath)
            strPath = rootPath;
          else
          {
            if (currentPath.EndsWith("\\"))
            {
              strPath = currentPath.Substring(0, currentPath.Length - 1);
              strPath = strPath.Substring(0, strPath.LastIndexOf("\\") + 1);
            }
            else
              strPath = currentPath.Substring(0, currentPath.LastIndexOf("\\") + 1);
          }
        }
        else if (ftpPath.StartsWith("\\"))
          strPath = currentPath + ftpPath.Substring(1, ftpPath.Length);
        else
          strPath = currentPath + ftpPath;

        if (!strPath.EndsWith("\\"))
          strPath = strPath + "\\";

        // File
        if (Path.GetFileName(strPath) != "")
        {
          showMessage("550 " + ftpPath + " is not a directory.");
          return;
        }

        DirectoryInfo dirInfo = new DirectoryInfo(strPath);

        // Path is Read-Only
        if (dirInfo.Attributes == FileAttributes.ReadOnly)
        {
          showMessage("550 " + ftpPath + ": Access is denied.");
          return;
        }

        if (Directory.Exists(strPath))
        {
          // Change Directory
          Directory.SetCurrentDirectory(strPath);
          currentPath = strPath;

          if (currentPath == rootPath)
            currentPathStr = "/";
          else
            currentPathStr = "/" + currentPath.Replace(rootPath, "");

          currentPathStr = currentPathStr.Replace("\\", "/");

          if (currentPathStr.EndsWith("/") && currentPathStr.Length > 1)
            currentPathStr = currentPathStr.Substring(0, currentPathStr.Length - 1);

          showMessage("250 CWD command successful. " + currentPathStr);
        }
        else
          showMessage("550 " + ftpPath + " is not a subdirectory of " + currentPathStr + ".");
      }
      catch (Exception ex)
      {
        showMessage("500 " + ex.StackTrace.ToString());
      }
    }

    // Create a new directory
    private void makeDirectory(string ftpPath)
    {
      string strPath = "";

      try
      {
        if (ftpPath.StartsWith("\\"))
          ftpPath = ftpPath.Substring(1, ftpPath.Length);

        strPath = currentPath + ftpPath;

        if (!strPath.EndsWith("\\"))
          strPath = strPath + "\\";

        Console.WriteLine("New Path: " + strPath);

        DirectoryInfo dirInfo = new DirectoryInfo(currentPath);

        // Path is Read-Only
        if (dirInfo.Attributes == FileAttributes.ReadOnly)
        {
          showMessage("550 " + ftpPath + ": Access is denied.");
          return;
        }

        // Directory Exists
        if (Directory.Exists(strPath))
          showMessage("550 " + ftpPath + ": Cannot create a file/path when that file/path already exists.");
        else
        {
          Directory.CreateDirectory(strPath);
          showMessage("257 \"" + ftpPath + "\" directory created.");
        }
      }
      catch (Exception ex)
      {
        showMessage("500 " + ex.StackTrace.ToString());
      }
    }

    // Delete a existing directory
    private void removeDirectory(string ftpPath)
    {
      string strPath = "";

      try
      {
        if (ftpPath.StartsWith("\\"))
          ftpPath = ftpPath.Substring(1, ftpPath.Length);

        strPath = currentPath + ftpPath;

        if (!strPath.EndsWith("\\"))
          strPath = strPath + "\\";

        Console.WriteLine("Delete Path: " + strPath);

        if (Directory.Exists(strPath))
        {
          DirectoryInfo dirInfo = new DirectoryInfo(currentPath);

          // Path is Read-Only
          if (dirInfo.Attributes == FileAttributes.ReadOnly)
          {
            showMessage("550 " + ftpPath + ": Access is denied.");
            return;
          }

          string[] fileEntries, dirEntries;
          fileEntries = Directory.GetFiles(strPath);
          dirEntries = Directory.GetDirectories(strPath);

          // Directory is empty
          if (fileEntries.Length == 0 && dirEntries.Length == 0)
          {
            // Delete Directory 
            Directory.Delete(strPath);
            showMessage("250 RMD command successful.");
          }
          else
            showMessage("550 " + ftpPath + ": The directory is not empty.");
        }
        else
          showMessage("550 " + ftpPath + " is not existed.");
      }
      catch (Exception ex)
      {
        showMessage("500 " + ex.StackTrace.ToString());
      }
    }

    // Delete a existing file
    private void removeFile(string ftpFile)
    {
      string strFile = "";

      try
      {
        if (ftpFile.StartsWith("\\"))
          ftpFile = ftpFile.Substring(1, ftpFile.Length);

        strFile = currentPath + ftpFile;

        Console.WriteLine("Delete File: " + strFile);

        if (File.Exists(strFile))
        {
          FileInfo fileInfo = new FileInfo(strFile);

          // File is Read-Only
          if (fileInfo.Attributes == FileAttributes.ReadOnly)
            showMessage("550 " + ftpFile + ": Access is denied.");
          else
          {
            // Delete File 
            File.Delete(strFile);
            showMessage("250 DELE command successful.");
          }
        }
        else
          showMessage("550 " + ftpFile + ": The system cannot find the file specified.");
      }
      catch (Exception ex)
      {
        showMessage("500 " + ex.StackTrace.ToString());
      }
    }

    // ls / list / nlst
    private void listDirectory(string strList, bool showDetail)
    {
      string strPath = "";
      string strBuff = "";

      if (strList == "")
        strPath = currentPath;
      else
        strPath = currentPath + strList;

      if (Directory.Exists(strPath))
      {
        if (blnBinary)
        {
          if (showDetail)
            showMessage("150 Opening Binary mode data connection /bin/ls.");
          else
            showMessage("150 Opening Binary mode data connection for file list.");
        }
        else
        {
          if (showDetail)
            showMessage("150 Opening ASCII mode data connection /bin/ls.");
          else
            showMessage("150 Opening ASCII mode data connection for file list.");
        }

        string[] fileEntries = Directory.GetFiles(strPath);
        FileInfo fileInfo;
        string strName, strSize, strDate, strSpace;

        // 顯示檔案內容
        foreach (string fileName in fileEntries)
        {
          if (showDetail)
          {
            // 顯示詳細檔案內容

            fileInfo = new FileInfo(fileName);

            strDate = fileInfo.LastWriteTime.ToString("MM-dd-yy  HH:mm");
            strSize = fileInfo.Length.ToString();
            strName = fileName.Substring(fileName.LastIndexOf("\\") + 1);

            strSpace = new string((char)32, 20 - strSize.Length);

            strBuff = strBuff + strDate + strSpace + strSize + " " + strName + "\r\n";
          }
          else
          {
            // 僅顯示檔案名稱
            strName = fileName.Substring(fileName.LastIndexOf("\\") + 1);
            strBuff = strBuff + strName + "\r\n";
          }
        }

        string[] dirEntries = Directory.GetDirectories(strPath);
        DirectoryInfo dirInfo;

        // 顯示目錄內容
        foreach (string dirName in dirEntries)
        {
          if (showDetail)
          {
            // 顯示詳細目錄內容
            dirInfo = new DirectoryInfo(dirName);

            strDate = dirInfo.LastWriteTime.ToString("MM-dd-yy  HH:mm");
            strName = dirName.Substring(dirName.LastIndexOf("\\") + 1);
            strBuff = strBuff + strDate + "       <DIR>         " + strName + "\r\n";
          }
          else
          {
            // 僅顯示目錄名稱
            strName = dirName.Substring(dirName.LastIndexOf("\\") + 1);
            strBuff = strBuff + strName + "\r\n";
          }
        }

        // Use data port to send path information 
        showData(strBuff);

        byte[] sendByte = Encoding.Default.GetBytes(strBuff);

        showMessage("226 Transfer complete.");

        // Demo only
        showMessage("ftp: " + sendByte.Length + " bytes received.");
      }
      else
        showMessage(strPath + " is not a valid file or directory.");
    }
  }
}
