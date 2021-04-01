using System;
using System.Collections.Generic;
using System.Text;

using System.IO;
using System.Drawing;
using System.Drawing.Imaging;

// Windows API
using System.Runtime.InteropServices;

public class RemoteControl : System.MarshalByRefObject
{
  //
  // 常數宣告
  //
  const int SM_CXSCREEN = 0; // 為GetSystemMetrics()API之參數，代表螢幕的寬度(pixel)
  const int SM_CYSCREEN = 1; // 為GetSystemMetrics()API之參數，代表螢幕的高度(pixel)

  // 滑鼠事件
  const uint MOUSEEVENTF_LEFTDOWN = 0x0002;   // 按下滑鼠左鍵 
  const uint MOUSEEVENTF_LEFTUP = 0x0004;     // 釋放滑鼠左鍵 
  const uint MOUSEEVENTF_RIGHTDOWN = 0x0008;  // 按下滑鼠右鍵 
  const uint MOUSEEVENTF_RIGHTUP = 0x0010;    // 釋放滑鼠右鍵 

  // 滑鼠輸入
  const uint INPUT_MOUSE = 0;

  // 滑鼠參數之結構
  struct MOUSEINPUT
  {
    public uint dx;          // x coordinate of the mouse
    public uint dy;          // y coordinate of the mouse
    public uint mouseData;   // If dwFlags contains MOUSEEVENTF_WHEEL, then mouseData provides the amount of wheel movement. Otherwise, it is 0.
    public uint dwFlags;     // Set of bit flags that indicate various aspects of mouse motion and button clicks.
    public uint time;        // Time stamp for the event, in milliseconds
    public uint dwExtraInfo; // Ignored
  }

  // 鍵盤參數之結構
  struct KEYBDINPUT
  {
    public ushort wVk;       // virtual-key code
    public ushort wScan;     // hardware scan code for the key
    public uint dwFlags;     // various aspects of a keystroke
    public uint time;        // Ignored
    public uint dwExtraInfo; // Ignored
  }

  [StructLayout(LayoutKind.Explicit)]
  struct INPUT
  {
    [FieldOffset(0)]
    public uint type;

    // union
    [FieldOffset(4)]
    public MOUSEINPUT mi;

    [FieldOffset(4)]
    public KEYBDINPUT ki;
  }

  //
  // Windows API宣告
  //

  // Keystrokes, mouse motions, and button clicks
  [DllImport("user32.dll")]
  static extern uint SendInput(uint nInputs, ref INPUT pInputs, int cbSize);

  // 取得螢幕的寬度與高度
  [DllImport("user32.dll")]
  static extern int GetSystemMetrics(int nIndex);

  // 取得視窗的控制代碼
  [DllImport("user32.dll")]
  static extern IntPtr GetDesktopWindow();

  // 自來源(Source)裝置內容控制代碼移轉Pixel至目的(Destination)裝置內容控制代碼
  [DllImport("gdi32.dll")]
  static extern bool BitBlt(IntPtr hdcDest, int nXDest, int nYDest,
      int nWidth, int nHeight, IntPtr hdcSrc, int nXSrc, int nYSrc, System.Int32 dwRop);

  // 設定滑鼠
  [DllImport("user32.dll")]
  static extern void SetCursorPos(int x, int y);

  // 
  // 自訂 function
  //

  // 判斷滑鼠輸入
  public void MouseButtonCall(bool mouse_press, bool left, int x, int y)
  {
    INPUT mouseinput = new INPUT();

    // 滑鼠輸入 = 0
    mouseinput.type = INPUT_MOUSE;
    mouseinput.mi.dx = (uint)x;   // x coordinate of the mouse
    mouseinput.mi.dy = (uint)y;   // y coordinate of the mouse
    mouseinput.mi.mouseData = 0;
    mouseinput.mi.dwFlags = 0;
    mouseinput.mi.time = 0;
    mouseinput.mi.dwExtraInfo = 0;

    if (left)  /* 滑鼠左鍵 */
      mouseinput.mi.dwFlags = mouse_press ? MOUSEEVENTF_LEFTDOWN : MOUSEEVENTF_LEFTUP;
    else       /* 滑鼠右鍵 */
      mouseinput.mi.dwFlags = mouse_press ? MOUSEEVENTF_RIGHTDOWN : MOUSEEVENTF_RIGHTUP;

    // 定義傳入SendInput之結構數目
    uint nInputs = 1;

    SendInput(nInputs, ref mouseinput, Marshal.SizeOf(mouseinput));
  }

