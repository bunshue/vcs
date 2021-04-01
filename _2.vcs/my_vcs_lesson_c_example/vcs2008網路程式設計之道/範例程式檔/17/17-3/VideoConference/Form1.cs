using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.Net;
using System.Net.Sockets;
using System.IO;
using System.Drawing;
using System.Drawing.Imaging;
using System.Threading;
using System.Collections;

namespace VideoConference
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    int device = 0;
    int hwnd;

    TcpListener tcpListener;
    NetworkStream clientStream;
    Thread localThread;

    // 宣告Windows API
    const int WM_USER = 0x400;
    const int WM_CAP_DRIVER_CONNECT = WM_USER + 10;
    const int WM_CAP_DRIVER_DISCONNECT = WM_USER + 11;
    const int WM_CAP_FILE_SAVEAS = WM_USER + 23;
    const int WM_CAP_EDIT_COPY = WM_USER + 30;
    const int WM_CAP_SET_PREVIEW = WM_USER + 50;
    const int WM_CAP_SET_PREVIEWRATE = WM_USER + 52;
    const int WM_CAP_SET_SCALE = WM_USER + 53;
    const int WM_CAP_SEQUENCE = WM_USER + 62;

    const int WS_CHILD = 0x40000000;
    const int WS_VISIBLE = 0x10000000;
    const short SWP_NOSIZE = 1;
    const short SWP_NOMOVE = 2;
    const short SWP_NOZORDER = 4;
    const short HWND_BOTTOM = 1;

    [DllImport("avicap32.dll")]
    static extern int capCreateCaptureWindowA(string lpszWindowName, int dwStyle, int x, int y, int nWidth, int nHeight, int hWndParent, int nID);

    //[DllImport("avicap32.dll")]
    //static extern bool capGetDriverDescriptionA(short wDriver, byte[] lpszName, int cbName, byte[] lpszVer, int cbVer);

    [DllImport("user32.dll", EntryPoint = "SendMessageA")]
    static extern int SendMessage(int hwnd, int wMsg, int wParam, [MarshalAs(UnmanagedType.AsAny)] object lParam);

    [DllImport("user32.dll", EntryPoint = "SetWindowPos")]
    static extern int SetWindowPos(int hwnd, int hWndInsertAfter, int x, int y, int cx, int cy, int wFlags);

    [DllImport("user32.dll")]
    static extern bool DestroyWindow(int hndw);

    private void Form1_Load(object sender, EventArgs e)
    {
      StartWebCam();
    }

    private void Form1_FormClosing(object sender, FormClosingEventArgs e)
    {
      try
      {
        tcpListener.Stop();
        localThread.Abort();
      }
      catch (Exception) { }
    }

    private void StartWebCam()
    {
      // 建立視訊裝置的控制代碼 (Handle to a Window) 
      // 並輸出至指定的PictureBox物件中
      hwnd = capCreateCaptureWindowA("WebCam", (WS_CHILD | WS_VISIBLE), 0, 0, 0, 0, picLocal.Handle.ToInt32(), 0);

      // 連接至視訊裝置
      if (SendMessage(hwnd, WM_CAP_DRIVER_CONNECT, device, 0) == 1)
      {
        // 設定預覽比率
        SendMessage(hwnd, WM_CAP_SET_SCALE, 1, 0);
        // 設定預覽速率
        SendMessage(hwnd, WM_CAP_SET_PREVIEWRATE, 30, 0);
        // 開始視訊裝置預覽
        SendMessage(hwnd, WM_CAP_SET_PREVIEW, 1, 0);
        // 調整預覽大小至PictureBox
        SetWindowPos(hwnd, HWND_BOTTOM, 0, 0, picLocal.Width, picLocal.Height, (SWP_NOMOVE | SWP_NOZORDER));
      }
      else
      {
        // 無法連接至視訊裝置
        DestroyWindow(hwnd);

        MessageBox.Show("無法連接至視訊裝置.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);

        Environment.Exit(0);
      }
    }

    private void btnStart_Click(object sender, EventArgs e)
    {
      btnStart.Enabled = false;

      // 停止視訊裝置
      SendMessage(hwnd, WM_CAP_DRIVER_DISCONNECT, device, 0);
      DestroyWindow(hwnd);

      StartWebCam();

      // 錄影
      SendMessage(hwnd, WM_CAP_SEQUENCE, 0, 0);
    }

    private void btnStop_Click(object sender, EventArgs e)
    {
      btnStart.Enabled = true;

      // 停止視訊裝置
      SendMessage(hwnd, WM_CAP_DRIVER_DISCONNECT, device, 0);
      DestroyWindow(hwnd);
    }

    private void btnSend_Click(object sender, EventArgs e)
    {
      if (txtHost.Text != "")
        timer1.Enabled = true;
      else
        MessageBox.Show("請輸入遠端IP位址或DNS名稱.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
    }

    private void btnListen_Click(object sender, EventArgs e)
    {
      btnListen.Enabled = false;

      localThread = new Thread(new ThreadStart(ReceiveVideo));
      localThread.Start();
    }

    private void ReceiveVideo()
    {
      try
      {
        // 設定伺服端所需使用的IP位址與通訊埠
        tcpListener = new TcpListener(Dns.Resolve(Dns.GetHostName()).AddressList[0], 5000);
        // 開始接聽等候用戶端的網路連結請求
        tcpListener.Start();
        // 建立用戶端連線
        Socket clientSocket = tcpListener.AcceptSocket();
        // 建立伺服端的輸出入串流
        NetworkStream serverStream = new NetworkStream(clientSocket);

        // 自輸出入串流中取得影像
        this.picRemote.Image = Image.FromStream(serverStream);

        // 關閉伺服端服務
        tcpListener.Stop();

        if (clientSocket.Connected == true)
        {
          while (true)
          {
            ReceiveVideo();
          }
        }
        clientStream.Flush();

      }
      catch (Exception)
      {
        btnListen.Enabled = true;
        localThread.Abort();
      }
    }

    private void timer1_Tick(object sender, EventArgs e)
    {
      int port = 5000;

      try
      {
        // 複雜影像至剪貼簿(Clipboard)
        SendMessage(hwnd, WM_CAP_EDIT_COPY, 0, 0);

        // 自剪貼簿(Clipboard)取得物件
        IDataObject data = Clipboard.GetDataObject();

        // 建立記憶體的資料流
        System.IO.MemoryStream memStream = new System.IO.MemoryStream();

        if (data.GetDataPresent(typeof(System.Drawing.Bitmap)))
        {
          Image image = ((Image)(data.GetData(typeof(System.Drawing.Bitmap))));

          // 將影像依指定格式儲存至指定的資料流
          image.Save(memStream, ImageFormat.Bmp);
        }

        // 將影像依指定格式儲存至指定的資料流
        picLocal.Image.Save(memStream, ImageFormat.Jpeg);

        // 回傳記憶體資料流之位元組陣列
        byte[] buffer = memStream.GetBuffer();

        // 建立用戶端TcpClient
        TcpClient tcpClient = new TcpClient(txtHost.Text, port);
        // 取得用戶端的輸出入串流
        clientStream = tcpClient.GetStream();

        // 建立BinaryWriter
        BinaryWriter binarywriter = new BinaryWriter(clientStream);
        binarywriter.Write(buffer);
        binarywriter.Flush();
        binarywriter.Close();

        memStream.Flush();
        memStream.Close();

        clientStream.Flush();
        clientStream.Close();

        tcpClient.Close();
      }
      catch (Exception ex)
      {
        MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
      }
    }
  }
}
