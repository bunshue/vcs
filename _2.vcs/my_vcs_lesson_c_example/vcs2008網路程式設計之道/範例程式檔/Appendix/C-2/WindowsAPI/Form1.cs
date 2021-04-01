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

    private void btnShow_Click(object sender, EventArgs e)
    {
      int iResult = Test.MessageBox(0, txtMsg.Text, txtCaption.Text, Test.MB_OKCANCEL | Test.MB_ICONINFORMATION);
    }
  }
}