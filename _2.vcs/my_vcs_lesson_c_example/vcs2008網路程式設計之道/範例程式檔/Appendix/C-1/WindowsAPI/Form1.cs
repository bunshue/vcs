using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace WindowsAPI
{
  public partial class Form1 : Form
  {
    public Form1()
    {
      InitializeComponent();
    }

    public const int MB_OKCANCEL = 1;
    public const int MB_ICONINFORMATION = 64;

    [DllImport("user32.dll")]
    public static extern int MessageBox(int hWnd, string lpText, string lpCaption, uint wType);

    private void btnShow_Click(object sender, EventArgs e)
    {
      int iResult = MessageBox(0, txtMsg.Text, txtCaption.Text, MB_OKCANCEL | MB_ICONINFORMATION);
    }
  }
}