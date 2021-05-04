using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.IO;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace WebCam
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    int device = 0;
    int hwnd;

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
      btnStart.Enabled = true;
      btnSave.Enabled = false;

      StartWebCam();
    }

    private void StartWebCam()
    {
      // 建立視訊裝置的控制代碼 (Handle to a Window) 
      // 並輸出至指定的PictureBox物件中
      hwnd = capCreateCaptureWindowA("WebCam", (WS_CHILD | WS_VISIBLE), 0, 0, 0, 0, picCapture.Handle.ToInt32(), 0);

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
        SetWindowPos(hwnd, HWND_BOTTOM, 0, 0, picCapture.Width, picCapture.Height, (SWP_NOMOVE | SWP_NOZORDER));
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
      btnSave.Enabled = true;

      // 停止視訊裝置
      SendMessage(hwnd, WM_CAP_DRIVER_DISCONNECT, device, 0);
      DestroyWindow(hwnd);

      StartWebCam();

      // 錄影
      SendMessage(hwnd, WM_CAP_SEQUENCE, 0, 0);
    }

    private void btnSave_Click(object sender, EventArgs e)
    {
      btnStart.Enabled = true;
      btnSave.Enabled = false;

      string file = Directory.GetCurrentDirectory() + "\\file.avi";

      // 儲存影像
      SendMessage(hwnd, WM_CAP_FILE_SAVEAS, 0, file);

      MessageBox.Show("影像已被儲存至" + file, "Information", MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    private void btnStop_Click(object sender, EventArgs e)
    {
      btnStart.Enabled = true;
      btnSave.Enabled = false;

      // 停止視訊裝置
      SendMessage(hwnd, WM_CAP_DRIVER_DISCONNECT, device, 0);
      DestroyWindow(hwnd);
    }
  }
}
