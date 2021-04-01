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
  // �`�ƫŧi
  //
  const int SM_CXSCREEN = 0; // ��GetSystemMetrics()API���ѼơA�N��ù����e��(pixel)
  const int SM_CYSCREEN = 1; // ��GetSystemMetrics()API���ѼơA�N��ù�������(pixel)

  // �ƹ��ƥ�
  const uint MOUSEEVENTF_LEFTDOWN = 0x0002;   // ���U�ƹ����� 
  const uint MOUSEEVENTF_LEFTUP = 0x0004;     // ����ƹ����� 
  const uint MOUSEEVENTF_RIGHTDOWN = 0x0008;  // ���U�ƹ��k�� 
  const uint MOUSEEVENTF_RIGHTUP = 0x0010;    // ����ƹ��k�� 

  // �ƹ���J
  const uint INPUT_MOUSE = 0;

  // �ƹ��ѼƤ����c
  struct MOUSEINPUT
  {
    public uint dx;          // x coordinate of the mouse
    public uint dy;          // y coordinate of the mouse
    public uint mouseData;   // If dwFlags contains MOUSEEVENTF_WHEEL, then mouseData provides the amount of wheel movement. Otherwise, it is 0.
    public uint dwFlags;     // Set of bit flags that indicate various aspects of mouse motion and button clicks.
    public uint time;        // Time stamp for the event, in milliseconds
    public uint dwExtraInfo; // Ignored
  }

  // ��L�ѼƤ����c
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
  // Windows API�ŧi
  //

  // Keystrokes, mouse motions, and button clicks
  [DllImport("user32.dll")]
  static extern uint SendInput(uint nInputs, ref INPUT pInputs, int cbSize);

  // ���o�ù����e�׻P����
  [DllImport("user32.dll")]
  static extern int GetSystemMetrics(int nIndex);

  // ���o����������N�X
  [DllImport("user32.dll")]
  static extern IntPtr GetDesktopWindow();

  // �ۨӷ�(Source)�˸m���e����N�X����Pixel�ܥت�(Destination)�˸m���e����N�X
  [DllImport("gdi32.dll")]
  static extern bool BitBlt(IntPtr hdcDest, int nXDest, int nYDest,
      int nWidth, int nHeight, IntPtr hdcSrc, int nXSrc, int nYSrc, System.Int32 dwRop);

  // �]�w�ƹ�
  [DllImport("user32.dll")]
  static extern void SetCursorPos(int x, int y);

  // 
  // �ۭq function
  //

  // �P�_�ƹ���J
  public void MouseButtonCall(bool mouse_press, bool left, int x, int y)
  {
    INPUT mouseinput = new INPUT();

    // �ƹ���J = 0
    mouseinput.type = INPUT_MOUSE;
    mouseinput.mi.dx = (uint)x;   // x coordinate of the mouse
    mouseinput.mi.dy = (uint)y;   // y coordinate of the mouse
    mouseinput.mi.mouseData = 0;
    mouseinput.mi.dwFlags = 0;
    mouseinput.mi.time = 0;
    mouseinput.mi.dwExtraInfo = 0;

    if (left)  /* �ƹ����� */
      mouseinput.mi.dwFlags = mouse_press ? MOUSEEVENTF_LEFTDOWN : MOUSEEVENTF_LEFTUP;
    else       /* �ƹ��k�� */
      mouseinput.mi.dwFlags = mouse_press ? MOUSEEVENTF_RIGHTDOWN : MOUSEEVENTF_RIGHTUP;

    // �w�q�ǤJSendInput�����c�ƥ�
    uint nInputs = 1;

    SendInput(nInputs, ref mouseinput, Marshal.SizeOf(mouseinput));
  }

  // ���ʷƹ�
  public void MoveMouse(int x, int y)
  {
    SetCursorPos(x, y);
  }

  // ���o�ù����줸�հ}�C
  public byte[] GetDesktopBuffer()
  {
    // ���o�ù����e�׻P���רëإ�Size����
    System.Drawing.Size desktopsize = new System.Drawing.Size(GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN));

    // ���o����������N�X (Handle to a Window) 
    IntPtr hwnd = GetDesktopWindow();

    // �q��������N�X�إ߷s��Graphics����
    System.Drawing.Graphics graphics = System.Drawing.Graphics.FromHwnd(hwnd);

    // �ʸ� GDI+ �I�}�Ϩëإ�Bitmap����
    // �Ѽ�: 
    //   width: �sBitmap���e��
    //   height: �sBitmap������
    //   grapics: �sBitmap�ѪR�ת�Graphics����
    System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap(desktopsize.Width, desktopsize.Height, graphics);

    // �q���w��Image�إ߷sGraphics����
    System.Drawing.Graphics bitmapGraphics = System.Drawing.Graphics.FromImage(bitmap);

    // ���o�ӷ��ϰ줧�˸m���e����N�X (Handle to a Device Context)
    IntPtr hdcSrc = graphics.GetHdc();

    // ���o�ت��ϰ줧�˸m���e����N�X
    IntPtr hdcDest = bitmapGraphics.GetHdc();

    // �ۨӷ��ϰ줧�˸m���e����N�X�줸�϶��ಾ�ܥت��ϰ줧�˸m���e����N�X
    BitBlt(hdcDest, 0, 0, desktopsize.Width, desktopsize.Height, hdcSrc, 0, 0, 0xCC0020);

    // ����Ѹ˸m���e����N�X�C 
    graphics.ReleaseHdc(hdcSrc);

    // ����Ѹ˸m���e����N�X�C 
    bitmapGraphics.ReleaseHdc(hdcDest);

    // ����Graphics����ҨϥΪ��Ҧ��귽 
    graphics.Dispose();

    // ����Graphics����ҨϥΪ��Ҧ��귽 
    bitmapGraphics.Dispose();

    /******************/
    /* ø�s������� */
    /******************/

    // �]�w�ƹ���Ь��b�����
    System.Windows.Forms.Cursor cursor = System.Windows.Forms.Cursors.Arrow;

    // �]�w�x�Υ��W���� X �y��
    int x = System.Windows.Forms.Cursor.Position.X - 10;
    // �]�w�x�Υ��W���� Y �y��
    int y = System.Windows.Forms.Cursor.Position.Y - 10;
    // �]�w�x�Ϊ��e��
    int width = cursor.Size.Width;
    // �]�w�x�Ϊ�����
    int height = cursor.Size.Height;

    // �q���w��Image�إ߷sGraphics����
    System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(bitmap);

    // �إ߷sRectangle����
    System.Drawing.Rectangle targetRect = new Rectangle(x, y, width, height);

    // �b���w���d��ø�s�������
    cursor.Draw(g, targetRect);

    /*****************************/
    /* �x�s�v���ܰO�����Ƭy */
    /*****************************/

    // �إ߰O���骺��Ƭy
    System.IO.MemoryStream memStream = new System.IO.MemoryStream();

    // ���w�x�s���v���榡��JPEG�榡
    System.Drawing.Imaging.ImageFormat format = System.Drawing.Imaging.ImageFormat.Jpeg;

    // �N�v���H���w�榡�x�s�ܰO�����Ƭy
    bitmap.Save(memStream, format);

    // �^�ǰO�����Ƭy���줸�հ}�C
    return memStream.GetBuffer();
  }
}