  // 移動滑鼠
  public void MoveMouse(int x, int y)
  {
    SetCursorPos(x, y);
  }

  // 取得螢幕之位元組陣列
  public byte[] GetDesktopBuffer()
  {
    // 取得螢幕的寬度與高度並建立Size物件
    System.Drawing.Size desktopsize = new System.Drawing.Size(GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN));

    // 取得視窗的控制代碼 (Handle to a Window) 
    IntPtr hwnd = GetDesktopWindow();

    // 從視窗控制代碼建立新的Graphics物件
    System.Drawing.Graphics graphics = System.Drawing.Graphics.FromHwnd(hwnd);

    // 封裝 GDI+ 點陣圖並建立Bitmap物件
    // 參數: 
    //   width: 新Bitmap的寬度
    //   height: 新Bitmap的高度
    //   grapics: 新Bitmap解析度的Graphics物件
    System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap(desktopsize.Width, desktopsize.Height, graphics);

    // 從指定的Image建立新Graphics物件
    System.Drawing.Graphics bitmapGraphics = System.Drawing.Graphics.FromImage(bitmap);

    // 取得來源區域之裝置內容控制代碼 (Handle to a Device Context)
    IntPtr hdcSrc = graphics.GetHdc();

    // 取得目的區域之裝置內容控制代碼
    IntPtr hdcDest = bitmapGraphics.GetHdc();

    // 自來源區域之裝置內容控制代碼位元區塊轉移至目的區域之裝置內容控制代碼
    BitBlt(hdcDest, 0, 0, desktopsize.Width, desktopsize.Height, hdcSrc, 0, 0, 0xCC0020);

    // 釋放由裝置內容控制代碼。 
    graphics.ReleaseHdc(hdcSrc);

    // 釋放由裝置內容控制代碼。 
    bitmapGraphics.ReleaseHdc(hdcDest);

    // 釋放Graphics物件所使用的所有資源 
    graphics.Dispose();

    // 釋放Graphics物件所使用的所有資源 
    bitmapGraphics.Dispose();

    /******************/
    /* 繪製虛擬游標 */
    /******************/

    // 設定滑鼠游標為箭號游標
    System.Windows.Forms.Cursor cursor = System.Windows.Forms.Cursors.Arrow;

    // 設定矩形左上角的 X 座標
    int x = System.Windows.Forms.Cursor.Position.X - 10;
    // 設定矩形左上角的 Y 座標
    int y = System.Windows.Forms.Cursor.Position.Y - 10;
    // 設定矩形的寬度
    int width = cursor.Size.Width;
    // 設定矩形的高度
    int height = cursor.Size.Height;

    // 從指定的Image建立新Graphics物件
    System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(bitmap);

    // 建立新Rectangle物件
    System.Drawing.Rectangle targetRect = new Rectangle(x, y, width, height);

    // 在指定的範圍內繪製虛擬游標
    cursor.Draw(g, targetRect);

    /*****************************/
    /* 儲存影像至記憶體資料流 */
    /*****************************/

    // 建立記憶體的資料流
    System.IO.MemoryStream memStream = new System.IO.MemoryStream();

    // 指定儲存之影像格式為JPEG格式
    System.Drawing.Imaging.ImageFormat format = System.Drawing.Imaging.ImageFormat.Jpeg;

    // 將影像以指定格式儲存至記憶體資料流
    bitmap.Save(memStream, format);

    // 回傳記憶體資料流之位元組陣列
    return memStream.GetBuffer();
  }
}
