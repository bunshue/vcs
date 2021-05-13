using System;
using System.Runtime.InteropServices;

namespace vcs_MessageBox2
{
  class Test
  {
    // «Øºc¨ç¦¡
    public Test()
    {
    }

    public const int MB_OKCANCEL = 1;
    public const int MB_ICONINFORMATION = 64;

    [DllImport("user32.dll")]
    public static extern int MessageBox(int hWnd, string lpText, string lpCaption, uint wType);
  }
}
